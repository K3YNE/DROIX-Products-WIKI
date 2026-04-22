---
title: "How to fix battery icon disappearing on the GPD WIN MAX 2 2025"
type: source
subtype: kb-article
slug: gpd-win-max-2-2025-battery-icon-fix
brand: gpd
product: gpd-win-max-2
source_url: "https://gpdstore.net/kb/gpd-win-max-2-support-hub/kb-article/how-to-fix-battery-icon-disappearing-on-the-gpd-win-max-2-2025/"
published: 2025-10-10
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, gpd, gpd-win-max-2, troubleshooting]
---

A problem has been discovered affecting the [GPD WIN MAX 2 2025](https://gpdstore.net/product/gpd-win-max-2-2025/ "GPD WIN MAX 2 2025 ") HX 370 series of devices. It has been observed that after updating the AMD graphics driver software, it can sometimes cause the battery status indicator to vanish from view.

In the past, several alternative solutions have been suggested; however, their effectiveness has been inconsistent, resolving the issue for some individuals but not for all. The solution detailed below has been successfully verified across multiple devices. We would like to acknowledge user expormz on [Reddit](https://www.reddit.com/r/gpdwin/comments/1o2np9v/max2_hx370_solution_to_the_disappearance_of_the/ " Reddit") for providing this information.

Take the text that follows and place it in a new file that you name `scan-devices.xml`. As an alternative, you can use the provided link [here](https://gofile.me/7AWvf/zOKo8hCWZ "here") to download and unzip the file.

```
<?xml version="1.0" encoding="UTF-16"?>
 <Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
   <RegistrationInfo>
     <Date>2025-10-09T23:43:33.4221277</Date>
     <Author>GPDWINMAX2\expormz</Author>
     <URI>\scan-devices</URI>
   </RegistrationInfo>
   <Triggers>
     <BootTrigger>
       <Enabled>true</Enabled>
     </BootTrigger>
   </Triggers>
   <Principals>
     <Principal id="Author">
       <UserId>S-1-5-21-329286994-4123067376-2057571490-1001</UserId>
       <LogonType>S4U</LogonType>
       <RunLevel>HighestAvailable</RunLevel>
     </Principal>
   </Principals>
   <Settings>
     <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
     <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
     <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
     <AllowHardTerminate>true</AllowHardTerminate>
     <StartWhenAvailable>false</StartWhenAvailable>
     <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
     <IdleSettings>
       <StopOnIdleEnd>true</StopOnIdleEnd>
       <RestartOnIdle>false</RestartOnIdle>
     </IdleSettings>
     <AllowStartOnDemand>true</AllowStartOnDemand>
     <Enabled>true</Enabled>
     <Hidden>false</Hidden>
     <RunOnlyIfIdle>false</RunOnlyIfIdle>
     <WakeToRun>true</WakeToRun>
     <ExecutionTimeLimit>PT72H</ExecutionTimeLimit>
     <Priority>7</Priority>
   </Settings>
   <Actions Context="Author">
     <Exec>
       <Command>C:\Windows\System32\pnputil.exe</Command>
       <Arguments>/scan-devices</Arguments>
     </Exec>
   </Actions>
 </Task>
```

Perform a **right-click** on the **Windows Start** menu icon and from the context menu that appears, choose **Computer Management**.

Select Computer Management

Inside the **Computer Management** window, navigate to and click on **Task Scheduler**. Afterward, find and select the **Import Task** option located in the right-hand pane.

Task Scheduler

Browse to the location of the `scan-devices.xml` file you created or downloaded, select it, and then confirm by clicking **OK**.

Open scan-devices xml file

In the provided text box labelled **Enter the object name to select**, type in the name of your Windows user account, then click the **Check Names**‘button to validate it.

Input your Windows account name

After your Windows account name has been successfully verified, you may proceed by clicking the **OK** button.

Input your account name checked

When the **Create Task** dialog box appears, you must ensure that the options for **Run whether user is logged on or not** and **Run with the highest privileges** are both ticked, as illustrated in the image. With these settings confirmed, press **OK** to continue.

Create task

Returning to the main **Task Scheduler** interface, you are now able to exit the program. Restart your [GPD WIN MAX 2 2025](https://gpdstore.net/product/gpd-win-max-2-2025/ "GPD WIN MAX 2 2025 ") device, and upon rebooting, the battery indicator should be restored.

Task Scheduler Summary Confirmed

Important considerations: This solution is specific to the user profile you selected during the setup. For any other Windows accounts on the device, you will need to perform these steps again.

Should you encounter any difficulties after attempting this procedure, we kindly ask you to reach out to our support team by emailing support@droix.net. Please include your original order number along with a description of the problem, and we will be glad to assist you.
