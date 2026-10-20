---
kind: forum-thread
id: "toolkitzone-forums/8739"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "8739"
title: "3.0.4 Patch - Fix List - Patch Available"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=8739"
written: "2004-09-14T19:31:00"
last_post: "2004-09-14T19:31:00"
date_confidence: "exact"
captured: ["20050312071744"]
author: "Xavier"
repliers: []
authors: ["Xavier"]
posts_present: 1
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_93812_amp_", captured: "20050312071744", sha256: "64c1e482ea55a7fdb41db14eee811b9b94ede2ea701bfb8ed0d3a6fe47798a75", wayback_url: "https://web.archive.org/web/20050312071744/http://www.toolkitzone.com/forums/viewtopic.php?p=93812&amp="}
links:
  - {url: "http://www.toolkitzone.com/fileman.php?id=3&file=820", status: "captured", local: "wayback/toolkitzone.com/fileman.php__id_3_file_820"}
---

# 3.0.4 Patch - Fix List - Patch Available

### Xavier · 2004-09-14 19:31 · #B93812

[Download Here](http://www.toolkitzone.com/fileman.php?id=3&file=820)
Help File Fixes
+ Outdated commands remaining
+ Some new commands missing
+ One or two syntax errors
Toolkit3 Fixes
tile editor ::
+ Flooding transparently / flooding tiles with transparent regions, these regions would turn black.
+ In isometric mode, the first flood would flood whole tile even if a region was boxed.
+ Undo not working.
+ Multiple windows opening instead of one.
+ isometric preview box update in 2D mode.
+ save bug in tile bitmap editor
tile grabber ::
+ Loading an image wider than the screen, the last column of tiles would disappear.
animation editor ::
+ *.anm not saving
board editor ::
+ laying down a tile in the board editor erasing the grid
program editor ::
+ file save bug
misc ::
+ *.gif format not supported
+ toolkit3.exe sometimes crashing when main file editor closing
+ Mouse cursor shown by default
Trans3 Fixes
+ *.gif format not supported
+ Crashes after the start program on Win95/98
+ Fixed WinColor() bug
+ tile characters appear as glitchy graphic squares or cursor hands on Win95/98
+ Loading a game from the start menu, the player was invisible.
+ Last frame of walking animations not shown.
+ Temporarily changed save / load dialogs back to tk2 (Windows) dialogs.
+ Changed #Prompt back to old (tk2) prompt.
+ if items start off-screen they become screen-size blurs.
+ improved pixel movement
