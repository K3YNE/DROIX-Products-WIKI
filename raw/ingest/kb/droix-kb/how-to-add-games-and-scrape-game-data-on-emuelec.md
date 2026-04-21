---
title: How to add games and scrape game data on EMUELEC
source_url: "https://droix.net/knowledge-base/article/how-to-add-games-and-scrape-game-data-on-emuelec/"
source_site: droix.net
type: kb-article
date: 2022-09-01
wp_id: 2184
---

EMUELEC is a popular choice for many retro [handheld game consoles](https://droix.net/product-category/handhelds/handheld-game-consoles/) such as those made by [Anbernic](https://droix.net/brand/anbernic/). While it is very easy to add new games to your micro SD card (which we explain below), adding box art, game info etc. aka “game scraping” can be harder if you are not familiar with the process.

## How to add games to EMUELEC?

Your micro SD card used for game storage on the handheld can be removed and read on your PC without any additional steps. Switch off your handheld and remove the micro SD card and insert it into your PC card reader.

Open File Explorer and you should see your micro SD card with a number of folders with familiar console names. There may be some differences in names or missing ones depending on what your handheld supports.

Micro SD Card folders

You can now copy your game ROMs from your PC to the micro SD cards respective folder. For example Genesis / Mega Drive games goes into the “megadrive” folder. PC Engine games go into the “pcengine” folder and so on.

Copy over all your files and once completed you can eject the card from your PC, re-insert it back into your handheld and switch it back on.

Depending on how many games you have added, you may notice that it is taking a little longer to boot to the menu. It is scanning for and adding any new games it finds on the micro SD card. Let it finish scanning.

If you browse through the systems you will notice that new game system menus are now shown if there were previously no games for it.

New Game System

When you choose that system, it will show the newly added games, but no box art or game information.

No game box art or description

We now need to scrape the game data.

## How to scrape game data on EMUELEC?

### Check that you are connected to the internet

First, check that you are connected to the internet. From the **Settings** menu, choose **Network Settings** and confirm the internet status is showing as **Connected**. If it is not, **enable the WiFi** and choose your **WiFi SSID** (access point) and enter your password.

Check you are connected to the internet

### Scraping Setup

Return to the main **Settings** menu, and choose **Scrape**

Choose Scrape

There are two sources to scrape from which you can change between by pressing Left or Right on the **Scrape From** menu entry; ScreenScraper and TheGamesDB. ScreenScraper has more options for what content you want to download, and TheGamesDB is more simplified. Either one can be used, but be aware that both are free to use, they can be busy at some times or not working at all.

Screenscraper

For the moment, leave the scraping settings as they are and scroll down to **Scrape Now** and choose that. A new menu will show with some settings for what to scrape. We recommend leaving it on these default settings.

Scrape Now Menu

### Game scraping

Choose **START** to return back and **Scrape Now** again to start scraping. A popup will show onscreen to show the progress of the game scraping.

Scraping in progress

This can take some time depending on how busy the service is and how many games are being scraped. Leave the handheld on charge and check back every so often. Once the scraping has completed you will be notified.

Scraping Finished

## How to update the Game Lists on EMUELEC

Now you need to update the game database to include the scraped data. From the **Settings** menu, choose **Games Settings**

Games Settings

Then choose **Update Games Lists** from the menu

Update Games Lists

The game database will now be updated with the newly scraped data including box art and description. Again, this may take some time depending on how many games need to be updated.

Updating Games Lists

When this has completed you can now browse a game system and the box art and description will now be shown.

Box art and Description now showing!

## Box art or Description still not showing?

There may be some games that are still missing box art and/or description. This may be due to the game name not being recognised or there is currently no image or text for the game.

Another reason is if you change theme and by default it uses a different image category just as screenshot instead of box art. You will need to either change the category in the theme to box art for example, or re-scrape your collection in the **Scrape Setting**s to “screenshot”.