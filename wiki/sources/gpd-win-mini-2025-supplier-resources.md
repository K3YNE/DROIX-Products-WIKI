---
title: "GPD WIN Mini 2025 Supplier Resources"
type: source
subtype: resource-firmware
slug: gpd-win-mini-2025-supplier-resources
brand: gpd
product: gpd-win-mini
source_url: https://www.gpd.hk/gpdwinmini2025firmwaredriver
created: 2026-04-22
updated: 2026-04-22
tags: [resource-firmware, resource-bios, resource-driver, resource-tool, resource-manual, gpd]
---

## GPD WIN Mini 2025 Supplier Resources

All resources from the [[gpd|GPD]] official firmware & driver page. Applies to [[gpd-win-mini]] (2024 and 2025 models). The page covers models with 8840U, AI 9 365, and AI 9 HX 370 APUs.

**Individual source pages:** [[gpd-win-mini-2025-bios-v2-10-365-370]], [[gpd-win-mini-2025-bios-v2-11-8840u]], [[gpd-win-mini-2025-controller-firmware-v1-23]], [[gpd-win-mini-2025-firmware-win11-24h2]], [[gpd-win-mini-2025-user-manual]], [[gpd-win-mini-2025-gamepad-firmware]], [[gpd-drivers-v4-1-0]], [[gpd-motionassistant-v1-2-0-9]], [[gpd-gpdtool-v1-45]], [[gpd-amd-handheld-control-v1-0-0]], [[gpd-dtsx-audio]], [[gpd-gamepad-test-v1-03]], [[gpd-power-control-panel]].

---

### Windows 11 Firmware

| Resource | Date | SHA1 | Notes | Download |
|----------|------|------|-------|----------|
| GPD WIN Mini 2025 (8840U / 365 / 370) Windows 11 24H2 Home Firmware **(current)** | 2025-03-18 | `30B2D557AEB549ACDC6C36D4E1DE95F209614BBE` | Includes latest integrated graphics driver; resolves issue of internal screen not working when connecting to GPD G1. Applies to all three APU variants. Reinstallation removes all data on drive C — back up first. SHA1 tool: [HashTools](https://www.binaryfortress.com/HashTools/Download/) | [Download](https://drive.google.com/file/d/1p4z9nrqFEqsZeJC3XSMZOb4L5WyorU43/view?usp=sharing) · [Installation Guide](https://drive.google.com/file/d/1lk__yZ55QZwLxYJbXSPltD4ZPYvjeiBD/view?usp=sharing) |

**Installation:** Reinstallation removes all data on drive C. Always back up data before proceeding.

---

### Manuals

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| GPD WIN Mini 2025 User Manual **(current)** | 2024-12-10 | PDF — WIN Mini 2025 function keys and ports description | [Download](https://drive.google.com/file/d/1deZsZ-q-7gB7cJ5NkcklI0Cn0QtRa5df/view?usp=sharing) |

---

### BIOS

| Resource | Version | Date | Applies To | Notes | Download |
|----------|---------|------|-----------|-------|----------|
| GPD WIN Mini 2025 BIOS & EC Firmware **(current for AI 9 365/370)** | v2.10 BIOS + v2.07 EC | 2025-07-07 | AI 9 365 / AI 9 HX 370 only | Introduces battery threshold management — charges only to the set percentage. Does not apply to 8840U. | [Download](https://drive.google.com/file/d/1VrWuBvOYZymtjwKtjPxjjM6FdYLmzXmU/view?usp=sharing) |
| GPD WIN Mini 2025 BIOS & EC Firmware **(current for 8840U)** | v2.11 BIOS + v2.04 EC | 2025-08-21 | 8840U (FP8) only | Fixed issue where BIOS always displayed 8GB VRAM regardless of modifications. Does not apply to 365/370. | [Download](https://drive.google.com/file/d/1X0taJotRecAYBqZyqe3UG9a4fnn2hTR8/view?usp=drive_link) |

---

### Drivers

| Resource | Version | Date | Notes | Download |
|----------|---------|------|-------|----------|
| GPD WIN Mini 2025 (8840U / 365 / 370) Drivers **(current)** | V4.1.0 | 2025-01-18 | Latest driver package for all three APU variants. After extracting, double-click `AutoInstallDrivers.bat` for automatic installation. | [Download](https://drive.google.com/file/d/1nl_pGzcp9JmTBiG0sGhTmv_OuGkqBh8o/view?usp=drive_link) |

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

### Controller Firmware and Tools

| Resource | Version | Date | Notes | Download |
|----------|---------|------|-------|----------|
| GPD WIN Mini 2025 Controller Firmware + GPD WinControls **(current)** | Firmware v1.23 + WinControls v2.08 | 2026-03-19 | Combined package. `GPD WIN Mini 2025_V1.23_260302.exe` is the controller firmware; after upgrading, recalibrate with `Win3TestV1.04.exe`. `GPD WinControlsV2.08.exe` is a beta customization tool — requires firmware upgrade and recalibration first. | [Download](https://drive.google.com/file/d/1yXF178_teuyyfh17TsW76I5CtlpUHL6p/view?usp=sharing) |
| GamePad Test Calibration Tool | V1.03 | 2024-09-02 | Tool for WIN Mini grip back button mapping, programming, and vibration adjustment | [Download](https://www.gpd.hk/filedownload/145135) |

---

### Audio

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| DTS:X Audio Technology, 3D Sound Field | 2024-12-24 | After downloading, decompress and execute `DTS_install.bat` to install automatically | [Download](https://drive.google.com/file/d/1XYJ61YhmMUCBburRNxQVJm4Tra1kApv8/view?usp=sharing) |

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
- Hardware: Fixed WIN 5 Controller Switch key invocation (Note: Requires Firmware v1.11)

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
| WIN Mini 2025 Windows 11 24H2 Firmware (2025-03-18) | `30B2D557AEB549ACDC6C36D4E1DE95F209614BBE` |
