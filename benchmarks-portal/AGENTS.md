# DROIX Benchmarks Portal

This folder is a self-contained local app for importing, maintaining, and comparing DROIX product benchmark data. It is intentionally isolated so it can later move into its own repository.

## Project Shape

- Framework: Next.js + TypeScript.
- Database: SQLite at `data/benchmarks.sqlite` by default.
- Workbook import source: `../raw/benchmarks/Products Benchmarks Results.xlsx` by default.
- Wiki product import source: `../wiki/products` by default.
- All app code, scripts, schema, and docs should stay inside `benchmarks-portal/`.

## Commands

```bash
npm install
npm run import:wikidocs
npm run import:excel
npm run import:all
npm run test
npm run build
npm run dev -- --port 3001
```

Use environment variables when the project is moved:

```bash
BENCHMARKS_DB=/path/to/benchmarks.sqlite
BENCHMARKS_WORKBOOK=/path/to/Products\ Benchmarks\ Results.xlsx
WIKI_PRODUCTS_DIR=/path/to/wiki/products
```

## Data Rules

1. Do not edit the Excel workbook from this app. Treat it as immutable import/source material.
2. Do not edit parent wiki pages from this app unless the user explicitly asks for wiki maintenance.
3. After the initial import, the portal database is the source of truth for new benchmark entries.
4. Preserve raw Excel labels, sheet names, row numbers, cell addresses, hidden-row status, notes, and dates for auditability.
5. Do not silently force uncertain product mappings. Use `product_aliases.status = 'needs_review'`.
6. Benchmarks from hidden Excel rows must stay imported but hidden from default comparisons.
7. TDP may come from a column header, row notes, or model text. Store the source in `benchmark_results.tdp_source`.
8. eGPU rows should preserve host product, eGPU product, connection type, and internal/external display context when parseable.

## Import Expectations

The real workbook currently imports as:

- 19 sheets
- 424 benchmark row entries
- 5 hidden rows in `eGPU benchmarks`
- GPD WIN 5 Max+ 395 maps to `gpd-win-5-max-395`
- GPD WIN 5 Max 385 maps to `gpd-win-5-max-385`
- 2026 Windows handheld gaming results include parsed TDP values: 4W, 15W, 28W, 55W, 75W

If these numbers change because the workbook changes, update the tests deliberately.

## UI Rules

- Keep the app practical and data-dense. This is an internal benchmark maintenance tool, not a marketing site.
- Prefer tables, filters, segmented controls, checkboxes, and clear status pills.
- Product detail pages should always show source context: sheet, row, notes, TDP, connection/display context, and source cell.
- Comparison views should exclude disabled metrics and hidden source rows by default.
- Alias review should make it easy to approve/correct raw labels without losing the original label.

## Engineering Rules

- Keep changes scoped to this folder unless asked otherwise.
- Match the existing simple TypeScript/SQL style before adding abstractions.
- Prefer straightforward SQL queries over introducing an ORM.
- Add or update import tests when changing parsing, mapping, or schema behavior.
- Run `npm run test` and `npm run build` before handing off changes.
