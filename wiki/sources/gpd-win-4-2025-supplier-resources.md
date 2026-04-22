---
title: "GPD WIN 4 2025 Supplier Resources"
type: source
subtype: resource-firmware
slug: gpd-win-4-2025-supplier-resources
brand: gpd
product: gpd-win-4
source_url: https://www.gpd.hk/gpdwin42025firmwaredriver
created: 2026-04-22
updated: 2026-04-22
tags: [resource-firmware, resource-bios, resource-driver, resource-tool, resource-manual, gpd]
---

## GPD WIN 4 2025 Supplier Resources

All resources from the [[gpd|GPD]] official firmware & driver page. Applies to [[gpd-win-4]] (2025 model with 8840U and AI 9 HX 370 APUs).

---

### Windows 11 Firmware

| Resource | Date | SHA1 | Notes | Download |
|----------|------|------|-------|----------|
| GPD WIN 4 2025 (8840U / 370) Windows 11 24H2 Home Firmware **(current)** | 2024-12-20 | `730BD7B9D989797488C1509E590085FD9941E80C` | Covers both 8840U and AI 9 HX 370 variants. Includes integrated Windows 11 drivers. Reinstallation removes all data on drive C — back up first. SHA1 tool: [HashTools](https://www.binaryfortress.com/HashTools/Download/) | [Download](https://drive.google.com/file/d/1vr_seeh5rmQUe-Ez49htZ63ykrkyHT4x/view?usp=sharing) · [Installation Guide](https://drive.google.com/file/d/1lk__yZ55QZwLxYJbXSPltD4ZPYvjeiBD/view?usp=sharing) |

**Installation:** Reinstallation removes all data on drive C. Always back up data before proceeding.

---

### Manuals

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| GPD WIN 4 (2025) User Manual **(current)** | 2025-01-20 | PDF — WIN 4 (2025) function keys and ports description | [Download](https://drive.google.com/file/d/1ZmWE0g86tDTDCX_V7lhdR1M0rEcPuFgw/view?usp=sharing) |

---

### BIOS

| Resource | Version | Date | Applies To | Notes | Download |
|----------|---------|------|-----------|-------|----------|
| GPD WIN 4 BIOS **(current for AI 9 HX 370)** | v0.14 | 2026-01-27 | AI 9 HX 370 only | Format USB drive to FAT32, place BIOS file on USB drive, power on and press F7 to select USB boot and flash BIOS. Keep device on charge. WinRAR decompression password: `123` | [Download](https://drive.google.com/file/d/1hr2732KTjdowesKg2WsqJ_l6mwJVGV5z/view?usp=sharing) |
| GPD WIN 4 BIOS **(current for 8840U)** | v0.04 | 2025-09-28 | 8840U only | Format USB drive to FAT32, place BIOS file on USB drive, power on and press F7 to select USB boot and flash BIOS. Keep device on charge. | [Download](https://drive.google.com/file/d/1Q8KpdqiPj-dUVlN-S7UWyPsJC4qGZWpX/view?usp=drive_link) |

---

### Drivers

| Resource | Version | Date | Notes | Download |
|----------|---------|------|-------|----------|
| GPD WIN 4 2025 (8840U / 370) Drivers **(current)** | V4.1.0 | 2025-01-18 | Latest driver package. After extracting, double-click `AutoInstallDrivers.bat` for automatic installation. | [Download](https://drive.google.com/file/d/1nl_pGzcp9JmTBiG0sGhTmv_OuGkqBh8o/view?usp=drive_link) |

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

### Audio

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| DTS:X Audio Technology, 3D Sound Field | 2024-12-24 | After downloading, decompress and execute `DTS_install.bat` to install automatically | [Download](https://drive.google.com/file/d/1XYJ61YhmMUCBburRNxQVJm4Tra1kApv8/view?usp=sharing) |

---

### Tools

| Resource | Version | Date | Notes | Download |
|----------|---------|------|-------|----------|
| WinControls **(current)** | v1.16 | 2024-12-26 | WIN 4 grip customization tool. Fixed issue with grip mapping key defaulting to mouse mode. Tutorial: [Download](http://www.gpd.hk/filedownload/88998). Unzip Password: `123` | [Download](https://drive.google.com/file/d/1odg796V28sIAN1-SBnAZFSi7wInfKTFl/view?usp=sharing) |
| GPD WIN 4 Grip 3D Printing File | — | 2023-04-03 | 3D printing file for WIN 4 handle with detailed instructions inside | [Download](https://drive.google.com/file/d/1xmDOZaLhpdVo5kin6nyQjQIAGo-gNk_c/view?usp=sharing) |

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

Power management and system monitoring tool for handheld gaming devices, developed by Deen0X. Exclusively supports AMD processor systems. Supports: English, French, German, Spanish, Italian, Russian, Simplified Chinese, Traditional Chinese, Japanese, Korean, Polish, Portuguese (Brazil), Turkish, and Czech.

Bug reports: [Telegram community](https://t.me/AMDHandheldControl)

---

#### Power Control Panel — 2022-09-02 (legacy)

[Download](https://drive.google.com/file/d/1bITmR1WxqqRmxRkoFzjnSMj1zHYElpXY/view?usp=sharing)

Compatible Devices (Windows only): Win 2, Win 3, Win 4, Win max 2020, Win Max 2021 Intel/AMD, Win Max 2 1260p, Win Max 2 6800U, Pocket 2, Pocket 3. Requires [.NET 6.0 desktop runtime](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-6.0.10-windows-x64-installer).

---

### GPD OS / Alternative OS Firmware

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| Bazzite (Fedora Atomic Desktop + Steam OS Gaming Mode) | 2024-08-21 | Custom image on Fedora Atomic Desktops with Steam Deck gaming client. TDP control via Handheld Daemon (pre-installed) or Decky Loader plugin. See [community docs](https://universal-blue.discourse.group/docs?topic=2418). | [bazzite.gg](https://bazzite.gg/) |
| GPD OS (WIN Max 2 6800U) Firmware | 2022-12-13 | Manjaro/SteamOS-like Linux by Furkan Kardame. Linux Kernel 6.0. Use balenaEtcher to install. | [Download](https://mirror.fkardame.com/Linux/Images/GPD/) |
| balenaEtcher Image Disk Writing Tool (Portable Edition) | 2022-12-13 | Supported formats: img, iso, zip, bz2, dsk, etch, gz, hddimg, raw, xz | [balena.io/etcher](https://www.balena.io/etcher/) |

---

### SHA1 Checksums Summary

| File | SHA1 |
|------|------|
| WIN 4 2025 Windows 11 24H2 Firmware (2024-12-20) | `730BD7B9D989797488C1509E590085FD9941E80C` |
