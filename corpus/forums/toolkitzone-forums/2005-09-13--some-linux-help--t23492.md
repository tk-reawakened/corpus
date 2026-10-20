---
kind: forum-thread
id: "toolkitzone-forums/23492"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Computing &amp; Technology"
skin: "phpbb2"
thread_id: "23492"
title: "Some Linux Help..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23492"
written: "2005-09-13T21:27:00"
last_post: "2005-09-14T22:48:00"
date_confidence: "exact"
captured: ["20051018074336", "20060109091423", "20060109092345", "20060109092556", "20060109104749", "20060109110908"]
author: "Marz"
repliers: ["bracken", "Colin", "Michael J. Hill"]
authors: ["Marz", "bracken", "Colin", "Michael J. Hill"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_256954_amp_3Bsid_c4c810a9c494ebedd3088202f0c6c267", captured: "20060109092556", sha256: "cbf875b84992e7995d804ecd8d9ad9ba54e5adf0456ad5aa1f569e243dfe49ae", wayback_url: "https://web.archive.org/web/20060109092556/http://www.toolkitzone.com/forums/viewtopic.php?p=256954&amp%3Bsid=c4c810a9c494ebedd3088202f0c6c267"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_257023_amp_3Bsid_c4c810a9c494ebedd3088202f0c6c267", captured: "20060109104749", sha256: "78b491b42c6f148f091d1d0d8d7ccd0ae131efe0a83b252fe1f845bec5afbd70", wayback_url: "https://web.archive.org/web/20060109104749/http://www.toolkitzone.com/forums/viewtopic.php?p=257023&amp%3Bsid=c4c810a9c494ebedd3088202f0c6c267"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_257041_amp_3Bsid_c4c810a9c494ebedd3088202f0c6c267", captured: "20060109092345", sha256: "ab15c4d89cc304de5806a5e8713f4be9252bd907a32b86e018dd19e4b5d73b9d", wayback_url: "https://web.archive.org/web/20060109092345/http://www.toolkitzone.com/forums/viewtopic.php?p=257041&amp%3Bsid=c4c810a9c494ebedd3088202f0c6c267"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_257118_amp_3Bsid_c4c810a9c494ebedd3088202f0c6c267", captured: "20060109110908", sha256: "5064b57214aa1daff30de9837e55329262499713d750917c9a8ca121db70aaca", wayback_url: "https://web.archive.org/web/20060109110908/http://www.toolkitzone.com/forums/viewtopic.php?p=257118&amp%3Bsid=c4c810a9c494ebedd3088202f0c6c267"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_257168_amp_3Bsid_cc194ea384cda74cd58b441534454b34", captured: "20051018074336", sha256: "d2bac972b5a17ac14312ea1650fca495b4d3a27576c93e2c940a8fc8c43fbe20", wayback_url: "https://web.archive.org/web/20051018074336/http://www.toolkitzone.com/forums/viewtopic.php?p=257168&amp%3Bsid=cc194ea384cda74cd58b441534454b34"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_257290_amp_3Bsid_c4c810a9c494ebedd3088202f0c6c267", captured: "20060109091423", sha256: "a81d36e05f5fefa82d1d8f191aa2919f69e0da94f3dd629ca1a97d8a2c3a7e3b", wayback_url: "https://web.archive.org/web/20060109091423/http://www.toolkitzone.com/forums/viewtopic.php?p=257290&amp%3Bsid=c4c810a9c494ebedd3088202f0c6c267"}
links: []
---

# Some Linux Help...

### Marz · 2005-09-13 21:27 · #B256954

Questions:
- How do I mount my Windows hard drive from linux (I'm using FC) so that I can copy files. I need to format and wipe the windows hard drive because it went all screwy, and I don't want to lose all my files.
- How do I upgrade to FC4? I can't seem to use yum correctly to do this, and I don't know where to wget from.
- Is it possible to play WoW on my linux machine yet?
Thanks Smile

### bracken · 2005-09-13 23:48 · #B257023

depending on what filesystem you have on windows your command can be a little different. This should do it though.

**Code:**

```
mount -t auto /dev/hdb1 /mnt/windows
```

the /dev/hdb1 should be whatever your windows partition is. You'll have to make a directory at your mount point. (in the code /mnt/windows) You also might need to replace 'auto' with 'ntfs' Hopefully you have the module to recognize ntfs. Note, you can't write to an ntfs file system, only read. If ntfs is listed when you type

**Code:**

```
cat /proc/filesystems
```

than the module is installed.
Upgrading? I don't know, I've never used fc. Google gave me a lot of tutorials when I searched for upgrading to fedora core 4.
WoW? There are a few windows emulators and other similar things out there. I don't know if WoW specifically works. There is one emulator that specializes in games, but I can't remember what it's called right now. You'll have to do some research on that one. ;)

### Colin · 2005-09-14 00:22 · #B257041

If you just want to update Fedora Code simply, you could just install FC4. Anaconda (the installer) has an upgrade option. I'm sure this isn't the most efficient, but it's definitely easy, and it lets you have a physical copy of FC4 too for next time you install.

### Michael J. Hill · 2005-09-14 03:25 · #B257118

The fact remains that Fedora Core should've automatically mounted your windows partition to begin with.
Upgrading - I don't use Fedora Core, so, i can't help there.
As far as playing WoW in Linux, the best software I can think of that'd run it is TransGaming's Cedega. This isn't free software, but for $15, it's worth it, it'll play many Windows games, and is actually designed just to play the games. Also, paying that $15 gives you free access to a year's worth of updates.

### bracken · 2005-09-14 15:12 · #B257168

Cedega! That's the one I was thinking of. ;) I just couldn't remember what it was called. As big a fan of Linux as I am, I must say a lot of the aps have weird names. ;)

### Colin · 2005-09-14 22:09 · #B257290

**Michael J. Hill wrote:**

> The fact remains that Fedora Core should've automatically mounted your windows partition to begin with.
>

Anaconda gives the option, but it's not done by default.

### Michael J. Hill · 2005-09-14 22:48 · #B257307

The only Fedora Core i've ever used, 2, didn't even have an option, it just mounted the drive automatically.
