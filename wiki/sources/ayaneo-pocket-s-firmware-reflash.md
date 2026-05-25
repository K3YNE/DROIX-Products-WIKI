---
title: "AYANEO Pocket S Firmware Reflash Guide"
type: source
subtype: kb-article
slug: ayaneo-pocket-s-firmware-reflash
brand: ayaneo
product: ayaneo-pocket-s
source_url: "https://droix.net/knowledge-base/article/ayaneo-pocket-s-firmware-reflash-guide/"
published: 2024-10-14
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, ayaneo, ayaneo]
---

The [AYANEO Pocket S](https://droix.net/product/ayaneo-pocket-s/) is a high-end flagship Android handheld game console. Since its launch, the AYANEO Pocket S has received wide acclaim and recognition from gamers. At the same time, AYANEO’s R&D team continues to optimize the software ecosystem to create a more complete handheld gaming experience for gamers.

This time, we have brought gamers the [AYANEO Pocket S](https://droix.net/product/ayaneo-pocket-s/) system upgrade package and image flashing tool, as well as a guide to the system package flashing guide, so that gamers can DIY upgrade Pocket S and instantly get the purest handheld gaming experience.

## Downloading the Software and Firmware

You can download all the files required [here](https://droidbox.sharepoint.com/:f:/s/Purchasing/Eh46N8n1Zk9Mj_ddPod1qN0BWlFhr5OUrgoJVQmaNJniOQ?e=aMGkAe).

## Installation of software and drivers

Install the QPST Tool  
Install the Qualcomm 9008 Driver

## Firmware Updating

Open the QFIL Tool, select **Flat Build**

![AYANEO Pocket S Firmware Reflash Guide](https://droix.net/knowledge-base/wp-content/uploads/2024/10/AYANEO-Pocket-S-Firmware-Reflash-Guide-1-1024x775.jpg)

Select **Browse**. Choose the firmware package path, select all files in the lower right corner, choose **thexbl sdevprg\_ns.melf file**, and click **Open**

![AYANEO Pocket S Firmware Reflash Guide-2](https://droix.net/knowledge-base/wp-content/uploads/2024/10/AYANEO-Pocket-S-Firmware-Reflash-Guide-2-1024x590.jpg)

AYANEO Pocket S Firmware Reflash Guide-2

Select **Load XML**. The path will be automatically located, after confirming the correct path above, select all files, and click **Open**

![AYANEO Pocket S Firmware Reflash Guide](https://droix.net/knowledge-base/wp-content/uploads/2024/10/AYANEO-Pocket-S-Firmware-Reflash-Guide-3-1024x596.jpg)

Click configuration at the top, then select **FireHose Configuration**.

![AYANEO Pocket S Firmware Reflash Guide](https://droix.net/knowledge-base/wp-content/uploads/2024/10/AYANEO-Pocket-S-Firmware-Reflash-Guide-4-1024x744.jpg)

Choose Device Type: **UFS**  
Check: **Reset After Download** – device will automatically boot after download  
Check: **Erase All Before Download** – fully erase before downloading  
Choose according to your needs, and click **OK**

![AYANEO Pocket S Firmware Reflash Guide](https://droix.net/knowledge-base/wp-content/uploads/2024/10/AYANEO-Pocket-S-Firmware-Reflash-Guide-5-1024x505.jpg)

The device enters 9008 mode, connect USB to PC, and 901D port will be displayed at this time.

![AYANEO Pocket S Firmware Reflash Guide](https://droix.net/knowledge-base/wp-content/uploads/2024/10/AYANEO-Pocket-S-Firmware-Reflash-Guide-6-1024x760.jpg)

Adb reboot edl – the device enters 9008 mode, and will display as 9008 at this time.

![AYANEO Pocket S Firmware Reflash Guide](https://droix.net/knowledge-base/wp-content/uploads/2024/10/AYANEO-Pocket-S-Firmware-Reflash-Guide-7-1024x767.jpg)

Click **Download** to start downloading.

Once the process has completed, the AYANEO Pocket S will automatically reboot. The first boot may take longer than usual as everything is being set up again.
