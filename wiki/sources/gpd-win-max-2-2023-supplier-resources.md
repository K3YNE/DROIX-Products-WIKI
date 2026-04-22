---
title: "GPD WIN Max 2 2023 & 2024 Supplier Resources"
type: source
subtype: resource-firmware
slug: gpd-win-max-2-2023-supplier-resources
brand: gpd
product: gpd-win-max-2
source_url: https://www.gpd.hk/gpdwinmax22023firmwaredriver
created: 2026-04-22
updated: 2026-04-22
tags: [resource-firmware, resource-bios, resource-driver, resource-tool, gpd]
---

Official firmware, driver, BIOS, and tool resources for the GPD WIN Max 2 2023 and 2024 models (8840U / 7840U / 7640U / 6800U variants). Retrieved from the GPD official resource page on 2026-04-21.

Applies to: [[gpd-win-max-2]]

Note: This page covers the 2023/2024 refresh models. For the original GPD WIN Max 2 (6800U only), see [[gpd-win-max-2-supplier-resources]].

---

## Windows 11 Firmware

| Resource | Date | SHA1 | Download |
|---|---|---|---|
| WIN Max 2 (8840U / 7840U / 7640U / 6800U) Windows 11 24H2 Home Firmware **(current)** | 2024-12-20 | `730BD7B9D989797488C1509E590085FD9941E80C` | [Download](https://drive.google.com/file/d/1vr_seeh5rmQUe-Ez49htZ63ykrkyHT4x/view?usp=sharing) |
| WIN Max 2 (8840U / 7840U / 7640U / 6800U) Windows 11 Home Firmware | 2024-03-08 | — | [Download](https://drive.google.com/file/d/1LY44bRqhijfFIsHbGPV0BARA8DGwy6i7/view?usp=drive_link) |

**Installation notes:** Full flash firmware (Windows 11 integrated with drivers). Instructions are included in the compressed package. **Warning: Reinstallation removes all data on drive C. Back up before proceeding.**

SHA1 Verification Tool: [HashTools](https://www.binaryfortress.com/HashTools/Download/)
Installation Guide: [View](https://drive.google.com/file/d/1lk__yZ55QZwLxYJbXSPltD4ZPYvjeiBD/view?usp=sharing)

---

## Drivers & BIOS

### Driver Package

| Resource | Version | Date | Download |
|---|---|---|---|
| WIN Max 2 (8840U / 7840U / 7640U / 6800U) Drivers **(current)** | v4.1.0 | 2025-01-18 | [Download](https://drive.google.com/file/d/1nl_pGzcp9JmTBiG0sGhTmv_OuGkqBh8o/view?usp=sharing) |

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
| WIN Max 2 (2023 & 2024) BIOS **(current)** | v0.42 | 2024-10-23 | Applicable to WIN Max 2 (7640U, 7840U, 8840U). Device must be charging during upgrade. Resolves flickering screen issue on some displays. | [Download](https://drive.google.com/file/d/1SYoew6sO0NW1Z4rTsy1q2qHHpttJ4iKL/view?usp=sharing) |

### Controller / Keyboard Firmware

| Resource | Version | Date | Notes | Download |
|---|---|---|---|---|
| WIN Max 2 2023 Gamepad/Keyboard-Mouse Firmware **(current)** | v3.14 / v1.23 | 2023-12-15 | Applicable to WIN Max 2 (6800U, 7640U, 7840U). After upgrade, adjust dead zones through WinControls V1.15. Upgrade instructions included. | [Download](https://drive.google.com/file/d/1A-KtimY3wZbTgzh5zmb4RrhQj6zTVIZA/view?usp=sharing) |

### Additional Drivers

| Resource | Date | Notes | Download |
|---|---|---|---|
| CS1197 Fingerprint Driver for Linux | 2025-02-17 | Applies to all versions of WIN Max 2. | [GitHub](https://github.com/ericlinagora/libfprint-CS9711) |
| DTS:X Audio Driver | 2024-02-19 | Right-click `DTS_install.bat` → "Run as administrator" to install; `DTS_uninstall.bat` to uninstall. | [Download](https://drive.google.com/file/d/1UpVU3lOfRa0AL4hZiHgSNkumc6bZpESY/view?usp=sharing) |
| WIN Max 2 Screen Color Calibration File | 2025-05-15 | ICM profiles in D65 and D70 color temperatures. See installation steps below. | [Download](https://drive.google.com/file/d/1k5Ci2eJSOT7iJARbb1g4WXsevpUp4NYJ/view?usp=sharing) |

**Screen Color Calibration — ICM Profile Installation (Windows):**

The files are in .icm format (Windows only). Available in two variants:
- **D65** (6500K): Simulates average daylight in the Northern Hemisphere (cloudy northern window light), cool-toned with higher blue light proportion.
- **D70** (~7000K): White point calibration targeting the D70 color temperature standard. Cooler, bluish-white. Suitable for specialized high color temperature scenarios.

Installation steps:
1. Copy the .icm file to `C:\Windows\System32\spool\drivers\color`.
2. Open system search bar, type "Color Management" and launch the tool.
3. In the Devices dropdown, select the target monitor, check "Use my settings for this device", then click Add.
4. Select the imported color profile (.icm) and confirm.
5. Switch to the Advanced tab and click "Change system defaults".
6. Under the Advanced tab again, check "Use Windows display calibration" and click "Reload current calibration".

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

Grip customization tool. Fixes issue with grip mapping key defaulting in mouse mode.

### GamePad Test Calibration Tool V1.02

**Release date:** 2022-09-02

**Download:** [Download](https://www.gpd.hk/filedownload/89292)

Tool for WIN Max 2 grip back button mapping, programming, and vibration adjustment.

### GPD Keyboard Assistant Tool v1.06

**Release date:** 2021-12-16

**Download:** [Download](https://drive.google.com/file/d/1vo0IARTCvnmvVINl9_cxvMpL1zKNsfGw/view?usp=sharing)

Download and unzip, then double-click to run the installation.

### Power Control Panel v2

**Release date:** 2022-09-02

**Download:** [Download](https://drive.google.com/file/d/1bITmR1WxqqRmxRkoFzjnSMj1zHYElpXY/view?usp=sharing)

**Requirements:** .NET 6.0 desktop runtime ([download](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-6.0.10-windows-x64-installer)) OR self-contained zip in releases.

Compatible devices (Windows only): Win 2, Win 3, Win Max 2020, Win Max 2021 Intel/AMD, Win Max 2 1260p, Win Max 2 6800U, Pocket 2, Pocket 3.

Note: This tool is a community-developed work in progress.

---

## Documentation & Reference

| Resource | Date | Notes | Download |
|---|---|---|---|
| WIN MAX 2 (2023) User Manual | 2023-09-06 | PDF with functional key descriptions. | [Download](https://drive.google.com/file/d/1A86vx8izfC6yWtSlTOKg0PIOlJ8iCKaK/view?usp=sharing) |
| WIN Max 2 (2023) Q & A | 2023-09-06 | PDF with frequently asked questions. | [Download](https://www.gpd.hk/filedownload/108824) |

---

## 3D Printing Files

| Resource | Date | Notes | Download |
|---|---|---|---|
| 3D Printing Files for M.2 to Oculink Adapter Cover | 2023-09-13 | Intermediate open cover for matching M.2 to Oculink on WIN Max 2 (6800U, 7640U, 7840U). | [Download](https://www.gpd.hk/filedownload/109242) |

---

## GPD OS / Linux Firmware

| Resource | Date | Notes | Download |
|---|---|---|---|
| Bazzite (Fedora Atomic + SteamOS Gaming Mode) | 2024-08-21 | Fedora-based SteamOS alternative with Handheld Daemon pre-installed. [Documentation](https://universal-blue.discourse.group/docs?topic=2418) | [bazzite.gg](https://bazzite.gg/) |
| GPD OS (WIN Max 2 6800U) — Manjaro/SteamOS | 2022-12-13 | Linux Kernel 6.0, Manjaro desktop + Steam OS game mode. **Install BIOS v1.03 before flashing** (otherwise USB may not be recognized). Use balenaEtcher. First boot: connect Wi-Fi, launch Steam before switching to Deck GamePad UI. [Setup video](https://youtu.be/aekVivINoOQ) — BIOS v1.03: [Download](https://drive.google.com/file/d/1UkfUfCggsuPkHGI9UtLk-lsd2hEZddjM/view?usp=share_link) | [Mirror](https://mirror.fkardame.com/Linux/Images/GPD/) |
| balenaEtcher (Portable) | 2022-12-13 | Image writing tool. Supported formats: img, iso, zip, bz2, dsk, etch, gz, hddimg, raw, xz. | [balena.io](https://www.balena.io/etcher/) |

---

## SSD Installation

Video guide: 4G Module And 2230 SSD Assembling Tutorial On GPD WIN MAX 2 (linked from official resource page).
