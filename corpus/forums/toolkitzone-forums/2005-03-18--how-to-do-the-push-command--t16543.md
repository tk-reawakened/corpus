---
kind: forum-thread
id: "toolkitzone-forums/16543"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "16543"
title: "How to do the #push() command"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=16543"
written: "2005-03-18T03:05:00"
last_post: "2005-03-19T02:43:00"
date_confidence: "exact"
captured: ["20050318123216", "20050323023321", "20050323222115"]
author: "Gishzni79"
repliers: ["adrian", "AlienDude", "Guest"]
authors: ["Gishzni79", "adrian", "AlienDude", "Guest"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_182086", captured: "20050323023321", sha256: "0862eca448341b9f789b260e2c98535e3d42dc56083c2736b4127510fa877d9e", wayback_url: "https://web.archive.org/web/20050323023321/http://www.toolkitzone.com/forums/viewtopic.php?p=182086"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_182086_amp_", captured: "20050318123216", sha256: "0f83fa43989fde42b9bfc390c6c33e2eae3b4322c7e429d77ae87bb8d6ac147a", wayback_url: "https://web.archive.org/web/20050318123216/http://www.toolkitzone.com/forums/viewtopic.php?p=182086&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_182164_amp_", captured: "20050323222115", sha256: "2d5ee69cd15307821c5ca454d4904072a9c0bf97a3f1696afb363a1ba6c5e5e0", wayback_url: "https://web.archive.org/web/20050323222115/http://www.toolkitzone.com/forums/viewtopic.php?p=182164&amp="}
links: []
---

# How to do the #push() command

### Gishzni79 · 2005-03-18 03:05 · #B182086

I need help with using the push command.I have the toolkit version 3.0.5 and I need to know how to totally work the program. It keeps saying i need 1 or 2 data elements. Please give an example of what a complete push command should look like. Thank You!!!

### adrian · 2005-03-18 12:04 · #B182164

this is how it needs to look like:
Push("NE,NW,SW,SE", "Frap")
Frap is the name of the char that you whant to move.
NE,NW,SW,SE are directions
N (north)
S (south)
........
........
........

### AlienDude · 2005-03-18 18:29 · #B182286

You need the push(dir$,... , "name"), dir$, element 1, handle$ element 2. That is whats REQUIRED.
You probably did a typo.

### Guest · 2005-03-19 02:43 · #B182559

thanks for the advice
gishzni79
