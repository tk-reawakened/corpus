---
kind: forum-thread
id: "toolkitzone-forums/12553"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "12553"
title: "Items Versus Characters"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12553"
written: "2004-12-13T05:24:00"
last_post: "2004-12-15T03:40:00"
date_confidence: "exact"
captured: ["20050119211843"]
author: "Serge"
repliers: ["matt72186", "Ross L.", "Alex0Xander", "Guest", "stanleywuu", "Dont_Think_So"]
authors: ["Serge", "matt72186", "Ross L.", "Alex0Xander", "Guest", "stanleywuu", "Dont_Think_So"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139971_amp_", captured: "20050119211843", sha256: "773a16ee37fb1473cf1c680b793de2012c138103a222ec26e915861b1b6e75be", wayback_url: "https://web.archive.org/web/20050119211843/http://www.toolkitzone.com/forums/viewtopic.php?p=139971&amp="}
links: []
---

# Items Versus Characters

### Serge · 2004-12-13 05:24 · #B138957

It seems to me that there should be little difference in the TK when dealing with characters compared to dealing with items (NPCs).
Instead of having to use .chr format for characters, and .itm format for items, it should all be the same as .itm. They should all be universal, generic objects, edited in the same editor. It makes more sense to me, anyway. Then instead of having set HP/MP/defense/whatever for the character, just allow people to set certain variables relating to the item that can either be global, or limited to if that item is on a board (have a little check box to make it global). Then we wouldn't need the silly DestroyPlayer() etc.., we could just use functions dealing with items. Maybe set up 5 or whatever number the player specifies of "reserved" item slots for each board, for players.
Anyway, these are just a few ideas of how to do it, maybe they aren't very good, but I think the point is that it is something that should be done.

### matt72186 · 2004-12-13 05:43 · #B138967

Yeah I like your suggestion, it would be even better if TK Components were object-ized in RPG Code, so each object (item/player) on the current board can be referenced as a Sprite object in the board's Sprite Array
Board->Sprite[0]->Destroy()

### Ross L. · 2004-12-13 10:56 · #B139001

A great suggestion. This is less confusing to the average new user also, and we like User Friendlyness. Very Happy

### Alex0Xander · 2004-12-13 14:00 · #B139022

I like the idea. Go-go super Dev team!

### Guest · 2004-12-13 23:27 · #B139165

While your at it, combine the format with enemies as well, since they now can use the same kinds of animations and even stances.

### stanleywuu · 2004-12-13 23:37 · #B139175

But if each item is reserved for a lot of variables, would that make everything go slower or even worse have memory problems?

### Dont_Think_So · 2004-12-13 23:40 · #B139181

Everything is stored in memory anyway...

### Serge · 2004-12-15 03:40 · #B139971

**Quote:**

> While your at it, combine the format with enemies as well, since they now can use the same kinds of animations and even stances.
>

Ah yes, thanks for adding that. I think it would be good if all such things were combined into one sort of multipurpose, flexible object.
