---
title: How To Download And Prepare Firmware Files
source_url: "https://droix.net/knowledge-base/article/how-to-download-and-prepare-firmware-files/"
source_site: droix.net
type: kb-article
date: 2022-07-01
wp_id: 1921
---

### In this article

1. [Download Types](https://droix.zendesk.com/hc/en-gb/articles/360016773898-How-To-Download-And-Prepare-Firmware-Files#Download_Types)
   1. [Type A – The Compressed File](https://droix.zendesk.com/hc/en-gb/articles/360016773898-How-To-Download-And-Prepare-Firmware-Files#Type_A_-_The_Compressed_File)
   2. [Type B – The Split File](https://droix.zendesk.com/hc/en-gb/articles/360016773898-How-To-Download-And-Prepare-Firmware-Files#Type_B_-_The_Split_File)
   3. [Type C – The Raw File(s)](https://droix.zendesk.com/hc/en-gb/articles/360016773898-How-To-Download-And-Prepare-Firmware-Files#Type_C_-_The_Raw_File(s))
2. [Preparation Steps](https://droix.zendesk.com/hc/en-gb/articles/360016773898-How-To-Download-And-Prepare-Firmware-Files#Preparation_Steps)
   1. [Formatting](https://droix.zendesk.com/hc/en-gb/articles/360016773898-How-To-Download-And-Prepare-Firmware-Files#Formatting)
   2. [Type A – Imaging](https://droix.zendesk.com/hc/en-gb/articles/360016773898-How-To-Download-And-Prepare-Firmware-Files#Type_A_-_Imaging)
   3. [Type B – Manually prepared bootable USB.](https://droix.zendesk.com/hc/en-gb/articles/360016773898-How-To-Download-And-Prepare-Firmware-Files#Type_B_-_Manually_prepared_bootable_USB.)

Hi there!

We at DroiX sell a variety of devices wherein it is possible to reinstall firmware, either stock or custom. So we figured it’d be handy to create a small guide that covers the variety of steps you might need to perform in most cases.

# Download Types

## Type A – The Compressed File

You’ll most commonly encounter this when looking for the firmware for GPD devices, or mini PC’s.

A compressed file is a regular file, or collection of files, that have been shrunk in size through the use of a particular compression algorithm.

A compressed file may have a file extension like .7z, .zip, .rar, or more.

To access them in most cases, you’ll need to download file compression software. Such as [7zip](https://www.7-zip.org/) or [WinZip](https://www.winzip.com/win/en/). We personally suggest 7zip, as it’s lightweight and simple to use.

Once downloaded, right click and “extract” the file (you may want to examine the contents first to check the folder structure – some people place files in a folder before compressing them, while others may just compress the files directly

## Type B – The Split File

Split files are most commonly found for extra large downloads. By splitting a file into multiple pieces, it makes it easier to download and transfer the file.

Picture a 100GB file. Pretty hefty, right? Now imagine if your internet cut out when you had 75GB of it downloaded. You would have to download the **whole** thing again.

Now picture a 100GB file split into ten separate 10GB files. Even if your internet does cut out partway through, you only have to redownload the single part that it cut out for.

To reconstruct the original file, place all the parts in the same folder, then extract only the FIRST one (001).

The reconstruction will then take place automatically.

## Type C – The Raw File(s)

This one is self-explanatory! For smaller firmware files (usually anything under 10GB or so), the file will not be compressed.

Just download the file and move onto the next step!

# Preparation Steps

## Formatting

We’d advise formatting your media first before loading firmware onto it to minimize the chance of errors occurring.

To format it, insert the media into your system, then right click it in File Explorer. Select “Format” from the context menu.

Formatting

Make sure the card is formatted as whatever is required – this will typically be NTFS or FAT32, then click format.

Now your media clean and ready to be used.

Note that in the case of the following segment (Type A), the partition format is not important, as it will be overwritten anyway.

## Type A – Imaging

It is possible to quickly duplicate a storage device’s contents through the method of “disc imaging”. With the image file (.img) you have downloaded, download imaging software. We highly suggest Win32DiskImager, as it is lightweight, straightforward and easy to use.

*Note that as of writing, Win32 Disk Imager does not play nice with services that persistently scan for drives, such as Google Backup, or Linux File Systems for Windows by Paragon Software. If Disk Imager will not start, exit these programs/disable these services, then try it again.*

WIN32 Disk Imager

This is what the interface should look like.

The main aspects you should be concerned with are:

**Device**: The partition that you are going to write to/read from. **Note that Win32DiskImager will overwrite/copy the ENTIRE device that the partition is on. Not just the selected partition.**

**Image File:** This is where you select the image file you’ve downloaded/extracted. If you type in a filename that does not exist, a file will be created automatically you “read” the device.

**Write:** Start copying the image file’s contents to the device.

**Read:** Copy the device to an image file. If no image file exists, will create one with the chosen name. Use this to make backups.

## Type B – Manually prepared bootable USB.

This is similar to the imaging process and in some aspects is actually more straightforward, as it should not require you to download additional software.

If you download a compressed file containing the firmware for a GPD Win 2, Beelink MINI PC, or similar device – you may find it contains multiple folders and files, with names like “script” or “boot”.

What you will need to do here is first – format the device you intend to use; in 99% of cases this should be a singular NTFS partition. **Make sure that the partition is called “WINPE” when doing so**.

Once that’s done, just copy over all the files onto the root of the partition. It will probably look very similar to this.

Copy over the files

Your USB drive is then good to go! Plug it in, enter the BIOS or boot menu (the shortcut keys are most often ESC, F1, F2, F7 and F12 – it varies depending on device) and select it from the list of bootable devices, and the installation will generally proceed automatically.