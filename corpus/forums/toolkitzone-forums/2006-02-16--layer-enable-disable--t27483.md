---
kind: forum-thread
id: "toolkitzone-forums/27483"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "27483"
title: "Layer enable/disable"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27483"
written: "2006-02-16T03:11:00"
last_post: "2006-02-18T23:37:00"
date_confidence: "exact"
captured: ["20060305160210"]
author: "Dont_Think_So"
repliers: ["vrn790", "Delano"]
authors: ["Dont_Think_So", "vrn790", "Delano"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_299655_amp_3Bsid_41a8f0424612fd95602078968b75364d", captured: "20060305160210", sha256: "042c314c7615fbe9969194a64b5d8e937812613fce06af0f0d3f11900348f9ea", wayback_url: "https://web.archive.org/web/20060305160210/http://toolkitzone.com/forums/viewtopic.php?p=299655&amp%3Bsid=41a8f0424612fd95602078968b75364d"}
links: []
---

# Layer enable/disable

### Dont_Think_So · 2006-02-16 03:11 · #B298721

Here's an idea that cropped up on the coding help forum:
Now that the render system has been rewritten to draw layer-by-layer (at least, I believe this is the case), couldn't we get some RPGCode commands to switch the drawing of layers on or off? This would allow for some interesting effects, such as turning weather on or off in a custom menu, or allowing the player to go up some steps and appear on a new floor (while still having NPCs moving underneath), which could mimic depth.

### vrn790 · 2006-02-17 00:22 · #B299009

I like the idea. In addition, it would also be nice if you could choose which layers to turn on and off Smile

### Delano · 2006-02-17 10:09 · #B299153

Boards aren't drawn layer by layer, so any rapid switching would be a bad idea (e.g., to emulate rain), but in principle it would work.

### vrn790 · 2006-02-18 23:37 · #B299655

I didn't mean that i wanted to rapidly switch layers. Let me clarify a bit: Basically, by choosing what layers to turn on and off, you could make different floors in a building and such. Now, pretend that every floor uses two layers. For the first floor, you could enable the first two layers and turn off the rest. Then when the character steps onto the second floor, you could enable the third and fourth layers and turn off the rest. So, you could simulate depth and create complex structures without having to use one gigantic board or more than one board.
