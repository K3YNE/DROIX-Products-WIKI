---
title: Ingest Progress
type: analysis
slug: ingest-progress
created: 2026-04-22
updated: 2026-04-22
tags: [ingest, progress, automation]
---

# Ingest Progress Tracker

State machine for the autonomous bulk ingestion loop. Read this file at the start of each iteration.

## Current State

- **Phase:** 5 (Verification)
- **Phase 1 position:** 195/195 COMPLETE
- **Phase 2 position:** 387/387 COMPLETE
- **Phase 3 position:** 237/237 COMPLETE
- **Phase 4 position:** 67/67 COMPLETE
- **Total processed:** 886/886
- **Last batch:** 2026-04-22 Phase 4 (all 67 supplier resource files — 61 source pages + 30 minimal hubs)

## Phase Completion

- [x] Phase 0: Pre-flight (brand/category resolution)
- [x] Phase 1: Product pages (195/195) COMPLETE
- [x] Phase 2: KB articles (387/387) COMPLETE
- [x] Phase 3: Blog reviews (237/237) COMPLETE
- [x] Phase 4: Supplier resources (67/67) COMPLETE
- [ ] Phase 5: Verification (in progress)

## Phase 1 Queue — Product Pages (195 files)

Process in this order. Read files from the ingest ledger (`wiki/analysis/ingest-ledger.md`), rows with `type: product-page`.

**Batch size:** 8-10 per iteration

**Priority tiers:**
1. **Tier A — Already-onboarded products** (have wiki/products/ hubs): process first, no hub creation needed
2. **Tier B — Primary brands** (gpd, ayaneo, onexplayer, ayn, retroid, anbernic, konkr): main products, then accessories
3. **Tier C — Secondary brands** (beelink, gmktec, minisforum, acepc, droix, rocktek, miyoo, aokzoe): main products
4. **Tier D — Generic/unresolved** (no brand or minor brand): accessories, peripherals, legacy

## Phase 2 Queue — KB Articles (387 files)

Read files from ledger rows with `type: kb-article`.

**Batch size:** 5-8 per iteration

**Priority:** GPD articles first (largest set, most support-critical), then DROIX-branded, then other brands, then generic guides last.

## Phase 3 Queue — Blog Reviews (237 files)

Read files from ledger rows with `type: review-blog`.

**Batch size:** 3-5 per iteration

**Priority:** Recent (2025-2026) first, then 2023-2024, then older.

## Phase 4 Queue — Supplier Resources (67 files)

Files in `raw/supplier-resources/ayaneo/` (39) and `raw/supplier-resources/onexplayer/` (28).

**Batch size:** 2-3 per iteration

## Brand Resolution Rules

For files with `unresolved-brand` in the ledger, apply these rules:

| File pattern / keyword | Resolved brand | Notes |
|---|---|---|
| `droix-t8`, `droix-x3`, `droix-x7`, `droix-q8`, `droix-imxq`, `droix-imx6`, `droix-ck1`, `droix-ck2`, `droix-share`, `droix-play`, `droix-i9`, `droix-b52`, `control-centre`, `t8-s-plus`, `go-v3` | droix | Legacy DROIX TV boxes and accessories |
| `kodi`, `dbmc`, `xbmc`, `spmc`, `libreelec`, `openelec`, `coreelec` | droix | Generic media centre guides, brand as droix |
| `android-box`, `android-tv-box`, `set-top-box`, `surround-sound`, `recovery-menu` (generic) | droix | Generic Android box guides |
| `vpn`, `ipvanish`, `wifi` (generic), `network-sharing`, `streaming-and-casting` | droix | Generic networking/streaming guides |
| `rs-97`, `r36s`, `r46s` | generic | No-name Chinese handhelds |
| `x9`, `x9-pro` | generic | Generic game sticks |
| `budplus` | budplus | Projector brand |
| `moza` | moza | Camera gimbal brand |
| `g20-air-mouse`, `g30-air-mouse`, `air-mouse` (no brand) | generic | Generic peripherals |
| `gulikit` | gulikit | Controller brand |
| `ipega` | ipega | Controller brand |
| `kingspec` | kingspec | Storage brand |
| `nikko` | nikko | Electronic badge brand |
| `rii` | rii | Keyboard/remote brand |
| `scy` | scy | SSD brand |
| `easysmx` | easysmx | Controller brand |
| `retroflag`, `gpi-case`, `nespi` | retroflag | Raspberry Pi case brand |
| `gameforce` | gameforce | Handheld brand |
| `bittboy`, `pocket-go` | bittboy | Legacy handheld brand |
| `ldk` | ldk | Legacy handheld brand |
| `moqi` | moqi | Android gaming phone brand |
| `asus` | asus | Mini PC brand |
| `retropie` (generic) | generic | OS/software, not product-specific |
| `ak3v` | acepc | Mini PC brand (AK3V = ACEPC product) |
| `dmaf5`, `um250`, `um700` | minisforum | Mini PC brand |
| `how-to-assemble-the-dmaf5` | minisforum | MinisForum assembly guide |
| `justice-or-equality` | skip | Not product-related, skip entirely |
| `bt-are-your-isp` | skip | ISP article, not product-related |
| `how-to-basic` | skip | Generic, not product-related |

## Category Resolution Rules

For files with `unresolved-category` in the ledger:

| File pattern / keyword | Resolved category |
|---|---|
| `screen-protector` | accessory |
| `case`, `carrying-case`, `bag`, `hardshell` | accessory |
| `grip`, `grip-caps`, `thumb-caps`, `joystickcaps` | accessory |
| `magic-modules` | accessory |
| `headphones`, `earphones` | accessory |
| `micro-sd-card`, `ssd`, `nvme`, `storage` | accessory |
| `cable`, `usb-c`, `oculink` | accessory |
| `stylus` | accessory |
| `docking`, `dock`, `hub` | accessory |
| `air-mouse`, `keyboard`, `gamepad`, `controller` | accessory |
| `badge` | accessory |
| `projector` | accessory |
| `ayaneo-next` | handheld-pc |
| `ayaneo-pocket-dmg` | android-handheld |
| `gpd-xd`, `gpd-win` (legacy) | handheld-pc |
| `gpd-pocket` (legacy) | umpc |
| `droix-t8`, `droix-x3`, `droix-q8`, `droix-imxq`, `droix-x7`, `android-box` | media-player |
| `kodi`, `libreelec`, `openelec`, `streaming`, `vpn`, `network` (generic) | general-guide |
| `windows-10`, `teamviewer`, `drivers` (generic) | general-guide |
| `retropie`, `emuelec` (generic) | general-guide |
| `recovery-menu` (generic), `factory-reset` (generic), `play-store` | general-guide |
| `firmware` (product-specific) | inherit from product |

## Notes

- `general-guide` category: these KB articles don't map to a specific product category. Create source pages under the closest brand entity, or under DROIX if no brand. Do NOT create product hubs for generic guides.
- `media-player` category: legacy DROIX TV boxes. Create a `media-player` category entity if needed, or fold into existing categories.
- `skip` brand: files that are not product-related at all. Log them as skipped, do not ingest.
- When a file maps to an already-onboarded product (check wiki/products/), attach source page directly — no hub creation needed.
- When a file maps to a new product, run onboarding workflow first.

## Errors

(none yet)

## Skipped Files

(none yet)
