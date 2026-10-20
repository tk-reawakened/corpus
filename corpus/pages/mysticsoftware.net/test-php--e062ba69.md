---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=files/TextBattle.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=files/TextBattle.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040910092840"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_files_2FTextBattle.prg", captured: "20040910092840", sha256: "53565707d80c7524ed7fe4af80f31bdb17733a854747e16cee6a843b96c5ae0e", wayback_url: "https://web.archive.org/web/20040910092840/http://www.mysticsoftware.net/test.php?mode=6&file=files%2FTextBattle.prg"}
---

# Mystic Software

#method Battle(playername$,enename$,enehp!,enefp!,gp!,exp!,chance!) { ***********BATTLE SYSTEM CODE STARTS HERE****************** **************** *LOOK FOR TBD\'s, AND PUT IN YOU PLAYER\'s VARIABLES (SUCH AS HEALTH) ****** #fontsize(14) #mwin(" has entered a battle with !") :top #mwin("You can Attack with A or run with R") #wait(A$) #if(A$=="R") { #random(chance!,run!) #if(run!==1) { #mwin("You\'ve escaped!") #wait() #end() } #if(run!~=1) { #mwin("Couldn\'t get away!") #branch(:top_ } } #if(A$=="A") { #enehp!=enehp!-player[fight]! #mwin(" did damage to !") #mwin(" now has health!") #if(enehp!<=0) { #mwin("You killed !") #giveexp(playername$,exp!) #mwin(" gained exp!") #givegp(gp!) #mwin(" gained gold!") #wait() #end() } #if(enehp!>=1) { ******************TBD**************** *You probably will have to change the player\'s health variable ************************************* #player[health]!=player[health]!-enefp! #mwin(" did damage, now has /!") #if(player[health]!<=0) { #mwin(" has been killed!") #end() } #if(player[health]!>=1) { #branch(:top) } **********METHOD END************* }
