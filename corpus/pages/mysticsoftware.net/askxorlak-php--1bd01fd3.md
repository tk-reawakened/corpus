---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/askxorlak.php?mode=1&question=8"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://mysticsoftware.net/askxorlak.php?mode=1&question=8"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040505102854"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/askxorlak.php__mode_1_question_8", captured: "20040505102854", sha256: "ca10a6ab881af6e4f4acd80430e9e9138b410a36ad6553b1cb1a3c4b74107d1a", wayback_url: "https://web.archive.org/web/20040505102854/http://mysticsoftware.net/askxorlak.php?mode=1&question=8"}
---

# Mystic Software

How do realtime battle systems work?
The enemies of realtime battle systems don't wait for you to make choices before attacking. So the main battle loop is usually going to look somewhat like this: #while(battleover!=0) { #get(a$) #playerturn #enemyturn } The #get function works just like #wait, only if a key isn't being pressed at the time it will just set a$="" (nothing). The method #playerturn can then check the value of this variable and update what the player is doing accordingly (i.e. in an "Area" BS, move the player or thrust a sword; in a menu based realtime battle, perhaps move a cursor or confirm a command). Then the enemy gets a chance to update its state in the #enemyturn method and the cycle repeats. Of course there is much more to a battle system than this, but that covers the very basics. See MrG's for an example of an area based realtime system.
[Zelda Battle](files/zelda2.zip)
