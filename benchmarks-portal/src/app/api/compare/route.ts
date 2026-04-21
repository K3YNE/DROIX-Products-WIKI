import { NextResponse } from "next/server";
import { rows } from "@/lib/db";

export const runtime = "nodejs";

export function GET(request: Request) {
  const url = new URL(request.url);
  const ids = (url.searchParams.get("products") ?? "")
    .split(",")
    .map((id) => Number(id))
    .filter(Boolean);
  const includeHidden = url.searchParams.get("hidden") === "1";
  const metric = url.searchParams.get("metric");
  if (!ids.length) return NextResponse.json([]);
  const placeholders = ids.map(() => "?").join(",");
  const params: unknown[] = [...ids];
  const filters = [`p.id IN (${placeholders})`, "bd.enabled = 1"];
  if (!includeHidden) filters.push("r.source_hidden = 0");
  if (metric) {
    filters.push("bd.key = ?");
    params.push(metric);
  }
  const data = rows(
    `SELECT p.id AS product_id, p.title AS product_title, p.slug,
      r.id AS run_id, r.sheet_name, r.source_row, r.tested_on, r.notes, r.source_hidden,
      bd.key AS metric_key, bd.display_name, bd.unit AS definition_unit,
      br.value_numeric, br.value_text, br.unit, br.resolution, br.tdp_watts, br.tdp_source
     FROM benchmark_results br
     JOIN benchmark_runs r ON r.id = br.run_id
     JOIN products p ON p.id = r.product_id
     JOIN benchmark_definitions bd ON bd.id = br.definition_id
     WHERE ${filters.join(" AND ")}
     ORDER BY bd.group_name, bd.display_name, br.tdp_watts, p.title`,
    params
  );
  return NextResponse.json(data);
}
