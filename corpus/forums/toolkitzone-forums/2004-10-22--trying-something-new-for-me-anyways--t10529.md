---
kind: forum-thread
id: "toolkitzone-forums/10529"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "10529"
title: "Trying something new. For me anyways......"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10529"
written: "2004-10-22T22:59:00"
last_post: "2004-10-31T16:46:00"
date_confidence: "exact"
captured: ["20050109194031"]
author: "Ross L."
repliers: ["catwhowalksbyhimself", "Angel of Death"]
authors: ["Ross L.", "catwhowalksbyhimself", "Angel of Death"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_119533_amp_", captured: "20050109194031", sha256: "49a99065d0053b8c1d4805136eea943d3c045a937014132fc3192a9046462814", wayback_url: "https://web.archive.org/web/20050109194031/http://www.toolkitzone.com/forums/viewtopic.php?p=119533&amp="}
links:
  - {url: "http://www.hsgamers.com/gameboy/screenshots/fireemblem/3.jpg", status: "external", local: null}
  - {url: "http://www.nintendoinsider.com/site/media/fe2.jpg", status: "external", local: null}
  - {url: "http://www.the-nextlevel.com/reviews/handheld/fire_emblem/screen07.jpg", status: "external", local: null}
  - {url: "http://www.the-nextlevel.com/reviews/handheld/fire_emblem/screen09.jpg", status: "external", local: null}
---

# Trying something new. For me anyways......

### Ross L. · 2004-10-22 22:59 · #B115418

Ok my brother and I are planning on making a new kind of game that won't be serious at all in it's nature. The most serious part about the game is the battles, which I am having difficulty thinking of how to go about coding it. I was hoping that matt would finish his Battle System tutorial, but it seems he is a bit too busy now. Razz
At any rate, the Battle System in mind is Tactics. Sadly, I am not the most well versed in RPGCode and could really use some help with the coding. ^^
![](http://www.the-nextlevel.com/reviews/handheld/fire_emblem/screen07.jpg)
![](http://www.hsgamers.com/gameboy/screenshots/fireemblem/3.jpg)
![](http://www.the-nextlevel.com/reviews/handheld/fire_emblem/screen09.jpg)
![](http://www.nintendoinsider.com/site/media/fe2.jpg)
It looks very simple and looks like mostly animation. Basically it's like any other tactics game. You can select which unit you want to move, you move them, and then you have a menu, which hass all your options.
Maybe it is more complex than I am thinking it is?

### catwhowalksbyhimself · 2004-10-25 22:21 · #B116931

No, not really. You are correct. Just like any CBS, it is basically just a series of menus strung together.

### Angel of Death · 2004-10-31 16:46 · #B119533

Well, as for selecting and moving the things...
There're five ways I can think of right now. First one is to scroll through the people on a menu, and give options on where to move and stuff when you get to them.
Second, is to use the mouse, and to store the name or whatever you identify a character by in it in a coordinate variable thing. Like, if oyu click on tile 4,3 and Bob was there, it would be XY[5][4]$="Bob" (I'm hoping you're using TK3 or this'll be more complicated)
Third one uses a keyboard cursor, which scrolls along the screen, either by 1 or so pixel or 32 pixels (one tile =P). Uses the same idea as number two, with the multidimentional arrays.
Last two are just modified versions of 2 and 3, where you store it in something like BobX!=5, BobY!=4... and then checks every one of the characters' coordinates to see if they match the cursor.
Of course, I'm not really sure what all you need help on, so this is all I can say now XD
