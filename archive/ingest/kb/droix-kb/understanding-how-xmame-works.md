---
title: Understanding how XMame Works
source_url: "https://droix.net/knowledge-base/article/understanding-how-xmame-works/"
source_site: droix.net
type: kb-article
date: 2022-07-01
wp_id: 1925
---

### In this article

1. [What Is MAME?](https://droix.zendesk.com/hc/en-gb/articles/360011568538-Understanding-how-XMame-Works#What_Is_MAME?)
2. [How do I get XMame to work?](https://droix.zendesk.com/hc/en-gb/articles/360011568538-Understanding-how-XMame-Works#How_do_I_get_XMame_to_work?)

The RG350 models (as well as other retro gaming handhelds)come with a plethora of emulators already installed, and you can always add more down the line (see our [handy guide](https://droix.zendesk.com/hc/en-gb/articles/360011035237) for how!). But one of the most common questions we get is how to get XMame up-and-running.

# What Is MAME?

MAME is a free, open-source emulator intended to support and enable to playing of as many arcade games as possible, for the purpose of preservation (since as times goes on, the hardware that arcade machines work with will deteriorate, much like any physical media).

Being open-source, there have been many variants of MAME developed for a variety of devices. Two of which are available for the RG350 – **Mame4All**, and **XMame**.

The difference between the two mostly lies in certain features that are too numerous to really list here. But the main difference you might be concerned with is compatibility! Mame4All and XMame support different games, so if a game doesn’t work on the one you’ve chosen, you might want to try using the other instead.

# How do I get XMame to work?

For the purposes of this guide, we’ll assume you’re using some model of RG350 (be it the regular one, the RG350P or the RG350M).

Out of the two available, XMame is slightly less intuitive of the two. When you first start it, you’ll likely be met with a blank list with only the game “Hook” in it, or perhaps “Ninja Baseball Batman”, or even some version of Street Fighter.

What you’ll see is dependent on the version you have selected. The port of XMame to the RG350 contains three versions of XMame, version 0.69, version 0.84, and version 0.52. Each version is slightly different regarding performance and which kinds of games it can run. Press the Right shoulder button to switch between versions.

Most of the games in XMame use the [0.37b5 romset,](https://www.google.co.uk/search?q=mame+37b5+romset) so XMame will be expecting the filenames to conform to it. In short, a romset is a collection of ROMs (games) that have been compiled and tweaked to run with a specific version of MAME. Some versions of MAME may run better with certain romsets, some with different emulators – emulation is very nebulous in nature.

If you press the left shoulder button, you’ll switch between various views for the list of games. You can choose between:

* Available Games (ROMs that Xmame has successfully located)
* Avaliable – Clones (Clones are alternative versions of an existing ROM – generally you don’t need to worry about this, but using clones may be worth trying if a game isn’t running too well)
* Your list of favourites (you can select favourites by pressing “Y”)
* All Games (search this list to see what there is to play!)

A slightly annoying quirk of XMame is that it is hard-coded to look at the internal SD card for the games. You can find these folders in:

/usr/local/share/xmame/xmame52

/usr/local/share/xmame/xmame69

/usr/local/share/xmame/xmame82

Inside each of these directories is the “roms” subfolder where the games are chosen from. **Copy your games into these “roms” folders.**

You can realistically access these three folders and modify them in one of three ways:

* Remove the internal SD card and adjust the contents through a PC
* Connect the RG350 via USB cable to a PC and use the “Network” feature (see [this guide](https://droix.zendesk.com/hc/en-gb/articles/360011035237) for an outline of how to connect)
* Use the built-in DinguxCmdr application (which is essentially a simple file browser that allows you to move, delete, copy and add files/directories natively)

Now, once you’ve copied your games over, hours and hours of retro gaming fun awaits!

*This guide is still under development and may be adjusted in the future with more pictures, tricks and tips to help you further use and understand XMame!*

If you’re looking for a new Retro Gaming handheld, we sell a variety on our store here: <https://droix.net/collections/retro-gaming-handhelds>