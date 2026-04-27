# Activity Log

## [2026-04-23] audit | Resource pages: full audit, dedicated pages, cross-model linking
- **Problem:** Dedicated resource pages (GPD WIN 5) were missing `download_url` in frontmatter and body. No other model had dedicated resource pages. Cross-model resources were duplicated without `applies_to` linking.
- **Fixed existing pages (6):** Added `download_url` to [[gpd-win-5-firmware-win11-25h2]], [[gpd-win-5-firmware-win11-24h2]], [[gpd-win-5-bios-v2-25]], [[gpd-win-5-drivers-2025-10-30]], [[gpd-win-5-user-manual-2025-09-04]], [[gpd-motionassistant-v1-2-0-9]].
- **Created GPD shared resource pages (9):** [[gpd-gpdtool-v1-45]], [[gpd-amd-handheld-control-v1-0-0]], [[gpd-dtsx-audio]], [[gpd-power-control-panel]], [[gpd-gamepad-test-v1-03]], [[gpd-drivers-v4-1-0]], [[gpd-firmware-win11-24h2-shared]], [[gpd-wincontrols-v1-16]], plus GPD WIN 5 model-specific: [[gpd-win-5-controller-firmware-v1-11]], [[gpd-win-5-ofn-firmware-2025-11-27]], [[gpd-win-5-wincontrols-v2-08]], [[gpd-win-5-smart-dock-manual-2025-09-04]].
- **Created GPD model-specific pages (~51):** Dedicated pages for current firmware, BIOS, drivers, manuals, and tools for WIN 4 (all years), WIN Mini (2024/2025), WIN Max 2 (all years), Pocket 4, DUO, MicroPC 2, G1, Pocket 3.
- **Created AYANEO dedicated pages (~125):** Dedicated pages for all current resources across 32 AYANEO supplier-resources pages (drivers, controller firmware, EC firmware, BIOS, tools, OTA updates).
- **Created ONEXPLAYER dedicated pages (~67):** Dedicated pages for all resources across 26 ONEXPLAYER supplier-resources pages (drivers, system packs, BIOS, controller firmware).
- **Updated supplier-resources indexes (72):** All GPD (14), AYANEO (32), ONEXPLAYER (26) supplier-resources pages now include "Individual source pages" lines linking to their dedicated pages.
- **Updated product hub pages (8):** GPD WIN 4, WIN Mini, WIN Max 2, Pocket 4, DUO, MicroPC 2, G1, Pocket 3 — Resources sections now reference dedicated pages.
- **Updated AGENTS.md:** Added mandatory `download_url` rule, cross-model detection guidance, and supplier-resources ↔ dedicated page relationship documentation.
- **Updated index.md:** Added GPD Shared Resource Pages section, updated WIN 5 resources line.
- **Total new pages created: ~243**

## [2026-04-22] lint | Post-ingestion audit: all issues resolved
- **none catalogued:** 0 remaining in wiki/products/ (was 37)
- **Stub pages:** 0 remaining (was 30) — all expanded with Summary, Resources, and wikilinks
- **Supplier Resources sections:** 0 remaining (was 22) — all merged into ## Resources
- **Slug mismatches:** 0 remaining — 10 ONEXPLAYER source files renamed to standard convention
- **Broken wikilinks:** 0 remaining for renamed slugs; onexplayer-onexfly 1-to-many links fixed
- **index.md:** GPD section updated with all 28 new supplier-resources links (including 9 legacy product entries)
- **ayaneo-slide-getting-started:** `product: null` corrected to `product: ayaneo-slide`

## [2026-04-22] enrich | Expanded 30 stub product pages (AYANEO + ONEXPLAYER)
- Full enrichment with specs, reviews, KB links (14): [[ayaneo-2]], [[ayaneo-2021]], [[ayaneo-air]], [[ayaneo-geek]], [[ayaneo-pocket-air]], [[ayaneo-pocket-micro-classic]], [[ayaneo-am02]], [[ayaneo-slide]], [[onexplayer-1-amd]], [[onexplayer-1-mini]], [[onexplayer-1-mini-amd]], [[onexplayer-2]], [[onexplayer-onexfly]], [[one-netbook-5]]
- Moderate enrichment with Summary + Resources (16): [[ayaneo-air-1s]], [[ayaneo-air-plus]], [[ayaneo-kun]], [[ayaneo-founder]], [[ayaneo-next-lite]], [[ayaneo-pocket-air-mini]], [[ayaneo-pocket-fit-elite]], [[ayaneo-am01]], [[ayaneo-am01s]], [[onexplayer-1]], [[onexplayer-1-mini-intel]], [[onexplayer-2pro]], [[onexplayer-game-console]], [[onexplayer-m1]], [[onexplayer-sugar-1]], [[onexplayer-x1-air]]
- Fixed: [[ayaneo-slide-getting-started]] `product: null` → `product: ayaneo-slide`
- All stub placeholder text removed; all pages now website-ready

## [2026-04-22] fix | Resources sections: populated 37 product hubs, removed all "none catalogued" entries
- Updated GPD (12): [[gpd-pocket-3]], [[gpd-pocket-4]], [[gpd-win-3]], [[gpd-win-4]], [[gpd-win-max-2]], [[gpd-win-mini]], [[gpd-duo]], [[gpd-g1]], [[gpd-micro-pc]], [[gpd-micropc-2]], [[gpd-p2-max]], [[gpd-win-5-smart-dock]]
- Updated AYANEO (14): [[ayaneo-2s]], [[ayaneo-3]], [[ayaneo-ag01]], [[ayaneo-flip]], [[ayaneo-flip-1s-ds]], [[ayaneo-next]], [[ayaneo-pocket-ace]], [[ayaneo-pocket-dmg]], [[ayaneo-pocket-ds]], [[ayaneo-pocket-evo]], [[ayaneo-pocket-micro]], [[ayaneo-pocket-s]], [[ayaneo-pocket-s2]], [[ayaneo-pocket-vert]]
- Updated ONEXPLAYER (9): [[onexplayer-g1]], [[onexplayer-onexfly-apex]], [[onexplayer-mini-pro]], [[onexplayer-onexfly-f1-pro]], [[onexplayer-onexgpu-2]], [[onexplayer-super-x]], [[onexplayer-x1-amd]], [[onexplayer-x1-mini]], [[onexplayer-x1-pro]]
- Updated AYN (6): [[ayn-odin-2]], [[ayn-odin-2-mini]], [[ayn-odin-2-portal]], [[ayn-odin-3]], [[ayn-odin-pro]], [[ayn-thor]]
- Updated Other (3): [[anbernic-rg-slide]], [[droix-nh8]], [[konkr-pocket-fit]]
- Also merged all stray "## Supplier Resources" sections into "## Resources" (22 pages normalised)

## [2026-04-22] ingest | Supplier resources: 15 GPD legacy product source pages
- Created: [[gpd-pocket-3-supplier-resources]], [[gpd-win-3-supplier-resources]], [[gpd-win-max-2021-supplier-resources]], [[gpd-p2-max-2022-supplier-resources]], [[gpd-micropc-supplier-resources]], [[gpd-p2-max-supplier-resources]], [[gpd-pocket-2-supplier-resources]], [[gpd-win-max-supplier-resources]], [[gpd-xp-plus-supplier-resources]], [[gpd-xp-supplier-resources]], [[gpd-pocket-supplier-resources]], [[gpd-win-2-supplier-resources]], [[gpd-win-supplier-resources]], [[gpd-xd-plus-supplier-resources]], [[gpd-xd-supplier-resources]]
- Removed raw files: GPD-POCKET-3-Resources.md, GPD-WIN-3-Resources.md, GPD-WIN-MAX-2021-Resources.md, GPD-P2-MAX-2022-Resources.md, GPD-MICROPC-Resources.md, GPD-P2-MAX-Resources.md, GPD-POCKET-2-Resources.md, GPD-WIN-MAX-Resources.md, GPD-XP-PLUS-Resources.md, GPD-XP-Resources.md, GPD-POCKET-Resources.md, GPD-WIN-2-Resources.md, GPD-WIN-Resources.md, GPD-XD-PLUS-Resources.md, GPD-XD-Resources.md
- Notes: Covers 8 Windows/UMPC products (Pocket 3, WIN 3, WIN Max 2021, P2 Max 2022, MicroPC, P2 Max, Pocket 2, WIN Max, WIN 2, WIN) and 5 legacy products (Pocket 1, XP Plus, XP, XD Plus, XD). Pocket 3 has most recent BIOS (N6000 v1.15) and firmware (Win11 22H2, 2025-02-26). WIN Max 2021 BIOS at V1.18. MicroPC BIOS v4.18 / EC v4.08 (2023-09-21). P2 Max BIOS V0.29 (current). WIN 2 BIOS 2.13 (current). XD Plus has two board revisions — firmware V1.14 for VR (new) board. XD has 8 firmware versions (3.3.6–3.4.9). XP Plus at V1.07 (2022-08-21). XP at V1.41 (2022-03-24). GPD Pocket (original) has richest resource set with Ubuntu 16.04 through 19.10 images, BIOS 0807 (current), and extensive community Linux builds. Many resources shared across products (Pocket 3/WIN 3/WIN Max 2021 share Drivers V1.7; N6000 Pocket 3 and P2 Max 2022 share Drivers V1.3/V6.0; Pocket 2/WIN 2/MicroPC/P2 Max share same Windows 10 driver package).

## [2026-04-22] ingest | Supplier resources: 6 GPD source pages (medium-priority batch)
- Created: [[gpd-win-mini-2024-supplier-resources]], [[gpd-win-4-2023-supplier-resources]], [[gpd-win-max-2-2023-supplier-resources]], [[gpd-g1-supplier-resources]], [[gpd-win-4-supplier-resources]], [[gpd-win-max-2-supplier-resources]]
- Updated: [[index]] (added Resources lines to gpd-win-mini, gpd-win-4, gpd-win-max-2, gpd-g1 entries)
- Removed raw files: GPD-WIN-MINI-2024-Resources.md, GPD-WIN-4-2023-Resources.md, GPD-WIN-MAX-2-2023-Resources.md, GPD-G1-Resources.md, GPD-WIN-4-Resources.md, GPD-WIN-MAX-2-Resources.md
- Notes: WIN 4 and WIN Max 2 each have two source pages — one for the original 6800U model and one for the 2023/2024 refresh. WIN Mini 2024 has BIOS V2.18 (current), WIN 4 2023 has BIOS v0.62 (current), WIN Max 2 2023 has BIOS v0.42 (current). GPD G1 has no BIOS on the resource page — directs to AMD official driver page for RX 7600M XT. Screen Color Calibration ICM files (D65/D70) available for WIN Max 2 (both original and 2023 pages). MotionAssistant v1.2.0.9 (2026-02-08) and GPDTool v1.45 (2026-04-13) are current handheld tools across all products.

## [2026-04-22] fix | Slug standardisation: ONEXPLAYER supplier-resource source pages
- Renamed 10 source files to follow `<brand>-<model>` slug convention per AGENTS.md
- `onexplayer1-supplier-resources` → [[onexplayer-1-supplier-resources]]
- `onexplayer1amd-supplier-resources` → [[onexplayer-1-amd-supplier-resources]]
- `onexplayer1mini-supplier-resources` → [[onexplayer-1-mini-supplier-resources]]
- `onexplayer1mini-amd-supplier-resources` → [[onexplayer-1-mini-amd-supplier-resources]]
- `onexplayer1mini-intel-supplier-resources` → [[onexplayer-1-mini-intel-supplier-resources]]
- `onexplayer-minipro-6800u-supplier-resources` → [[onexplayer-mini-pro-6800u-supplier-resources]]
- `onexfly-apex-supplier-resources` → [[onexplayer-onexfly-apex-supplier-resources]]
- `onexfly-f1-pro-supplier-resources` → [[onexplayer-onexfly-f1-pro-supplier-resources]]
- `onexfly-7840u-supplier-resources` → [[onexplayer-onexfly-7840u-supplier-resources]]
- `onexfly-8840u-supplier-resources` → [[onexplayer-onexfly-8840u-supplier-resources]]
- Fixed 1-to-many links: [[onexplayer-2]], [[onexplayer-2pro]], [[onexplayer-onexfly]]
- Updated: [[index]], all affected product pages

## [2026-04-22] ingest | Supplier resources: 61 source pages, 30 minimal product hubs, 1 FAQ page
- Processed ALL supplier resource files from raw/supplier-resources/ (AYANEO + ONEXPLAYER)
- **AYANEO source pages (34):**
  - Windows Console (17): [[ayaneo-2s-supplier-resources]], [[ayaneo-3-supplier-resources]], [[ayaneo-flip-supplier-resources]], [[ayaneo-flip-1s-supplier-resources]], [[ayaneo-next-supplier-resources]], [[ayaneo-kun-supplier-resources]], [[ayaneo-2-supplier-resources]], [[ayaneo-2021-supplier-resources]], [[ayaneo-air-supplier-resources]], [[ayaneo-air-1s-supplier-resources]], [[ayaneo-air-plus-6800u-supplier-resources]], [[ayaneo-air-plus-7x20u-supplier-resources]], [[ayaneo-air-plus-intel-supplier-resources]], [[ayaneo-geek-supplier-resources]], [[ayaneo-slide-supplier-resources]], [[ayaneo-founder-supplier-resources]], [[ayaneo-next-lite-supplier-resources]]
  - Android Console (12): [[ayaneo-pocket-s-supplier-resources]], [[ayaneo-pocket-s2-supplier-resources]], [[ayaneo-pocket-ace-supplier-resources]], [[ayaneo-pocket-dmg-supplier-resources]], [[ayaneo-pocket-ds-supplier-resources]], [[ayaneo-pocket-evo-supplier-resources]], [[ayaneo-pocket-micro-supplier-resources]], [[ayaneo-pocket-air-supplier-resources]], [[ayaneo-pocket-air-mini-supplier-resources]], [[ayaneo-pocket-micro-classic-supplier-resources]], [[ayaneo-pocket-fit-elite-supplier-resources]], [[konkr-pocket-fit-supplier-resources]]
  - Mini PC (3): [[ayaneo-am01-supplier-resources]], [[ayaneo-am01s-supplier-resources]], [[ayaneo-am02-supplier-resources]]
  - Shared/Tools (2): [[ayaneo-windows-console-supplier-resources]], [[ayaspace-supplier-resources]]
- **ONEXPLAYER source pages (27):** [[onexfly-apex-supplier-resources]], [[onexfly-f1-pro-supplier-resources]], [[onexplayer-super-x-supplier-resources]], [[onexplayer-x1-pro-supplier-resources]], [[onexplayer-x1-8840u-supplier-resources]], [[onexplayer-x1-155h-supplier-resources]], [[onexplayer-x1-mini-supplier-resources]], [[onexplayer-g1-a1370-supplier-resources]], [[onexplayer-g1-255h-supplier-resources]], [[onexplayer-m1-supplier-resources]], [[onexgpu-2-supplier-resources]], [[one-netbook-5-supplier-resources]], [[onexplayer-sugar-1-supplier-resources]], [[onexplayer-x1-air-supplier-resources]], [[onexplayer-2-6800u-supplier-resources]], [[onexplayer-2pro-7840-supplier-resources]], [[onexplayer-2pro-8840-supplier-resources]], [[onexplayer-game-console-supplier-resources]], [[onexfly-7840u-supplier-resources]], [[onexfly-8840u-supplier-resources]], [[onexplayer1-supplier-resources]], [[onexplayer1amd-supplier-resources]], [[onexplayer1mini-supplier-resources]], [[onexplayer1mini-amd-supplier-resources]], [[onexplayer1mini-intel-supplier-resources]], [[onexplayer-minipro-6800u-supplier-resources]], [[onexplayer-faqs-supplier-resources]]
- **Minimal product hubs created (30):**
  - AYANEO (17): [[ayaneo-2]], [[ayaneo-2021]], [[ayaneo-air]], [[ayaneo-air-1s]], [[ayaneo-air-plus]], [[ayaneo-geek]], [[ayaneo-kun]], [[ayaneo-slide]], [[ayaneo-founder]], [[ayaneo-next-lite]], [[ayaneo-pocket-air]], [[ayaneo-pocket-air-mini]], [[ayaneo-pocket-micro-classic]], [[ayaneo-pocket-fit-elite]], [[ayaneo-am01]], [[ayaneo-am01s]], [[ayaneo-am02]]
  - ONEXPLAYER (13): [[onexplayer-2]], [[onexplayer-2pro]], [[onexplayer-onexfly]], [[onexplayer-game-console]], [[onexplayer-1]], [[onexplayer-1-amd]], [[onexplayer-1-mini]], [[onexplayer-1-mini-amd]], [[onexplayer-1-mini-intel]], [[onexplayer-m1]], [[one-netbook-5]], [[onexplayer-sugar-1]], [[onexplayer-x1-air]]
- **Updated 22 existing product hubs** with Supplier Resources sections: [[ayaneo-2s]], [[ayaneo-3]], [[ayaneo-flip]], [[ayaneo-flip-1s-ds]], [[ayaneo-next]], [[ayaneo-pocket-s]], [[ayaneo-pocket-s2]], [[ayaneo-pocket-ace]], [[ayaneo-pocket-dmg]], [[ayaneo-pocket-ds]], [[ayaneo-pocket-evo]], [[ayaneo-pocket-micro]], [[konkr-pocket-fit]], [[onexplayer-onexfly-apex]], [[onexplayer-onexfly-f1-pro]], [[onexplayer-super-x]], [[onexplayer-x1-pro]], [[onexplayer-x1-amd]], [[onexplayer-x1-mini]], [[onexplayer-onexgpu-2]], [[onexplayer-g1]], [[onexplayer-mini-pro]]
- Skipped 4 empty category index files (Android Console, Mini PC, Linux — no resources returned by API)
- Notes: Supplier resource files remain in raw/supplier-resources/ as reference per instructions. AYANEO resources extracted from ayaneo.com API with version numbers, dates, changelogs, and download URLs. ONEXPLAYER resources extracted from onexplayerstore.com with Google Drive/OneDrive download links. AYASpace v3.0.0.30 is the current AYANEO system tool version. BIOS flashing instructions preserved where provided.

## [2026-04-22] ingest | 127 remaining DROIX blog review articles (batch 2)
- Created 127 source pages from remaining droix.net blog reviews (Sept 2022 - March 2026)
- Brand breakdown: GPD (14), AYANEO (18), ONEXPLAYER (12), Anbernic (12), Beelink (4), Minisforum (5), GMKTec (9), AYN (6), Retroid (5), Miyoo (2), DROIX own-brand (8), Geekom (5), ACEPC (3), AOKZOE (1), ONE-Netbook (2), Chuwi (1), RockTek (2), beCreatus (1), BudPlus (1), KONKR (1), Maxtang (1), Nikko (1), Triple Aero (1), BIWIN (1)
- Products covered include: GPD WIN 4 (6800U), WIN MAX 2 (6800U/2023/2024), Pocket 3, AYANEO 2/2S/3/Geek/Geek 1S/Flip/Slide/Pocket Air/S/S2/DMG/Micro/Micro Classic/ACE/DS/VERT/AG01, ONEXPLAYER Mini Pro/2/X1/X1 AMD/X1 Mini/X1 Pro/ONEXFLY/F1 Pro/G1/ONEXGPU/ONEXGPU 2/Apex, AYN Odin Pro/2/2 Mini/2 Portal/Loki/Thor/Odin 3, Anbernic RG353V/M/PS/405V/505/Nano/ARC/35XX/35XX Plus/H/SP/556/Cube/40XXV/Slide, Retroid Pocket 3+/2S/Flip/4 Pro/5, Miyoo Mini Plus/A30, GMKTec NucBox7/G5/K6/K8/K9/M3/M4/M5/M6/GBook, and many mini PCs and accessories
- All 137 files archived to archive/ingest/blog/droix-reviews/
- Raw ingest directory cleared

## [2026-04-22] ingest | 100 blog review articles (17 GPDStore + 83 DROIX)
- Created 100 source pages from blog reviews:
  - **GPDStore reviews (17):** GPD WIN 4 (2022, 2024, 2025), GPD WIN MAX 2 (2022, 2024, 2025), GPD WIN Mini (2024, 2025), GPD Pocket 3 (7505), GPD Pocket 4 (HX 370), GPD Duo (HX 370), GPD G1 eGPU, GPD MicroPC 2 (N250/N300), GPD WIN 5 (MAX+ 395), BIWIN Mini SSD, GPD WIN 5 Docking Station, GPD P2 MAX 2022
  - **DROIX reviews (83):** Spanning 2017-2022, covering GPD (WIN 2/3/Max/XP/Pocket/P2 Max), AYANEO (NEO 2021/Pro/Air/NEXT), ONEXPLAYER (1S/Mini/AMD), Anbernic (RG351V/M/P/MP, RG300X, RG503, RG353P, RG552, WIN 600), Retroid (Pocket 2/2+/3), Beelink (SEi 10, U59, SER3/4/5, GK35/Pro, GTi11, GT King, GTR4/5, GT-R7, Mini S), MinisForum (X400/X500, HX90, TL50, HM50/80, JB95, UM350, B550), GMKTec (NucBox5), Miyoo (Mini V2), DROIX own-brand (CK2, Stheno F5, Proteus G4/G7/10/10S/11), controllers (EasySMX), accessories
- Updated product hubs with blog review references: [[gpd-win-4]], [[gpd-win-5]], [[gpd-win-max-2]], [[gpd-win-mini]], [[gpd-pocket-3]], [[gpd-pocket-4]], [[gpd-duo]], [[gpd-g1]], [[gpd-micropc-2]], [[gpd-p2-max]]
- Archived 17 files to archive/ingest/blog/gpdstore-reviews/
- Archived 83 files to archive/ingest/blog/droix-reviews/

## [2026-04-22] ingest | 108 DROIX KB articles (batch 3: how-to-switch through your-tv-isnt)
- Created 108 source pages from droix.net knowledge base (remaining droix-kb files)
- Skipped 1 file: justice-or-equality.md (garbled/non-product content)
- Brand breakdown: droix (55), gpd (17), anbernic (8), beelink (5), minisforum (5), onexplayer (3), retroid (3), generic (12)
- Updated 7 product hubs with KB references: [[gpd-win-5]], [[gpd-win-4]], [[gpd-win-max-2]], [[gpd-win-mini]], [[gpd-win-3]], [[gpd-g1]], [[onexplayer-onexfly-f1-pro]]
- Topics: BIOS updates, firmware flashing, device teardowns, network troubleshooting, Kodi/DBMC setup, custom firmware for retro handhelds, Windows reinstallation, driver management, VPN setup, key mapping, international shipping, warranty transfer

## [2026-04-22] ingest | 100 DROIX KB articles (batch 2: how-to-delete through how-to-stream)
- Created 100 source pages from droix.net knowledge base (how-to-delete-and-disable-add-ons-in-kodi through how-to-stream-any-magnet-torrent-link)
- Updated 15 product hubs with KB references: [[gpd-win-5]], [[gpd-win-max-2]], [[gpd-win-mini]], [[gpd-win-4]], [[gpd-win-3]], [[gpd-pocket-4]], [[gpd-pocket-3]], [[ayaneo-next]], [[ayn-thor]], [[ayn-odin-2]], [[retroid-pocket-flip]], [[onexplayer-onexfly-f1-pro]], [[droix-proteus-11]], [[rocktek-gx1]], [[miyoo-a30]]
- Brand distribution: gpd (28), droix/generic (42), ayaneo (3), onexplayer (3), ayn (2), retroid (3), anbernic (7), beelink (2), minisforum (3), retroid (2), other (5)
- All 100 files archived to archive/ingest/kb/droix-kb/
- 109 KB articles remaining in raw/ingest/kb/droix-kb/

## [2026-04-22] ingest | 96 DROIX KB articles (first 100 alphabetically, 4 skipped)
- Created 96 source pages from droix.net knowledge base:
  - **Skipped (4):** bt-are-your-isp (not product-related), how-to-basic (joke page), egpu-fix (duplicate of GPDStore version), addressing-windows-11-24h2-bsods (duplicate of GPDStore version)
  - **DROIX legacy media players (24):** [[droix-recovery-menu]], [[droix-t8-firmware-recovery]], [[droix-t8-mini-how-to-guide]], [[droix-t8-s-how-to-guide]], [[droix-imx6-setup-guide]], [[droix-imxqpro-how-to-guide]], [[droix-x7-q7-how-to-guide]], [[droix-imx6-factory-reset-alternative]], [[droix-play-gamepad-manual]], [[droix-i9-mini-keyboard-guide]], [[droix-share-how-to]], [[droix-share-android-demo]], [[droix-checking-drive-partitions]], [[droix-formatting-internal-hard-drive]], [[droix-go-v3-launcher-change]], [[droix-t8-s-plus-launcher-change]], [[droix-remote-control-guide]], [[droix-b52-air-mouse-calibration]], [[droix-emulate-controller-interface]], [[droix-heads-up-notifications]], [[droix-sky-router-disconnect-fix]], [[droix-control-centre-kodi-fixes]], [[droix-control-centre-maintenance]], [[droix-google-play-store-first-run]]
  - **Kodi/LibreELEC guides (11):** [[droix-clearing-kodi-data]], [[droix-cast-youtube-to-kodi]], [[droix-libreelec-file-transfer]], [[droix-fix-blank-kodi-keyboard]], [[droix-kodi-confluence-shortcuts]], [[droix-kodi-library-setup]], [[droix-kodi-lip-sync-adjustment]], [[droix-kodi-background-change]], [[droix-close-kodi-correctly]], [[droix-configure-kodi-correctly]], [[beelink-gt-king-coreelec-install]]
  - **DROIX general/cross-brand guides (12):** [[droix-wifi-troubleshooting]], [[droix-clear-app-data-android-6-7-devices]], [[droix-clear-app-data-android-6-7]], [[droix-copy-files-via-usb-ftp]], [[droix-connect-ipega-gamepads]], [[handheld-tdp-performance-guide]], [[handheld-companion-guide]], [[benchmark-windows-device]], [[benchmark-windows-android-handheld]], [[add-games-roms-handheld]], [[budplus-s3-getting-started]], [[mini-pc-reinstall-windows-guide]]
  - **Anbernic (6):** [[anbernic-charging-guide]], [[anbernic-arc-getting-started]], [[anbernic-rg35xx-plus-getting-started]], [[anbernic-rg405v-getting-started]], [[anbernic-rg350-add-emulators]], [[anbernic-rg351p-add-games]]
  - **AYANEO (4):** [[ayaneo-pocket-s-firmware-reflash]], [[ayaneo-pocket-s-getting-started]], [[ayaneo-slide-getting-started]], [[ayaneo-joystick-calibration]]
  - **AYN (2):** [[ayn-odin-2-getting-started]], [[ayn-odin-2-super-dock-getting-started]]
  - **GPD (12):** [[gpd-pocket-best-software]], [[gpd-win-3-touch-panel-fix]], [[gpd-xd-plus-firmware-flash]], [[gpd-win-software-getting-started]], [[gpd-win-4-6800u-lcd-firmware-fix]], [[gpd-win-max-reset-guide]], [[gpd-xd-plus-miravision-settings]], [[gpd-joystick-calibration]], [[gpd-win-4-2023-2024-getting-started]], [[gpd-win-max-2-2023-getting-started]], [[gpd-win-mini-2023-2024-getting-started]], [[gpd-bios-updates-guide]], [[gpd-tool-download-setup-guide]]
  - **AOKZOE (1):** [[aokzoe-a1-pro-getting-started]]
  - **Beelink (1):** [[beelink-pc-firmware-reinstall]]
  - **Generic/retro (6):** [[bittboy-pocket-go-custom-firmware]], [[custom-firmware-retro-handhelds]], [[emuelec-add-games-scrape-data]], [[emuelec-wifi-theme-scrape]], [[gmenu2x-change-emulator-folder]], [[retroflag-gpi-case-wifi]]
  - **Other brands (8):** [[minisforum-assembly-guide]], [[minisforum-um780-xtx-getting-started]], [[minisforum-un100-getting-started]], [[miyoo-mini-plus-getting-started]], [[onexplayer-onexfly-getting-started]], [[onexplayer-onexgpu-getting-started]], [[retroid-pocket-3-plus-flip-getting-started]], [[retroid-pocket-4-getting-started]]
  - **DROIX accessories/generic getting-started (9):** [[droix-nt8-getting-started]], [[droix-pm13-getting-started]], [[getting-started-handheld-gaming-pc]], [[getting-started-mini-pc]], [[getting-started-portable-monitor]], [[getting-started-retro-handheld]], [[gulikit-7in1-dock-getting-started]], [[nespi-4-build-guide]]
- Updated product hubs: [[ayaneo-pocket-s]], [[ayn-odin-2]], [[gpd-win-3]], [[gpd-win-4]], [[gpd-win-max-2]], [[gpd-win-mini]], [[anbernic-rg405v]], [[anbernic-rg35xx-plus]], [[anbernic-rg-arc-s]], [[aokzoe-a1-pro]]
- Archived all 100 raw files to archive/ingest/kb/droix-kb/
- Notes: Full content reproduction per AGENTS.md rules. DroiX/DroidBOX references normalized to DROIX. 2 articles skipped as duplicates of existing GPDStore KB versions. 2 articles skipped as not product-related.

## [2026-04-22] ingest | 68 GPDStore KB articles (FAQs, guides, BIOS updates, hardware repairs, software tools)
- Created 68 source pages (2 skipped — gpd-win-5-getting-started and gpd-win-5-faq already existed):
  - **FAQs (8):** [[gpd-duo-faq]], [[gpd-g1-faq]], [[gpd-micropc-2-faq]], [[gpd-pocket-3-faq]], [[gpd-pocket-4-faq]], [[gpd-win-4-faq]], [[gpd-win-max-2-faq]], [[gpd-win-mini-faq]]
  - **Getting started (4):** [[gpd-win-max-2-getting-started]], [[gpd-win-mini-getting-started]], [[droix-pm14-getting-started]], [[gpd-156-portable-monitor-getting-started]]
  - **BIOS updates (10):** [[gpd-duo-bios-update]], [[gpd-g1-bios-update]], [[gpd-micropc-2-bios-update]], [[gpd-pocket-4-bios-update]], [[gpd-win-4-bios-update]], [[gpd-win-5-bios-update-guide]], [[gpd-win-max-2-bios-update]], [[gpd-win-max-2-2025-bios-update]], [[gpd-win-mini-bios-update]], [[gpd-win-mini-2025-bios-update]]
  - **Hardware repairs (16):** [[gpd-win-5-triggers-fix]], [[gpd-win-5-left-joystick-replacement]], [[gpd-win-5-right-joystick-replacement]], [[gpd-win-4-ssd-replacement]], [[gpd-win-4-triggers-replacement]], [[gpd-win-4-display-replacement]], [[gpd-win-max-2-keyboard-replacement]], [[gpd-win-max-2-display-replacement]], [[gpd-win-max-2-ssd-trigger-battery-replacement]], [[gpd-win-mini-teardown]], [[gpd-win-mini-2025-display-replacement]], [[gpd-win-mini-2024-fan-replacement]], [[gpd-win-mini-2025-battery-replacement]], [[gpd-win-mini-2025-right-joystick-replacement]], [[gpd-pocket-4-fan-replacement]], [[gpd-pocket-4-keyboard-replacement]]
  - **Firmware/software (6):** [[gpd-win-5-optical-mouse-firmware]], [[gpd-win-mini-2025-gamepad-firmware]], [[gpd-motion-assistant-software]], [[gpd-tool-frontend]], [[gpd-egpu-fix-hx-365-370]], [[gpd-duo-screen-tearing-fix]]
  - **Device-specific guides (8):** [[gpd-win-5-usb-charger-guide]], [[gpd-win-5-battery-cable-extender]], [[gpd-win-5-mini-ssd-guide]], [[gpd-win-max-2-2025-4g-module-install]], [[gpd-win-max-2-2025-battery-icon-fix]], [[gpd-pocket-4-module-change]], [[gpd-micropc-2-tdp-change]], [[gpd-micropc-2-enable-windows-updates]], [[gpd-duo-video-input-guide]]
  - **Cross-product guides (16):** [[gpd-optimisation-guide]], [[gpd-amd-graphics-drivers]], [[gpd-add-games-roms]], [[gpd-retroarch-setup]], [[gpd-benchmark-guide]], [[gpd-benchmark-device-performance]], [[gpd-factory-reset]], [[gpd-reinstall-windows]], [[gpd-update-windows-drivers]], [[gpd-rufus-bootable-usb]], [[gpd-recalibrate-controls]], [[gpd-ram-frequency-change]], [[gpd-warranty-transfer]], [[gpd-wd-sandisk-ssd-firmware-fix]]
- Updated product hubs: [[gpd-win-5]], [[gpd-win-4]], [[gpd-win-max-2]], [[gpd-win-mini]], [[gpd-duo]], [[gpd-g1]], [[gpd-pocket-3]], [[gpd-pocket-4]], [[gpd-micropc-2]] (added KB article wikilinks)
- Updated brand entity: [[gpd]] (comprehensive Knowledge Base section with all articles grouped by product)
- Archived all 70 raw files to archive/ingest/kb/gpdstore-kb/
- Notes: Full content reproduction per AGENTS.md rules. Every Q&A, step, checklist, warning, troubleshooting item, image reference, and external link preserved.

## [2026-04-22] ingest | 8 GPDStore KB getting-started articles
- Created: [[gpd-pocket-4-getting-started]], [[gpd-micropc-2-getting-started]], [[gpd-duo-getting-started]], [[gpd-g1-getting-started]], [[gpd-pocket-3-getting-started]], [[gpd-win-4-getting-started]], [[droix-sd1-getting-started]], [[droix-nh8-getting-started]]
- Created: [[droix-nh8]] (new product hub for DROIX NH8 USB Hub with NVMe)
- Updated: [[gpd-pocket-4]], [[gpd-micropc-2]], [[gpd-duo]], [[gpd-g1]], [[gpd-pocket-3]], [[gpd-win-4]], [[droix-sd1]] (added Knowledge Base sections)
- Updated: [[index.md]] (added KB links to 7 products, added DROIX NH8 product hub entry)
- Notes: Full content reproduction per AGENTS.md rules. Each source page includes all inspection checklists, update procedures, software recommendations, accessory descriptions, FAQ Q&A pairs, and troubleshooting steps from the original articles.

## [2026-04-22] onboard + ingest | Remaining 56 GPDStore product pages: 10 new product hubs, 56 source pages

### New product hubs (10)
- [[gpd-win-4]] — Sliding keyboard handheld, yearly refreshes (2022/2023/2024/2025). AMD Ryzen 6800U through AI 9 HX 370.
- [[gpd-win-3]] — Intel Tiger Lake handheld (i5-1135G7/i7-1195G7), Thunderbolt 4. Discontinued.
- [[gpd-win-max-2]] — 10.1" large-format handheld, yearly refreshes (2021/2022/2023/2024/2025). AMD Ryzen 6800U through AI 9 HX 370.
- [[gpd-win-mini]] — Compact clamshell handheld, yearly refreshes (2023/2024/2025). AMD Ryzen 7640U through AI 9 HX 370.
- [[gpd-duo]] — Dual 13.3" AMOLED UMPC with stylus support. Ryzen AI 9 HX 370 / 8840U.
- [[gpd-g1]] — eGPU dock with AMD RX 7600M XT. OCuLink/USB4/TB3/TB4. 2023 and 2024 models.
- [[gpd-pocket-3]] — 8" modular UMPC (Intel Pentium Gold 7505). KVM/RS-232 expansion modules.
- [[gpd-p2-max]] — 8.9" mini laptop (Intel Pentium Silver N6000). Discontinued.
- [[gpd-micro-pc]] — Original MicroPC (Intel Celeron N4120). RS-232 serial port. Predecessor to MicroPC 2.
- [[gpd-portable-monitor]] — 15.6" 4K portable monitors (3 variants: Adobe RGB, stylus, touchscreen).

### New source pages (56)
- 10 product page sources for devices with new hubs
- 16 yearly-refresh product page sources (WIN 4 x4, WIN Max 2 x5, WIN Mini x3, WIN Max 2021 x1, G1 x2, P2 Max x1)
- 15 accessory source pages (cases, grips, docking stations, LTE modules, screen protectors, styluses, cables)
- 6 storage/SSD source pages (BIWIN 2230 NVMe, Mini SSD, RD510 reader)
- 5 monitor source pages (3x 15.6" 4K variants, DROIX PM13, DROIX PM14)
- 4 cable/connectivity source pages (USB 4.0 x2, USB-C to HDMI, USB5, OCuLink)

### Updated pages
- [[gpd]] — Added 10 new products to lineup table, cleared Forthcoming section
- [[handheld-pc]] — Added WIN 4, WIN 3, WIN Max 2, WIN Mini
- [[egpu]] — Added GPD G1
- [[umpc]] — Added GPD DUO, Pocket 3, P2 Max, MicroPC
- [[amd-rx-7600m-xt]] — Added GPD G1 to products using this chip
- [[index]] — Added all 10 new product hubs, 56 source pages, GPDStore standalone accessories section

### Notes
- GPD G1 is a DIFFERENT product from [[onexplayer-g1]] (the dual-keyboard Windows handheld). GPD G1 is an eGPU dock.
- WIN Max 2021 and WIN Max 2 (2022 original) list identical specs on GPDStore (both show Ryzen 7 6800U). The "2021" branding may refer to a pre-refresh variant.
- GPD DUO is categorised as UMPC (not handheld-pc) due to its laptop form factor and productivity focus.
- GPD Pocket 2 case source page created but GPD Pocket 2 hub not onboarded (legacy product).
- SD1 Docking Station appears on both GPDStore and DROIX store; source page links to existing [[droix-sd1]] hub.
- BIWIN Mini SSD has 1-year warranty (not the standard 2-year), noted on source page.
- Archived: 56 files from `raw/ingest/product/gpdstore-shop/`

## [2026-04-22] onboard + ingest | Final 25 DROIX product pages: 9 product hubs, 25 source pages, 1 new brand entity

### New brand entity
- [[miyoo]] — budget Linux retro handheld manufacturer (A30, Mini Plus)

### New product hubs (9)
- [[miyoo-a30]] — Allwinner A33, 2.8" IPS, Linux retro handheld
- [[miyoo-mini-plus]] — SigmaStar SSD202D, 3.5" IPS, MiniUI/Onion OS retro handheld
- [[r36s]] — RK3326, 3.5" IPS, vertical Linux retro handheld (generic)
- [[r46s]] — RK3566, 4" IPS 1:1 square display, Linux retro handheld (generic)
- [[droix-proteus-11]] — DROIX own-brand mini PC (Intel i5-1135G7 / i7-1165G7, Thunderbolt 4)
- [[droix-sd1]] — DROIX own-brand 6-in-1 USB-C docking station
- [[x9-game-stick]] — Amlogic S905X3 retro game stick (EmuELEC, 4K HDMI)
- [[x9-pro-game-stick]] — Amlogic S905X3 retro game stick (64-256 GB variants)
- [[budplus-s3-projector]] — BudPlus 1080p Android 9 home cinema projector

### New source pages (25)
- 9 product page sources for new hubs above
- 16 accessory source pages: animal thumb grip caps, AYANEO thumb caps (S2/Micro/DMG/ACE), Miyoo Mini Plus case, GPD earphones, MicroSD card, SCY mSATA SSD, KingSpec 2230 NVMe, DROIX USB 4.0 cable, ONEXPLAYER X1 controller bag, GuliKit 7-in-1 dock, GuliKit KingKong 2 Pro controller, iPega 9120 controller, G20 air mouse, G30 air mouse, NIKKO electronic badge, MOZA AirCross GH4/GH5 PSU

### Updated pages
- [[droix]] — added Proteus 11, SD1, and DROIX-branded accessories
- [[ayaneo-pocket-s2]] — added thumb caps accessory
- [[onexplayer-x1-amd]], [[onexplayer-x1-mini]] — added controller bag accessory
- [[android-handheld]] — added Miyoo A30, Mini Plus, R36S, R46S
- [[mini-pc]] — added Proteus 11
- [[media-player]] — added X9, X9 Pro game sticks
- [[accessory]] — added SD1, BudPlus S3
- [[index]] — added all new products, Miyoo brand, standalone accessories

### Notes
- R36S and R46S listed under "GameForce" brand on DROIX; they are generic Chinese handhelds.
- X9 and X9 Pro game sticks share identical S905X3 hardware; differ only in storage options.
- R46S has spec discrepancies: body says 1.8 GHz / 4000 mAh / 8 hours; spec table says 1.5 GHz / 7 hours. Flagged on source page.
- MOZA AirCross PSU is a camera gimbal accessory — flagged as non-gaming.
- NIKKO Electronic Badge is a social wearable display — flagged as non-gaming.
- Miyoo Mini Plus battery discrepancy: body says 3000 mAh / 8 hours; spec table says 7 hours.
- Archived: 25 files from `raw/ingest/product/droix-shop/`

## [2026-04-22] onboard + ingest | Multi-brand batch: 31 files, 26 product hubs, 31 source pages, 7 new brand entities

### New brand entities created
- [[beelink]] (13 mini PCs), [[gmktec]] (5 mini PCs), [[acepc]] (2 mini PCs), [[aokzoe]] (1 handheld PC), [[minisforum]] (1 mini PC), [[rocktek]] (4 media players)
- [[media-player]] — new product category entity for Android TV boxes / Google TV devices

### Retroid (3 hubs + 5 source pages)
- Created product hubs: [[retroid-pocket-3-plus]], [[retroid-pocket-4-pro]], [[retroid-pocket-flip]]
- Created source pages: [[retroid-pocket-3-plus-product-page-droix]], [[retroid-pocket-4-pro-product-page-droix]], [[retroid-pocket-flip-product-page-droix]], [[retroid-pocket-flip-case-product-page-droix]], [[retroid-pocket-flip-grip-product-page-droix]]
- Updated: [[retroid]] (3 products added), [[android-handheld]] (3 new entries)

### Beelink (13 hubs + 13 source pages)
- Created product hubs: [[beelink-eqi12]], [[beelink-eqr5]], [[beelink-eqr6]], [[beelink-gti10]], [[beelink-gti11]], [[beelink-gti13]], [[beelink-gti14-ultra]], [[beelink-mini-s]], [[beelink-s12]], [[beelink-sei12-i7]], [[beelink-sei12]], [[beelink-sei14]], [[beelink-t5]]
- Created source pages: corresponding `-product-page-droix` for each

### GMKTec (5 hubs + 5 source pages)
- Created product hubs: [[gmktec-g1]], [[gmktec-nucbox-g3]], [[gmktec-nucbox-k9]], [[gmktec-nucbox-m3]], [[gmktec-nucbox-m5]]

### Other brands (5 hubs + 8 source pages)
- Created: [[acepc-picobox-mini]], [[acepc-picobox-pro]], [[aokzoe-a1-pro]], [[minisforum-elitemini-um690]], [[rocktek-g2]], [[rocktek-g2-rtx5000]], [[rocktek-gb1]], [[rocktek-gx1]]

### Updated entity/category pages
- [[mini-pc]] — full product tables (22 products across 4 brands)
- [[handheld-pc]] — added [[aokzoe-a1-pro]]
- [[android-handheld]] — added 3 Retroid products
- [[index]] — all 26 new products + 7 new brands + media-player category

### Notes
- Beelink GTi11 spec table is minimal (only brand listed); hub uses product description data.
- Several Beelink/GMKTec products have discrepancies between product copy and spec table (e.g., Ethernet speed, WiFi version). Flagged on source pages.
- RockTek G2 base model shows Android 14 in spec table but Android TV 11 in copy; RTX5000 bundle shows Android TV 11 consistently.
- ACEPC PicoBox Pro has RAM discrepancy: spec table says 32 GB but configurations list 16 GB.
- Retroid Pocket 4 listing covers both RP4 (D900) and RP4 PRO (D1100) in one page; hub created for PRO as primary.
- Archived: 31 files from `raw/ingest/product/droix-shop/`

## [2026-04-22] onboard + ingest | ONEXPLAYER batch: 9 new products, 20 source pages
- Created product hubs: [[onexplayer-mini]], [[onexplayer-mini-pro]], [[onexplayer-onexfly-f1-pro]], [[onexplayer-onexgpu]], [[onexplayer-onexgpu-2]], [[onexplayer-super-x]], [[onexplayer-x1-amd]], [[onexplayer-x1-mini]], [[onexplayer-x1-pro]]
- Created source pages: [[onexplayer-mini-product-page-droix]], [[onexplayer-mini-pro-product-page-droix]], [[onexplayer-onexfly-f1-pro-product-page-droix]], [[onexplayer-onexgpu-product-page-droix]], [[onexplayer-onexgpu-2-product-page-droix]], [[onexplayer-super-x-product-page-droix]], [[onexplayer-x1-amd-product-page-droix]], [[onexplayer-x1-mini-product-page-droix]], [[onexplayer-x1-pro-product-page-droix]], [[onexplayer-apex-battery-product-page-droix]], [[onexplayer-apex-battery-cable-product-page-droix]], [[onexplayer-apex-battery-dock-product-page-droix]], [[onexplayer-apex-case-product-page-droix]], [[onexplayer-onexfly-case-product-page-droix]], [[onexplayer-onexgpu-case-product-page-droix]], [[onexplayer-onexgpu-2-case-product-page-droix]], [[onexplayer-oculink-cable-product-page-droix]], [[onexplayer-x1-bag-product-page-droix]], [[onexplayer-x1-connector-product-page-droix]], [[onexplayer-x1-mini-keyboard-product-page-droix]]
- Updated: [[onexplayer]] (11 products), [[onexplayer-onexfly-apex]] (accessories), [[handheld-pc]] (7 new entries), [[egpu]] (2 new entries), [[index]], [[log]]
- Archived: 20 files from `raw/ingest/product/droix-shop/onexplayer-*.md`
- Notes: ONEXFLY F1 Pro has 3 CPU tiers (8840U/HX365/HX370) in one listing. Super X is a 14" AMOLED tablet with up to 128GB RAM and cTDP 45-120W. X1 series features native OCuLink and 3-in-1 detachable controllers. ONEXGPU 2 benchmarks: Time Spy 15,916, Fire Strike 42,949 (RX 7800M). Mini is legacy (LPDDR4X, no video out on AMD variant). OCuLink cable compatible across ONEXGPU, ONEXGPU 2, and X1.

## [2026-04-22] onboard + ingest | AYN Odin family (4 new hubs, 12 source pages)
- Created product hubs: [[ayn-odin-2]], [[ayn-odin-2-mini]], [[ayn-odin-2-portal]], [[ayn-odin-pro]]
- Created source pages: [[ayn-odin-2-product-page-droix]], [[ayn-odin-2-mini-product-page-droix]], [[ayn-odin-2-portal-product-page-droix]], [[ayn-odin-pro-product-page-droix]], [[ayn-odin-3-product-page-droix]], [[ayn-odin-2-case-product-page-droix]], [[ayn-odin-2-screen-protector-product-page-droix]], [[ayn-odin-2-super-dock-product-page-droix]], [[ayn-odin-2-mini-case-product-page-droix]], [[ayn-odin-2-mini-screen-protector-product-page-droix]], [[ayn-odin-2-portal-case-product-page-droix]], [[ayn-odin-2-portal-screen-protector-product-page-droix]]
- Updated: [[ayn-odin-3]] (added tiers, product page ref, predecessor link), [[ayn]] (full product table, 6 products), [[qualcomm-snapdragon-8-gen-2]] (added Odin 2/Mini/Portal), [[qualcomm]] (added 3 products to tables), [[android-handheld]] (added 4 products), [[index]], [[log]]
- Notes: Odin 2 family all use Snapdragon 8 Gen 2 / Adreno 740. Odin Pro is a legacy SD845 device (out of stock). Odin 2 Portal was previously the Android performance reference before the Odin 3. Super Dock is out of stock. Accessories (cases, screen protectors, dock) attached to parent product hubs.

## [2026-04-22] ingest | Phase 1 Batch 6: AYANEO accessories (13 source pages)
- Created: [[ayaneo-pocket-s-accessories-product-page-droix]], [[ayaneo-3-case-product-page-droix]], [[ayaneo-3-screen-protector-product-page-droix]], [[ayaneo-joystickcaps-product-page-droix]], [[ayaneo-magic-modules-product-page-droix]], [[ayaneo-pocket-dmg-case-product-page-droix]], [[ayaneo-pocket-evo-case-product-page-droix]], [[ayaneo-pocket-evo-screen-protector-product-page-droix]], [[ayaneo-pocket-micro-case-product-page-droix]], [[ayaneo-pocket-micro-leather-case-product-page-droix]], [[ayaneo-pocket-micro-screen-protector-product-page-droix]], [[ayaneo-pocket-s-grip-caps-product-page-droix]], [[ayaneo-pocket-s-case-product-page-droix]]
- Updated: [[ayaneo-3]], [[ayaneo-pocket-dmg]], [[ayaneo-pocket-evo]], [[ayaneo-pocket-micro]], [[ayaneo-pocket-s]]
- Archived: 13 files from `raw/ingest/product/droix-shop/`
- Notes: All AYANEO accessories attached to parent product hubs. Magic modules are magnetic modular accessories for AYANEO 3. Joystickcaps compatible with AYANEO 3 and Pocket EVO. All Anbernic + AYANEO product pages now complete.

## [2026-04-22] onboard | 8 AYANEO products (4 Windows handhelds, 4 Android handhelds)
- Created product hubs: [[ayaneo-2s]], [[ayaneo-3]], [[ayaneo-flip]], [[ayaneo-next]], [[ayaneo-pocket-dmg]], [[ayaneo-pocket-evo]], [[ayaneo-pocket-micro]], [[ayaneo-pocket-s]]
- Created source pages: [[ayaneo-2s-product-page-droix]], [[ayaneo-3-product-page-droix]], [[ayaneo-flip-product-page-droix]], [[ayaneo-next-product-page-droix]], [[ayaneo-pocket-dmg-product-page-droix]], [[ayaneo-pocket-evo-product-page-droix]], [[ayaneo-pocket-micro-product-page-droix]], [[ayaneo-pocket-s-product-page-droix]]
- Updated: [[ayaneo]], [[handheld-pc]], [[android-handheld]], [[qualcomm-snapdragon-g3x-gen-2]], [[index]]
- Notes: AYANEO 3 features modular controller system (56 combos, GuliKit collab) and links to [[amd-ryzen-ai-9-hx-370]]. AYANEO Flip is the original DS/KB clamshell preceding [[ayaneo-flip-1s-ds]]. AYANEO Next is legacy Zen 3 (out of stock). Pocket DMG/EVO/S use [[qualcomm-snapdragon-g3x-gen-2]]. Pocket Micro uses MediaTek Helio G99 (no entity page yet).

## [2026-04-22] ingest | Phase 1 Batch 4: Remaining Anbernic products + accessories (3 new products, 3 cases)
- Created: [[anbernic-rg35xx-plus]], [[anbernic-rg35xxsp]], [[anbernic-rg405v]] (product hubs), [[anbernic-rg35xx-plus-product-page-droix]], [[anbernic-rg35xxsp-product-page-droix]], [[anbernic-rg405v-product-page-droix]], [[anbernic-rg-nano-case-product-page-droix]], [[anbernic-rg405v-case-product-page-droix]], [[anbernic-rg552-case-product-page-droix]] (source pages)
- Updated: [[anbernic]], [[anbernic-rg-nano]], [[index]]
- Archived: 6 files from `raw/ingest/product/droix-shop/`
- Notes: RG35XXSP is a clamshell (GBA SP-style) variant with magnetic closure and Hall switch auto-wake. RG405V runs Android 12 with Unisoc Tiger T618. RG552 case source page created but parent product anbernic-rg552 not yet onboarded.

## [2026-04-22] ingest | Phase 1 Batch 3: Anbernic product pages (8 new products onboarded)
- Created: [[anbernic-rg-40xxv]], [[anbernic-rg-arc-s]], [[anbernic-rg-cube]], [[anbernic-rg-nano]], [[anbernic-rg28xx]], [[anbernic-rg300x]], [[anbernic-rg353p]], [[anbernic-rg353ps]] (product hubs), [[anbernic-rg-40xxv-product-page-droix]], [[anbernic-rg-arc-s-product-page-droix]], [[anbernic-rg-cube-product-page-droix]], [[anbernic-rg-nano-product-page-droix]], [[anbernic-rg28xx-product-page-droix]], [[anbernic-rg300x-product-page-droix]], [[anbernic-rg353p-product-page-droix]], [[anbernic-rg353ps-product-page-droix]] (source pages)
- Updated: [[anbernic]], [[index]]
- Archived: 8 files from `raw/ingest/product/droix-shop/anbernic-*.md`
- Notes: Onboarded 8 new Anbernic products spanning budget retro handhelds. Range from keychain-sized RG Nano (75g, 1.54" screen) to RG Cube (Unisoc T820, Android 13, square 720x720 display). RG353P is dual-boot Android+Linux; RG353PS is Linux-only variant with less RAM. RG300X is legacy (Ingenic JZ4770, no wireless).

## [2026-04-22] ingest | Phase 1 Batch 2: Already-onboarded product pages (gpdstore-shop)
- Created: [[gpd-win-5-product-page-gpdstore]], [[gpd-pocket-4-product-page-gpdstore]], [[gpd-micropc-2-product-page-gpdstore]], [[gpd-win-5-battery-product-page-gpdstore]], [[gpd-win-5-case-product-page-gpdstore]], [[gpd-win-5-docking-station-product-page-gpdstore]], [[gpd-micropc-2-case-product-page-gpdstore]], [[gpd-pocket-4-4g-lte-module-product-page-gpdstore]], [[gpd-pocket-4-kvm-module-product-page-gpdstore]], [[gpd-pocket-4-protective-case-product-page-gpdstore]], [[gpd-pocket-4-rs-232-module-product-page-gpdstore]]
- Updated: [[gpd-win-5]], [[gpd-pocket-4]], [[gpd-micropc-2]], [[index]]
- Archived: 11 files from `raw/ingest/product/gpdstore-shop/`
- Notes: Completed Tier A (all already-onboarded products). GPDStore pages are brief listings with headline specs, in-box contents, and shipping info. Docking station page confirmed as same product as [[gpd-win-5-smart-dock]]. Pocket 4 Ryzen AI 9 HX 370 on pre-order ETA 30 April 2026.

## [2026-04-22] ingest | Phase 1 Batch 1: Already-onboarded product pages (droix-shop)
- Created: [[ayaneo-ag01-product-page-droix]], [[ayn-thor-product-page-droix]], [[ayn-thor-carrying-case-product-page-droix]], [[konkr-pocket-fit-product-page-droix]], [[onexplayer-onexfly-apex-product-page-droix]], [[ingest-progress]]
- Updated: [[ayaneo-ag01]], [[ayn-thor]], [[konkr-pocket-fit]], [[onexplayer-onexfly-apex]], [[index]]
- Archived: `raw/ingest/product/droix-shop/ayaneo-ag01.md`, `raw/ingest/product/droix-shop/ayn-thor.md`, `raw/ingest/product/droix-shop/thor-carrying-case.md`, `raw/ingest/product/droix-shop/konkr-pocket-fit.md`, `raw/ingest/product/droix-shop/onexplayer-onexfly-apex.md`
- Notes: Bulk ingestion Phase 1 start. Updated AG01 with full port specs. Updated AYN Thor with 4-model lineup (Lite/Base/Pro/Max) and dual AMOLED display details. Updated KONKR Pocket FIT with Snapdragon 8 Elite variant and 144Hz display. Updated ONEXFLY Apex with full I/O, controls, modular battery details.

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
