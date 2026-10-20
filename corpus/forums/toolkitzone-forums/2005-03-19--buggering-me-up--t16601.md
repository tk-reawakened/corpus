---
kind: forum-thread
id: "toolkitzone-forums/16601"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "16601"
title: "Buggering me up"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=16601"
written: "2005-03-19T15:16:00"
last_post: "2005-03-21T18:03:00"
date_confidence: "exact"
captured: ["20050326002825"]
author: "TK Apprentice"
repliers: ["Delano"]
authors: ["TK Apprentice", "Delano"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_182866_amp_", captured: "20050326002825", sha256: "63431e6f7e35d597772d6f1da9ff201a33a68a0c8062c8c9276d9b9ec2d251fb", wayback_url: "https://web.archive.org/web/20050326002825/http://toolkitzone.com/forums/viewtopic.php?p=182866&amp="}
links: []
---

# Buggering me up

### TK Apprentice · 2005-03-19 15:16 · #B182668

The toolkit is screwing me right up with tons of new bugs I'm getting.
For reference I am running Xp pro with sp2 and the latest dev build.
numero uno: When the screen scrolls up and down every tile on every board goes a few shades darker.
2: Character some times jams when moving for abour 0.5 seconds when moving, it seems to be random when it happens. No random battles to cause the problem.
3: On a board with animated tile after again a random time I am getting a 'application error' 'reference memory could not be read' I have random battles enabled so I think that could be the problem. I know you habe plugin probs so this backs it up.(tk3 battle sys plug)
4: When Item is added to board it is added to a random slot instead of the next abailable one( board is empty apart from grass tiles and item - no multitask and character.)
5: When I first looked at item list it gave slot options 0-4 when looking back later it said slot 0-13
6: When trying to use the activation prog on an item it wont work.
Should keep you busy, Have fun.

### Delano · 2005-03-19 22:45 · #B182824

Things seem to be getting worse and worse, hey?
1) Ambient variables maybe?
2) This is the redrawing of large boards, and not something we're addressing at the moment.
3) If it only happens on boards with anim tiles, then it's probably the anim tiles, not the battle system.
4,5) Yeah, it's messed up.
6) It works for me.

### TK Apprentice · 2005-03-20 01:46 · #B182866

1: ambiant variables, anything I can do about them or is it a sys bug?
3: removed the anim tiles, its the bs alright
4,5: did you know about these already? any plan for a fix in 3.06?
6: I'm not sure but I had ticked the board driven box without putting anything in it, would that have overridden the board set activation prog?
How about tabs loading slowly when switching between them?

### Delano · 2005-03-20 16:42 · #B183076

1) "Ambient variables" as in - are you using them anywhere? These are the things that change the lightness of the board.
3) So it only happens with random battles?
4,5) I thought Colin had looked into it.
6) No that shouldn't override it. Do you have an activation key assigned in the main file?

### TK Apprentice · 2005-03-20 23:17 · #B183246

1: No I'm not using them
3: sorry, ignore this one. for some reason the toolkit removed the enemys from their slots which caused the error
4,5: I had a look on the bug list, I can't see it mentioned
6: No activation keys set. There was a sound set to the items walking animation but I can't see how that would affect it.

### Delano · 2005-03-21 12:22 · #B183446

**TK Apprentice wrote:**

> 6: No activation keys set. There was a sound set to the items walking animation but I can't see how that would affect it.
>

... If there's no general activation key set, then how do you mean to activate the item?

### TK Apprentice · 2005-03-21 18:03 · #B183568

mybad, yes I have space bar set as the activation key
