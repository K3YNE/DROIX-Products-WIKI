---
title: "RG351 FAQ"
type: source
subtype: kb-article
slug: rg351-faq
brand: anbernic
product: null
source_url: "https://droix.net/knowledge-base/article/rg351-faq/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, anbernic]
---

```
Note: This guide is still under construction
```

Hi there! You may be here because you’ve purchased an RG351 (from us, we hope 🙂 ) and want to get to grips with your new handheld device.

The RG351 is decidedly different from its predecessors due to the fact that it no longer runs the OpenDinguX operating system, but instead runs EmuELEC, a linux distribution based on CoreELEC.

(In other words, it’s a Linux distribution designed explicitly to emulate games)

We at DROIX decided to create a little guide in order to help you get accustomed to the new system. So read on!

## EmuELEC Breakdown

EmuELEC is composed of two core components:

### RetroArch

RetroArch forms the backbone of the system. It is a front-end for a collection of emulators that enables you to have “all-in-one” experience, seamlessly switching between various emulators, adjusting configurations, and in recent years, enabling online play for classic games that never used to have it.

While it has become far more user-friendly in recent years, it is still recommended you have at least knowledge of how emulation works before delving into it. Otherwise you may end up breaking something!

You can read more about it here: https://www.retroarch.com/

When delving into the nitty-gritty of emulation, playing with shaders, rendering options, and more, more time will likely be spent here.

### EmulationStation

EmulationStation is another front-end for emulators that provides a more visually customizable, streamlined, user-friendly experience. With the ability to easily change themes, scrape online databases for boxart of games, sort games into collections, and more.

With how the RG351 is set up, EmulationStation acts moreso as a front-end for RetroArch rather than the emulators themselves. Most of the emulators on the system are run through RetroArch.

For general everyday usage, most of your time will likely be spent in the EmulationStation GUI.

## Navigating the UI

The UI of the RG351 is decidedly more flashy than its predecessors. The default setup may appear something like this if it boots into EmulationStation:

[Image Coming Soon!]

Navigation is the same as always however. Use the **analogue stick** or **directional pad** to move around, and the **A button** or **B button** to select items and exit menus respectively.

You can also press the **START button** to open the EmulationStation menu. From here there are a number of options to select, such as.

* EMUELEC SETTINGS
  + Tweak how EmuELEC itself runs. You can do things such as enable Bluetooth, create backups of configs, and change which frontend runs on startup (if you like, you can set things so that RetroArch is what launches initially, rather than EmulationStation)
* UI SETTINGS
  + Change how the EmulationStation UI looks. You can change the themes, group games into custom collections, and more!
* NETWORK SETTINGS
  + Connect the RG351 wirelessly to your internet connection and enable online play with select emulators.

## How Do I Exit Games?

### RetroArch Cores

**Unless stated otherwise, this is the standard way to exit an emulator on the RG351.**

To exit most emulators in the RG351, you’ll need to press the **left analog stick** and the **right analog stick** simultaneously.

This will bring up the menu for RetroArch. To be specific, the “Quick Menu” for the game you’re currently playing. The quick menu contains various options immediately relevant to your current game.

Now press the **B button.**

You’ll be taken to the main menu for RetroArch. Press the **down** input on the **directional pad** or **analog stick** to scroll through the options until you find “Quit RetroArch”. Then press the **A button**.

You’ll finally be taken back to EmulationStation and can select your next game.

### Nintendo DS (DraStic)

To exit DraStic. Press the **left analog stick**. Then press **up** or **down** on the **directional pad** until the menu becomes visible.

A slightly inconvenient quirk of DraStic is that the cursor appears to have a mind of its own. Pressing up or down once or twice won’t exactly move the cursor as many places in the menu as you expect it to.

Nonetheless, wrestle with the cursor until it is over the “Exit DraStic” option, then press the **B** **button**. You will then be taken back to EmulationStation.

(As a side note, press the **A button** to exit DraStic menu and go back to the game you were playing).

### Arcade (MAME)

To exit arcade games in the MAME emulator, press the **right analog stick**, and you will immediately be taken back to EmulationStation.

You can also press the **left analog stick** to open the menu for MAME, should you wish to change various options.

### Playstation Portable (PPSSPP)

Press the **right analog stick** to enter the quick menu for PPSSPP.

Use the **directional pad** or **analog stick** to highlight the “Exit to menu” button, then press the **B button**.

Use the **directional pad** or **analog stick** to highlight the “Exit” button, then press the **B button**. You’ll then be taken back to EmulationStation.

## Network Play

One of the biggest features of the RG351 is the ability to play retro games online using your regular Wi Fi connection.

Something to note is that this online play is done through simulating same-system multiplayer. In essence, it is like someone is remotely plugging in a Player 2 controller into your emulated console.

So with that in mind, you can’t emulate the multiplayer, or the functions of, games that required hardware peripherals to connect, such as link cables.

Netplay is supported for most platforms on the system. With exceptions being made for PSX (PS1), N64 and Dreamcast titles

### Getting Connected

First of all, you’ll need to connect to your Wi-Fi connection, The RG351 can only recognize signals in the 2.4GHz band, bear in mind.

On the main screen of EmulationStation, press the **start button**. The main menu will appear.

Navigate to Network Settings, select it, then choose the “WIFI SSID” option. You’ll see a list of all visible nearby internet connections.

Once you’ve located and selected the one you wish to connect to, select the “WIFI KEY” option, then input the password for the Wi-Fi connection (if applicable).

Once finished, select the “BACK” button. The system will freeze for a minute, indicating it is currently attempting to connect.

If successful, when you open the Network Settings menu again, the “STATUS” should read “CONNECTED”, and you should also be able to see your device’s (local) IP address.

### Hosting

Enter the RetroPie Quick Menu (press the **left stick** and **right stick**) and press the **B button** to go up a level. Then press right on the **directional pad** or **analogue stick** until you see an icon that looks like a headset. This is the “**Netplay**” section.

Select the “**Host**” option. Then scroll down and tick the “**Publicly Announce Netplay**” option. Scroll back up and select the “**Start Netplay Host**” option.

If successful, you should see a message pop up indicating as such (alongside your public-facing IP address).

You are now hosting your room. Once someone joins, they’ll be able to manipulate whatever Player 2(or 3, or 4) can in the respective game.

If you get the error message “**Port Mapping Failed**” wait a brief moment, then try hosting again.

### Joining

Before joining a host, please be aware that the ROM file used needs to be EXACTLY the same between all connected users. If there is any difference whatsoever, an error message along the lines of “Cannot retrieve header” will appear.

As before, enter the RetroPie menu and navigate to the Netplay section.

Scroll to the bottom and select “Refresh Netplay Host List”. You should then see multiple rooms available. These are all other people using RetroArch on various devices (not just RG351’s!) that are hosting netplay sessions for various games.

Find the one that matches the host (you can see the filename for the game being played, as well as the core, build version of retroarch, and the country of the host). When you find a match, select them, and if all is well you’ll be connected.

Your game state will immediately advance so that it mirrors the host, so there is no need to worry about “being on the same screen”, or anything along those lines.

### Leaving

Open the RetroPie netplay menu once more. You should see a new option “Disconnect from Netplay Host”. Select this.

The netplay session will end, and you will no longer be synchronized with the host. Your game will continue to run independently however from the same state as when you left.

## What Are Cores?

One of the defining features of RetroArch and EmulationStation is the ability to switch between multiple different emulators (also known as “cores”) for the same system.

As an emulator itself is an interpretation of how a retro system runs, different people have come to different conclusions. Nobody quite has the right answer, but the results can vary a fair bit.

For example, the N64 has two cores:

* Mupen64Plus
  + From what we have observed, Mupen64Plus provides more accurate visuals at the cost of performance.
* ParaLLElN64
  + ParaLLEl64 suffers a large number of visual glitches. But the performance is noticably better than Mupen64 in most scenarios.

What you pick is up to you, ultimately.

### How To Change Default Cores/Emulators

Cores can be changed in one of two ways – we’ll cover the easiest way, through EmulationStation.

Press the **Start Button** anywhere within EmulationStation, then select “**Games Settings**“.

Navigate down to “**Per System Advanced Configuration**“, then select the emulator you wish to change the core for.

Under the emulator option, press left/right on your **directional pad** or **analog stick** to select the emulator you wish to use.

Once set, the next time you launch a game for that system, it will use the selected emulator.