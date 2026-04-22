---
title: "GPD MicroPC Supplier Resources"
type: source
subtype: resource-firmware
slug: gpd-micropc-supplier-resources
brand: gpd
product: gpd-micro-pc
source_url: https://www.gpd.hk/gpd_micropc_firmware_driver_bios
created: 2026-04-22
updated: 2026-04-22
tags: [resource-firmware, resource-bios, resource-driver, gpd]
---

Supplier resource page for the GPD MicroPC (original model), extracted from the GPD official firmware/driver/BIOS page. The MicroPC uses an Intel Celeron N4100. Retrieved 2026-04-21.

**BIOS archive decompression password:** 123456

## Windows Firmware

| Resource | Version / Date | Changelog | Download |
| --- | --- | --- | --- |
| MicroPC_RS5_X64_20200602_user-EN **(current)** | 2020-06-02 | Latest Windows firmware with integrated hardware drivers. No need to install drivers separately. Tutorial included in archive. | [Download](https://drive.google.com/file/d/1yOrtBo8DI66KeJBscwArkAzEXV4ue5PC/view?usp=sharing) |
| GPD MicroPC Windows Firmware 20190601 | 2019-06-01 | Earlier firmware with integrated hardware drivers. Tutorial included. | [Download](https://drive.google.com/open?id=1cCaRiQdkU_w16PuroUN45soBN9wr6-YS) |

## Linux Firmware

| Resource | Version / Date | Notes | Download |
| --- | --- | --- | --- |
| Ubuntu MATE for GPD MicroPC **(current)** | — | Includes display rotation, accelerometer support, fractional scaling (~1280×720 effective), HDaudio driver, s2idle suspend, scroll wheel emulation, Tear-Free rendering, double-size console font. No fingerprint reader support. Run `umpc-ubuntu.sh enable`. | [Download](https://ubuntu-mate.org/download/gpd_pocket_3/impish/) |

## Drivers & Tools

| Resource | Version / Date | Notes | Download |
| --- | --- | --- | --- |
| GPD MicroPC Driver **(current)** | — | Also supports Pocket 2, P2 Max, WIN 2. Not compatible with Windows 10 1607. | [Download](https://drive.google.com/file/d/1JAIVHNnEjjcQUASOaCR6U96NEY34X3wm/view?usp=sharing) |
| AMR Firmware (factory default touchpad restore) | — | Restores the MicroPC touchpad to default factory settings. Use if "GPD Micro PC touchpad firmware 20190618" was installed and you want to revert. | [Download](https://drive.google.com/open?id=1x23ZsNrbnDcfPO5puKdb6JSiqpZJa0eG) |

## BIOS

| Resource | Version / Date | Changelog | Download |
| --- | --- | --- | --- |
| MicroPC BIOS & EC **(current)** | v4.18 / EC v4.08 — 2023-09-21 | **EC upgrade first:** Format USB as Fat32, copy MicroPC_EC_V4.08 folder contents to USB root, insert into MicroPC, power on, press Fn+F7 for boot menu, select USB. **BIOS upgrade:** Copy MicroPC.4.18.exe from MicroPC.BIOS.V4.18\AfuWin to desktop, right-click and run as administrator. If error occurs, do not turn off — end DOS process in Task Manager and retry. Decompression Password: 123456. | [Download](https://drive.google.com/file/d/1IO86RNOBS6kJyppdWE4h1CnyGsNrzF6s/view?usp=sharing) |
