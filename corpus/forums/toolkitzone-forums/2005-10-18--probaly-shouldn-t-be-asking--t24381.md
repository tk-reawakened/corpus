---
kind: forum-thread
id: "toolkitzone-forums/24381"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "24381"
title: "Probaly shouldn't be asking....."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=24381"
written: "2005-10-18T02:09:00"
last_post: "2005-10-18T21:14:00"
date_confidence: "exact"
captured: ["20060110160946"]
author: "TOPLIZARDS8"
repliers: ["Dont_Think_So", "p90m16mp5a4"]
authors: ["TOPLIZARDS8", "Dont_Think_So", "p90m16mp5a4"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_265178_amp_3Bsid_b4534c849086ea60f22aa5790d1e69a7", captured: "20060110160946", sha256: "420f9caa6772d3fbc3a256b5ed62f74ec67b579f3b394d6a640d7440615d7f9b", wayback_url: "https://web.archive.org/web/20060110160946/http://toolkitzone.com/forums/viewtopic.php?p=265178&amp%3Bsid=b4534c849086ea60f22aa5790d1e69a7"}
links: []
---

# Probaly shouldn't be asking.....

### TOPLIZARDS8 · 2005-10-18 02:09 · #B265166

I am sorry if this is in the tutorial/command reference but how do you get player location and item location? After you get these locations how do you see if they have the same location?
Thanks and sorry in advance!

### Dont_Think_So · 2005-10-18 02:25 · #B265170

**RPGCode Function Reference wrote:**

> NAME: Item Location
> FORMAT: itemLocation(item_num!, x!, y!, layer!)
> This command locates a specific item on the board.
> - item_num! is a numerical value for which item you wish to find.
> - x!,y!,layer! are the x, y, and layer coordinates returned as the location.
> createItem("man.itm", itmMan!)
>

**RPGCode Language Features wrote:**

> playerX[x!]!  the x! coordinate of the players on your team. x! is a value between 0 and 4.
> playerY[x!]!  the y! coordinate of the players on your team. y! is a value between 0 and 4.
>

Wink

### TOPLIZARDS8 · 2005-10-18 02:46 · #B265178

Sad I just can't figure this out! Even with the info you gave me! Very Happy Anyways if anyone could would they write me a program so that if you are at the same location as a ball you can kick it in any direction by pushing the item 2 times in whatever direction. Or that you can shoot by pushing the ball E 6 times.
Very Happy I don't know if I should move this to the job section. If anyone thinks so just tell me and I'll edit this Laughing

### p90m16mp5a4 · 2005-10-18 21:14 · #B265361

Flip on over to Version3, it will work then.
