---
title: How to install MinUI custom firmware
source_url: "https://droix.net/knowledge-base/article/how-to-install-minui-custom-firmware/"
source_site: droix.net
type: kb-article
date: 2024-07-09
wp_id: 57944
---

If you have a device including the RGB30, M17 (early revs), Trimui Smart (and Pro), [Miyoo Mini Plus](https://droix.net/product/miyoo-mini-plus/), [Miyoo A30](https://droix.net/product/miyoo-a30/), and the [Anbernic](https://droix.net/product-attribute/brands/anbernic/) RG\*XX family of vintage gaming handhelds, and less clutter, fast menu navigation and a speedier experience, MinUI is a great alternative to [Spruce](https://droix.net/knowledge-base/article/how-to-install-spruce-custom-firmware-on-the-miyoo-a30/). It has a variety of improvements and features including optimised emulators, a cleaner frontend and minimal browsing experience with no game screenshot or boxart. Here is our guide on how to install MinUI for the Miyoo A30.

## You will need

|  |  |
| --- | --- |
| Latest MinUI Custom Firmware | <https://github.com/shauninman/MinUI/> |
| MiniTool Partition Wizard | <https://cdn2.minitool.com/?p=pw&e=pw-free> |

## Download and extract the MinUI archive

Download the latest version of the MinUI OS from [here](https://github.com/shauninman/MinUI/releases). You will want the **base** and **extras** files. Right click on each file and choose **Extract All** and extract to a new folder on your PC

Once extracted, you will have a list of folders and files similar to below:

MinUI for Miyoo A30 base and extra folders

Navigate to the **MinUI-xxx-extras** folder and press **CTRL+A** to select all the contents, then **CTRL+C** to copy them. Now navigate to the **MinUI-xxx-base** folder and press **CTRL+V** to paste the copied files. You may be prompted to overwrite files, if so, choose **Yes**.

Once completed, the **MinUI-xxx-base** folder should look similar to below.

MinUI for Miyoo A30 base folder structure

## Transfer old card files to new card

If you want to transfer your games files from the original micro SD card you can do so now. We are using the Miyoo A30 classic gaming handheld in this example, so the folders may be slightly different on yours.

Insert the original Micro SD card in to your PC and navigate to the correct drive for it. You will see a number of files and folders.

Miyoo A30 micro SD card structure

Right click on the **Roms** folder and copy this to the root folder of the **MinUI-xxx-base** folder you extracted on your PC. It will now copy your games to the PC. Depending on the number of games you have on the card this may take some time.

## Prepare the new Micro SD card

We recommend using [MiniTool Partition Wizard](https://cdn2.minitool.com/?p=pw&e=pw-free) to prepare your new micro SD card for the portable retro gaming console. Download and install the software.

### Format the micro SD card

Load the MiniTool Partition Wizard software. Insert the micro SD card into your PC. The card will now appear in MiniTool. **Double** and **triple** check that you are using the correct drive for your micro SD card for the following process!

Right click on the micro SD card drive and choose **Delete All Partition**s. Next, right click on the **Unallocated** space to the right and choose **Create**.

Format Options

A menu will show with some options, for the **File System** option, change this to **FAT32**, then click on **OK**. Double and triple check you have chosen the correct drive for your micro SD card. Now click on **Apply**, the software will delete the original partitions, and then format the card to **FAT32**. This may take a short while if the card is large.

## Copy MinUI to the micro SD card

You can now copy all of the contents to your new micro SD card in one go. Navigate to the ****MinUI-xxx-base**** folder that you extracted and copied your game to. Highlight all of the files and folders by pressing **CTRL+A** and then copy the files by pressing **CTRL+C**. Next navigate to your new micro SD card and press **CTRL+V**.

Everything will now be copied to your new micro SD card in one go. This may take some time if you have a large number of games. Do not remove the micro SD card or switch off the PC during this process.

## First boot of MinUI

Once all of the files have been copied to the micro SD card, you can safely eject it. Now insert it into the Miyoo A30 mobile gaming handheld and switch it on.

MinUI for Miyoo A30 Menus

The first boot will take longer than usual as it finishes setting up the software and scans for any games you copied over. Again this may take some time if you have a lot of games.

Once completed you will now be able to use the [Miyoo A30](https://droix.net/product/miyoo-a30/) retro gaming handheld with MinUI. Enjoy!

MinUI for Miyoo A30 Game