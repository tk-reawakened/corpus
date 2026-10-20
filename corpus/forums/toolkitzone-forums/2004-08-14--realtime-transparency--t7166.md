---
kind: forum-thread
id: "toolkitzone-forums/7166"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "toolkit 3.x"
skin: "phpbb2"
thread_id: "7166"
title: "Realtime Transparency..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7166"
written: "2004-08-14T15:55:00"
last_post: "2004-08-14T17:15:00"
date_confidence: "exact"
captured: ["20040912085448"]
author: "Marz"
repliers: ["Colosseus"]
authors: ["Marz", "Colosseus"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_75324_amp_", captured: "20040912085448", sha256: "b31109f84e00afce9f042218202c5dea9cf0f0dc1c45121990d8560e8f7d850f", wayback_url: "https://web.archive.org/web/20040912085448/http://www.toolkitzone.com/forums/viewtopic.php?p=75324&amp="}
links:
  - {url: "http://www.cywh.com/disc.php?forum=5/", status: "external", local: null}
  - {url: "http://www.mysticsoftware.net/images/tk_army.png", status: "captured", local: "wayback/mysticsoftware.net/images/tk_army.png"}
  - {url: "http://www.zakap.com/marz/", status: "external", local: null}
---

# Realtime Transparency...

### Marz · 2004-08-14 15:55 · #B75300

Hey,
I'm not sure if the name is misleading, but I want to be able to set tiles on other tiles in "realtime" without having to layer them onto different tiles in the Tile Editor. This allows me to save space, rather than have multiple layered tiles. For example, rather than have a "fence on dirt" and "fence on grass" tile, along with a fence tile, a dirt tile, and a grass tile, I can simple have 3 tiles, and then 'layer' them on in the board editor.
Is this already possible?
_________________
[![](http://www.mysticsoftware.net/images/tk_army.png)](http://www.cywh.com/disc.php?forum=5/)
Long live the OT Community!
[TK Centre](http://www.zakap.com/marz/)

### Colosseus · 2004-08-14 17:15 · #B75324

The Board Editor has up to 8 layers. Put all the terrain and stuff on layer 1, and then put your transparent tile at the desired position on layer 2. Switch back to layer 1. You won't see the tile, but it's there though - and it will appear when you run your game and play on that board. But to preview it, you could click the "Draw All Layers" button in the Board Editor.
You could also try the SetImageTransparent function... I don't know if it works with Tile files, but it works with bitmaps, jpegs, gifs and other picture files.
Good luck
