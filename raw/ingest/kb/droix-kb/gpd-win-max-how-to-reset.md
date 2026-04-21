---
title: GPD Win Max – How To Reset
source_url: "https://droix.net/knowledge-base/article/gpd-win-max-how-to-reset/"
source_site: droix.net
type: kb-article
date: 2021-11-20
wp_id: 991
---

Hi there! If you’re here or have been directed here, it’s likely you’re experiencing issues with your GPD Win Max, and are looking to either factory reset your GPD Win Max, or reinstall Windows 10 on your GPD Win Max as part of a troubleshooting process.

Sometimes things just start to bug out. Maybe a botched Windows update, or an incompatible program has started a chain reaction of inconsistencies, dependency failures, and so on and so forth. So completely resetting the system in some form is perhaps the best way to troubleshoot the issue.

## How To Reset The Win Max

A factory reset is faster than a reinstallation of Windows. However, to do this you’ll need to have GPD’s version of the Windows installation present on your device. If you’ve installed an alternative operating system, or have installed a generic version of Windows 10, this method will not be possible

With that in mind, to initiate the reset, simply press F7 when the device is powering on. You’ll be taken to the boot menu, like so:

Select “UEFI OS (Biwin SSD)”.

Press the big blue start button – and the device will proceed to reset and reboot automatically.

(We highly suggest making sure the device is connected to the charge while the reset is underway, as if the device shuts off during this process it may cause issues)

## How To Reinstall Windows 10

To reinstall Windows 10 on your GPD Win Max, you’ll need to prepare a bootable installation USB. This can be done in one of two ways.

### Preparing the USB

#### Method 1: Copy/Paste the necessary files

Download the latest firmware file from GPD’s website: https://www.gpd.hk/gpdwinmaxfirmware

Once you’ve downloaded the zip file, extract it using a tool of your choice. WinZip and 7zip are two good examples. If your OS supports it, you can also just use the native compression utility (i.e., right click and “Extract All…” in Windows 10)

Next you’ll need to:

* Format the USB as an NTFS drive
* Make sure the partition is called “WINPE”.

This can be done natively in Windows 10, but also through a myriad of other free tools like [MiniTool Partition Wizard](https://www.partitionwizard.com/).

Once the drive is formatted, copy the contents of the extracted zip file onto the root of the USB. It should look something like this:

Now your USB is ready for use!

#### Method 2: Write a pre-made image

This method is slightly more stSghtforward for those who are unsure what files go where, or how to format their drive.

Download this image file we at DroiX have prepared – it’s been creased using the firmware that was available around the time of the Win Max’s commercial release (late September/early October), dated 18/06/2020.

[[Click here to download!]](https://go.droix.net/WIN-MAX-FW) (If that link doesn’t work, copy-paste this: https://go.droix.net/WIN-MAX-FW)

You’ll also need to download Win32DiskImager, which you can here: https://sourceforge.net/projects/win32diskimager/.

Once downloaded, insert the USB you plan to use into your PC, and start up Win32DiskImager. You’ll see a window like this.

Click the blue folder icon, then navigate to where you’ve downloaded the image file, and select it.

Then – make sure the “Device” drive letter matches the USB you’ve inserted (you can check this in File Explorer).

Now click “Write”, and the USB memory still will start being prepared with the chosen image. You can do other things with the PC in the meanwhile, but just make sure to not close the app or the computer, as you’ll need to start the writing process over again.

Once finished, you’ll have a new USB called “WINPE” with all the requisite files, and can get started with the reinstallation.

### Installing Windows 10 on the GPD Win Max

Insert the USB stick into either of the USB-A ports on the rear of the Win Max, as seen here.

Now turn on the device while pressing F7. As seen in the previous section, this will bring up the boot menu.

Select the device that corresponds to the USB you’ve inserted (i.e., in this guide we’ve used a Toshiba memory stick, so we’ll select the Toshiba TransMemory option).

Now the reinstallation will begin. Just sit back, make sure that the system is connected to a charger, and wait!

Once finished, the system will reboot automatically into a fresh new installation of Windows 10.

Thanks for sticking with the guide this long! If you’ve just chanced across this guide and don’t have a Win Max of your own just yet – you can order one from us at DroiX here! https://droix.net/collections/windows-gaming-handhelds/products/gpd-win-max

Until next time!