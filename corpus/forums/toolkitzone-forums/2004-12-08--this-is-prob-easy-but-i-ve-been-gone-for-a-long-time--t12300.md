---
kind: forum-thread
id: "toolkitzone-forums/12300"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12300"
title: "This is prob easy, but I've been gone for a long time..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12300"
written: "2004-12-08T01:59:00"
last_post: "2004-12-11T01:21:00"
date_confidence: "exact"
captured: ["20041227215343"]
author: "GStick"
repliers: ["Mystinar", "Levi", "TheCPPFreak220"]
authors: ["GStick", "Mystinar", "Levi", "TheCPPFreak220"]
posts_present: 9
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_137767_amp_", captured: "20041227215343", sha256: "68fdde7c96393e8656fa766b0fcbe4b2369c764522d0d6d28c0859495ca5ebc1", wayback_url: "https://web.archive.org/web/20041227215343/http://www.toolkitzone.com/forums/viewtopic.php?p=137767&amp="}
links: []
---

# This is prob easy, but I've been gone for a long time...

### GStick · 2004-12-08 01:59 · #B136300

Ok, most of you prob don't remember me, but I left when TK 3 was in it's Beta and stuff, but I'm back, and I don't remember how to increase the player's FP and DP, I figured out the HP and SMP, but I still can't figure out FP and DP. But like I said, this is prob really easy, I just can't remember...
Thanks in advance

### Mystinar · 2004-12-08 02:05 · #B136305

Ahem:
PlayerFP! + x!

### Levi · 2004-12-08 02:06 · #B136306

Is everyone's RPGCode getting erased around here or what?

### GStick · 2004-12-08 14:06 · #B136455

I couldn't get it to work, yea, I think my RPG Code is getting erased, a lot, ok, here's my code:

**rpgcode:**

```
MWin("Used Stat Seed!")

Wait()

MWinCls()

handle$ = TargetHandle()

old_MaxHP! = GetMaxHP("handle$")

MaxHP("handle$", old_MaxHP!+2)

old_MaxSMP! = GetMaxSMP("handle$")

MWin("HP increased by 2!")

Wait()

MWinCls()

MWin("FP increased by 2!")

Wait()

MWinCls()

MWin("DP increased by 2!")

Wait()

MWinCls()

MWin("SMP increased by 2!")

Wait()

MWinCls()
```

What happens is, all the Message Windows appear ok, but after the item is used, it isn't removed from the inventory like the other items that have similar code, and it doesn't increase any of the player's stats. I want it to increase the stats of the player that is using the item. Thanks.
EDIT: o yea, the empty spots in the code are where I put in Mystinars code, but for FP and DP.

### TheCPPFreak220 · 2004-12-08 20:21 · #B136565

**Code:**

```
MWin("Used Stat Seed!")

Wait()

MWinCls()

handle$ = TargetHandle()

old_MaxHP! = GetMaxHP(handle$)

MaxHP(handle$, old_MaxHP!+2)

old_MaxSMP! = GetMaxSMP(handle$)

MWin("HP increased by 2!")

Wait()

MWinCls()

MWin("FP increased by 2!")

Wait()

MWinCls()

MWin("DP increased by 2!")

Wait()

MWinCls()

MWin("SMP increased by 2!")

Wait()

MWinCls()
```

### GStick · 2004-12-08 20:59 · #B136586

Thats the same code I have, and it doesn't work right

### TheCPPFreak220 · 2004-12-08 21:10 · #B136593

Nope, i got rid of a few "" 's. You had them around handle$ and they should not of been there.

### GStick · 2004-12-11 01:13 · #B137765

o, ok, thanks, I'll try it

### TheCPPFreak220 · 2004-12-11 01:21 · #B137767

no problem.
