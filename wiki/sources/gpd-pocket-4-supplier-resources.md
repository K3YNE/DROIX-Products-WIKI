---
title: "GPD Pocket 4 Supplier Resources"
type: source
subtype: resource-firmware
slug: gpd-pocket-4-supplier-resources
brand: gpd
product: gpd-pocket-4
source_url: https://www.gpd.hk/gpdpocket4firmware
created: 2026-04-22
updated: 2026-04-22
tags: [resource-firmware, resource-bios, resource-driver, resource-tool, resource-manual, gpd]
---

## GPD Pocket 4 Supplier Resources

All resources from the [[gpd|GPD]] official firmware, driver & BIOS page. Applies to [[gpd-pocket-4]] (8840U, AI 9 365, and AI 9 HX 370 variants).

---

### Windows 10 / 11 Firmware

| Resource | Date | SHA1 | Notes | Download |
|----------|------|------|-------|----------|
| GPD Pocket 4 (8840U / 365 / 370) Windows 11 24H2 Home Firmware **(current)** | 2025-03-18 | `30B2D557AEB549ACDC6C36D4E1DE95F209614BBE` | Includes latest integrated graphics driver; resolves issue of internal screen not working when connecting to GPD G1. Covers all three APU variants. Reinstallation removes all data on drive C — back up first. SHA1 tool: [HashTools](https://www.binaryfortress.com/HashTools/Download/) | [Download](https://drive.google.com/file/d/1p4z9nrqFEqsZeJC3XSMZOb4L5WyorU43/view?usp=sharing) · [Installation Guide](https://drive.google.com/file/d/1lk__yZ55QZwLxYJbXSPltD4ZPYvjeiBD/view?usp=sharing) |

**Installation:** Reinstallation removes all data on drive C. Always back up data before proceeding.

---

### Manuals

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| GPD Pocket 4 Instruction Manual **(current)** | 2025-01-20 | PDF — answers about GPD Pocket 4 frequently asked questions | [Download](https://drive.google.com/file/d/1Uf5xnBRTJ5oCaYCYKjeghhMJC0fRjYJr/view?usp=sharing) |

---

### BIOS

| Resource | Version | Date | Applies To | Notes | Download |
|----------|---------|------|-----------|-------|----------|
| GPD Pocket 4 BIOS & EC Firmware **(current for AI 9 365/370)** | v2.10 BIOS + v1.13 EC | 2025-06-27 | AI 9 365 / AI 9 HX 370 only | Fixes touchscreen randomly malfunctioning when waking from sleep. Both EC and BIOS updates required. | [Download](https://drive.google.com/file/d/1BdFEi57OFLDmYv3l-5PZxJj4fFBA7rke/view?usp=drive_link) |
| GPD Pocket 4 BIOS & EC Firmware **(current for 8840U)** | v3.08 BIOS + v1.11 EC | 2025-08-21 | 8840U (FP8) only | Fixed issue where BIOS always displayed 8GB VRAM regardless of modifications. | [Download](https://drive.google.com/file/d/1ZN22u_4_5wCzaL21IJ-MBFnkCePxdMU8/view?usp=sharing) |

---

### Drivers

| Resource | Version | Date | Notes | Download |
|----------|---------|------|-------|----------|
| GPD Pocket 4 (8840U / 365 / 370) Drivers **(current)** | v4.2.0 | 2025-03-07 | Latest driver package for all three APU variants. After extracting, double-click `AutoInstallDrivers.bat` for automatic installation. | [Download](https://drive.google.com/file/d/1Loh1-PmlLJEBUv9lp7F0K9CSaZ853hir/view?usp=sharing) |
| 4G LTE Module Driver | — | 2023-09-19 | 4G LTE module driver package for Pocket 4. After extracting, double-click to execute the installation. | [Download](https://drive.google.com/file/d/12Bad5Nrt3Pp5Jad1ZqFi3ziAAHTP06Ah/view?usp=sharing) |

#### Updating AMD and Intel Drivers Manually

**AMD GPU Driver Update:**
1. Open [AMD Driver Download Page](https://www.amd.com/en/support/download/drivers.html)
2. Select the corresponding processor and click Search
3. Locate the driver with "WHQL Recommended" label and download/install

**AMD Chipset Driver Update:**
1. Open [AMD Driver Download Page](https://www.amd.com/en/support/download/drivers.html)
2. Follow steps and click "Submit"
3. Download/install drivers for your Windows version. Use "Previous Version" if latest is unstable.

**Intel Driver Update (Wi-Fi/Bluetooth only):**
1. Open [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html)
2. Download and install Intel® DSA — identifies and updates outdated Intel hardware drivers automatically

---

### Fingerprint Drivers

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| GPD DUO & GPD Pocket 4 Fingerprint Driver (Windows) | 2025-02-17 | Windows 11 Fingerprint Driver V5.2.69.24 WHQL for GPD DUO & Pocket 4 | [Download](https://drive.google.com/file/d/11GT_whG5Pldjwp_abVV9QcTT4WLV_lJE/view?usp=sharing) |
| Linux Fingerprint Driver for GPD DUO & GPD Pocket 4 | 2025-02-17 | Supported distros: Ubuntu, Debian, Fedora, Redhat, Kylin, UOS, Zhongke Fangde, Alibaba Cloud Workspace, etc. | [Ubuntu & Debian](https://github.com/ftfpteams/focaltech-linux-fingerprint-driver/tree/main/Ubuntu_Debian/x86) · [Fedora & Redhat](https://github.com/ftfpteams/focaltech-linux-fingerprint-driver/tree/main/Fedora_Redhat) · [UOS](https://github.com/ftfpteams/focaltech-linux-fingerprint-driver/tree/main/Uos) · [Install Tutorial](https://badb100d.com/2025/02/16/2025-02-16/) |

---

### Audio

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| DTS:X Audio Technology, 3D Sound Field | 2024-12-05 | After downloading, decompress and execute `DTS_install.bat` to install automatically | [Download](https://drive.google.com/file/d/1uDVXLAQDi8IJPaVwe-qujx2PITdZbNbx/view?usp=sharing) |

---

### Tools

| Resource | Version | Date | Notes | Download |
|----------|---------|------|-------|----------|
| GPD Pocket 4 HDMI IN Tool **(current)** | V2.1.9 | 2025-04-10 | HDMI IN video capture tool with KVM module support. Resolves the sound output issue. | [Download](https://drive.google.com/file/d/13wUIh_PnTBcRBQS_nDyMq1N4msA1zJUL/view?usp=sharing) |
| GPD Pocket 4 HDMI IN Tool (third-party: OBS) | — | — | Open Broadcaster Software — popular live broadcast tool with sound output support. For Linux: see [OBS download page](https://obsproject.com/download) | [obsproject.com](https://obsproject.com/download) |
| Pocket 4 Resolution Correction | — | 2025-01-18 | Adds more resolutions and resolves issue where only three resolutions display under Windows 11 after installing original Microsoft image. Right-click `GPD-P4-LCD_resolution.bat` and select "Run as administrator" | [Download](https://www.gpd.hk/filedownload/144102) |
| GPD Keyboard Assistant Tool | v1.06 | 2021-12-16 | Download and unzip, then double-click to run the installation | [Download](https://drive.google.com/file/d/1vo0IARTCvnmvVINl9_cxvMpL1zKNsfGw/view?usp=sharing) |

---

### Keyboard Firmware

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| Pocket 4 Keyboard Firmware Update **(current)** | 2025-01-16 | Adds keyboard backlight feature with three states: Off → On for 30 seconds then auto-off → Always On. Toggle with Fn + Spacebar. Default state on first boot is "On for 30 seconds then auto-off". | [Download](https://drive.google.com/file/d/1633qk8aLeg-9nbsNJ_JokwZNRks2pj3M/view?usp=sharing) |

---

### Handheld Front-end Tools

#### MotionAssistant v1.2.0.9 (current) — 2026-02-08

**Note:** The Winring0 driver used by MotionAssistant has been blocked by Microsoft and may be flagged as malicious. MotionAssistant uses this driver for TDP adjustment, hardware monitoring, and fan control. If these features malfunction, it is likely due to isolation by Windows Security Center.

Unzip Password: `123`

**Downloads:**
- [Portable Version](https://drive.google.com/file/d/1VgxU_Wt_VaVpN-MTkmdVye25mVvrorXY/view?usp=sharing)
- [Installer Version](https://drive.google.com/file/d/1YC6JLePydHL1NRDlxfZyx37Gi1InITZY/view?usp=sharing)
- [RTSS 736](https://drive.google.com/file/d/1tZmkLGyr2rOWBOgEhIBHGZT2Sakhspz9/view?usp=sharing)
- [Video Tutorials](https://www.youtube.com/watch?v=Gc94JVHOcFs)
- [Motion Assistant V1.2.0.8 + Power Mod 2.1.1](https://github.com/ThatUsernameAlreadyExist/Motion-Assistant-Power-Mod/releases/tag/1.2.0.8-2.1.1) (community shell mod by Alexander)

**v1.2.0.9 Changelog:** See [[gpd-win-5-supplier-resources]] for the full changelog (shared across all GPD products).

---

#### GPD Official Handheld Front-end Tool — GPDTool v1.45 (current) — 2026-04-13

[Download](https://drive.google.com/file/d/11Rmk4zknLFEquK_uJwuehsuL7sPYa_RO/view?usp=drive_link)

Download and extract the file, then run the installer directly. For issues: sales011@softwincn.com

**v1.45 Release Notes:** See [[gpd-win-5-supplier-resources]] for the full release notes (shared across all GPD products).

---

#### AMD Handheld Control v1.0.0 — 2026-02-04

[Portable Version](https://drive.google.com/file/d/1NQYLidkNZQOmWCn_wqKznFueiiyvXDDH/view?usp=sharing)

Power management and system monitoring tool for handheld gaming devices, developed by Deen0X. Exclusively supports AMD processor systems.

Bug reports: [Telegram community](https://t.me/AMDHandheldControl)

---

### Linux Firmware

| Resource | Notes | Download |
|----------|-------|----------|
| Ubuntu MATE for GPD Pocket 3 (1195G7) | Configuration changes include: frame buffer and Xorg display rotation, accelerometer support for automatic screen rotation, automatic touchscreen and stylus rotation, fractional scaling default (~1920x1200 effective), audio via HDaudio legacy driver, suspend via s2idle, scroll wheel emulation. No fingerprint reader support. Install script: `git clone https://github.com/wimpysworld/umpc-ubuntu.git && sudo ./umpc-ubuntu.sh enable` | [ubuntu-mate.org](https://ubuntu-mate.org/download/gpd_pocket_3/impish/) |
| Rufus — USB Drive Creation Utility | Useful for creating USB installation media, flashing BIOS from DOS, running low-level utilities | [rufus.ie](http://rufus.ie/en/) |

---

### SHA1 Checksums Summary

| File | SHA1 |
|------|------|
| Pocket 4 Windows 11 24H2 Firmware (2025-03-18) | `30B2D557AEB549ACDC6C36D4E1DE95F209614BBE` |
