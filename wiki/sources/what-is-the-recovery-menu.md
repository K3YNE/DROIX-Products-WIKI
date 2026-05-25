---
title: "What Is The Recovery Menu?"
type: source
subtype: kb-article
slug: what-is-the-recovery-menu
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/what-is-the-recovery-menu/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix]
---

You may have come across references to the (Android) Recovery Menu in some of our other How To articles.  
We explain what it is, and what the various entries found within do.

The screenshots shown below were taken from an Android 6 powered device. Earlier models will have very similar menus, though LibreELEC is only shown on recent dual boot devices.

How to access – <https://droix.net/accessing-your-droidboxs-recovery-menu>

When navigating the menus, you can use the Up, Down, Left, Right and OK buttons on your infrared remote control. If you use a controller with Air Mouse mode, first turn it upside down/disable the Air Mouse, as small movements will otherwise be interpreted as wanting to scroll up or down the list very quickly.

![Android 6 Recovery Menu Reboot System Now Highlighted](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170724_180314_0-300x169.png)  
-Reboot system now  
Selecting this will exit the Recovery menu and boot into the operating system you last used.

![Android 6 Recovery Menu Reboot To Bootloader Highlighted](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170724_180319_0-300x169.png)  
-Reboot to bootloader  
Ignore this one entirely.

![Android 6 Recovery Menu Apply Update From EXT Highlighted](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170724_180322_0-300x169.png)  
– Apply update from EXT  
If you want to flash a firmware from a ZIP file you have been provided, this is the entry to click. It leads to two further choices:

![Android 6 Recovery Menu Apply Update From EXT Selected, Update From sdcard Highlighted](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170724_180448_0-300x169.png)  
— Update from sdcard  
This is the preferred method, instructions will be included with your firmware link, but copying the ZIP file downloaded to an SD memory card works the best.

![Android 6 Recovery Menu Apply Update From EXT Selected, Update From udisk Highlighted](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170724_180451_0-300x169.png)  
— Update from udisk  
Some devices can also update their firmware via a ZIP file stored on a USB storage device. If this approach fails, use a memory card instead.

![Android 6 Recovery Menu Apply Update From Cache Highlighted](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170724_180325_0-300x169.png)  
– Apply update from cache  
Ignore this one entirely.

![Android 6 Recovery Menu Apply Update From ADB Highlighted](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170724_180328_0-300x169.png)  
– Apply update from ADB  
This option is used when you want to flash a file via an ADB connection between two devices. Safe to ignore entirely.

![Android 6 Recovery Menu Wipe Data / Factory Reset Highlighted](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170724_180331_0-300x169.png)  
– Wipe data/factory reset  
If you want to wipe all data from your device, leaving just the operating system and applications in place, this is the entry to use. Anything you have configured, downloaded or moved will be lost, so back up first. See the link regarding how to access the menu for more information.  
You will be asked to confirm you are certain that you want to wipe everything.

![Android 6 Recovery Menu Wipe Cache Partition Highlighted](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170724_180333_0-300x169.png)  
– Wipe cache partition  
If you need to wipe the device’s cache, this is the entry to use. Again, you’ll be asked if you are certain.

![Android 6 Recovery Menu Mount System Highlighted](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170724_180336_0-300x169.png)  
– Mount /system  
Ignore this one entirely.

![Android 6 Recovery Menu View Recovery Logs Highlighted](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170724_180340_0-300x169.png)  
![Android 6 Recovery Menu View Recovery Logs Selected, 1st Entry Highlighted](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170724_180725_0-300x169.png)  
– View recovery logs  
If something went wrong, you can find out more information here.

![Android 6 Recovery Menu Start Android Highlighted](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170724_180344_0-300x169.png)  
– Start Android  
Exit the Recovery menu and specifically start the Android operating system.

![Android 6 Recovery Menu Start LibreELEC Highlighted](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170724_180348_0-1-300x169.png)  
– Start LibreELEC  
Exit the Recovery menu and specifically start the second operating system (if present).

![Android 6 Recovery Menu Power Off Highlighted](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20170724_180352_0-1-300x169.png)  
– Power off  
Ignore this one entirely.

You will see an error message related to “/misc” – these appear on all devices and are safe to disregard entirely.
