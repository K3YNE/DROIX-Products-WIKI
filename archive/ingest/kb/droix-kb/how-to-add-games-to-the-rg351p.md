---
title: How To Add Games To The RG351P
source_url: "https://droix.net/knowledge-base/article/how-to-add-games-to-the-rg351p/"
source_site: droix.net
type: kb-article
date: 2021-11-20
wp_id: 1105
---

Inveitably, most people who purchase the an RG351P will wonder how they add more games to it. We at DroiX are here to outline those two processes in the form of a handy text guide. This guide is also applicable to the RG351M.

This guide will be covering Windows specifically. However, the process will be broadly the same for Mac devices as well. You will just need to find the equivalent locations/features within the Mac interface.

There are two ways in which you can add games to the RG351P and it’s contemporaries (as a note, you can also remove games through these same methods). The first of which is…

## Via SD Card

This is the most stSghtforward, and preferred way to add and remove games from the RG351P, RG351M, and RG351V.   
You will need a PC, and a way of reading microSD cards. Either a USB card reader, or a native microSD card slot works fine.

Firstly, remove the SD card from the system, and insert it into your PC.

There might be a sticker over your SD card slot. You’ll need to remove it first.

Now, open the games partition in your file explorer.

The drive letter will change automatically based on how many drives are already connected.

Finally, copy your game files over into the respective folder to add them to the device, or delete them to remove them from the device! It’s really that easy!

There will already be a number of folders present as a sort of structural guide. You can delete the platform-related ones as you wish, but do not rename them!

## I can’t see the partition!

If you can’t see the GAMES partition, it is likely that there has not been a drive letter assigned to it. In essence, this is like trying to enter a house with no door.

To fix this, you will need to assign a drive letter to the partition. This can be done either through [third party tools](https://www.partitionwizard.com/), or directly in Windows as follows.

Firstly, open the disk management interface. Type “disk manager” in the Windows 10 search bar, then select “Create & Format Hard Disk Partitions”.

You can type a variety of approximations to get the same result. “drive manager”, “disk m” – it usually works.

Now right click the GAMES partition and select “Change Drive Letter and Paths…”

The partition will usually be around 56GB in size.

Click “Add”, choose a drive letter, then click “OK” in both windows.

The letters available will depend on what’s already in the device. It doesn’t matter which one you pick.

You’ll now be able to see the partition, and can add/remove games as you please.

The other way of adding/removing games from the RG351P (and its family) is:

## Via SSH

This method is a little more complex, but is overall not difficult. You will need:

This second method can be used even if you do not have an SD card reader.

First, make sure that your RG351P is connected to the internet, and make a note of its IP address.

The IP address may be different each time you connect. Keep that in mind.

Now, open your FTP Client and create a new SFTP connection for the IP address (host name) you have written down.  
**The RG351P username is “root”**, and **the RG351P password is “emuelec”**. Leave the port as 22.  
Save it, and click “Login”.

If you get a warning regarding connecting to an unknown server, just click “Yes”.

If successful, you should now be able to browse the contents of the device. Should you be unsuccessful, make sure that the host name and username/password are correct.

The left half represents our PC. The right half represents the handheld.

Navigate to the correct folder, and you can now copy over and remove files as your FTP client allows. Click the folder with two dots as the name to go up a directory level.

The correct directory is /var/media/GAMES.

You can now remove games by clicking them and deleting them (in WinSCP – click the file and then click the red cross icon that lights up). Or you can copy the files over from your PC to the device (in WinSCP – just drag and drop from the left side to the right side).

---

Thanks for reading this far! If you’re interested in a retro handheld of your own (at the time of writing, including the RG351P, RG351M and RG351V), feel free to check out the variety we have on offer below.

Until next time!