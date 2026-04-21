# GPD MicroPC Resources

Raw supplier resource extraction from GPD. This file intentionally preserves source-page text and links for later wiki ingest.

## Source Metadata

- Product slug: `gpd-micropc`
- Source URL: https://www.gpd.hk/gpd_micropc_firmware_driver_bios
- Page title: GPD MicroPC Firmware & Driver & BIOS - Shenzhen GPD Technology Co., Ltd.
- Page ID: `71357`
- Retrieved: 2026-04-21
- Head script: https://img.website.xin/pubsf/18006/18006016/cdn-static-pages/pages/pc/71357_en-us.html.Head.js?version=20260421170442
- Body script: https://img.website.xin/pubsf/18006/18006016/cdn-static-pages/pages/pc/71357_en-us.html.Body.js?version=20260421170442
- Download policy: URLs only; firmware, driver, BIOS, archive, and executable files were not downloaded.

## Tabs

### How to upgrade GPD WIN 2 128GB SSD to 512GB

- Tab area: `tabArea0`
- Resource blocks detected: 2

#### 1. MicroPC_RS5_X64_20200602_user-EN

- Block ID: `smv_con_31_58`; visual top: `50px`
- Links:
  - Download: https://drive.google.com/file/d/1yOrtBo8DI66KeJBscwArkAzEXV4ue5PC/view?usp=sharing

Regarding the firmware instructions: The firmware is similar to the Ghost system you commonly use, as it already includes integrated hardware drivers. Therefore, there is no need to install drivers separately. After downloading the firmware and extracting it, there will be a tutorial inside. You can follow the instructions provided to complete the process.
（new）MicroPC_RS5_X64_20200602_user-EN
Download

#### 2. Regarding the firmware instructions: The firmware is similar to the Ghost system you commonly use, as it already includes integrated hardware drivers. Therefore

- Block ID: `smv_con_36_58`; visual top: `350px`
- Links:
  - Download: https://drive.google.com/open?id=1cCaRiQdkU_w16PuroUN45soBN9wr6-YS

Regarding the firmware instructions: The firmware is similar to the Ghost system you commonly use, as it already includes integrated hardware drivers. Therefore, there is no need to install drivers separately. After downloading the firmware and extracting it, there will be a tutorial inside. You can follow the instructions provided to complete the process.
GPD MicroPC Windows Firmware 20190601
Download

### GPD WIN 2 - How To Install / Upgrade Your SSD

- Tab area: `tabArea1`
- Resource blocks detected: 1

#### 1. Ubuntu MATE for GPD MicroPC

- Block ID: `smv_con_147_11`; visual top: `50px`
- Links:
  - Download: https://ubuntu-mate.org/download/gpd_pocket_3/impish/
  - https://www.youtube.com/watch?v=bLI0cFaXJp8: https://www.youtube.com/watch?v=bLI0cFaXJp8
  - https://github.com/wimpysworld/umpc-ubuntu: https://github.com/wimpysworld/umpc-ubuntu

Download
（New）Ubuntu MATE for GPD MicroPC
Configuration changes for the GPD MicroPC include:
1. Enable frame buffer and Xorg display rotation.
2. Accelerometer support for automatic screen rotation.
3. Also automatically rotates touch screen and stylus (draw and erase)
4. Enable fractional scaling by default, Results in an effective resolution of ~1280x720 to make the display panels easily readable.
5. Simple to toggle on/off via the Display Scaler app if you want to restore full resolution.
6. Enable audio via the HDaudio legacy driver.
7. Suspend is implemented via s2idle
8. A temporary workaround until S3 sleep state is supported via the kernel.
9. Enable scroll wheel emulation while holding down the centre trackpad button.
10. Enable Tear-Free rendering by default.
11. Enable double size console (tty) font resolution.
12. Sadly, no support for the fingerprint reader. AFAIK only USB fingerprint readers are supported in Linux.
https://www.youtube.com/watch?v=bLI0cFaXJp8
Putting the cherries on top of the Ubuntu MATE image for the GPD MicroPC. I explain how the automatic screen rotation is implemented, the fractional scaling configuration and complete final QA
https://github.com/wimpysworld/umpc-ubuntu
Please execute the following command to update the device driver:
git clone https://github.com/wimpysworld/umpc-ubuntu.git
cd umpc-ubuntu
sudo ./umpc-ubuntu.sh enable

### Driver and Tool

- Tab area: `tabArea2`
- Resource blocks detected: 2

#### 1. Also supports Pocket 2, P2 Max, WIN 2, but not compatible with Window 10 1607

- Block ID: `smv_con_53_58`; visual top: `50px`
- Links:
  - Download: https://drive.google.com/file/d/1JAIVHNnEjjcQUASOaCR6U96NEY34X3wm/view?usp=sharing

Also supports Pocket 2, P2 Max, WIN 2, but not compatible with Window 10 1607
GPD MicroPC Driver
Download

#### 2. This is a firmware that restores the MicroPC touchpad to the default factory settings. If you upgraded the MicroPC touchpad firmware to "GPD Micro PC touchpad f

- Block ID: `smv_con_63_58`; visual top: `300px`
- Links:
  - Download: https://drive.google.com/open?id=1x23ZsNrbnDcfPO5puKdb6JSiqpZJa0eG

This is a firmware that restores the MicroPC touchpad to the default factory settings. If you upgraded the MicroPC touchpad firmware to "GPD Micro PC touchpad firmware 20190618", you don't like it. You can download the touchpad settings before this firmware is restored.
AMR Firmware normal
Download

### BIOS

- Tab area: `tabArea1592644551046`
- Resource blocks detected: 2

#### 1. MicroPC BIOS v4.18 & EC v4.08 09/21/2023

- Block ID: `smv_con_93_58`; visual top: `50px`
- Dates found: 09/21/2023 -> 2023-09-21
- Links:
  - Download: https://drive.google.com/file/d/1IO86RNOBS6kJyppdWE4h1CnyGsNrzF6s/view?usp=sharing

First, upgrade the EC by formatting the USB drive as Fat32. Copy the contents of the MicroPC_EC_V4.08 folder to the root directory of the USB drive. Insert the USB drive into the USB port of the main unit. Power on the device and press Fn+F7 to enter the boot menu. Select the USB drive as the boot option and proceed with the upgrade.
Next, upgrade the BIOS. Copy the MicroPC.4.18.exe file from the MicroPC.BIOS.V4.18\AfuWin folder to the desktop. Right-click on the file and select "Run as administrator." During the upgrade process, if you encounter an error prompt, do not turn off the device. Instead, end the DOS process in the Task Manager and retry the upgrade.
Decompression Password: 123456
（New）MicroPC BIOS v4.18 & EC v4.08 09/21/2023
Download

#### 2. How To Install / Upgrade Your SSD

- Block ID: `smv_con_133_32`; visual top: `2154px`

How To Install / Upgrade Your SSD
How to upgrade GPD WIN 2 128GB SSD to 512GB
GPD WIN 2 - How To Install / Upgrade Your SSD

### How to upgrade GPD WIN 2 128GB SSD to 512GB

- Tab area: `tabArea0`
- Resource blocks detected: 0

#### Raw Tab Text


(No visible text extracted.)

### GPD WIN 2 - How To Install / Upgrade Your SSD

- Tab area: `tabArea1`
- Resource blocks detected: 0

#### Raw Tab Text


(No visible text extracted.)

## Extracted Checksums

- No SHA1-style checksums detected.

## Password / Archive Notes

- Decompression Password: 123456

## Link Table

| Tab | Resource context | Link label | Original href | Resolved URL |
| --- | --- | --- | --- | --- |
| How to upgrade GPD WIN 2 128GB SSD to 512GB | MicroPC_RS5_X64_20200602_user-EN | Download | https://drive.google.com/file/d/1yOrtBo8DI66KeJBscwArkAzEXV4ue5PC/view?usp=sharing | https://drive.google.com/file/d/1yOrtBo8DI66KeJBscwArkAzEXV4ue5PC/view?usp=sharing |
| How to upgrade GPD WIN 2 128GB SSD to 512GB | Regarding the firmware instructions: The firmware is similar to the Ghost system you commonly use, as it already includes integrated hardware drivers. Therefore | Download | https://drive.google.com/open?id=1cCaRiQdkU_w16PuroUN45soBN9wr6-YS | https://drive.google.com/open?id=1cCaRiQdkU_w16PuroUN45soBN9wr6-YS |
| GPD WIN 2 - How To Install / Upgrade Your SSD | Ubuntu MATE for GPD MicroPC | Download | https://ubuntu-mate.org/download/gpd_pocket_3/impish/ | https://ubuntu-mate.org/download/gpd_pocket_3/impish/ |
| GPD WIN 2 - How To Install / Upgrade Your SSD | Ubuntu MATE for GPD MicroPC | https://www.youtube.com/watch?v=bLI0cFaXJp8 | https://www.youtube.com/watch?v=bLI0cFaXJp8 | https://www.youtube.com/watch?v=bLI0cFaXJp8 |
| GPD WIN 2 - How To Install / Upgrade Your SSD | Ubuntu MATE for GPD MicroPC | https://github.com/wimpysworld/umpc-ubuntu | https://github.com/wimpysworld/umpc-ubuntu | https://github.com/wimpysworld/umpc-ubuntu |
| Driver and Tool | Also supports Pocket 2, P2 Max, WIN 2, but not compatible with Window 10 1607 | Download | https://drive.google.com/file/d/1JAIVHNnEjjcQUASOaCR6U96NEY34X3wm/view?usp=sharing | https://drive.google.com/file/d/1JAIVHNnEjjcQUASOaCR6U96NEY34X3wm/view?usp=sharing |
| Driver and Tool | This is a firmware that restores the MicroPC touchpad to the default factory settings. If you upgraded the MicroPC touchpad firmware to "GPD Micro PC touchpad f | Download | https://drive.google.com/open?id=1x23ZsNrbnDcfPO5puKdb6JSiqpZJa0eG | https://drive.google.com/open?id=1x23ZsNrbnDcfPO5puKdb6JSiqpZJa0eG |
| BIOS | MicroPC BIOS v4.18 & EC v4.08 09/21/2023 | Download | https://drive.google.com/file/d/1IO86RNOBS6kJyppdWE4h1CnyGsNrzF6s/view?usp=sharing | https://drive.google.com/file/d/1IO86RNOBS6kJyppdWE4h1CnyGsNrzF6s/view?usp=sharing |

## Non-URL / Placeholder Links

| Tab | Resource context | Link label | Href |
| --- | --- | --- | --- |
| How to upgrade GPD WIN 2 128GB SSD to 512GB | MicroPC_RS5_X64_20200602_user-EN | (no label) |  |
| How to upgrade GPD WIN 2 128GB SSD to 512GB | Regarding the firmware instructions: The firmware is similar to the Ghost system you commonly use, as it already includes integrated hardware drivers. Therefore | (no label) |  |
| GPD WIN 2 - How To Install / Upgrade Your SSD | Ubuntu MATE for GPD MicroPC | (no label) |  |
| Driver and Tool | Also supports Pocket 2, P2 Max, WIN 2, but not compatible with Window 10 1607 | (no label) |  |
| Driver and Tool | This is a firmware that restores the MicroPC touchpad to the default factory settings. If you upgraded the MicroPC touchpad firmware to "GPD Micro PC touchpad f | (no label) |  |
| BIOS | MicroPC BIOS v4.18 & EC v4.08 09/21/2023 | (no label) |  |
| BIOS | How To Install / Upgrade Your SSD | (no label) |  |
| BIOS | How To Install / Upgrade Your SSD | How to upgrade GPD WIN 2 128GB SSD to 512GB |  |
| BIOS | How To Install / Upgrade Your SSD | GPD WIN 2 - How To Install / Upgrade Your SSD |  |
