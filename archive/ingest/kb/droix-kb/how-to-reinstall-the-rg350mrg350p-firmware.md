---
title: How to reinstall the RG350M/RG350P firmware
source_url: "https://droix.net/knowledge-base/article/how-to-reinstall-the-rg350m-rg350p-firmware/"
source_site: droix.net
type: kb-article
date: 2022-07-01
wp_id: 1905
---

### In this article

1. [You will need:](https://droix.zendesk.com/hc/en-gb/articles/360010449277-How-to-reinstall-the-RG350M-RG350P-firmware#h.4egzrwk0ahuy)
2. [Removing the Micro SD Card](https://droix.zendesk.com/hc/en-gb/articles/360010449277-How-to-reinstall-the-RG350M-RG350P-firmware#h.ubzo8t34k54c)
3. [Formatting](https://droix.zendesk.com/hc/en-gb/articles/360010449277-How-to-reinstall-the-RG350M-RG350P-firmware#Formatting)
4. [Writing the firmware to the microSD card](https://droix.zendesk.com/hc/en-gb/articles/360010449277-How-to-reinstall-the-RG350M-RG350P-firmware#Writing_the_firmware_to_the_microSD_card)

If your RG350M is not booting or you are upgrading to a larger Micro SD Card you will need to reinstall the firmware. You can follow this guide for how to reinstall the original firmware.

**IMPORTANT:** Do NOT install RG350 firmware on a RG350M, it may not work. While it will not damage the device, you will need to reinstall the correct firmware below.

This guide is also applicable to the RG350P, as the design of the devices is the same. However, you will need different firmware (see below)

### **You will need:**

Original RG350M firmware: You can download it from[here](https://go.droix.net/RG350M-FW). Once downloaded, extract the .img file with software such as**[7zip](https://www.7-zip.org/)**, WinRAR, Zip etc.

OR

Original RG350P firmware: [Here](https://go.droix.net/RG350P-FW).

Disk image writing software: You can use any software such as Win32 DiskImager or Etcher for example.

<https://sourceforge.net/projects/win32diskimager/> – Win32 Disk Imager

<https://mac.softpedia.com/get/Utilities/ApplePi-Baker.shtml> – ApplePi Baker (for Mac – this guide doesn’t reference it, but the overall process is the same)

### **Removing the Micro SD Card**

There may be a security sticker covering the Micro SD Card slot. You can use your fingernail or similar to break the seal either side of the Micro SD Card as shown in the below photo.

Break the seal and remove sd card

Gently press the Micro SD card and it should click and pop up. You can now remove the card.

### **Formatting**

We’d advise formatting your media first before loading firmware onto it to minimize the chance of errors occurring.

To format it, insert the media into your system, then right click it in File Explorer. Select “Format” from the context menu.

Formatting

Make sure the card is formatted as anything that’s readable – this will typically be NTFS or FAT32, then click format.

Format removable disk

Now your media clean and ready to be used.

### **Writing the firmware to the microSD card**

It is possible to quickly duplicate a storage device’s contents through the method of “disc imaging”. With the image file (.img) you have downloaded, download imaging software. We highly suggest Win32DiskImager, as it is lightweight, straightforward and easy to use.

*Note that as of writing, Win32 Disk Imager does not play nice with services that persistently scan for drives, such as Google Backup, or Linux File Systems for Windows by Paragon Software. If Disk Imager will not start, exit these programs/disable these services, then try it again.*

WIN32 disk imager

This is what the interface should look like.

The main aspects you should be concerned with are:

**Device**: The partition that you are going to write to/read from. **Note that Win32DiskImager will overwrite/copy the ENTIRE device that the partition is on. Not just the selected partition.**

**Image File:** This is where you select the image file you’ve downloaded/extracted. If you type in a filename that does not exist, a file will be created automatically you “read” the device.

**Write:** Start copying the image file’s contents to the device.

**Read:** Copy the device to an image file. If no image file exists, will create one with the chosen name. Use this to make backups.

So to summarize: Select the SD card as the “device”, select the image file downloaded prior, then click “Write”.

Do not remove the SD card or close the application during this process, otherwise you will need to restart the process.

Once finished, you can insert it back into the TF1/Internal card slot