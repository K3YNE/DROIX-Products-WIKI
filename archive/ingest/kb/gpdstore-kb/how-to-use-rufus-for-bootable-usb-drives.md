---
title: How to use Rufus for bootable USB drives
source_url: "https://gpdstore.net/kb/software-guides/kb-article/how-to-use-rufus-for-bootable-usb-drives/"
source_site: gpdstore.net
type: kb-article
date: 2025-10-14
wp_id: 1250592
---

To reinstall Windows on your [GPD mini laptop](https://gpdstore.net/product-category/gpd-mini-laptop/ "GPD mini laptop") or [handheld gaming PC](https://gpdstore.net/product-category/gpd-handheld-gaming-pcs/ "handheld gaming PC"), you will likely have an .ISO image that must first be copied to a USB drive. You will then need to boot your GPD device from this drive to begin the installation. This tutorial will explain the procedure for creating bootable USB drives with the Rufus utility.

To start, you will need to download and set up the most recent version of Rufus from its official [homepage](https://rufus.ie/ "homepage"). You should also have the Windows .ISO file saved to your PC and possess a USB drive with enough storage for the installation; 16GB is generally sufficient, but a 32GB or larger drive is a safer option.

Launch Rufus, and a user interface resembling the one in the image below will be displayed.

Rufus bootable USB software

Initially, you must click on the **Device** dropdown menu and choose your USB drive from the available options. This is the drive the .ISO file will be written to. It is critically important to double-check and even triple-check that you have selected the correct drive, as choosing the wrong one could erase your main Windows installation on the computer you are currently using.

Choose your drive

After that, press the **SELECT** button, browse to the location of your .ISO image, and select it.

Choose your ISO file

You can then click the **START** button to commence the .ISO image writing operation.

Click START to begin writing the ISO

A final pop-up will appear, warning you to confirm that you have selected the correct destination drive for the .ISO file. Choose **OK** to continue or **Cancel** to return to the setup screen.

Rufus Warning before proceeding

The writing procedure will then start. The duration of this process will depend on the size of your .ISO file and the speed of your USB drive, potentially taking several minutes or more. Wait for it to complete, at which point the green progress bar will indicate it is **READY**.

USB writing started



Copying the ISO to the USB



ISO copy completed

Once it has finished, you can safely eject the USB drive and proceed with the Windows installation on your GPD device.