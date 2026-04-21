---
title: UPnP – Serving All Your Media Anywhere In The House!
source_url: "https://droix.net/knowledge-base/article/upnp-serving-all-your-media-anywhere-in-the-house/"
source_site: droix.net
type: kb-article
date: 2021-11-20
wp_id: 940
---

This post on **UPnP** (**U**niversal **P**lug a**n**d **P**lay) continues our series on ways to use your DroiX Android Powered Kodi TV box as a media server for your home.

Whether you’re looking to save money (less power required for our models, compared to a full sized PC/laptop) on your electricity builds, keep the noise of your PC to a minimum throughout the day (pop over to <https://droix.net/sipping-power-quiet-characteristics-of-a-droidbox-as-a-server-vs-a-pc> if you’ve not had a chance to read it yet) or just want to more fully realize the potential of your existing technology, we are covering approaches you can use.  
As you may have guessed from part of the meaning behind UPnP, the system exists with the idea of ensuring end users can simply attach new devices to their home network, without needing to delve deeply into subnet masks, IP addresses that can change each boot, announcements or mapping network drives.  
So where should you start? First of all, make sure the storage device you are using for your media collection can be seen (and files opened) on your DroiX device. Whether you’re using a memory card, USB thumb drive or external hard drive, plug it in, then open the ES File Explorer application.

Now expand the “Local” menu on the left, and click on the entry that relates to your storage device. Navigate to a folder with media in it and open one or two to ensure everything is OK with local playback of the files. If anything doesn’t work at this point, you should pause following the steps here and check the storage device on another piece of hardware, perhaps a PC.

If the files played OK, let’s carry on…

Next you will need to decide which application you want to use to serve up your media via UPnP.

**Kodi** and **DBMC** can share media via UPnP, but don’t forget to add the media to the application’s library first.  
We have a post covering this topic at <https://droix.net/adding-to-your-library> as well as a more detailed version (also covering other aspects of setting up Kodi and DBMC) here – <https://droix.net/setting-up-kodi-the-right-way> .

Once Kodi has a library full of your media, you will need to head to System/Settings in Kodi or DBMC and then click on the Services entry. You can click on the “Settings Level” area to ensure all options are shown by changing it to Advanced. The exact options to choose will depend on your usage, but you’ll want to have UPnP sharing and Updates turned on as a minimum.

Another option is to install an application via Google’s Play Store (please see <https://droix.net/adding-to-your-library> if you’ve not yet used it) to handle sharing your media via UPnP. There are a variety of UPnP server apps to choose from but we recommend **BubbleUPnP** as there is both a free and paid version and it is very easy to set up. You can find more information on BubbleUPNP at <https://play.google.com/store/apps/details?id=com.bubblesoft.android.bubbleupnp>.

To see an example of using UPnP to stream media *to* your DroiX, see the video below. You can obviously instead install the application onto your DroiX itself, so the media all comes from storage devices connected to it, rather than from your phone/tablet.

<https://youtu.be/Z4ZV1McFuJQ>

However you choose to set up your DroiX device as a UPnP server, once completed you will find you can now use your existing UPnP clients/services on devices throughout your household to enjoy your media in a location and at a time convenient for you. You won’t need to remember IP addresses or passwords, and you will also find that the UPnP capable playback application will have ways or sorting/categorizing your media collection, making browsing an intuitive experience.

One thing to consider when using UPnP is the type of media you are sharing. Visitors to your house (with your WiFi password or a network cable) will be able to easily access your shared pictures/videos/music, so make sure you don’t have anything shared that would embarrass you. Likewise, if you have young children in your house, they will find it trivial to scan through your shared media, so you may want to use an alternative approach (such as [SMB/Samba sharing](https://droix.net/network-sharing-local-storage-for-kodi-and-dbmc/) with a username and password set) if you have a lot of violent horror movies for example.