---
kind: forum-thread
id: "toolkitzone-forums/6987"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "6987"
title: "I want to get into a fight with ONE enemy"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=6987"
written: "2004-08-11T01:18:00"
last_post: "2004-08-23T16:54:00"
date_confidence: "exact"
captured: ["20040818050402", "20040824064918", "20040925162200"]
author: "zeno"
repliers: ["MrB", "KSNiloc", "Gnarf", "Dont_Think_So", "bushido_EX", "Mark_of_the_Dragon", "trunksbrief39"]
authors: ["zeno", "MrB", "KSNiloc", "Gnarf", "Dont_Think_So", "bushido_EX", "Mark_of_the_Dragon", "trunksbrief39"]
posts_present: 10
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_73033_amp_", captured: "20040818050402", sha256: "b1bb71f5a1b41ec88cc295a9e623a623434c5b7c6627c28109c94df1a9071438", wayback_url: "https://web.archive.org/web/20040818050402/http://www.toolkitzone.com/forums/viewtopic.php?p=73033&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_73063_amp_", captured: "20040824064918", sha256: "c7baeff69a089d2b4b22b9b963f33fa903274c735128fb7aee998945a2ba433e", wayback_url: "https://web.archive.org/web/20040824064918/http://www.toolkitzone.com/forums/viewtopic.php?p=73063&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_76011_amp_", captured: "20040925162200", sha256: "3f12ba9b1e7cac1949cfe20a102aca3df2f22e98322a24b6bc0be45715bf2931", wayback_url: "https://web.archive.org/web/20040925162200/http://www.toolkitzone.com/forums/viewtopic.php?p=76011&amp="}
links:
  - {url: "http://s4.invisionfree.com/Art_Contests/index.php?act=idx", status: "external", local: null}
  - {url: "http://www.geocities.com/midget4d2/home.html", status: "external", local: null}
  - {url: "http://www.mg.geahost.com/rg", status: "external", local: null}
  - {url: "http://www.mg.geahost.com/small_rg.gif", status: "external", local: null}
  - {url: "http://www.mg.geahost.com/tkg", status: "external", local: null}
  - {url: "http://www.mg.geahost.com/tkg/small_tkg.gif", status: "external", local: null}
  - {url: "http://www.mg.geahost.com/tkgforum", status: "external", local: null}
  - {url: "http://www.posergallery.com/wip/20040811-154415.jpg", status: "external", local: null}
  - {url: "http://www.toolkitzone.com/games.php?game=394", status: "captured", local: "wayback/toolkitzone.com/games.php__game_394"}
---

# I want to get into a fight with ONE enemy

### zeno · 2004-08-11 01:18 · #B73000

I want to be able to get into a fight with ONE boss to fight not a random number of bosses...can anyone help?
_________________
I am the best thats all there is to it.

### MrB · 2004-08-11 02:29 · #B73033

I guess you could could make a program to manually pick the enemy, and then just use #fight or whatever the appropiate command is.
You'd have to say "No" not using the default battle system, and then run the program that picks the enemy.
Doing this would force you to manually pick the enemies for the entire game, but if you always want only one enemy to be picked, then I guess it's worth it.
There may be an easier way though, I'm not too experienced with the default battle system.
_________________
"A man who makes no mistakes usually does not make anything." - E. J. Phelps
[![](http://www.mg.geahost.com/small_rg.gif)](http://www.mg.geahost.com/rg) [![](http://www.mg.geahost.com/tkg/small_tkg.gif)](http://www.mg.geahost.com/tkg)
Relax man. Join the [tkg_gaming forums](http://www.mg.geahost.com/tkgforum).

### KSNiloc · 2004-08-11 03:19 · #B73063

You want the FightEnemy() command, not Fight(), Zeno.
_________________
I xeroxed a mirror - now I have an extra xerox machine.

### Gnarf · 2004-08-11 07:10 · #B73130

#fightenemy lets you select who you want to fight...just type in there file_name$ and bkg$
_________________
-Gnarf-
ED 2oo4
[![](http://www.posergallery.com/wip/20040811-154415.jpg)](http://www.geocities.com/midget4d2/home.html)
[Tales Of A Cleric *UPDATE*](http://www.toolkitzone.com/games.php?game=394)
[Art Contest Forums](http://s4.invisionfree.com/Art_Contests/index.php?act=idx)
Everyone wants a piece of my Gnarf.
In memory of DEXTER....goodbye... Crying or Very sad

### zeno · 2004-08-12 01:03 · #B73640

whenever i use the #fightenemy command it just says "unreconised file format" with my enemys name and stuff...i think that it might be a bug
_________________
I am the best thats all there is to it.

### Gnarf · 2004-08-12 01:10 · #B73648

unrecognised file format means you put in a wrong fielname that you dont have...
Here is an example...
#fightenemy("mole.ene","mybackground.bkg")
And they HAVE to be files in YOUR game... Very Happy
_________________
-Gnarf-
ED 2oo4
[![](http://www.posergallery.com/wip/20040811-154415.jpg)](http://www.geocities.com/midget4d2/home.html)
[Tales Of A Cleric *UPDATE*](http://www.toolkitzone.com/games.php?game=394)
[Art Contest Forums](http://s4.invisionfree.com/Art_Contests/index.php?act=idx)
Everyone wants a piece of my Gnarf.
In memory of DEXTER....goodbye... Crying or Very sad

### Dont_Think_So · 2004-08-12 04:32 · #B73787

Also, you don't need to disable fighting altogether; you could just disable fighting for the board, or have it an activated program.
_________________
"I am all but nothing." -Dont_Think_So
"I have succeded in all but one thing - failure" -Dont_Think_So
Obey Dont_Think_So! Obey! If you can read this, then you have internet explorer. Get Firefox now!

### bushido_EX · 2004-08-15 19:23 · #B76011

Wait, but to do that is it still necessary to disable default battle and choose the enemies for every battle in the game?
*ex
_________________
Yatta!!

### Mark_of_the_Dragon · 2004-08-18 15:29 · #B77646

No. It is not.
_________________
Never meddle in the affairs of dragons for you are crunchy and taste good with ketchup...
Message to you all: Read the help files before you ask questions; most questions can be answered. Also, make a game using default systems first; that will put you in a better position to make everythign on your own. You think xorlak relied on MrG for everything? No.

### trunksbrief39 · 2004-08-23 16:54 · #B80174

Fightenemy works perfect for me...
_________________
"Fear of living on, natives getting restless now! Mutiny in the air! Got some death to do! Mirror stares back hard, kill is such a friendly word! It seems the only way, for reaching out again!" - Metallica "Welcome Home (Sanitarium)"
