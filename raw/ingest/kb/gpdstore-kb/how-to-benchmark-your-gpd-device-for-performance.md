---
title: How to benchmark your GPD device for performance
source_url: "https://gpdstore.net/kb/software-guides/kb-article/how-to-benchmark-your-gpd-device-for-performance/"
source_site: gpdstore.net
type: kb-article
date: 2025-05-16
wp_id: 1087379
---

You might want to assess the performance of your [GPD handheld PC for gaming](https://gpdstore.net/product-category/gpd-handheld-gaming-pcs/) or [mini laptop](https://gpdstore.net/product-category/gpd-mini-laptop/) for various reasons. Perhaps you’re fine-tuning its settings to achieve optimal performance, or you suspect a problem, such as the device overheating, which could be causing the CPU to reduce its speed.

This guide will show you a straightforward and repeatable method for benchmarking your device. The resulting data will help you pinpoint instances of better or worse performance in different assessments.

## Default Benchmark Settings

If you have been asked to perform a benchmark test by the GPDSTORE customer service, the settings used must match our own settings. We can then accurately compare the results to identify if there is a problem with the software setup or an actual hardware issue.

Please reset the Motion Assist settings to their default values and set the TDP to 28W which is the optimal TDP for performance vs power usage. Please see the [guide here](https://droix.net/knowledge-base/article/changing-the-tdp-or-performance-profile-on-your-windows-android-handheld/) on how to change the TDP as well as the other default settings on Motion Assist.

## Download & Install 3DMARK

To begin, download and install 3DMark. The demo version for Windows can be obtained directly from [Steam](https://store.steampowered.com/app/223850/3DMark/). For the purposes of these tests, the complimentary versions are adequate, and purchasing the full version is unnecessary. Alternatively you can download from the [official website](https://benchmarks.ul.com/3dmark#windows).

Once you have installed 3DMark, open the application. If you receive a notification to update the software, please proceed with the update. Depending on the source from which you downloaded the software, you might need to perform this update process one or more times.

## One Time Benchmark

Click on the **Benchmarks** icon at the top.

3DMARK Home Page

Scroll down the list and locate the **Time Spy** (not Time Spy Extreme) benchmark and click on that.

3DMARK Benchmarks Page

Confirm that you are using the correct GPU for the test. This would normally be the internal GPU found inside the handheld unless you are testing external GPU cards performance. Click on the **Run** icon to begin the benchmark. The process will take around 10-15 minutes.

3DMARK Time Spy Page

After the benchmark finishes, a screen displaying the results will appear. It’s important to record the Time Spy Score, along with the Graphics score and CPU score, which are shown to its right. As an alternative, you can capture this information by taking a photograph with your phone or by taking a screenshot (using the Print Screen key) to save a copy.

3DMARK Time Spy Benchmarks result

You can then make any changes such as changes to the TDP and click the **Run Again** icon to repeat the benchmark test.

## Stress Test

From the Home screen, click on the **Stress Test** icon at the top.

3DMARK Home Page Stress Test

Before proceeding, ensure that the “**Steel Nomad Light Stress Test**” option is chosen. Double-check that the appropriate GPU is selected for the assessment; this will usually be the integrated GPU within your handheld device, unless you are specifically evaluating the performance of an external graphics card. To initiate the stress test, click on the “**Run Stress Test**” icon. This testing procedure typically lasts for approximately 20 minutes.

3DMARK Windows Stress Test Page

Upon completion of the stress test, a results screen will be displayed. Take note of the “Frame rate stability,” “Best loop score,” and “Worst loop score.” Alternatively, you can capture this information by taking a photograph with your mobile phone or by taking a screenshot (using the Print Screen key) to retain a copy.

3DMARK Windows Stress Test Results Page

You can then make any changes such as changes to the TDP and click the **Run Again** icon to repeat the stress test.

## Other Benchmarks

For those interested in evaluating the performance of a specific component of your Windows device, such as the speed of your SSD, please consult our guide titled [How to Benchmark Your GPD here](https://gpdstore.net/kb/software-guides/kb-article/how-to-benchmark-your-gpd/).