---
title: "How to Factory Reset Your Windows Device"
type: source
subtype: kb-article
slug: how-to-factory-reset-your-windows-device
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/factory-reset-windows/"
published: 2022-03-31
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix, windows, reset]
---

In this article, we’ll be covering everything about factory resetting your [Windows](https://www.microsoft.com/en-gb/windows/windows-11) devices from [Mini PCs](https://droix.net/product-category/mini-pcs/) and [Handheld Gaming Devices](https://droix.net/product-category/handhelds/handheld-gaming-pcs/). We’ll explain what a factory reset is, when it’s necessary, and guide you through the preparation and execution process.

## What is a Factory Reset?

There may come a point in the process of using your device where you simply want to… start over! A **factory reset**, also known as a **hard reset**, **master reset**, or **formatting**, involves erasing all the data on your device and restoring it to its original settings using specialized software. While this process deletes all user data and application data, the operating system and pre-installed applications are reverted to their initial state, as they were on a new device.

## Why Would I Want to Reset My Device?

So if hard resetting your device deletes everything… why would you ever use it? This process can be beneficial, especially for resolving performance-related issues. Maybe your device consistently freezes, crashes, or performs slowly. Or maybe you’ve accidentally botched an update of some kind. A master reset can potentially address all of this by removing any problematic settings, corrupt files, or malware that may be causing the issue.

Additionally, factory resetting should be a necessity when preparing your device for sale, disposal, transfer of ownership, or return. It guarantees that all personal information is wiped clean, saving time compared to manually deleting each item.

***Note: If you intend to reset your device, please follow this guide carefully. Incorrect and improper use may render your device inoperable. DROIX assumes no responsibility for any damages incurred.***

## UEFI OS vs Native Windows

When it comes to [Windows](https://www.microsoft.com/en-gb/windows/windows-11) devices, there are typically two methods of performing a factory reset.

* Resetting the device via the native Windows utility (“Reset this PC”)
* Resetting the device via a manufacturer-developed “recovery partition”

In this article, we’ll go over how you access both, as well as the positives and negatives of either method

### via Native Windows Utility

Natively resetting the device through Windows is something just about EVERY Windows device, and is a built-in feature of the operating system.

To access this utility, simply search “Reset this PC” in the Windows search bar.

Upon starting up the utility, you’ll be given the option to keep your personal files (i.e., photos, documents, etc.), or to remove everything.

While this handy utility is universal – it does take substantially longer than just reinstalling windows, or performing the process via the second method.

### via Recovery Partition

This second method of resetting is **not universal** and is instead dependent on the specific installation of Windows and the manufacturer of the device.

Pictured: The GPD reset utility on the original 2020 GPD WIN MAX

Some devices feature a second partition on the hard disk which contains a utility that can wipe the device’s main partition. These utilities are very basic and consist of a basic “reset” button on a blue background.

Depending on the device’s age, some devices that may include this are:

* [One-Netbook](http://go.droix.net/ONE-NETBOOK) products – including the [ONEXPLAYER 1S](https://droix.net/product/onexplayer-1s/)
* [GPD](https://droix.net/product-attribute/brands/gpd/) products — most commonly found in the original [GPD WIN MAX](https://droix.net/product/gpd-win-max/) and onwards

To access this, you’ll need to find a way to boot the device into the partition.

* You can either enter the BIOS or boot menu during start-up, and select the partition
* Or you can enter the Windows Advanced Startup Settings

#### Entering the BIOS/Boot Menu

The exact steps for this will vary depending on the device you’re using.

Most commonly, the way to do this is to press F7 while the device is powering up. You will know you’ve been successful when a blue window appears.

You can also enter the BIOS by pressing ESC, F1, F2 or whatever the specified key is for your device. From the BIOS, you’ll be able to navigate to the boot options via your keyboard and select the drive of your choice.

In most cases, the partition will be called “UEFI OS”, although it may be different depending on the device.

## Advanced Startup Menu

The quickest way to enter the advanced startup menu is by holding the LEFT SHIFT key, and then selecting the restart option from within the Windows start menu, like so:

You’ll see several options, but the one you should pick is “Use a device”.

Select UEFI OS from the list of options here (there may be a large number of different options, depending on how your hard drive is partitioned and/or what USB devices you have connected.

The system will now reboot into the recovery partition. From here, you can begin the reset process — which is entirely automatic, although you will either need to connect a charger or ensure that the battery is over a certain percentage before it will start.

After about 15-20 minutes, the reset should finish. The system will then reboot into a fresh install of Windows!
