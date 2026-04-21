# Raw Ingest Manifest

**Fetched:** 2026-04-21 23:33

## Counts

| Source | Type | Count |
|--------|------|-------|
| gpdstore.net | Reviews | 17 |
| gpdstore.net | KB articles | 78 |
| gpdstore.net | Shop products | 121 |
| droix.net | KB articles | 313 |
| droix.net | KB skipped (GPD dupes) | 33 |
| droix.net | Reviews | 220 |
| droix.net | Shop products | 265 |
| droix.net | Shop skipped (GPD dupes) | 159 |

## Deduplication Rules

- gpdstore.net is fetched first and takes priority for all GPD content.
- droix.net KB: articles skipped if normalised title matches a gpdstore KB article.
- droix.net shop: products skipped if URL slug starts with `gpd-` or matches gpdstore product.

## Errors

- gpdstore product page https://gpdstore.net/product/gpd-win-max-2-2025-4g-lte-add-on: 404 Client Error: Not Found for url: https://gpdstore.net/product/gpd-win-max-2-2025-4g-lte-add-on
- gpdstore product page https://gpdstore.net/product/gpd-win-mini-case-2025: 404 Client Error: Not Found for url: https://gpdstore.net/product/gpd-win-mini-case-2025
- gpdstore product page https://gpdstore.net/product/gpd-win-mini-grips-2025: 404 Client Error: Not Found for url: https://gpdstore.net/product/gpd-win-mini-grips-2025
