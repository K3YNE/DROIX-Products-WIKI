---
title: Retroflag GPi FAQ
source_url: "https://droix.net/knowledge-base/article/retroflag-gpi-faq/"
source_site: droix.net
type: kb-article
date: 2021-11-20
wp_id: 512
---

### Screen display is distorted and/or speaker is buzzing

The common cause of this is the cartridge. The pogo pins which connect the GPi to the Raspberry Zero are not making proper contact. We find that screwing the brass stand-offs quite tight to the case and Zero, and then tightening the silver case screws until they cant be turned any more with little pressure. If you the loosen the silver case screws by a half turn this seems to fix the issue.

Other things you can check are that the contacts on the cartridge may be dirty from finger prints.

### D-Pad is not responding on the Menu or in-game

The GPi case has two controller modes; “Hat mode” and “Axis mode”. Depending on the emulator you are using you may find one mode has better compatibility than the other.

If you find that the D-Pad is not responding in the Menu or in game. Hold the **LEFT** D-Pad button and **SELECT** for 5 seconds until the power LED flashes purple. You should now be able to use the D-Pad to navigate. Note: On some models you need to hold **LEFT** and **START**.

To switch to the other mode, hold the **UP** D-Pad button and **SELECT** for 5 seconds until the power LED flashes purple. Note: On some models you need to hold **UP** and **START**.

You can find more details on the two controller modes **[here](https://droix.net/how-to-switch-input-modes-on-retroflag-gpi-case/)**.

### How to connect Retroflag GPi to WiFi?

You need to have a Raspberry Pi **Zero W** installed, a **Zero** does not support WiFi or Bluetooth. You can follow our guide **[here](https://droix.net/how-to-connect-retroflag-gpi-case-to-wifi/)** for use with popular prebuilt images.

### How do I flash an .img file?

You can find a guide on flashing a MicroSD Card image (.img) file at **<https://droix.net/how-to-flash-a-retropie-sd-card-image-for-the-gpi/>**

### How do I copy ROM’s to the Mini SD Card?

Retropie and Recalbox for example use EXT4 file system as it is Linux based. Unfortunately Windows can not read this format so it is not as simple as copying files via a card reader. There are a few solutions:

– FTP Transfer over WiFi  
– USB transfer – potentially requires mini USB adaptor  
– Copy from PC. If using Windows you will need software such as Paragon Software **<https://www.paragon-software.com/fr/home/linuxfs-windows/>**

You can read more about these methods at [**https://retropie.org.uk/docs/Transferring-Roms/**](https://retropie.org.uk/docs/Transferring-Roms/). We will have more detailed guides soon.