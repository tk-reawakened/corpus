---
kind: forum-thread
id: "toolkitzone-forums/24020"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "P90\\'s Coding forum Tuts&source"
skin: "phpbb2"
thread_id: "24020"
title: "Worms armageddon battle system"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=24020"
written: "2005-10-03T05:35:00"
last_post: "2005-10-04T21:20:00"
date_confidence: "exact"
captured: ["20060111131441"]
author: "eclipze"
repliers: ["p90m16mp5a4", "Tao-Kun", "Greg"]
authors: ["eclipze", "p90m16mp5a4", "Tao-Kun", "Greg"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_262415_amp_3Bsid_f2c01a272b36fe85bb1c4aa1247f23ae", captured: "20060111131441", sha256: "e979927969dcdd516705405369f8a605aa0c8099a3590bab8b1795c1600df47e", wayback_url: "https://web.archive.org/web/20060111131441/http://www.toolkitzone.com/forums/viewtopic.php?p=262415&amp%3Bsid=f2c01a272b36fe85bb1c4aa1247f23ae"}
links: []
---

# Worms armageddon battle system

### eclipze · 2005-10-03 05:35 · #B261989

does anyone have or know how to code a worms armageddon battle system with the movement and the turns??

### p90m16mp5a4 · 2005-10-03 07:30 · #B262001

I don't know that game, I'm sure if it's 2d and not an action based game then yes, it's possible to code.

### eclipze · 2005-10-03 08:07 · #B262004

worms armageddon is a side view game, and u have turns, when its ur teams turn you get to move around and try to kill the enemy with weapons.you only get one chance per person in each turn. Once u have all people on ur team finished there turn its the computers turn and they try to kill you, it keaps on going till one of the teams dies
^
^
i want to make a battle system like that

### p90m16mp5a4 · 2005-10-03 09:06 · #B262006

Why dont you stick with learning how to make a basic BS first, then move on.

### eclipze · 2005-10-04 05:51 · #B262225

can u tell me how to attack with a gun with sertain ranges plz?

### Tao-Kun · 2005-10-04 16:52 · #B262325

It is totally possible to make a battle system like that, but why would you want to? The worm games are plain dum, although funny to watch those little fuckers blow each other up. Although a battle system like that is totally simple to make, you will have problems having the camera to go left to right. (Maybe if you created invisble characters and made them move e,w when its that player turn to attack) Lol, I mightcreate something like that when I get home, or atlease, after the expo. But I'm with Bob on this one. Try to create a basic battle system first before moving on.
As for the shooting question, Hmm, get the X and Y of the enemy, then subtract it by the X and Y of the character, then determ if the sum of the two postion is greater then or less then the gun's range. Although, I doubt it would work for a Active time battle game, but for the turn battle systems, it would work; atlease, I think so.

### Greg · 2005-10-04 21:20 · #B262415

I suppose a cheaper scaled down version of the battle system could be possible, but the TK is too slow for many of the graphical effects in Worms and it's almost impossible to make destructable terrain like in Worms.
As I said, it'd probably be slow!
