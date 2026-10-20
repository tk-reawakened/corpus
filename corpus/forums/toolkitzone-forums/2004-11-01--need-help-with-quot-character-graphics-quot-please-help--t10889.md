---
kind: forum-thread
id: "toolkitzone-forums/10889"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "editor help"
skin: "phpbb2"
thread_id: "10889"
title: "Need help with &quot;Character Graphics&quot;! Please help!!"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10889"
written: "2004-11-01T17:44:00"
last_post: "2004-12-18T06:20:00"
date_confidence: "exact"
captured: ["20050119034210"]
author: "TheMatrixMaster"
repliers: ["Nick", "hseal777", "Kasai_Ryane"]
authors: ["TheMatrixMaster", "Nick", "hseal777", "Kasai_Ryane"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139453_amp_", captured: "20050119034210", sha256: "b9a53f8276cd947fc0a48002262fd4b8cba4c67abce01b428c8413d6cd701255", wayback_url: "https://web.archive.org/web/20050119034210/http://www.toolkitzone.com:80/forums/viewtopic.php?p=139453&amp"}
links: []
---

# Need help with &quot;Character Graphics&quot;! Please help!!

### TheMatrixMaster · 2004-11-01 17:44 · #B119971

Sorry if this has been answered before but I cannot figure it out... Sad Anyways here's my problem...I downloaded some character tilesets that I want to use as my main characters, however I cannot figure out how to create the graphics with .tst files. Any help would be appreciated!
Thanks,
TheMatrixMaster

### Nick · 2004-11-01 21:25 · #B120029

If the character is single tiled (32x32), just go to the Animation editor and make a set of animations using the tiles you downloaded. If they're multiple tiles (32x64 and up), make tile bitmaps for each frame and use the Tile Bitmaps as frames in your animations.

### hseal777 · 2004-12-14 04:51 · #B139426

Hey thanks for that also...I was gonna make a post on the same thing! Very Happy

### hseal777 · 2004-12-14 06:01 · #B139453

Hmm.... Sad ...I'm still havin problems with this though. First of all, what would you use to bitmap the tiles?

### Kasai_Ryane · 2004-12-15 19:02 · #B140183

umm...use tile animator in the rpg tool kit editor. now if you wanted the taller sprites (32X64 pixels) you would create one frame for the lower half, and one frame for the upper half. now when you go back into the characters, paste the top frame on the top half, and paste the lower half of you character on the bottom frame (do this by clicking the blank spaces) i recommend just using tile editor, unless you have plugins for other programs, tile editor will produce the best results if you are new.

### hseal777 · 2004-12-18 06:20 · #B141450

Great advice! Very Happy
