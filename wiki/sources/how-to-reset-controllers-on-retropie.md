---
title: "How to reset controllers on RetroPie"
type: source
subtype: kb-article
slug: how-to-reset-controllers-on-retropie
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/how-to-reset-controllers-on-retropie/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix, reset, emulation]
---

If you find yourself in the situation where you are not able to use a controller on the menus then you can follow the steps below to reset it if you have a USB keyboard.

The following steps which will reset the controller input and when it next boots it will have the option to configure the controllers.

Plug a USB keyboard into one of the side USB ports.  
Plug the controller(s) into the front USB ports.

When it has booted up to the menu, Press **F4** on keyboard, this will go to command prompt  
Type in: **sudo ~/RetroPie-Setup/retropie\_setup.sh** and press Return on the keyboard

Choose **Manage Packages**

Choose **Manage Core Packages**

Choose **emulationstation (Installed)**

Choose **Configurations / Options** (it may also be named Configurations Tools)

Choose the option to **Clear/Reset Emulation Station input configuration**

Choose **Yes** to proceed to clear the controller settings.

A prompt will confirm the settings have been cleared. Choose **OK** and then keep choosing **Exit** to return to the Command Prompt screen.

Type: **reboot** and press Return on the keyboard.

This will reboot the system and go back into the menus where you will be able to reconfigure the controls when prompted.

Do this for the first controller and to skip buttons, hold any button for a couple of seconds. Then when you get to **HOTKEY**, press the **SELECT**button.

Then for the second controller, press **START**and you will see an option for configuring a controller. You can repeat the process again.

Your controllers are now set up.
