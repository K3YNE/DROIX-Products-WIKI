---
title: How To Reinstall Windows On The MinisForum UM250 / DMAF5 / UM700
source_url: "https://droix.net/knowledge-base/article/how-to-reinstall-windows-on-the-minisforum-um250-dmaf5-um700/"
source_site: droix.net
type: kb-article
date: 2022-03-17
wp_id: 1594
---

Welcome to our brief guide on how to reinstall Windows 10 on the MinisForum UM250, MinisForum DMAF5, and MinisForum UM700.

Before proceeding, you will need the following tools:

* [The MinisForum UM250, DMAF5 and UM700 firmware.](https://go.droix.net/DMAF5-UM250-UM700-FW)
* A USB stick of at least 8GB in size.
* Imaging software. This guide uses [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/), but alternatives are acceptable too.

## Preparing the Installation Media

To reinstall windows on any device, you will need to prepare a piece of installation media. This will be a USB flash drive of at least 8GB in size.

You will need to format the USB drive. This can be done using your operating system’s [built-in formatting tool](https://www.windowscentral.com/how-format-usb-flash-drive-windows-10), or you can download a third-party partition management utility, such as [MiniTool’s Partition Wizard.](https://www.partitionwizard.com/)

When you format the drive, there are two things you must make sure of:

* That the partition is called WINPE
* That the partition is in the NTFS format

**If the drive does not conform to these two rules, it will not function as a bootable drive.**

## Working with compressed files (.zip, .rar, etc.)

One way that firmware files will be distributed is in the format of a compressed file. This will be one or more files ending with an extension such as .zip, .rar or even .7z.

To access the contents of these compressed files, you will need to extract them. You can either use your operating system’s  or you can use a third-party tool such as [7zip](https://www.7-zip.org/download.html) (recommended!) or [WinRAR](https://www.win-rar.com/start.html?&L=0).

In Windows 10, to open .zip files, you can right click the file and select “extract” from the context menu. For other file types, such as .rar and .7z, you will need third party software (once again, we suggest 7zip!).

### There are multiple compressed files? How do I extract multiple zip/rar/etc. files?

Occasionally, large downloads may be split into multiple parts. The main benefit of this is that it makes large files easier to download, because rather than download a huge chunk, you can download it in multiple “easier to digest” packages (so if you lose connection during the download, you don’t lose as much progress).

This does come with it’s own issues however, such as more potential locations for a download/upload to become corrupt.

Multi-part compressed files will often have suffixes like .001, .002, and so on. This indicates what part of the zip it is.

To “combine” the multiple parts, **all you need to do is place all the parts into the same folder on your PC, and then extract the first one as you would any normal file**.

### Working with the contents

Inside the compressed file, assuming it is not an .img (in which case, skip to the Working with Images part of this guide), you will multiple files and folders, like so.

Copy all these files and folders onto the ROOT of your prepared USB drive. By “root”, we mean place the files directly. Do **not** put them all in one folder, and then place that folder onto the USB drive.

Rename the USB drive to “WINPE”, and now you’re ready to go!

## Working with Image files (.img)

Sometimes firmware may be distributed as an .img file. An .img file is basically a snapshot of an already prepared USB which you will need to use a tool such as [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/), or [ApplePi Baker](https://www.tweaking4all.com/software/macosx-software/applepi-baker-v2/) (for Macintosh users).

Some of the image files you’ll find in the guide are prepared by us at DroiX. Essentially, all we’ve done is follow the compressed-file part of this guide, and have turned it into an .img for you to use!

Either way, let’s continue…

### Using Win32 Disk Imager

Win32 Disk Imager is a lightweight, powerful, and easy-to-use tool for both reading and writing image files.

Make sure your USB drive is inserted, and you have the image file downloaded.

Under “Device”, select the drive letter that corresponds to the USB drive. If there is only one Hard Drive/Solid State Drive in your computer, the USB will probably automatically be assigned the drive letter D:\ , but make sure to check!

Under “Image File”, navigate to the image you downloaded previously. It doesn’t really matter where its saved, as long as you can find it (and it won’t be moved during this process)

Then, click “Write”, and the process will begin. This will probably take around 30 to 60 minutes depending on the speed of your computer and the connected USB ports (you can use the PC for other things in the meantime, just make sure not to disconnect the USB drive, add/remove any files to the USB drive or close the application!).

When the bar is filled and you get the popup informing you that the imaging is complete, it’s safe to remove the USB drive.

## Booting into the USB

Now your USB has been successfully prepared, it’s time to actually use it to carry out the reinstall.

To do this, insert the USB into your PC or laptop. Then, while the USB or laptop is booting, press a certain key combination:

* To enter the BIOS on most devices, you will need to press one of the following: ESC, F1, F2, F12
  + If you enter the BIOS, you will need to press left/right on your attached keyboard until you are under the “Save & Exit” menu.
* To enter the boot menu, on most devices you will need to press F7.

Now you will see a list of bootable devices. Select the one that conforms to your USB memory stick – for example, a Kingston USB stick might who up in the boot list as a “Kingston DataTraveller”. Select it.

The installation itself will now proceed automatically. Note however that there are some devices whose reinstalls require user input (a simple yes/no to confirm if you wish to proceed), so keep an eye out (so you’re not waiting around for longer than necessary!).