---
title: How to power your PC via schedule – Enabling Auto-Power-On on your PC
source_url: "https://droix.net/knowledge-base/article/how-to-power-your-pc-via-schedule-enabling-auto-power-on-on-your-pc/"
source_site: droix.net
type: kb-article
date: 2022-01-13
wp_id: 1525
---

In this guide, we’re going to go over how to enable Auto-Power-On on the [Beelink GK35 mini PC](https://droix.net/product/beelink-gk35/). This process can likely broadly apply to other computers as well.

Automation – it’s a wonderful thing! Through the magic of scheduling and passive “listening”, it is possible to cut out a good chunk of the busywork that would otherwise take up valuable time from your day.

This extends to even the simple act of turning on a computer! Thanks to a handy feature called auto-power-on, it’s possible to schedule your PC to turn itself on without human intervention. This is excellent for those who use their PC at similar times each day, and want it to be ready for them in advance.

## How do I enable Auto-Power-On

**FIRST,** before doing anything. You’ll need to make sure that Fast Startup is **disabled**. Fast-startup is a Windows power settings option that increase the speed at which the computer powers on.

### How to disable Fast Startup in Windows 10

In the age of M.2 NVMe SSDs however, where boot speeds are already extremely fast, the speed gain is negligible, and it ultimately causes more problems than it fixes. In this case, it can hinder auto-power-on and other automation functions from working outright.

To disable fast startup, first open the **control panel** and select **power options**. This can be done by searching for the control panel in the Start menu search bar, then selecting the icon with the green battery. (If you can’t see, change the “View by” to “large icons”.

Changing the view style makes it easier to find what you’re looking for.

Next, select “**choose what the power buttons do**”.

The option can be found on the left-most side of the window.

You will then need to uncheck “**turn on fast startup**” if it is enabled. If the option is greyed out, click the “**change settings that are currently unavailable**” to fix this.

The option will likely be greyed out by default.

Now that you’ve disabled fast startup, you can begin to enable auto-power on.

### How to access the BIOS

Enter the BIOS for the system. There’s two ways to do this:

* Press ESC, DEL, or other keys as defined by your system during the initial booting of the PC (in the case of the GK35, when you see the Beelink logo).
* Access it through Windows’ Advanced Startup Options.

Because we’re already in Windows at this point, it will be quicker to do it via the latter.

In the Windows **start menu**, select the **power** button, then select **restart** **while holding the LEFT SHIFT** key.,

Ignore the other options.

This will bring you into the Advanced Startup options.

From here, select Troubleshoot, Advanced Options, then finally UEFI Firmware Settings. This will reboot the PC straight into the BIOS.

* Once again, ignore the other options. You want “Advanced options”.
* This option will take you straight to the BIOS, after a reboot.

### Enabling Auto-Power-On (RTC Wake)

You can navigate the BIOS via the arrow, enter and escape keys on your keyboard.

Press the right arrow key to move to the **advanced** tab.

From the list of items, select **S5 RTC Wake Settings**.

Finally, select the **Wake Up System from S5** option and set it to either Fixed Time or Dynamic Time.

* **Fixed Time** allows you to set a specific time (24-hour Clock Format) for the system to power on. Some computers can support more granite scheduling (i..e, specific days of the week).
* **Dynamic Time** allows you to make the system automatically power on after a certain period of time has elapsed after it is powered off. For the GK35, you can set this interval to be anywhere from 1 to 5 minutes.

Select whichever type of auto-wake you’re happy with, and then press the escape key.

Navigate to the **Save & Exit** tab, then click **Save Changes and Exit** to exit the BIOS and go back to Windows.

Now whenever your PC is next powered off, it will automatically turn itself on at the time defined by you!

## What is the “S5” power option?

Enabling auto-power on may not initially be as straightforward as you’d like. The Aptio Setup Utility that acts as the BIOS for most mini PC’s can be a harsh, archaic environment full of confusing technical terminology.

In the GK35, the option for auto-power-on is under the “S5 RTC Wake Settings” menu item.

To break it down into easily digestible components:

* “S5” refers to the System Power State. Modern computers can have their power state categorized into 7 distinct stages.
  + S0 = The computer is on.
  + S1-S3 = The computer is asleep. The higher the number, the deeper the sleep and the lower the power consumption. Deeper sleeps will take longer to wake from.
  + S4 = The computer is in hibernation. This is lowest possible point of power consumption without the device being outright turned off. Most useful on mobile devices like laptops.
  + S5 = The system is turned off, except for a small trickle of electricity to components such as the power button and ambient LED lights.
  + G3 = The system is completely off. No electricity, etc. Not commonly found in consumer computers.
* “RTC” stands for “real time clock”. This is a clock that counts time independent of the system’s power state. Ever wonder how your computer knows what day/time it is even when powered off? This is how.
* “Wake” refers to the act of waking up the computer from a “sleep” state (see above).

For more about System Power States, check out the [official Microsoft documentation](https://docs.microsoft.com/en-us/windows/win32/power/system-power-states).