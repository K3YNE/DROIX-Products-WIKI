---
title: "GPD WIN Max 2 2025 Supplier Resources"
type: source
subtype: resource-firmware
slug: gpd-win-max-2-2025-supplier-resources
brand: gpd
product: gpd-win-max-2
source_url: https://www.gpd.hk/gpdwinmax22025firmware
created: 2026-04-22
updated: 2026-04-22
tags: [resource-firmware, resource-bios, resource-driver, resource-tool, resource-manual, gpd]
---

## GPD WIN Max 2 2025 Supplier Resources

All resources from the [[gpd|GPD]] official firmware & driver page. Applies to [[gpd-win-max-2]] (2025 model with 8840U and AI 9 HX 370 APUs).

**Individual source pages:** [[gpd-win-max-2-2025-user-manual]], [[gpd-win-max-2-2025-battery-icon-fix]], [[gpd-win-max-2-fingerprint-driver-linux]], [[gpd-win-max-2-screen-calibration]], [[gpd-firmware-win11-24h2-shared]], [[gpd-drivers-v4-1-0]], [[gpd-motionassistant-v1-2-0-9]], [[gpd-gpdtool-v1-45]], [[gpd-amd-handheld-control-v1-0-0]], [[gpd-dtsx-audio]], [[gpd-gamepad-test-v1-03]], [[gpd-power-control-panel]].

---

### Windows 11 Firmware

| Resource | Date | SHA1 | Notes | Download |
|----------|------|------|-------|----------|
| GPD WIN Max 2 2025 (8840U / 370) Windows 11 24H2 Home Firmware **(current)** | 2024-12-20 | `730BD7B9D989797488C1509E590085FD9941E80C` | Covers both 8840U and AI 9 HX 370 variants. Includes integrated Windows 11 drivers. Reinstallation removes all data on drive C — back up first. SHA1 tool: [HashTools](https://www.binaryfortress.com/HashTools/Download/) | [Download](https://drive.google.com/file/d/1vr_seeh5rmQUe-Ez49htZ63ykrkyHT4x/view?usp=sharing) · [Installation Guide](https://drive.google.com/file/d/1lk__yZ55QZwLxYJbXSPltD4ZPYvjeiBD/view?usp=sharing) |

**Installation:** Reinstallation removes all data on drive C. Always back up data before proceeding.

---

### Manuals

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| WIN MAX 2 (2025) User Manual **(current)** | 2024-12-06 | PDF — functional key descriptions for the GPD WIN Max 2 (2025) | [Download](https://drive.google.com/file/d/1z_aGJMkNDQCtHXh2e9Nm0Q2yW_16kPvn/view?usp=sharing) |

---

### Drivers

| Resource | Version | Date | Notes | Download |
|----------|---------|------|-------|----------|
| GPD WIN Max 2 2025 (8840U / 370) Drivers **(current)** | V4.1.0 | 2025-01-18 | Latest driver package. After extracting, double-click `AutoInstallDrivers.bat` for automatic installation. | [Download](https://drive.google.com/file/d/1nl_pGzcp9JmTBiG0sGhTmv_OuGkqBh8o/view?usp=sharing) |

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
| WinControls **(current)** | v1.16 | 2024-12-26 | WIN Mini/Max 2 grip customization tool. Fixed issue with grip mapping key defaulting to mouse mode. Tutorial: [Download](http://www.gpd.hk/filedownload/88998). Unzip Password: `123` | [Download](https://drive.google.com/file/d/1odg796V28sIAN1-SBnAZFSi7wInfKTFl/view?usp=sharing) |
| GamePad Test Calibration Tool | V1.03 | 2024-09-02 | Tool for WIN Max 2 grip back button mapping, programming, and vibration adjustment | [Download](https://www.gpd.hk/filedownload/145135) |
| GPD Keyboard Assistant Tool | v1.06 | 2021-12-16 | Download and unzip, then double-click to run the installation | [Download](https://drive.google.com/file/d/1vo0IARTCvnmvVINl9_cxvMpL1zKNsfGw/view?usp=sharing) |
| Fix the WIN Max 2 Battery Icon | — | 2025-12-10 | After downloading, unzip the file. Double-click to execute, or right-click and select "Run as administrator" | [Download](https://www.gpd.hk/filedownload/2976392) |

---

### Linux / Fingerprint Drivers

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| CS1197 Fingerprint Driver for Linux | 2025-02-17 | Applies to all versions of WIN Max 2 | [GitHub](https://github.com/ericlinagora/libfprint-CS9711) |

---

### Display

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| WIN Max 2 Screen Color Calibration File | 2025-05-15 | .icm format files for Windows only. Two variants: D65 (6500K, average daylight) and D70 (7000K, cooler white point calibration). Installation: copy .icm to `C:\Windows\System32\spool\drivers\color`, open Color Management, select device, check "Use my settings for this device", click Add and select the profile. In Advanced tab, click "Change system defaults", check "Use Windows display calibration", click "Reload current calibration". | [Download](https://drive.google.com/file/d/1k5Ci2eJSOT7iJARbb1g4WXsevpUp4NYJ/view?usp=sharing) |

---

### 3D Printing Files

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| 3D Printing Files for M.2 to Oculink Adapter Cover | 2023-09-13 | Intermediate open cover for M.2 to Oculink adapter on WIN Max 2 (6800U, 7640U, 7840U). Download and print yourself. | [Download](https://www.gpd.hk/filedownload/109242) |

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

Compatible Devices (Windows only): Win 2, Win 3, Win max 2020, Win Max 2021 Intel/AMD, Win Max 2 1260p, Win Max 2 6800U, Pocket 2, Pocket 3. Requires [.NET 6.0 desktop runtime](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-6.0.10-windows-x64-installer).

---

### GPD OS / Alternative OS Firmware

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| Bazzite (Fedora Atomic Desktop + Steam OS Gaming Mode) | 2024-08-21 | Custom image on Fedora Atomic Desktops with Steam Deck gaming client. TDP control via Handheld Daemon (pre-installed) or Decky Loader plugin. See [community docs](https://universal-blue.discourse.group/docs?topic=2418). | [bazzite.gg](https://bazzite.gg/) |
| GPD OS (WIN Max 2 6800U) Firmware | 2022-12-13 | Manjaro/SteamOS-like Linux by Furkan Kardame. Linux Kernel 6.0. Before installing, update to BIOS v1.03 (required or USB devices may fail to recognise). Use balenaEtcher to install. | [Download](https://mirror.fkardame.com/Linux/Images/GPD/) · [BIOS v1.03](https://drive.google.com/file/d/1UkfUfCggsuPkHGI9UtLk-lsd2hEZddjM/view?usp=share_link) |
| balenaEtcher Image Disk Writing Tool (Portable Edition) | 2022-12-13 | Supported formats: img, iso, zip, bz2, dsk, etch, gz, hddimg, raw, xz | [balena.io/etcher](https://www.balena.io/etcher/) |

---

### SHA1 Checksums Summary

| File | SHA1 |
|------|------|
| WIN Max 2 2025 Windows 11 24H2 Firmware (2024-12-20) | `730BD7B9D989797488C1509E590085FD9941E80C` |
