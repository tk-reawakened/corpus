---
kind: forum-thread
id: "toolkitzone-forums/12276"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12276"
title: "Items won't appear"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12276"
written: "2004-12-07T15:37:00"
last_post: "2004-12-15T22:50:00"
date_confidence: "exact"
captured: ["20041227095924"]
author: "Guest"
repliers: ["Delano", "jcb020790"]
authors: ["Guest", "Delano", "jcb020790"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_136055_amp_", captured: "20041227095924", sha256: "27f666f9756e1753331857638a57a008e169250cc9fbc68b371e21b7468f644d", wayback_url: "https://web.archive.org/web/20041227095924/http://www.toolkitzone.com/forums/viewtopic.php?p=136055&amp="}
links: []
---

# Items won't appear

### Guest · 2004-12-07 15:37 · #B136013

I've got a story sequence where I have three items sitting on the board. The problem is the only item which will appear is the one in item slot 0. The code section is:
#CreateItem("DarkXenth.itm",0)
#PutItem(0,9,5,1)
#CreateItem("Spikehead.itm",1)
#PutItem(1,3,5,1)
#CreateItem("Gorgeye.itm",2)
#PutItem(2,11,7,1)
#Wait()
Any apparent problem?

### Delano · 2004-12-07 18:00 · #B136055

Hmm, nothing immediately jumps out. Try a #ForceRedraw() after placing the last one; the screen may not being updated properly.

### jcb020790 · 2004-12-15 22:50 · #B140269

If that did'nt work, You probobly forgot to set a graphic for the item.
