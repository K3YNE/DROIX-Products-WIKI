---
title: "How to Install OnionOS for Retro Handhelds"
type: source
subtype: kb-article
slug: how-to-install-onionos-for-retro-handhelds
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/install-onionos/"
published: 2023-06-01
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix, installation, custom-firmware]
---

Installing a custom OS is one of the best things you can do for your retro device, especially the [Miyoo Mini Plus+](https://droix.net/product/miyoo-mini-plus/). For [Miyoo](https://droix.net/product-attribute/brands/miyoo/) retro handhelds, OnionOS is the cream of the crop of custom operating systems. Sporting additional features, a new UI and compatibility with tons of games and console emulators you’d be silly not to install it.

It can seem like a daunting thing, installing [OnionOS](https://onionui.github.io/) but I promise you it’s simpler than you think. In this guide, I’m going to take you step-by-step to get OnionOS installed and running so that you can play all your favourite retro games in the style they deserve.

## Preparing your MicroSD Card

Our journey into [OnionOS](https://onionui.github.io/) starts on your PC, to do so you need to remove the [MicroSD card](https://droix.net/product-attribute/storage-technology/micro-sd/) from the bottom of your device.

Once it’s removed you can plug it into your PC, this can be done in a few different ways. You can use an SD card converter, as we did in the photos, the included microSD to USB adapter that comes in the box or even just straight into the PC if your computer has a microSD card slot. Any method is perfect.

Once it’s in, make sure your computer can see it by going to This PC and confirming it’s there. Once you’re sure the computer can read it, we’re going to format the card. This will delete everything currently saved on it. Optionally I recommend you make a backup. This is done by creating a new folder on your PC and dragging the contents over.

Once you’re ready to format we need to install a piece of software called [Rufus](https://rufus.ie/en/) which will help us. You can download it from this link [here](https://rufus.ie/en/). Scroll down and download the latest version for your PC. If you’re not sure what version is best go with the Standard Windows x64 platform as that is the most common. Run the .exe file when it downloads.

When you open the program you’ll be greeted with the screen below. We’ll need to ensure the format is set up first. Ensure your device is the microSD card you’ve plugged in. Set boot selection to ‘Non bootable’. Set the partition scheme to ‘MBR’. The target system to ‘BIOS or UEFI’. Give the volume an appropriate label, such as ‘OnionOS-Installer’ and finally set the file system to ‘FAT32’. You’re ready to click ‘Start’. When you do so a warning will pop up letting you know the device will be erased. Click ‘OK’.

Once it’s completed the formatting you can double-check by going back to the PC and making sure the computer can see the volume.

Now that the MicroSD card is ready, we need to download OnionOS. You can do so from the GitHub page [here](https://github.com/OnionUI/Onion/wiki/Installation) and click on the zip file of the latest version that’s compatible with your device to download.

Once it’s downloaded, head to where the file is located. Right-click and click on ‘Extract All…’ This will open a new popup, click on ‘Extract’ to extract the files.

Your newly extracted files will now pop up. Copy **ALL** of these folders to the formatted microSD card.

Once that is done, safely eject the card. You can now place the microSD card back into the Miyoo Mini Plus+ and we can get started with the installation.

## Installing OnionOS

Press the power button on the top of the device to power it on.

You will be greeted with the OnionOS boot screen.

The device will automatically begin installing OnionOS and [RetroArch](https://www.retroarch.com/), let it complete this part of the installation unhindered.



Once that’s done you will be taken to a short menu that you can scroll through, this would be good to read over if you’re new to OnionOS.



Now you can decide what you want installed on your device. The first page is a list of emulators. You can go through and select what you want to install, I’d recommend selecting them all. Do this easily by pressing ‘X’.



You can go to the next page by pressing R2 on the back of the device.

The next page is a list of apps you can install on the device. Again I would recommend selecting them all by pressing ‘X’

Third, you have a list of more experimental emulators, these may require additional set-up. If you are new to OnionOS I recommend leaving these be, but if you’re up for the challenge feel free to install any or all of them.

Finally press R2 again to go to the summary page to confirm your choices, and then press Start to install.

The device will then start to install all of your selected choices.

Once it has completed the installation, you will be taken to the home page.

Congratulations you have installed OnionOS! Here you can find your favourite games, your entire game and app libraries as well as settings to tweak the device to your specifications.

When a new version is released and you want to upgrade OnionOS, check out our guide on how to do so [here](https://droix.net/knowledge-base/article/how-to-upgrade-onionos/)!

You can also install customs ROMs and BIOS’ by following our guide [here](https://droix.net/knowledge-base/article/installing-games-and-roms/).

Now go and play all your classic favourites!
