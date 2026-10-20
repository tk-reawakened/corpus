---
kind: forum-thread
id: "toolkitzone-forums/26048"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Legacy Support"
skin: "phpbb2"
thread_id: "26048"
title: "About items on board"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=26048"
written: "2005-12-24T12:16:00"
last_post: "2005-12-28T19:35:00"
date_confidence: "exact"
captured: ["20060319213338", "20060320044945", "20060320133933"]
author: "imprulz"
repliers: ["Hubert Cumberdale"]
authors: ["imprulz", "Hubert Cumberdale"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_282357_amp_3Bsid_cad13df95b73f649347301b933478a1e", captured: "20060319213338", sha256: "444d0b7271bce59c67d2ef1d98e98b6de2d3783e0b9e123be9d19b4b85ce26b2", wayback_url: "https://web.archive.org/web/20060319213338/http://toolkitzone.com/forums/viewtopic.php?p=282357&amp%3Bsid=cad13df95b73f649347301b933478a1e"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_283533", captured: "20060320044945", sha256: "594434d20f6d56710310096c2ea9b3fa50bf78d7001d6c7a5adc6368b2f9d0ef", wayback_url: "https://web.archive.org/web/20060320044945/http://toolkitzone.com/forums/viewtopic.php?p=283533"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_283533_amp_3Bsid_06e0f790333e23d2463ff11405c7f78a", captured: "20060320133933", sha256: "ee3c6e8f3c1a0ba29938a263e57df9a7eeb0223b7f264bc3453eceb326811e25", wayback_url: "https://web.archive.org/web/20060320133933/http://toolkitzone.com/forums/viewtopic.php?p=283533&amp%3Bsid=06e0f790333e23d2463ff11405c7f78a"}
links: []
---

# About items on board

### imprulz · 2005-12-24 12:16 · #B282357

do you need an rpg code when you put items on board and you can pick them up and keep it? I tried putting an item on board, but whenever i walk on it in order to pick it up, i always get bumped into it and i cant pick it at all... pls help?
thnks in advance!!

### Hubert Cumberdale · 2005-12-28 19:35 · #B283533

**Code:**

```
#giveitem("Item Name")
```

You should also Read all the command available to you carefully. They're sorted by type I think so any more command like this should be easy to find. If you're having trouble figuring out how to use a command, look for the explanation and how to use it in the help manual.
