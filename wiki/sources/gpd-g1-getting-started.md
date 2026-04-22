---
title: Getting Started with the GPD G1 eGPU Docking Station
type: source
subtype: kb-article
slug: gpd-g1-getting-started
brand: gpd
product: gpd-g1
source_url: "https://gpdstore.net/kb/accessories-support-hub/kb-article/getting-started-with-the-gpd-g1-egpu-docking-station/"
published: 2024-09-06
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, gpd, getting-started, g1, egpu, docking-station, oculink, usb4]
---

# Getting Started with the GPD G1 eGPU Docking Station

The [[gpd-g1|GPD G1 eGPU docking station]] adds a wide range of connectivity options for your handheld or mini PC, including three USB-3 ports, an SD card reader, two HDMI ports, and a DisplayPort. With the ability to connect via OCuLink or USB 4.0, you can transform your compatible device into a high-performance gaming PC.

## Setting Up Your GPD G1 eGPU Docking Station

Setting up the GPD G1 eGPU docking station is quick and straightforward. You can connect peripherals such as a USB mouse, keyboard, or USB stick using the three available USB ports. For display, you have the option to connect one or more monitors using the two HDMI ports or the DisplayPort. If your display supports DisplayPort, it is recommended for the best experience, although HDMI will work just as well.

For certain devices, like the [[gpd-win-max-2|GPD WIN MAX 2 2024]] and [[gpd-win-4|GPD WIN 4 2024]], an OCuLink port is available. If you have one of these newer devices, you can benefit from faster data transfer speeds. Otherwise, you can connect via USB 4.0, which is supported by other devices, including the AYANEO series, older GPD models, ONEXPLAYER, and AOKZOE handhelds.

### Connecting with OCuLink

If you're using the OCuLink connection, remember to connect both the OCuLink cable and the USB 4 cable if you want to use the docking station's ports. The USB connection is necessary for USB peripherals, the SD card reader, and video outputs. Make sure both the GPD G1 and your device are powered off before connecting the OCuLink and/or USB 4.0 cables.

### Connecting Without OCuLink

If your device doesn't have an OCuLink port, simply connect the USB 4 cable between the GPD G1 and your device. Be sure to double-check which port on your device supports USB 4.0, as some ports may not be compatible.

### Powering On

Once all connections are in place, power on the GPD G1 eGPU docking station first. Wait a few seconds, then turn on your device. After a short moment, your device will boot into Windows, and you'll be ready to enjoy enhanced performance with your GPD G1.

## Updating & Installing AMD Graphics Drivers

If your graphics drivers are already up to date, the GPD G1 may automatically set up and install the necessary drivers. To confirm, go to Windows Device Manager > Display Devices. If you see the AMD Radeon RX 7600M XT listed, the drivers have been successfully installed.

When connected via USB 4 only, you should also receive a notification indicating that AMD XConnect Technology has been enabled. This notification will not display if OCuLink is used.

### Troubleshooting & Updating Drivers

If the eGPU is not detected or you wish to update to the latest drivers, follow the step-by-step guide: How to Uninstall and Install AMD Graphics Drivers (available in a dedicated KB article).

After updating or installing the drivers, shut down your device and then turn off the GPD G1. Wait a few moments, power on the GPD G1 first, and then turn on your device.

### Verifying Installation

Once Windows has booted up again, check that the AMD Radeon RX 7600M XT appears under Windows Device Manager > Display Devices. If it doesn't show up, switch off the GPD G1, wait ten seconds, and then turn it back on. The AMD Radeon RX 7600M XT should now be listed in Display Devices.

## Updating the GPD G1 BIOS (Optional)

If you need to update your GPD G1's BIOS, the process is simple and straightforward. Follow the dedicated G1 BIOS Update guide (available as a separate KB article).

## Troubleshooting Your GPD G1 eGPU

### Why Are Games Running Slower Than Expected?

If your games are running slower than anticipated, several factors could be causing the issue:

**Ensure the Game Is Using the Correct GPU:** Verify that the game is utilizing the AMD Radeon RX 7600M XT eGPU instead of your device's internal graphics, like the AMD Radeon 780M. Check the game's video or display settings to see if there's an option to select the GPU. This setting might be listed under names like "GPU" or "Monitor."

**Adjust Game Video Settings:** If the video settings are too high, the game may not perform as expected. Many games offer recommended settings that automatically optimize graphics based on your hardware. If issues persist, try lowering the screen resolution to 1440P, 1080P, or even 720P. Alternatively, start with lower default graphics settings and gradually increase them until performance starts to degrade. Then revert to the previous stable setting.

**Internal Display Considerations:** Using the internal display of your handheld can reduce the eGPU's efficiency. This is because data must travel from the handheld to the GPD G1 and back again, consuming twice the bandwidth through the USB 4 cable. To improve performance, it's recommended to use an external display when possible, as this requires less bandwidth and boosts efficiency.

### AMD Radeon RX 7600M XT Not Detected

If your device is not detecting the AMD Radeon RX 7600M XT, follow these steps:

**Ensure Device Compatibility:** Make sure your device supports either OCuLink or USB 4.0. Check that all cables are securely inserted into the correct ports on both ends.

**Using USB 4:** If your device lacks an OCuLink port, confirm that you are connecting to a USB 4 port. If your device has multiple Type-C ports, refer to the manual to identify the correct USB 4.0 port.

**Power Cycle the GPD G1:** Try switching off the GPD G1, wait a few moments, and then turn it back on. Windows should recognize the device, and you may hear the default USB connection sound. If connected via USB 4, you should also receive a notification that AMD XConnect Technology has been enabled.

**Reinstall the Drivers:** Sometimes, conflicts may occur between newer and older driver versions. Try reinstalling the drivers by following the steps in the AMD Graphics Drivers guide to fully uninstall and reinstall fresh drivers.

### Resolving GPD G1 Connectivity Issues

To use the additional ports on the GPD G1, the USB cable must be connected, as the OCuLink cable only transfers data for the GPU. A USB 4.0 cable is included with the GPD G1, and it's recommended to use this specific cable. Other cables might be USB 3.0 or simply charging cables, which won't provide the necessary functionality.

## Where to Buy OCuLink and USB 4.0 Cables

Available from [[droix|DROIX]] (GPDStore):

* **USB 4.0 Type-C Cable** — 40Gbps data transfer speed, Thunderbolt 3 & 4, up to 240W Power Delivery, supports up to 8K @ 60Hz video output, built-in wattage display.
* **GPD OCuLink SFF8611 Cable** — Official GPD OCuLink cable, compatible with GPD G1 eGPU, adapter for devices without OCuLink, support for PCIe Gen 4.0 & 5.0, speeds up to 16GT/s & 32GT/s per lane. Includes 1x M.2 8612 Adapter Card.
* **GPD G1 eGPU Docking Station Protective Case** — Official GPD G1 case with soft lined interior and snug fit.
