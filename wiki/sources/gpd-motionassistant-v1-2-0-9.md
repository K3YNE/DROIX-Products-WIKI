---
title: MotionAssistant v1.2.0.9 (GPD Handheld Front-end Tool)
type: source
subtype: resource-tool
slug: gpd-motionassistant-v1-2-0-9
brand: gpd
product: gpd-win-5
variant: null
source_url: https://gpd.hk/gpdwin5firmware
tool_name: MotionAssistant
version: v1.2.0.9
release_date: 2026-02-08
extraction_password: "123"
download_url: https://drive.google.com/file/d/1VgxU_Wt_VaVpN-MTkmdVye25mVvrorXY/view?usp=sharing
applies_to: [gpd-win-5, gpd-win-4, gpd-win-mini, gpd-win-max-2, gpd-pocket-4, gpd-duo]
created: 2026-04-21
updated: 2026-04-23
tags: [gpd, tool, motionassistant, front-end, rtss, winring0, resource]
---

# MotionAssistant v1.2.0.9

Current GPD Handheld Front-end Tool. Handles TDP adjustment, hardware monitoring, fan control, on-screen keyboard, hotkeys, RTSS OSD, and gyroscope simulation.

Available for the [[gpd-win-5]] and the broader GPD handheld lineup. Also adapted for recently-released AMD rebranded models and the Lenovo Legion Go 2 chassis gyroscope in this release.

## Key caveats

- MotionAssistant depends on the **Winring0** driver, which Microsoft has flagged as malicious. If Windows Security Center quarantines the driver, TDP adjustment, hardware monitoring, and fan control will malfunction.
- Portable download extraction password: `123`.

## Notable changes in 1.2.0.9

- Added Legion Go 2 device-body gyroscope support (controllers / fan control not yet adapted).
- Added "Disable Tablet Mode" toggle in Advanced Settings.
- Added RTSS OSD toggle hotkey; temperature in simplified OSD.
- Added 30-second TDP reset cycle; new TDP ±5 hotkeys.
- Fixed a bug where WIN 5 powered via USB-C was locked at 65 W TDP and could not be restored.
- Specified `ze_loader.dll` at v1.11.0 — Intel iGPU users should install the Intel 6647 driver before the latest iGPU driver.
- Optimised brightness hotkey (±10 step), on-screen keyboard toggle logic, gyroscope after hibernation.

Full changelog is on the raw page.

## Download

- [Portable Version](https://drive.google.com/file/d/1VgxU_Wt_VaVpN-MTkmdVye25mVvrorXY/view?usp=sharing) (unzip password: `123`)
- [Installer Version](https://drive.google.com/file/d/1YC6JLePydHL1NRDlxfZyx37Gi1InITZY/view?usp=sharing)
- [RTSS 736](https://drive.google.com/file/d/1tZmkLGyr2rOWBOgEhIBHGZT2Sakhspz9/view?usp=sharing)
- [Video Tutorials](https://www.youtube.com/watch?v=Gc94JVHOcFs)
- [Motion Assistant V1.2.0.8 + Power Mod 2.1.1](https://github.com/ThatUsernameAlreadyExist/Motion-Assistant-Power-Mod/releases/tag/1.2.0.8-2.1.1) (community shell mod by Alexander)
