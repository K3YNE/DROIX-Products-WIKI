---
title: "GPD WIN 5 Supplier Resources"
type: source
subtype: resource-firmware
slug: gpd-win-5-supplier-resources
brand: gpd
product: gpd-win-5
source_url: https://www.gpd.hk/gpdwin5firmwaredriver
created: 2026-04-22
updated: 2026-04-22
tags: [resource-firmware, resource-bios, resource-driver, resource-tool, resource-manual, gpd]
---

## GPD WIN 5 Supplier Resources

All resources from the [[gpd|GPD]] official firmware & driver page. Applies to [[gpd-win-5]].

**Note on individual source pages:** Several resources from this page have dedicated versioned source pages in the wiki. Where a dedicated page exists, it is linked in the table below. This page serves as the complete index and preserves all resource metadata.

Individual source pages that exist: [[gpd-win-5-firmware-win11-25h2]], [[gpd-win-5-firmware-win11-24h2]], [[gpd-win-5-bios-v2-25]], [[gpd-win-5-drivers-2025-10-30]], [[gpd-win-5-user-manual-2025-09-04]], [[gpd-win-5-optical-mouse-firmware]].

---

### Windows 11 Firmware

| Resource | Version / Date | SHA1 | Notes | Download |
|----------|---------------|------|-------|----------|
| GPD WIN 5 Windows 11 25H2 Home Firmware **(current)** | 2025-11-27 | `3A7B73EBAA90AF1FDEEA4D9840B438DA9DB76398` | Integrated Windows 11 drivers. Reinstallation erases all data on drive C. Back up before proceeding. SHA1 tool: [HashTools](https://www.binaryfortress.com/HashTools/Download/) | [Download](https://drive.google.com/file/d/1LhGo7VP8ROkv9Jo_oHeqketOkDBzVBGJ/view?usp=sharing) · [Installation Guide](https://drive.google.com/file/d/1lk__yZ55QZwLxYJbXSPltD4ZPYvjeiBD/view?usp=sharing) |
| GPD WIN 5 Windows 11 24H2 Home Firmware | 2025-09-05 | `76AB196F524AC72EDBCB9B2BD6BC792C473AD485` | Integrated Windows 11 drivers. Reinstallation erases all data on drive C. Back up before proceeding. | [Download](https://drive.google.com/file/d/1j5XbXf3lyEVQGHGQVyhED8hTKqDFuaFm/view?usp=sharing) · [Installation Guide](https://drive.google.com/file/d/1lk__yZ55QZwLxYJbXSPltD4ZPYvjeiBD/view?usp=sharing) |

**Installation:** Reinstalling firmware will erase all data on drive C. Always back up data before proceeding.

---

### Manuals

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| GPD WIN 5 User Manual **(current)** | 2025-09-04 | PDF — WIN 5 function keys and ports description | [Download](https://drive.google.com/file/d/1UzklmmiFL72I8tqQm6GAR_fp6M-ubvoO/view?usp=sharing) |
| GPD WIN 5 Smart Dock User Manual **(current)** | 2025-09-04 | PDF — port descriptions for the WIN 5 Smart Dock | [Download](https://drive.google.com/file/d/1Xpj9vVDWmu6V3ITgPd5BfMQO3aOtj2wB/view?usp=sharing) |

---

### Controller Firmware

| Resource | Version | Date | Changelog | Download |
|----------|---------|------|-----------|----------|
| GPD WIN 5 Controller Firmware **(current)** | v1.11 | 2026-04-13 | Modified HID data reporting method to support third-party software in retrieving real-time button status. Note: update MotionAssistant simultaneously for full compatibility. | [Download](https://drive.google.com/file/d/1-KSPFUbRNpQMx1YlAKbDGLLOs3txlIQh/view?usp=sharing) |
| WIN 5 Controller Firmware | v1.08 | 2025-11-10 | Switch to controller mode first, then upgrade. | [Download](https://drive.google.com/file/d/1nE6aDPS6oECxTm8o1F1Y-D1GlJc2-RLI/view?usp=sharing) |

---

### OFN (Optical Finger Navigation) Firmware

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| WIN 5 OFN Firmware **(current)** | 2025-11-27 | Resolves optical finger mouse drift issue | [Download](https://drive.google.com/file/d/1-_al7KG5Kb55-Pp4jjR8sMOjdAVxNBIO/view?usp=sharing) |

---

### BIOS

| Resource | Version | Date | Changelog | Download |
|----------|---------|------|-----------|----------|
| GPD WIN 5 BIOS **(current)** | v2.25 | 2026-01-15 | AMD officially updated BIOS code. Completely new version — cannot flash back to older BIOS after upgrading. In Windows: download and extract, double-click to execute upgrade. System will auto-restart into BIOS, then shut down after upgrade (manual restart required). Keep device on charge during upgrade. WinRAR extraction password: `123` | [Download](https://drive.google.com/file/d/1WmonHwGCSn8zzuzDogr5KHk5-_2NKvBH/view?usp=sharing) |

---

### Drivers

| Resource | Version | Date | Notes | Download |
|----------|---------|------|-------|----------|
| GPD WIN 5 Drivers **(current)** | — | 2025-10-30 | Latest driver package. After extracting, double-click `AutoInstallDrivers.bat` for automatic installation. | [Download](https://drive.google.com/file/d/1aGyzyMp-kpirpwy9TDfRTzqd_ERjN4L3/view?usp=sharing) |

#### Updating AMD and Intel Drivers Manually

The official driver package may not be updated in real time. After a period of device usage, manual upgrades may be needed.

**AMD GPU Driver Update:**
1. Open [AMD Driver Download Page](https://www.amd.com/en/support/download/drivers.html)
2. Select the corresponding processor and click Search
3. Expand drivers for your pre-installed Windows version; locate the driver with the "WHQL Recommended" label and download/install it

**AMD Chipset Driver Update:**
1. Open [AMD Driver Download Page](https://www.amd.com/en/support/download/drivers.html)
2. Follow the steps, then click "Submit"
3. Expand drivers for your Windows version and download/install. Click "Previous Version" if the latest version is unstable.

**Intel Driver Update (Wi-Fi/Bluetooth only):**
1. Open [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html)
2. Download and install Intel® DSA — it will identify and update outdated Intel hardware drivers automatically

---

### Audio

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| DTS:X Audio Technology, 3D Sound Field | 2025-12-24 | After downloading, decompress and execute `DTS_install.bat` to install automatically | [Download](https://drive.google.com/file/d/1XYJ61YhmMUCBburRNxQVJm4Tra1kApv8/view?usp=sharing) |

---

### Tools

| Resource | Version | Date | Notes | Download |
|----------|---------|------|-------|----------|
| WinControls **(current)** | v2.08 | 2025-11-10 | WIN 5 Controller Customization Tool | [Download](https://drive.google.com/file/d/1-meuFEBHPheR2PGB9aCye5v4hsPgI-c2/view?usp=sharing) |
| GamePad Test Calibration Tool | V1.04 | 2025-11-10 | Tool for WIN 5 grip back button mapping, programming, and vibration adjustment | [Download](https://drive.google.com/file/d/1V2HxYxXoj1ChTbp41D820er3eD1e_zid/view?usp=sharing) |

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

**v1.2.0.9 Changelog:**
1. Adapted the gyroscope in the Legion Go 2 device body. Gyroscope support for its controllers and fan control has not been adapted.
2. Adapted support for various AMD rebranded models (recently released).
3. Added a "Disable Tablet Mode" option in Advanced Settings. When disabled, Tablet Mode will automatically turn off upon the next launch of the motion assistant.
4. Added an OSD toggle hotkey in the RTSS OSD settings. Temperature display has been added to the simplified mode.
5. Added a 30-second cycle for resetting TDP. It will reapply the current TDP if an abnormal decrease is detected. Added TDP ±5 hotkeys.
6. Optimized the logic for the Win5 keyboard key: press to bring up the on-screen keyboard, press again to close it.
7. Optimized the control of the CPU frequency upper limit by the "Optimize CPU Frequency" option; the maximum frequency is restored when the option is disabled.
8. Improved the display of some controls in Dark Mode; the title bar has been changed to a darker color.
9. Optimized the gyroscope simulation process after resuming from hibernation, fixing an issue where simulation failed on some devices after wake-up.
10. Optimized hotkey detection by shortening the judgment interval. The brightness hotkeys now adjust brightness by ±10.
11. Specified the ze_loader.dll version as 1.11.0. For Intel models unable to lock the GPU frequency, please install the Intel 6647 version iGPU driver first, then update to the latest version.
12. Fixed an issue where the power limit was locked at 65W and could not be restored when the GPD Win5 was powered via the USB-C port.
13. Corrected some text displays. Fixed an issue where OSD monitoring displayed incorrectly when hardware monitoring was turned off.
14. Fixed an issue where LT/RT could not be properly registered as hotkeys.
15. Fixed an issue that could cause a freeze when setting TDP consecutively.
16. Fixed an issue where certain options in specific game profiles, such as CPU frequency limits, were not applied automatically.
17. Fixed an issue where frame locking failed in some specific game profiles. Changed the frame locking strategy for specific profiles; it no longer sets a global configuration but instead uses an RTSS process-specific configuration for frame locking.
18. Fixed an issue causing the application to crash when refreshing the tray icon.

**Power Mod 2.1.1 additions** (community mod by Alexander — shell-based modification of v1.2.0.8 with a new UI):
- Fixed saving settings if the application is installed in Program Files
- Improved for displays with very high DPI (>175%)
- Scrollbar visibility now depends on the OS setting
- Added localization via ini files (pmgui/Localization folder)
- Added Simplified Chinese, Spanish, Korean, and Japanese languages
- Added option to hide tabs in the left menu (Advanced Settings → Appearance)
- Added gamepad navigation (shoulder buttons switch tabs, D-pad/stick navigate, A=select, B=back, right stick scroll, Start=collapse menu)
- Added option to swap X and Y axes (for Win 4)
- Fixed non-working keyboard hotkeys

---

#### GPD Official Handheld Front-end Tool — GPDTool v1.45 (current) — 2026-04-13

[Download](https://drive.google.com/file/d/11Rmk4zknLFEquK_uJwuehsuL7sPYa_RO/view?usp=drive_link)

Download and extract the file, then run the installer directly. For issues: sales011@softwincn.com

**v1.45 Release Notes:**

*Feature Additions:*
- UI/UX: Full visual overhaul and UI beautification
- Performance: Integrated CPU frequency capping and real-time CPU/GPU status monitoring
- Power Management: Implemented AC/DC power state linkage (Auto-switch between High-Performance and Low-Power modes)
- RTSS Integration: Added horizontal parameter display toggle and dynamic font size scaling slider
- Input: Independent OSK (On-Screen Keyboard) full-screen invocation; custom hotkey mapping for OSK; D-Pad now mirrors Left-Joystick functionality

*Optimizations & Logic:*
- Thermal: Refined fan control algorithms for both Auto and Manual modes
- System: Disabled Windows right-edge gestures by default upon installation (toggleable via System Settings)
- Deployment: Added automated software whitelisting and official Windows Uninstaller support

*Bug Fixes:*
- Compatibility: Resolved service initialization failures on specific hardware models
- Anti-Cheat: Fixed false positive triggers for Easy Anti-Cheat (EAC)
- Hardware: Fixed WIN 5 Controller Switch key invocation (Note: Requires Controller Firmware v1.11)

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
| GPD OS (WIN Max 2 6800U) Firmware | 2022-12-13 | Manjaro/SteamOS-like Linux by Furkan Kardame. Linux Kernel 6.0. Use balenaEtcher to install. Steps on first boot: connect Wi-Fi, start Steam before switching to GamePad UI, reboot if KDE plasma appears. | [Download](https://mirror.fkardame.com/Linux/Images/GPD/) |
| balenaEtcher Image Disk Writing Tool (Portable Edition) | 2022-12-13 | Supported formats: img, iso, zip, bz2, dsk, etch, gz, hddimg, raw, xz | [balena.io/etcher](https://www.balena.io/etcher/) |

---

### Miscellaneous

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| WIN 5 Battery Power Port Cover 3D Printing File | 2025-11-12 | STP format 3D model for a dust cover for the battery interface on the back of the WIN 5. Recommended material: soft silicone. | [Download](https://drive.google.com/file/d/1sj62V3yCTbgivBTsyBLRIzEhGHdjDOBm/view?usp=sharing) |

---

### SHA1 Checksums Summary

| File | SHA1 |
|------|------|
| WIN 5 Windows 11 25H2 Firmware (2025-11-27) | `3A7B73EBAA90AF1FDEEA4D9840B438DA9DB76398` |
| WIN 5 Windows 11 24H2 Firmware (2025-09-05) | `76AB196F524AC72EDBCB9B2BD6BC792C473AD485` |
