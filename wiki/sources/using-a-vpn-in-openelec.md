---
title: "Using A VPN In openELEC"
type: source
subtype: kb-article
slug: using-a-vpn-in-openelec
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/using-a-vpn-in-openelec/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix]
---

We’ve used an account with IPVanish – [https://www.ipvanish.com/](https://www.ipvanish.com/?a_aid=56793406edacd&a_bid=48f95966) – for this example.

If you follow the steps in this post and find you do not have an option to manually create a VPN connection, please instead follow the steps linked to in the paragraph below.

#### NO VPN CONNECTION CREATION OPTION?

If you follow this guide and find you do not have the option to add a new VPN connection, please refer to <https://seo-michael.co.uk/vpn-manager-for-openvpn-openelec-kodi/> for another approach involving a couple of add-ons you can use instead to create and control the connection. After the “Select VPN Manager for OpenVPN” step in that guide, open the add-on as normal, and select “Change or disconnect VPN connection” to trigger the Wizard.

#### VPN CONNECTION CREATION METHOD

Using the VPN connection creation process within OpenELEC’s Configuration program Add-on is the simplest route as it involves no further downloading.

The first step is to make sure your account is working OK on the DROIX using IPVanish’s official Android application. See <https://play.google.com/store/apps/details?id=com.ixolit.ipvanish&hl=en_GB> for a description of the app. Once configured and tested as OK in Android, next switch to the openELEC operating system (see <https://www.youtube.com/watch?v=BTjGdT0VKMU> for details).

From the Program Add-ons (or under the System menu in the Confluence skin) start OpenELEC (Configuration)

Kodi System OpenELEC

[Program Add-ons> Also Has openELEC’s Configuration” width=”300″ height=”169″>](https://droix.net/wp-content/uploads/2016/02/20160210_172844_0.png) Kodi>Program Add-ons> Also Has openELEC’s Configuration

In the Network area, click on Add new VPN configuration

For now we are using PPTP, if we have more success with openVPN we will update this guide.

VPN Type: pptp

[Virtual Private Networks > Add new VPN configuration” width=”300″ height=”169″>](https://droix.net/wp-content/uploads/2016/02/20160210_170023_0.png) Network > Virtual Private Networks > Add new VPN configuration

VPN Connection Creation

VPN Type

Network name: Whatever you like, the company name and location of server can help with multiple connections  
VPN Server: Here you would put XXXXXX.ipvanish.com (I tried an Atlanta server that started “atl”)

Username: Your IPVanish username

Passphrase: Your IPVanish password

VPN DNS Domain: leave at the default value of  vpn  , don’t touch this

Select Network Name

Something Descriptive You’ll Remember Easily

Click the VPN Server entry to enter address

Click Username and Passphrase

Make sure capital letters, numbers etc are typed in carefully

Again, CASE MaTtErs

Show Advanced: Yes (click this)

Refuse Chap  
Require MPPE  
Refuse PAP  
Refuse EAP

The other settings I left at default.

Click Show Advanced if you want this to work

Copy these settings or check the text below

Continuation of settings to be copied

Then click the Save button.

From here, go to the Connections list and click on the new VPN entry you created and named. Select Connect.

openELEC Connections Area

openELEC Connections Area Click And Connect

If you want to double check if the system is working (assuming the State: changes to ready) you can open the Wookie Wizard (as one example, other tests can be found online) from Kodi’s homescreen to Video Add-ons. Next select the Tools entry (you’ll need to remove (Kodi’s Homescreen>System>Add-ons>My Add-ons>Video Add-ons>Wookie>Uninstall) and reinstall it if you still have the older interface, see <https://www.youtube.com/watch?v=6bQZyKiayYA> ).

Leave it a few seconds, and the IP address and related country will be shown. To disconnect from the VPN return to Program Add-ons>OpenELEC Configuration>Network . Click the VPN connection in use and disconnect. If you now re-run the test, your home’s IP address and actual location will show.