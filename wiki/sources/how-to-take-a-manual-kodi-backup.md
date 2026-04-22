---
title: "How to take a manual Kodi Backup"
type: source
subtype: kb-article
slug: how-to-take-a-manual-kodi-backup
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/how-to-take-a-manual-kodi-backup/"
published: 2021-11-20
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix]
---

There are applications and program add-ons to do this job automatically, but if you want to carry this out manually, perhaps prune the add-ons you don’t use etc, please do the following:  
  
Open the ES File Explorer application on your device and expand the LOCAL menu. Click on the Home link. Expand the TOOLS menu below that now and turn on Show Hidden Files. Now click on the Home/ shortcut under the LOCAL menu and navigate to (click on each folder name listed:)

* Android/Data/org.xbmc.kodi/files/.kodi/userdata and the addon\_data folder
* Android/Data/com.semperpax.spmc/files/.spmc/userdata (and the addon\_data folder) for SPMC/older DBMC installations
* Android/Data/uk.droidbox.dbmc/files/.dbmc/userdata (and the addon\_data folder) for more recent DBMC installations

Copy and paste these two directories to a new location, if you use a USB device or memory card, the backup will remain in place even if you need to factory reset in the future.

To double check it works, you could install Kodi on a phone/tablet/PC/Mac , NOT configure it, close Kodi down. Then “restore” (copy and paste back place) the backup you made above to your non-DROIX device, and see if the set up is transferred OK. If it does, you should be reasonably confident that your backup is functioning and will work on your DROIX (without having to actually wipe your DROIX’s Kodi install first!).