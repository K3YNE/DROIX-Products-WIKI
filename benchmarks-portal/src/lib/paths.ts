import path from "node:path";

export const appRoot = process.cwd();

export function dbPath() {
  return process.env.BENCHMARKS_DB ?? path.join(appRoot, "data", "benchmarks.sqlite");
}

export function wikiProductsDir() {
  return process.env.WIKI_PRODUCTS_DIR ?? path.resolve(appRoot, "../wiki/products");
}

export function workbookPath() {
  return (
    process.env.BENCHMARKS_WORKBOOK ??
    path.resolve(appRoot, "../raw/benchmarks/Products Benchmarks Results.xlsx")
  );
}
