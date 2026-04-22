---
title: "How to install a RetroPie image to your MicroSD, HDD or SSD for your Raspberry Pi 4"
type: source
subtype: kb-article
slug: how-to-install-a-retropie-image-to-your-microsd-hdd-or-ssd-for-your-raspberry-pi
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/how-to-install-a-retropie-image/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix, installation, emulation]
---

Hi there! A friend of us here at DROIX has created a handy video going over the process of how to install a RetroPie image on an SSD (or a 2.5-inch HDD), so we felt it’d be helpful to the community at large to post it onto our knowledge base!

If you are familiar with our [RETROFLAG NESPI 4 DIY Kit,](https://droix.net/product/droix-nespi-4-diy-console/) you may notice that it comes with a hollow “cartridge”. This cartridge is used to hold a 2.5-inch SSD or HDD that can then be inserted into the system to run whatever OS you have installed on it. Much like the cartridge-based system of the device the NESPI 4 is styled after!

The most common OS people choose to run on the NESPi is [RetroPie.](https://retropie.org.uk/) An open source project with the aim of turning the Raspberry Pi series of computers into fully-fledged retro gaming machines.

We provide our kit with a microSD card since it’s the most lightweight and easy to handle method, but for those who wish to use an SSD/HDD of their own, check the below video for more information on how to install a RetroPie image on your device of choice!

## [Video] How to install a RetroPie image

<https://youtu.be/J1fGwdXcKT4>

We also wrote a transcript of the video on how to install a RetroPie image for those who may be harder of hearing, or unable to listen right now!

```
0:00 Intro
Hello and welcome to Retro Gaming Batner. In this brief video, I will be showing how to install  a pre-built RetroPie image onto your microSD card, hard drive or SSD.
The process is quite easy, but if you have never done it before, it can be a bit daunting. At the end, you get to enjoy some retro games. What's there to lose?

 0:31 Extracting Archive (.rar) files
Once you have downloaded the RetroPie image files. They may be in an archive format such as .rar. You will first need to extract the archive to get an image file. If you do not have an archive extractor, then you can download WinRar or 7zip. There are links to both in the description.
Right-click on the file, and depending on which software you are using, you will see options to extract the archive. Here they are for both WinRar and 7Zip.
Choose "extract here" and it will start to extract the file.
Depending on the size of the files and your drive speed, this may take some time. So while you're waiting, check out some more of our videos!

 1:19 How to write an image file to your storage

Once the extraction process has completed, you should now see a .img file in the same folder. Now, you can write the image file to your Raspberry Pi storage.
I recommend BalenaEtcher for writing images, as for me at least it's a bit faster than others, and it's also available on Mac and Linux.
Connect the pi's storage to your pc and run (Balena)Etcher in admin mode. Choose "flash from file" and it will bring up the file browser. Locate and select the image file.
Now, click on "select target", it should hide drives that are your Windows drive (for example), but it may not be 100% accurate. You need to select the one that is your microSD card, hard drive, or SSD. It won't be the same name as mine, so check the drive size matches up in particular.
Make sure you are 100% sure that it is the correct drive. Otherwise you could end up writing over your main drive for example.
Click on "flash" to begin the image flashing process. You will get a warning to ensure that you have chosen the correct device. Double and triple-check and if everything is good, click on "yes im sure" to begin flashing.
Depending on the image size and the speed of data transfer from your pc to the storage, the image writing may take some time. Just let it write the image and go and watch some more of our videos!

 3:05 After the image has been written
Once the process is complete, you can close etcher and safely eject the storage from your PC.
You can now connect the storage to your Raspberry Pi and start the first boot.

 3:27 Useful tips for when first booting a RetroPie image
The first time you boot up, the software needs to set up a few things such as re-sizing the disc partition. The time it takes can depend on the size of your storage; for example, resizing a 256GB partition to one TB and also the speed of the storage.
So just be patient, let it run for 15 minutes or so. It may also reboot the Pi a couple of times in-between.
And then it should boot up to RetroPie with no issues!
Future boots will be faster.
And the final step - enjoy some retro gaming classics!
```

We hope that you’ve found this guide on how to install a RetroPie image to be helpful. Thank you for taking the time to make the video, [Retro Gaming Banter](https://www.youtube.com/channel/UCoogjKYAtZpoiNyxOHG0nJg?sub_confirmation=1)!

Until next time!
