---
kind: forum-thread
id: "toolkitzone-forums/12558"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "12558"
title: "Leveling up enemys"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12558"
written: "2004-12-13T15:36:00"
last_post: "2004-12-21T01:00:00"
date_confidence: "exact"
captured: ["20050119034219"]
author: "prowlor"
repliers: ["Dont_Think_So", "Akura_TheDragonBlader", "p90m16mp5a4", "Alex0Xander", "matt72186", "nOObified"]
authors: ["prowlor", "Dont_Think_So", "Akura_TheDragonBlader", "p90m16mp5a4", "Alex0Xander", "matt72186", "nOObified"]
posts_present: 9
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139498_amp_", captured: "20050119034219", sha256: "73b2fe2eaa065e16ad7df3029f40b13a1419edb7211b0a3639f7e9262da2555e", wayback_url: "https://web.archive.org/web/20050119034219/http://www.toolkitzone.com/forums/viewtopic.php?p=139498&amp="}
links: []
---

# Leveling up enemys

### prowlor · 2004-12-13 15:36 · #B139040

I want to make a system where the enemys level up when you do, so your not taking down the enemys in a single hit. is there a method/peice of code in RPGC i could use to accomplish this?

### Dont_Think_So · 2004-12-13 23:20 · #B139161

Why make the player level up at all if the increased numbers have the exact same effect?

### Akura_TheDragonBlader · 2004-12-13 23:33 · #B139171

Go custom. Or you could make serveral copies of each enemy, and have a battle program run the default with a skill level based on some insane calculation of your levels. Custom is better though.

### prowlor · 2004-12-14 14:45 · #B139498

in response to Dont_Think_So: its because the game only features one island for which to level up on, and those enemys will level up to give you the ammount of EXP you would need as well as a chalange. But there are bosses that wont level up, and you would need to level up to be able to defeat them.

### p90m16mp5a4 · 2004-12-15 23:22 · #B140312

EDIT:
blah balh i suck at this.
edit#2:
I really cant for the life of me get the enemies fp or dp stats changed, just add more health to your characters and really strong special moves. change the default ai to custom ( would you rather program ai or an entire battle system? ) possibly, if you set the enemies skill high enough, it might have common sense to just use spc attacks instead of fight attacks. I don't know, haven't tried.
I would be waiting to give specific assistance, or helping in any possible way that i could. ( however much that would help.. )
-signed a truly gloomy p90
-oh i forgot i already have a signature
-...

### Alex0Xander · 2004-12-16 00:28 · #B140342

**Dont_Think_So wrote:**

> Why make the player level up at all if the increased numbers have the exact same effect?
>

I think he emans at intervals. Like if the player is Levels 10-20, all mosnters in the area will become stronger, that way the player does not breeze through the level.
Custom stats and custom battle system is the only way i see this happening. Now i dont know much about classes, but this might also be a good place to implement classes(for monster). You would have different levels for every monster, then have your BS check what level the character is and load up the enemies into the BS accordingly.

### Dont_Think_So · 2004-12-16 01:32 · #B140378

Or, of course, MrG's Misc Plugin and his fancy la-dee-da GetFP and GetDP commands.

### matt72186 · 2004-12-16 04:17 · #B140465

I have an idea, when the player levels up just don't actually increase the stats, tell the player they levelled up, even show fake better stats in the custom menu, but don't actually let the player level up, because that's pretty much what this idea is accomplishing.

### nOObified · 2004-12-21 01:00 · #B143153

I've always considered the idea of allowing npc's/mobs to level up over time, while within their own ecosystem/habitat - such as, the player character enters their lair and the mobs kills them... mob shouts, "DING." And use an aggregated formula to determine what percent of the population of mob(x) will be at any given level... // add edit: insert here, "initially."
1% of the mobs will be at +200% base level // if base = level 2, then 1% will be at level 6.
10% of the mobs will be at +100% base level // if base = level 2, then 10% will be at level 4.
And then create loot tables that graduate with each tier increment. In the above example, there are three tiers - base, base +100%, base +200%. All those mobs at 6th level can be treated as named or unique or special mobs that drop special items/gear.
