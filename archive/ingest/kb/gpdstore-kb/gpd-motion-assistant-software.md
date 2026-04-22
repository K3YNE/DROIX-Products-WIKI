---
title: GPD Motion Assistant Software
source_url: "https://gpdstore.net/kb/gpd-duo-support-hub/kb-article/gpd-motion-assistant-software/"
source_site: gpdstore.net
type: kb-article
date: 2026-02-10
wp_id: 1275548
---

You will find the newest release of the GPD Motion Assistant Software below, offered as both a standalone package and a setup file. Access the most recent Power Mod edition (featuring a more intuitive interface) directly on the GitHub repository [here](https://github.com/ThatUsernameAlreadyExist/Motion-Assistant-Power-Mod/releases "here").

## Latest GPD Motion Assistant Software Downloads

GPD Motion Assistant Software v1.2.0.9 [Installable Version](https://gofile.me/7AWvf/KLDDdfWVA)  
GPD Motion Assistant Software v1.2.0.9 [Portable Version](https://gofile.me/7AWvf/zd3Lv2LAT)

NOTE: Microsoft recently started blocking a specific driver (Winring0) because it was flagged as unsafe. However, **MotionAssistant actually needs this driver to work correctly.** It uses it to manage your power settings (TDP), check hardware stats, and control your fans. If these features stop working, it is likely because Windows Security has blocked the driver.

### Changes for version 1.2.0.9

1. Added support for the Legion Go 2 built-in gyroscope. Controller gyroscope and fan control are not supported yet.
2. Added support for various AMD rebranded models (recent releases).
3. Added a “Disable Tablet Mode” option in Advanced Settings. When disabled, tablet mode will be automatically turned off the next time Motion Assistant starts.
4. Added an OSD toggle hotkey to RTSS OSD settings. Temperature display is now included in the simplified mode.
5. Added a 30-second TDP reapply loop. When abnormal TDP drops occur, the current TDP will be reset. Added TDP ±5 hotkeys.
6. Optimized Win5 keyboard logic: press once to bring up the on-screen keyboard, press again to close it.
7. Optimized the “Optimize CPU Frequency” option’s control over the CPU frequency limit; canceling it now restores the maximum frequency.
8. Improved the display of some controls in dark mode; the title bar is now dark.
9. Optimized the gyroscope emulation flow after sleep/wake, fixing an issue where emulation failed to work properly on some models after waking.
10. Optimized hotkey detection and reduced the detection interval. Brightness hotkeys are now ±10 per step.
11. Fixed the ze\_loader.dll version to 1.11.0. If Intel models cannot lock GPU frequency, please install Intel iGPU driver version 6647 first, then update to the latest version (available in the group).
12. Fixed an issue on GPD Win5 where the power limit was locked at 65W when powered via the USB-C port and could not be restored.
13. Corrected some text display issues. Fixed incorrect OSD display when hardware monitoring is disabled.
14. Fixed an issue where LT/RT could not be properly recorded as hotkeys.
15. Fixed a potential system freeze when setting TDP repeatedly.
16. Fixed an issue where some options (such as CPU frequency limits) in per-profile configurations were not applied automatically.
17. Fixed an issue where frame rate limiting did not work properly in some game-specific profiles. Updated the frame-limiting strategy: no longer uses global settings, now applies RTSS per-process frame limiting instead.
18. Fixed a crash caused by errors when refreshing the system tray icon.Added support for the Legion Go 2 built-in gyroscope. Controller gyroscope and fan control are not supported yet.