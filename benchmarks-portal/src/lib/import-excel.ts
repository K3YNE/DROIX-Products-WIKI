import ExcelJS from "exceljs";
import { getDb } from "./db";
import {
  normalizeLabel,
  parseConnectionType,
  parseDisplayMode,
  parseResolution,
  parseTdpTokens,
  searchableLabel,
  slugify
} from "./normalize";
import { workbookPath } from "./paths";

type Header = {
  column: number;
  key: string;
  group: string;
  metric: string;
  displayName: string;
  unit: string | null;
  resolution: string | null;
  tdpWatts: number | null;
};

type ProductCandidate = {
  id: number;
  title: string;
  slug: string;
  search: string;
};

function cellText(value: ExcelJS.CellValue | undefined) {
  if (value === null || value === undefined) return "";
  if (value instanceof Date) return value.toISOString().slice(0, 10);
  if (typeof value === "object") {
    if ("text" in value && value.text) return String(value.text);
    if ("richText" in value && Array.isArray(value.richText)) {
      return value.richText.map((part) => part.text).join("");
    }
    if ("result" in value) return cellText(value.result as ExcelJS.CellValue);
  }
  return String(value).replace(/\n/g, " ").trim();
}

function modelColumnHeader(worksheet: ExcelJS.Worksheet) {
  return cellText(worksheet.getCell(2, 1).value).toLowerCase();
}

function hasTwoHeaderRows(worksheet: ExcelJS.Worksheet) {
  const header = modelColumnHeader(worksheet);
  return header.includes("model") || header.includes("product");
}

function headerValue(worksheet: ExcelJS.Worksheet, row: number, column: number) {
  return cellText(worksheet.getCell(row, column).value);
}

function inferUnit(group: string, metric: string) {
  const text = `${group} ${metric}`.toUpperCase();
  if (text.includes("BATTERY")) return "time";
  if (text.includes("FAN") || text.includes("DB")) return "dB";
  if (text.includes("TEMPERATURE") || text.includes("°C")) return "°C";
  if (text.includes("READ") || text.includes("WRITE") || text.includes("MBPS")) return "MB/s";
  if (/(FORZA|SHADOW|TOMB|CYBERPUNK|STREET FIGHTER|CALL OF DUTY|SOTTR)/.test(text)) return "fps";
  return "score";
}

function makeHeaders(worksheet: ExcelJS.Worksheet) {
  const twoRows = hasTwoHeaderRows(worksheet);
  const headers: Header[] = [];
  for (let column = 1; column <= worksheet.columnCount; column += 1) {
    const group = twoRows ? headerValue(worksheet, 1, column) : "";
    const metric = twoRows ? headerValue(worksheet, 2, column) : headerValue(worksheet, 1, column);
    const displayName = [group, metric].filter(Boolean).join(" / ").trim();
    if (!displayName) continue;
    const normalized = displayName.toUpperCase().replace(/\s+/g, " ");
    headers.push({
      column,
      key: slugify(normalized),
      group: group || "General",
      metric,
      displayName,
      unit: inferUnit(group, metric),
      resolution: parseResolution(displayName),
      tdpWatts: parseTdpTokens(displayName)[0] ?? null
    });
  }
  return headers;
}

function valueParts(value: ExcelJS.CellValue | undefined) {
  if (value === null || value === undefined || value === "") return null;
  if (value instanceof Date) {
    const hours = String(value.getUTCHours()).padStart(2, "0");
    const minutes = String(value.getUTCMinutes()).padStart(2, "0");
    const seconds = String(value.getUTCSeconds()).padStart(2, "0");
    return { numeric: null, text: seconds === "00" ? `${hours}:${minutes}` : `${hours}:${minutes}:${seconds}` };
  }
  if (typeof value === "number") return { numeric: value, text: String(value) };
  if (typeof value === "string") {
    const trimmed = value.trim();
    const numeric = Number(trimmed.replace(/,/g, ""));
    return { numeric: Number.isFinite(numeric) && trimmed !== "" ? numeric : null, text: trimmed };
  }
  return { numeric: null, text: cellText(value) };
}

function loadProducts(): ProductCandidate[] {
  return getDb()
    .prepare("SELECT id, title, slug FROM products")
    .all()
    .map((product) => {
      const p = product as { id: number; title: string; slug: string };
      return { ...p, search: searchableLabel(p.title) };
    });
}

function findProduct(rawLabel: string, products: ProductCandidate[]) {
  const database = getDb();
  const existing = database
    .prepare(
      "SELECT product_id, confidence, status FROM product_aliases WHERE raw_label = ? AND product_id IS NOT NULL"
    )
    .get(rawLabel) as { product_id: number; confidence: number; status: string } | undefined;
  if (existing) return { id: existing.product_id, confidence: existing.confidence, status: existing.status };

  const search = searchableLabel(rawLabel);
  let best: ProductCandidate | null = null;
  let bestScore = 0;
  for (const product of products) {
    if (!product.search) continue;
    let score = 0;
    if (search === product.search) score = 1;
    else if (search.includes(product.search)) score = Math.min(0.95, product.search.length / search.length);
    else if (product.search.includes(search)) score = Math.min(0.8, search.length / product.search.length);
    if (score > bestScore) {
      best = product;
      bestScore = score;
    }
  }
  if (best && bestScore >= 0.62) return { id: best.id, confidence: bestScore, status: bestScore >= 0.86 ? "approved" : "needs_review" };
  return null;
}

function ensureBenchOnlyProduct(rawLabel: string) {
  const database = getDb();
  const slugBase = `bench-${slugify(searchableLabel(rawLabel) || rawLabel)}`;
  let slug = slugBase;
  let index = 2;
  while (database.prepare("SELECT id FROM products WHERE slug = ?").get(slug)) {
    slug = `${slugBase}-${index}`;
    index += 1;
  }
  const result = database
    .prepare(
      "INSERT INTO products (slug, title, type, source, needs_review) VALUES (?, ?, 'bench_only', 'excel', 1)"
    )
    .run(slug, normalizeLabel(rawLabel));
  return Number(result.lastInsertRowid);
}

function upsertAlias(rawLabel: string, productId: number | null, confidence: number, status: string, notes: string | null) {
  getDb()
    .prepare(
      `INSERT INTO product_aliases (raw_label, normalized_label, product_id, confidence, status, notes, updated_at)
       VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
       ON CONFLICT(raw_label) DO UPDATE SET
         normalized_label = excluded.normalized_label,
         product_id = COALESCE(product_aliases.product_id, excluded.product_id),
         confidence = CASE WHEN product_aliases.status = 'approved' THEN product_aliases.confidence ELSE excluded.confidence END,
         status = CASE WHEN product_aliases.status = 'approved' THEN product_aliases.status ELSE excluded.status END,
         notes = COALESCE(product_aliases.notes, excluded.notes),
         updated_at = CURRENT_TIMESTAMP`
    )
    .run(rawLabel, searchableLabel(rawLabel), productId, confidence, status, notes);
}

function ensureDefinition(header: Header) {
  const database = getDb();
  const existing = database.prepare("SELECT id FROM benchmark_definitions WHERE key = ?").get(header.key) as
    | { id: number }
    | undefined;
  if (existing) return existing.id;
  const result = database
    .prepare(
      `INSERT INTO benchmark_definitions (key, group_name, metric_name, display_name, unit, higher_is_better, enabled)
       VALUES (?, ?, ?, ?, ?, ?, 1)`
    )
    .run(
      header.key,
      header.group,
      header.metric,
      header.displayName,
      header.unit,
      header.unit === "dB" || header.unit === "°C" ? 0 : 1
    );
  return Number(result.lastInsertRowid);
}

function sourceDate(value: ExcelJS.CellValue | undefined) {
  if (value instanceof Date) return value.toISOString().slice(0, 10);
  const text = cellText(value);
  return text || null;
}

function parseEgpuProductId(rawModel: string, products: ProductCandidate[]) {
  const upper = rawModel.toUpperCase();
  const known = [
    ["GPD G1", "GPD G1"],
    ["ONEXGPU", "ONEXGPU"],
    ["AG01", "AYANEO AG01"]
  ];
  for (const [needle, label] of known) {
    if (upper.includes(needle)) {
      const match = findProduct(label, products);
      if (match) return match.id;
      return ensureBenchOnlyProduct(label);
    }
  }
  return null;
}

function warning(batchId: number, sheet: string, row: number | null, cell: string | null, message: string) {
  getDb()
    .prepare(
      "INSERT INTO import_warnings (import_batch_id, sheet_name, source_row, source_cell, message) VALUES (?, ?, ?, ?, ?)"
    )
    .run(batchId, sheet, row, cell, message);
}

export async function importExcel(file = workbookPath()) {
  const database = getDb();
  const workbook = new ExcelJS.Workbook();
  await workbook.xlsx.readFile(file);

  const oldBatches = database
    .prepare("SELECT id FROM import_batches WHERE source_type = 'excel'")
    .all() as Array<{ id: number }>;
  for (const batch of oldBatches) {
    database.prepare("DELETE FROM benchmark_runs WHERE import_batch_id = ?").run(batch.id);
    database.prepare("DELETE FROM import_warnings WHERE import_batch_id = ?").run(batch.id);
  }
  database.prepare("DELETE FROM import_batches WHERE source_type = 'excel'").run();

  const batchResult = database
    .prepare("INSERT INTO import_batches (source_type, source_path) VALUES ('excel', ?)")
    .run(file);
  const batchId = Number(batchResult.lastInsertRowid);

  let products = loadProducts();
  let rowCount = 0;
  let resultCount = 0;

  const insertRun = database.prepare(`
    INSERT INTO benchmark_runs (
      import_batch_id, product_id, raw_model, normalized_model, sheet_name, source_row, source_hidden,
      tested_on, notes, row_tdp_watts, egpu_product_id, connection_type, display_mode
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `);
  const insertResult = database.prepare(`
    INSERT INTO benchmark_results (
      run_id, definition_id, value_numeric, value_text, unit, resolution, tdp_watts, tdp_source, source_cell
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
  `);

  for (const worksheet of workbook.worksheets) {
    const twoHeaderRows = hasTwoHeaderRows(worksheet);
    const dataStart = twoHeaderRows ? 3 : 2;
    const firstMetricColumn = twoHeaderRows
      ? headerValue(worksheet, 2, 3).toLowerCase() === "date"
        ? 4
        : 3
      : 2;
    const headers = makeHeaders(worksheet).filter((header) => header.column >= firstMetricColumn);

    for (let rowNumber = dataStart; rowNumber <= worksheet.rowCount; rowNumber += 1) {
      const excelRow = worksheet.getRow(rowNumber);
      const rawModel = normalizeLabel(cellText(excelRow.getCell(1).value));
      if (!rawModel) continue;
      const notes = twoHeaderRows ? cellText(excelRow.getCell(2).value) : "";
      const dateValue = twoHeaderRows && headerValue(worksheet, 2, 3).toLowerCase() === "date" ? excelRow.getCell(3).value : null;
      const rowTdps = parseTdpTokens(`${rawModel} ${notes}`);
      const match = findProduct(rawModel, products);
      let productId = match?.id ?? null;
      if (!productId) {
        productId = ensureBenchOnlyProduct(rawModel);
        products = loadProducts();
        upsertAlias(rawModel, productId, 0, "needs_review", "No confident wiki match; bench-only product created");
      } else {
        upsertAlias(rawModel, productId, match?.confidence ?? 0.75, match?.status ?? "needs_review", null);
      }

      const runResult = insertRun.run(
        batchId,
        productId,
        rawModel,
        searchableLabel(rawModel),
        worksheet.name,
        rowNumber,
        excelRow.hidden ? 1 : 0,
        sourceDate(dateValue),
        notes || null,
        rowTdps.length ? rowTdps.join(",") : null,
        parseEgpuProductId(rawModel, products),
        parseConnectionType(`${rawModel} ${notes}`),
        parseDisplayMode(`${rawModel} ${notes}`)
      );
      const runId = Number(runResult.lastInsertRowid);
      rowCount += 1;

      for (const header of headers) {
        const cell = excelRow.getCell(header.column);
        const parts = valueParts(cell.value);
        if (!parts) continue;
        const definitionId = ensureDefinition(header);
        const tdpSource = header.tdpWatts ? "header" : rowTdps.length === 1 ? "row_context" : null;
        const tdpWatts = header.tdpWatts ?? (rowTdps.length === 1 ? rowTdps[0] : null);
        if (header.unit === "time" && parts.numeric !== null && !String(cell.numFmt ?? "").toLowerCase().includes("h")) {
          warning(batchId, worksheet.name, rowNumber, cell.address, "Battery/time value is numeric with no time format; preserved as entered.");
        }
        insertResult.run(
          runId,
          definitionId,
          parts.numeric,
          parts.text,
          header.unit,
          header.resolution,
          tdpWatts,
          tdpSource,
          cell.address
        );
        resultCount += 1;
      }
    }
  }

  database
    .prepare("UPDATE import_batches SET completed_at = CURRENT_TIMESTAMP, row_count = ?, result_count = ? WHERE id = ?")
    .run(rowCount, resultCount, batchId);

  return { batchId, sheets: workbook.worksheets.length, rows: rowCount, results: resultCount, file };
}
