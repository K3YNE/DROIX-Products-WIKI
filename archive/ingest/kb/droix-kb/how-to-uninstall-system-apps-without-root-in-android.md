---
title: How to Uninstall System Apps Without Root in Android
source_url: "https://droix.net/knowledge-base/article/uninstall-android-system-apps/"
source_site: droix.net
type: kb-article
date: 2021-11-20
wp_id: 1077
---

When you buy a new [Android](https://www.android.com/) device, whether it’s a [handheld](https://droix.net/product-category/handhelds/retro-gaming-handheld/) or smartphone, chances are it comes with plenty of preinstalled bloatware. While you can uninstall those third-party bloatware apps, some of the apps are installed as system apps and cannot be removed. This is especially true for the whole suite of Google apps. If you are not a fan of Google Play Music or Google Duo, sorry, you can’t remove them from your device. To get rid of system apps, you have to root your phone. The bad thing is, that it is not easy to root your device, and you will void your warranty by doing so. In addition, rooting your phone also prevents you from using certain apps like Internet Banking and Google Pay.

Here are a few ways to remove bloatware/system apps without root in [Android](https://droix.net/product-attribute/operating-system/android-13/).

## Uninstall/Disable the bloatware

For the third-party bloatware, most of them can be easily uninstalled.

1. On your Android phone, go to “Settings -> Manage Applications.”

2. Find the app that you want to remove and tap on it.

3. If there is an “Uninstall” button, tap it to begin.

4. If you see a “Disable” button instead of an Uninstall button, this means that the apps cannot be uninstalled but can be disabled.

“Disabled” means that the app becomes dormant, won’t show up in your application list and won’t be recognized as an installed app.

Tap on the Disable button to disable the app.

1. Open “Hidden Settings for MIUI.”

2. Go to “Manage applications” and find the application you want to disable.

3. Tap on the “Disable” button.

## Uninstall system apps using adb

Adb is a powerful tool for you to debug your phone. It also comes with commands for you to manage app packages (in this case, uninstall packages).

1. To use adb, you need to install adb on your desktop computer.

For Linux, you can just install “android-tools” from your Software Center or package manager.

For Windows, follow [the instructions here](https://www.maketecheasier.com/get-started-with-android-debug-bridge-adb/) to install adb.

2. Next, you need to enable “[Developer Options](https://www.maketecheasier.com/how-to-enable-developer-options-in-android/)” on your phone. Once enabled, go into the Developer Option, scroll down the list and enable “USB debugging.”

3. Connect your phone to the desktop via USB. When prompted, change the “charge only” mode to “file transfer (MTP)” mode.

4. In [Windows](https://www.microsoft.com/en-gb/windows/windows-11), navigate to the adb directory and launch the command prompt in that folder. For Linux, just open the Terminal.

Type the following command to start adb and verify that the phone is connected.

```
adb devices
```

If you see an entry listed under the “List of devices” section, then your device is connected.

5. Start the adb shell.

```
adb shell
```

6. List all the packages installed in the phone.

```
pm list packages
```

The list will be very long. You can use `grep` to narrow down the list. For example, to only show Google packages, use the command:

```
pm list package | grep 'google'
```

7. Find the name of the app you want to uninstall. The name is the entry after `Package:`. For example, the package name for the Google Contact app is `com.google.android.contacts`.

If you have trouble identifying the package name, simply go to Google Play Store on your browser and search for the app. Check the URL for the package name.

8. Type the following command to uninstall the app.

```
pm uninstall -k --user 0 package-name
```

You should see the word “Success” if the uninstallation is successful.

The `--user` flag in the above command is important because it tells the system to uninstall the app for the current user only (and `0` is the default/main user of the phone). There is no way you can uninstall the app from all users unless you root the phone.

As a word of warning, uninstalling system apps have the potential to break the system, so only uninstall the apps that you are sure of. Apps like Gmail, Google Play Music, Google Play Movies, etc., are safe to uninstall but don’t ever remove the Google Play Store or any of the files associated with it. If the phone becomes unstable after you uninstall a particular app, either reinstall back from the Google Play Store or factory reset your phone.

## Conclusion

Depending on your phone manufacturer, some phones come with only a few bloatware, and the system apps can be disabled easily while others are full of third-party apps that you cannot remove or disable at all. The instructions above will allow you to get rid of those bloatware system apps from your [Android](https://www.android.com/) phone, without having to root your phone.