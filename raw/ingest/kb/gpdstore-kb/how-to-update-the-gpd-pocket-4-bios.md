---
title: How to update the GPD Pocket 4 BIOS
source_url: "https://gpdstore.net/kb/gpd-pocket-4-support-hub/kb-article/how-to-update-the-gpd-pocket-4-bios/"
source_site: gpdstore.net
type: kb-article
date: 2025-03-07
wp_id: 1073923
---

Our step by step guide on how to update the [GPD Pocket 4](https://gpdstore.net/gpd-mini-laptop/gpd-pocket-4/) BIOS will walk you through the process of doing so.

You will need a USB flash drive, any size should do. Format the memory stick to prepare it for the new files. **Right click** on the drive of the USB flash drive, choose **Format** and then **Start** to format it.

**Next you will need to download the BIOS files. There are two versions depending on which processor your GPD Pocket 4 BIOS has. You can check by the label on the back of the device to confirm, or from within Windows Task Manager CPU. Or if you are unsure and purchased the Pocket 4 from us at GPDSTORE, please contact support with your order number and we can check. We do not accept responsibility if something goes wrong.**

Ways to identify your CPU on your device:

* To access Task Manager, **right click** on the **Windows Start** icon and choose Task Manager from the list. Alternatively you can type Task Manager in the Windows Search Bar.
* You can find your CPU model in Windows quickly through **Settings (About your PC)**, or the S**ystem Information app (msinfo32)**, all showing the processor’s name and spec.  
  Using Settings (Easiest for Windows 10/11)  
  Click the Start Menu (Windows icon) and type **about**.  
  Select **About your PC** from the results.  
  Look under “**Device specifications**” for the Processor entry, which lists your CPU model (e.g., Intel Core i7-10750H).

Task Manager CPU

Next you will need to download the BIOS files. There are two versions depending on which processor your GPD Pocket 4 BIOS has. You can check by the label on the back of the device to confirm, or from within Windows Task Manager CPU. Or if you are unsure and purchased the Pocket 4 from us at GPD Store, please contact support with your order number and we can check.

|  |  |
| --- | --- |
| **MODEL** | **DOWNLOAD** |
| GPD Pocket 4 **8840U** CPU | [P4(8840U)-L\_BIOS.V3.06\_EC.V1.11.rar](https://drive.google.com/file/d/19b0cV80NS-v8WJFKYdvFAgdDLhpnSG7R/view?usp=sharing) |
| GPD Pocket 4 **HX 365** and GPD Pocket 4 **HX 370** CPU | [P4(370\_365)\_BIOS.V2.10\_EC.V1.13\_250627.rar](https://drive.google.com/file/d/1BdFEi57OFLDmYv3l-5PZxJj4fFBA7rke/view?usp=drive_link) |

**Please note:** the process for updating the BIOS is the same regardless of which processor and BIOS files you are installing. For simplicity we will be showing the process for updating the HX 370 CPU as this is the most popular model, but it will apply for the 8840U and HX 365 models with different filenames for example. We highly recommend keeping the GPD Pocket 4 charged while performing any upgrades.

First extract the download archive. You will have two folders similar to below

Extracting the files

## BIOS Update

Enter the **P4\_BIOS.vxxxx** fodler and open the **P4\_xxxx\_GPD.exe** file. A window with some information on what to do and not do during the BIOS update will be displayed.

GPD Pocket 4 BIOS update checklist

Once you have read the information, press any key to proceed with the upgrade. The first stage will take a few moments and once completed you will be prompted to confirm to restart the device to continue. Choose **Y**.

GPD Pocket 4 BIOS first stage update

Your GPD Pocket will now reboot and proceed with the BIOS update. Do **NOT** switch off your device during this process!

GPD Pocket 4 BIOS updating main firmware

The process will take around 3 to 5 minutes to complete. Once completed, the Pocket 4 will reboot and take a few moments to update. The screen may switch off during this process, do not switch off your device until at least the Windows log in screen has appeared.

## EC Firmware Update

The second part of the process is to update the EC firmware. Enter the **P4\_EC.Vx.xx** folder and copy all of the contents to your USB flash drive

Copy the contents to the flash drive

Once the contents have copied over, switch off your GPD Pocket 4. Now switch on the GPD Pocket 4 and hold the **FN key + F7** key until the boot menu appears. In our image below, the USB flash drive is the second option on the menu. Your flash drives name and menu option may be different. Choose your flash drive to proceed.

GPD Pocket 4 BIOS Upgrade Boot Menu

Some progress text will briefly appear on screen, you can wait a few seconds or press any key to continue.

GPD Pocket 4 BIOS EC Upgrade

The upgrade process will start and the screen will update on the progress. The process should only take a minute or two.

GPD Pocket 4 BIOS EC Upgrade

Once completed, the GPD Pocket 4 will power off. Wait a few moments and you can power it back on. Press the **Del** key to enter the BIOS. You can now check which BIOS and EC version you are to confirm the upgrade has completed.

In the below image we can see the BIOS is now on 2.07 and the EC is on 1.11. Your numbers may be different to different CPU or newer firmware updates.

Check it has been updated

Once confirmed you can exit the BIOS and it will reboot and load Windows. You can now continue using your [GPD Pocket 4](https://gpdstore.net/gpd-mini-laptop/gpd-pocket-4/).