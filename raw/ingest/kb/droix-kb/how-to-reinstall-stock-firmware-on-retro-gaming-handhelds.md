---
title: How to Reinstall Stock Firmware on Retro Gaming Handhelds
source_url: "https://droix.net/knowledge-base/article/stock-firmware-retro-handhelds/"
source_site: droix.net
type: kb-article
date: 2023-06-07
wp_id: 2823
---

For any number of reasons, you may need to roll back your firmware and install the stock version. Be it a device getting bricked, unstable update, preparing to sell or just a fresh start. The firmware on your device is an important collection of software that provides low-level control for a device’s specific hardware. Naturally an important installation, and one you want to get right. In this guide, we’re going to go through the process of formatting and preparing your device and installing the stock firmware onto it. This process is different for many devices so each process and what devices it’s for will be listed below, make sure to follow along for your device.

## Prepare your MicroSD Card

The first thing we need to do is prepare the [MicroSD Card](https://droix.net/product-attribute/storage-technology/micro-sd/).

Power off your device and remove the [MicroSD](https://droix.net/product/micro-sd-card-tf/) card by pushing it further in, it will click out and you will be able to pull it out.

Once it’s out you can plug it into your PC, this can be done in a few different ways. You can use an SD card converter, as we did in the photos, the included MicroSD to USB adapter that comes in the box or even just straight into the PC if your computer has a MicroSD card slot. Any method is perfect.

Once it’s in, make sure your computer can see it by going to This PC and confirming it’s there. This process will remove all data on the card, so it would be a good idea to back it up by going into the SD card and copying the contents to a folder on your computer.

Once you’re sure the computer can read it, we’re going to format the card. This will delete everything currently saved on it. Optionally I recommend you make a backup. This is done by creating a new folder on your PC and dragging the contents over.

Once you’re ready to format we need to install a piece of software called Rufus which will help us. You can download it from this link [here](https://rufus.ie/en/).

Scroll down and download the latest version for your PC. If you’re not sure what version is best go with the Standard Windows x64 platform as that is the most common. Run the .exe file when it downloads.

When you open the program you’ll be greeted with this screen.

We’ll need to ensure the format is set up first. Ensure your device is the microSD card you’ve plugged in. Set boot selection to ‘Non bootable’. Set the partition scheme to ‘MBR’. The target system to ‘BIOS or UEFI’. Give the volume an appropriate label, such as ‘Firmware-Installer’ and finally set the file system to ‘FAT32’. You’re ready to click ‘Start’. When you do so a warning will pop up letting you know the device will be erased. Click ‘OK’.

Your device is now formatted, and we can get ready to install the stock firmware. This is where the process forks for all devices. Follow along with device-specific instructions.

Find your device from the list of manufacturers below:

* [Miyoo](#h-miyoo)
* [Anbernic](#Anbernic)
* [Retroid](#h-retroid)

## Miyoo

This section will cover the [Miyoo products](https://droix.net/product-attribute/brands/miyoo/) such as the Miyoo Mini and the [Miyoo Mini Plus+](https://droix.net/product/miyoo-mini-plus/). The process for these devices is very similar but may not be one-to-one, as the firmware is a low-level piece of software that interacts directly with the hardware, it is necessary to ensure that the software is made specifically for your device.

### Installing Stock Firmware on your Miyoo Mini

The first thing you need to do is download the firmware, you can do this from [here](https://droidbox.sharepoint.com/:u:/s/Purchasing/EdOIz4W8PtJJvbmtx6Riop8BlVnzN6lPB6CQzEDd_XJ_Ww?e=iTBJFN). This will download a ZIP folder called ‘Firmware 0419’. Extract its contents by right-clicking and pressing ‘Extract All’. Follow the steps to extract the contents.

Inside you will find three files, two ‘read me’ files and one .img file. The readme file is below:

```
Upgrade Tutorial
1. Copy the img image file to the root directory of the SD card
2. Keep the machine turned off, insert the copied SD card into the machine
3. Plug in the USB charging cable, wait for a few seconds and a rocket icon will appear to indicate that the upgrade is in progress (the charging cable cannot be unplugged during the upgrade process)
4. After the upgrade is completed, a charging pattern will appear (delete the SD card img image file)
```

To reiterate, copy the .img file to the now formatted SD card. Ensure that it is the only thing on the card and not in any folders. Safely eject the MicroSD card and put it back into the Miyoo Mini by clicking it in. **Do not press the power button** simply plug in your charging cable and the device will automatically power on and complete the update. When it has done so you can delete the .img file from the device by putting it back into your computer and deleting it or from the device itself if you’re able to.

### Installing Stock Firmware on your Miyoo Mini Plus+

The process for installing stock firmware on the Miyoo Mini Plus+ is slightly different. Let’s get started. You can download the files necessary [here](https://droidbox.sharepoint.com/:u:/s/Purchasing/EbHEPDBP4gJLqN4hSmvX3aABLk-6PF8eoX94AQjxjLFSoA?e=9q6nFW). This will download a file called ‘MINI+No games.zip’. As it is a zip file you will need to extract its contents. Inside the extracted folder, you may need to go another folder deep, you will find the firmware contents, as seen below.

You need to copy **all** of these folders to the **root** of the SD card. That means that the only thing stored on the SD are the files above, they shouldn’t be in any folders or anything like that. Just the files above. I believe in you.

Once that is done, you can safely eject the MicroSD card and, put it back into your Miyoo Mini Plus+ and boot it up. It will boot up and you can start using it.

## Anbernic

This section of the guide will focus on [Anbernic devices](https://droix.net/product-attribute/brands/anbernic/). The process for these devices can vary quite significantly so be sure to find your device and follow along with the process closely.

### Installing Stock Firmware on your Gaming Handheld

The firmware download for all devices can be found below. The guide can be used for all devices but will focus on the RG35XX.

|  |  |
| --- | --- |
| RG35XX | [Products – RG35XX系统及升级工具v1.0-20230606T143610Z-001.zip – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/EYEagpefHklDon2RK3OyMF0BqwBrf9O1i4skfZm2AAtSJg?e=NKlc1t) |
| RG300X | [300x-anberNIX-001.zip](https://droidbox.sharepoint.com/:u:/s/Purchasing/Ea6LpNQdzYtFgHUovZolE6QB6dIxNtv223ljy_tRGpGdOg?e=Kq47xe) |
| RG350 | [Products – RG350-orig-img-may-2020.img – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/EXPnrx1TgUhGm1TecftmOb4BVkWAk09lLI7DXwVPeMdgkg?e=PPvO1y) |
| RG350M | [Products – RG350m-HDMI-orig-img-may-2020.img – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/EXzNLh1CjNRNhILv3eIQ4nUBnwMKsXNRyR--LPVgq7tc7A?e=JbikAu) |
| RG350P | [Products – RG350-orig-img-may-2020.img – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/EfRrANske1lFpgT1VGzuS40BSt6C3R5hF4BIeMw4xV0lsQ?e=tkR6ig) |
| RG351M | [Products – RG350-orig-img-may-2020.img – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/EZcdhiSpgBJEnzsxBHXoobUBtVstOYTsIjxSD6P2Cf7zpw?e=ayVSq8) |
| RG351MP | [Product](https://droidbox.sharepoint.com/:u:/s/Purchasing/Ee2uF4suHvhIlyx0bPyH-70BJKOEHPYBFdBZvZChOCBi-w?e=MAvIjB)[s](https://droidbox.sharepoint.com/:u:/s/Purchasing/Ee2uF4suHvhIlyx0bPyH-70BJKOEHPYBFdBZvZChOCBi-w?e=pUh7Ry) [– RG351MP\_INT\_20210923.img – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/Ee2uF4suHvhIlyx0bPyH-70BJKOEHPYBFdBZvZChOCBi-w?e=CAfAr1) |
| RG351P | [Products – RG351\_STOCK\_FW\_CLEAN.img – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/EZdejwVUvIpAr_Hz_xpxm_IB_Nl7lYE8ZMrIXF6EixnXjA?e=q1fTag) |
| RG351V | [Products – 351V\_20210329\_INT.img – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/EZVte5ldYpNIpeuOvB5_9H8BsXj6f_iqHrgVx1QpHBx8zw?e=tLjzaL) |
| RG353P | Linux: [Products – anbernic-rg353-31-20230403.img-001.gz – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/EfU42Y9DnaFOiPmw2xuKJwMBA6dqk4Pt6nkxvr7ihyZWRQ?e=MdCYxJ) Android 11: [Products – RG353-Android11-V1.17E-20230109.zip – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/ESvmGJhq2ClLo0flbFTj7ZsByimjJvIyALI9CgUm-CROog?e=B7utiP) |
| RG353V | [Products – rg353v and rg353m google play store pack.zip – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/EaEvthJ6OTdGsxQrk497M3cB8Fe0prjZfh9CygZZwWDkeQ?e=ZFFuMh) |
| RG503 | [Products – anbernic-rg503-31-20221102.img-001.gz – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/EZ1fAv7fh8xFqXtqyjJG2eIBCl4juG5CHuYmkWeRNQtpbA?e=e4LLX7) |
| RG505 | [Products – RG505\_ota\_from\_V1.20\_to\_V1.21.zip – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/EWwZYz5GBjJBoLnyng5PnpkBr9dPV3_7AvV0VH9bbY4RCw?e=wZhyxc) |
| RG552 | Android: [Products – RG552-Android-v1.11e.zip – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/Ea4Be-NahqNCkv1IweXB8JcBan50pVFObak2owYnqLZEuA?e=4hOAip) Linux: [RG552-LINUX-FW-20211207.img](https://droidbox.sharepoint.com/:u:/s/Purchasing/EWcCJ7qj1NNKtt_W-kI9NuIBuqD3hMoTzAhDnjyRb3ArEQ?e=BNVG7i) |
| RS07 | [Products – RS-07-console-full-200715.zip – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/EVrvpsPlFNZHsjMETiS5SZEB4I_lTpWYgWK-qcXbhPaL6A?e=4BpTDI) |
| RS-97 Pro | [Products – ProFirmwareWithGames.img – All Documents (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/EThBnOgQ1tBBn8MWiKT3R0sBlXK9mO_t70veUUOyyvRT2A?e=Of79EH) |
| RG Nano | [Anbernic-sdcard-1.0.1.img.zip (sharepoint.com)](https://droidbox.sharepoint.com/:u:/s/Purchasing/EVdJoOWQAp5GmClTitthE5kBRKYV7ujTiWU_SPaVogLGYA?e=84XXGu) |

Open Rufus

Ensure that your MicroSD cards are selected under Device. click on ‘SELECT’ and find the .img file that you extracted and open it. Rufus will auto-fill the rest of the requirements. Click ‘START’. It will ask for permission, click OK. This will flash the stock firmware image file to your MicroSD card. Give it a minute or two to complete. Once it is done you can safely eject the MicroSD card and put it back into your device and boot up.

You can also install customs ROMs and BIOS’ by following our guide [here](https://droix.net/knowledge-base/article/how-to-add-new-games-and-roms-to-your-gaming-handheld/).

Now go and play all your classic favourites!

## Retroid

Below are our guides for [Retroid](https://droix.net/product-attribute/brands/retroid/) devices, follow along for your device-specific instructions.

### Reinstall Firmware on your Retroid Pocket 2

The Retroid Pocket 2 comes with Android 6.0 installed, this guide will show you how to follow the official update to [Android 8.1](https://droix.net/product-attribute/operating-system/android-8-1/).

The Retroid Pocket 2 is set apart from its contemporaries in the “retro handheld” space by being one of the few devices that runs Android. This makes it slightly more involved to update or install custom firmware compared to devices such as [ANBERNIC’s RG351P](https://droix.net/product/anbernic-rg351p-games-console/), for which updates are just a matter of [flashing an SD card](https://droix.net/knowledge-base/rg351-custom-firmware-installation/).  
There are some differences between Android 6.0 and 8.1 (in terms of app compatibility, etc.), so you might not feel as though an update is necessary. If not, you can also use this guide as a way to simply re-flash the device. For those unfamiliar with Android devices, “flashing” is just another term for installing firmware on the device. In this context, it is like reinstalling Windows on your PC. A useful troubleshooting technique.

You will need a Windows PC or Laptop, a USB A-to-C cable, and you will also need a fair few files before starting, which are all as follows (**most of these files can be found at [-> this link <-](https://go.droix.net/RP2-FW)**):

* **Retroid OS Backup Software – *RP2 Key Backup Tools.zip***  
  Software for backing up the unique Retroid OS key for your device. Without this key, you will not be able to receive OTA updates from Retroid or access the full features of Retroid OS.
* **SPFlash** – *SPFlashWin.1832.zip*  
  The software we’ll use to install the updates.
* **The Actual Firmware** – *RP2-6.0v5.zip* (Android 6.0) **OR***RP2-8.1v3.zip* (Android 8.1)  
  You can choose between Android 6.0 (what is already installed) or Android 8.1 (the update).
* **Google’s Android USB Drivers** –*usb\_driver\_r13-windows.zip*  
  Without these, your PC will not be able to connect to the Retroid Pocket 2. You can also grab these directly from Google here: <https://developer.android.com/studio/run/win-usb>
* **MediaTek Preloader Drivers** – MT65XX-Preloader-drivers.rar  
  Required for SPFlash to operate in conjunction with the Retroid Pocket 2.
* **File Archival Software** – *<https://www.7-zip.org/>*  
  Most of these files are .zip so they can be opened natively in Windows 10. For anything else, however (.7z, .rar, etc.) you’ll need specialized software. We suggest 7zip, as it is free, open-source, lightweight, and non-intrusive. You can use alternatives such as WinZip and WinRAR if you wish, however.
* **A stock SD card**– <https://droidboxforums.com/threads/stock-sd-card-for-retroid-pocket-2-download-link.22039/>  
  You’ll need the SD card in the unit to be loaded up with the stock files (Retroid OS-related things primarily)

**WARNING:**Please ensure that you follow this guide exactly. If you use the wrong files, disconnect the device during the process, or otherwise fail to follow the outlined steps in some form. **You risk bricking your device and rendering it inoperable.** DroiX is NOT responsible in the event this occurs.

Now that you have all the files, we’ll get this guide started.

Download and install the Android USB and MT65xx Preloader drivers.

Extract the zip file, then right-click android\_winusb.inf. Click install.  
You will probably see a pop-up window requiring you to confirm the installation. This is just a security measure (you should only install apps from trusted sources). Click “Install”.

Download, extract the zip file, then click “install.exe”. The drivers will install, you’ll get a short message confirming they’re installed, and you’re good to go!  
(If you get a warning indicating that the drivers may not have been installed correctly – ignore it)

First, download the backup tools (*RP2 Key Backup Tools.zip*). Extract the contents.

Then, power on your Retroid Pocket 2 and enable USB Debugging. You can do this by:

1. Open Settings
2. Scroll down to the System section, select “About phone”
3. Select “Build number” 7 times. You’ll then get a notification that “You are now a developer”
4. Back out to the main Settings menu, and “Developer options” will now be available. Select it.
5. Scroll down and make sure “USB debugging” is enabled.

Now connect your Retroid Pocket 2 to your PC. Open the backup tools folder, and double-click the “RP2 Key Backup.bat” file to run the backup process. If successful, a “device\_key” file will be generated.

Important: **Make sure that your Retroid Pocket 2 is powered off during this step**, **and that the stock SD card (or a card you’ve prepared with the same files) is inserted.**

First, download the firmware for Android 6.0 (*RP2-6.0v5.zip*) or Android 8.1 (*RP2-8.1v3.zip*) respectively. Extract them.

Download, and extract SPFlash (*SPFlashWin.1832.zip*). Then run flash\_tool.exe to open the software. You’ll be met with a screen like this:

Under “Download-Agent”, select the “**MTK\_AllInOne\_DA.bin**” file, this will be found in the SPFlash folder.  
For the Scatter-loading File, navigate to the 6.0 or 8.1 firmware folder you downloaded previously, and select the “**MT6580\_Android\_scatter.txt**” file.

Now depending on what firmware you have here, the next step will differ.

* For the drop-down box (see under “**Authentication File**“, **if you are changing to a different Android version** (i.e., 6.0 -> 81.), select “**Format All + Download**“
* **If you are re-flashing or updating to the same version**, change the box to “**Download only**“, then scroll down the list of options and **uncheck** the “userdata” option.

Now click the “Download” button at the top of the program. You can then connect your **powered-off** Retroid Pocket 2, and the process will automatically be carried out.

Once finished, disconnect your Retroid Pocket 2 from your computer.**It will not boot if it is connected.**

Now boot up your system once more. It will take longer than usual to boot up, and when it does, it will boot into the Retroid OS. Hold the HOME button and select “switch system” from the menu to be taken back to the regular Android OS.

Connect your Retroid Pocket to your PC, open the backup tools folder from earlier, and then run the “**RP2 Key Restore.bat**” file. Your RP2 will then reboot automatically once the process is complete.

With this, you will have now completed the re-flash/upgrade process. Enjoy your fresh Retroid Pocket 2!

The first time you reboot into Android, there may be missing apps. If you leave the system for a short while, it will automatically start running a script to re-install the selection of stock apps on the device. After this is complete, it will reboot automatically.

### Reset Android on your Retroid Handheld

Sometimes you don’t need to completely reinstall your firmware and operating system and just to want to get a fresh start on a device, Whether you’re selling it, giving it away, resolving an issue or just need a refresh this guide will show you how to reset all of your Retroid and Android devices.

From the home page of your Retroid device, you need to click on ‘Settings’. If you cannot find the Settings icon, swipe down the notification shade, and then swipe down again. You will find a settings icon in the bottom right of the extended shade.



Once you’re in the settings, scroll all the way to the bottom and open ‘System’.

From here click on Advances -> Reset options



Erase all data (factory reset)

Press Erase data, if your battery is less than 30% you will get a warning. Simply ensure your device is plugged in and continue. Erase data.



The device will now restart. If you are selling or giving your device away this is where you stop. Let it erase and restart and when it boots up again hold down the power button to turn it off and you’re done.

If you are keeping the device, however, we will continue with the setup.

The device will now boot up, you will see the Retroid boot logo as it loads.

The setup program will automatically boot and begin. Follow along with your preferred settings and options.

Connecting to the internet and enabling Google Play Services is recommended.

You will come to a screen that asks which apps you wish to preinstall. Go through and select which ones you want. If you’re not sure I recommend selecting them all.

The selected apps will then begin installing.

Select your launcher of choice. Retroid’s custom one and Android’s built-in one.



You’ve now finished and start enjoying your device!