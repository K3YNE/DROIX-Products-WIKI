---
title: How to install Ubuntu Linux 24.10 on the GPD Pocket 3
source_url: "https://gpdstore.net/kb/gpd-pocket-3-support-hub/kb-article/how-to-install-ubuntu-linux-24-10-on-the-gpd-pocket-3/"
source_site: gpdstore.net
type: kb-article
date: 2024-10-14
wp_id: 3936
---

### Installation

Refer to the official [Ubuntu installation tutorial](https://ubuntu.com/tutorials/install-ubuntu-desktop) for general guidance on the installation process.

1. Download the installer named `ubuntu-24.10-desktop-amd64.iso` from the [Ubuntu 24.10 download page](https://releases.ubuntu.com/oracular/) and write it to a USB disk.
2. Proceed with the installation as usual, then reboot when it’s complete.

### Post-installation

#### Screen Scale

1. Right-click on the desktop wallpaper and select **Display settings**.
2. Enable **Fractional scaling**.
3. Adjust the window if needed.
4. Set the scale to **150%**.
5. Click **Apply** and confirm by selecting **Keep Changes**.
6. Close the **Display settings**.
   * Alternatively, you can adjust the font size using **gnome-tweaks**.

#### Unpin Apps from the Sidebar

1. Right-click on any unwanted apps in the sidebar and select **Unpin**.
2. Go to **Settings → Ubuntu Desktop → Icon size**, and set the size to **32**.

#### Display Orientation on Startup

To correct the screen orientation during startup and shutdown:

1. Open **Terminal** from the menu.
2. Paste the following command and press Enter:  
   `echo 'GRUB_CMDLINE_LINUX_DEFAULT="$GRUB_CMDLINE_LINUX_DEFAULT fbcon=rotate:1 video=DSI-1:panel_orientation=right_side_up"' | sudo tee /etc/default/grub.d/fbcon-rotate.cfg && sudo update-grub && echo Success`
3. Enter your password when prompted.
4. If the command executes successfully, you should see a **Success** message.
5. Reboot to apply the changes.

#### Screen Auto-rotation

1. Open **Terminal** and paste the following command, then press Enter  
   `sudo apt install --update gnome-shell-extension-manager && echo Success`
2. Enter your password when prompted and wait for the **Success** message.
3. Launch **Extension Manager** from the menu.
4. Click **Browse**, search for “rotate,” and install the **Screen rotate** extension.
5. Switch to the **Installed** page, and click the ⚙️ settings icon for the **Screen rotate** extension.
6. Set the orientation offset to **1**.
7. If the screen orientation is incorrect, reboot the device.
8. You can now toggle screen auto-rotation from the quick menu in the top-right corner. Test by rotating the device.

#### On-Screen Keyboard — Option 1

1. Open the ⚙️ settings of the **Screen rotate** extension again.
2. Check the box for **Show OSK in portrait orientation**.
   * Note: There is still a need to find a way to hide the accessibility icon.
   * In this configuration, the on-screen keyboard (OSK) will only be enabled in portrait mode. Swipe up from the bottom to show the keyboard, and use the hide button to dismiss it.

#### On-Screen Keyboard — Option 2 (Currently Broken)

This method is awaiting compatibility with Gnome 47.

1. Open **Extension Manager** from the menu.
2. Click **Browse**, search for “OSK,” and install the **TODO** extension.
3. You can now toggle the on-screen keyboard from the menu bar in the top-right corner.

### KVM Module

The KVM module functions as a standard webcam. **TODO**: Explore compatible apps.

### Fingerprint Reader

The fingerprint reader (FocalTech FTE3600) is not supported. For more details, see the related issue on [libfprint](https://gitlab.freedesktop.org/libfprint/wiki/-/issues/47).

### Further Reading

* [Ubuntu installation tutorial](https://ubuntu.com/tutorials/install-ubuntu-desktop)
* [GPD Pocket 3 – ArchWiki](https://wiki.archlinux.org/title/GPD_Pocket_3)

Information taken from <https://gist.github.com/epsimatic>