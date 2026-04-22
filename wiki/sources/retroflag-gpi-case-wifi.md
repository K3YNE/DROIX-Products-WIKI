---
title: "How to Connect Retroflag GPi Case to WiFi"
type: source
subtype: kb-article
slug: retroflag-gpi-case-wifi
brand: generic
product: null
source_url: "https://droix.net/knowledge-base/article/how-to-connect-retroflag-gpi-case-to-wifi/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, generic]
---

You need to have a Raspberry Pi **Zero W** installed, a **Zero** does not support WiFi or Bluetooth.

Create a new text file and name it **wpa\_supplicant.conf**

Open the **wpa\_supplicant.conf** file with notepad (or notepad++).

Copy and paste the following text in to the file

> country=US  
> ctrl\_interface=DIR=/var/run/wpa\_supplicantGROUP=netdev  
> update\_config=1  
> network={  
> ssid=”your\_wifi\_ssid”  
> psk=”your\_wifi\_password”  
> key\_mgmt=WPA-PSK  
> priority=1  
> }

You can now update the three lines shown below in the red boxes

Replace the country code if needed (GB, FR, DE, ES, US, CA etc..).

Replace **your\_wifi\_ssdid** with your wifi ssid (ex: ‘’homewifi’’).

Replace **your\_wifi\_password** with your wifi password (ex: ‘’1234’’).

Save and copy it to the root of boot partition on your Micro SD Card (the only partition you see on PC after burning the image file).

Copy it on **wifibackup** folder too for an easy re enable by script.

Insert the Micro SD Card back into the Retroflag GPi case and it is now ready to use.
