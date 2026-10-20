---
kind: forum-thread
id: "toolkitzone-forums/11793"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "11793"
title: "Character Animation Question"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11793"
written: "2004-11-26T17:43:00"
last_post: "2004-11-29T05:01:00"
date_confidence: "exact"
captured: ["20050112162115"]
author: "forsaken"
repliers: ["Moo Of Doom", "Bad Kids", "Avathar", "matt72186"]
authors: ["forsaken", "Moo Of Doom", "Bad Kids", "Avathar", "matt72186"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_131479_amp_", captured: "20050112162115", sha256: "4e8edbbfcaff9f8034ef1b7581642f0faf4dc4045ded0132a6a06581f7d6baf1", wayback_url: "https://web.archive.org/web/20050112162115/http://www.toolkitzone.com/forums/viewtopic.php?p=131479&amp="}
links: []
---

# Character Animation Question

### forsaken · 2004-11-26 17:43 · #B130490

is it possible to make it so your characters graphics change later on in the game. Lets say if your carrer is to become a mage and you have certain graphics and then you hit level 10 for example. You make his graphics change to a different sprite.

### Moo Of Doom · 2004-11-26 19:14 · #B130515

#Newplyr("Lvl10mage.tem")
That just changes the walking graphics. I think you'd need to have a custom level up prog though...

### forsaken · 2004-11-26 20:28 · #B130528

got it working thx

### Bad Kids · 2004-11-27 01:19 · #B130672

uh and this is beginer code not advance, and you don't need a custom level. You just need a prg called levelmanager or something and have whole bunch of if commonds like this;

**rpgcode:**

```
If(level = 10)

{

//whatever here. like change graphic.

}
```

Easy stuff.

### Avathar · 2004-11-29 04:29 · #B131462

damn you all! I knew that one! lol
edit: I can still help!
getlevel("CharacterName",dest!)
if(dest!== 10)
{
newplyr("NewFileName.tem")
}
Something like that. You might have to use exp instead of level, i would have to screw around with it a little.

### matt72186 · 2004-11-29 04:43 · #B131466

Here's a better way to accomplish this (although what everyone else says works)
In start.prg:
PGraphic[10]$ = "newimageforlevel10.tem"
PGraphic[50]$ = "newimageforlevel50.tem"
and for levelup.prg:
playerLevel! = GetLevel(playerHandle[0]$)
if(pGraphic[playerLevel!]$ ~= "")
{
NewPlyr(pGraphic[playerLevel!]$)
}

### Avathar · 2004-11-29 05:01 · #B131479

yah, thats pretty good... lol
