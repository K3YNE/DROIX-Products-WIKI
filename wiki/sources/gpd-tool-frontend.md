---
title: "GPD Tool – Frontend software for GPD devices"
type: source
subtype: kb-article
slug: gpd-tool-frontend
brand: gpd
source_url: "https://gpdstore.net/kb/gpd-duo-support-hub/kb-article/gpd-tool-frontend-software-for-gpd-devices/"
published: 2026-03-19
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, gpd]
---

GPD Tool serves as a successor to the MotionAssist software that has shipped with GPD devices for many years. It introduces a modern, redesigned interface alongside a range of new functions and features to give you greater control over your [GPD handheld gaming PCs](https://gpdstore.net/product-category/gpd-handheld-gaming-pcs/ "GPD handheld gaming PCs").

* Full controller navigation support
* Can be invoked in any fullscreen game, with customizable keyboard and controller shortcuts
* TDP adjustment support
* In-game performance monitoring and frame rate limiting
* Customizable fan silent mode
* Volume and brightness adjustment
* Game “Freezer” feature to suspend processes and save power
* On-screen keyboard support
* Supports 7 languages: Chinese, English, Japanese, Korean, Russian, French, and Spanish

## GPD Tool Downloads

You can download the latest release as well as previous releases below.

|  |  |
| --- | --- |
| GPD Tool v1.45 | [Download here](https://gofile.me/7AWvf/EierB889A) |
| GPD Tool v1.31 | [Download here](https://gofile.me/7AWvf/b85y8Njq1) |

Changes in latest GPD Tools v1.45:

* Can be manually re-enabled in Windows settings if needed
* Brand-new redesigned UI
* Added CPU frequency limit option
* Added CPU and GPU status display in the UI
* Added horizontal layout toggle for RTSS in-game overlay, along with a font size adjustment slider
* Optimized fan control logic for both automatic and manual modes
* On-screen keyboard can now be launched in full screen independently
* On WIN5, it can be triggered via the built-in keyboard shortcut
* You can also assign a separate hotkey for the on-screen keyboard
* Added power profile linkage:
* Automatically switches to high performance when plugged in
* Automatically switches to low power mode when unplugged
* Automatically added to whitelist after installation
* Fixed issue where the service failed to start after installation on some devices
* Fixed issue triggering Easy Anti-Cheat (EAC)
* Fixed issue with WIN5 controller shortcut key not working
* Requires controller firmware update to version 1.10 (version 1.09 is not supported)
* Added D-pad navigation support (same functionality as the left joystick)
* Added uninstall option (can now be removed via Control Panel)
* Removed edge gesture toggle setting
* Windows right-edge gesture is now disabled by default after installation

## Procedures for Installing GPD Tool

* **Obtain the latest GPD Tool build** via the provided download links.
* **Unzip the downloaded file** if it arrives in a compressed archive format.
* **Launch the setup file** and adhere to the guided on-screen instructions.
* **Permit the process to finish**, then reboot your system if the installer requests it.
* **Once restarted, locate the GPD Tool shortcut** within the Windows notification area (system tray).
* **Launch the interface** by either clicking the tray icon or using the **CTRL + SHIFT + F3** shortcut.
* **If the Performance tab isn’t showing**, verify that RivaTuner and DirectX are installed, then restart your machine once more.

## Procedures for Updating GPD Tool

* **Acquire the most recent edition** of the GPD Tool software.
* **Ensure the current GPD Tool application is completely shut down** from the system tray prior to starting the update.
* **Execute the new installer** and permit it to replace the previous installation if prompted.
* **Perform a system restart** once the update process concludes.
* **Start the GPD Tool** to ensure the updated version is functioning as intended.
* **In the event a controller firmware update is necessary** for this version, finish that update before investigating any other issues.

## Procedures for Uninstalling GPD Tool

* **Access the Windows Control Panel.**
* **Navigate to the Programs and Features menu.**
* **Identify GPD Tool** within the list of currently installed applications.
* **Highlight the entry** and select the Uninstall option.
* **Restart your machine** once the software has been removed.
* **Should you wish to reinstall later**, download the current release and perform a clean installation after your reboot.

## GPD Tool User Guide

To open the GPD Tool overlay, click the Windows toolbar icon in the bottom right corner of your screen, or use the keyboard shortcut ***CTRL*** + ***SHIFT*** + ***F3***.

GPD Tool – Overlay Menu

You may find the text is by default in Chinese language, you can change it to your preferred language by following the steps in the below image:

GPD Tool – Change Language

Here’s a breakdown of all the options available to you.

### TDP Settings

This section is used to manage your device’s TDP (Thermal Design Power). The range of values available will vary depending on which device you own.

GPD Tool – Change TDP

Use the slider to manually set the TDP to your desired level, or choose from the Low, Mid, or High preset buttons to quickly apply a set of default values.

### Performance

Enabling the Performance setting requires RivaTuner to be installed on your device. NOTE: DirectX may also be required for this feature to function correctly — you can download it [here](https://www.microsoft.com/download/details.aspx?id=35).

GPD Tool – Performance with RivaTuner

Once activated, RivaTuner lets you display real-time on-screen data including Frames Per Second, CPU Temperature, and more.

### FPS Lock

When FPS Lock is enabled, the frame rate in games will be capped at 60 Frames Per Second (FPS). Turning this off (the default state) allows your games to run at their maximum achievable frame rate.

### Fan Speed

The fan operates in Automatic mode by default. Use the Default, Balance, or Quiet shortcut buttons to switch between fan speed profiles. You can also disable Auto mode and manually adjust the slider to set a specific fan speed of your choosing.

### Volume and Brightness Settings

These are pretty self-explanatory 🙂 Use the sliders to increase or decrease your volume and screen brightness levels respectively.

### Shortcut Buttons

* **Desktop** – Minimises all open applications and reveals the desktop
* **Switch App** – Opens the Windows task switcher
* **Screenshot** – Captures and saves a screenshot to your Photos “Screenshot” folder
* **Force Quit** – Allows you to select and close a running application
* **Keyboard** – Displays an on-screen keyboard
* **Task Mgr** – Opens the Windows Task Manager
* **Game Fridge** – Freezes and unfreezes compatible applications to help boost overall performance

### Settings

GPD Tool – Settings

* **Auto Start** – Toggle whether GPD Tool launches automatically when Windows boots
* **Edge Gesture** –
* **Hotkey** – Set a custom hotkey combination to open the GPD Tool overlay
* **Theme** – Pick from three colour themes: Fresh Blue, Cyber Yellow, and Vibe Purple
* **CPU Turbo** – Toggle Turbo Boost on or off to improve performance in select games
* **Language** – Automatically detects your Windows language by default, but can be changed manually here

### Back Button Configuration

Clicking the small **GPD** logo in the bottom left corner of the overlay (see image below) will open the Back Button Configuration menu.

GPD Tool – Back Button Configuration

From here you can assign functions to the back buttons on your GPD handheld, if your device has them , such as custom button combinations.

## In-Depth Troubleshooting Guide

### GPD Tool Fails to Launch

If the application refuses to open, start by checking the Windows system tray for the GPD Tool icon. If the program is active in the background, simply clicking that icon should bring the overlay to the front. Should the icon be absent, try restarting your hardware, running Windows Update, ensuring your AMD drivers are current, and then attempting to launch the software again.

### Overlay Not Showing During Gameplay

If the interface isn’t appearing while you are in a game, verify that GPD Tool is actually running and double-check that the assigned hotkey hasn’t been modified. It is helpful to test the default shortcut, **CTRL + SHIFT + F3**, on your desktop first to confirm it works globally. If the issue is specific to one title, exit the game, restart GPD Tool, and try again. Note that certain anti-cheat software or exclusive fullscreen modes can occasionally block the overlay.

### Performance Settings Are Unresponsive or Locked

If you find that the Performance features are greyed out, you likely need to install or refresh your installation of RivaTuner Statistics Server (RTSS) and ensure all DirectX components are present. After installing these, reboot Windows before attempting to toggle the settings again.

* **RivaTuner Download:** <https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/>
* **DirectX Package:** <https://www.microsoft.com/download/details.aspx?id=35>

### Keyboard Shortcut Fails to Respond

If your hotkey isn’t triggering the tool, navigate to the Settings menu to verify which key combination is currently set. It’s possible another background utility is already utilizing that specific shortcut. Try assigning a unique key combo, saving the changes, and then restarting the GPD Tool.

### Functional Issues Following Installation

If certain features remain unavailable after setup, confirm that your Windows OS is fully updated and the latest AMD graphics drivers are installed. Ensure you have performed a full system restart after the initial installation. Be aware that some capabilities are dependent on specific system components or updated device firmware.

### Complications Arising After a Software Update

If a newer release introduces bugs, check if that version requires a corresponding controller firmware update or a specific software dependency. For instance, some builds require updated firmware before all shortcuts will behave correctly. If issues persist, uninstall the software, reboot your device, and perform a clean installation of the latest compatible version.

### Conflicts with Anti-Cheat or Game Stability

If a game flags the software for anti-cheat reasons or experiences compatibility issues, make sure you have updated to the most recent version of GPD Tool, as patches for these problems are frequently included in new releases. Test the tool with the game closed, then relaunch the title after the update is finished.

### Application Doesn’t Launch on System Startup

If GPD Tool is not starting automatically when you boot up, enter the Settings menu and verify that the “Auto Start” option is toggled on. Restart Windows to confirm that the tray icon successfully appears upon login.

## Supplementary Frequently Asked Questions

**Which legacy software is superseded by GPD Tool?** On supported GPD hardware, this application serves as the official successor to the older **MotionAssist** utility.

**What are the ways to access the GPD Tool interface?** You can bring up the tool by locating its icon in the Windows system tray or by using the **CTRL + SHIFT + F3** hotkey combination.

**Is RivaTuner a mandatory requirement?** RivaTuner is only essential if you plan to use the real-time **performance monitoring** capabilities. The core functions of the GPD Tool will remain operational even if RivaTuner is not installed.

**Does this software rely on DirectX?** While not always required for the base app, specific elements of the **performance overlay** may need DirectX components to be present on your system to function correctly.

**Can I delete GPD Tool at a later date?** Certainly. Current versions of the software are fully integrated with the standard Windows removal process, allowing you to uninstall it via the **Control Panel** whenever you wish.
