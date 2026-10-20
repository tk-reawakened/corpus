---
kind: forum-thread
id: "toolkitzone-forums/12492"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12492"
title: "Gfx Loading Question"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12492"
written: "2004-12-12T01:40:00"
last_post: "2004-12-12T01:59:00"
date_confidence: "exact"
captured: ["20041227215242"]
author: "Zio"
repliers: ["Dont_Think_So"]
authors: ["Zio", "Dont_Think_So"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_138272_amp_", captured: "20041227215242", sha256: "50dd61ddd14f3d5a4b31d1ad0314c68b2fbd017a42644952cec7d98b04f8b44c", wayback_url: "https://web.archive.org/web/20041227215242/http://www.toolkitzone.com/forums/viewtopic.php?p=138272&amp="}
links: []
---

# Gfx Loading Question

### Zio · 2004-12-12 01:40 · #B138249

How would i go about makeing it so that none of my menu gfx show untill they are all loaded??

### Dont_Think_So · 2004-12-12 01:42 · #B138253

You will have to draw them all to a canvas first, then display the canvas on the screen. Look up all canvas-related commands in the reference.

### Zio · 2004-12-12 01:46 · #B138259

that's what i thought but the only command that draws to a canvas is the #Bitmap command and it doesn't have an x,y position variable unless i can use #SetImage and in that case it doesn't say how.

### Dont_Think_So · 2004-12-12 01:47 · #B138261

Heh, the reference is incomplete.
All graphics commands draw to canvases. Just add the canvas ID at the end.

### Zio · 2004-12-12 01:48 · #B138262

thanks man

### Zio · 2004-12-12 01:56 · #B138267

one more quick question, is #Animation compatible or will i have to just load it after i draw the canvas??

### Dont_Think_So · 2004-12-12 01:58 · #B138270

Hmm... I'm not sure. You will have to experiment, but if I had to guess, it's not compatible. If it is, then you would have to constantly draw the canvas on the screen.

### Zio · 2004-12-12 01:59 · #B138272

ok, thanks again
