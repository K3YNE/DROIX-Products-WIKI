---
title: How to Update the GPD G1 eGPU BIOS (2023)
source_url: "https://droix.net/knowledge-base/article/gpd-g1-egpu-bios/"
source_site: droix.net
type: kb-article
date: 2023-12-05
wp_id: 43579
---

Ready to boost your [GPD G1 eGPU (2023)](https://droix.net/product/gpd-g1/)? Updating the BIOS on your G1 docking station can drastically amp up its performance. But if you don’t know where to start, or just need a quick refresher, this guide makes it easy. We’ll take you through the process, from formatting your USB to every step of the installation itself.

**Please note that this guide is for the GPD G1 (GPD G1 2023) and not for the GPD G1 2024 models**. **We will update when there is a BIOS for 2024 model**

Updating your G1’s BIOS is a practical move to enhance your device. A BIOS update can fix existing bugs, and improve stability, and performance. It ensures your G1 docking station runs efficiently with the latest hardware and software, giving you a smoother, more reliable gaming and computing experience. In short, regularly updating your BIOS is key to getting the most out of your GPD G1 eGPU, keeping it compatible and functioning at its best.

## GPD G1 Setup

Before installing the Drivers or vBIOS update, we need to correctly set up our devices to ensure there are no issues during installation. Set up the G1 docking station and check that power is supplied to it. Then connect the GPD G1 to your handheld device, preferably using the GPD [USB 4.0](https://www.techradar.com/news/usb4-everything-you-need-to-know) cable supplied with your G1 eGPU. Finally, insert the [USB flash drive](https://en.wikipedia.org/wiki/USB_flash_drive) into your handheld device – if you do not have any more available ports, simply transfer the files onto the handheld device and remove the USB before connecting it to the dock. Ensure your G1 eGPU and handheld are both turned on. It is important to note that the GPD G1 will be recognized as an [AMD Radeon RX 7600M XT](https://droix.net/product-attribute/graphics-gpu-model/radeon-rx-7600m-xt/).

If you have any other issues with your docking station, please check out our [GPD G1 eGPU getting started guide](https://droix.net/knowledge-base/en-gb/article/getting-started-with-the-gpd-g1-egpu-docking-station/), linked below.

> [Getting Started with the GPD G1 eGPU Docking Station](https://droix.net/knowledge-base/en-gb/article/gpd-g1-egpu-docking-station/)

<https://droix.net/knowledge-base/en-gb/article/gpd-g1-egpu-docking-station/embed/#?secret=qE8GhYmcqu#?secret=IWM1pDpQSG>

## Reformat USB

The initial step in updating your GPD G1 eGPU involves preparing a USB for BIOS flashing. Before proceeding, be aware that formatting the USB drive will erase all its contents. Hence, it’s best to use a USB drive that’s either empty or contains no essential data. Once you’ve connected the USB to your PC, navigate to the File Explorer, right-click on the USB drive, and select the ‘format’ option (see *Images 1 & 2* below). It’s important to note that your USB name may vary based on its brand, model, or any previous renaming.

1. Right click USB device



2. Select ‘format’

Initiating the format process will cause a window to appear – change the ‘File system’ to; NTFS, FAT32 or FAT16 and press ‘Start’ to begin formatting (refer to *Image 3* below). You may be warned that any contents on the USB will be erased. Select okay (refer to *Image 4* below) and the USB will begin formatting. Once the USB is successfully formatted, a notification window will pop up, confirming the completion of the process (see *Image 5* below).

3. USB formatting menu



4. Warning message



5. Formatting complete

With the USB now formatted, the next step is to download and transfer the correct firmware and driver files onto it. These are essential for a successful update of your GPD G1 docking station.

## Download Latest Firmware & Drivers

The next thing to do is to download and install the latest Firmware and Drivers – specifically the vBIOS and AMD Graphics Drivers. You can find both direct links below. We have also linked the G1 2023 eGPU firmware from GPD’s website as an alternative link.

|  |  |
| --- | --- |
| **Firmware & Drivers** | **Link** |
| vBIOS | [Download](https://droidbox.sharepoint.com/:u:/s/Purchasing/EZNPq67lBR1EmhYmjgHyS-QB4ag9Zkmm0XIxHiTlZasHQw?e=GdyTpE), [Alternative Link](https://gpd.hk/gpdg1firmwaredriver) (2023 models only) |
| AMD Graphics Drivers | [Download](https://droidbox.sharepoint.com/:u:/s/Purchasing/Ee621n1UQqFMpWueJRqHbbEBOz76fnp_GOqDeEGByILwWw?e=djMJUR), [Alternative Link](https://gpd.hk/gpdg1firmwaredriver) |

The vBIOS firmware files are intended for the 2023 model of the GPD G1 eGPU only. Any deviation from the instructions or negligence may render your device inoperable. DroiX assumes no responsibility.

Make sure to save the Firmware and Driver files onto the USB device. After downloading you may need to unzip any folders, which can be done by right-clicking on the folder and selecting ‘extract all’ (please refer to *Image 1* below). A window will open asking you where to extract your folder, simply continue without any changes until the process is completed (refer to *Images 2 & 3* below). Once complete, eject your USB and insert it into your handheld device.

1. Extract folder



2. Select ‘extract’



3. Extraction complete

## Installing vBIOS

Navigate to your vBios folder and run `AMDVBFlash_v5.0.638-standalone-NBD-windows.exe`. Please note that your file name may differ depending on the version. Although this `.exe` file is recommended for non-GPD devices, we ran into a slight issue when flashing the BIOS using a [GPD Win Max 2 (2023)](https://droix.net/product/gpd-win-max-2-2023/), so we recommend running it just to avoid any unforeseen problems.

After running this file, the setup window will open (refer to *Image 1* below). Continue until the installation begins (refer to *Images 1, 2 & 3* below). Once the installation has finished, follow the on-screen instructions. Before finishing, you can uncheck the “open installed folder” option as we will not need to change anything there (refer to *Image 5* below).

1. AMDVBFlash setup window



2. Install location



3. Start menu shortcut



4. Installation complete



5. Close setup window

### Changing G1 eGPU Wattage

Whilst updating the vBIOS, we are also able to change the wattage of the GPD G1 docking station from one of several preset options. This is a completely **optional** step and can be skipped – in this case, continue to ‘***Installing vBIOS Cont.***‘

If you are looking to modify the wattage, right-click the `Auto Updater.bat` file and choose ‘Edit’ (refer to *Images 1 & 2* below). This will open up the `.bat` file in Notepad. Navigate to the line: `amdvbflash.exe -fp -p 0 .\BRT124608_100W.001.sbin`, which is highlighted in blue (see *Image 4* below). Change this line to one of the three options listed below:

|  |  |
| --- | --- |
| **Wattage** | **Code** |
| 80W | `amdvbflash.exe -fp -p 0 .\BRT124609_80W.001.sbin` |
| 100W (Default) | `amdvbflash.exe -fp -p 0 .\BRT124608_100W.001.sbin` |
| 120W | `amdvbflash.exe -fp -p 0 .\BRT124604_120W.001.sbin` |

Please check that any changes are correct (refer to *Image 4* below.). Once you are happy, save the `.bat` file and continue.

1. Right-click `Auto Updater.bat`



2. Select edit




3. Find line



4. Change GPD G1 Wattage

## Installing vBIOS Cont.

Run the `Auto Updater.bat` (refer to *Image 1* below) to begin the vBIOS flashing. This will open the Command Prompt, and whilst the screen looks daunting, you don’t have to do much!

1. Run `Auto Updater.bat`

In the Command Prompt, you’ll be asked to accept the End-User License Agreement (EULA). Simply type ‘**y**‘ and press **Enter** to agree, as shown in green (see *Image 2* below). Following this, the G1 eGPU BIOS flashing process will automatically initiate if everything is correct. During this time, it’s crucial not to press any keys to avoid accidental disruptions. Once the flashing completes, the Command Prompt will display a message, also highlighted in green (refer to *Image 2* below), to confirm whether the flash was successful.

2. Successful BIOS flash

Upon completing the flashing process, a message may appear instructing you to ‘`Press any key to continue...`‘, which is highlighted in purple in the image above. It is strongly advised **not** to follow this prompt. As we experienced, pressing any key at this stage may inadvertently initiate a reflash of the vBIOS and present the same message afterwards. Creating a loop as it does not tell you how to proceed. To avoid this, simply close the command prompt once the flashing process is complete.

## Successful Flash

After a successful flash, Close the Command Prompt and restart your G1 eGPU by simply turning it off and on using the power button. The next step is to ensure that your connected device can recognize the GPD eGPU. You might receive a notification when the G1 docking station is connected or disconnected (see *Image 1* for reference). Alternatively, the G1 eGPU connection status can be verified in the Device Manager.

In the Device Manager, the G1 eGPU should appear as `AMD Radeon RX 7600M XT` listed under Display Adapters (refer to *Image 2* below). If the GPD G1 dock isn’t recognized, or if there’s a warning sign ⚠️ next to it, the AMD Graphics Drivers may need to be installed or updated. If you have already installed/updated them prior, we recommend you do it again after completing the BIOS flash.

1. Windows System Notification



2. Connected in Device Manager

## Installing AMD Drivers

We already have a guide covering how to correctly [install the latest AMD Graphics Drivers](https://droix.net/knowledge-base/article/how-to-uninstall-old-amd-graphics-drivers-and-install-new-ones/). We recommend you follow this guide when installing/updating the Graphics drivers for your G1 eGPU docking station.

> [How to uninstall old AMD graphics drivers and install new ones](https://droix.net/knowledge-base/article/update-amd-graphics-drivers/)

<https://droix.net/knowledge-base/article/update-amd-graphics-drivers/embed/#?secret=5EBt75fvPm#?secret=8JFqfPtejH>

After the installation of the latest AMD drivers is complete, a device restart is necessary to activate them. Post-reboot, it’s crucial to verify in the Device Manager whether the G1 docking station is successfully connected and functioning as intended – remember the GPD G1 eGPU should be recognised as the [AMD Radeon RX 7600M XT](https://www.amd.com/en/products/graphics/amd-radeon-rx-7600m-xt) (as shown below).

5. Connected in Device Manager



---

We hope by following the steps outlined in this guide, you have now successfully installed the latest BIOS for your G1 docking station and resolved any issues you may have been experiencing. These procedures are essential for maintaining the optimal performance and reliability of your G1 eGPU. We hope this guide has been helpful through the update process and troubleshooting potential issues. Should you encounter further challenges or have additional questions, refer to this guide or speak with our [Customer Support team](https://droix.net/contact-us/). Have fun gaming with your newly updated GPD G1 eGPU!