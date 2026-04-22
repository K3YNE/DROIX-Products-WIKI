---
title: "MOQI i7S Stock Firmware – How to Flash your MOQI i7S"
type: source
subtype: kb-article
slug: moqi-i7s-stock-firmware-how-to-flash-your-moqi-i7s
brand: generic
product: null
source_url: "https://droix.net/knowledge-base/article/moqi-i7s-stock-firmware/"
published: 2022-01-21
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article]
---

Hi there! If you’re the owner of the popular (but sadly discontinued) MOQI i7s, you may be looking for where to get its stock firmware. Download the MOQI i7s firmware and learn how to install it with our handy guide!

## Why would I need MOQI i7s firmware?

Whatever the device, having access to the stock firmware is a useful thing to have in your toolkit. Be it for troubleshooting, preparing to give away to a friend/relative, or simply just starting fresh and “ungumming the works” (or so to speak.

For that reason, we’re compiling a short-ish guide that will show you how to easily and quickly re-flash the firmware for your unit.

## You Will Need:

* [QPST Tool (Qualcomm Product Support Tool)](https://go.droix.co.uk/MOQI-i7S-QPST)
  + A suite of software tools for servicing Qualcomm devices, like the MOQI i7s
* Qualcomm USB drivers
  + Included in the QPST Tool download.
* [MOQI i7s Firmware](https://go.droix.co.uk/MOQI-i7S-FW)
  + Contains all the necessary files to be used in QPST. **Do not use other firmware.**
* A USB Type-C Cable
  + From our experiments, you **need** to use a Type-C-to-Type-C cable.
* A laptop or PC with a USB Type-C port
  + An adapter for a Type-A port may potentially work, depending on your hardware. We can’t guarantee this however.
* File Archival Software
  + We recommend [7zip](https://www.7-zip.org/), as it is open-source, lightweight and free.

Download all of the above (where applicable), and we can proceed with the flashing process.

## Install the Qualcomm Software

You’ll need to install the Qualcomm USB drivers and firmware before proceeding . Fortunately, this is extremely straightforward.

First, extract the QPST tool. In it will be a folder and a few files.

Run the **QPST.2.7.496.1.exe** file. This is a regular installation process, so just follow the prompts and you’ll be good to go.

Once this is set up, you’ll need to install the Qualcomm USB drivers. In the **Driver** subfolder. Run the **Qualcomm USB Driver V1.0.exe** file. Then select **WWAN-HCP is not used to get IPAddress** option.

Select Next, and then just continue through the installation as normal.

Ensure you have downloaded and extracted the MOQI i7s firmware file from the previous section (**MUCH-i7s-9.6.35.zip**), and you can continue with the installation process.

## MOQI i7s Firmware Installation Process

With the QPST now installed, you’ll need to open a program called **QFIL** (Qualcomm Flash Image Loader).

By default, this will be located in the following directory:

```
C:\Program Files (x86)\Qualcomm\QPST\bin\QFIL.exe
```

Run this executable file, and the QFIL program will open. On the first run, it will look something like this.

Under **Select Build Type**, change the selected option to **Flat Build**.

You will then need to point various fields to the correct files.

Click **Browse…** and navigate to the MOQI i7s firmware folder (by default, called **MUCH-i7s-9.6.35**). Select the **prog\_firehose\_ddr.elf** file.

At this stage, the **Download** button will still be greyed out. Select **Load XML…** and then chose **rawprogram0\_NOFLASH\_FSG.xml** and **patch0.xml** from the MOQI i7s firmware folder.

---

## Connecting the MOQI i7s

Next, we’ll need to connect the MOQI i7S **in download mode** to our PC.

To put the MOQI i7s in download mode, first ensure that it is **turned off** (but also has enough charge to power on).

Then, hold both the **volume up** and **volume down** buttons, and press the **power button** for about ~5 seconds.

You will know you are successfully in download mode when the device does not respond to power button presses.

(To **exit** download mode, hold the power button down for a long time. *About* ~15 seconds).

Now connect the device to your PC or laptop via the USB cable.

The USB Type-C port on the MOQI i7S



---

After connecting the device, go back to the QFIL and chose **Select port…**, and you should see a new device in the list called **Qualcomm HS-USB-QDLoader XXXX** (where XXXX will be a random number). Select it.

**Finally**, click **Configuration** at the top of the application and open FireHose configuration.

Enable **Reset After Download**, and click OK.

The QFIL FireHose Configuration

Now you’re ready to reflash! Double check to ensure that your QFIL window looks identical to this (or at least almost – as the directory you have saved the files in may be named differently). Then click **Download**.

The process will take a minute or two to complete. Once finished, your MOQI i7s will automatically restart (exiting download mode in the process).

Enjoy!

While the MOQI i7S may be discontinued, you may be interested in more recent Android gaming handhelds such as the [GPD XP](https://droix.net/product/gpd-xp/) and the [ANBERNIC RG552](https://droix.net/product/rg552/)!

## My PC does not detect the MOQI i7s!

* You may need to disable enforced driver signatures before installing drivers. [A guide for doing so can be found here](https://windowsreport.com/driver-signature-enforcement-windows-10/#:~:text=Press%20and%20hold%20the%20Shift,select%20Disable%20driver%20signature%20enforcement.).
* Try using a device with a dedicated USB Type-C port. During our testing, the MOQI i7S would not be detected via a Type-A to Type-C cable.

---