---
kind: forum-thread
id: "toolkitzone-forums/16563"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "16563"
title: "Toolkit Question"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=16563"
written: "2005-03-18T17:59:00"
last_post: "2005-03-18T23:56:00"
date_confidence: "exact"
captured: ["20050326002813"]
author: "Japanimanga"
repliers: ["Delano"]
authors: ["Japanimanga", "Delano"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_182470_amp_", captured: "20050326002813", sha256: "633283c10eee8a69b54d936d2fad08a92cbe229ac4e0c6e9bf1c558732812d39", wayback_url: "https://web.archive.org/web/20050326002813/http://toolkitzone.com/forums/viewtopic.php?p=182470&amp="}
links: []
---

# Toolkit Question

### Japanimanga · 2005-03-18 17:59 · #B182272

Hi, I need help creating a NPC for my game. It says to create one, but doesn't tell how. Please help me!

### Delano · 2005-03-18 23:56 · #B182470

An NPC is just an Item with walking graphics. After creating and animating the NPC, check the "Board Driven" option to let this item be active on a board and click the corresponding "Edit". For "Program to run while item is on board" select "wander.prg" for basic wandering, or you can write a more complex routine using the PushItem() command and a loop. Set a program that, for instance, makes the npc talk and set it as the "program to run when item is picked up". Then place the item on a board (RPGCode > Set Item in the board editor).
