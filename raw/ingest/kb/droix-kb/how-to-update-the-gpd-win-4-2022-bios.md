---
title: How to Update the GPD WIN 4 2022 BIOS
source_url: "https://droix.net/knowledge-base/article/how-to-install-the-gpd-win-4-bios-update/"
source_site: droix.net
type: kb-article
date: 2023-04-24
wp_id: 2462
---

Ready to boost your [GPD](https://droix.net/product-attribute/brands/gpd/) WIN 4? Updating your WIN 4 BIOS can significantly improve its performance, stability and combability. But if you don’t know where to start, or just need a quick refresher, this guide makes it easy. We’ll take you through the process, from formatting your USB to every step of the installation itself.

***WARNING: This article is intended for the GPD WIN 4 2022 only, not for any previous or future models, like the GPD WIN 4 2023.***

***WARNING: If you intend to upgrade your GPD WIN 4 BIOS, please follow this guide carefully. Incorrect and improper use or deviation from the instructions may render your device inoperable. DroiX assumes no responsibility for any damages incurred.***

Ways to identify your CPU on your device:

* To access Task Manager, **right click** on the **Windows Start** icon and choose Task Manager from the list. Alternatively you can type Task Manager in the Windows Search Bar.
* You can find your CPU model in Windows quickly through **Settings (About your PC)**, or the S**ystem Information app (msinfo32)**, all showing the processor’s name and spec.  
  Using Settings (Easiest for Windows 10/11)  
  Click the Start Menu (Windows icon) and type **about**.  
  Select **About your PC** from the results.  
  Look under “**Device specifications**” for the Processor entry, which lists your CPU model (e.g., Intel Core i7-10750H).

Task Manager CPU

## GPD WIN 4 ***2022*** BIOS Update Video

Turn on subtitles for multi-language text

## Download and Extract the BIOS update

For the GPD WIN 4 Stuttering fix, please see our guide [here](https://droix.net/knowledge-base/article/gpd-win-4-lcd-firmware-update/) for how to update and install the fix.

You can download the latest GPD WIN 4 BIOS update file [here](https://droidbox.sharepoint.com/:u:/s/Purchasing/ERjXPLgc8qJKigLco-dW1goBclLVoRiNKe_N2zoluueSgQ?e=afv0lH). Once you have downloaded it, extract the contents of it to your PC. There should be an *Upgrade\_instructions.txt* and *startup.nsh* files, and two folders; *EFI* and *WIN4\_19\_0606A*, or a similar name depending on firmware version).

You can now copy the files and folders to your FAT32-formatted USB stick.

GPD WIN 4 BIOS update files

You can now safely eject the USB stick and plug it into your GPD Win 4. Connect the power supply to the GPD WIN 4.

## Installing the BIOS Update

Power on the GPD WIN 4 then immediately press whilst holding the FN key, and tap the F7 key during the startup. You may need to tap the F7 key a few times to get the boot menu. Once the menu appears, select the USB drive as the boot device.

The BIOS update will now proceed and take a few moments. During this time, do not remove the USB stick or switch off the GPD WIN 4.

Once the update has been completed, the GPD WIN 4 will shut down.

## The first boot will take a little longer than usual

You can now switch on the GPD WIN 4 when you are ready to use it.

Please note that due to the BIOS update effectively resetting the BIOS, the first boot may take a few minutes and show a black screen while it is updating. Do not switch it off during the process. Subsequent boots will be at the normal fast speed you are used to.