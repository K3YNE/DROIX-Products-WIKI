---
title: Copying Files To And From LibreELEC’s Storage
source_url: "https://droix.net/knowledge-base/article/copying-files-to-and-from-libreelecs-storage/"
source_site: droix.net
type: kb-article
date: 2021-11-20
wp_id: 131
---

If you find you want to transfer files to your DroiX device, whilst it is using the LibreELEC operating system, this post explains how to do so  
  
Steps to take:

* Boot up your DroiX device, and ensure you are in the LibreELEC operating system, not Android
* Download the file you need on your PC/laptop/other device
* Open Windows Explorer/My Computer (Windows Flag and E combo on your keyboard)
* Navigate to your device’s Downloads folder and right click the file/directory you want to transfer, select COPY
* Type into the address bar: \\LIBREELEC and press Return (if you named your device differently then amend as required)
* If you see a web page pop up, ensure a) You are using \\ , not // and b) That you are in Windows Explorer, not a browser. Hold down the Windows Flag key on your keyboard and tap E
* Navigate to the \\LIBREELEC\Downloads path
* Right click an empty area and select paste

When you need to access files transferred in this manner from within LibreELEC, they are to be found at the /storage/downloads path (click the Home folder first, or Root filesystem then Storage)

You can carry out the same task on a Mac (using their equivalent), Android tablets and phones (with a File Browser that can navigate other devices on your home’s local network) and any other hardware and OS combination that can access SMB shares.

The steps above should work for any LibreELEC installation, unless a service has been disabled. Please note only some DroiX devices come with LibreELEC, those currently on sale are the [DroiX T8-S Plus v2](https://droidbox.co.uk/droidbox-t8s-plus-dualboot-android-libreelec-4k-amlogic-s812.html) and the [iMXQpro v2](https://droidbox.co.uk/droidbox-imxqpro-mxq-pro-best-android-tv-box-kodi-box-libreelec-amlogic-s905.html). Previous models featuring LibreELEC or OpenELEC include the DroiX T8-S, T8-S Plus v1 and the DroiX T8 Mini.

If you have an older device using OpenELEC, the steps above will still work, however the address to enter would be \\OPENELEC instead of \\LIBREELEC.

Should using the network name not work, you can also replace it with the same two backslashes, then the IP address for your LibreELEC powered device. To find this, click the System Info entry found under the System menu (OpenELEC 6.x, LibreELEC 7.x), or System Information when you click the Settings/System cog at the top of the homescreen (LibreELEC 8.x).

If you prefer, you can also use SSH/SFTP

* Enter the DroiX device’s IP (internal/LAN) address as the server in your SSH client, the username is  root  and the password is  libreelec . To check your device’s IP address, boot into LibreELEC and click on the System Info entry under System menu (for LibreELEC 7 and earlier) or click the Settings cog at the top of the screen, then System Information.
* The first time you connect, your SSH client may well ask if you want to accept the device’s key
* You can then initiate a transfer from your PC to LibreELEC’s storage system as normal