---
title: Benchmark Methodology
type: concept
created: 2026-04-21
updated: 2026-04-21
sources: [gpd-win-5-review.md, onexfly-apex-review.md, onexplayer-g1-review.md, ayaneo-flip-1s-ds-review.md, ayaneo-pocket-ace-review.md, ayaneo-pocket-s2-review.md, ayn-odin-3-review.md, ayn-thor-review.md, konkr-pocket-fit-review.md, anbernic-rg-slide-review.md, ayaneo-ag01-review.md]
tags: [benchmarks, testing, methodology, geekbench, 3dmark, cinebench]
---

# Benchmark Methodology

[[DroiX]] uses a consistent benchmarking approach across reviews, enabling meaningful cross-device comparisons. Results are always presented alongside multiple devices for context.

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

A defining characteristic of [[DroiX]] reviews: benchmark results are never shown in isolation. Every score is placed alongside results from other devices in the same category, giving viewers immediate context for how a new device compares to existing options.
