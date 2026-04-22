---
title: "How to update the GPD MicroPC 2 BIOS"
type: source
subtype: kb-article
slug: gpd-micropc-2-bios-update
brand: gpd
product: gpd-micropc-2
source_url: "https://gpdstore.net/kb/gpd-micropc-2-support-hub/kb-article/how-to-update-the-gpd-micropc-2-bios/"
published: 2025-07-30
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, gpd, gpd-micropc-2, bios]
---

Updating the [GPD MicroPC 2](https://gpdstore.net/laptops/gpd-micropc-2/) firmware is a simple procedure, but it can seem intimidating for first-timers. Our guide will take you through each step of the process.

The current version v2.13 has the following changes:

* Removed invalid DDR frequency settings
* Added TDP setting options for 6W, 8W, 10W, 12W; 6W and 8W support fan silent fan mode
* Enabled advanced options

Please note that while BIOS updating is generally fine, there are risks. Please ensure you follow all steps correctly, identify that you are installing the correct BIOS for your device, have a fully charged battery and also connected to a charger. Do not switch off the device unless instructed to. We do not accept responsibility if something goes wrong.

Ways to identify your CPU on your device:

* To access Task Manager, **right click** on the **Windows Start** icon and choose Task Manager from the list. Alternatively you can type Task Manager in the Windows Search Bar.
* You can find your CPU model in Windows quickly through **Settings (About your PC)**, or the S**ystem Information app (msinfo32)**, all showing the processor’s name and spec.  
  Using Settings (Easiest for Windows 10/11)  
  Click the Start Menu (Windows icon) and type **about**.  
  Select **About your PC** from the results.  
  Look under “**Device specifications**” for the Processor entry, which lists your CPU model (e.g., Intel Core i7-10750H).

Task Manager CPU

## Check which BIOS version you are currently on

Power on the [GPD MicroPC 2](https://gpdstore.net/laptops/gpd-micropc-2/) and immediately and repeatedly tap the **Backspace** key on the keyboard. Keep doing this until the BIOS menu is shown. If it boots to Windows, repeat the process again.

GPD MicroPC 2 BIOS Main Page

The BIOS version number will be displayed on the Project Version, in the above image it is 2.13 and the EC Version is 2.13, which is BIOS v2.13

## Downloading the Update

First, you’ll need to get the [GPD MicroPC 2 BIOS update here](https://gofile.me/7AWvf/BHBVYtuoP). Be aware that some antivirus programs might incorrectly flag the file as a threat because its purpose is to modify the system’s BIOS.

**Changes for v2.17**

* Fix Touch Screen no function after S3 resume while OS is Linux issue.
* This BIOS was built with EC V2.14 included, Please update BIOS with AC inserted.
* Support Windows update EC.

## Preparation Steps

Before starting the installation, ensure your [GPD MicroPC 2](https://gpdstore.net/laptops/gpd-micropc-2/) is fully charged and plugged into the power adapter. We also advise closing any open software, as the device will restart automatically once the update is done.

After downloading, extract the contents of the .zip file. You should see a file named **BIOS\_M2\_V2.17\_GPD.exe** in the **AfuWin** folder.

## Installing the BIOS Update

Run the .exe file by double-clicking it and approve any Administrator access requests that appear. After a moment, a command prompt window will open to begin the update.

Updating GPD MicroPC 2 BIOS – Pre-update information

Before proceeding, please verify that your device’s battery is full and the power adapter is connected. When you are ready, press any key to initiate the BIOS update.

Updating GPD MicroPC 2 BIOS – Reading Flash

After a brief wait, you will be prompted to reboot the device to proceed with the BIOS update.

Once rebooted, the BIOS update will now proceed. Do not switch off the device during this process. It will take a couple of minutes to update.

GPD MicroPC 2 BIOS Update – Updating the firmware

When the update is complete, the GPD MicroPC 2 will reboot and show a blank screen. Do NOT switch off or press any buttons during this process. It may take a few minutes.

GPD MicroPC 2 LED On

Allow a moment for the [GPD MicroPC 2](https://gpdstore.net/laptops/gpd-micropc-2/) to shut down and power off completely. Wait until the power LED is no longer lit, then press the power button to switch the device back on. Windows will then boot up as normal. Please be aware that the initial startup following a BIOS update can sometimes take a little longer than usual.

This concludes the BIOS update process, and your device is now ready for use.

To verify that the update was successful, you can enter the BIOS menu and check the number displayed next to the EC Version. This number should match the version you just installed For example in the below photo, the Project Version shows 2.17 and the EC Version shows 2.13

GPD MicroPC 2 BIOS 2.17

## GPD MicroPC 2 UMPC

[Shop now](https://gpdstore.net/laptops/gpd-micropc-2/)
