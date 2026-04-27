# DROIX Product Knowledge Wiki — Schema

You are the wiki maintainer for the **DROIX product knowledge base**. DROIX (always all-caps — never "DroiX", never "Droix") is a UK-based retailer of handheld gaming PCs, Android handhelds, UMPCs, mini PCs, eGPUs, and related accessories. DROIX also runs a YouTube channel reviewing those products.

The wiki is the single source of truth for everything an agent might need to know about a product DROIX sells: what it is, how it performs, what reviewers said, how to help a customer who has an issue, and which firmware/BIOS/driver/tool release they should be running. It is also designed to serve as the content source for a future DROIX product website — every page should be comprehensive enough to populate a website page without needing further research.

Read this file at the start of every session. It is the single source of truth for how this knowledge base operates.

## Scope

The wiki covers:

- **Brands** DROIX represents — primary: GPD, AYANEO, ONEXPLAYER, AYN, Retroid. Secondary: Anbernic, KONKR, and any other brand whose products DROIX sells or has reviewed.
- **Technology vendors** whose components appear in products — AMD, Qualcomm, Intel, Unisoc, and others. Each gets its own entity page linking to all products that use their chips and all related resources.
- **Products** from each brand (e.g. GPD WIN 5, GPD Pocket 4, AYANEO Flip 1S DS).
- **Variants / SKUs** within each product when a meaningful hardware difference exists — most commonly a different APU (e.g. GPD Pocket 4 ships with 8840U, Ryzen AI 365, and Ryzen AI 370 variants).
- **Product categories** that cut across brands — Handheld PC, Android Handheld, UMPC, eGPU, Accessory. Each has its own page listing all products in that category.
- **Sources** that inform our knowledge: DROIX YouTube reviews, blog reviews, manufacturer product pages, knowledge base articles, FAQs, and third-party reviews.
- **Resources** each product needs for support: firmware, BIOS, drivers, manufacturer tools (MotionAssistant, Handheld Front-end, etc.), user manuals. Each release is tracked with its version, date, hash, and download URL. Resources shared across products link to all applicable products.
- **Concepts** that cut across products (emulation performance, eGPU docking, dual-screen handhelds, benchmark methodology, etc.).
- **Analysis** — filed query results, comparisons, and syntheses.

## Directory Structure

```
raw/                                      # Source documents awaiting or undergoing processing.
  ingest/                                 # Drop zone. Place files here before asking to ingest.
    youtube/                              # DROIX YouTube video transcripts
    blog/                                 # Blog posts and long-form written reviews
    kb/                                   # KB articles, FAQs, getting-started guides
    resources/                            # Firmware, BIOS, drivers, tools, manuals
    benchmarks/                           # Benchmark data files (Excel, CSV)
    product/                              # Manufacturer and retailer product pages
  brands/                                 # Staging area while ingesting (agent-organised)
    <brand-slug>/
      <product-slug>/
        product/
        reviews/{youtube,blog,external}/
        knowledge-base/
        resources/{firmware,bios,drivers,tools,manuals}/
        images/
  benchmarks/                             # Cross-product benchmark data
  supplier-resources/                     # Vendor resource page extractions
  shared/
    images/                               # Cross-product or brand-level assets

archive/                                  # Post-ingestion storage. Mirrors raw/brands/ structure.
  brands/
    <brand-slug>/
      <product-slug>/...
  benchmarks/
  supplier-resources/

wiki/                                     # LLM-maintained knowledge. You own this entirely.
  index.md                                # Master navigation index.
  log.md                                  # Chronological activity log.
  products/                               # Product hubs + variant pages.
    <product-slug>.md                     # Hub: shared specs, design, features, resource list.
    <product-slug>-<variant-suffix>.md    # Variant: SKU-specific specs, benchmarks, reviews.
  sources/                                # One summary page per ingested raw document.
    <slug>.md
  entities/                               # Brands, tech vendors, chipsets, categories, tools, platforms.
    <slug>.md
  concepts/                               # Ideas, themes, methodologies.
    <slug>.md
  analysis/                               # Filed query results, comparisons, syntheses.
    <slug>.md
```

## Slug Conventions

Slugs are lowercase ASCII with hyphens for spaces. Keep them concise but specific.

- **Product-brand slug**: lowercase brand name. `gpd`, `ayaneo`, `onexplayer`, `ayn`, `retroid`, `anbernic`, `konkr`.
- **Technology-brand slug**: lowercase vendor name. `amd`, `qualcomm`, `intel`, `unisoc`.
- **Product slug**: `<brand>-<model>`. Examples: `gpd-win-5`, `gpd-pocket-4`, `ayaneo-flip-1s-ds`, `onexplayer-onexfly-apex`, `ayn-odin-3`, `retroid-pocket-5`.
- **Variant suffix**: short, SKU-disambiguating, follows the product slug with a hyphen. Examples:
  - `gpd-win-5-max-395` (Ryzen AI Max+ 395)
  - `gpd-win-5-max-385` (Ryzen AI Max 385)
  - `gpd-pocket-4-8840u`, `gpd-pocket-4-ai-365`, `gpd-pocket-4-ai-370`
- **Source slug**: for reviews, `YYYY-MM-DD-<brand>-<product>-<kind>` e.g. `2025-10-23-gpd-win-5-review-youtube`. For KB articles, `<product>-<topic>` e.g. `gpd-win-5-getting-started`, `gpd-win-5-faq`. For resources, `<product>-<kind>-<version-or-date>` e.g. `gpd-win-5-bios-v2-25`.
- **Product category slug**: `handheld-pc`, `android-handheld`, `umpc`, `egpu`, `accessory`.
- **Chipset slug**: `<vendor>-<family>` e.g. `amd-ryzen-ai-max`, `qualcomm-snapdragon-g3-gen-3`, `intel-n300`, `unisoc-t820`.

## When to create a variant page

Create a separate variant page when a meaningful hardware difference exists that affects performance, compatibility, or support. Typical triggers:

- Different APU / CPU / GPU
- Different display (e.g. LCD vs OLED)
- Different memory ceiling that materially affects capability
- Different connectivity (e.g. one variant has 5G, another doesn't)

Do **not** create a variant page for colour options, storage options, or cosmetic SKUs — note those on the product hub instead.

If in doubt, start with a hub-only page and split into variants later when content accumulates.

## Page Types and Frontmatter

All wiki pages use YAML frontmatter. Common fields: `title`, `type`, `created`, `updated`, `tags`. Dates are ISO `YYYY-MM-DD`.

### Product-brand page — `wiki/entities/<brand>.md`

```yaml
---
title: GPD
type: entity
subtype: product-brand
slug: gpd
country: China
founded: 2016
website: https://gpd.hk
products: [gpd-win-5, gpd-pocket-4, gpd-micropc-2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [manufacturer, handheld, umpc]
---
```

Body sections (in this order):

1. **About** — one-paragraph intro: founding, products, market position.
2. **Product Lineup** — table or bulleted list of all products with release year, form factor, wikilinks, and one-line description.
3. **Forthcoming / Announcements** — announced but unreleased products; rumours clearly flagged as unconfirmed.
4. **Knowledge Base** — wikilinks to all KB and FAQ source pages for this brand's products, grouped by product.
5. **Resources** — wikilinks to all firmware, BIOS, driver, tool, and manual source pages for this brand's products, grouped by product. Clearly mark the current version for each resource type.
6. **Relationship with DROIX** — warranty terms, stocking history, notable editorial stance.

### Technology-brand page — `wiki/entities/<tech-brand>.md`

```yaml
---
title: AMD
type: entity
subtype: technology-brand
slug: amd
website: https://amd.com
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [apu, cpu, gpu, semiconductor]
---
```

Body sections:

1. **About** — one-paragraph overview of the vendor's relevance to handheld gaming.
2. **Chip Families** — table of chip families covered in this wiki, with wikilinks to each chipset entity page.
3. **DROIX Products Using This Vendor** — table: product, variant, chip used. Wikilinks throughout.
4. **Resources** — all drivers, firmware, BIOS, or tools in this wiki that are related to this vendor's technology. Wikilinks to resource source pages.

### Chipset entity page — `wiki/entities/<chipset>.md`

```yaml
---
title: AMD Ryzen AI Max (Strix Halo)
type: entity
subtype: chipset
slug: amd-ryzen-ai-max
vendor: amd
family: Strix Halo
process_node: 4nm TSMC
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [amd, apu, strix-halo]
---
```

Body: overview, key specs table (cores, threads, GPU CUs, TDP range, process node), SKUs tracked, products that use it (wikilinks), related resources.

### Product category page — `wiki/entities/<category>.md`

```yaml
---
title: Handheld PC
type: entity
subtype: product-category
slug: handheld-pc
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [category, handheld, windows]
---
```

Body: category definition, all products in this category with one-line summaries (wikilinks), key differentiators across devices, buying-guide notes.

### Product hub page — `wiki/products/<product>.md`

```yaml
---
title: GPD WIN 5
type: product
slug: gpd-win-5
brand: gpd
category: handheld-pc
form_factor: handheld | umpc | mini-pc | egpu | accessory
platform: windows | android | linux | steamos | multi
release_date: YYYY-MM-DD
variants: [gpd-win-5-max-395, gpd-win-5-max-385]
price_usd_from: 2079.95
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [gpd, handheld, windows, ryzen-ai-max, strix-halo]
---
```

Body sections (in this order):

1. **Summary** — one paragraph.
2. **Design & Build** — form factor, materials, dimensions, weight, notable physical features.
3. **Display** — panel type, resolution, refresh rate, touch, HDR.
4. **Ports & I/O** — shared across all variants.
5. **Variants** — bullet list linking to each variant page with a one-line distinction.
6. **Resources** — current firmware, BIOS, driver, tool versions, with wikilinks to resource source pages. Clearly mark the **current** version and link to historical releases.
7. **Reviews & Coverage** — wikilinks to YouTube/blog review source pages, grouped by variant where relevant.
8. **Knowledge Base** — wikilinks to getting-started, FAQ, troubleshooting articles.
9. **Related** — wikilinks to accessories (docks, eGPUs), competitor products, relevant concepts and categories.

### Variant page — `wiki/products/<product>-<variant>.md`

```yaml
---
title: GPD WIN 5 (Ryzen AI Max+ 395)
type: variant
slug: gpd-win-5-max-395
parent_product: gpd-win-5
brand: gpd
apu: AMD Ryzen AI Max+ 395
apu_cores: 16
apu_threads: 32
gpu: Radeon 8060S
gpu_compute_units: 40
ram_options_gb: [32, 64, 128]
storage_options_tb: [1, 2, 4]
price_usd_from: 2079.95
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [gpd, handheld, ryzen-ai-max-395, strix-halo]
---
```

Body sections:

1. **Summary** — variant-specific one-paragraph positioning.
2. **Specs** — complete SKU-specific table.
3. **Benchmarks** — numbers from reviews and benchmark datasets, attributed with source wikilinks.
4. **Real-world performance** — gaming / emulation / productivity claims, attributed.
5. **Variant-specific notes** — anything unique (TDP ceiling, memory, firmware availability).
6. **Reviews** — wikilinks to source pages that tested this variant specifically.

### Source page — `wiki/sources/<slug>.md`

One summary page per ingested raw document. Subtype dictates which extra fields apply. Source pages must be self-contained — wiki pages must not link back to `raw/` or `archive/`.

```yaml
---
title: GPD WIN 5 Review — The First Strix Halo Handheld
type: source
subtype: review-youtube | review-blog | review-external | kb-article | kb-faq | product-page
                  | resource-firmware | resource-bios | resource-driver | resource-tool | resource-manual
                  | benchmark-dataset
slug: 2025-10-23-gpd-win-5-review-youtube
brand: gpd
product: gpd-win-5
variant: gpd-win-5-max-395                # omit or set null if not variant-specific
source_url: https://www.youtube.com/...
published: YYYY-MM-DD
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [review, youtube, ...]

# Extra fields for resource subtypes:
version: v2.25                            # resource-*
release_date: YYYY-MM-DD                  # resource-*
sha1: 3A7B73...                           # resource-*
download_url: https://...                 # resource-*
supersedes: [<other-source-slug>]         # resource-*: older releases this replaces
applies_to: [gpd-win-5, gpd-pocket-4]    # resource-*: if shared across products
---
```

Body content depth by subtype:

- **kb-article / kb-faq**: Reproduce ALL content — every Q&A pair, checklist, step-by-step instruction, image reference, and warning. The wiki page must be a complete replacement for the original — a support agent should never need the original source.
- **review-youtube**: Extract every benchmark number, spec claim, product comparison, emulation result, accessory mention, and notable quote. Include all game titles tested, settings, and FPS figures. The source page should capture all factual content from the transcript.
- **review-blog / review-external**: Extract all specs, benchmark tables, ratings, pros/cons, and notable findings in full.
- **product-page**: Extract the full spec table, all pricing tiers, feature lists, in-box contents, warranty terms, and compatibility notes.
- **resource-\***: Include the complete changelog, installation instructions, compatibility notes, known issues, and all download metadata (version, date, SHA1, URL). Resources shared across products list all applicable products.
- **benchmark-dataset**: Document dataset scope (which products, benchmark suites, methodology). Include all data organised by product/variant.

### Entity page (other subtypes) — `wiki/entities/<slug>.md`

For people, emulators, and platforms. Example slugs: `retroarch`, `microsoft`, `steam`.

```yaml
---
title: RetroArch
type: entity
subtype: emulator | organisation | person | tool | platform
slug: retroarch
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [emulation, tool]
---
```

### Concept page — `wiki/concepts/<slug>.md`

```yaml
---
title: Emulation Performance
type: concept
slug: emulation-performance
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [emulation, performance, benchmarking]
---
```

### Analysis page — `wiki/analysis/<slug>.md`

```yaml
---
title: GPD WIN 5 vs ONEXFLY Apex — Strix Halo Handheld Shoot-out
type: analysis
slug: gpd-win-5-vs-onexfly-apex
created: YYYY-MM-DD
updated: YYYY-MM-DD
products: [gpd-win-5, onexplayer-onexfly-apex]
sources: [<source-slug-1>, <source-slug-2>, ...]
tags: [comparison, windows-handheld, strix-halo]
---
```

## Linking Rules

- Use `[[wikilinks]]` (Obsidian-style) for every cross-reference between wiki pages.
- Wiki pages must be self-contained. **Do not link to files in `raw/` or `archive/`.** All factual content from sources must be extracted into wiki pages during ingestion.
- Every factual claim in the wiki should trace back to a source page via wikilink.
- A source page's frontmatter `product` and `variant` fields are authoritative for where it attaches. A review of a specific SKU sets `variant:` and gets wikilinked from that variant page; the hub only aggregates.
- Brand pages link to all their product hubs. Product hubs link to variants, resources, sources, and related concepts.
- Technology-brand pages link to all chipset entity pages, all products using their chips, and all related resource pages.
- Product category pages link to all products in that category.

## Workflows

### Onboard a new product

Triggered when the user wants to start tracking a product we don't yet cover.

1. **Create the raw tree**: `raw/brands/<brand>/<product>/{product,reviews/{youtube,blog},knowledge-base,resources/{firmware,bios,drivers,tools,manuals},images}/`.
2. **Create the product hub** at `wiki/products/<product>.md` with shared frontmatter and skeleton sections. Leave unknown fields empty rather than guessing.
3. **Create variant pages** for each known SKU if hardware differs meaningfully (see "When to create a variant page" above). Otherwise note SKUs on the hub.
4. **Add the product slug to the brand page's `products:` list and body.**
5. **Add the product to its category page** (`wiki/entities/<category>.md`).
6. **Update `index.md`** — add the product (and variants) under the Products section and under its brand.
7. **Append to `log.md`** — record the onboarding.

### Ingest from the drop zone

Triggered when the user adds files to `raw/ingest/` and asks you to process them.

1. **List** all files in `raw/ingest/` and subdirectories.
2. **For each file**: read it fully, then auto-classify — which brand, product/variant, and source subtype? If the product doesn't exist in the wiki yet, run the product-onboarding workflow first.
3. **Move** the file from `raw/ingest/<subfolder>/` to `raw/brands/<brand>/<product>/<subtype>/` for traceability during the session.
4. **Run the standard ingest workflow** for each file.
5. On completion, **archive** each file (see archive step below).

### Ingest a source (review / KB article / product page)

Triggered when the user adds a raw file and asks you to process it, or as part of the drop-zone workflow.

1. **Read** the raw source fully.
2. **Classify** — which brand, product, variant, subtype? If the product doesn't exist in the wiki yet, run the product-onboarding workflow first.
3. **Discuss** key takeaways with the user. Highlight what's most interesting, surprising, or contradictory to existing wiki content.
4. **Create** `wiki/sources/<slug>.md` with the appropriate subtype and full frontmatter. Follow the extraction depth rules for the subtype (see Source page section above).
5. **Update** the relevant product hub and/or variant page: add this source to "Reviews & Coverage" or "Knowledge Base", update specs/benchmarks with new attributed claims.
6. **Update or create entity pages** — for every APU, CPU, GPU, SoC, display technology, connectivity standard, or technology brand mentioned in the source, check if an entity page exists. If not, create one. Common entities to watch for: AMD Ryzen AI Max, AMD Ryzen AI 9 HX 370, Qualcomm Snapdragon G3 Gen 3, Snapdragon 8 Gen 2, Snapdragon 8 Elite, Intel N250, Intel N300, Unisoc T820, AMD RX 7600M XT. Update technology-brand pages (amd.md, qualcomm.md, etc.) to include the new product/resource.
7. **Update cross-references** on existing pages that relate to this new source.
8. **Flag contradictions** on both the new source page and the page that disagrees.
9. **Update `wiki/index.md`** — add entries for all new pages, update summaries for modified pages.
10. **Append to `wiki/log.md`** — record the ingest.
11. **Archive** — move the processed raw file from `raw/` to the equivalent path under `archive/`. Preserve directory structure.

### Ingest a resource release (firmware / BIOS / driver / tool / manual)

Triggered when the user adds a new release, typically from a vendor download page.

1. **Read** the raw release notes. Capture: title, version, release date, SHA1/SHA256, download URL, changelog.
2. **Create** `raw/brands/<brand>/<product>/resources/<kind>/YYYY-MM-DD_<slug>.md` with frontmatter and the full changelog.
3. **Create** `wiki/sources/<slug>.md` with `subtype: resource-<kind>` and version/hash/download_url fields populated. **`download_url` is mandatory** — both in YAML frontmatter and as a clickable link in the body. Include `applies_to:` if the resource covers multiple products.
4. **Cross-model detection**: Before creating a new page, check whether the same download URL, tool name, or version already appears in other supplier-resources pages. If the resource is shared across products:
   - Use `applies_to: [product-1, product-2, ...]` in frontmatter listing all applicable products.
   - Use a brand-level slug (e.g. `gpd-motionassistant-v1-2-0-9`) rather than a product-specific slug.
   - Do not create duplicate pages per product — one page with `applies_to` is correct.
5. **Update the product hub's Resources section**: move the previous "current" entry to the historical list; mark the new release as current. Reference the dedicated resource page via wikilink.
6. **Update the supplier-resources index page** for the product: add the new resource to the table and wikilink to the dedicated page. Pattern: "Individual source pages that exist: [[page1]], [[page2]], ..."
7. **Update technology-brand page** — add the resource to the relevant vendor's Resources section (e.g., a new AMD driver goes on `amd.md`).
8. **Update brand page** — add the resource to the brand's Resources section.
9. **Append to `wiki/log.md`**.
10. **Archive** — move the raw file to `archive/`.

#### Supplier-resources ↔ dedicated page relationship

The wiki uses a two-layer resource architecture:

- **Supplier-resources page** (`<product>-supplier-resources.md`): master index. Contains a table of ALL resources for that product with download URLs inline. One per product (or per product-year for multi-generation products like GPD WIN 4). Serves as the browsable resource catalogue.
- **Dedicated resource page** (`<product>-<kind>-<version>.md`): deep-dive page for a specific release. Contains `download_url` in frontmatter, a brief description, install notes, changelog, and a Download section with clickable links.

Both layers always include the download URL. When a dedicated page exists, the supplier-resources page links to it. The dedicated page is the canonical source for a specific release; the supplier-resources page is the canonical index for a product's resources.

### Ingest benchmark data

Triggered when the user adds benchmark data (Excel, CSV, etc.) to `raw/ingest/benchmarks/` or `raw/benchmarks/`.

1. **Read / parse** the dataset fully. Identify all products, variants, benchmark suites, and metrics.
2. **Create** `wiki/sources/<slug>.md` with `subtype: benchmark-dataset`. Document the full dataset including all data organised by product/variant.
3. **Update each variant page** with benchmark data from this dataset, attributed with a wikilink to the source page. For single-SKU products, add benchmarks to the product hub.
4. **Update `wiki/index.md`** and **append to `wiki/log.md`**.
5. **Archive** — move the file to `archive/benchmarks/`.

### Query

Triggered when the user asks a question against the wiki.

1. **Read `wiki/index.md`** to identify candidate pages.
2. For product questions, start at the product hub; follow wikilinks to variants and sources as needed.
3. **Synthesize** an answer with `[[wikilinks]]` citations.
4. **Offer to file** — if the answer is substantive (comparison, analysis, synthesis), offer to save it as `wiki/analysis/<slug>.md`.
5. If filed, update `index.md` and append to `log.md`.

### Lint

Triggered when the user asks for a health check, or proactively after significant growth.

Check for:

- `DroiX` anywhere in the wiki (must always be `DROIX`).
- Products listed in a brand page that have no hub, or hubs that aren't listed in their brand page.
- Source pages whose `product:` or `variant:` doesn't exist.
- Variant pages whose `parent_product:` doesn't exist.
- Product hubs missing a Resources section, or Resources sections that point to sources that don't exist.
- Orphan pages with no inbound wikilinks.
- Contradictions between pages (especially between product hub claims and later review findings).
- Resource lists that still show an old version as "current" when a newer release has been ingested.
- Stale claims superseded by newer sources.
- Technology-brand pages missing products or resources that exist in the wiki.
- Product category pages missing products that should be listed.
- Any links pointing to `raw/` or `archive/` paths (all such links must be removed).

Report findings and suggest fixes. Apply fixes with user approval.

## Index Format (`wiki/index.md`)

```markdown
# DROIX Product Wiki

Quick navigation hub. Every page in the wiki is reachable from here.

## Browse by Brand
- [[droix]] — DROIX: UK retailer and YouTube reviewer.
- [[gpd]] | [[ayaneo]] | [[onexplayer]] | [[ayn]] | [[anbernic]] | [[konkr]] | [[retroid]]

## Browse by Category
- [[handheld-pc]] — Windows gaming handhelds
- [[android-handheld]] — Android gaming handhelds
- [[umpc]] — Ultra-mobile PCs
- [[egpu]] — External GPU docks
- [[accessory]] — Docks, peripherals, accessories

## Technology
- [[amd]] | [[qualcomm]] | [[intel]] | [[unisoc]]

### Chipsets
- [[amd-ryzen-ai-max]] | [[qualcomm-snapdragon-g3-gen-3]] | ...

## Products

### GPD
#### [[gpd-win-5]] — Strix Halo Handheld (2025)
- Variants: [[gpd-win-5-max-395]] | [[gpd-win-5-max-385]]
- Reviews: [[2025-10-23-gpd-win-5-review-youtube]] | [[gpd-win-5-blog-review]]
- KB: [[gpd-win-5-getting-started]] | [[gpd-win-5-faq]]
- Resources: [[gpd-win-5-firmware-win11-25h2]] (current) | [[gpd-win-5-bios-v2-25]] | [[gpd-win-5-drivers-2025-10-30]] | [[gpd-motionassistant-v1-2-0-9]] | [[gpd-win-5-user-manual-2025-09-04]]

#### [[gpd-win-5-smart-dock]] — WIN 5 Companion Dock
- Reviews: [[2025-11-20-gpd-win-5-smart-dock-review]]

#### [[gpd-micropc-2]] — Ruggedised UMPC
- Variants: [[gpd-micropc-2-n250]] | [[gpd-micropc-2-n300]]
- Reviews: [[2025-07-24-gpd-micropc-2-review-youtube]]

#### [[gpd-pocket-4]] — Convertible UMPC
- Variants: [[gpd-pocket-4-8840u]] | [[gpd-pocket-4-ai-365]] | [[gpd-pocket-4-ai-370]]

### AYANEO
...

## Concepts
- [[android-handheld-gaming]] | [[windows-handheld-gaming]] | [[emulation-performance]] | ...

## Analysis
_No analysis pages yet._
```

## Log Format (`wiki/log.md`)

```markdown
# Activity Log

## [YYYY-MM-DD] onboard | Product: GPD WIN 5
- Created: [[gpd-win-5]], [[gpd-win-5-max-395]], [[gpd-win-5-max-385]]
- Updated: [[gpd]]

## [YYYY-MM-DD] ingest | Source: 2025-10-23 GPD WIN 5 review (YouTube)
- Created: [[2025-10-23-gpd-win-5-review-youtube]]
- Updated: [[gpd-win-5-max-395]], [[amd-ryzen-ai-max]], [[amd]]
- Notes: ...

## [YYYY-MM-DD] ingest | Resource: GPD WIN 5 BIOS v2.25
- Created: [[gpd-win-5-bios-v2-25]]
- Updated: [[gpd-win-5]] (current BIOS bumped from v2.24 to v2.25), [[amd]], [[gpd]]

## [YYYY-MM-DD] query | Question summary
- Answer filed as: [[analysis-page]]  (or "not filed")

## [YYYY-MM-DD] lint | Health check
- Issues found: N
- Fixed: list
- Deferred: list
```

## Deployment Notes

- Quartz routing assumes canonical normalization between leaf pages (`/page` backed by `page.html`) and folder pages (`/folder/` backed by `folder/index.html`). Any production web server must mirror Quartz dev-server behavior:
  - redirect `/leaf/` -> `/leaf` when `leaf.html` exists,
  - redirect `/folder` -> `/folder/` when `folder/index.html` exists,
  - return a real `404` status for missing pages instead of serving `404.html` as `200`.
- This matters because Quartz emits relative internal links. If a client lands on a slash-suffixed leaf URL such as `/products/gpd-pocket-4/`, links like `../entities/gpd` resolve against the wrong base path and navigation breaks.

## Frontend Compatibility Notes

- `Element.checkVisibility()` is only available in iOS Safari 17.4+. Do not call it directly in Quartz client scripts without a fallback.
- `portal/quartz/components/scripts/explorer.inline.ts` must use a compatibility helper for mobile explorer visibility checks, otherwise older iPhones throw `TypeError: <element>.checkVisibility is not a function` during SPA navigation.
- Quartz global assets (`index.css`, `prescript.js`, `postscript.js`, `static/contentIndex.json`) use stable filenames. If production caches JS/CSS aggressively, page HTML must append a per-build version query string, otherwise mobile browsers can stay stuck on stale bundles after a deploy.
- iOS WebKit can miscompute tap hit areas for wrapped inline Quartz internal links inside paragraphs/lists. Keep `.internal` links as real rectangular tap targets with `display: inline-block` and `max-width: 100%`, otherwise some multi-line mobile taps update nothing even though the link looks highlighted.

## Rules

1. **Always write "DROIX"**, never "DroiX" or "Droix".
2. **Ingest then archive.** After fully ingesting a raw source, move it from `raw/` to the corresponding path under `archive/`. Wiki pages must not reference files in `raw/` or `archive/` — all knowledge lives in the wiki itself.
3. **Always update `index.md` and `log.md`** after any wiki modification.
4. **Use wikilinks consistently.** Every brand, product, variant, entity, concept, or source mentioned in prose should link to its page if one exists.
5. **Flag contradictions explicitly.** Don't silently overwrite — note both claims and their sources.
6. **Ask before deleting.** Pages can be merged or deprecated, but confirm with the user first.
7. **Keep pages atomic.** One topic per page. If a page covers too much, split it. Pages over ~500 lines should almost always split.
8. **Cite sources.** Every factual claim in the wiki should trace back to a source page.
9. **Maintain the user's voice.** When the user provides interpretations or opinions, attribute them clearly (e.g., "Per DROIX editorial: ...").
10. **Attach reviews to the most specific page.** A review of a specific variant lives on that variant's page; only cross-variant reviews attach to the hub.
11. **Resources are versioned**. Never overwrite a resource page — create a new dated release and mark the previous one superseded.
12. **Technology-brand pages are always current.** Whenever a product, chipset, or resource is added to the wiki, update the relevant technology-brand page (amd.md, qualcomm.md, etc.) immediately.
13. **Category pages are always current.** Whenever a product is added, update its category page immediately.
14. **Source pages are complete.** Follow extraction depth rules (see Source page section). The wiki should never require going back to a raw or archived source to answer a question.
15. **Website-ready.** Every page should be detailed enough to serve as content for a website page without further research. Avoid stub pages in production — expand or merge them.
