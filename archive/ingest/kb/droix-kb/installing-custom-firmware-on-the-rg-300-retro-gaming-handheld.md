---
title: Installing custom firmware on the RG-300 retro gaming handheld
source_url: "https://droix.net/knowledge-base/article/installing-custom-firmware-on-the-rg-300-retro-gaming-handheld/"
source_site: droix.net
type: kb-article
date: 2021-11-20
wp_id: 453
---

You can buy the RG-300 from **<https://droidbox.co.uk/rg300-retro-console-droix-handheld-gaming-console-portable-retro-gaming.html>**

### **You will need**

MiniTool Partition Wizard Free Edition from **<https://www.minitool.com/download-center/>**  
Win32 DiskImager program from **<https://sourceforge.net/projects/win32diskimager/>** or Etcher from **<https://www.balena.io/etcher/>**

### **Custom Firmware File**

You will first need to identify which model of RG300 you have. The screen is different manufacturer between the two and requires a different firmware. If you use the wrong firmware you will get a blank screen when switched on.

NOTE: V1 may be referred to as the Gameboy model and the V2 as the SNES model due to the colour of the case.

The latest versions of both firmware can be found on the forums at **<https://www.droidboxforums.com/forums/rg-300-retro-gaming-handheld.163/>**

### **Removing the Micro SD Card**

On the back of the RG-300, remove the battery cover.

You can now remove the battery to reveal the Micro SD Card.

You can now gently remove the Micro SD Card from the slot. There may be a sticker covering the SD Card, carefully remove the sticker.

### **Preparing The Micro SD Card**

Insert your Micro SD Card into your PC and load Mini Tool Partition Wizard.

Identify and double check that you can see the Micro SD Card and then select it by clicking on the text for the card to select all of the card.

Right Click on the same area and choose **Delete All Partitions**

Right Click on the **Unallocated Space** area and choose **Create** from the menu.

Select the drop down menu for **File System** and choose **FAT32**, then click on **OK**.

Click on **Apply** to begin deleting the partitions and format the Micro SD Card.

Once it has completed you are ready to write the custom firmware.

### **Writing the Custom Firmware**

Insert the Micro SD Card into your PC’s card reader if you have not already.

Extract the custom firmware archive file. You should have a file with the filename extension of .img. For example *RG-300\_RG-PlusV2\_RS97-V3.0-CFW-Comic-book.03-07-19.img*

Load the Win32 DiskImager program and choose the first drive (Device) for your SD Card reader.

Click on the small blue folder icon and select the .img file that you have extracted

Double and triple check that you have selected the correct drive for the Micro SD Card and that you have prepared and chosen the correct image file. Once checked, press **Write** to begin writing the image file.

The process should take around 15 minutes depending on the speed of the Micro SD card and your PC.

Once completed, you can click on **Exit** to close the program.

### Expanding the available drive space for games

Load the Mini Tool Partition Wizard software. You will now see that there five partitions on the MicroSD Card.

**Note:** If the partition named **‘main’** does not have a drive letter, Right click on it and choose Change Letter and then assign it one.

We now want to expand the partition named ‘**main**’ to use the remaining available space. Right click on the ‘main’ partition and choose **Extend**

Drag the slider all the way to the right to fully allocate all the space to the ‘main’ partition. Click on **OK**.

Click on Apply in the top left to start allocating the free space to the ‘**main**’ partition. This may take some time depending on the size of your MicroSD Card

Once complete, you can now exit the Mini Tool Partition Wizard software.

### **Adding your own games**

You can use either the internal or external Micro SD card to add your own games. We recommend using an external Micro SD card as it is quicker and easier to update if you wish to add or delete games in the future.

**Internal SD Card Only**

If you are using the internal Micro SD card you will need to copy the files to a specific location. First insert the card into your PC. You may get some notifications that new drives are not formatted, select **Cancel** for all of them.

Choose the last USB Device on your list, it may have a **retrofw** icon. You should see the contents of it similar to below. You can copy any files to the **roms** folder.

If you can not see this drive, load Mini Tool Partition Wizard, Right Click on the **RETROFW** area and choose **Change Letter** from the menu.

You can choose any available drive letter from the drop down menu. Click on **OK** once chosen.

Click on **Apply**.

**External Micro SD Card Only**

If you have not already, format your Micro SD card to **FAT32**. Insert the Micro SD Card into your PC. In Explorer, right click on the Micro SD Card drive and choose **Format**.

To access the External Micro SD card in the file browser, press X several times until you are the system root and then choose **media** and then **mmcblk1p:1** to access the files on your SD card. You can update emulator short cuts by pressing Select and update to start in a different folder.

### **Copying files**

We recommend keeping an organised folder structure if you are planning to add many games. By making folders for each system it allows for easier finding of games and also faster loading times. Make a folder for each of the systems you plan to add games for.

If you have a large number of games for a system, you can organise it further into sub-folders such as A-F, G-L, M-S, T-Z. This makes it faster to load the list of games, and also saves time for you scrolling to get to a game beginning with R for example.

### **Finishing up**

Once you are done copying over your files, you can insert the Micro SD Card into either the internal or external Micro SD Card slot.

Reinsert the battery into the battery compartment and then put the battery compartment lid back into place.

Switch on your RG-300  and after a few moments it should boot to the custom firmware.