---
kind: forum-thread
id: "toolkitzone-forums/12279"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "computing & technology"
skin: "phpbb2"
thread_id: "12279"
title: "Networking computers possible?......"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12279"
written: "2004-12-07T17:11:00"
last_post: "2004-12-09T15:10:00"
date_confidence: "exact"
captured: ["20041227215309"]
author: "Ivan"
repliers: ["EB", "Michael J. Hill", "Dont_Think_So", "Spyder", "Nih", "Colosseus"]
authors: ["Ivan", "EB", "Michael J. Hill", "Dont_Think_So", "Spyder", "Nih", "Colosseus"]
posts_present: 14
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_136989_amp_", captured: "20041227215309", sha256: "665386f86835c0cdc33f732e1ad430adc593e4ac9b54afa0f8d6eca2a4c28232", wayback_url: "https://web.archive.org/web/20041227215309/http://www.toolkitzone.com/forums/viewtopic.php?p=136989&amp="}
links: []
---

# Networking computers possible?......

### Ivan · 2004-12-07 17:11 · #B136029

Ok my question is not if you can network computers but lets say i network 4 computers, each one at about 1.8ghz off of an amd athlon xp like i have. Then when i network with good Ethernet cable or something would it be possible to make the computers share resources including proccessing? I mean it would be the sensible thing if lets say you're working on a 3d game, using nice 3d software, couldnt you do it so when you are processing something, the process splits into 4 smaller processes and each computer ends up processing 1 part(1 out of 4) and then they all send it back to the original computer, or maybe make a setup of 5 computers, where the 5th computer is the main computer and you use it do do everything and on a large process it would do the process split except that it would split into 4 processes between the four extra processes so that when the processes are being transfered back to it it could take it in faster than if it was processing itself.
I'm sorry if this is a bit unclear or maybe i dont know what i'm talking about but i think a setup like this would increase processing speeds a lot. Spyder and Randy you the xperts on this so please help.

### EB · 2004-12-07 18:00 · #B136054

No.

### Ivan · 2004-12-07 18:10 · #B136058

is anybody working on making it possible? like microsoft or something?

### Michael J. Hill · 2004-12-07 20:22 · #B136115

This is part of the premise of IBM's cell processing technology, but it's not practical in a mainstream application such as this, at least, not yet.

### Dont_Think_So · 2004-12-07 20:47 · #B136123

There is some sort of networking software that allows you to do that, however it only works for specific applications designed to do just that.

### Spyder · 2004-12-07 21:04 · #B136131

Even if there was a way, it wouldn't work for games, because the bandwidth is way too low on a network. The information would travel between the computers at an extremely slow rate compared to how fast it travels between components on one computer.

### Ivan · 2004-12-08 02:18 · #B136322

i meant when you're using programs to make games, like 3d studio max or 3d gamestudio or like maya or something.

### Michael J. Hill · 2004-12-08 03:06 · #B136357

The time it takes to render a 3d image, the bandwidth would bottleneck it, giving you no noticeable increase in performance, and actually, it may be detrimental.

### Spyder · 2004-12-08 10:01 · #B136429

Only thing I could see making any use out of it would be rendering large movie files or something, where you could send a chunk of data to each computer to render.

### Dont_Think_So · 2004-12-08 22:39 · #B136626

Which is generally what it is used for. That and other extremely large calculations.
Like pi to thousands of units.
Or the SETI project.

### Nih · 2004-12-09 03:06 · #B136816

Hmm... I think it all has to do with compilers, actually. If I'm not mistaken, there's a set of compiling tools for Valve Hammer Editor (the mapping utility for Half-Life) that allows you to use multiple networked computers to compile faster. However, I doubt things like this exist for 3D modelling software, though you may look it up.

### Ivan · 2004-12-09 03:38 · #B136838

thanks I'll look into it more

### Dont_Think_So · 2004-12-09 04:03 · #B136851

No, this stuff is mainly used for 3D modelling software.

### Colosseus · 2004-12-09 15:10 · #B136989

There's no use for a professional company to render a huge 3D movie on ONE computer. That would mean Ice Age wouldn't come until, like, 2100. So, network rendering isn't that uncommon at all. For example Lightwave 3D allows network rendering.
