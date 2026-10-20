---
kind: forum-thread
id: "toolkitzone-forums/6794"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions &amp; bugs"
skin: "phpbb2"
thread_id: "6794"
title: "Pusing Dialgonly???"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=6794"
written: "2004-08-06T15:39:00"
last_post: "2004-08-17T18:22:00"
date_confidence: "exact"
captured: ["20040906182002", "20040928044306"]
author: "Master Tamer"
repliers: ["Occasionally_Correct", "The_Anonym0us", "KSNiloc", "Marz", "neiltaco", "Colosseus", "Rueben"]
authors: ["Master Tamer", "Occasionally_Correct", "The_Anonym0us", "KSNiloc", "Marz", "neiltaco", "Colosseus", "Rueben"]
posts_present: 16
pages_present: [1, 2]
pages_total: 2
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_70832_amp_", captured: "20040906182002", sha256: "4c98b75c9381e0c62b2a5c0044a3024a781973486b0f8f08391f1db7f44e3b22", wayback_url: "https://web.archive.org/web/20040906182002/http://www.toolkitzone.com/forums/viewtopic.php?p=70832&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_77166_amp_", captured: "20040928044306", sha256: "b1b965c6a87d2a859ccf47ac9654c45f2153de55aa6faa46725d7c95aecc8b43", wayback_url: "https://web.archive.org/web/20040928044306/http://www.toolkitzone.com/forums/viewtopic.php?p=77166&amp="}
links:
  - {url: "http://darkage.mysticsoftware.net", status: "captured", local: "wayback/mysticsoftware.net/darkage.mysticsoftware.net/index-431440"}
  - {url: "http://www.cywh.com/disc.php?forum=5/", status: "external", local: null}
  - {url: "http://www.geocities.com/tamexplayer/antimastertamer.PNG", status: "external", local: null}
  - {url: "http://www.hilaryduff.com", status: "external", local: null}
  - {url: "http://www.mysticsoftware.net/images/tk_army.png", status: "captured", local: "wayback/mysticsoftware.net/images/tk_army.png"}
  - {url: "http://www.rpgadev.com", status: "external", local: null}
  - {url: "http://www.rpgadev.com/header1.jpg", status: "external", local: null}
  - {url: "http://www.toolkitzone.com/forums/viewtopic.php?t=7888", status: "never-captured", local: null}
  - {url: "http://www.zakap.com/marz/", status: "external", local: null}
---

# Pusing Dialgonly???

### Master Tamer · 2004-08-06 15:39 · #B70817

As you know there is a push command: #push(direction$, handle$)I was thinking how we cant move diagonly? : #push("NW", "handle")
Unlessin you can allready do that in TK3. I never tried it.
_________________
MMORPG creation
[![](http://www.rpgadev.com/header1.jpg)](http://www.rpgadev.com)
[![](http://www.geocities.com/tamexplayer/antimastertamer.PNG)](http://www.hilaryduff.com)

### Occasionally_Correct · 2004-08-06 15:49 · #B70826

You can.

**I wrote:**

> NAME: Push
> FORMAT: #Push(direction$, handle$)
> DESCRIPION: Pushes a player around the screen in the specified directions. For Push to work, the player must be on the board, and they must be in your team at the time. The directions allowed are the following:
> - "N", "NORTH", and "1" all push the player north.
> - "S", "SOUTH", and "2" all push the player south.
> - "E", "EAST", and "3" all push the player east.
> - "W", "WEST", and "4" all push the player west.
> - "NE", "NORTHEAST", and "5" all push the player north-east.
> - "NW", "NORTHWEST", and "6" all push the player north-west.
> - "SE", "SOUTHEAST", and "7" all push the player south-east.
> - "SW", "SOUTHWEST", and "8" all push the player south-west.
> - handle$ is the handle of the player to push.
> By default, the value of handle$ is "Target" which is the player you are currently using. This means that if you leave handle$ out, it pushes the player that you see walking around when you play a game.
> All directions must be inside quotation marks (" ") and must be separated by a comma (,). Different types of directions are allowed to be mixed. This means that you are allowed to have this as the directions: "N, SOUTH, 3, 1, NE, SW".
>
> **Code:**
>
> ```
> PutPlayer("Frap",3,5,1)
>
>
> Mwin("Frap: Hey, watch me walk diagonally.")
>
>
> a$ = Wait()
>
>
> Mwincls()
>
>
> Push("NE,NE,SW,SE", "Frap") *Pushes Frap diagonally
>
>
> Mwin("Frap: Now, I'll walk in a circle!")
>
>
> Wait()
>
>
> Mwincls()
>
>
> Push("S,SE,E,NE,N,NW,W,SW", "Frap")
> ```
>

_________________
:: I'm so tired. Everything seems funny. ::

### Master Tamer · 2004-08-06 16:00 · #B70832

ah. Okay.
_________________
MMORPG creation
[![](http://www.rpgadev.com/header1.jpg)](http://www.rpgadev.com)
[![](http://www.geocities.com/tamexplayer/antimastertamer.PNG)](http://www.hilaryduff.com)

### The_Anonym0us · 2004-08-14 02:41 · #B75055

Something thats been bugging me is whether pathfind will return the directions numerically, or literally. Or can you choose?

### KSNiloc · 2004-08-14 03:33 · #B75081

It returns commas and all. Just use Split() in 3.0.4 to grab the individual directions.
_________________
[Perfection](http://www.toolkitzone.com/forums/viewtopic.php?t=7888)

### Marz · 2004-08-14 03:43 · #B75084

**KSNiloc wrote:**

> It returns commas and all. Just use Split() in 3.0.4 to grab the individual directions.
>

Great, perfect, can I please have 3.04 then? Razz
_________________
[![](http://www.mysticsoftware.net/images/tk_army.png)](http://www.cywh.com/disc.php?forum=5/)
Long live the OT Community!
[TK Centre](http://www.zakap.com/marz/)

### neiltaco · 2004-08-14 06:00 · #B75144

*stabz Marz*

### The_Anonym0us · 2004-08-16 15:42 · #B76543

**KSNiloc wrote:**

> It returns commas and all. Just use Split() in 3.0.4 to grab the individual directions.
>

What I meant was does it return NE,S,W or 9,2,4?

### Occasionally_Correct · 2004-08-16 15:50 · #B76546

**The_Anonym0us wrote:**

>
> **KSNiloc wrote:**
>
> > It returns commas and all. Just use Split() in 3.0.4 to grab the individual directions.
> >
>
> What I meant was does it return NE,S,W or 9,2,4?
>

It should return "NE,S,W,SW,N,NE", etc..
_________________
:: I'm so tired. Everything seems funny. ::

### KSNiloc · 2004-08-16 22:04 · #B76719

"a$ = Wait() "
What garbage is this?
Is you're not using a, don't create it, please.
_________________
[Perfection](http://www.toolkitzone.com/forums/viewtopic.php?t=7888)

### Occasionally_Correct · 2004-08-17 06:56 · #B76994

I see no reason to pick on me for using something you deem unfit. Besides, I don't see you ratting on CBM for using Wait(a$) in every example in the old help files, when he could have used Wait(). Wink
However, I've used the nifty find/replace feature of WordPad to get rid of unneeded return variables for Wait(), just for you. Smile
_________________
:: I'm so tired. Everything seems funny. ::

### Colosseus · 2004-08-17 09:52 · #B77027

After all, you don't save THAT much memory by cutting off some return variables.

### Rueben · 2004-08-17 17:29 · #B77142

I think using a$ as thee default wait variable (as I've done for years) just seems to fit. No idea why.
_________________
David "Rueben" Smith
Author/Creator - The Fourth Dimension
Music Composer - [Dark Age 2 & Dark Age EX](http://darkage.mysticsoftware.net)

### Occasionally_Correct · 2004-08-17 17:31 · #B77145

**Rueben wrote:**

> I think using a$ as thee default wait variable (as I've done for years) just seems to fit. No idea why.
>

It's probably because it's an easy referal that you most likely won't be using for anything else. Razz
_________________
:: I'm so tired. Everything seems funny. ::

### KSNiloc · 2004-08-17 18:09 · #B77162

When CBM write the help files, you couldn't go Wait(). That, my friend, is why. Wink
_________________
[Perfection](http://www.toolkitzone.com/forums/viewtopic.php?t=7888)

### Occasionally_Correct · 2004-08-17 18:22 · #B77166

**KSNiloc wrote:**

> When CBM write the help files, you couldn't go Wait(). That, my friend, is why. Wink
>

And I took that into consideration. It wouldn't have taken him long to change that, however.
Aside, it's not yours to judge. You can write your own help files if you want to. As for me, I think I'll write what I please, thank you. Smile
_________________
:: it's better in the matinee, the dark of the matinee ::
