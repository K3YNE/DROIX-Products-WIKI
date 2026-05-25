---
title: "Restoring The Format Option In LibreELEC On Your DROIX T8-S Plus v2 Android Powered Box"
type: source
subtype: kb-article
slug: restoring-the-format-option-in-libreelec-on-your-droix-t8-s-plus-v2-android-powe
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/restoring-the-format-option-in-libreelec-on-your-droidbox-t8-s-plus-v2-android-powered-box/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix]
---

If you have a hard drive installed inside your T8-S Plus v2 device, you may find the option to to format the disk, in LibreELEC, is missing.  
This guide will restore the option, it should take less than 10 minutes to complete. If you prefer, you can wait for this patch to be included in the next OTA firmware update.

If you need access to the ability to format your drive with an EXT4 partition, first please download **LibreELEC-DroidBOX.aarch64-T8Mini-7.0.3.001.tar** from https://mega.nz/file/aHBERTza#H5eQg1MY5vfYuPelnlKsN07AdF0yS9Rmn8p17xR82js

You should not open or extract the TAR file that this downloads, just move it to your DROIX storage area within LibreELEC.

There are a number of ways to achieve this:

#### Over your home’s network, via SMB filesharing

1. Boot your T8-S Plus v2 device into the LibreELEC operating system. Click on the SYSTEM INFO entry under the SYSTEM menu in Kodi’s homescreen.  
   ![Kodi LibreELEC System System Info Entry](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/1KodiLibreELECSystemSystemInfoEntry-300x169.png)
2. Take a note of the IP address it displays.  
   ![Kodi LibreELEC System System Info Results](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/2KodiLibreELECSystemSystemInfoResults-300x169.png)
3. On your PC, hold down the Windows flag on your keyboard and then tap the R key. You can now release both.
4. Type in two back slashes (so NOT the one under the ? symbol on most keyboards), then the IP address you took a note of before and click the OK button.  
   If this doesn’t work, you can also try two backslashes and then typing in LibreELEC and clicking OK.  
   ![LibreELEC Device's IP Address Entered Into Windows' Run Box](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/3IPAddress.png)
5. Open the Update folder shown.  
   ![Windows Explorer Navigating](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/4WindowsExplorerNavigating-300x132.png)
6. Now find your PC’s download folder and copy the TAR file  
   ![Copy Downloaded File](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/5CopyDownloadedFile-300x166.png)
7. before pasting it into the Update folder you have just browser to.  
   ![Copying File Across](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/6CopyingFileAcross-300x137.png)
8. Restart the T8-S Plus v2 device, and allow the file to be processed.

#### SSH

1. Take the IP address you entered previously (or use LibreELEC) and enter it as the server in your SSH client, the username is  root  and the password is  libreelec  
   ![Connection Details](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/1ConnectionDetails-300x196.png)
2. The first time you connect, your SSH client may well ask if you want to accept the device’s key  
   ![Key To Accept](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/2KeyToAccept-300x250.png)
3. You can then initiate a transfer from your PC to the T8-S Plus v2 as normal  
   ![Connected](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/3Connected-300x221.png)![Transferring](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/4Transferring-300x221.png)

#### 

#### Within Kodi itself, whilst in LibreELEC on your DROIX T8-S Plus v2

This approach is a little more involved, as you will need to first add the (hidden) Update directory as a source.

1. Click the File Manager entry under the System menu, whilst your device is booted in LibreELEC with the TAR file on a storage device (USB thumb drive, memory card, external hard drive etc) attached to the DROIX device.
2. Double click the Add source entry on either side  
   ![Kodi File Manager](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/1-Kodi-File-Manager-300x169.png)
3. Now carefully type exactly this into the top box: /storage/.update  
   ![Add Source](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/2-Add-Source-300x169.png)
4. Now label this source (or accept the default suggested) and click OK  
   ![](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/3-Label-Source-300x169.png)
5. You can now open the Update folder (the path has a full stop before the name as the folder is hidden) one side of the screen.  
   On the other side of the screen, navigate to the storage device where you have the TAR file.
6. Long click the remote’s OK button on the TAR file (you can also press the Menu button or use the C key if you have a QWERTY keyboard).
7. Decide where you want to move (cut and paste) or copy (copy and paste) the file and then confirm this action when asked.  
   ![Navigate And Copy](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/4-Navigate-And-Copy-300x169.png)![Confirm Action](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/5-Confirm-Action-300x169.png)![Copying In Progress](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/6-Copying-In-Progress-300x169.png)![File Copied Successfully](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/7-File-Copied-Successfully-300x169.png)
8. Once the file has finished copying across, you can reboot your device for this update to be processed.

Whichever method you use, once the update has been processed and LibreELEC loads up, head to the Program menu and click on it.

Now open Program Addons and select the LibreELEC Configuration entry.

You should now see the option to format your internal hard drive (DON’T FORGET TO REMOVE OTHER STORAGE DEVICES FIRST!) when you scroll down the list first shown.

![Format Option Returned To LibreELEC](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/7FormatOptionReturnedToLibreELEC-1-300x169.png)
