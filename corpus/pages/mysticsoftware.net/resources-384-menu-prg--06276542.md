---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/resources/384_menu.prg"
site: "mysticsoftware.net"
title: ""
original_url: "http://mysticsoftware.net/resources/384_menu.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20221201091127"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/resources/384_menu.prg", captured: "20221201091127", sha256: "4aba4ed57e643b8ac7fa8a69e7e8fde5ab613fd1e943fe384edbe666295dcb70", wayback_url: "https://web.archive.org/web/20221201091127/http://mysticsoftware.net/resources/384_menu.prg"}
---

# (untitled)

") #text (7.5,2.25,"Level ") #text (1.5,3,"HP: / ") #text (1.5,3.75,"SMP: / ") #text (7.5,3,"Attack: ") #text (7.5,3.75,"Defense: ") } *Aww, c'mon! Common sense, guys. The color changes for every player!!!! #if (playerHandle[1]$~="") { #colorrgb (0,255,0) #text (1.5,5," ") #text (7.5,5,"Level ") #text (1.5,5.75,"HP: / ") #text (1.5,6.5,"SMP: / ") #text (7.5,5.75,"Attack: ") #text (7.5,6.5,"Defense: ") } #if (playerHandle[2]$~="") { #colorrgb (0,0,255) #text (1.5,8," ") #text (7.5,8,"Level ") #text (1.5,8.75,"HP: / ") #text (1.5,9.5,"SMP: / ") #text (7.5,8.75,"Attack: ") #text (7.5,9.5,"Defense: ") } #if (playerHandle[3]$~="") { #colorrgb (255,255,0) #text (1.5,10.75," ") #text (7.5,10.75,"Level ") #text (1.5,11.5,"HP: / ") #text (1.5,12.25,"SMP: / ") #text (7.5,11.5,"Attack: ") #text (7.5,12.25,"Defense: ") } #if (playerHandle[4]$~="") { #colorrgb (0,255,255) #text (1.5,14," ") #text (7.5,14,"Level ") #text (1.5,14.75,"HP: / ") #text (1.5,15.5,"SMP: / ") #text (7.5,14.75,"Attack: ") #text (7.5,15.5,"Defense: ") } #if (gp!=0) { #colorrgb (255,255,255) #text (1.5,20,"You have no money!") } #if (gp!>0) { #colorrgb (255,255,255) #text (1.5,20,"GP: ") } #done!=0 *Makes buttons. Change the graphics if you like. #setbutton ("button_items.GIF",0,520,1,60,60) #setbutton ("button_players.GIF",1,520,75,60,60) #setbutton ("button_save.GIF",2,520,150,60,60) #setbutton ("button_cheat.GIF",3,520,225,60,60) #setbutton ("button_return.GIF",4,520,300,60,60) #setbutton ("button_quit.GIF",5,520,375,60,60) *Waits for you to click. (CLICK NOW!!!) #while (done!=0) { #mouseclick (x!,y!) #checkbutton (x!,y!,click!) #if (click!=0) { #done!=1 #bordercolor (255,255,255) #bordercolor (0,0,0) *Item Button Click #internalmenu (1) #branch (:main) } #if (click!=1) { #done!=1 #bordercolor (255,255,255) #bordercolor (0,0,0) *Player Button Click #prompt ("What will you do? Check [status], [equip]/remove items, or check/use [abilities]? Type nothing/anything else to cancel",player$) #if (player$="status") { *Want to check players status #internalmenu (3) #branch (:main) } #if (player$="equip") { *Equip/remove items #internalmenu (2) #branch (:main) } #if (player$="abilities") { *Check/use abilities #internalmenu (4) #branch (:main) } #branch (:main) } #if (click!=2) { *Save Game #done!=1 #dirsav (dest$) #if (dest$~="CANCEL") { #save (dest$) } #bordercolor (255,255,255) #bordercolor (0,0,0) #mwin ("Game Saved!") #wait #mwincls #branch (:main) } #if (click!=3) { *Cheater! Cheat System. Edit cheats and passwords if you like. #done!=1 #prompt ("Type a cheat word.",cheat$) #if (cheat$="Monopoly") { #bordercolor (255,255,255) #bordercolor (0,0,0) #givegp (1000000) #mwin ("Received 1,000,000 GP!!!") #wait #mwincls #branch (:main) } #if (cheat$="Elixir") { #bordercolor (255,255,255) #bordercolor (0,0,0) #inn #mwin ("All players restored to full energy!!!") #wait #mwincls #branch (:main) } #if (cheat$="Superman") { #bordercolor (255,255,255) #bordercolor (0,0,0) #giveexp (playerHandle[0]$,10000) #giveexp (playerHandle[1]$,10000) #giveexp (playerHandle[2]$,10000) #giveexp (playerHandle[3]$,10000) #giveexp (playerHandle[4]$,10000) #inn #mwin ("All players get 10,000 additional experience points!!!!") #wait #mwincls #branch (:main) } #branch (:main) } #if (click!=4) { #done!=1 #send (previousboard$,previousx!,previousy!,previouslayer!) #end } #if (click!=5) { #dos } } } #menu
