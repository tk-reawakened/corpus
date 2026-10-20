---
kind: page
id: "toolkitzone.net/toolkitzone.net/thread/29/"
site: "toolkitzone.net"
title: "Welcome Guest. Please or . Login Register"
original_url: "http://toolkitzone.net/thread/29/"
written: null
date_confidence: "unknown"
updated: null
captured: ["20170228155351"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.net/thread/29/index", captured: "20170228155351", sha256: "9b8b1f33f067986acc1b22101c6579c86fee9808be32b136c39a89477c5d74d9", wayback_url: "https://web.archive.org/web/20170228155351/http://toolkitzone.net/thread/29/"}
---

# Welcome Guest. Please or . Login Register

[![Toolkitzone](//storage.proboards.com/6485149/images/7gAH7AdAG8qWcbWHeVa5.png)](/)
-
-
-
- [ Toolkitzone
- [ News
- [ Welcome
- [ Site Suggestions
- [ RPG Toolkit 4.x
- [ News
- [ Discussion
- [ Complete Games
- [ Incomplete Games
- [ Support
- [ Tutorials
- [ RPG Toolkit 3.x
- [ Complete Games
- [ Incomplete Games
- [ Support
- [ Tutorials
- [ Resources
- [ Graphics
- [ Music & Sound Effects
- [ Plugins
- [ Other Game Development Systems
- [ Complete Games
- [ Incomplete Games
- [ General
- [ General Discussion
- [ Gaming
- [ My Things
![swordmaster Avatar](http://cdn.staticneo.com/w/naruto/thumb/c/c6/Kabutoyakushi.jpg/300px-Kabutoyakushi.jpg)
Posts: 52
[RPGToolkit 4.0 News Feed](/thread/29/rpgtoolkit-4-news-feed) Apr 24, 2016 11:38:20 GMT -5
Post by swordmaster on Apr 24, 2016 11:38:20 GMT -5
Hi Guys, I've been working on the Browser based engine over the week and I've updated the demo available at:
I'm up to the first 3 rooms in the The Wizard's Tower, I added some blocks in the first room, in case you are wondering why they are there. If you don't see anything new then you might need to clear your browser cache. Just trigger the programs around the doors to switch from board to board. Also I tested it in Microsoft Edge just now and everything is working, it works on Chrome, Firefox, and Edge from my experiences. Might take a couple of seconds to load the intro so be patient! Things I've added: swordmaster [[rpgtoolkit.github.io](http://rpgtoolkit.github.io)](http://rpgtoolkit.github.io)
- Program execution, including board switching, custom drawing, message windows, and block pushing.
- The intro program!
- Board switching.
- Basic items stuff.
Problems I'm aware of:
- Kicking off a program is a little slow, execution is fine though.
- In some cases you can pass through solid vectors mostly around where edges meet.
- I made the text in the intro program to bold!![xD](//storage.proboards.com/6485149/images/kqbTYyvd1sk5KGKjM_zQ.png)
![grindalf Avatar](//storage.proboards.com/6485149/avatar/jSCebVQf5xPbyRV6pz4h.gif)
Posts: 67
[RPGToolkit 4.0 News Feed](/thread/29/rpgtoolkit-4-news-feed) Apr 24, 2016 12:45:12 GMT -5
Post by grindalf on Apr 24, 2016 12:45:12 GMT -5
YAAAAAAAAY awesome stuff works in Microsoft edge now I'm gunna guess that everyone can see the vectors and its not just me. Blocks are more squished than mine were(not that I'm complaining, just pointing it out) It is a little laggy in places but overall still playable(maybe that's just edge)![:D](//storage.proboards.com/6485149/images/NVnxz5kJDjGvY6S0Az1D.png)
![swordmaster Avatar](http://cdn.staticneo.com/w/naruto/thumb/c/c6/Kabutoyakushi.jpg/300px-Kabutoyakushi.jpg)
Posts: 52
[RPGToolkit 4.0 News Feed](/thread/29/rpgtoolkit-4-news-feed) Apr 25, 2016 3:28:33 GMT -5
Post by swordmaster on Apr 25, 2016 3:28:33 GMT -5
, great it worked! Yeah everyone can see those vectors I just have them on for debugging. I made the blocks smaller based on the comments in this guys video: He was a little bit confused by the appearance of the taller blocks so I made them smaller, also I haven't figured out how to draw the player around items yet. If they were taller then the player currently would be drawn on top when he is behind it! So I got to fix that first too Any areas in particular you noticed the lag? [grindalf](/user/3)
![:P](//storage.proboards.com/6485149/images/78_BYEEEfPkO9BbtO1Rm.png)
![grindalf Avatar](//storage.proboards.com/6485149/avatar/jSCebVQf5xPbyRV6pz4h.gif)
Posts: 67
[RPGToolkit 4.0 News Feed](/thread/29/rpgtoolkit-4-news-feed) Apr 25, 2016 6:19:41 GMT -5
Post by grindalf on Apr 25, 2016 6:19:41 GMT -5
mostly in the block pushing but overall it was running a little slow. I woudent worry about it though as its not that bad. I did like the way a block could be pushed by pushing another block that didn't work in the original
![Cuthalion Avatar](//storage.proboards.com/6485149/avatar/8_9wfZRfi__oYb4moQo3.jpg)
Posts: 52
[RPGToolkit 4.0 News Feed](/thread/29/rpgtoolkit-4-news-feed) Apr 25, 2016 10:44:16 GMT -5
Post by Cuthalion on Apr 25, 2016 10:44:16 GMT -5
For getting z-order correct, the game has to look at the point where the object/player is standing, rather than the top-left of their drawing rectangle. Between the feet, rather than over the head. You might be able to fudge this by using the position of the lowermost tile of a player's graphic (if they're made of tiles), or the bottom edge or half a tile-height above the bottom edge. It may be best to offer the game designers the ability to designate the ground point of an animation. I don't remember how TK3 did it.
![swordmaster Avatar](http://cdn.staticneo.com/w/naruto/thumb/c/c6/Kabutoyakushi.jpg/300px-Kabutoyakushi.jpg)
Posts: 52
[RPGToolkit 4.0 News Feed](/thread/29/rpgtoolkit-4-news-feed) Apr 27, 2016 7:23:18 GMT -5
Post by swordmaster on Apr 27, 2016 7:23:18 GMT -5
, yeah watching that video again I can see how pushing blocks worked in TK3 looks like it pushed them a set number of pixels, 32 from what I can tell. I'll revise the blocking pushing code to work the same way. When it comes to speed I'll probably focus on getting features complete, then I'll start tuning performance towards the end. , yeah I've come up with a solution in my head for the item drawing. I'll probably order all the sprites and players on the board for each layer based on their animations bottom y value. Then just draw the ones closet to the top of the screen first, this will achieve the illusion of depth that I need. [grindalf](/user/3)
by Last Edit: Apr 27, 2016 7:23:36 GMT -5 [swordmaster](/user/4)
![Cuthalion Avatar](//storage.proboards.com/6485149/avatar/8_9wfZRfi__oYb4moQo3.jpg)
Posts: 52
[RPGToolkit 4.0 News Feed](/thread/29/rpgtoolkit-4-news-feed) Apr 27, 2016 20:31:10 GMT -5
Post by Cuthalion on Apr 27, 2016 20:31:10 GMT -5
Guessing the block pushing pushes exactly one tile width/height, whatever that is defined as. (Or it might push it one tile, then snap it to that tile in case it was not aligned at the start of the push. I don't know if I've ever used the command; I'm just guessing.) I think that item drawing order should work fine. I do basically the same in my non-TK engine, but with more complicated shenanigans because of the isometric perspective and the ability of tiles to be tall and stuff.
rpg17
![rpg17 Avatar](http://s5149.storage.proboards.com/6485149/a/n3wRLBmaUFtlA5lEEUBU.png)
Posts: 0
[RPGToolkit 4.0 News Feed](/thread/29/rpgtoolkit-4-news-feed) Apr 27, 2016 22:42:02 GMT -5 via mobile
Post by rpg17 on Apr 27, 2016 22:42:02 GMT -5
Humm... Anyway to make it android accessible? It interprets commands and sends it to the engine if I've looked at it right. :/ idk. Figured I'd ask. It loads I just can't hit enter lol.
![swordmaster Avatar](http://cdn.staticneo.com/w/naruto/thumb/c/c6/Kabutoyakushi.jpg/300px-Kabutoyakushi.jpg)
Posts: 52
[RPGToolkit 4.0 News Feed](/thread/29/rpgtoolkit-4-news-feed) Apr 28, 2016 7:08:24 GMT -5
Post by swordmaster on Apr 28, 2016 7:08:24 GMT -5
, Looking at the C++ source for trans3 it pushes items 32 pixels if it is in tile based movement or 8 pixels if it is in pixel movement. It is hardcoded to those values I'll probably follow that convention for now. @rpg17, errr is that rpggamer17? I'm afraid mobile gaming is a ways down the line at the moment, but I'd like to add it eventually [Cuthalion](/user/7)
![:)](//storage.proboards.com/6485149/images/bed0tKwtj8NvFSLwGpkw.png)
rpg17
![rpg17 Avatar](http://s5149.storage.proboards.com/6485149/a/n3wRLBmaUFtlA5lEEUBU.png)
Posts: 0
[RPGToolkit 4.0 News Feed](/thread/29/rpgtoolkit-4-news-feed) Apr 28, 2016 20:30:09 GMT -5 via mobile
Post by rpg17 on Apr 28, 2016 20:30:09 GMT -5
This Forum Is Hosted For FREE By Get Your Own !
