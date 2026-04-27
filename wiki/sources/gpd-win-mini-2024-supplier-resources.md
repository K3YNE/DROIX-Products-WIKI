---
title: "GPD WIN Mini / 2024 Supplier Resources"
type: source
subtype: resource-firmware
slug: gpd-win-mini-2024-supplier-resources
brand: gpd
product: gpd-win-mini
source_url: https://www.gpd.hk/gpdwinminifirmwaredriver
created: 2026-04-22
updated: 2026-04-22
tags: [resource-firmware, resource-bios, resource-driver, resource-tool, gpd]
---

Official firmware, driver, BIOS, and tool resources for the GPD WIN Mini and WIN Mini 2024 (8840U / 7840U / 7640U variants). Retrieved from the GPD official resource page on 2026-04-21.

Applies to: [[gpd-win-mini]]

**Individual source pages:** [[gpd-win-mini-bios-v2-18]], [[gpd-win-mini-controller-firmware-v5-04]], [[gpd-win-mini-firmware-win11-24h2]], [[gpd-win-mini-user-manual]], [[gpd-drivers-v4-1-0]], [[gpd-motionassistant-v1-2-0-9]], [[gpd-gpdtool-v1-45]], [[gpd-amd-handheld-control-v1-0-0]], [[gpd-dtsx-audio]], [[gpd-power-control-panel]].

---

## Windows 11 Firmware

| Resource | Date | SHA1 | Download |
|---|---|---|---|
| WIN Mini (8840U / 7840U / 7640U) Windows 11 24H2 Home Firmware **(current)** | 2025-01-18 | `12DD1623F9515C6F8ACA77CF42AFF6C6CF9A0542` | [Download](https://drive.google.com/file/d/1ZTyRcPTNitTTPaw__XtFkl1wjatJA4h3/view?usp=drive_link) |
| WIN Mini (8840U / 7840U / 7640U) Windows 11 Home Firmware | 2024-03-08 | — | [Download](https://drive.google.com/file/d/1LY44bRqhijfFIsHbGPV0BARA8DGwy6i7/view?usp=sharing) |

**Installation notes:** This is a full flash firmware (Windows 11 integrated with drivers). Instructions are included in the compressed package. **Warning: Reinstallation removes all data on drive C. Back up before proceeding.**

SHA1 Verification Tool: [HashTools](https://www.binaryfortress.com/HashTools/Download/)
Installation Guide: [View](https://drive.google.com/file/d/1lk__yZ55QZwLxYJbXSPltD4ZPYvjeiBD/view?usp=sharing)

---

## Drivers & BIOS

### Driver Package

| Resource | Version | Date | Download |
|---|---|---|---|
| WIN Mini (8840U / 7840U / 7640U) Drivers **(current)** | v4.1.0 | 2024-05-07 | [Download](https://drive.google.com/file/d/1nl_pGzcp9JmTBiG0sGhTmv_OuGkqBh8o/view?usp=drive_link) |

**Installation:** Extract files, then double-click `AutoInstallDrivers.bat` for automatic installation.

### Updating AMD / Intel Drivers Independently

The official driver package may become outdated after a period of device usage. GPD recommends updating drivers manually when needed:

**AMD GPU Driver:**
1. Go to the [AMD driver download page](https://www.amd.com/en/support/download/drivers.html).
2. Select the corresponding processor and click Search.
3. Expand drivers for your pre-installed Windows version; locate the "WHQL Recommended" label and download.

**AMD Chipset Driver:**
1. Go to the [AMD driver download page](https://www.amd.com/en/support/download/drivers.html).
2. Follow the on-screen steps and click Submit.
3. If the version is unstable, click "Previous Version" for a more stable release.

**Intel Wi-Fi / Bluetooth Driver (Intel DSA):**
1. Open [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
2. Download and install Intel DSA. It identifies Intel hardware driver versions and upgrades automatically.

### BIOS

| Resource | Version | Date | Notes | Download |
|---|---|---|---|---|
| WIN Mini BIOS **(current)** | V2.18 | 2023-12-14 | Adds PCIe 3.0 speed support for SSDs. Device must be charging during upgrade. | [Download](https://drive.google.com/file/d/1SHT6ReLbf9pfOCdd1jkbuMDPqGXdB9Y3/view?usp=sharing) |

EFI Upgrade file: [Download](https://drive.google.com/file/d/1CJU6eN7zNG8Xa5FH6ZbeED4qmbc2cwxa/view?usp=sharing)

### Additional Drivers

| Resource | Date | Notes | Download |
|---|---|---|---|
| DTS:X Audio Driver | 2024-02-19 | Right-click `DTS_install.bat` → "Run as administrator" to install; `DTS_uninstall.bat` to uninstall. | [Download](https://drive.google.com/file/d/1UpVU3lOfRa0AL4hZiHgSNkumc6bZpESY/view?usp=sharing) |
| WIN Mini Controller Firmware v5.04 & v5.10 | 2024-01-22 | Double-click to execute. Keep device in controller mode. | [Download](https://drive.google.com/file/d/1K4J8nZTF9CIKg4E0yhhKv2zgeSRUmuXG/view?usp=sharing) |
| Resolution Options Fix | 2023-11-21 | Resolves missing resolution options after OS reinstall or driver update. Extract and run batch file. | [Download](https://drive.google.com/file/d/1hemMDj7zXXaDMRmAf46Y1MOUUcP-TmVi/view?usp=sharing) |
| 4G LTE Module Driver | 2023-09-19 | Extract and double-click to install. | [Download](https://drive.google.com/file/d/12Bad5Nrt3Pp5Jad1ZqFi3ziAAHTP06Ah/view?usp=sharing) |

---

## Handheld Front-end Tools

### MotionAssistant v1.2.0.9 (current)

**Release date:** 2026-02-08

**Downloads:**
- Portable Version (no install required, unzip and run): [Download](https://drive.google.com/file/d/1VgxU_Wt_VaVpN-MTkmdVye25mVvrorXY/view?usp=sharing) — Unzip Password: `123`
- Installer Version: [Download](https://drive.google.com/file/d/1YC6JLePydHL1NRDlxfZyx37Gi1InITZY/view?usp=sharing)
- RTSS 736: [Download](https://drive.google.com/file/d/1tZmkLGyr2rOWBOgEhIBHGZT2Sakhspz9/view?usp=sharing)
- Video Tutorials: [YouTube](https://www.youtube.com/watch?v=Gc94JVHOcFs)
- Motion Assistant V1.2.0.8 + Power Mod 2.1.1 (third-party UI mod by Alexander): [GitHub](https://github.com/ThatUsernameAlreadyExist/Motion-Assistant-Power-Mod/releases/tag/1.2.0.8-2.1.1)

**Known issue:** The Winring0 driver used by MotionAssistant for TDP adjustment, hardware monitoring, and fan control has been flagged as malicious by Microsoft. If these features malfunction, check Windows Security Center for isolation.

**V1.2.0.9 Changelog:**
1. Adapted the gyroscope in the Legion Go 2 device body (controller gyroscope and fan control not yet adapted).
2. Adapted support for various AMD rebranded models (recently released).
3. Added "Disable Tablet Mode" option in Advanced Settings — Tablet Mode auto-off on next launch.
4. Added OSD toggle hotkey in RTSS OSD settings. Temperature display added to simplified mode.
5. Added 30-second TDP reset cycle — reapplies current TDP if abnormal decrease detected. Added TDP ±5 hotkeys.
6. Optimized Win5 keyboard key logic: press to open on-screen keyboard, press again to close.
7. Optimized "Optimize CPU Frequency" option — maximum frequency restored when option is disabled.
8. Improved Dark Mode control display; title bar changed to a darker color.
9. Optimized gyroscope simulation after hibernation resume — fixed simulation failure on wake-up.
10. Optimized hotkey detection by shortening judgment interval. Brightness hotkeys now adjust by ±10.
11. Specified ze_loader.dll version as 1.11.0. For Intel models unable to lock GPU frequency, install Intel 6647 version iGPU driver first.
12. Fixed issue where power limit was locked at 65W when GPD Win5 powered via USB-C port.
13. Corrected text display issues. Fixed OSD monitoring display when hardware monitoring was off.
14. Fixed issue where LT/RT could not be properly registered as hotkeys.
15. Fixed potential freeze when setting TDP consecutively.
16. Fixed issue where certain game profile options (e.g. CPU frequency limits) were not applied automatically.
17. Fixed frame locking failure in some game profiles. Frame locking now uses RTSS process-specific configuration.
18. Fixed crash when refreshing the tray icon.

**Power Mod 2.1.1 additions (by Alexander):**
- Fixed saving settings when installed in Program Files
- Improved support for very high DPI displays (>175%)
- Scrollbar visibility follows OS settings
- Added localization via ini files (Simplified Chinese, Spanish, Korean, Japanese)
- Added option to hide tabs in left menu (Advanced Settings → Appearance)
- Added gamepad navigation: shoulder buttons switch tabs, D-pad/left stick navigate, A=select, B=back, right stick=scroll, Start=collapse/expand menu
- Added option to swap X and Y axes (for Win 4)
- Fixed non-working keyboard hotkeys

### GPDTool v1.45 (current)

**Release date:** 2026-04-13

**Download:** [Download](https://drive.google.com/file/d/11Rmk4zknLFEquK_uJwuehsuL7sPYa_RO/view?usp=drive_link)

**Installation:** Download and extract, then run the installer directly. For issues, contact: sales011@softwincn.com

**GPD TOOL v1.45 Release Notes:**

Feature Additions:
- UI/UX: Full visual overhaul and UI beautification.
- Performance: Integrated CPU frequency capping and real-time CPU/GPU status monitoring.
- Power Management: AC/DC power state linkage (Auto-switch between High-Performance and Low-Power modes).
- RTSS Integration: Added horizontal parameter display toggle and dynamic font size scaling slider.
- Input: Independent OSK (On-Screen Keyboard) full-screen invocation; custom hotkey mapping for OSK; D-Pad mirrors Left-Joystick functionality.

Optimizations:
- Thermal: Refined fan control algorithms for Auto and Manual modes.
- System: Disabled Windows right-edge gestures by default upon installation (toggleable via System Settings).
- Deployment: Added automated software whitelisting and official Windows Uninstaller support.

Bug Fixes:
- Compatibility: Resolved service initialization failures on specific hardware models.
- Anti-Cheat: Fixed false positive triggers for Easy Anti-Cheat (EAC).
- Hardware: Fixed WIN 5 Controller Switch key invocation (Note: Requires Firmware v1.11).

### AMD Handheld Control v1.0.0

**Release date:** 2026-02-04

**Download (Portable):** [Download](https://drive.google.com/file/d/1NQYLidkNZQOmWCn_wqKznFueiiyvXDDH/view?usp=sharing)

Power management and system monitoring tool for handheld gaming devices developed by Deen0X. Exclusively supports AMD processors. Supports: English, French, German, Spanish, Italian, Russian, Simplified Chinese, Traditional Chinese, Japanese, Korean, Polish, Portuguese (Brazil), Turkish, Czech.

Bug reports: [Telegram](https://t.me/AMDHandheldControl)

### WinControls v1.16

**Release date:** 2024-12-26

**Download:** [Download](https://drive.google.com/file/d/1odg796V28sIAN1-SBnAZFSi7wInfKTFl/view?usp=sharing) — Unzip Password: `123`

Tutorial: [Download tutorial](http://www.gpd.hk/filedownload/88998)

WIN Mini grip customization tool. Fixes issue with grip mapping key defaulting in mouse mode.

### GamePad Test Calibration Tool V1.02

**Release date:** 2022-09-02

**Download:** [Download](https://www.gpd.hk/filedownload/89292)

Tool for WIN 4/Mini grip back button mapping, programming, and vibration adjustment.

### Power Control Panel v2

**Release date:** 2022-09-02

**Download:** [Download](https://drive.google.com/file/d/1bITmR1WxqqRmxRkoFzjnSMj1zHYElpXY/view?usp=sharing)

**Requirements:** .NET 6.0 desktop runtime ([download](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-6.0.10-windows-x64-installer)) OR self-contained zip in releases.

Compatible devices (Windows only): Win 2, Win 3, Win 4, Win Max 2020, Win Max 2021 Intel/AMD, Win Max 2 1260p, Win Max 2 6800U, Pocket 2, Pocket 3.

Note: This tool is a community-developed work in progress.

---

## Documentation & Reference

| Resource | Date | Notes | Download |
|---|---|---|---|
| WIN Mini Q & A | 2023-08-10 | PDF with frequently asked questions. | [Download](https://drive.google.com/file/d/1VX_cry_PoXPiGzehmf5uc_mtGiSZhIu0/view?usp=drive_link) |
| WIN Mini User Manual | 2023-08-10 | PDF with function key and port descriptions. | [Download](https://drive.google.com/file/d/1EiD-QKLuLQP3Uap3gUxbaRhQDwu__vuH/view?usp=drive_link) |

---

## 3D Printing Files

| Resource | Date | Notes | Download |
|---|---|---|---|
| 3D Files for WIN Mini C and D Shell | 2023-11-03 | C-side and D-side outer shell. Users can modify or CNC machine. | [Download](https://drive.google.com/file/d/1-98hcTwsny1eC5ckBRF9QoTNMIAKS6fA/view?usp=sharing) |
| 3D File for WIN Mini Grip | 2023-12-28 | 3D file for the WIN Mini grip. | [Download](https://drive.google.com/file/d/1Wfz4i1WPdPR7CN-9lCbQSZt2Me--iK2P/view?usp=sharing) |

---

## GPD OS / Linux Firmware

| Resource | Date | Notes | Download |
|---|---|---|---|
| Bazzite (Fedora Atomic + SteamOS Gaming Mode) | 2024-08-21 | Fedora-based SteamOS alternative with Handheld Daemon pre-installed. [Documentation](https://universal-blue.discourse.group/docs?topic=2418) | [bazzite.gg](https://bazzite.gg/) |
| GPD OS (WIN Max 2 6800U) — Manjaro/SteamOS | 2022-12-13 | Linux Kernel 6.0, Manjaro desktop + Steam OS game mode. Use balenaEtcher to flash. First boot: connect Wi-Fi, launch Steam before switching to Deck GamePad UI. [Setup video](https://youtu.be/aekVivINoOQ) | [Mirror](https://mirror.fkardame.com/Linux/Images/GPD/) |
| balenaEtcher (Portable) | 2022-12-13 | Image writing tool. Supported formats: img, iso, zip, bz2, dsk, etch, gz, hddimg, raw, xz. | [balena.io](https://www.balena.io/etcher/) |

---

## SSD Installation

Video guide: How To Replace The SSD on GPD WIN Mini (linked from official resource page).
