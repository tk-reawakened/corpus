---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/askxorlak.php?mode=1&question=5"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://mysticsoftware.net/askxorlak.php?mode=1&question=5"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040505102818"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/askxorlak.php__mode_1_question_5", captured: "20040505102818", sha256: "f989b4d9edeb2153f3e713d92859b899dd78d48064e1cbc9b2d54a2270febb78", wayback_url: "https://web.archive.org/web/20040505102818/http://mysticsoftware.net/askxorlak.php?mode=1&question=5"}
---

# Mystic Software

How do I remove an NPC from a board permanently?
If you remove an NPC/item from a board, you'll notice that everything is reset when you leave and come back and the NPC returns. You can sort of get around this with conditional activations, but there is a more reliable method. Don't set the item down in the board editor. Instead set it when the player first enters the board with some RPG Code. In your warp program, do something like this: #send("board.brd",x!,y!,layer!) #if(talkedtoNPC!=0) { #createitem("npc.itm",0) #putitem(0,item_x!,item_y!,item_layer!) } Initially talkedtoNPC! is 0 and the item is set on the board whenever the player enters. Setting #talkedtoNPC!=1 will prevent the item from coming back. Also note you can use this method for making NPCs appear later in the game as well. But wait! If you don't set the item in the board editor, how do you give it run time and activation programs? Remember that you can set default values for these in the item editor under the "Board-Driven" check.
