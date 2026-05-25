---
title: "Network Sharing Local Storage For Kodi and DBMC"
type: source
subtype: kb-article
slug: network-sharing-local-storage-for-kodi-and-dbmc
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/network-sharing-local-storage-for-kodi-and-dbmc/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix]
---

If you’re reading this post, you either want to use your DROIX® device like a NAS, or possibly want to ensure Kodi is able to write to the storage devices you have attached. If so, scroll down for the details…

We have included relevant screenshots to illustrate the steps required. If you’re unsure how to proceed, please do drop us a line.

![Play Store Open](https://droix.net/wp-content/uploads/2016/11/1-Play-Store-Open-300x169.png)

First, you will need to sign into Google’s Play Store if you haven’t done so already. Please see <https://droix.net/first-run-of-googles-play-store> for more details if you’re not sure how to do this.

Once signed in, please check all the applications are up to date. Click the menu button in the top left of the screen, then on to the Your Apps & Games entry. If updates are available, allow them to be processed.  
![Play Store Search](https://droix.net/wp-content/uploads/2016/11/2-Play-Store-Search-300x169.png)

Now click on the search bar at the top and type in sambadroid

![Play Store SambaDroid Search Results](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/3-Play-Store-SambaDroid-Search-Results-300x169.png)Once the Play Store has searched, you should see the SambaDroid entry, please click it

![Play Store SambaDroid Entry](https://droix.net/wp-content/uploads/2016/11/4-Play-Store-SambaDroid-Entry-300x169.png)

![Play Store SambaDroid Accept](https://droix.net/wp-content/uploads/2016/11/5-Play-Store-SambaDroid-Accept-300x169.png)

![Play Store SambaDroid Installing](https://droix.net/wp-content/uploads/2016/11/6-Play-Store-SambaDroid-Installing-300x169.png)Now select the Install button and wait for the application to download and be installed

![Play Store SambaDroid Installed](https://droix.net/wp-content/uploads/2016/11/7-Play-Store-SambaDroid-Installed-300x169.png)

Click the Open button

![SambaDroid SuperSU Request](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/8-SambaDroid-SuperSU-Request-300x169.png)When asked, click the Grant button

![SambaDroid First Run](https://droix.net/wp-content/uploads/2016/11/9-SambaDroid-First-Run-300x169.png)Take note of the first run help shown

![SambaDroid Initializing](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/10-SambaDroid-Initializing-300x169.png)

![SambaDroid Click Stop](https://droix.net/wp-content/uploads/2016/11/11-SambaDroid-Click-Stop-300x169.png)Click the Stop button

![SambaDroid Click Manage Shares](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/12-SambaDroid-Manage-Shares-300x169.png)Now head to Manage Shares, as we will need to reconfigure it slightly

![SambaDroid Click Click Share](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/13-SambaDroid-Click-Share-300x169.png)Click the entry at the top

![SambaDroid Click Default Share](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/14-SambaDroid-Default-Share-300x169.png)You can leave the Name as sdcard if you like, though in this example we will rename it to AllStorage

![SambaDroid Click Edit Share Name](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/15-SambaDroid-Edit-Share-Name-300x169.png)

![SambaDroid Click Path Dots](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/16-SambaDroid-Click-Path-Dots-300x169.png)Click the icon of 3 dots on the Path line

![SambaDroid Folder Selection Scroll Down Click Storage](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/17-SambaDroid-Folder-Selection-Scroll-Down-Click-Storage-300x169.png)You will be presented with a screen showing folders in the root of your device, scroll down and select the /storage/ folder

![SambaDroid Click Select Button](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/18-SambaDroid-Click-Select-Button-300x169.png)Click the “Select” button with a tick at the top of your screen

![SambaDroid Confirmation Of Changes Click OK](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/19-SambaDroid-Confirmation-Of-Changes-Click-OK-300x169.png)Assuming the changes are still shown, click the OK button

![SambaDroid Return Back One Screen](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/20-SambaDroid-Return-Back-One-Screen-300x169.png)Return one screen back, either with the Return button on your remote, or the logo and arrow shown top left

![SambaDroid Check Shows As Running OK](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/21-SambaDroid-Check-Shows-As-Running-OK-300x169.png)The service should restart itself, if it hasn’t click the Start button

The following is just for people wanting to use Sambadroid without other devices on their network. If you’re using this application to share files to other devices, please click [here](#not-kodi) to skip the section below.

![Open Kodi or DBMC To Test SambaDroid](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/22-Open-Kodi-or-DBMC-To-Test-SambaDroid-300x169.png)Next, open up Kodi or DroidBOX Media Centre (whichever you normally use) to test the system works

![Kodi DBMC Add Source](https://droix.net/wp-content/uploads/2016/11/23-Kodi-DBMC-Add-Source-300x169.png)The exact screen will depend on what you are using the storage device for, however you will normally have a Browse button to click

![Kodi DBMC SMB Samba Windows Network](https://droix.net/wp-content/uploads/2016/11/24-Kodi-DBMC-SMB-300x169.png)Select the Windows network (SMB) entry if present, or the Add Network Location entry

![Select Correct Domain](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/25-Select-Correct-Domain-300x169.png)Select the correct Workgroup name (this will depend on your OS/network configuration)

![Select Device SambaDroid](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/26-Select-SambaDroid-300x169.png)Unless you have already changed the network name given to your DroidBOX, you need to click SAMBADROID here

![Select The Desired Share](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/27-Select-Share-300x169.png)As with some other steps, the name you click here will depend on what you entered previously. Here we are going to select the AllStorage entry

![Select Exact Location And Did It Work](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/28-Select-Exact-Location-And-Did-It-Work-300x169.png)From here, navigate to the exact device and folder you want to have Kodi or DBMC use. Once set, make sure you’re able to read/write to the location

.

![SambaDroid Click Top Left](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/29-SambaDroid-Click-Top-Left-300x169.png)If the system is working, return to the SambaDroid application, and click the top left corner to have the menu slide in

![SambaDroid Click Options](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/30-SambaDroid-Click-Options-300x169.png)Click the Options entry

![Cancel Advert for SambaDroid Pro](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/31-Cancel-Advert-for-SambaDroid-Pro-300x169.png)Consider purchasing the application (the “Pro” version) if you want to support the application’s author, or would benefit from the extra features found in his premium version

![SambaDroid Default Options](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/32-SambaDroid-Default-Options-300x169.png)Here you can see the options in their default state

![SambaDroid Turn On Autostart](https://droix.net/wp-content/uploads/2016/11/33-SambaDroid-Turn-On-Autostart-300x169.png)Tick the “Boot autostart” entry

![SambaDroid Other Options](https://droix.net/knowledge-base/wp-content/uploads/sites/3/2021/11/34-SambaDroid-Other-Options-300x169.png)You will also find other entries in this list that may be of interest (to change your DROIX network name from SambaDroid for example)

A final test is to now reboot your device (don’t forget to make sure [Kodi or DBMC has been properly closed down](https://droix.net/closing-down-gracefully) first), then re-check that Kodi or DBMC and SambaDroid are still playing nicely together.
