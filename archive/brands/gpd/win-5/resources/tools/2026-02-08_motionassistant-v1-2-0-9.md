---
title: MotionAssistant v1.2.0.9 (GPD Handheld Front-end Tool)
product: gpd-win-5
kind: tool
tool_name: MotionAssistant
version: v1.2.0.9
release_date: 2026-02-08
source_url: https://gpd.hk/gpdwin5firmware
extraction_password: "123"
captured: 2026-04-21
tags: [gpd, tool, motionassistant, front-end, rtss, winring0]
---

# MotionAssistant v1.2.0.9

The portable version does not require installation; it can be used directly after unzipping. **Unzip password: `123`.**

Recently, the Winring0 driver was blocked by Microsoft and flagged as malicious. MotionAssistant uses this driver for three functions: TDP adjustment, hardware monitoring, and fan control. If these features malfunction, it is likely due to isolation by Windows Security Center.

## V1.2.0.9 Changelog

1. Adapted the gyroscope in the Legion Go 2 device body. Gyroscope support for its controllers and fan control has not been adapted.
2. Adapted support for various AMD rebranded models (recently released).
3. Added a "Disable Tablet Mode" option in Advanced Settings. When disabled, Tablet Mode will automatically turn off upon the next launch of MotionAssistant.
4. Added an OSD toggle hotkey in the RTSS OSD settings. Temperature display has been added to the simplified mode.
5. Added a 30-second cycle for resetting TDP. It will reapply the current TDP if an abnormal decrease is detected. Added TDP ±5 hotkeys.
6. Optimized the logic for the Win5 keyboard key: press to bring up the on-screen keyboard, press again to close it.
7. Optimized the control of the CPU frequency upper limit by the "Optimize CPU Frequency" option; the maximum frequency is restored when the option is disabled.
8. Improved the display of some controls in Dark Mode; the title bar has been changed to a darker color.
9. Optimized the gyroscope simulation process after resuming from hibernation, fixing an issue where simulation failed on some devices after wake-up.
10. Optimized hotkey detection by shortening the judgment interval. The brightness hotkeys now adjust brightness by ±10.
11. Specified the ze_loader.dll version as 1.11.0. For Intel models unable to lock the GPU frequency, please install the Intel 6647 version iGPU driver first, then update to the latest version (available in the group chat).
12. Fixed an issue where the power limit was locked at 65W and could not be restored when the GPD WIN5 was powered via the USB-C port.

## Bundled / related downloads

- Power Mod 2.1.1
- Portable Version
- Installer Version
- RTSS 736
- Video Tutorials (linked from the GPD download page)
