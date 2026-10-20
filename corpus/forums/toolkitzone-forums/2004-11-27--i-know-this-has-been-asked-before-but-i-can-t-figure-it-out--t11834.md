---
kind: forum-thread
id: "toolkitzone-forums/11834"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "editor help"
skin: "phpbb2"
thread_id: "11834"
title: "I know this has been asked before, but i can't figure it out"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11834"
written: "2004-11-27T14:01:00"
last_post: "2004-11-27T16:12:00"
date_confidence: "exact"
captured: ["20050112161959"]
author: "King Arthur"
repliers: ["Delano"]
authors: ["King Arthur", "Delano"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_130906_amp_", captured: "20050112161959", sha256: "a3e961d455d714a267a739ed8d7f634bda93f2cd260f58eeae41c450fbd8df1d", wayback_url: "https://web.archive.org/web/20050112161959/http://www.toolkitzone.com/forums/viewtopic.php?p=130906&amp="}
links: []
---

# I know this has been asked before, but i can't figure it out

### King Arthur · 2004-11-27 14:01 · #B130895

I'm trying to make my main character and some enemies and when it comes to the graphics part the only available option is the same default character, I can't seem to use any of the one's I downloaded.
Can someone please help me, I promis if you do you might soon *or in about a year) have something new and fun to play. (well probably not),
King Arthur

### Delano · 2004-11-27 16:12 · #B130906

You need to make animations (.anm's) from your tilesets for each sprite. In the animation editor, click the sprite frame to insert a tile or bitmap, and use the tools on the left to create new frames. You might also need to set the transparent colour for each frame here. You'll need to make separate animations for each direction, and once saved, you can set them in the graphics sections of the characters, items and enemies.
