---
title: "How to Add to Your Kodi Library"
type: source
subtype: kb-article
slug: droix-kodi-library-setup
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/how-to-add-to-your-kodi-library/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix]
---

This guide uses the Confluence skin to set up the library, if you’re not comfortable switching skins yet, you may want to wait a week or two before attempting this. If you’re happy clicking on the System menu itself, then Appearance, you can select which skin to use there at the top by clicking it.

Assuming you’re using the Confluence skin now, open up Kodi and hover over the Videos menu. Select files.   
Click on the Add Videos entry, and then the Browse option. Where you go from here depends whether you’re adding local files (for example hard drive physically connected to your device) or over the network (such as media stored on your laptop).

If it is a **local device**, then click on ROOT FILE SYSTEM, then scroll down to and click on STORAGE. If you can’t find what you need, go back one directory and click on MNT.  
Different devices (and firmwares) use different labels, but if you have a USB device attached with the files on (as opposed to a memory card in the device), look for usb\_storage (or simlar), and then click on USB\_DISK0 (assuming you just have one hard drive connected). Finally, click on the name of your hard drive (this will be the label it was given during formatting, or since). Some models will use SDA1 or similar.

If you’re using a memory card, instead of usb\_storage, select external\_sd, sdcard1 or similar.

Now supposed you have all your films in a folded called “GreatMovies”. You would now select that folder, and click the OK button.  
Skip past the following paragraph about adding files over a network to see what needs to be done to complete this process of importing items to your library…

If your adding films/TV series from a hard drive that is connected to a **different device** (over your **home network**), then click on ADD NETWORK LOCATION, instead of root file system. You can use the Windows network (SMB) option instead, however if this doesn’t work on your home’s network, please switch to the Add Network Location option instead.

You’ll need to know a little bit about the PC/NAS/laptop that you’re want to import files from – its IP address, and the user name and password you use to log on (assuming you use security).  
Leave Protocol at SMB (assuming your PC/laptop is Windows based), for server name, enter the IP address of your PC/laptop/NAS. Next to Shared Folder, you’ll need to enter the name you’ve given your network share**§**.  
(Please note, you can instead use the Browse button, instead of manually entering the IP address and folder name, but if that doesn’t work, it doesn’t harm to know your way round your home’s network manually. You can also leave the folder field blank and navigate around all your network shared folders, however this means that everything shared on your PC is easily accessible on your device. If you have media that you’d prefer children not to have two or three click access to, approach with caution!)  
Enter the user name and password you log on to your PC with (for example admin and password). Click OK, and now select the new entry in the list, it will start with SMB:// Navigate to the folder containing the movies/TV series/music videos etc, and click OK.

In either case (local hard drive/network source) you now need to select a name for this import. so click on the text underneath “Enter a name for this media source”. Type in something that makes it easy to remember what you’re importing/playing in the future, and click Done. Now click OK, and select the appropriate option under the text “This directory contains”. Movies, TV Shows or Music Videos are your choices.

If needed, modify the options under Content Scanning options, then click OK. In this last step, you’ll be asked if you want to refresh info for all items within this path. Click Yes. If you’re adding a handful of files, and your internet is working properly, you’ll be done in a minute or two. If you’re importing your entire back catalogue of digital media, it is safe to go and have a cup of tea at this point.

Once this stage completes, you’re done. From now on, when you click on Videos>Files (or with some skins, Videos>Films or even Kids>Films) you should see your entire collection (don’t forget to move the cursor to the far left of your screen to flip between different view modes), with posters, descriptions and other info on hand.

Depending on the version of Kodi you use, and the skin, you may find different entries for pictures, music and other media. If there is a files sub-menu option below it, you can repeat the above process for ensuring Kodi has easy access to tunes and images as well.

If you are using the Confluence Customizable Mod skin in Kodi, you can swap one of the Menu shortcuts to lead to your library instead:  
Open Kodi, click on the System menu. Head to the Appearance section, then click the Settings entry just under Skin Confluence Customizable Mod.  
Now click on Submenu items. Within one of categories shown (3D, Family, Sports etc) find a shortcut you don’t use and click it. Now select Videos Menu, then Videos (Library). Finally click the home icon bottom right of XBMC/Kodi’s screen, and you should find the shortcut has been switched to your Library.

\*\*\*

**§** I’m assuming you’ve already shared the folder with media in it over the network at this point. When you did so, you’ll have had a chance to give it a convenient name. This is what you enter in the Shared Folder box. If you haven’t yet network-shared the folder you need, visit [http://windows.microsoft.com/en-gb/…ver-the-network-from-windows-vista-inside-out](http://windows.microsoft.com/en-gb/windows-vista/share-files-and-folders-over-the-network-from-windows-vista-inside-out) and start reading from the paragraph titled “Sharing files and folders from any folder”. I believe the steps apply to Vista and Windows 7, I’ve not tried it in Windows 8 yet.

\*\*\*

You can label the imports anything you like, but I’ve stuck to something obvious that guests can figure out, like Kids’ TV, Kids’ Films, Music Videos, Films, TV Series. The kids’ stuff is all on a portable hard drive directly connected to the DROIX directly, whilst the rest is on one of the portable hard drives connected to my PC.

Your PC/laptop/NAS does need to be turned on for any files stored there to be accessed by Kodi. There is a *small* effect on the space left on your DROIX. I have around 1.2Tb of files in my Kodi library, and although none of them are actually stored on my device’s internal storage, the metadata for each film/video etc is. So, for every film that has the poster downloaded, the actor and production staff listed, lyrics etc, I lose some space on the DROIX device. Right now this metadata takes up 770Mb of space on my device.
