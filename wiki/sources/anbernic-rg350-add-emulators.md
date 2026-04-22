---
title: "How to Add Emulators to the RG350/RG350M"
type: source
subtype: kb-article
slug: anbernic-rg350-add-emulators
brand: anbernic
product: null
source_url: "https://droix.net/knowledge-base/article/how-to-add-emulators-to-the-rg350-rg350m/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, anbernic]
---

One of the best things about the RG350M (and its predecessor, the RG350) is that there’s a host of community-developed emulators and applications available for you to mix and match at your leisure, allowing you to create a truly personalised retro gaming handheld.

For the purposes of this guide, we’ll be showing you how to install mame4all, which is an alternative MAME emulator that’s slightly easier to get up-and-running than its xmame counterpart. But you can use this for any emulator.

You can download the opk file for mame4all [here](https://rs97.bitgala.xyz/RG350M/Add%20on%20pack/emulators/mame4all.opk). There’s also a larger variety of emulators for the RG350M in general available [here](https://rs97.bitgala.xyz/RG350M/Add%20on%20pack/emulators/).

This guide is also applicable to the RG350. In this case, you’ll need to download your emulators from [here](https://rs97.bitgala.xyz/RG-350/localpack/).

## Connecting the RG350M

Firstly, make sure your RG350M is connected to your PC in via the USB/DC port.

Then, open the Network app.

Select “allow login without password”.

## Transferring Files Over

We’re using [WinSCP](https://winscp.net/eng/index.php) here, but you can use an alternative application (such as [FileZilla](https://filezilla-project.org/)) if you’d like, as all that is required is the ability to copy files over from your PC to the RG350M).

In WinSCP, create a “New Site” with the parameters that show up for you in the network app on the RG350M (in this case, the host name is the IP address – for us, 10.1.1.2 – and the username is root).

You’ll then be connected to the device.

In the left pane, navigate to the folder where you’ve downloaded the mame4all.opk file.

In the right pane, go to the root of the device (keep clicking the folder with two dots until you can’t go any further). Then follow the path: **media -> data -> apps**.

Now you’re set, just copy over the mame4all.opk file to the apps folder on the right side.

Once done, you can safely disconnect your device.

If done correctly, mame4all should appear in the list of emulators, like so.

## A Quicker Way?

A faster way to load apps and emulators on the device is to do so via the external SD card port.

Using any kind of microSD card reader, simply drag and drop the mame4all OPK into the “APPS” folder on the external SD card. The emulator/app will then be visible when the card is inserted into the device.

We don’t recommend this, as it could potentially cause issues regarding file paths depending on the emulator. It’s easier in the long-run to just add it to the internal card.
