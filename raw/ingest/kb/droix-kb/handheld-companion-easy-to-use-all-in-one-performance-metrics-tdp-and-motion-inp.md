---
title: Handheld Companion – Easy to use all in one performance metrics, TDP and motion input control
source_url: "https://droix.net/knowledge-base/article/handheld-companion/"
source_site: droix.net
type: kb-article
date: 2023-06-28
wp_id: 3009
---

[Handheld Companion](https://github.com/Valkirie/HandheldCompanion) is an extremely useful application if you have a [Windows handheld gaming PC](https://droix.net/product-category/handhelds/handheld-gaming-pcs/). It provides easy access to functions and features that you may find by installing multiple applications and configuring them all separately. This is not a sponsored article or anything, just a very useful app we use every day on our handhelds!

## Handheld Companion Overview Video

## What does Handheld Companion work on?

Handheld Companion runs with a vast number of handheld gaming PCs. Not all features may be present on some models due to hardware differences such as a built-in gyroscope.

It runs on AYA NEO consoles – including the 2S, and the [AYA NEO Next](https://droix.net/product/ayaneo-next-pro/) series, Air and Geek series. It also supports the GPD WIN and the [GPD WIN Max](https://droix.net/product/gpd-win-max-2-2023/) series, Steam Deck, ASUS ROG Ally and Lenovo Legion.

Supported sensors are Bosch BMI160 (and similar) USB IMU (GY-USB002) for external motion devices.

## Main Software

We will take a few moments first to go over the main software where you can set a few things up.

### Controller

Handheld Companion Controller

Some handhelds identify as OEM controllers which can have compatibility issues with some games either not being recognised at all or incorrectly configured. From here you can change the identity of your handheld controller to for example a Xbox 360 or a PlayStation DualShock 4 controller.

### Profiles

Handheld Companion Profiles

The profiles tab lets you set up different profiles which is very handy to have. You can set up profiles per application, for example when a certain game is running it will switch to an Xbox 360 controller, set the [TDP](https://www.tomshardware.com/reviews/tdp-thermal-design-power-definition,5764.html) to automatically adjust and the frame rate to 60 FPS with some more power for the GPU. Every game can have different setups and it saves a lot of time constantly changing settings when using these profiles.

### Overlay

Handheld Companion Overlay

The overlay is an onscreen display of performance metrics showing varying levels of CPU, GPU, TDP and Battery information. This is useful for benchmarking, or simply setting up your game for the best graphics levels to run at 60 FPS for example. You can change the position of the data on the screen, the size and colours amongst others.

### Hotkeys

Handheld Companion Hotkeys

The Hotkeys settings allow you to configure a variety of different button combinations to perform various functions. The most basic is setting up a key to bring up the overlay, but you can also have a virtual trackpad like the Steam Deck and 3D controller overlay, as well as switching TDP for example. For handhelds like the AYA Neo 2S, this is great as four custom buttons can easily be used.

## In-game Overlay

### On-screen stats

While you are in a game or emulator, if you have enabled the performance metrics display you will see them on screen. Along the bottom of the overlay are four icons for the Settings, Power, Profile and Task Manager.

Handheld Companion Performance Metrics

### Quick Settings

The power icon gets you quick access to a bunch of commonly used functions such as the display level of the on-screen stats, changing the display resolution, fan settings and power mode.

Handheld Companion Overlay

### TDP Settings

The most useful is the profile icon where you can adjust various power-related settings. From here you can limit the frame rate and TDP limit or have it running automatically adjusting levels based on demand, and adjusting the CPU and GPU power balance.

The auto TDP is especially useful for saving battery life as we will show. For example, we are playing Forza Horizon 5 on the AYA NEO 2S and the frame rate is around 90+ FPS and the TDP around 28W. We don’t need to go above 60 FPS, the TDP is set too high and is wasting battery life

Handheld Companion Overlay

By enabling the automatic TDP and setting the frame rate to 60 FPS. The game will now target a 60 FPS rate and automatically adjust the power demand based on that. We can now see the TDP at around 11W compared to around 28W previously. It is not 100% perfect and you may see some dips below 60 FPS now and again but it’s often barely noticeable unless you have the FPS counter on screen.

Handheld Companion Auto TDP Enabled

The game does need to be configured to run above 60 FPS beforehand, it won’t magically make everything run at the best graphics at 60 FPS, that’s not possible. But by spending a little time setting up the graphics etc, you can get some great results and save some battery life.

## Motion Control

More games are taking advantage of motion control and not forgetting emulators as well. Most Windows handhelds have a built-in gyroscope which is often overlooked as it can be a bit of a pain to set up and get it working. The Handheld controller software makes this process extremely easy now.

Handheld Companion Motion Control Setup

We will use the [YuZu emulator](https://yuzu-emu.org/) as an example. To enable motion controls, simply start the service in the main Handheld Companion software. Then in the Yuzu emulator go to the Input setup and define all your controls. At the bottom is a Motion setting, select that and then shake your handheld. You will see the setting update to “cemuhookudp”.

Now load a motion control-compatible game and you will now be able to use your controller for motion input. If it’s not working, check the game settings in case you need to enable it.

Handheld Companion Motion Control on Yuzu

You may need to tweak the settings to get motion input to your preference but it works very well overall. There are guides on the Handheld Companion homepage for setting up different compatible emulators

## Final thoughts

So that’s our brief overview of Handheld Companion. For us, it is a great timesaver as it has everything we need in one easy-to-use install-and-use package. There’s minimal setting up and it gives us fast access to performance metrics, easy TDP changing, display settings and more that we don’t use but you might.

[DOWNLOAD HANDHELD COMPANION](https://github.com/Valkirie/HandheldCompanion)

You can learn more about and download Handheld Companion on the official [GitHub page here](https://github.com/Valkirie/HandheldCompanion). If you have a Windows handheld gaming PC then we highly recommend giving it an install and you probably won’t be able to live without it!