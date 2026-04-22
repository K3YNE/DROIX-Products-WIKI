---
title: "How To Install and Update Windows 10 & 11"
type: source
subtype: kb-article
slug: how-to-install-and-update-windows-10-11
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/how-to-install-and-update-windows/"
published: 2022-07-05
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix, windows, installation]
---

This guide will explain how to install and update [Windows Operating System](https://www.microsoft.com/en-gb/windows/windows-11) onto your [Mini PC](https://droix.net/product-category/mini-pcs/) or [Windows device](https://droix.net/product-category/handhelds/handheld-gaming-pcs/). We will also go over AMD and Intel driver installations and hardware drivers specific to your model.

If you have a GPD device, we recommend installing the GPD versions which include Windows and GPD drivers.

## Overview

We recommend installing the version of Windows that you originally had installed. You can always easily upgrade from 10 to 11 providing your device meets the requirements.

Once you have installed either Windows 10 or 11, we next recommend installing the device’s hardware drivers. This will enable hardware such as Wi-Fi and Ethernet drivers, correct screen orientation and touchscreen on handheld devices etc. This will also allow you to connect to the internet to update your OS and firmware etc.

After you have installed the hardware drivers we recommend performing a Windows Update to bring the version of Windows and its software up to the very latest version.

Finally, we recommend installing either the AMD or Intel (depending on your device’s hardware) assistant software which will update the processor and graphics drivers.

---



---

## How to install Windows 10

### What you will need

* 16GB+ [USB](https://en.wikipedia.org/wiki/USB_3.0) stick
* [RUFUS](https://rufus.ie/en/) ISO installer – easily create bootable USB drives
* If you are installing on a PC gaming handheld we recommend using a USB keyboard and mouse as onscreen keyboards and touchscreens may not work until the drivers are installed.

### Step 1

Go to [rufus.com](https://rufus.ie/en/) then download and install Rufus from there.

Rufus Website

### Step 2

The direct download for the Windows 10 ISO is no longer made available by Microsoft. But you can download their “Windows 10 installation media” tool which will create the ISO for you. You can download the tool here. Follow the instructions on the page and when prompted to “Select which media you want to use” choose the **ISO file**.

### Step 3

Once the ISO is downloaded, connect the memory stick and open Rufus. First, ensure your memory stick is the right one shown by checking the **Device** drop-down menu.

On the **Boot Selection** drop-down menu, ensure that “Disk or ISO image” is selected. Click **SELECT** to the right of it and navigate to the ISO image downloaded earlier

Double-check that you have selected the correct Device and Boot Selection ISO file. Then click the Start button, and a message will appear, click **OK** to start.

Rufus device properties

The memory stick will now be written onto, this process can take 10-20 minutes depending on the speed of your USB stick. You can see the progress bar at the bottom of the software.

### Step 4

Once the process has finished. Eject the USB stick and plug it into your mini PC or handheld USB port.

### Step 5

Switch on your device and repeatedly press **ESCAPE** and **DELETE** on your keyboard straight afterwards, it will boot to the BIOS menu. Press Right on the keyboard until the **Save & Exit** menu and then highlight your USB stick, Pick partition 1 and press **ENTER/RETURN**. The device may reboot and then load the Windows Setup menu.

A BIOS screen, yours may be slightly different in content

### Step 6

Some steps may be slightly different, missing or new depending on the options you choose. These are the standard options when installing Windows.

When you get to the Setup screen, change the language to whatever you desire. Then proceed to the Next screen. If you have already used your device with Windows previously, select the option that states you already have a key. If not, enter your license key in the text bar.

Initial Setup menus

Choose your operating system, if you are unsure, select Windows 10 Home. When you confirm this, choose **Custom Install** when prompted for the installation type.

Choosing your Windows version

Click all the partitions on the drive and **Delete** them until you have one drive named “Drive 0 Unallocated Space”. Click on **New** then click on **Apply** which will format it ready for the Windows installation.

Deleting any old partitions and creating new ones

When you are done, click **Next**. Windows will now proceed to install and set up. This will take several minutes. It may either switch off or reboot a few times until you see the Windows Setup screen. It will then take a few minutes to load and it may reboot again once or twice during the process.

Installing Windows

### Step 7

Once the initial installation process has been completed you can choose your Region, Keyboard Layout. You can optionally choose a Wi-Fi point to connect to and you can create your profile, name your PC and create a password.

Main Windows Setup

The device will now finish installing and setting up Windows 10. This may take some time so be patient. You can now skip to the Adding or updating hardware device drivers part of this article.

---

## How to install Windows 11

Here you will find out how to install [Windows 11](https://www.microsoft.com/en-gb/windows/windows-11).

### What you will need

* 16GB+ USB stick
* If you are installing on a PC gaming handheld we recommend using a USB keyboard and mouse as onscreen keyboards and touchscreens may not work until the drivers are installed.

### Step 1

You can download the “Windows 11 Installation Assistant” from <https://www.microsoft.com/en-gb/software-download/windows11>

Download Installation Assistant

Once downloaded and installed, load the Installation Assistant software. You can select the Language you want then press **Next**. When it asks you what media you want to use, select the “USB flash drive” option. Please ensure you use the correct one and proceed. The software will then download and copy the Windows 11 installation to your USB stick. Once it has finished, you can remove the USB stick.

### Step 2

Insert the USB stick into the port in your mini PC or handheld. Switch it on and repeatedly press **ESCAPE** and **DELETE** on your keyboard, it will boot to the BIOS menu. Press Right on the keyboard until the **Save & Exit** menu and then highlight your USB stick. Pick the “Partition 1 ” for the USB stick, and press **ENTER/RETURN**. The device may reboot and then load the Windows Setup menu.

A BIOS screen, yours may be slightly different in content

### Step 3

Choose your region and keyboard layout.

Choosing your region and language

### Step 4

Make sure you choose the operating system version here that you previously had installed. If you are unsure choose Windows 11 Home.

Choosing your Windows version

### Step 5

Windows will proceed to install and set up ready for first use. This can take some time and the device may reboot a few times during the process.

---

## Adding or updating hardware device drivers

We recommend first adding or updating drivers specific to your device when you first boot Windows. This will add drivers for the hardware in your device such as video output, W-iFi, and Ethernet for example.

Each device will have its own drivers. **You should only install drivers that are made for your device!** Installing the wrong drivers may cause hardware not to be recognised or other issues. You can find your device drivers on the below websites.

AYANEO devices – <https://www.ayaneo.com/support/download>  
ONEXPLAYER devices – <https://onexplayerstore.com/blogs/driver-software/>  
GPD devices – <https://www.gpd.hk/download>  
MINISFORUM devices – <https://www.minisforum.com/front/support>  
BEELINK devices – <https://www.bee-link.com/cms/support/productlist?id=7>  
GMKtec devices – <https://www.gmktec.com/pages/firmware-update?spm=..index.header_1.1>

We recommend downloading all drivers for your device’s model. Once you have them, follow the install instructions for each driver download. If there are no instructions there is usually a .exe, .bat or .cmd file you need to run and it will install the drivers.

---

## Updating Windows 10

Windows 10 updates

First, make sure you’re connected to the internet. Press the **Windows button**, then **Settings**, click Update and Security, and then click “Check for updates”. Click on updates, and then Windows will download and install all updates, let it download and install everything. This can take some time for it to download and reinstall, so be patient. You may also need to restart your device and check again for any further updates.

---

## Updating Windows 11

Windows 11 updates

Updating Windows 11 is very similar to updating Windows 10. First, make sure you’re connected to the internet. Press the **Windows button**, then **settings**, click update and security, then click check for updates. Click on updates and they will be downloaded and installed, let it download everything. You may also need to restart your PC and check for additional updates or patches.

---

## Updating AMD drivers

In this part, we will show how to update the AMD drivers. You will only need to install these if you have AMD hardware.

### Step 1

Go to [www.amd.com/en/support](http://www.amd.com/en/support). There will be an option to download “Auto-Detect and Install for Windows 10/11”. Download and install this application.

AMD drivers website

### Step 2

Open the application, then follow the prompts to install it. The software will prompt for which items to install or update, and choose to install everything.

It will then download the latest drivers and install them. Depending on how many updates are available, please give it some time to complete. Once it has finished, you can reboot your PC.

AMD Driver installation

---

## Updating Intel drivers

In this section, you will learn how to install Intel drivers. You only need to update these if you have Intel hardware.

Intel driver website

### Step 1

Open up your browser and go to [Intel® Driver & Support Assistant](https://www.intel.co.uk/content/www/uk/en/support/detect.html) and click the **download now** button, proceed to follow all of the prompts to begin the installation. After the Install is finished you will need to restart your device.

Intel driver software installation

### Step 2

Once loaded, open your **Windows search bar** and open the **Intel driver and support assistant** from there. The software will then check for any software updates available. Select all of the updated drivers or software.

Load the Intel driver and support assistant software

### Step 3

After the download has been completed, the assistant will then install all of the software required to keep your drivers up to date. When it is all finished your mini PC will then restart again, once that is done you are finished!

Intel driver installation

---

## Installing any other software or drivers

Depending on what external peripherals you are using, you will need to install the drivers and/or software for them. It is out of the scope of this guide to list every software or driver but you can usually find drivers on the manufacturers’ website in their Support section.

We hope this guide has served its purpose in helping you learn how to install everything you need for your mini PC or handheld! We stock a range of [Mini PCs](https://droix.net/product-category/mini-pcs/) and [handheld game consoles](https://droix.net/product-category/handhelds/handheld-game-consoles/) and this guide applies to each one that is capable of running Windows.
