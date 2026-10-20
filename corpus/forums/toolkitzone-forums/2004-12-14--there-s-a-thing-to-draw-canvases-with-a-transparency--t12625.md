---
kind: forum-thread
id: "toolkitzone-forums/12625"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "12625"
title: "There's a thing to draw canvases with a transparency..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12625"
written: "2004-12-14T23:29:00"
last_post: "2004-12-20T20:42:00"
date_confidence: "exact"
captured: ["20050119034433"]
author: "Angel of Death"
repliers: ["matt72186", "Dont_Think_So"]
authors: ["Angel of Death", "matt72186", "Dont_Think_So"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139728_amp_", captured: "20050119034433", sha256: "46989d939f9ffedf0472ff5367a09507dc300beda727daef1bc67a70c0adaa5a", wayback_url: "https://web.archive.org/web/20050119034433/http://www.toolkitzone.com/forums/viewtopic.php?p=139728&amp="}
links: []
---

# There's a thing to draw canvases with a transparency...

### Angel of Death · 2004-12-14 23:29 · #B139713

But is there a command that'll let the cnvRenderNow! canvas do that? I can't use tiles that use black in them that're layered above other tiles without it messing up... =/

### matt72186 · 2004-12-14 23:40 · #B139718

Yeah render it on another canvas, then render that canvas to the cnvrendornow! I think that should work

### Dont_Think_So · 2004-12-15 00:02 · #B139728

Well, the cnvRenderNow! canvas is by default completely black, and so rendering transparently would simply replace black with black, and then render it transparent still.

### Angel of Death · 2004-12-20 20:32 · #B142830

**Dont_Think_So wrote:**

> Well, the cnvRenderNow! canvas is by default completely black, and so rendering transparently would simply replace black with black, and then render it transparent still.
>

No... Say I have a tile that's completely black, and I put it on layer two. I have one underneithe it, on layer one, that isn't. I'll be able to see through the layer two one and into layer one.
This is mostly a problem with tiles where I use transparency but don't layer it in the tile editor... because outlines, and stuff, don't show up right.

### Dont_Think_So · 2004-12-20 20:42 · #B142840

That's exactly what I said.
The only solution is to use 1,0,0 (or something to that effect) as black.
