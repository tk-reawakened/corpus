---
kind: forum-thread
id: "toolkitzone-forums/12583"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "12583"
title: "collision detection"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12583"
written: "2004-12-14T05:14:00"
last_post: "2004-12-17T17:59:00"
date_confidence: "exact"
captured: ["20041228072429"]
author: "saberknight"
repliers: ["matt72186", "dragcash"]
authors: ["saberknight", "matt72186", "dragcash"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139481_amp_", captured: "20041228072429", sha256: "9b6598a3fe68a92398d4718557c9ca454600efd7fccc5ae56b41efbc2c628e07", wayback_url: "https://web.archive.org/web/20041228072429/http://www.toolkitzone.com/forums/viewtopic.php?p=139481&amp="}
links:
  - {url: "http://sourceforge.net/projects/fury2/", status: "external", local: null}
  - {url: "http://sphere.sf.net/", status: "external", local: null}
---

# collision detection

### saberknight · 2004-12-14 05:14 · #B139441

Hay I started working on a vb.net port of the tool kit im working on the trans i wanted to know what the best way to do collision detection would be im using GDI to draw everything ok so it wont work like the rpg tool kit the variables and methods are different but i think it will be better given enough time

### matt72186 · 2004-12-14 05:26 · #B139444

Wow.. you don't even know simple algorithms like collision detection, and you're trying to make a complete remake of the RPG Toolkit in .net. Personally (and I mean this with respect to the RPG Toolkit and with no offense to you as a person)
1) I wouldn't trust the "RPG Toolkit" in your hands
2) You wouldn't be able to call it the "RPG Toolkit" since it really would have no relation to it other than perhaps the file formats if you kept them intact.
3) Collision detection in RPG Toolkit isn't pixelbased so it's all a matter of detecting if two rectangles are overlapping (by comparing their x1, y1, x2, y2 values)

### saberknight · 2004-12-14 05:35 · #B139447

I know that much!
1.I don't have another name Embarassed
2.no the file format is not the same mine is better I think Cool
3.I know that you can check the x and y values im not stupid but I was asking the best way to do it do i store the stop x and y locations in an array or do i keep the section permissions in an array or what Question
PS. I plan to go open source with the trans after I finish the proof of concept
The .dll files Im making make it easy to store save and load the game data
so I hope people will pitch in

### dragcash · 2004-12-14 06:10 · #B139456

**matt72186 wrote:**

> Wow.. you don't even know simple algorithms like collision detection, and you're trying to make a complete remake of the RPG Toolkit in .net. Personally (and I mean this with respect to the RPG Toolkit and with no offense to you as a person)
> 1) I wouldn't trust the "RPG Toolkit" in your hands
> 2) You wouldn't be able to call it the "RPG Toolkit" since it really would have no relation to it other than perhaps the file formats if you kept them intact.
> 3) Collision detection in RPG Toolkit isn't pixelbased so it's all a matter of detecting if two rectangles are overlapping (by comparing their x1, y1, x2, y2 values)
>

Mat let him dream man, we all gotta start somewhere Wink

### matt72186 · 2004-12-14 11:32 · #B139481

**saberknight wrote:**

> I know that much!
> 1.I don't have another name Embarassed
> 2.no the file format is not the same mine is better I think Cool
> 3.I know that you can check the x and y values im not stupid but I was asking the best way to do it do i store the stop x and y locations in an array or do i keep the section permissions in an array or what Question
> PS. I plan to go open source with the trans after I finish the proof of concept
> The .dll files Im making make it easy to store save and load the game data
> so I hope people will pitch in
>

Here's my best advice, check out some other RPG Editors (open source ones) and see how they did it, you can learn a lot by looking at what already works. Editors that I know are open source are Sphere ( <http://sphere.sf.net/>), Fury^2 ( <http://sourceforge.net/projects/fury2/>), and obviously the RPG Toolkit (here)

### saberknight · 2004-12-17 17:59 · #B141108

I Know a few ways to do it but i desided i would rather work on an existing project not just start my own from scratch but thanks
