---
title: Manually Choosing Default Video Player
source_url: "https://droix.net/knowledge-base/article/manually-choosing-default-video-player/"
source_site: droix.net
type: kb-article
date: 2021-11-20
wp_id: 719
---

If you want to keep your current build of Kodi, but would like to experiment with using MX Player as the default video player within Kodi/DBMC/XBMC/SPMC then read on.

If these steps don’t work or you’d prefer a simpler approach, please grab the APK file linked to here – <https://droix.net/kodi-spmc-and-dbmc-downloads/> (it will mention MX Player in the description).

Download <https://droidbox.co.uk/playercorefactory.xml> , you can either right click the link and select a Save option, or open the link and then save the file. Keep the extension as XML and do not rename it please.

With a file browsing application, please navigate to the area you downloaded the XML file to and copy it. Next navigate to /Android/data/org.xbmc.kodi/files/.kodi/userdata/ (the org.xbmc.kodi folder may be named differently, but it should have Kodi, SPMC or XBMC in it still). Paste the file there (if you can’t find the path, expand ES File Explorer’s Tools menu on the left and turn on Shown Hidden Files.

Now when you next start Kodi, and select a video, you should find it automatically uses MX Player. If you want to use an Android media playing application other than VLC, you’ll need to amend the rule section at the end. Also, the entries above may become outdated if the filename reference is altered by the application’s author(s).