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

![](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/RetroPie-Reset-Controllers-1-300x169.png)

Choose **Manage Packages**

![](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/RetroPie-Reset-Controllers-2-300x169.png)

Choose **Manage Core Packages**

![](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/RetroPie-Reset-Controllers-3-300x169.png)

Choose **emulationstation (Installed)**

![](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/RetroPie-Reset-Controllers-4-300x169.png)

Choose **Configurations / Options** (it may also be named Configurations Tools)

![](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/RetroPie-Reset-Controllers-5-300x169.png)

Choose the option to **Clear/Reset Emulation Station input configuration**

![](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/RetroPie-Reset-Controllers-6-300x169.png)

Choose **Yes** to proceed to clear the controller settings.

![](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/RetroPie-Reset-Controllers-7-300x169.png)

A prompt will confirm the settings have been cleared. Choose **OK** and then keep choosing **Exit** to return to the Command Prompt screen.

![](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/RetroPie-Reset-Controllers-8-300x169.png)

Type: **reboot** and press Return on the keyboard.

This will reboot the system and go back into the menus where you will be able to reconfigure the controls when prompted.

![](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/RetroPie-Reset-Controllers-9-300x169.png)

Do this for the first controller and to skip buttons, hold any button for a couple of seconds. Then when you get to **HOTKEY**, press the **SELECT**button.

![](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/RetroPie-Reset-Controllers-10-300x169.png)

Then for the second controller, press **START**and you will see an option for configuring a controller. You can repeat the process again.

Your controllers are now set up.
