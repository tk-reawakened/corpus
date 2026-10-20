---
kind: forum-thread
id: "toolkitzone-forums/12209"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "editor help"
skin: "phpbb2"
thread_id: "12209"
title: "Not making solids"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12209"
written: "2004-12-06T02:39:00"
last_post: "2004-12-06T22:26:00"
date_confidence: "exact"
captured: ["20050116084231"]
author: "solaceinsilence"
repliers: ["Koh Wei Zane", "Delano"]
authors: ["solaceinsilence", "Koh Wei Zane", "Delano"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135683_amp_", captured: "20050116084231", sha256: "300e4876e4ea5448376a02e6d926dc367b28b3841a7c3944b300d0eab4c718ea", wayback_url: "https://web.archive.org/web/20050116084231/http://www.toolkitzone.com/forums/viewtopic.php?p=135683&amp="}
links: []
---

# Not making solids

### solaceinsilence · 2004-12-06 02:39 · #B135347

I download Toolkit 3.0.4 now i laid down tiles and selected them as solids and saved. but when i test my game the tiles that i selected as solids show up as under tiles and my character moves under them instead of being stoped beside them as a normal solid tile would. any thing im doing wrong here?

### Koh Wei Zane · 2004-12-06 02:45 · #B135350

Erm... May be related to board saving.
Go to your game folder, then uncheck read only on your boards folder... Dunno, Nick said something like that. Might want to try it out?

### solaceinsilence · 2004-12-06 02:51 · #B135356

ok ty, i will try that out. i dunno it rather strange, this is the first time i tried Toolkit 3.X.X relase. i like it so far, other than this catch up.

### Delano · 2004-12-06 17:47 · #B135567

This is probably being caused because the tiles are on a layer above the player; if this is the case, the tiles the player walks on automatically become "under" tiles.
Check which layer you've placed the tiles on, and check which layer your character is on.

### solaceinsilence · 2004-12-06 22:26 · #B135683

Ok well i checked both out both of your replies and i've solved the problem for now. I hope this doesn't happen again cause it was a nusence.
