---
kind: forum-thread
id: "toolkitzone-forums/7210"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "7210"
title: "I need an explanation on how to make NPC's"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7210"
written: "2004-08-15T16:52:00"
last_post: "2004-08-17T03:21:00"
date_confidence: "exact"
captured: ["20040915043701", "20040925162005"]
author: "vUnit321"
repliers: ["sims116", "bradseguin", "stanleywuu", "khaldore", "Darkswordsman", "jo_potato"]
authors: ["vUnit321", "sims116", "bradseguin", "stanleywuu", "khaldore", "Darkswordsman", "jo_potato"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_75909_amp_", captured: "20040915043701", sha256: "4466d014a74a7449af589e31d5b6483bde4be3a6eeb139fcbd8604b5ad954cb4", wayback_url: "https://web.archive.org/web/20040915043701/http://www.toolkitzone.com/forums/viewtopic.php?p=75909&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_76929_amp_", captured: "20040925162005", sha256: "f5f5d22e4fdbc83e879f22c61dd0ee4a7fd4ffa78b153c03b0b65d7fd9a35639", wayback_url: "https://web.archive.org/web/20040925162005/http://www.toolkitzone.com/forums/viewtopic.php?p=76929&amp="}
links:
  - {url: "http://dontemailmeanycrap.com/avatar.gif", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v325/brent329/sw018.gif", status: "external", local: null}
  - {url: "http://img85.exs.cx/img85/3596/Niloc.gif", status: "external", local: null}
  - {url: "http://overkill2013.geahost.com/Anti-Everything.png", status: "external", local: null}
  - {url: "http://thanian-nation.com/oy/asimir.jpg", status: "external", local: null}
  - {url: "http://www.geocities.com/joshryu", status: "external", local: null}
  - {url: "http://www.geocities.com/joshryu/beowulf_trogdor.jpg", status: "external", local: null}
  - {url: "http://www.toolkitzone.com/games.php?game=482", status: "never-captured", local: null}
---

# I need an explanation on how to make NPC's

### vUnit321 · 2004-08-15 16:52 · #B75909

Okay, I've been trying for several days to make an NPC.
I've already made the NPC sprite (graphics). But I don't know how to put it in the game. Should I put it in as a tile? How would I make the NPC Conversation when my character goes up to it and press the Talk key (Presetted) or something.
_________________
[Initial D Midnight Showdown](http://www.toolkitzone.com/games.php?game=482)
- Overall 4%
- RPGCode 6%
- Storyline 1%
- Sprites/Gfx 7%
- Sounds/Music 5%
- Map/Board 2%

### sims116 · 2004-08-15 17:20 · #B75933

you gotta be more presise on what you want to do, no1 will answer this unless you tell them the exact details and try to use rpgcode terms.
_________________
Soul Calibur 2 : "This rod will be your doom!" - Kilik, "Justice will prevail, Just kidding!"- Xianchua, "uhh... your definitly not my type" - Cassandra, "I will show you the greatest nightmare!" - Nightmare.
hehe! i know most of them of by heart!!!! Very Happy

### bradseguin · 2004-08-15 18:19 · #B75977

READ THE TUTORIAL!!!! READ IT AGAIN!!! THEN READ IT A THIRD TIME!
STUDY IT!!! That should work.
_________________
![](http://thanian-nation.com/oy/asimir.jpg)![](http://img85.exs.cx/img85/3596/Niloc.gif)
[img]
![](http://overkill2013.geahost.com/Anti-Everything.png)
![](http://dontemailmeanycrap.com/avatar.gif)
![](http://img.photobucket.com/albums/v325/brent329/sw018.gif)
Wherever you see the evil monkey on the stairs pointing at you, you know I was there.

### stanleywuu · 2004-08-15 20:05 · #B76038

Um....I think I know what he's trying to say
Make them into items, then put the items on the board
_________________
There is no death, there is force

### khaldore · 2004-08-15 20:42 · #B76076

Here's the basic ideas for making an NPC:
1: Create an item (let's call it dingbat.itm), and give that item the graphics the same way you would for a player character.
2: Open whichever board (let's call that wheee.brd) you want the NPC to be on, and click "RPGCode" in the menu bar above, then choose "Set Item". Click the tile you want the NPC to be at.
3: When you choose to set the item, click the "Advanced" tab, and select the Activation Type "When Player Presses Activation Key Beside Item". Then, place whichever program you want to run when that key is pressed in the box below, labeled "Activation Program".
4: From there, you can either make it run each time, or only once by changing the option in "Activation" at the bottom. Once everything looks the way you want it to look, click "Set Item".
Hopefully that'll help you out some. Smile
_________________
Current Project: Ageless (Demo 1.0)
Completion: 45%
Custom Menu: 45%, on hold
Custom Battle System: Not Started
Characters: 75%

### vUnit321 · 2004-08-15 20:51 · #B76081

ok thanks, i got it working now.
_________________
[Initial D Midnight Showdown](http://www.toolkitzone.com/games.php?game=482)
- Overall 4%
- RPGCode 6%
- Storyline 1%
- Sprites/Gfx 7%
- Sounds/Music 5%
- Map/Board 2%

### Darkswordsman · 2004-08-16 22:33 · #B76734

If you want your non-moving type NPC. Say you have a person tile in your tileset, Put it at where you want the npc to be, Then, Make it solid. then create a program like this:

**Code:**

```
 #Mwin("NPC: HI MY NAME IS MR NPC")

#Wait(a$)

#Mwincls
```

Yeah, Then Set the program on the tile you created earlier on the board, then if yuo step on it. it should shw that message...

### jo_potato · 2004-08-17 03:21 · #B76929

**bradseguin wrote:**

> READ THE TUTORIAL!!!! READ IT AGAIN!!! THEN READ IT A THIRD TIME!
> STUDY IT!!! That should work.
>

yes read the tutorial if u havent but not tat much times. it isnt that helpful
_________________
![](http://www.geocities.com/joshryu/beowulf_trogdor.jpg)
Beowulf vs. Trogdor
~~
Current Projects: SpaceNerds
________________________________________
[www.geocities.com/joshryu](http://www.geocities.com/joshryu)
