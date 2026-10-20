---
kind: forum-thread
id: "toolkitzone-forums/12561"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12561"
title: "Cut-scene at beginning... How the hell?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12561"
written: "2004-12-13T16:59:00"
last_post: "2004-12-13T20:39:00"
date_confidence: "exact"
captured: ["20041228072358"]
author: "Village Idiot"
repliers: ["Levi"]
authors: ["Village Idiot", "Levi"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139096_amp_", captured: "20041228072358", sha256: "accda39118441cc5a74fae4f9ae84a24bb0cd1b1b0f7cf23f87a283b5f1b5161", wayback_url: "https://web.archive.org/web/20041228072358/http://www.toolkitzone.com/forums/viewtopic.php?p=139096&amp="}
links: []
---

# Cut-scene at beginning... How the hell?

### Village Idiot · 2004-12-13 16:59 · #B139063

I've been trying to figure this out for a long time now, but being new at rpgcode, it's a bit difficult. It's different from Visual Basic, the first programming language I learned. Anyway, I can't figure out how to go straight from the startup program to a scene without allowing the player to move on the board first. My first idea was to surround the player with the program, and when he or she steps on it, run it and deactivate all of the other ones... but that doesn't work for a character who's supposed to be waking up. I also need to know how to set enemies on the board and erase them after they've been dealt with... do you make them Items and include a #FightEnemy command upon pickup? Help me out here, people.

### Levi · 2004-12-13 19:18 · #B139087

For the first one in your main file thing. remove the start up board. You can then load a board with the character without loading out of the program. Effectivley keeping control until you release it.
For the enemies you create items with the enemies graphics. Like you would NPC's. Then have a varaible array that holds whether or not the characters exist on that board. When you run into each item the item's program will start a battle. And at the end of the battle will remove the character from the array before redrawing them.
I hope that helps, I'm not good at explaining myself.

### Village Idiot · 2004-12-13 20:39 · #B139096

Alright. i shall try that, then. Thanks a lot.
