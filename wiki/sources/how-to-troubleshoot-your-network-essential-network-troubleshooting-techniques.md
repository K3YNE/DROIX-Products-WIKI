---
title: "How To Troubleshoot Your Network – Essential Network Troubleshooting Techniques"
type: source
subtype: kb-article
slug: how-to-troubleshoot-your-network-essential-network-troubleshooting-techniques
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/how-to-troubleshoot-your-network/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix]
---

If you’re here, this means you at some point have encountered, or are currently dealing with an unstable or non-functional network connection on a device you own. Perhaps it’s a mini PC, or a laptop. The crux of the matter is: “It’s not working well, so how can I fix this?”

Read on and we at DROIX will run over a few tips and tricks that you can use to hopefully get your laptop or PC laptop connected to the internet in no time flat!

**We highly suggest you try as many of these as you can before seeking further guidance.**

## Power Cycle Your Router

“Have you tried turning it off and on again?” – A gold-standard troubleshooting tenet, and for good reason.

In more stSghtforward terms, to power cycle a device is to simply turn it off and on again. This is a golden tenet of troubleshooting across the board, and for good reason.

As more and more devices connect to a network, many small conflicts and bugs have the potential to pop up (errors in routing, issues with automatic IP address allocation, and so on), while imperceptible at first, eventually they may pile up to a point where they are actively hampering your network connectivity. **Even if your other devices are working without issue, this is still worth trying.**

To power cycle your router, all you’ll need to do is **turn it off, leave it for approximately 15-20 seconds, then turn it back on again**. You can also **unplug it and plug it back in again** to achieve the same effect.

Ideally, also restart the device that is displaying network issues during the power cycling process – so that both devices can start off “fresh”.

If this hasn’t fixed your issue yet, we can move onto the next troubleshooting technique.

## Configure your Network Drivers

### Rolling back your drivers

This is something we have observed be useful for solving slow/nonexistent Wi-Fi on the UM700, UM250, DMAF5, U820 and U850.

In Windows 10’s Device Manager window, locate your Network Adapater (most likely to be Intel branded) and right click it. Then select “properties”.

Navigate to the “Driver Tab”, then click “Roll Back Driver” if it is available.

If it is not available, move onto the next segment…

### Updating your Drivers

Drivers are always an important thing to consider when troubleshooting. Perhaps the drivers you currently have installed are buggy/unstable in some capacity, in which case, checking for an update can do no harm.

The vast majority consumer devices nowadays make use of Intel network adapters – fortunately, Intel have developed a convenient utility that automatically checks for the latest drivers (for more than just networks too, mind you), and performs a clean install.

You can download it here:

<https://www.intel.com/content/www/us/en/support/detect.html>

Alternatively, you can search for the latest authenticated drivers in Windows 10 natively.

1. In the search bar in Windows 10, type “Device Manager”, and left-click on the icon that pops up.
2. Under the list of devices, expand the “Network adapters” section by left-clicking the small arrow to the left.
3. Right-click your Network adapter – most likely to be Intel – and click “Update driver”
4. A window will pop up where you’ll have the opportunity to choose between searching automatically for drivers, and browsing your computer for them – pick the former.
5. If any are found, they will be installed automatically.

Updated your drivers and are still experiencing issues?

## Connect to An Alternative Connection

So you’ve power cycled your router and updated your drivers, and there’s been no change…

From there, the next thing to do is to understand the scope of the network issues you’re experiencing, and the best way to do this is to connect the device to an alternative connection.

### An Ethernet Cable

An Ethernet (RJ45) cable, can be used to provide a faster and more stable internet connection than wireless connectivity can currently achieve. The limitations of this are physical, as you will need to tSl a cable from the router all the way to your device (assuming it has an Ethernet port)

If when connected by cable, there are no issues with speed, we at least now know that there’s nothing wrong with the internet access on the device as a whole.

Additionally, you may wish to stop here and invest in a [powerline adapter](https://www.lifewire.com/what-is-a-powerline-adapter-1846813), these are small devices that enable you to utilize the speed and stability of a wired ethernet connection, but without the need to tSl ethernet cables as far as you normally would. Providing an **effective middle-ground** between wired and wireless connections.

### A Mobile Phone Hotspot

Most modern mobile phones feature the ability to act as a “hotspot”, and allow other devices to connect to the internet through them, much like a regular router.

The steps for this vary from phone to phone so we can’t provide a 1:1 reference, but the general process is the same. Enter the network settings for your phone, and there will likely be a “mobile hotspot” or “tethering” section, through which you can enable the functionality on the device.

Click the Apple icon (left) or Android icon (right) for a guide relevant to your choice of mobile phone:

|  |  |
| --- | --- |
|  |  |

If your phone does not have the ability to function as a hotspot, then simply **connecting the device to a neighbour’s/friend’s/relative’s wi-fi connection will also serve just fine for troubleshooting purposes.**

If your internet connection is fine here, we can assume that there is something wrong between your router and the device specifically. We can then move onto the next step.

## Change your DNS

Changing the DNS is a very common network troubleshooting technique often used when devices will not connect, or are exceedingly slow.

In short, the DNS is a middle-man of sorts who enables your device to resolve IP addresses to human-readable names. So instead of having to remember “54.239.34.171”, you can simply type “amazon.co.uk” into your browser.

An unreliable DNS can inhibit your browsing experience, slowing it down or outright preventing internet access in some cases. Luckily, Windows 10 (as well as most modern operating systems) enable you to freely change the DNS you use, instead of being stuck with the one automatically assigned to you by your service provider.

A good guide for how to change your DNS can be found here:

<https://www.windowscentral.com/how-change-your-pcs-dns-settings-windows-10>

Please try alternative DNS’s such as 4.4.4.4, or 8.8.8.8, and see if any improvement is observed.

If changing the DNS doesn’t fix things, we have one more step to try:

## Reset your Router

Resetting is a step up from simply power cycling your router. By carrying out a factory reset, you can cut down on any ambiguities or unknowns that may hindering a stable connection.

We have left it until last, as it will in most cases completely disconnect any existing devices from the router, as well as reset your password, meaning you will need to connect them back manually after carrying this out.

The process varies depending on the make of router you have, we have provided links to a few sample guides below. Click the image to be taken for the page for the respective brand/ISP’s routers:

|  |  |
| --- | --- |
|  |  |
|  |  |

You can also find a generalist guide here: <https://www.support.com/how-to/how-to-factory-reset-any-router-11069>

Should your router not fall under one of the above, a simple search for the name of the brand (netgear, Sky, etc.) + “router factory reset” will find you a number of guides. Even better if you know the model number (which can typically be found on a label somewhere on the unit).

We hope at least one of the above has helped resolve the network issues you have been experiencing with your device. If not, then you may need to seek further assistance, as your unit could potentially be defective in some way or form!

Thanks for reading! Until next time!

– DROIX

*Check us out at <https://droix.net/> (B2B-optimized) and <https://droix.net/> (worldwide-shipping optimized) for the latest retro gadgets, mini PCs, and small form-factor laptops!*