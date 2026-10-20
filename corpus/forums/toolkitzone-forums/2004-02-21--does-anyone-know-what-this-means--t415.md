---
kind: forum-thread
id: "toolkitzone-forums/415"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "415"
title: "Does Anyone Know What this means?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=415"
written: "2004-02-21T04:56:00"
last_post: "2004-08-18T04:03:00"
date_confidence: "exact"
captured: ["20040928044538"]
author: "Alex0Xander"
repliers: ["KSNiloc", "Danny 666"]
authors: ["Alex0Xander", "KSNiloc", "Danny 666"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_77482_amp_", captured: "20040928044538", sha256: "15c33a8da22801a5519501fcaf0b17d63a97e6ab32b79c0fc6c46dc6e8ac2ae2", wayback_url: "https://web.archive.org/web/20040928044538/http://www.toolkitzone.com/forums/viewtopic.php?p=77482&amp="}
links:
  - {url: "http://thanian-nation.com/oy/asimir.jpg", status: "external", local: null}
---

# Does Anyone Know What this means?

### Alex0Xander · 2004-02-21 04:56 · #B3012

What does this mean?:
A runtime error has occured
Code: 6
Description: Overflow
Im making my battle system and so far all i have is the background go black with #clear
Then a randomization of monsters, then i load those monsters with Mrgs misc #PutEnemy.
Also the monsters dont show up on the screen.

### KSNiloc · 2004-02-21 05:39 · #B3020

In most IDEs "Overflow" refers to a variable being set to high, low, long, or accessing further into an array then was dimmed. Of course it won't be the latter in RPGCode. As for MrG's #PutEnemy, it isn't the best... You'd be better off to move away from RPGToolkit file formats. Make a file called Rat.prg for a rat enemy. In it do something like this...
#Method LoadStats()
{
#hp!=50
#mp!=20
#st!=30
#speed!=20
#dp!=999
}
Then, from your battlesystem and supposing the name of the enemy is in enemy$...
#to_run$="#"+enemy$+".LoadStats"
#RPGCode(to_run$)
Then you'll have that enemy's stats in variables so you could pump them into an array.
_________________
Fin.

### Danny 666 · 2004-08-18 04:03 · #B77482

huh?
_________________
![](http://thanian-nation.com/oy/asimir.jpg)
