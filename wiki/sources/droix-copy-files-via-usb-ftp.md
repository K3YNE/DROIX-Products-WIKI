---
title: "Copying Files via USB Cable from PC"
type: source
subtype: kb-article
slug: droix-copy-files-via-usb-ftp
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/copying-files-via-usb-cable-from-pc/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix]
---

Copying files to your Micro SD card is fastest and easiest done with a Card reader. But if you do not have one, you can copy files from your PC to the device via the USB cable and FTP software.

**IMPORTANT NOTE:** This will give you access to the firmware storage area in which you should not alter files. You should only change files on the SD card and nowhere else. Changing files elsewhere can corrupt the firmware and you may need to reinstall it. You do this at your own responsibility.

#### **You will need**

* The Type-A to Type-C USB cable that comes with the device. You may be able to use other Type-A to Type-C USB cables, Type-C to Type-C will not work.
* FTP Software: We recommend FileZilla at **<https://filezilla-project.org/>** which has versions for Windows, Mac OSX and Linux.

#### **Setting up the device**

Connect the Type-A to Type-C USB cable to your PC and the correct port on your device. In this example on the RG350M it is the 2nd USB port located on the right side of the device.

Switch on the device and navigate to the Settings menu and choose **Network**.

The app will load and present some information including the **IP address** and **login user name**. In the below photo you can see it is **10.1.1.2** and **root** respectively, these may be different for your device.

You can leave the password disabled. You do not need to set or change the password as the device does not connect over the internet, but you can change it if you wish to.

#### **Transferring Files**

Open the **FileZilla** software on your PC. Enter the details from your device into the respective boxes and click on **Quickconnect**.

Host: is the IP address, in this example it is **10.1.1.2**Username: is the Login, in this example it is **root**If you chose to set a password you can enter it in the Password field.

A notification may appear which is safe to ignore, click on **OK** to continue.

You should now be connected to your device. The two panels in the central area are your **PC (local site)** on the left and the **device (remote site)** on the right. They will show the storage contents of each on the panel.

Change to the location of the files on your PC first, by navigating to the correct folder. You can now navigate to the SD Card on the device. The location will be **/media/sdcard/**, click on the respective folders to navigate to this location.

You will now see your Micro SD Card contents. Depending which files you are copying over, you can choose the correct folder here. If for example you are copying game ROMs to the card, then you would choose **ROMS** folder and then the folder for the system for example **MD** for Mega Drive / Genesis games.

On the left panel (PC) you can highlight a file by clicking on it once, or multiple files by selecting them all and **Right Click** to bring up the menu. Choose **Upload** from the options. The transfer process will now begin. Depending on the number and size of the files this process may take some time. If a file already exists on the device you may be prompted to Overwrite or Skip.

You can check the status of the transfers on the bottom panel under **Queued Files**, **Failed Transfers** and **Successful Transfers**.

Once the files have completed uploading you can press the **Disconnect** icon.

You can now disconnect the USB cable from the device and exit the Network app. The files are now on the device and ready to access.
