# Activity Log

## [2026-04-22] ingest | Product-page batch: AYANEO Pocket S2, DS, and VERT
- Created: [[ayaneo-pocket-s2-product-page]], [[ayaneo-pocket-s2-bag-product-page]], [[ayaneo-pocket-ds-product-page]], [[ayaneo-pocket-ds-bag-product-page]], [[ayaneo-pocket-vert-product-page]], [[qualcomm-snapdragon-8-plus-gen-1]]
- Updated: [[ayaneo-pocket-s2]], [[ayaneo-pocket-ds]], [[ayaneo-pocket-vert]], [[ayaneo]], [[android-handheld]], [[qualcomm]], [[qualcomm-snapdragon-g3-gen-3]], [[qualcomm-snapdragon-g3x-gen-2]], [[android-handheld-gaming]], [[index]], [[ingest-ledger]]
- Archived: `raw/ingest/product/droix-shop/ayaneo-pocket-s2.md`, `raw/ingest/product/droix-shop/ayaneo-pocket-s2-bag.md`, `raw/ingest/product/droix-shop/ayaneo-pocket-ds.md`, `raw/ingest/product/droix-shop/ayaneo-pocket-ds-bag.md`, `raw/ingest/product/droix-shop/ayaneo-pocket-vert.md`
- Notes: Attached simple bags to their parent product hubs. Flagged S2 display-size ambiguity, DS display-stack ambiguity, and VERT LCD/LTPS wording conflict on the source/product pages.

## [2026-04-22] ingest | Product-page batch: RG Slide and Pocket ACE
- Created: [[anbernic-rg-slide-product-page]], [[ayaneo-pocket-ace-product-page]], [[ayaneo-pocket-ace-case-product-page]], [[ayaneo-pocket-ace-grips-product-page]], [[qualcomm-snapdragon-g3x-gen-2]]
- Updated: [[anbernic-rg-slide]], [[ayaneo-pocket-ace]], [[anbernic]], [[ayaneo]], [[android-handheld]], [[qualcomm]], [[qualcomm-snapdragon-8-gen-2]], [[index]], [[ingest-ledger]]
- Archived: `raw/ingest/product/droix-shop/anbernic-rg-slide.md`, `raw/ingest/product/droix-shop/ayaneo-pocket-ace.md`, `raw/ingest/product/droix-shop/ayaneo-pocket-ace-case.md`, `raw/ingest/product/droix-shop/ayaneo-pocket-ace-grips.md`
- Notes: Attached accessory pages to [[ayaneo-pocket-ace]] rather than creating standalone hubs. Corrected the [[ayaneo-pocket-ace]] chipset from the older wiki's [[qualcomm-snapdragon-8-gen-2]] attachment to [[qualcomm-snapdragon-g3x-gen-2]], supported by both the existing review and the new product page. Flagged source-level display/spec contradictions on the affected source pages.

## [2026-04-21] ingest-prep | Full corpus queue and tooling
- Created: [[mini-pc]], [[ingest-ledger]]
- Updated: [[index]]
- Tooling: added `tools/wiki_ingest.py` for source scanning, canonical batch selection, classification validation, structural linting, ledger generation, and batch reporting.
- Notes: Scanner tracks 856 pending records: 828 staged ingest sources plus 28 archived GPD supplier-resource bundles. Open classification/onboarding issues are recorded in [[ingest-ledger]].

## [2026-04-21] restructure | Wiki schema v3 — navigation, technology brands, benchmarks, archive

**Schema (AGENTS.md):**
- New entity subtypes: `product-brand` (replaces `brand`), `technology-brand` (AMD, Qualcomm, Intel, Unisoc), `product-category` (Handheld PC, Android Handheld, UMPC, eGPU, Accessory)
- Richer brand page schema: Product Lineup table, Forthcoming/Announcements, Knowledge Base index, Resources index, Relationship with DROIX
- Technology-brand page schema: Chip Families table, DROIX Products table, Resources section
- New source subtype: `benchmark-dataset`
- Ingest-then-archive rule replaces raw/ immutability rule
- `raw:` frontmatter field removed from source pages; raw/ links prohibited in wiki
- Added `raw/ingest/{youtube,blog,kb,resources,benchmarks,product}/` drop-zone structure
- New `archive/` directory for post-ingestion storage
- Extraction depth rules by source subtype (kb = reproduce ALL, youtube = extract ALL benchmarks/specs)
- Auto-entity creation rule: create entity page for every chip/tech mentioned during ingest
- Rules 12–15 added: tech brands always current, category pages always current, sources are complete, website-ready

**New entity pages created:**
- Technology brands: [[amd]], [[qualcomm]], [[intel]], [[unisoc]]
- Chipsets: [[qualcomm-snapdragon-8-gen-2]], [[qualcomm-snapdragon-8-elite]], [[amd-ryzen-ai-9-hx-370]], [[intel-n250]], [[intel-n300]], [[unisoc-t820]], [[amd-rx-7600m-xt]]
- Product categories: [[handheld-pc]], [[android-handheld]], [[umpc]], [[egpu]], [[accessory]]

**Updated entity pages:**
- All 8 product-brand entities: subtype changed from `brand` to `product-brand`; added Product Lineup tables, Forthcoming/Announcements, Knowledge Base index, Resources index, Relationship with DROIX
- [[gpd]] and [[ayaneo]] fully expanded; [[ayn]], [[onexplayer]], [[anbernic]], [[konkr]], [[retroid]] expanded with placeholder KB/Resources/Announcements sections

**Index.md:**
- Rebuilt as brand-centric + category navigation hub
- Browse by Brand section (all product brands)
- Browse by Category section (5 category pages)
- Technology section (4 tech vendors + chipset listing)
- Products section: each product nested with variants, reviews, KB, resources

**Source pages:**
- Removed `raw:` frontmatter field from all 25 source pages
- Removed all `[Raw source](...)` body links from all 25 source pages

**Benchmark integration:**
- Created [[products-benchmarks-results]] (subtype: benchmark-dataset) with full data extraction from Products Benchmarks Results.xlsx
- Updated [[gpd-win-5-max-395]], [[gpd-win-5-max-385]], [[onexplayer-onexfly-apex-max-395]] with full TDP-scaled gaming benchmark tables
- Updated [[gpd-micropc-2-n250]], [[gpd-micropc-2-n300]] with synthetic benchmark tables
- Updated Android product hubs ([[anbernic-rg-slide]], [[ayaneo-pocket-ace]], [[ayaneo-pocket-s2]], [[ayaneo-pocket-ds]], [[ayaneo-pocket-vert]], [[konkr-pocket-fit]], [[ayn-odin-3]], [[ayn-thor]]) with AnTuTu, Geekbench, 3DMark data

**Archive migration:**
- Moved all 58 files from `raw/brands/`, `raw/supplier-resources/`, `raw/benchmarks/` to `archive/`
- `raw/` is now clean (ingest drop-zone structure only)
- Legacy empty folders removed: `raw/assets/`, `raw/blog-review/`, `raw/youtube-review/`, `raw/knowledge-base/`, `raw/product/`

## [2026-04-21] restructure | Wiki schema v2 — brand → product → variant → resources

- Rewrote [AGENTS.md](../AGENTS.md) as the single source of truth: DROIX spelling rule, directory layout, slug conventions, page-type catalog (brand / product / variant / source / entity / concept / analysis), onboarding + ingest + resource + lint workflows. Supersedes the pre-existing draft.
- **raw/ restructure** — collapsed the old `raw/assets/`, `raw/youtube-review/`, `raw/blog-review/`, `raw/knowledge-base/`, `raw/product/` folders into per-product trees under `raw/brands/<brand>/<product>/` with subfolders for `product/`, `reviews/{youtube,blog,external}/`, `knowledge-base/`, `resources/{firmware,bios,drivers,tools,manuals}/`, `images/`. 15 YouTube transcripts and 4 GPD WIN 5 first-party documents migrated. Legacy empty folders are flagged for manual deletion (sandbox cannot delete from the mounted workspace).
- **wiki/products/** — created 14 product hubs + 8 variant pages across GPD, AYANEO, ONEXPLAYER, AYN, Anbernic, KONKR. Hub + variant pattern adopted; reviews link variant-primary, hub-secondary.
- **wiki/sources/** — renamed the 15 existing review slugs to the new dated `YYYY-MM-DD-<brand>-<product>-<kind>` form (e.g. `gpd-win-5-review.md` → [[2025-10-23-gpd-win-5-review-youtube]]). All 16 pre-existing source pages migrated to the new frontmatter schema (subtype / brand / product / variant / raw / source_url). Seeded 6 GPD WIN 5 resource pages ([[gpd-win-5-firmware-win11-25h2]], [[gpd-win-5-firmware-win11-24h2]], [[gpd-win-5-bios-v2-25]], [[gpd-win-5-drivers-2025-10-30]], [[gpd-motionassistant-v1-2-0-9]], [[gpd-win-5-user-manual-2025-09-04]]) and 3 first-party content pages ([[gpd-win-5-product-page]], [[gpd-win-5-getting-started]], [[gpd-win-5-faq]]).
- **wiki/entities/** — rewrote all 7 brand entities to the new schema with `products: [...]` manifests, added new stub [[retroid]], and added 2 chipset entities [[amd-ryzen-ai-max]] and [[qualcomm-snapdragon-g3-gen-3]]. Fixed [[droix]] to always use the "DROIX" spelling.
- **wiki/concepts/** — 7 concept pages relinked to the new slug scheme (product hubs + dated source slugs), replaced incorrect DROIX-case wikilinks with `[[droix|DROIX]]`, and updated frontmatter `sources:` lists to the new dated slugs.
- **wiki/index.md** — rebuilt from scratch around the new structure (Brands / Products by brand / Sources by subtype / Entities / Concepts / Analysis).
- Notes: Schema migration only — no new data ingested. Next ingest should onboard the full product catalogue (Retroid line, additional GPD/AYANEO/ONEXPLAYER/AYN SKUs) and backfill resource pages for products beyond the WIN 5.

## [2026-04-21] ingest | GPD WIN 5 Review (GPD Store blog)
- Created: [[gpd-win-5-blog-review]]
- Updated: [[2025-10-23-gpd-win-5-review-youtube]] (added 85W TDP update, linked blog review), [[gpd]] (added WIN Mini 2025 and WIN MAX 2 2025, blog rating), [[egpu-docking]] (added GPD Store quote, 85W TDP note)
- Notes: First-party written review from gpdstore.net by Dave. Same device as DROIX video but adds 85W TDP launch update, 6 extra game benchmarks, idle battery life, BIWIN Mini SSD brand, and 4.9/5 rating.

## [2026-04-21] ingest | Batch ingest of 15 DROIX video transcripts
- Created: [[2025-05-23-ayaneo-pocket-ace-review-youtube]], [[2025-06-25-ayaneo-ag01-review-youtube]], [[2025-07-02-anbernic-rg-slide-review-youtube]], [[2025-07-18-ayaneo-pocket-s2-review-youtube]], [[2025-07-24-gpd-micropc-2-review-youtube]], [[2025-08-29-onexplayer-g1-review-youtube]], [[2025-10-23-gpd-win-5-review-youtube]], [[2025-11-07-ayaneo-flip-1s-ds-review-youtube]], [[2025-11-14-konkr-pocket-fit-review-youtube]], [[2025-11-20-gpd-win-5-smart-dock-review]], [[2025-11-21-ayaneo-pocket-ds-review-youtube]], [[2026-01-27-ayn-thor-review-youtube]], [[2026-03-04-onexplayer-onexfly-apex-review-youtube]], [[2026-03-13-ayn-odin-3-review-youtube]], [[2026-03-31-ayaneo-pocket-vert-review-youtube]]
- Created: [[droix]], [[ayaneo]], [[ayn]], [[gpd]], [[onexplayer]], [[anbernic]], [[konkr]]
- Created: [[android-handheld-gaming]], [[windows-handheld-gaming]], [[emulation-performance]], [[egpu-docking]], [[dual-screen-handhelds]], [[display-technology]], [[benchmark-methodology]]
- Notes: First batch ingest. 15 source pages, 7 entity pages, 7 concept pages created. Sources span 2025-05-23 to 2026-03-31. Covers Android handhelds (AYANEO, AYN, Anbernic, KONKR), Windows handhelds (GPD, ONEXPLAYER, AYANEO), eGPU (AG01), UMPC (MicroPC 2), and accessories (Win 5 dock).

## [2026-04-21] init | Wiki initialized
- Created: directory structure, CLAUDE.md schema, index.md, log.md
- Notes: wiki bootstrapped with empty structure, ready for first ingest
