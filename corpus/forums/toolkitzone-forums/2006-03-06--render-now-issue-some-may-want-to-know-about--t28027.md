---
kind: forum-thread
id: "toolkitzone-forums/28027"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "28027"
title: "Render Now issue, some may want to know about."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=28027"
written: "2006-03-06T17:54:00"
last_post: "2006-03-07T06:34:00"
date_confidence: "exact"
captured: ["20060320134400"]
author: "Caliber Mengsk"
repliers: ["Dont_Think_So", "Greg", "Moo Of Doom", "Colin"]
authors: ["Caliber Mengsk", "Dont_Think_So", "Greg", "Moo Of Doom", "Colin"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_303995_amp_3Bsid_7661bbbbb86e5246ab8babb6f36bbb96", captured: "20060320134400", sha256: "bbc46dc28a18c39ae7e697597f7ea2a813b367d405dae07a49f518d5b8650227", wayback_url: "https://web.archive.org/web/20060320134400/http://toolkitzone.com/forums/viewtopic.php?p=303995&amp%3Bsid=7661bbbbb86e5246ab8babb6f36bbb96"}
links: []
---

# Render Now issue, some may want to know about.

### Caliber Mengsk · 2006-03-06 17:54 · #B303862

A true black color will show up as transparent on the render now canvas. O-o... can I just ask why? Black doesn't mean transparent on any other canvas, so why the render now? I think you should just have to set stuff to transparent like you would with a regular canvas by setimagetransparent. Is this a bug or something?

### Dont_Think_So · 2006-03-07 02:07 · #B303958

It's not a bug, it's just a strange feature. By default, the rendernow's transparent color is black; this way, using the color 0,0,0 will give you transparency (you can always use 0,0,1 where black is necessary).
I personally think it should be pure red (255,0,0) by default so it will match other areas of the toolkit, and there should be a command to change it.

### Caliber Mengsk · 2006-03-07 02:58 · #B303969

Agreed.

### Greg · 2006-03-07 03:04 · #B303971

Yeah. It needs to be a color only idiots would use (except in rare cases), AKA pure red, blue, or green.

### Moo Of Doom · 2006-03-07 05:57 · #B303991

Why not 0, 1, 2 like the tile transparent color?

### Colin · 2006-03-07 06:12 · #B303993

Why not this? Why not that? Because of how TK3.0.x is coded. Black is not a transparent colour for the canvas, it's the general transparent colour in 3.0.6. In 3.0.7, it will either not change, or become 255, 255, 255, but I prefer it not changing.

### Dont_Think_So · 2006-03-07 06:34 · #B303995

Shouldn't then the default background color for the cursor also be black?
