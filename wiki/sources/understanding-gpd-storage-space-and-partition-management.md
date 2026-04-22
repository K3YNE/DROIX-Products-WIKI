---
title: "Understanding GPD Storage Space and Partition Management"
type: source
subtype: kb-article
slug: understanding-gpd-storage-space-and-partition-management
brand: gpd
product: null
source_url: "https://droix.net/knowledge-base/article/gpd-storage-space-issue/"
published: 2024-05-16
created: 2026-04-22
updated: 2026-04-22
tags: [kb-article, gpd]
---

We’ve received several reports from customers experiencing missing SSD or storage issues on their new [GPD devices](https://droix.net/product-attribute/brands/gpd/). This article clarifies the situation and explains how GPD has configured these devices.

A 2TB GPD WIN Max 2 showing a capacity of 300GB

So what’s the issue? Many customers believe their devices are missing storage because they cannot see the full capacity of the SSD. However, the storage may not actually be missing. Instead, GPD has been pre-configuring the SSD into two [partitions](https://en.wikipedia.org/wiki/Disk_partitioning) as described and shown below:

1. A smaller partition, allocated to the C: drive, that contains the Windows Operating System (OS).
2. Partition 2: This partition contains the remaining storage.

File Explorer



Disk Manager

## How to Check

If you believe your device is missing storage, you can verify the partitions and access the full storage capacity using two different methods.

### File Explorer

1. **Open File Explorer**
   * Press `Win + E` and select “This PC” from the File Explorer.
2. **View Drives**
   * In File Explorer, you should be able to see 2 (or more) Drives. The first is usually labelled as “Windows (C:)”, which is a smaller designated partition for the OS. The second partition should comprise the remaining storage.

Select “This PC”



Check Drives and total storage

Please note, there may be slight discrepancies due to differences in how storage capacity is calculated by manufacturers, operating systems, and depedning on SSD branding. Plus some space is aleady used for system files and formatting.

### Disk Management

1. **Open Disk Management:**
   * Press `Win + X` and select “Disk Management” from the menu.
2. **View Partitions:**
   * In Disk Management, you should see two partitions on your primary SSD. The first partition is usually labelled as “C:” and is smaller, designated for the OS. The second partition comprises the remaining storage.

Select “Disk Management”



Check total disk storage

Please note, there may be slight discrepancies due to differences in how storage capacity is calculated by manufacturers, operating systems, and depedning on SSD branding. Plus some space is aleady used for system files and formatting.

## Why the Preset Partitions?

On older devices, having dedicated partitions for OS and Data, allowed the system to run more efficiently and stably, which may still hold some merit on modern devices. But GPD has also implemented this partitioning to simplify System Maintenance — having a separate OS partition makes it easier to perform system updates, backups, and recoveries without affecting user data stored in the second partition. This means that you can reset or reinstall Windows without wiping the data on your second partition (as Windows has its own dedicated partition).