---
title: GPD WIN Max 2
type: product
slug: gpd-win-max-2
brand: gpd
category: handheld-pc
form_factor: handheld
platform: windows
created: 2026-04-22
updated: 2026-04-22
tags: [gpd, handheld, windows, amd, large-display]
---

# GPD WIN Max 2

The GPD WIN Max 2 is [[gpd|GPD]]'s large-format 10.1" Windows handheld gaming PC, refreshed annually. It features a built-in keyboard, touchscreen, and stylus support. The WIN Max 2021 is an earlier generation with the same form factor. Sold by [[droix|DROIX]] with a 2-year warranty.

## Yearly Models

| Year | CPU | GPU | RAM | Storage | Wi-Fi | Bluetooth |
|------|-----|-----|-----|---------|-------|-----------|
| 2021 | AMD Ryzen 7 6800U | Radeon 680M (12 CUs @ 2200 MHz) | Up to 32 GB LPDDR5 @ 6400 MT/s | Up to 2 TB PCIe NVMe | Wi-Fi 6 | 5.2 |
| 2022 (original) | AMD Ryzen 7 6800U | Radeon 680M (12 CUs @ 2200 MHz) | Up to 32 GB LPDDR5 @ 6400 MT/s | Up to 2 TB PCIe NVMe | Wi-Fi 6 | 5.2 |
| 2023 | AMD Ryzen 5 7640U / Ryzen 7 7840U | Radeon 760M / 780M | Up to 64 GB LPDDR5X @ 6400 MT/s | Up to 4 TB PCIe Gen 3 NVMe | Wi-Fi 6 | 5.2 |
| 2024 | AMD Ryzen 7 8840U (28W TDP) | Radeon 780M (12 CUs @ 2700 MHz) | Up to 64 GB LPDDR5X @ 6400 MT/s | Up to 4 TB PCIe 4.0 NVMe | Wi-Fi 6E | 5.3 |
| 2025 | AMD Ryzen AI 9 HX 370 / Ryzen 7 8840U | Radeon 890M / 780M | Up to 64 GB LPDDR5X @ 7500 MT/s | Up to 4 TB PCIe 4.0 NVMe | Wi-Fi 6E | 5.3 |

**Note:** The WIN Max 2021 product page shares identical specs to the 2022 original (both list Ryzen 7 6800U). The "2021" branding on GPDStore may be a naming convention for a pre-refresh model.

## Design & Build

- 10.1" touchscreen display with stylus support.
- Built-in QWERTY keyboard with trackpad.
- Larger form factor than the WIN 4 or WIN Mini — closer to a small laptop.
- OCuLink support from the 2023 model onward (used with [[gpd-g1]] eGPU).

## Resources

Keep this section current whenever a new firmware / BIOS / driver / tool release is ingested.

### WIN Max 2 Original (2022 — 6800U)

- **Firmware:** [[gpd-firmware-win11-24h2-shared]] — Windows 11 24H2 Home (2024-12-20). SHA1 `730BD7B9D989797488C1509E590085FD9941E80C`. Shared with 2023/2024 models. See also [[gpd-win-max-2-supplier-resources]].
- **BIOS (6800U):** [[gpd-win-max-2-bios-v1-05]] — BIOS V1.05 (2022-12-22). Fixes wireless screen projection failure and eGPU auto-connect. See also [[gpd-win-max-2-supplier-resources]].
- **Drivers:** [[gpd-win-max-2-drivers-v3-4]] — Drivers v3.4 (2024-05-07). Covers 6800U / 7640U / 7840U / 8840U. See also [[gpd-win-max-2-supplier-resources]].
- **Controller Firmware:** [[gpd-win-max-2-controller-firmware-v3-14]] — Gamepad/Keyboard-Mouse firmware v3.14/v1.23. See also [[gpd-win-max-2-supplier-resources]].
- **Touchpad Firmware:** [[gpd-win-max-2-touchpad-firmware-v1-0-3]] — Touchpad firmware v1.0.3 (6800U). See also [[gpd-win-max-2-supplier-resources]].
- **Display Calibration:** [[gpd-win-max-2-screen-calibration]] — ICM colour profiles (D65/D70). See also [[gpd-win-max-2-supplier-resources]].

### WIN Max 2 2023 & 2024 (7640U / 7840U / 8840U)

- **Firmware:** [[gpd-firmware-win11-24h2-shared]] — Windows 11 24H2 Home (2024-12-20). SHA1 `730BD7B9D989797488C1509E590085FD9941E80C`. See also [[gpd-win-max-2-2023-supplier-resources]].
- **BIOS:** [[gpd-win-max-2-2023-bios-v0-42]] — BIOS v0.42 (2024-10-23). Applies to 7640U, 7840U, 8840U. Fixes flickering screen. Device must be charging during upgrade. See also [[gpd-win-max-2-2023-supplier-resources]].
- **Drivers:** [[gpd-drivers-v4-1-0]] — Drivers v4.1.0 (2025-01-18). See also [[gpd-win-max-2-2023-supplier-resources]].
- **Manual:** [[gpd-win-max-2-2023-user-manual]]. See also [[gpd-win-max-2-2023-supplier-resources]].

### WIN Max 2 2025 (8840U / AI 9 HX 370)

- **Firmware:** [[gpd-firmware-win11-24h2-shared]] — Windows 11 24H2 Home (2024-12-20). SHA1 `730BD7B9D989797488C1509E590085FD9941E80C`. See also [[gpd-win-max-2-2025-supplier-resources]].
- **BIOS:** see [[gpd-win-max-2-2025-supplier-resources]] — no separate BIOS listed for 2025 model; see 2023/2024 page for applicable BIOS.
- **Drivers:** [[gpd-drivers-v4-1-0]] — Drivers V4.1.0 (2025-01-18). See also [[gpd-win-max-2-2025-supplier-resources]].
- **Manual:** [[gpd-win-max-2-2025-user-manual]]. See also [[gpd-win-max-2-2025-supplier-resources]].
- **Battery Icon Fix:** [[gpd-win-max-2-2025-battery-icon-fix]] — Fix for battery icon disappearing after AMD driver update (HX 370).

### Shared Tools & Drivers (all WIN Max 2 models)

- [[gpd-motionassistant-v1-2-0-9]] — MotionAssistant v1.2.0.9 (handheld front-end).
- [[gpd-gpdtool-v1-45]] — GPDTool v1.45 (official GPD handheld front-end).
- [[gpd-amd-handheld-control-v1-0-0]] — AMD Handheld Control v1.0.0.
- [[gpd-dtsx-audio]] — DTS:X Audio driver.
- [[gpd-win-max-2-fingerprint-driver-linux]] — CS1197 fingerprint driver for Linux.
- [[gpd-win-max-2-screen-calibration]] — Screen colour calibration ICM profiles.
- [[gpd-gamepad-test-v1-03]] — GamePad Test Calibration Tool V1.03 (2025 model).
- [[gpd-power-control-panel]] — Power Control Panel v2 (legacy, community).

## Reviews & Coverage

### Blog Reviews
- [[2023-03-28-gpd-win-max-2-2022-review-blog]] — GPDStore blog review of 2022 AMD model (6800U): emulation up to PS2/GameCube, modern AAA at low settings 30-40 FPS.
- [[2024-05-28-gpd-win-max-2-2024-review-blog]] — GPDStore blog review of 2024 model (8840U): PCMark 7,085; Cinebench SC 1,768 / MC 12,997.
- [[2025-01-24-gpd-win-max-2-2025-review-blog]] — GPDStore blog review of 2025 model (HX 370): PassMark 8,334; Forza 117 FPS @ 1080p; +32-45% over 6800U.
- [[2021-09-15-gpd-win-max-2021-review-blog]] — DROIX blog review of 2021 Intel model with benchmarks and emulator testing.
- [[2021-12-15-gpd-win-max-2021-amd-review-blog]] — DROIX blog review of 2021 AMD variant (Ryzen over Intel).
- [[2022-07-18-gpd-win-max-2-review-blog]] — DROIX blog review of WIN MAX 2 as work laptop and gaming handheld.

### Product pages
- [[gpd-win-max-2021-product-page-gpdstore]] — GPDStore listing (2021 model, out of stock).
- [[gpd-win-max-2-product-page-gpdstore]] — GPDStore listing (2022 original, out of stock).
- [[gpd-win-max-2-2023-product-page-gpdstore]] — GPDStore listing (2023 model, out of stock).
- [[gpd-win-max-2-2024-product-page-gpdstore]] — GPDStore listing (2024 model, out of stock).
- [[gpd-win-max-2-2025-product-page-gpdstore]] — GPDStore listing (2025 model, in stock).
- [[2022-10-05-gpd-win-max-2-6800u-review-blog]]
- [[2023-06-07-gpd-win-max-2-review-blog]]
- [[2023-08-16-gpd-win-max-2-review-blog]]

## Knowledge Base

- [[how-to-install-the-gpd-win-max-2-2025-4g-module]]
- [[how-to-replace-the-gpd-win-max-2-2024-2025-ssd-right-trigger-and-battery]]
- [[how-to-replace-the-gpd-win-max-2-display]]
- [[how-to-replace-the-keyboard-on-a-gpd-win-max-2]]
- [[gpd-win-max-2-2023-getting-started]] — Getting started guide for 2023 model (DROIX KB).

- [[gpd-win-max-2-getting-started]] — Getting started guide: inspection checklist, Windows/driver updates, software recommendations, accessories.
- [[gpd-win-max-2-faq]] — FAQ covering specs, versions, gaming performance, battery life, eGPU support.
- [[gpd-win-max-2-bios-update]] — BIOS update guide for 2022/2023/2024 models.
- [[gpd-win-max-2-2025-bios-update]] — BIOS update guide for 2025 HX 370 model.
- [[gpd-win-max-2-2025-4g-module-install]] — 4G module installation guide (2025 model, includes backplate swap).
- [[gpd-win-max-2-2025-battery-icon-fix]] — Fix for battery icon disappearing after AMD driver update (HX 370).
- [[gpd-win-max-2-keyboard-replacement]] — Video guide for keyboard replacement.
- [[gpd-win-max-2-display-replacement]] — Video guide for display replacement (2024/2025 models).
- [[gpd-win-max-2-ssd-trigger-battery-replacement]] — Video guide for SSD, right trigger, and battery replacement.
- [[gpd-recalibrate-controls]] — Joystick calibration tool for all GPD handhelds.
- [[how-to-update-the-gpd-win-max-2-touchpad-firmware]] — Touchpad firmware update and driver installation for the GPD WIN MAX 2.
- [[so-youve-just-bought-a-gpd-win-max-2]] — Getting started overview for new GPD WIN MAX 2 owners.

## Related

- [[gpd]] — Manufacturer.
- [[gpd-win-4]] — Smaller sliding-keyboard sibling.
- [[gpd-g1]] — Compatible eGPU dock (OCuLink).
- [[gpd-win-max-2-protective-case-product-page-gpdstore]] — Official leather case.
- [[gpd-win-max-2-4g-lte-add-on-product-page-gpdstore]] — 4G LTE module (2022/2024 models).
- [[gpd-protective-case-p2-max-win-max-2021-product-page-gpdstore]] — Shared case (P2 Max / Pocket 3 / WIN Max 2021).
- [[gpd-stylus-4096-pp-product-page-gpdstore]] — 4096-level pressure stylus (compatible).
- [[gpd-stylus-product-page-gpdstore]] — Stylus with metal buckle (compatible).
