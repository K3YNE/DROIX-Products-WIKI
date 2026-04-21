---
title: How to update the GPD WIN Mini 2025 BIOS
source_url: "https://gpdstore.net/kb/gpd-win-mini-support-hub/kb-article/how-to-update-the-gpd-win-mini-2025-bios/"
source_site: gpdstore.net
type: kb-article
date: 2025-03-10
wp_id: 1074305
---

Our step by step guide on how to update the [GPD WIN Mini 2025](https://gpdstore.net/gpd-handheld-gaming-pcs/gpd-win-mini-2025/) BIOS will walk you through the process of doing so.

You will need a USB flash drive, any size should do. Format the memory stick to prepare it for the new files. **Right click** on the drive of the USB flash drive, choose **Format** and then **Start** to format it.

Next you will need to download the BIOS files. There are two versions depending on which processor your [GPD WIN Mini 2025](https://gpdstore.net/gpd-handheld-gaming-pcs/gpd-win-mini-2025/) has. You can check by the label on the back of the device to confirm, or from within Windows Task Manager CPU. Or if you are unsure and purchased the WIN Mini 2025 from us at GPD Store, please contact support with your order number and we can check. We do not accept responsibility if something goes wrong.

Ways to identify your CPU on your device:

* To access Task Manager, **right click** on the **Windows Start** icon and choose Task Manager from the list. Alternatively you can type Task Manager in the Windows Search Bar.
* You can find your CPU model in Windows quickly through **Settings (About your PC)**, or the S**ystem Information app (msinfo32)**, all showing the processor’s name and spec.  
  Using Settings (Easiest for Windows 10/11)  
  Click the Start Menu (Windows icon) and type **about**.  
  Select **About your PC** from the results.  
  Look under “**Device specifications**” for the Processor entry, which lists your CPU model (e.g., Intel Core i7-10750H).

Task Manager CPU



|  |  |
| --- | --- |
| **MODEL** | **DOWNLOAD** |
| GPD WIN MINI 2025 **8840U** CPU | [Mini2025(8840U)\_BIOS.V2.08\_EC.V2.03.rar](https://droidbox.sharepoint.com/:u:/s/Purchasing/EaaQPrMuY9NKrg0dRep4M-oB-mmSZXmYCu6n8CkR9iqBRA?e=Omwq9k) |
| GPD WIN MINI 2025 **HX 365** and GPD WIN MINI 2025 **HX 370** CPU | [MiniPro(hx370-hx365)\_BIOS.V2.09\_EC.V2.06.rar](https://droidbox.sharepoint.com/:u:/s/Purchasing/EdJAWbAkUIBKtnQjj3qIalYBz1xwr5hYW1MnIk38gMrIgg?e=b9Hotx) |

**Please note:** the process for updating the BIOS is the same regardless of which processor and BIOS files you are installing. For simplicity we will be showing the process for updating the HX 370 CPU as this is the most popular model, but it will apply for the 8840U and HX 365 models with different filenames for example. We highly recommend keeping the [GPD WIN Mini 2025](https://gpdstore.net/gpd-handheld-gaming-pcs/gpd-win-mini-2025/) charged while performing any upgrades.

First extract the download archive. You will have two folders similar to below:

HX 365 / HX 370 Files

GPD WIN Mini 2025 HX 365/370 update files

8840U Files

GPD WIN Mini 2025 8840U update files

## BIOS Update

Enter the **MiniPro\_BIOS.Vx.xx** (or **Mini2025\_BIOS.Vx.xx** for 8840U model) folder and run the **MiniPro\_X.XX\_GPD.exe** (or **Mini2025\_x.xx\_GPD.exe** for 8840U model) file. A window with some information on what to do and not do during the BIOS update will be displayed.

BIOS update checklist

Once you have read the information, press any key to proceed with the upgrade. The first stage will take a few moments and once completed you will be prompted to confirm to restart the device to continue. Choose **Y**.

BIOS first stage update

Your [GPD WIN Mini 2025](https://gpdstore.net/gpd-handheld-gaming-pcs/gpd-win-mini-2025/) will now reboot and proceed with the BIOS update. Do **NOT** switch off your device during this process!

BIOS updating main firmware

The process will take around 3 to 5 minutes to complete. Once completed, the GPD WIN Mini 2025 will reboot and take a few moments to update. The screen may switch off during this process, do not switch off your device until at least the Windows log in screen has appeared.

## EC Firmware Update

The second part of the process is to update the EC firmware. Enter the **MiniPro\_EC.Vx.xx** (or **Mini2025\_EC\_Vx.xx** for 8840U model) folder and copy all of the contents to your USB flash drive.

EC firmware files

Once the contents have copied over, switch off your [GPD WIN Mini 2025](https://gpdstore.net/gpd-handheld-gaming-pcs/gpd-win-mini-2025/). Now switch on the GPD WIN Mini and hold the **FN key + F7** key until the boot menu appears. In our image below, the USB flash drive is the second option on the menu. Your flash drives name and menu option may be different. Choose your flash drive to proceed.

BIOS Upgrade Boot Menu

Some progress text will briefly appear on screen, you can wait a few seconds or press any key to continue.

The upgrade process will start and the screen will update on the progress. The process should only take a minute or two.

BIOS EC Upgrade

Once completed, the GPD WIN Mini 2025 will power off. Wait a few moments and you can power it back on. Press the **Del** key to enter the BIOS. You can now check which BIOS and EC version you are on to confirm the upgrade has completed.