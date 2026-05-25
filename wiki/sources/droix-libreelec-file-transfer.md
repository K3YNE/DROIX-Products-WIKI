---
title: "Copying Files To and From LibreELEC's Storage"
type: source
subtype: kb-article
slug: droix-libreelec-file-transfer
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/copying-files-to-and-from-libreelecs-storage/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix]
---

If you find you want to transfer files to your DROIX device, whilst it is using the LibreELEC operating system, this post explains how to do so  
  
Steps to take:

* Boot up your DROIX device, and ensure you are in the LibreELEC operating system, not Android  
  ![Kodi LibreELEC System System Info Results](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/2KodiLibreELECSystemSystemInfoResults-1-300x169.png)
* Download the file you need on your PC/laptop/other device  
  ![Example Download Link](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/DownloadLink-1.png)
* Open Windows Explorer/My Computer (Windows Flag and E combo on your keyboard)  
  ![Windows Explorer My Computer This PC](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/WindowsExplorerMyComputerThisPC-2-300x198.png)
* Navigate to your device’s Downloads folder and right click the file/directory you want to transfer, select COPY  
  ![Windows Explorer Right Click Copy](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/WindowsExplorerRightClickCopy-2-300x136.png)
* Type into the address bar: \\LIBREELEC and press Return (if you named your device differently then amend as required)  
  ![Windows Explorer Network Path In Address Bar](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/WindowsExplorerNetworkPathInAddressBar-2-300x198.png)
* If you see a web page pop up, ensure a) You are using \\ , not // and b) That you are in Windows Explorer, not a browser. Hold down the Windows Flag key on your keyboard and tap E  
  ![Not LibreELEC Shared Folders](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/NotLibreELECSharedFolders-2-300x149.png)
* Navigate to the \\LIBREELEC\Downloads path  
  ![Windows Explorer LE Downloads Folder](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/WindowsExplorerLEDownloadsFolder-1-300x198.png)
* Right click an empty area and select paste  
  ![Windows Explorer Right Click Paste](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/WindowsExplorerRightClickPaste-1-300x200.png)

When you need to access files transferred in this manner from within LibreELEC, they are to be found at the /storage/downloads path (click the Home folder first, or Root filesystem then Storage)  
![LibreELEC File Navigation](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170720_151932_0-2-300x169.png)

You can carry out the same task on a Mac (using their equivalent), Android tablets and phones (with a File Browser that can navigate other devices on your home’s local network) and any other hardware and OS combination that can access SMB shares.

The steps above should work for any LibreELEC installation, unless a service has been disabled. Please note only some DROIX devices come with LibreELEC, those currently on sale are the [DROIX T8-S Plus v2](https://droidbox.co.uk/droidbox-t8s-plus-dualboot-android-libreelec-4k-amlogic-s812.html) and the [iMXQpro v2](https://droidbox.co.uk/droidbox-imxqpro-mxq-pro-best-android-tv-box-kodi-box-libreelec-amlogic-s905.html). Previous models featuring LibreELEC or OpenELEC include the DROIX T8-S, T8-S Plus v1 and the DROIX T8 Mini.

If you have an older device using OpenELEC, the steps above will still work, however the address to enter would be \\OPENELEC instead of \\LIBREELEC.

Should using the network name not work, you can also replace it with the same two backslashes, then the IP address for your LibreELEC powered device. To find this, click the System Info entry found under the System menu (OpenELEC 6.x, LibreELEC 7.x), or System Information when you click the Settings/System cog at the top of the homescreen (LibreELEC 8.x).

If you prefer, you can also use SSH/SFTP

* Enter the DROIX device’s IP (internal/LAN) address as the server in your SSH client, the username is  root  and the password is  libreelec . To check your device’s IP address, boot into LibreELEC and click on the System Info entry under System menu (for LibreELEC 7 and earlier) or click the Settings cog at the top of the screen, then System Information.  
  ![Connection Details](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/1ConnectionDetails-1-300x196.png)
* The first time you connect, your SSH client may well ask if you want to accept the device’s key  
  ![Key To Accept](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/2KeyToAccept-1-300x250.png)
* You can then initiate a transfer from your PC to LibreELEC’s storage system as normal  
  ![Connected](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/3Connected-1-300x221.png)![Transferring](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/4Transferring-1-300x221.png)
