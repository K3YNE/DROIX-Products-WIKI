---
title: AMD Radeon RX 7600M XT
type: entity
subtype: chipset
slug: amd-rx-7600m-xt
vendor: amd
family: RDNA 3 (mobile)
process_node: 6nm TSMC
created: 2026-04-21
updated: 2026-04-21
tags: [amd, gpu, rdna3, rx-7600m-xt, egpu, discrete]
---

# AMD Radeon RX 7600M XT

The AMD Radeon RX 7600M XT is a mobile discrete GPU in AMD's RDNA 3 family. It serves as the eGPU inside the [[ayaneo-ag01|AYANEO AG01]] Starship dock — the only discrete GPU currently tracked in this wiki.

## Key Specs

| Spec | Value |
|------|-------|
| Compute Units | 32 CUs (RDNA 3) |
| VRAM | 8GB GDDR6 |
| TGP | ~75–120W |
| Process | 6nm TSMC |

## Products Using This Chip

- [[ayaneo-ag01]] — AYANEO Starship eGPU dock

## Performance Context

The RX 7600M XT in the [[ayaneo-ag01]] was reviewed in the context of the [[amd-ryzen-ai-max|Strix Halo]] era: at 80–85W TDP, Strix Halo's integrated GPU approaches the performance of the 7600M XT, narrowing the value proposition of eGPU docks. The [[2025-06-25-ayaneo-ag01-review-youtube|DROIX AG01 review]] addressed this directly. See [[egpu-docking]] for the broader eGPU analysis.
