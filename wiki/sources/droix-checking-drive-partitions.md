---
title: "Checking Drive Partitions on an Android Kodi TV Box"
type: source
subtype: kb-article
slug: droix-checking-drive-partitions
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/checking-your-drives-partitions-on-an-android-powered-kodi-tv-box/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix]
---

This article is for owners of a DROIX T8-S, T8-S Plus (v1 and v2) who have installed a hard drive.  
Although you can remove the hard drive from your DROIX internal bay and attach it to a PC to check the partition(s), you can also leave it in place and use an Android application instead.

#### Warning: Do not click on options related to formatting, mounting, clearing or erasing unless you have a good reason to do so. You can lose access to your data if you click the wrong options.

If you want to know more about the drive inside your T8-S, T8-S Plus v1 or [DROIX® T8-S Plus v2](https://droidbox.co.uk/droidbox-t8s-plus-dualboot-android-libreelec-4k-amlogic-s812.html?utm_campaign=DroidBOX+Website&utm_source=Top+Banner+Desktop&utm_medium=Android+Partition+Check) device, then AParted <https://play.google.com/store/apps/details?id=com.sylkat.AParted> is worth installing. With it you can check how many partitions are on your hard drive, and what type they are.

1. Open the Play Store app on your DROIX device. If you’ve not signed in and used it before, you might want to click over to <https://droix.net/first-run-of-googles-play-store> first.  
   ![Play Store Opened](https://droix.net/wp-content/uploads/2020/10/1PlayStoreOpened-1-300x169.png)
2. In the search bar at the top, enter these words:  
   AParted  
   ![Play Store Enter Search](https://droix.net/wp-content/uploads/2020/10/20170320_165317_0-1-300x169.png)
3. We want the app by sylkat. Don’t worry about the reference to SD cards, it also works on hard drives.  
   ![Select And Click Install](https://droix.net/wp-content/uploads/2020/10/20170320_165335_0-1-300x169.png)
4. Once clicked on, select the Install button  
   ![Play Store AParted Page](https://droix.net/wp-content/uploads/2020/10/20170320_165345_0-1-300x169.png)
5. Make sure you are happy accepting the permissions it requests (Android 5 users, Android 6 users will be asked when the app is opened)  
   ![Play Store AParted Accept Permissions](https://droix.net/wp-content/uploads/2020/10/20170320_165351_0-1-300x169.png)
6. Following the application’s installation, click the Open button  
   ![Play Store AParted Installed](https://droix.net/wp-content/uploads/2020/10/20170320_165412_0-1-300x169.png)

#### What Now?

You will now need to open the application

1. ![AParted Requesting Permission](https://droix.net/wp-content/uploads/2020/10/20170320_165424_0-1-300x169.png)  
   Carefully watch the screen for the window shown above, be sure to click the Grant button in time.
2. ![AParted Permission Granted Confirmation](https://droix.net/wp-content/uploads/2020/10/20170320_165426_0-1-300x169.png)If done correctly, the app will open with a confirmation shown as a toast notification towards the bottom of the screen.
3. ![AParted Permission Explanation](https://droix.net/wp-content/uploads/2020/10/20170320_165440_0-1-300x169.png)You will see the application author’s explanation for one of the permissions his work requires.
4. ![AParted Manual Link](https://droix.net/wp-content/uploads/2020/10/20170320_165448_0-1-300x169.png)  
   Offer to read the AParted manual, worth browsing first.
5. ![AParted Settings Screen](https://droix.net/wp-content/uploads/2020/10/20170320_165515_0-300x169.png)  
   Click the Settings tab and you will see this screen
6. ![AParted Settings Detected Devices](https://droix.net/wp-content/uploads/2020/10/20170320_165525_0-300x169.png)  
   Click the entry under “Detected Devices” and select the USBDisk entry.
7. ![AParted Settings Detected Devices Select USBDisk](https://droix.net/wp-content/uploads/2020/10/20170320_165530_0-300x169.png)  
   If everything has gone OK so far, the USBDisk will now show as the selected device.
8. ![AParted Settings Devices Change Confirmed](https://droix.net/wp-content/uploads/2020/10/20170320_165538_0-300x169.png)  
   Scroll down and click the Save button.
9. ![AParted Settings Devices Changed Click Save](https://droix.net/wp-content/uploads/2020/10/20170320_165546_0-300x169.png)  
   Now confirm you are certain you want to save this change of configuration.
10. ![AParted Click The Tools Tab](https://droix.net/wp-content/uploads/2020/10/20170320_165558_0-300x169.png)  
    Now click the Tools entry at the top
11. ![AParted Tools Area](https://droix.net/wp-content/uploads/2020/10/20170320_165617_0-300x169.png)  
    You can now see the number, size and type of partition(s) to be found on the hard drive. Remember not to change anything on the Create tab.

#### Alternative application

Another possibility is to use Parted4Android (SD Partition), see <https://play.google.com/store/apps/details?id=com.giis.parted4Android> for details. The interface is a little more modern looking and easier to use, however there was less information (specifically identifying as EXT rather than EXT4) when compared to the AParted.
