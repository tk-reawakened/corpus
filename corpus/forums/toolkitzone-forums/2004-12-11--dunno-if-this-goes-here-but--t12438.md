---
kind: forum-thread
id: "toolkitzone-forums/12438"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12438"
title: "Dunno if this goes here, but..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12438"
written: "2004-12-11T04:07:00"
last_post: "2004-12-12T03:12:00"
date_confidence: "exact"
captured: ["20041227215136"]
author: "khaldore"
repliers: ["p90m16mp5a4", "Digitaly Impaired", "Akura_TheDragonBlader", "Occasionally_Correct"]
authors: ["khaldore", "p90m16mp5a4", "Digitaly Impaired", "Akura_TheDragonBlader", "Occasionally_Correct"]
posts_present: 9
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_138303_amp_", captured: "20041227215136", sha256: "d4e59b885ec1b5cf03b1d2da47c7db1e084164046bae10c246ef13cd47be0c41", wayback_url: "https://web.archive.org/web/20041227215136/http://www.toolkitzone.com/forums/viewtopic.php?p=138303&amp="}
links: []
---

# Dunno if this goes here, but...

### khaldore · 2004-12-11 04:07 · #B137865

I couldn't think of anywhere else to put it, since (to an extent) it does deal with RPGCode. Anyhow... I've got several problems and questions I'm gonna toss out here.
1) My custom menu... I'm doing some extensive recoding, and it's going well so far, except for this: I'm still unsure if you can access a character's abilities, equipment, or items without using the default menu system. Now, I know MrG's plug has commands that allow you to access those areas via RPGCode (like the GetEquip command), but it seems to be incompatible with TK3. There's also a plug (BP's, I believe) that allows you to access the callbacks in RPGCode (which would solve this problem), but that doesn't seem to like TK3 either. So I'm kind of stuck... which leads me to my next question:
2) Python... plain and simple. Can it be used in any way, shape, or form with the TK? I'm still not too familiar with the language, but if it can be used to add functionality within my game, I'd like to give it a shot. *shrugs*
Anyhow, if anyone has a solution, flames, general blabber, just post away... at this point I need all the help I can get. Sad
Mike

### p90m16mp5a4 · 2004-12-11 04:18 · #B137869

Yes you can access them.. although I'm afraid the commands slip my mind. :-0. I have seen them before. However, custom menus normally come with custom STATS. I would try downloading some menu builders and look for the commands in there, but I'm sure someone will post them. If they aren't commands they are variables wich you can SHOW or use #mwin on. Like hp,
#gethp("urCHAR", menuhp!)
#text(12,11, menuhp!)
or something like that.

### khaldore · 2004-12-11 16:32 · #B138013

*nods* Well, with the exception of the following:
Equipment
Items
Abilities
I've been able to design the menu in such a way that the proper XP, HP, SMP, etc., values show up. I'll paste a bit of code in here to explain...

**Code:**

```
PixelText(tx1!, 20, "Khaldore")

PixelText(tx2!, 20, "Level: <Khaldore[level]!>")

PixelText(tx1!, 50, "Life: <Khaldore[hp]!>/Khaldore[maxhp]!>")

PixelText(tx2!, 50, "XP: <Khaldore[exp]!>/<kxp!>")

PixelText(tx1!, 80, "Mana: <Khaldore[smp]!>/<Khaldore[maxsmp]!>")

PixelText(tx2!, 80, "Atk/Def: <Khaldore[fp]!>/<Khaldore[dp]!>")
```

As you can see, most of the variables I use are ones I've set in the character editors, with the exception of kxp!, which I set via another method I wrote. That segment of things (thankfully) isn't where my troubles lie... but I'll take a look at some of the other custom menus here and at MS, maybe I'll find some inspiration for a workaround. Smile
Mike

### p90m16mp5a4 · 2004-12-11 23:51 · #B138204

Use internal menu, if you want to use the built in item system ( not custom item equiption and whatnot) it saves tons of time using regular items.
(notice i said WANT, i'm not your god, i'm just giving opinions )
#InternalMenu( 0 )
- Pops up an internal menu (0- main, 1-item, 2-equip, 3-details, 4-abilities)

### Digitaly Impaired · 2004-12-12 01:34 · #B138245

For the Equip part, You could store the weopons names with arrays:
Sword[num!] = Rapier
num! = num! + 1

### Akura_TheDragonBlader · 2004-12-12 01:34 · #B138246

**p90m16mp5a4 wrote:**

> Use internal menu, if you want to use the built in item system ( not custom item equiption and whatnot) it saves tons of time using regular items.
>

He said he doesn't. And, unfortunately, you really can't get equipment/items/abilities without either plugins, or a somewhat extensive system of coding. The latter can be done if you use the various programs(equipping programs, level up programs, etc.) to track the data, so it is possible with plugins.

### p90m16mp5a4 · 2004-12-12 03:00 · #B138296

i'm making that "extensive" system of coding...
my engine ( engine inside of tk engine ) should be done around March.. I'm ganna post my work when I have stuff that's actually usable. (blog or submit it)

### Occasionally_Correct · 2004-12-12 03:10 · #B138301

**khaldore wrote:**

> Now, I know MrG's plug has commands that allow you to access those areas via RPGCode (like the GetEquip command), but it seems to be incompatible with TK3. There's also a plug (BP's, I believe) that allows you to access the callbacks in RPGCode (which would solve this problem), but that doesn't seem to like TK3 either.
>

If you'd like, I can make you a plugin that works with TK3 that does what you need (most likely, anyway). PM me with the details. I'm feeling generous. Razz

**Quote:**

> 2) Python... plain and simple. Can it be used in any way, shape, or form with the TK? I'm still not too familiar with the language, but if it can be used to add functionality within my game, I'd like to give it a shot. *shrugs*
>

Not without a Python SDK of some sort. To my knowledge, there are only C++ and VB SDK's for TK3 (and I think someone made a Delphi SDK for TK2. I can't remember, though).

### p90m16mp5a4 · 2004-12-12 03:12 · #B138303

dude you f**ging rock!
ud
that would make alot of peoples non-custom stats dream come true!
-yes delphi was for tk2
