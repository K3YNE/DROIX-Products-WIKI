---
title: "How to Benchmark Your Windows Device"
type: source
subtype: kb-article
slug: benchmark-windows-device
brand: droix
product: null
source_url: "https://droix.net/knowledge-base/article/how-to-benchmark/"
published: 2023-07-13
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, droix]
---

Ensuring that our computers can withstand high-pressure situations is more important than ever. Stress testing and benchmarking your PC can help identify any weak spots or issues that you may be experiencing. So whether you’re a gamer pushing for optimal performance; a professional managing heavy-duty tasks; or just someone who wants to ensure their system is robust and dependable, understanding this process is the key.

In this comprehensive guide, we’ll cover what performance testing involves, the preparation process, the different tools available, including the ones we recommend, and how to perform these tests effectively. This guide is applicable for any Windows device including but not limited to; PCs, [Mini PCs](https://droix.net/product-category/mini-pcs/), Laptops and [Handheld PCs](https://droix.net/product-category/handhelds/handheld-gaming-pcs/).

## What is Benchmarking?

Stress testing is all about making sure your computer can handle tough situations. It’s essentially giving your PC a hard workout to see how well it copes when the workload gets busy or demanding. We do this by making the computer work extremely hard and putting it under a lot of stress – more than what we’d usually expect in everyday use. This is super important because it helps understand the strongest and most vulnerable parts of the system. This way, we figure out and prevent any potential problems that may occur in the future. It’s a smart move to ensure your computer stays reliable, especially for heavy-duty tasks or to understand the capability of your device.

We highly recommend running at least a general PC stress test whenever buying a new device, but for more in-depth results, you should test each component individually.

## Preparation

To guarantee accurate results from a performance test, you will need to minimise all other factors that may affect the accuracy and performance of the benchmark results. It’s crucial to establish a baseline with controlled variables, and the best way to do this is to ensure all of your firmware and drivers are up to date. We recommend you complete the following preparatory steps.

### Update BIOS Version

Your BIOS (Basic Input/Output System) or UEFI system is at the heart of your device. Verifying that your BIOS is up-to-date often fixes issues and improves performance, stability and compatibility. It’s important to note that you should only install stable BIOS updates, as an incorrect or unstable BIOS update can cause serious issues.

You can check our [Getting Started guides](https://droix.net/knowledge-base/tag/getting-started/) for your specific device to find the correct firmware updates.

### Update Windows

Next, ensure that your Operating System is updated to the latest version, as these updates often fix known bugs and issues that affect system stability related to outdated software. On Windows OS, this can be easily done in the **Windows Update** tab which can be found in **Settings**. Or you can check out our [How To guide](https://droix.net/knowledge-base/article/update-windows-and-drivers/).

### Update Drivers

You should also make sure you have the latest working versions of your device drivers. These drivers are specific to the individual hardware components (GPU, Chipset, network, sound card) and installing the latest revisions helps improve the stability, performance and communication of the specific component. The CPU and GPU have significant roles in system performance, making sure they are functioning correctly is critical for obtaining accurate results during stress testing.

You can check our [Getting Started guides](https://droix.net/knowledge-base/tag/getting-started/) for your specific device to find these driver updates.

### Scan for Malware

To be extra careful, we recommend running a full scan using a trusted antivirus tool like [Microsoft Defender](https://www.microsoft.com/en-gb/microsoft-365/microsoft-defender-for-individuals) or [Bitdefender](https://www.bitdefender.co.uk/) to detect any potential malware. It’s important to know that your system is clean and isn’t being compromised by any malware strains to avoid misinterpretation of any benchmarking data – a clean system establishes a baseline for performance level, as the system may underperform due to malware as opposed to hardware limitations.

### Restart Your Device

Restarting your PC terminates background processes and clears the memory and temporary files that have accumulated during use. It will also finalise any Firmware or Software updates, which are often required to complete the installation process. This again ensures a clear and consistent starting point as all memory is available for use during the tests and also any updates have been completed.

Close all unnecessary software before running to ensure the tests are accurate and consistent.

## General Tests

[PCMark](https://benchmarks.ul.com/pcmark10) is the industry standard for benchmarking the complete PC performance. We recommend this benchmark as it tests what real people would be using their devices for in day-to-day life – such as working with large office documents, media playback, image and video rendering and much more. Similar to its graphics rendering counterpart, 3DMark, this benchmark software not only breaks down your test results but also compares them to similar spec devices and hardware to ensure you have a deep but easy understanding of your device’s performance.

PCMark

[PassMark](https://www.passmark.com/) is a great alternative if you want to stress out your CPU, GPU, RAM and Storage in one go. Their benchmarks can be run as a whole, or individually if you want to stress something specifically.

PassMark

## CPU & GPU Tests

[3DMark](https://benchmarks.ul.com/3dmark) has a long history, being one of the most popular benchmarks for stress testing CPU and GPU for gaming. It’s considered the industry standard for graphics performance measurement. A free version is available for everyone and a paid upgrade features many additional benchmarks to run. Similar to its productivity counterpart, PCMark, you will get kind depth but easy-to-understand benchmark scores and comparison scores to ensure your device is working as intended.

3DMark

## CPU Only Tests

[Cinebench](https://www.maxon.net/en/cinebench) is highly recommended for CPU benchmark testing that uses Cinema4D’s rendering engine. It’s quick and simple to set up with little to no configuration – simply choose between running either or both, the single and multi-core tests, each taking around ten minutes.

Cinebench CPU benchmark

Another great alternative is [Prime95](https://www.mersenne.org/download/) which we use when experimenting with different settings.

## GPU Only Tests

[FurMark](https://geeks3d.com/furmark/) is an excellent choice for GPU stress testing and benchmarking on Windows devices. It’s a free and lightweight software that conducts intensive and stressful graphics card tests. This is simply the one we recommend. but there are plenty of alternatives available if needed.

FurMark GPU benchmark

## Memory **Only Te**s**ts**

The original benchmark for memory diagnostics is [MemTest86](https://www.memtest86.com/) and is still the best for testing your RAM. It does require you to make a USB boot drive and run the software from there. But it is worthwhile if you want to test your RAM accurately.

Memtest86

## Storage Only Tests

[CrystalDiskMark](https://crystalmark.info/en/software/crystaldiskmark/) is a free-to-use and extremely simple software to use for testing the performance of your SSD. This software benchmarks across multiple different tests to provide the read and write speed of your storage device.

CrystalDiskMark

---

These benchmarks and checks are meant to ensure your device works as intended and help detect any potential issues early on. If you encounter any problems or have any questions, reach out to [DROIX support](https://droix.net/contact-us/) or our [Discord community](https://go.droix.co.uk/discord) for help.
