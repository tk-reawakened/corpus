---
kind: forum-thread
id: "toolkitzone-forums/16366"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "editor help"
skin: "phpbb2"
thread_id: "16366"
title: "Enemy Questions"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=16366"
written: "2005-03-14T01:00:00"
last_post: "2005-03-16T00:41:00"
date_confidence: "exact"
captured: ["20050317184911"]
author: "War Torn"
repliers: ["spitfire", "Juggernaut", "Flytier16"]
authors: ["War Torn", "spitfire", "Juggernaut", "Flytier16"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_180197_amp_", captured: "20050317184911", sha256: "ed9cc3017209d9366668b9d44ef9431d20f5b94f7ddfcc6431f91fb985151dbc", wayback_url: "https://web.archive.org/web/20050317184911/http://www.toolkitzone.com/forums/viewtopic.php?p=180197&amp="}
links: []
---

# Enemy Questions

### War Torn · 2005-03-14 01:00 · #B180196

If I have a monster that has 12 parts how do I make it a One part (whole) monster scheduled battle, after the player defeats it it dissappears. Also How do I make the Tiles behind it show? Please reply back asap.

### spitfire · 2005-03-14 01:02 · #B180197

Please explain more clearly.

### War Torn · 2005-03-15 03:31 · #B180714

Well what I mean is, it is a 12 tile monster, How do I make it whole for animation, dissappear after one battle, and show the floor tiles behind it?

### Juggernaut · 2005-03-15 15:13 · #B180856

In the animation editor, in the bottom left is a button that says 'create tile bitmap". If you click that, you can make images for an animation out of tiles to about any size you want.

### Flytier16 · 2005-03-15 23:29 · #B180957

Hay i have made 12 block monsters and the backround have shown on mine so there must be a problem with you system?(Just thinking)

**Quote:**

> If I have a monster that has 12 parts how do I make it a One part (whole) monster scheduled battle, after the player defeats it it dissappears. Also How do I make the Tiles behind it show? Please reply back asap.
>

Can't understand very well plz next time speak in a real sentence.
(Good use real words in the right places)
FLY Very Happy

**Code:**

```
#Addplayer("Flytier16.tem")

#Mwin("I like to be in someones game that would be kick ass.")

#System.pause

#Mwincls()

#done=0

#While(done!==0)

{

#Mwin("Press:")

#Mwin("1-let flytier join")

#Mwin("2-Be gay and dont")

#Mwin("3-just stand there")

#System.pause

#If(Key$==1)

{

#Mwin("Dude you game ROXS!!!!!")

#System.pause

}

#If(Key$==2)

}

#Mwin("THis is one of the dumbest games ever!")

#System.pause

}

#If(Key$==3)

{

#Mwin("dude only retards stand there")

#System.pause

#End()

}
```

### War Torn · 2005-03-16 00:41 · #B181005

another problem, when I set warp tiles to different levels of a board and test it (walking onto it with my character) it freezes. Any ideas/checklists I need to find the problem?
