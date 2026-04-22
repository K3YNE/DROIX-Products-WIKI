---
title: "How to install Spruce Custom Firmware on the Miyoo A30"
type: source
subtype: kb-article
slug: how-to-install-spruce-custom-firmware-on-the-miyoo-a30
brand: droix
product: miyoo-a30
source_url: "https://droix.net/knowledge-base/article/how-to-install-spruce-custom-firmware-on-the-miyoo-a30/"
published: 2024-07-09
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix, miyoo-a30, firmware, installation, custom-firmware]
---

If you have a [Miyoo A30](https://droix.net/product/miyoo-a30/) retro gaming handheld and want to get the best performance from it, we highly recommend the Spruce custom firmware. It has a variety of improvements and features including optimised emulators, a cleaner frontend and game browsing experience, optimal settings and much more. Here is our guide on how to install Spruce.

## You will need

|  |  |
| --- | --- |
| Latest Spruce Custom Firmware | <https://github.com/tenlevels/spruce> |
| MiniTool Partition Wizard | <https://cdn2.minitool.com/?p=pw&e=pw-free> |

## Download and extract the Spruce archive

Download the latest version of the spruce OS from [here](https://github.com/tenlevels/spruce/releases). Right click on the file and choose **Extract All** and extract to a new folder on your PC

Once extracted, you will have a list of folders and files similar to below

Spruce folder structure

## Transfer old card files to new card

If you want to transfer your games and save files from the original Miyoo A30 classic gaming handheld micro SD card you can do so now.

Insert the original Micro SD card in to your PC and navigate to the correct drive for it. You will see a number of files and folders.

Miyoo A30 micro SD card structure

Right click on the **Roms** folder and copy this to the root folder of the Spruce files you extracted on your PC. It will now copy your games to the PC. Depending on the number of games you have on the card this may take some time.

You can also copy your old save and save state files. Navigate to the **/RetroArch/.retroarch/** folder and copy the **saves** and **states** folders to the **Saves** folder on Spruce root.

## Prepare the new Micro SD card

We recommend using [MiniTool Partition Wizard](https://cdn2.minitool.com/?p=pw&e=pw-free) to prepare your new portable retro gaming console micro SD card. Download and install the software.

### Format the micro SD card

Load the MiniTool Partition Wizard software. Insert the micro SD card into your PC. The card will now appear in MiniTool. **Double** and **triple** check that you are using the correct drive for your micro SD card for the following process!

Right click on the micro SD card drive and choose **Delete All Partition**s. Next, right click on the **Unallocated** space to the right and choose **Create**.

Format Options

A menu will show with some options, for the **File System** option, change this to **FAT32**, then click on **OK**. Double and triple check you have chosen the correct drive for your micro SD card. Now click on **Apply**, the software will delete the original partitions, and then format the card to **FAT32**. This may take a short while if the card is large.

## Copy Spruce to the micro SD card

You can now copy all of the contents to your new micro SD card in one go. Navigate to the Spruce folder that you extracted and copied your games & saves to. Highlight all of the files and folders by pressing **CTRL+A** and then copy the files by pressing **CTRL+C**. Next navigate to your new micro SD card and press **CTRL+V**.

Everything will now be copied to your new micro SD card in one go. This may take some time if you have a large number of games. Do not remove the micro SD card or switch off the PC during this process.

## First boot of Spruce OS

Once all of the files have been copied to the micro SD card, you can safely eject it. Now insert it into the [Miyoo A30](https://droix.net/product/miyoo-a30/) mobile gaming handheld and switch it on.

Spruce CFW for Miyoo A30

The first boot will take longer than usual as it finishes setting up the software and scans for any games you copied over. Again this may take some time if you have a lot of games.

Once completed you will now be able to use the [Miyoo A30](https://droix.net/product/miyoo-a30/) vintage gaming handheld with Spruce OS. Enjoy!

Spruce CFW Emulators Menus
