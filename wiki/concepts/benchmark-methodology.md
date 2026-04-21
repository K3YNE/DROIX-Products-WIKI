---
title: Benchmark Methodology
type: concept
created: 2026-04-21
updated: 2026-04-21
sources: [2025-10-23-gpd-win-5-review-youtube, 2026-03-04-onexplayer-onexfly-apex-review-youtube, 2025-08-29-onexplayer-g1-review-youtube, 2025-11-07-ayaneo-flip-1s-ds-review-youtube, 2025-05-23-ayaneo-pocket-ace-review-youtube, 2025-07-18-ayaneo-pocket-s2-review-youtube, 2026-03-13-ayn-odin-3-review-youtube, 2026-01-27-ayn-thor-review-youtube, 2025-11-14-konkr-pocket-fit-review-youtube, 2025-07-02-anbernic-rg-slide-review-youtube, 2025-06-25-ayaneo-ag01-review-youtube, gpd-win-5-blog-review]
tags: [benchmarks, testing, methodology, geekbench, 3dmark, cinebench]
---

# Benchmark Methodology

[[droix|DROIX]] uses a consistent benchmarking approach across reviews, enabling meaningful cross-device comparisons. Results are always presented alongside multiple devices for context.

## Synthetic Benchmarks

### CPU Performance
- **Geekbench 5 / Geekbench 6** — single-core and multi-core scores. Used across both Android and Windows devices.
- **Cinebench R23 / Cinebench 2024** — CPU rendering benchmark. Windows devices only.
- **PassMark** — general system performance. Windows devices.

### GPU / Graphics Performance
- **3DMark Wildlife Extreme** — primary GPU benchmark for Android devices
- **3DMark Time Spy** — primary GPU benchmark for Windows devices
- **3DMark Night Raid** — lighter GPU benchmark for Windows devices
- **3DMark Fire Strike** — additional GPU benchmark for Windows devices

### Overall System
- **AnTuTu** — overall device score for Android handhelds
- **PCMark** — overall system benchmark for Windows devices

## Gaming Benchmarks (Windows)

Real-world game tests at various resolutions and TDP settings:

- **Forza Horizon 5** — open-world racing, good GPU stress test
- **Shadow of the Tomb Raider** — built-in benchmark, widely used for comparisons
- **Cyberpunk 2077** — demanding title used to test performance ceilings

Tests are run at multiple resolutions and TDP levels to show the performance envelope of each device.

## Battery Testing

Standardized stress tests at maximum load:

- **Android:** AnTuTu stress test loop at full brightness + max performance mode
- **Windows:** Cinebench loop at full brightness + max performance mode

This worst-case approach gives a battery floor — real-world gaming battery life will always be better.

## Thermal & Acoustic Testing

- **Fan noise** — measured in dB, reported during load testing
- **Surface temperature** — measured in degrees Celsius on the device exterior during sustained load

## TDP-Scaled Testing (Windows)

For [[windows-handheld-gaming|Windows handhelds]], benchmarks are often run at multiple TDP levels (e.g., 15W, 28W, 45W, 80W) to show the performance-per-watt curve. This is critical information since TDP selection is the primary performance lever users have.

## Cross-Device Comparison

A defining characteristic of [[droix|DROIX]] reviews: benchmark results are never shown in isolation. Every score is placed alongside results from other devices in the same category, giving viewers immediate context for how a new device compares to existing options.
