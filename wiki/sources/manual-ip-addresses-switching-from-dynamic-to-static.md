---
title: "Manual IP Addresses – Switching From Dynamic To Static"
type: source
subtype: kb-article
slug: manual-ip-addresses-switching-from-dynamic-to-static
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/manual-ip-addresses-switching-from-dynamic-to-static/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix]
---

If you’re not sure what a static IP address is, and don’t have any problems on your home network, you can probably safely ignore the steps in this post. If, however, you want to open up ports on your device to the internet (for example we’ll be writing a post about using a DROIX Q7 as a security camera soon), then your DROIX device will always need to have the same IP address on your home network.

Just to be clear, your external IP address is the same for all devices on your network at home. This IP address is how servers and other computers communicate with you via the internet, and your ISP assigns it to you.

Your internal IP address is how different devices (whether they’re using WiFi or a network cable to connect) communicate with each other.

Think of your external IP address as being equivalent to your house’s postal address. If anyone wants to send you a parcel, they write the house address on a label, and the postman knows where to send it.

Your internal IP address is a bit like having all the rooms in your house clearly labelled, so if you’re told to take a pile of ironing to the kitchen, you don’t end up dumping it in the bathroom!

In case you don’t often get a chance to play with/tweak your device, we’ll go ahead with some basic instructions now.

First you’ll need to check your modem/router’s IP address. It will probably be something like:

192.168.1.1 OR 192.168.0.1, basically just a change from 1 to 0 in the third number of the IP address.

If you’re not certain how to check the modem/router’s IP address, try looking on the bottom of it, manufacturers often print a label there with the defaulty configuration values.

If that doesn’t help, click the Windows Start button on your PC (bottom left corner, normally an icon of a Windows flag), and then click Control Panel. In the Control Panel’s search box, type network and you should see in the results a heading called “Network and Sharing Center”. Within that list, click View Network Connections. From here, right click on the icon that is labelled with your PC’s method of network conneciton (so Local Area Connection for a cabled connection, or one that mentions WiFi for a wireless connection). After right clicking, a menu will appear, click on the Status entry. In the new window, click the Details button, and you’ll find your modem/router’s IP address listed in the IPv4 Default Gateway entry.

With this information ready, turn your DROIX device on, and click on the Settings icon in the list of all apps.

If you can see WiFi/Ethernet in a list on the left hand side, click on whichever your DROIX device is using. If you can’t see a long vertical list of Settings-related entries, click on the last tab on the right, and select the More/Advanced Settings button first.

If you’re using WiFi, then please:

Long click on the name of your WiFi network name and select Modify network

Click on the single down arrow at the bottom of the page if the on screen keyboard is in the way

Now tick the Show advanced options entry, leave Proxy at None, and change IP settings from DHCP to  to Static

You’ll need to scroll the page down to see all the settings you need to enter. Once complete, click the Save button

If you’re using Ethernet (a network cable) instead of WiFi, then please:

Select the Ethernet entry

Now click on Static IP Settings

Tick the Use static IP box

Enter in all the details requested and click the go back/return key on your remote control

Confirm you want to save these details

Recommended Settings:

**GATEWAY**: 192.168.1.1 (IF YOUR MODEM/ROUTER is actually 192.168.0.1 , use that instead)  
**SUBNET MASK**: 255.255.255.0 (if you’re not asked this, it may have prefilled Network Prefix Length with 24, leave that as it is)

**IP ADDRESS**: 192.168.1.250 (IF YOUR MODEM/ROUTER was 192.168.0.1 then use 192.168.0.250)

**DNS1** and **DNS2**: You can decide which DNS settings to use. Some people enter just their modem/router’s IP address (192.168.1.1 or 192.168.0.1) and let the modem/router farm out DNS requests correctly to the actually DNS servers (your ISPs).  
Or you can look up your ISP’s primary and secondary DNS servers and enter these. OR…  
You can use a 3rd party’s DNS servers. Most people would either go with Google or OpenDNS.  
Google’s primary= 8.8.8.8 and their secondary is 8.8.4.4  
OpenDNS primary= 208.67.220.220 and secondary = 208.67.222.222

Please note:  
There is the outside chance that instead of 192.168.1.x or 192.168.0.x your home network is based on a different range, or that your modem/router isn’t 192.168.0.1 or 192.168.1.1 , but those addresses cover 99% of default setups on home networks.

Also, using 192.168.x.250 is being a bit lazy/naughty, as we should really set up the X7’s IP address in your modem/router as static, and remove it from the DHCP pool. However, unless you’ve got hundreds of devices connected to your home network, a clash isn’t likely to occur.

That’s it, you should be done. Different versions of Android may have slightly different labels, but the process above should hold true if you use a bit of logic. For example, the screenshots above will match most DROIX models, but the iMX6, when entering static IP details for an Ethernet connection, looks like this: