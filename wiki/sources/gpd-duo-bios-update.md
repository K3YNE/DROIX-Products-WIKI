---
title: "How to update the GPD Duo BIOS"
type: source
subtype: kb-article
slug: gpd-duo-bios-update
brand: gpd
product: gpd-duo
source_url: "https://gpdstore.net/kb/gpd-duo-support-hub/kb-article/how-to-update-the-gpd-duo-bios/"
published: 2025-03-21
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, gpd, gpd-duo, bios]
---

Updating the BIOS for the first time can seem intimidating, but our step-by-step guide makes the process simple. Follow along to update the [GPD Duo](https://gpdstore.net/laptops/gpd-duo/) BIOS to the latest version with ease.

To begin, you’ll need a USB flash drive—any size should work. Format the drive to FAT32 to prepare it for the update files. To do this, right-click on the USB flash drive, select “Format,” choose FAT32 as the file system, and click “Start” to complete the formatting process.

Next, download the BIOS files. Please note that that there are two different firmware updates depending on which CPU (HX 370 or 8840U) you have. DO NOT install the wrong firmware, as installing so could render the device inoperable. You can verify your model by checking the label on the back of the device or by viewing the CPU information in Windows Task Manager. If you’re unsure and purchased your GPD Duo from us at GPD Store, contact our support team with your order number, and we will confirm your model for you. We do not accept responsibility if something goes wrong.

Ways to identify your CPU on your device:

* To access Task Manager, **right click** on the **Windows Start** icon and choose Task Manager from the list. Alternatively you can type Task Manager in the Windows Search Bar.
* You can find your CPU model in Windows quickly through **Settings (About your PC)**, or the S**ystem Information app (msinfo32)**, all showing the processor’s name and spec.  
  Using Settings (Easiest for Windows 10/11)  
  Click the Start Menu (Windows icon) and type **about**.  
  Select **About your PC** from the results.  
  Look under “**Device specifications**” for the Processor entry, which lists your CPU model (e.g., Intel Core i7-10750H).

Task Manager CPU



|  |  |  |
| --- | --- | --- |
| **MODEL** | **RELEASE NOTES** | **DOWNLOAD** |
| GPD DUO **HX 370 CPU** | Optimized sleep-related issues, and the BIOS Main page has added battery charging threshold management. | [D1(370)\_BIOS.V2.16.rar](https://droidbox.sharepoint.com/:u:/s/Purchasing/EagRtnk7llNKlXVaX2HEu5YBI8peQlp1ZVmWge3CPdkJKA?e=hBjDwU) |
| GPD DUO **8840U CPU** | Optimized sleep-related issues, and the BIOS Main page has added battery charging threshold management. | [D1(8840\_key)\_BIOS.V3.08.rar](https://droidbox.sharepoint.com/:u:/s/Purchasing/EU3yrx7TyuFKohhGKMVerK4B-747pS_DOYUuyXiabmrmzA?e=VS9jct) |

After copying the contents to the USB flash drive, power off your [GPD Duo](https://gpdstore.net/laptops/gpd-duo/). Ensure the device has at least 40% battery life before proceeding with the BIOS update, and we strongly recommend keeping it plugged in during the process to prevent any interruptions.

Next, turn on the [GPD Duo](https://gpdstore.net/laptops/gpd-duo/) and hold the **F7** key until the boot menu appears. In our example image, the USB flash drive appears as the second option in the menu. However, your flash drive’s name and position in the list may vary. Select your USB flash drive to continue with the update.

GPD Duo Boot Menu

The BIOS update process will now begin. During the first stage, you will see progress text displayed on the screen.

GPD Duo BIOS Update first part

Once this stage is complete, you will be prompted to press **Y** to continue.

GPD Duo BIOS Update first part prompt

After a brief pause, the second stage of the update will start. At this point, the screen may appear inactive for a short time—**do not turn off the GPD Duo.**

GPD Duo BIOS Update second part

Shortly after, the update process will resume, and you will see progress indicators on the screen. This stage will take a few minutes to complete. **DO NOT power off the GPD Duo during this process.**

GPD Duo BIOS Update second part progress

Once the update is finished, the [GPD Duo](https://gpdstore.net/laptops/gpd-duo/) will automatically shut down. You can now turn it back on and enter the BIOS by pressing the **ESC** key during startup. On the BIOS screen, you can verify the update by checking the **BIOS Information Project Version.** In our example, the update has been successfully applied to version **2.16.**

GPD Duo BIOS Update complete

At this point, you can exit the BIOS and resume using your [GPD Duo](https://gpdstore.net/laptops/gpd-duo/) as normal.
