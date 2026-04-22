---
title: How to Reflash AYN Odin 2 Firmware
source_url: "https://droix.net/knowledge-base/article/how-to-reflash-ayn-odin-2/"
source_site: droix.net
type: kb-article
date: 2023-12-20
wp_id: 47148
---

This guide is your comprehensive resource on reflashing firmware for your [AYN Odin 2](https://droix.net/product/ayn-odin-2/) devices. Whether you’re aiming to improve performance, fix bugs, or explore new features, our step-by-step instructions will lead you through the process with ease and precision.

If you intend to flash your device, please follow this guide carefully. Incorrect and improper use or deviation from the instructions may render your device inoperable. DroiX assumes no responsibility for any damages incurred.

## **Before We Start**

Before you begin reflashing your Android [Gaming Handheld](https://droix.net/product-category/handhelds/), it’s essential to ensure you have all the necessary tools listed below. We will provide links to the required firmware & software later in the guide, so there’s no need to search for them right now.

You will need:

* Windows device
* AYN Odin 2
* USB-C cable
* QPST Tool software
* Firmware

## **Download AYN Odin 2 Firmware**

|  |  |
| --- | --- |
| **Model** | **Download Link** |
| AYN Odin 2 | [Download](https://droidbox.sharepoint.com/:u:/s/Purchasing/EZ64QZTKmfFOi4vSEkzucLsBAzM29yscU1IXfzVlG4jfEQ?e=Acodcg), [Alternate Link](https://drive.google.com/drive/folders/1JzccpIsxaxuZ2ZKMe4EU8zlcg9I3GkfC) |

The Odin 2 Firmware is not an update. It is intended to reflash your device back to factory settings.

## AYN Odin 2 firmware update instructions

The instructions provided by AYN can be hard to understand at times. That’s why we’re going to walk you through the entire process step-by-step!

On your Windows device, **Extract** the downloaded **zip file** (refer to *Image 1* below). Open the extracted folder and then **Extract** all compressed folders within (see *Images 2 & 3* below).

1. Extract parent folder



2. Extract child folders



3. Child folders extracted

Navigate to **QPST\bin** and run **QFIL.exe** (see *Image 4* below). A program window will open, from here, ensure the **Flat Build** option is selected – then click **Browse…** and open the **xbl\_s\_devprg\_ns**.**melf** file located in **odin2\odin2\_20231201** (shown in *Images 5 & 6* below).

4. Run QFIL.exe



5. Select Flat Build and Path



6. Select .melf folder

Select **Load XML…** and open all of the **raw program XLM files** located in odin2\odin2\_20231201 by holding the Ctrl key and clicking on the respective files (see *Images 7 & 8* below). Another window will be displayed immediately afterwards – open all **patch XML files** from the same location (refer to *Image 9* below).

7. Select Load XLM…



8. Select all raw program files



9. select all patch files

You should be able to see the **RawProgram** and **Patch** files loaded in (see *Image 10* below). Before proceeding, ensure that the Storage Type is set to **UFS** – to change simply click the Storage type located at the bottom right and select **UFS** (refer to *Images 10 & 11* below).

10. XLM files loaded



11. Select storage type

Ensure your device is **powered down** and connect it to the computer. At this point, you should see that there is still **No Port Available** in QFIL (*Image 12* below). We recommend you open **Device Manager** so you can check if the port is correctly recognised once we power the device (*Image 13* below) – as you may need to update drivers if it’s not recognised here.

Press and hold the **volume-** and **power buttons**. This will go into the Odin 2 bootloader. Select **Emergency Mode**, and the Device Manager should recognise the correct port (**Qualcomm HS-USB QDLoader 9008**).

12. No Port Available



13. Device manager

In the QFIL program, you will also be asked to select an **Existing Port**. Click on **Select Port…** and choose the correct port (**Qualcomm HS-USB QDLoader 9008**) and press **OK** (refer to *Images 14 & 15* below). Sometimes the port may be automatically recognised and selected, if this is the case simply proceed to the next step.

14. Select port



15. Select port cont.

With the correct port selected, press **Download** to begin the firmware reflashing *(Image 16* below). You will see a blue bar indicative of the progress – during this time, do not disconnect your device or you may risk rendering the device inoperable. Once complete, you will see **Finish Download** displayed in the Status box (see *Image 18* below). Afterwards, you can simply need to exit the program and boot your Android Gaming Console.

16. Select Download



17. Progress bar



18. Successful download

When entering the bootloader and selecting emergency mode, it’s best to press download in QFIL as quickly as possible.

## Troubleshooting AYN Odin 2

We encountered a few issues whilst trying to install these drivers with the provided instructions, so we made a guide and are covering potential issues.

### Emergency Mode

When entering the handheld bootloader and selecting **Emergency Mode**, it’s best to press **Download** in QFIL as quickly as possible. Spending too much time here has been known to cause issues.

### Disabling Driver Signature

Disable your driver’s signature in the boot menu by pressing **F7** whilst restarting your PC. From here select:

1. **Troubleshoot**
2. **Advanced**
3. **Startup** **Settings**
4. **Restart**

Doing this will cause your PC to reboot with the driver signature disabled until the next time you reboot your device. From here, we recommend updating the drivers and then performing the reflashing whilst the driver signatures are disabled.

### Driver Update for AYN Odin 2

If your port is not being recognized, update its driver through the Device Manager. First, download the required port driver from the link provided below.

|  |  |
| --- | --- |
| **Drivers** | **Download Link** |
| Qualcomm HS-USB QDLoader 9008 | [Download](https://droidbox.sharepoint.com/:u:/s/Purchasing/EVqo_L32I65Au3liYP5kFyMBe5-YdHhJ3msQaEiaLkEgxA?e=PwYspe) |

Download, and extract the **CAB** file. Open Device Manager and add/update the drivers by clicking on either the specific device or **Action**, and then **Update Driver**. Search for the drivers locally and install them.

---