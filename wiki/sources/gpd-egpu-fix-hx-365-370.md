---
title: eGPU Fix for GPD HX 365 and HX 370 CPU Based GPD Devices
type: source
subtype: kb-article
slug: gpd-egpu-fix-hx-365-370
brand: gpd
product: gpd-win-4
source_url: "https://gpdstore.net/kb/gpd-duo-support-hub/kb-article/egpu-fix-for-gpd-hx-365-and-hx-370-cpu-based-gpd-devices/"
published: 2025-01-08
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, gpd, egpu, amd-drivers, troubleshooting]
---

If you are experiencing issues with your [[gpd-win-4|GPD WIN 4 2025]], [[gpd-win-max-2|GPD WIN MAX 2 2025]], [[gpd-win-mini|GPD WIN MINI 2025]], [[gpd-pocket-4|GPD Pocket 4]] or [[gpd-duo|GPD Duo]] devices when used with an eGPU such as the [[gpd-g1|GPD G1]], the latest AMD Adrenalin drivers will fix the issue.

If your AMD drivers are earlier than 25.3.1, then updating to the latest drivers will resolve the reliability issue with GPD's HX 365 and HX 370 devices.

## Loading the AMD Adrenalin Software

To check if your drivers are up to date, you can check on the taskbar for the AMD Adrenalin app.

Open the AMD Adrenalin software.

If the icon is not showing there, type "**AMD**" into the taskbar search and it will show up in the results.

If the software is not showing here either, then you may not have the AMD Adrenalin software installed. Please refer to the guide on [[gpd-amd-graphics-drivers|how to install AMD drivers]]. This will automatically install the latest drivers as part of the process and you will be ready to use your device with an eGPU.

## Checking for and Installing Driver Updates

Once the AMD Adrenaline software has loaded, the top right area will show your current driver version and a button to **Check for Updates** — click on this.

After a few moments you should be prompted to **Download** the update — choose this option.

Once the download has completed, you will be presented with an **Install** option — choose this and follow the prompts to update the drivers. Once updated, restart your device and it will be ready to use with your eGPU.

If you have not yet set up your eGPU such as the GPD G1, please follow the [[gpd-g1-getting-started|GPD G1 getting started guide]].
