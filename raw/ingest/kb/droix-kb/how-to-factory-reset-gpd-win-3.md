---
title: "How To: Factory Reset \u2013 GPD Win 3"
source_url: "https://droix.net/knowledge-base/article/how-to-factory-reset-gpd-win-3/"
source_site: droix.net
type: kb-article
date: 2021-11-20
wp_id: 1092
---

Hi there! With the [GPD Win 3](https://droix.net/product/gpd-win-3-1165g7/) on it’s way in the coming months, we at DroiX thought it might be helpful to create a quick guide going over how to factory reset your GPD Win 3.

Factory resetting is a way of returning the device to it’s default, “factory-fresh” state. Removing programs and restoring settings to the default configuration. This is a useful way of quickly troubleshooting a variety of problems, such as random crashes. If the issues persist after a factory reset, the issues you are experiencing may be emblematic of some greater problem with the device.

**DISCLAIMER: This will remove all data from the GPD Win 3. Back up any data or files that you do not wish to lose.**

## Ensure The GPD Windows Firmware Is Installed

In recent firmware releases, GPD have included a handy feature that is the lynchpin of this guide – the ability to factory reset your device without the need to install anything extra.

All that you must make sure of is that the Windows installation on your device is the release provided by GPD – and not a generic Windows 10 installation created using the Windows [Media Creation Tool](https://www.microsoft.com/en-gb/software-download/windows10). Otherwise you will not have access to the recovery partition.

## Access The UEFI OS Partition On the GPD Win 3

If you have ever seen our guide on [how to reset the GPD Win Max](https://droix.net/knowledge-base/gpd-win-max-how-to-reset/), the process is rather similar. Upon booting the device, press the F7 key repeatedly until you see a list of bootable devices – then select the UEFI OS from the list.

However, when taking pictures for this guide, we found that the GPD Win 3 boots *too fast* for us to catch the window for opening the boot menu.

Luckily, Windows 10 has a handy way of booting from alternative devices after it has already loaded.

On the desktop, open up the Windows Menu, then select the power button.

Now, **hold down the shift key** and select the “Reset” option. You’ll then be taken into the advanced startup settings menu.

From here, select “Use a device”. Then select UEFI OS (which should be the only option either way).

The system will then boot into the recovery partition. Press “Start” and the process will begin.

The process typically takes about 15 minutes. After which, your GPD Win 3 will automatically reboot into a fresh installation of Windows, with all prior data wiped.

We hope you’ve found this guide useful. If you have any suggestions or if something isn’t quite clear, please feel free to leave a comment, and we’ll get back to you as soon as we possibly can.

Additionally, if this has not fixed this issue, we suggest going one step further and trying a reinstall of windows entirely. You can follow our guide via the below link to do so:

Until next time!