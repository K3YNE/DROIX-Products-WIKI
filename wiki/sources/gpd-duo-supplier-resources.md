---
title: "GPD DUO Supplier Resources"
type: source
subtype: resource-firmware
slug: gpd-duo-supplier-resources
brand: gpd
product: gpd-duo
source_url: https://www.gpd.hk/gpdduofirmwaredriver
created: 2026-04-22
updated: 2026-04-22
tags: [resource-firmware, resource-bios, resource-driver, resource-tool, resource-manual, gpd]
---

## GPD DUO Supplier Resources

All resources from the [[gpd|GPD]] official firmware & driver page. Applies to [[gpd-duo]] (8840U and AI 9 HX 370 variants). Note that the GPD DUO has two distinct firmware streams — resources are clearly marked by variant.

**Individual source pages:** [[gpd-duo-bios-v2-17-370]], [[gpd-duo-bios-v3-08-8840u]], [[gpd-duo-firmware-win11-24h2-370]], [[gpd-duo-firmware-win11-24h2-8840u]], [[gpd-duo-user-manual]], [[gpd-duo-pocket-4-fingerprint-driver]], [[gpd-duo-igpu-screen-tearing-fix]], [[gpd-drivers-v4-1-0]], [[gpd-motionassistant-v1-2-0-9]], [[gpd-gpdtool-v1-45]], [[gpd-amd-handheld-control-v1-0-0]], [[gpd-dtsx-audio]].

---

### Windows 11 Firmware

| Resource | Date | SHA1 | Notes | Download |
|----------|------|------|-------|----------|
| GPD DUO (AI 9 HX 370) Windows 11 24H2 Home Firmware **(current for 370)** | 2025-03-18 | `30B2D557AEB549ACDC6C36D4E1DE95F209614BBE` | 370 variant only. **Must upgrade BIOS before upgrading system firmware** — install BIOS V2.12 first (see BIOS section). BIOS firmware v2.12 also resolves the flicker issue on the 370 version. SHA1 tool: [HashTools](https://www.binaryfortress.com/HashTools/Download/) | [Download](https://drive.google.com/file/d/1p4z9nrqFEqsZeJC3XSMZOb4L5WyorU43/view?usp=sharing) · [Installation Guide](https://drive.google.com/file/d/1lk__yZ55QZwLxYJbXSPltD4ZPYvjeiBD/view?usp=sharing) |
| GPD DUO (8840U) Windows 11 24H2 Home Firmware **(current for 8840U)** | 2024-12-20 | `A009376A9F17E881F81FE484E16BF54D3E8E8759` | 8840U variant only. Includes integrated Windows 11 drivers. Reinstallation removes all data on drive C — back up first. SHA1 tool: [HashTools](https://www.binaryfortress.com/HashTools/Download/) | [Download](https://drive.google.com/file/d/1p6m4Er4siM8rwWe2rR__RwgtY7xy1eo5/view?usp=sharing) · [Installation Guide](https://drive.google.com/file/d/1lk__yZ55QZwLxYJbXSPltD4ZPYvjeiBD/view?usp=sharing) |

**Important (370 variant):** Always upgrade BIOS to V2.12 or later before upgrading system firmware on the 370 version.

---

### Manuals

| Resource | Date | Notes | Download |
|----------|------|-------|----------|
| GPD DUO Instruction Manual **(current)** | 2024-11-26 | PDF — answers about GPD DUO frequently asked questions | [Download](https://drive.google.com/file/d/1DRfKFazRTqAr3nlOrTBpV2uf-slHLeez/view?usp=sharing) |

---

### BIOS

| Resource | Version | Date | Applies To | Notes | Download |
|----------|---------|------|-----------|-------|----------|
| GPD DUO (8840U) BIOS **(current for 8840U)** | v3.08 | 2025-03-24 | 8840U only | Optimized sleep-related issues. Added battery charging threshold management on BIOS Main page. | [Download](https://drive.google.com/file/d/1ElzfS5Rfcy0e5d0atV66lBJtGnQvGWXo/view?usp=sharing) |
| GPD DUO (370) BIOS **(current for 370)** | v2.17 | 2025-03-26 | AI 9 HX 370 only | Optimized sleep-related issues. Added battery charging threshold management. Fixed touch input on secondary screens caused by BIOS version v2.16. | [Download](https://drive.google.com/file/d/14QJRpRHO89ARfa9YnZoWZRocu8Tc_7Tq/view?usp=drive_link) |
| GPD DUO (370) BIOS & EC Firmware | v2.12 BIOS + v1.30 EC | 2025-02-07 | AI 9 HX 370 only | Resolved issues with GPD DUO not connecting to Nvidia graphics dock and not reading fan speed. **Required prerequisite before upgrading to 370 system firmware (03/18/2025 version).** | [Download](https://drive.google.com/file/d/14AuNnNHEoY-UnwFzYWz4gz2Heq_Y00sO/view?usp=drive_link) |

---

### Drivers

| Resource | Version | Date | Applies To | Notes | Download |
|----------|---------|------|-----------|-------|----------|
| GPD DUO (8840U / 370) Drivers **(current)** | v4.1.0 | 2025-01-18 | Both variants | Latest driver package. After extracting, double-click `AutoInstallDrivers.bat` for automatic installation. | [Download](https://drive.google.com/file/d/1nl_pGzcp9JmTBiG0sGhTmv_OuGkqBh8o/view?usp=sharing) |
| GPD DUO (370) iGPU Drivers — screen tearing fix | — | 2024-12-06 | AI 9 HX 370 only | iGPU driver package that fixes the screen tearing issue. After decompression, execute the `AutoInstallDrivers.bat` batch file. | [Download](https://drive.google.com/file/d/1B-qXUL4UKtIuJiy5jUAbTCX7PVQoHBM5/view?usp=sharing) |
| 4G LTE Module Driver | — | 2023-09-19 | Both variants | 4G LTE module driver package. After extracting, double-click to execute the installation. | [Download](https://drive.google.com/file/d/12Bad5Nrt3Pp5Jad1ZqFi3ziAAHTP06Ah/view?usp=sharing) |

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
| GPD DUO & GPD Pocket 4 Fingerprint Driver (Windows) | 2025-02-17 | Windows 11 Fingerprint Driver V5.2.69.24 WHQL — applies to both GPD DUO and [[gpd-pocket-4]] | [Download](https://drive.google.com/file/d/11GT_whG5Pldjwp_abVV9QcTT4WLV_lJE/view?usp=sharing) |
| Linux Fingerprint Driver for GPD DUO & GPD Pocket 4 | 2025-02-17 | Supported distros: Ubuntu, Debian, Fedora, Redhat, Kylin, UOS, Zhongke Fangde, Alibaba Cloud Workspace, etc. | [Ubuntu & Debian](https://github.com/ftfpteams/focaltech-linux-fingerprint-driver/tree/main/Ubuntu_Debian/x86) · [Fedora & Redhat](https://github.com/ftfpteams/focaltech-linux-fingerprint-driver/tree/main/Fedora_Redhat) · [UOS](https://github.com/ftfpteams/focaltech-linux-fingerprint-driver/tree/main/Uos) · [Install Tutorial](https://badb100d.com/2025/02/16/2025-02-16/) |

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
| DUO (370) Windows 11 24H2 Firmware (2025-03-18) | `30B2D557AEB549ACDC6C36D4E1DE95F209614BBE` |
| DUO (8840U) Windows 11 24H2 Firmware (2024-12-20) | `A009376A9F17E881F81FE484E16BF54D3E8E8759` |
