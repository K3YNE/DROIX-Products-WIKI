# DROIX Benchmarks Portal

Self-contained local portal for importing and maintaining DROIX benchmark data.

## Quick Start

```bash
npm install
npm run import:all
npm run dev
```

Default paths are relative to this folder:

- Wiki product pages: `../wiki/products`
- Benchmark workbook: `../raw/benchmarks/Products Benchmarks Results.xlsx`
- SQLite database: `data/benchmarks.sqlite`

Override them with:

```bash
WIKI_PRODUCTS_DIR=/path/to/wiki/products \
BENCHMARKS_WORKBOOK=/path/to/Products\ Benchmarks\ Results.xlsx \
BENCHMARKS_DB=/path/to/benchmarks.sqlite \
npm run import:all
```

The Excel workbook is treated as immutable seed/source material. New benchmark entries should be added in the portal database.
