---
kind: forum-thread
id: "toolkitzone-forums/27083"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "27083"
title: "Board Layering Advanced?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27083"
written: "2006-02-03T13:47:00"
last_post: "2006-02-03T16:04:00"
date_confidence: "exact"
captured: ["20060213005159", "20060302105721", "20060302105746", "20060320224502", "20060320224541", "20060320224559"]
author: "Ryukenshen"
repliers: ["Delano"]
authors: ["Ryukenshen", "Delano"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_294714", captured: "20060320224559", sha256: "0e1be31bce31267c98527f4604b6992f56f6b2510c1f71f4267474ff325e1a97", wayback_url: "https://web.archive.org/web/20060320224559/http://toolkitzone.com/forums/viewtopic.php?p=294714"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_294714_amp_3Bsid_3d65e9ce0605680f343b3057317c5fd0", captured: "20060302105721", sha256: "095e4c4ad1b2b1db0c43051b380055d66d2e3cdf18c8ab80ef6fd80d387c3ed3", wayback_url: "https://web.archive.org/web/20060302105721/http://toolkitzone.com/forums/viewtopic.php?p=294714&amp%3Bsid=3d65e9ce0605680f343b3057317c5fd0"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_294734", captured: "20060320224541", sha256: "a19f18e96472ad576e9283836f02467636f87d3ebb03e13ecfa8a40bfd8c9b8c", wayback_url: "https://web.archive.org/web/20060320224541/http://toolkitzone.com/forums/viewtopic.php?p=294734"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_294734_amp_3Bsid_3d65e9ce0605680f343b3057317c5fd0", captured: "20060302105746", sha256: "61152169c5a36d9fca4ed1aa67df48fc54d1132590f3fbbe26debdc8a6b92a8e", wayback_url: "https://web.archive.org/web/20060302105746/http://toolkitzone.com/forums/viewtopic.php?p=294734&amp%3Bsid=3d65e9ce0605680f343b3057317c5fd0"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_294735", captured: "20060320224502", sha256: "0e2f6a675c5f0f09fa7cdc7c92e1a3a015909289943f0f24729c9f2f184b8f63", wayback_url: "https://web.archive.org/web/20060320224502/http://toolkitzone.com/forums/viewtopic.php?p=294735"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_294735_amp_3Bsid_125a611e962141c45299d3c172df313f", captured: "20060213005159", sha256: "ab3c236c2f766e393cd73f51d8906e1fb1d8192eea4c5e886ae8a39e09090d48", wayback_url: "https://web.archive.org/web/20060213005159/http://toolkitzone.com/forums/viewtopic.php?p=294735&amp%3Bsid=125a611e962141c45299d3c172df313f"}
links:
  - {url: "http://www.gimp.org.", status: "external", local: null}
---

# Board Layering Advanced?

### Ryukenshen · 2006-02-03 13:47 · #B294714

I seem to have found a problem with Farodin's developement.
I've been trying to compile my boards in MS Paint, but, even with vector collision, it's not going to work. Too many objects are layered on top of each other. That's when I had an idea - layerable backgrounds!
If I could build my boards layer-by-layer and then add each background a layer above the other, I could continue developement. So this is very urgent (for me). Delano, or whoever it is making 3.0.7, this would be a useful feature for everyone. It is needed!

### Delano · 2006-02-03 15:49 · #B294734

It sounds like you need a better graphics editor! If you don't want to buy anything you could try the GIMP, it's free: [www.gimp.org.](http://www.gimp.org.)
On the TK side: in 3.0.7 you will be able to place images on any layer, so you could build up your background like that and have your players on high layers, rather than needing to layer the background.

### Ryukenshen · 2006-02-03 16:04 · #B294735

**Delano wrote:**

> On the TK side: in 3.0.7 you will be able to place images on any layer, so you could build up your background like that and have your players on high layers, rather than needing to layer the background.
>

It's just that I have so many cliffs (sorta like Golden Sun; if you've played it you know what I'm talking about) and it's simply so complex that setting up those vector collision positions everywhere would be overwhelming, so I'm first going to start with the bare ground on one layer, then add the objects sitting on it on the next, then the next cliff, the objects on the cliff, and any cliffs that are on that cliff, followed again by the objects resting upon my little mini-mountain. I must say, I am quite pleased with the way 3.0.7 seems to be coming along; the new features sound great, and I'm finally satisfied with Farodin's graphics. In fact, I could probably get a demo up about a month after 3.0.7's release, as the boards will already be done.
And those screenshots that Xavier posted of Lost Age and Freija utilizing the vector collision are brill. TK games are gonna get much sexier. Smile
