---
title: "GPD Optimisation Guide: Optimising Your Handheld Gaming PC"
source_url: "https://gpdstore.net/kb/gpd-duo-support-hub/kb-article/gpd-optimisation-guide/"
source_site: gpdstore.net
type: kb-article
date: 2024-11-11
wp_id: 3479
---

[GPD handheld gaming PCs](https://gpdstore.net/product-category/gpd-handheld-gaming-pcs/), such as the GPD Win 4, offer powerful performance in a compact form factor, but optimising Windows on these devices can significantly enhance both performance and battery life. From utilizing specialized software like Motion Assistant for auto-TDP adjustments to implementing system-level tweaks, there are various strategies to maximize the potential of your GPD portable gaming computer.

We have split our GPD Optimisation Guide into three sections based on general computer experience required.

## Low experience level

We begin our GPD optimisation guide with some easy tweaks you can perform straight away.

### Screen Brightness Adjustment

Adjusting screen brightness is an effective way to conserve battery life on Windows mobile gaming PCs such as the [GPD WIN MAX 2](https://gpdstore.net/shop/gpd-handheld-gaming-pcs/gpd-win-max-2-2024/). To change brightness in Windows 10 and 11:

* Use the Action Center: Click the notification icon in the taskbar and adjust the brightness slider
* Use keyboard shortcuts: Many laptops have dedicated function keys (often Fn + F1/F2) to control brightness
* Access Settings: Go to Settings > System > Display and use the brightness slider

Lowering screen brightness can significantly extend battery life, especially on portable gaming PCs.

### Disabling Windows Search Indexing

Disabling search indexing in Windows can improve system performance, especially on handheld gaming computers. To disable indexing:

* Open Services (services.msc) and locate “Windows Search”
* Set the Startup type to “Disabled” and click “Stop”
* Alternatively, use Command Prompt (as administrator) and enter: `sc stop "wsearch" && sc config "wsearch" start=disabled`

While disabling indexing may slow down searches, it can free up system resources. For users who keep files organized, this trade-off may be worthwhile. However, note that some Windows functions and apps may be affected, so consider your usage habits before making this change

### Graphics and Display Optimization

To optimise graphics and display settings for better performance and battery life on Windows compact gaming PCs:

* Lower the screen resolution: Go to Settings > System > Display and select a lower resolution from the “Display resolution” dropdown.
* Adjust visual effects: Open “Adjust the appearance and performance of Windows” and select “Adjust for best performance” to disable animations and visual enhancements.
* Reduce color depth: In advanced display settings, change the color depth to 16-bit for less demanding graphics processing.
* Enable Game Mode: For gaming, turn on Game Mode in Windows settings to prioritize system resources for games
* Update graphics drivers: Ensure your GPU drivers are up-to-date for optimal performance and compatibility.

These adjustments can significantly reduce system load and power consumption, extending battery life and improving performance on lower-end devices. Additionally, consider lowering in-game graphics settings such as anti-aliasing, shadows, texture quality, and resolution to further decrease demand on system resources. Capping the frame rate at 30-60 FPS can dramatically improve battery life, enhancing both performance and efficiency.

### Wireless Connectivity Management

To conserve battery life on a Windows mobile gaming PC, disabling Wi-Fi and Bluetooth when not in use can be effective. Here are methods to turn off these wireless connections:

* Use Device Manager: Open Device Manager, expand “Network Adapters” and “Bluetooth,” right-click on the respective adapters, and select “Disable” This method is more permanent but may be reversed by Windows updates on your gaming handheld.
* Enable Airplane Mode: Quick access through the Action Center or Settings > Network & Internet > Airplane mode This disables all wireless communications, including Wi-Fi and Bluetooth.
* Group Policy (for administrators): Disable Bluetooth and Wireless Autoconfig services through Computer Configuration > Windows Settings > System Services

Remember to check these settings after Windows updates, as they may sometimes re-enable wireless connections. While disabling these features conserves battery, it’s important to balance this with your connectivity needs.

### Windows and Driver Update Benefits

Updating drivers to the latest versions can significantly improve system performance and stability. Here’s how:

* Enhanced hardware compatibility: New driver versions often include optimizations for better communication between hardware components and the operating system, leading to improved overall system performance.
* Bug fixes and security patches: Driver updates frequently address known issues and vulnerabilities, reducing system crashes and protecting against potential security threats.
* Performance optimizations: Updated drivers, especially for graphics cards, can include performance enhancements that boost frame rates in games and improve rendering speeds for graphics-intensive applications.
* New feature support: Driver updates may enable support for new technologies or features, allowing your hardware to take advantage of the latest advancement.
* Improved power management: Some driver updates include optimizations for better power efficiency, potentially extending battery life on laptops and mobile devices.

While updating drivers is generally beneficial, it’s important to obtain updates from reliable sources such as device manufacturers’ websites or trusted driver management tools to avoid potential security risks. Read our [How to Update Windows and Drivers for your GPD guide here](https://gpdstore.net/kb-article/how-to-update-windows-and-drivers-for-your-gpd/) for further information.

## Medium experience level

Next in our GPD Optimisation Guide we move to the medium experience level. These will require some knowledge of what you need to do and be aware of.

### Auto TDP Adjustment Tools

[Handheld Companion](https://github.com/Valkirie/HandheldCompanion) offers powerful auto-TDP functionality for GPD and other Windows handheld gaming PCs, allowing dynamic power adjustments to optimise performance and battery life. To utilize this feature:

* Install Handheld Companion from the official GitHub repository
* Enable auto-TDP in the Performance settings and set a target FPS
* Create game-specific profiles to customize TDP limits and other settings

The software automatically adjusts TDP based on game demands, potentially extending battery life by 30 minutes or more in some titles. For optimal results, combine auto-TDP with frame rate limiting and CPU boost disabling. While Handheld Companion is highly versatile, users may need to experiment with settings to find the ideal balance between performance and power efficiency for each game.

### Disabling Background Processes

To optimise Windows performance, disabling non-essential background processes can be an effective strategy. Here’s how to manage these processes:

* Open Task Manager (Ctrl + Shift + Esc) and go to the “Startup” tab to disable unnecessary startup programs
* Use the Services app (services.msc) to disable non-essential services. Some safe-to-disable services include:
  + Windows Mobile Hotspot Service
  + Bluetooth Support Service (if not using Bluetooth devices)
  + Print Spooler (if not using printers)
  + Windows Camera Frame Server (if not using a webcam)
  + Windows Insider Service (unless part of the Insider Program)
* Consider using tools like MiniTool System Booster or PC HelpSoft Driver Updater to automate the process of identifying and disabling unnecessary background tasks

Remember to create a system restore point before making changes, and only disable services you’re certain you don’t need to avoid potential system issues.

## High experience level

And finally in our GPD Optimisation Guide we take a look at some of the more advanced and extreme methods that may improve system performance and/or battery life.

### Windows 10 LTSB Installation

Windows 10 LTSB (Long-Term Servicing Branch) is a specialized version of Windows 10 Enterprise designed for stability and minimal updates. While officially available only to organizations with volume licensing agreements, users can obtain it through Microsoft’s 90-day Enterprise evaluation program. To install Windows 10 LTSB:

* Download the ISO file from Microsoft’s evaluation center, selecting “Windows 10 LTSB” during download
* Create a bootable USB drive using tools like Rufus
* Install Windows following standard procedures, but be aware it will function normally for only 90 days without activation
* Install necessary drivers, which may require backing up original drivers or using manufacturer-provided installers

Note that while LTSB lacks many built-in Windows 10 apps and features like Microsoft Edge and Cortana, it receives regular security updates and is ideal for devices requiring long-term stability.

### ShutUp10 for Privacy Enhancements

O&O ShutUp10++ is a free, portable tool that gives users control over Windows 10 and 11 privacy settings. Key features include:

* Disabling telemetry, location services, and data collection
* Blocking app access to personal information like calendar and messages
* Turning off Cortana, SmartScreen filter, and automatic Windows updates
* Providing a simple interface to toggle numerous hidden Windows options

While [ShutUp10++](https://www.oo-software.com/en/shutup10) makes privacy changes easily accessible, it’s important to note that some modifications may only affect the user interface rather than underlying system behavior. Users should create a system restore point before making changes, as the tool allows reverting to default settings if needed.

### Removing Bloatware Applications

Removing bloatware from Windows can significantly improve system performance and free up storage space. To manually remove unwanted pre-installed apps on your compact gaming PC like the [GPD Win Mini](https://gpdstore.net/shop/gpd-handheld-gaming-pcs/gpd-win-mini-2024/):

* Open Settings > Apps > Installed Apps and uninstall unnecessary programs
* Right-click on Start menu items and select “Uninstall” for quick removal
* Use PowerShell commands to remove multiple apps at once (caution advised)

For a more comprehensive approach, consider using scripts like [Win11Debloat](https://github.com/Raphire/Win11Debloat), which can remove pre-installed apps, disable telemetry, and declutter the interface. However, exercise caution when using third-party tools or scripts, as they may unintentionally remove essential components. Always create a system restore point before making significant changes to your Windows installation.

## Share your optimisation tips

Have we missed a useful optimisation tip? Share them in the comments below and we may include them in our GPD Optimisation Guide. Thanks!