---
title: "Manually Updating Firmware On A DROIX Q8-S"
type: source
subtype: kb-article
slug: manually-updating-firmware-on-a-droix-q8-s
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/manually-updating-firmware-on-a-droix-q8-s/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix]
---

A new Android 5 firmware for Q8-S Owners has been released today.

**p.s. You update this firmware on your own risk  
“This applies to DROIX Q8-S only purchased before June 2016”**

For those already comfortable with the Rockchip tool and USB connections, here is the firmware image.

<https://1drv.ms/u/s!AlRdlhGu3fjihxhxz0khaXWCL8Q4>

You will need the drivers and a program to flash your Q8-S from your Windows PC. They are available from  
<https://1drv.ms/u/s!AlRdlhGu3fjihlnllfEYxvFaIuTE> and <https://1drv.ms/u/s!AlRdlhGu3fjihlit4Zg8z6z3vL44>

Extract (using [7-zip](http://www.7-zip.org/download.html) (free), [WinZip](http://www.winzip.com/downwz.htm), [WinRAR](http://www.rarlab.com/download.htm) or even [Windows built-in utility](http://windows.microsoft.com/en-us/windows/compress-uncompress-files-zip-files#), ) the contents of RK Release\_DriverAssistant.zip, and store it somewhere you can easily remember. Run the “DriverInstall” program and follow the onscreen instructions.

Now extract RKBatchTool1\_7.zip to a folder, and again make sure you remember where it has been placed!

You will need a standard USB cable to connect your PC to your Q8-S

With the power cable removed from your Q8-S, please:  
Locate the reset switch found on the left side of your Q8-S and hold it down. **Please don’t release it until told to.**  
Connect your USB cable, one end into your PC as normal, the other into the USB OTG socket at the rear of your Q8-S. It is the socket nearest to the aerial. You can now reconnect the power cable. Now press the Power On button to switch it on.

Once your PC notices there is new hardware attached, **you can let go of the reset switch**.

Once the driver installation is complete, please open the RKBatchTool folder you previously extracted, and run RKBatchTool–1.7.exe . If the drivers have installed correctly, then under Connected Devices, “1” should be green.

If that doesn’t happen, and you’re using a USB hub to connect the Q8-S, try a direct connection to one of your computer’s USB sockets, and if you have a choice, select a USB2 (rather than USB3) socket.

Click the … button at the top right corner, and point it to the folder you downloaded the large firmware file to earlier. Select the IMG file and click the Restore button, and wait until the process completes.

Once the firmware flash has completed, you can disconnect it from your PC. The first time you turn the Q8-S on you will find it takes a bit longer than usual to boot up. If any set up screens are presented, complete them and select which launcher you want to use, if asked.

Once you reach the Android launcher homescreen, please wait 20 minutes for applications to complete installing.