---
kind: forum-thread
id: "toolkitzone-forums/12523"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "general chat"
skin: "phpbb2"
thread_id: "12523"
title: "Any Online TK Related Questions..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12523"
written: "2004-12-14T16:51:00"
last_post: "2004-12-14T16:51:00"
date_confidence: "exact"
captured: ["20041228072433"]
author: "Caliber Mengsk"
repliers: []
authors: ["Caliber Mengsk"]
posts_present: 1
pages_present: [2]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 15, url: "http://toolkitzone.com/forums/viewtopic.php?t=12523", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139527_amp_", captured: "20041228072433", sha256: "562401df4834419356cd8469291000e7745108d4feb392615aaeda25b0d09319", wayback_url: "https://web.archive.org/web/20041228072433/http://www.toolkitzone.com/forums/viewtopic.php?p=139527&amp="}
links: []
---

# Any Online TK Related Questions...

> [!missing] gap:1-15 · http://toolkitzone.com/forums/viewtopic.php?t=12523 · never-captured
> Page 1 of 2 was not recovered.

### Caliber Mengsk · 2004-12-14 16:51 · #B139527

the split screen probably could work useing:
Canvas'
Threads
Branch loops
While loops
a faster RPGcode and Graphics engine in the TK.
but it is quite litereally possible. You would have to have a thread running to see the secondary keypresses for the 2nd player, then another to tell him which way to go. (only four way direction would work I think, but don't quote me on that.) Then use the render/canvas together to draw the second players screen. If I recall correctly, you can offset the boards from the origonal charactors (player ones) view. If anything, use a thread that has the pan offset so many tiles from player ones position. (getplayerpos() or something like that... Don't remember the exact one. rpgcode refrence would help there.)
Now, it would be VERY slow this way, that is why you would need the faster RPGcode and Graphics engine. ^_^ Which I am told will be in the next version of tk3, tk3.0.5(which from now on I will call 3.05) By Who? Resources my friend... resources...(actually.. I just don't remember who.)
