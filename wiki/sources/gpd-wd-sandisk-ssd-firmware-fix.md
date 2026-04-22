---
title: Firmware Update for WD/SanDisk 2TB SSDs Causing Windows 11 24H2 Crashes
type: source
subtype: kb-article
slug: gpd-wd-sandisk-ssd-firmware-fix
brand: gpd
source_url: "https://gpdstore.net/kb/gpd-duo-support-hub/kb-article/wd-sandisk-2tb-ssds-and-windows-11-24h2-crashes/"
published: 2025-04-17
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, gpd, ssd, firmware, windows-11, troubleshooting]
---

## The Problem: Unexpected System Instability

A significant issue has emerged for users attempting to install or run the Windows 11 version 24H2 update, manifesting as disruptive Blue Screen of Death (BSOD) errors. These system crashes appear specifically linked to certain 2TB NVMe Solid State Drives (SSDs) from Western Digital (WD) and its subsidiary, SanDisk. Reports highlight systems becoming unstable, frequently crashing, or getting stuck in boot loops. This problem could potentially affect users across various systems, including GPD handheld gaming PCs like the [[gpd-win-max-2|GPD WIN MAX 2 2025]] if equipped with one of the specific drives.

Western Digital has acknowledged the problem and pinpointed the cause. A corrective firmware update is now available for the specific SSD models involved, designed to resolve the incompatibility with Windows 11 24H2. WD strongly advises users whose systems contain the affected SSDs to apply this update as soon as possible.

Applying this firmware update is not just a fix for currently unstable systems; it is also a crucial preventative step. Users with potentially affected SSDs, perhaps in devices like the [[gpd-duo|GPD Duo]], should consider updating the firmware *before* upgrading to Windows 11 24H2 to avoid encountering these BSODs. There are indications Microsoft might block the 24H2 update on systems with the older, problematic firmware.

## Identifying the Issue: Symptoms and Affected Models

The most prominent sign of this problem is the appearance of frequent BSOD crashes following the installation or attempted installation of the Windows 11 24H2 update. These crashes might happen during regular use, amidst the update procedure, or soon after booting the system.

Specific error messages often accompany these BSODs, with "*CRITICAL_PROCESS_DIED*" being common, and "*KERNEL_DATA_INPAGE_ERROR*" appearing occasionally. Checking the Windows Event Viewer (System log) may also reveal recurring "stornvme" errors (Event ID 11), often mentioning controller errors on "\Device\RaidPort1" or "\Device\RaidPort2". These specific indicators strongly point towards the firmware incompatibility issue, potentially impacting users of various devices, including compact systems like the [[gpd-pocket-4|GPD Pocket 4]].

This issue is confirmed only for specific **2TB capacity models** within certain WD and SanDisk NVMe SSD product lines. Drives from the same product lines but with different capacities (like 1TB or 4TB) and other WD/SanDisk SSD models (including all WD SATA SSDs) are reportedly not affected.

### Affected WD and SanDisk 2TB NVMe SSD Models Requiring Update

| MODEL NAME | MODEL NUMBER | REQUIRED UPDATE FIRMWARE VERSION |
| --- | --- | --- |
| WD_BLACK SN770 NVMe SSD | WDBBDL0020BNC, WD0E | 731130WD |
| WD_BLACK SN770M NVMe SSD | WDBDNH0020BBK, WD0G | 731130WD |
| WD Blue SN580 NVMe SSD | WDBWMY0020BBL, WD0E | 281050WD |
| WD Blue SN5000 NVMe SSD | WDBS3F0020BNC, WD0E | 291020WD |
| SanDisk Extreme M.2 NVMe SSD | SDSSDX3N-2T00 | 731130WD |

You can usually find your SSD model in Windows using "System Information" or "Device Manager" (under Disk Drives). The model number is also printed on the SSD's physical label.

## Technical Background: The Host Memory Buffer (HMB) Conflict

The instability stems from a conflict between how Windows 11 version 24H2 handles the Host Memory Buffer (HMB) feature and the original firmware on the affected 2TB WD/SanDisk SSDs.

HMB is a feature common in DRAM-less NVMe SSDs, which do not have their own dedicated DRAM cache. It allows the SSD to use a small portion of the computer's main RAM for caching essential data like mapping tables, boosting performance.

Evidence suggests Windows 11 24H2 altered how it allocates RAM for HMB. While earlier Windows versions might have limited HMB allocation (potentially to 64MB), version 24H2 seems to allocate a larger amount, possibly up to the size requested by the SSD firmware itself — around 200MB for these specific 2TB drives.

The problem is that the original firmware on these particular 2TB models was apparently unable to reliably manage this larger HMB allocation. When Windows 11 24H2 assigned the larger memory buffer, it caused errors within the SSD controller, leading to system freezes and BSODs.

While some users found a temporary fix by editing the Windows Registry to force the older, smaller HMB allocation, this is not the official or recommended long-term solution and could potentially reduce SSD performance. Western Digital's firmware update directly corrects the issue within the drive's own software.

## The Solution: Applying the Firmware Update

Updating the SSD firmware using Western Digital's official software is the definitive fix. However, **extreme caution and preparation are necessary**.

### Step 1: ABSOLUTELY CRITICAL — Back Up Your Data

**Before you do anything else, back up every important file from the affected WD or SanDisk SSD.** Copy your data to a separate storage location — another internal drive, an external USB drive, network storage, or a trusted cloud service.

Firmware updates, while generally safe, carry an inherent risk. Power loss during the update, unexpected software errors, or other interruptions could corrupt the firmware, potentially making the SSD unusable and causing **total data loss**. **Do not skip this step.**

### Step 2: Obtain and Install Western Digital Dashboard

The WD Dashboard software has been discontinued by WD, but you can download the SanDisk version from the [SanDisk software downloads page](https://support-en.sandisk.com/app/products/downloads/softwaredownloads).

Install the software (compatible with Windows 10 and 11). Note that macOS users cannot use this tool for the update.

### Step 3: VITAL REQUIREMENT — Internal Drive Installation

**The affected SSD must be installed directly inside your computer.** It needs to be connected to an M.2 slot on the motherboard or via an appropriate internal PCIe adapter. This applies whether it is in a desktop, a standard laptop, or a specialized device like the [[gpd-win-max-2|GPD WIN MAX 2 2025]] or [[gpd-pocket-4|GPD Pocket 4]]. **The WD Dashboard software will almost certainly fail to detect the SSD correctly or perform the update if the drive is connected via an external USB enclosure or adapter.**

### Step 4: Execute the Firmware Update via WD Dashboard

With your data safely backed up, the Dashboard installed, and the SSD confirmed as internally connected, proceed with the update:

1. **Open** the Western Digital Dashboard application.
2. **Select the Drive:** Ensure the correct affected 2TB SSD is chosen from the list or dropdown menu.
3. **Go to Tools:** Click the "Tools" tab or section.
4. **Select Firmware Update:** Find the "Firmware Update" option.
5. **Check for Updates:** Click the "Check for Updates" button. The software will contact WD servers.
6. **Start Update:** If a new firmware (matching the version in the table above) is detected, click "UPDATE FIRMWARE".
7. **Follow Instructions:** Pay close attention to on-screen prompts. **Crucially, do not interrupt the process** (do not shut down, close the app, or disconnect power).
8. **Restart Required:** After the update finishes successfully, the Dashboard will likely ask you to shut down or restart your PC. This is essential for the new firmware to activate. Comply with the prompt.
9. **Verify (Optional):** After restarting, you can reopen the Dashboard, select the drive, and check the "Firmware Version" on the status page. It should now reflect the updated version.

## Post-Update: Next Steps and Support

After restarting with the updated firmware, the BSOD crashes specifically linked to the Windows 11 24H2 HMB issue should cease. Your system should now be stable, allowing you to run or install Windows 11 24H2 without the related errors.

If BSODs continue *after* confirming the correct firmware is successfully installed, or if you encountered errors *during* the update itself:

* If you are a **DROIX / GPD Store customer** and the SSD was included with your device, contact [customer service](https://gpdstore.net/contact-us/).
* **Contact WD Support:** Reach out to Western Digital's official customer support at [support.wd.com](http://support.wd.com). Have your SSD's serial number and system details ready.
* **Investigate Other Causes:** BSODs can have many causes beyond this specific firmware issue. If the update fixed the HMB problem but crashes persist, investigate other potential culprits like conflicting drivers, faulty RAM, overheating, power supply problems, or other hardware issues.
