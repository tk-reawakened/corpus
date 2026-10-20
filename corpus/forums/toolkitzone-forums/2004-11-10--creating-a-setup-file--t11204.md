---
kind: forum-thread
id: "toolkitzone-forums/11204"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "11204"
title: "Creating a Setup file"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11204"
written: "2004-11-10T15:25:00"
last_post: "2004-11-11T01:26:00"
date_confidence: "exact"
captured: ["20050110143026"]
author: "prowlor"
repliers: ["Akura_TheDragonBlader", "Colin", "catwhowalksbyhimself"]
authors: ["prowlor", "Akura_TheDragonBlader", "Colin", "catwhowalksbyhimself"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_123678_amp_", captured: "20050110143026", sha256: "d794705ddc8884cde1bdd453e0a8d88cdc8f27ab690bdf12da3a83f7a4dd9b90", wayback_url: "https://web.archive.org/web/20050110143026/http://www.toolkitzone.com/forums/viewtopic.php?p=123678&amp="}
links: []
---

# Creating a Setup file

### prowlor · 2004-11-10 15:25 · #B123399

I want to put my game on a CD, so that I can give to people, but for some reason it installs TK2 on their computer too, and they have access to all my programs and files and stuff... how can I create a Setup file without giving them access to everything?

### Akura_TheDragonBlader · 2004-11-10 20:33 · #B123471

There are several options. First of all, don't give them the TK installer. One thing you can try is using Clickteam's installer program to make a setup .exe and installs Trans3 and your game's files(as well as a shortcut that runs the .gam file through Trans3 to make running the game easy as a double-click). Another thing is to use the Create EXE option from the Toolkit's Build menu, but that is very unreliable. A third option(and probably best) is use the Pakfile manager to make a .tkp and use the first option, only make the shortcut have the pakfile run through Trans3. The only problem with that last one is that it takes a while to load and KSNiloc ripped Gamemaker 6.0's pretty dumb looking loading bar.

### Colin · 2004-11-10 22:39 · #B123564

My EXEs work fine... it's possible not in 3.04, but they use the same code as pakfiles... exactly.
... and I didn't mean to steal that bar Wink

### catwhowalksbyhimself · 2004-11-10 23:01 · #B123581

Actually, I think he is talking about a TK2 game (even though this forum is supposed to be TK3) so option 2 is not possible.

### Akura_TheDragonBlader · 2004-11-11 01:26 · #B123678

**KSNiloc wrote:**

> My EXEs work fine... it's possible not in 3.04, but they use the same code as pakfiles... exactly.
> ... and I didn't mean to steal that bar Wink
>

I kinda figured that, but how would you explain a Pakfile running almost perfectly(well, as good as the TK gets Wink) when an .exe won't even start? Sure... you didn't mean to steal it.
