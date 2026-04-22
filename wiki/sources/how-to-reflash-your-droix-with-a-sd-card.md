---
title: "How to reflash your DroiX with a SD Card"
type: source
subtype: kb-article
slug: how-to-reflash-your-droix-with-a-sd-card
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/how-to-reflash-your-droidbox-with-a-sd-card/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix, firmware]
---

This guide demonstrates how to reflash a firmware to your DROIX.

**Before proceeding, please ensure you have the correct firmware for your device. Using the wrong firmware can prevent your DROIX from working. You can find the firmware on the DROIX forums or in the email that we send to you.**

Once you have downloaded the zip file, do NOT extract it, it must be kept as a zip file.

Copy the zip file to a SD Card.

Turn your DROIX off and insert the SD memory card into the slot on your device.

Locate the Reset/Restore hole on your device. Depending on the model it may be on the side, back or in the A/V hole. Insert a cocktail stick, pin, paper clip or similar, gently into the hole and press and hold the reset button.

Turn the DROIX on, and keep the recessed switch held down for a good 15/20 seconds. If Android’s Recovery Menu appears before then, you can release the switch.

Once you see the Android Recovery Menu on screen, you can release the Restore button. If the menu highlight is constantly scrolling down, remove any USB dongles and use the original IR remote you got with the device. You can ignore the *Cannot load volume /misc!* message, this is perfectly fine.

Click on the option **Apply update from EXT**, the name may be slightly different on your device.

This time, click the option **Update from sdcard,** the name may be slightly different on your device.

Finally, click on the firmware zip file (in the example below it is *firmware.zip*) that you downloaded and copied to the SD Card.

The firmware flashing process will now start. It may take several minutes to complete, so do not switch off your device or press any buttons.

When the process is completed, you will be returned to the main Recovery Menu. Choose the **Wipe Data/Factory Reset** menu option and confirm **Yes** to any prompts. Repeat the process for **Wipe Cache Partition**. Again, the names may be slightly different on your device.

Once completed, you can remove the SD card from your DROIX. Next, select the **Reboot system now** option, the name may be slightly different on your device.

The first time you boot will take longer than usual while it completes setting up for the first time. Once you can see the Android launcher homescreen, please leave the device alone for 20 minutes. Do not reboot, switch to LibreELEC or power off during this time. Applications continue to install in the background and if interrupted may not resume the next time you boot up.
