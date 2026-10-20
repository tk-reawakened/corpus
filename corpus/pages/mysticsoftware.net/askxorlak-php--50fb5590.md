---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/askxorlak.php?mode=1&question=12"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/askxorlak.php?mode=1&question=12"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040628061857"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/askxorlak.php__mode_1_question_12", captured: "20040628061857", sha256: "3711940cdc63346ed7f6fe1c754bef743434472a7a985d0adfd00155ec869505", wayback_url: "https://web.archive.org/web/20040628061857/http://www.mysticsoftware.net/askxorlak.php?mode=1&question=12"}
---

# Mystic Software

How do I make an airship?
Airships can be tricky, but they're not impossible. In the simplest case, you're going to do a #newplyr to change the character graphics to the ship graphics and a #putplayer command to send the player to a new layer (you don't want things that were solid while on the ground to be solid when you're on the ship): #newplyr("airship.tem") #putplayer(playerHandle[0]$,playerX[0]!,playerY[0]!,2) *We'll assume that layer 2 is the "air" layer And to land: #newplyr("hero.tem") #putplayer(playerHandle[0]$,playerX[0]!,playerY[0]!,1) * 1 is the ground layer Now, of course all this does is change the hero into a flying ship and back again at will. If you want to leave the ship and have it stay there for you to come back to later, you'll have to "remember" where you parked it. Your landing method would look something like this: #newplyr("hero.tem") #putplayer(playerHandle[0]$,playerX[0]!,playerY[0]!,1) *Remember where we put it #airship_X_location!=playerX[0]! #airship_Y_location!=playerY[0]! #airship_board$=BoardTitle[8]$ * You have to get creative here, since there's no variable that contains the name of the current board. One way is to fill in the name of the current board as one the layer names in the board editor. #layerput(airship_X_location!,airship_Y_location, 2, "airship.gph") * set down an image of the parked airship on the board Now to get on the airship, you need to check if the player is standing over it: #if(airship_board$=BoardTitle[8]$) { #if(airship_X_location!=playerX[0]!) { #if(airship_Y_location!=playerY[0]!) { #newplyr("airship.tem") #putplayer(playerHandle[0]$,playerX[0]!,playerY[0]!,2) } } } Also, you'll probably want the player to be able to see the airship if you leave the board and come back. In your warp programs, you'll have to do something like this: #send( ... ) #if(airship_board$=BoardTitle[8]$) { #layerputairship_X_location!,airship_Y_location!, 2, "airship.gph") } #done
