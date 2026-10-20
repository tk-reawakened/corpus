---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/help.php?article=12&mode=1"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://mysticsoftware.net/help.php?mode=1&article=12"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040504142253"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/help.php__mode_1_article_12", captured: "20040504142253", sha256: "b3e51ff4559493a796491a2f65730259b1b434bd02f62e7e3d0e683bf8d3d676", wayback_url: "https://web.archive.org/web/20040504142253/http://mysticsoftware.net/help.php?mode=1&article=12"}
---

# Mystic Software

Skill level: Not for beginners Part 1: Introduction Part 2: An example... Part 3: Explanation of the example Part 4: Syntax explanation Part 5: Closing words Part 1: Introduction An If-Then-Else-IfEnd sulution is not built in in tk, but it's fully possible, and now, I will show you how to deal with the solution. In RPGCode, we only have one if command, #If. #If(statement is true) {*Then *commands to be run* }*End If Part 2: An example... Take a look at the following. You wanted to make a simple menu system, that prints the status for a player. You are using customized stats, except for HP and SMP. You have a #GetStatus-method that will get the specified status effect saved on a slot for a player. You have this algoritm inside a foor loop: #GetHP(playerhandle[qw_for!]$,qw_hp!) #If (qw_hp!=0) { #qw_status$="Dead" #Branch(:skip) } #If (qw_hp! < 20) { #qw_status$="Damagely wounded" #Branch(:skip) } #menu2.GetStatus(0,playerhandle[qw_for!]$,qw_status$) #If (qw_status$~="") { #Branch(:skip) } #menu2.GetStatus(1,playerhandle[qw_for!]$,qw_status$) #If (qw_status$~="") { #Branch(:skip) } #menu2.GetStatus(2,playerhandle[qw_for!]$,qw_status$) #If (qw_status$~="") { #Branch(:skip) } #menu2.GetStatus(3,playerhandle[qw_for!]$,qw_status$) #If (qw_status$~="") { #Branch(:skip) } #qw_status$="Normal" :skip #menu2.PrintText(283,qw_text_y!,"Status:
- If/Else/Endif - Written By BP
") Part 3: Explanation of the example: Here's how it works: first, it cecks if the player's hp is ike zero. Then it puts "Dead" into the var that contains the status. Then it branches to :skip, a label in the end of the if section. If he's not zero, then he's not dead. It skips the first If, and goes for the second. If the HP is low, but not zero, he's damagely wounded... and it goes on like this. But if he's alive, has smore hp then 20, and has no status effects acquired, then he is normal. You see that? The sentance before :skip. "It's nice that your algoritm works, but that doesn't explain the method..." Well, it does actually. I did explain the thing... Part 4: Syntax explanation #If(statement one==true) { *actions #Branch(:skip1) } #If(statement two==true) { *actions #Branch(:skip1) } #If(statement three==true) { *actions #Branch(:skip1) } #If(statement four==true) { *actions #Branch(:skip1) } *else actions :skip1 #If(statement one==true) { *actions #Branch(:skip2) } #If(statement two==true) { *actions #Branch(:skip2) } *else actions :skip2 Have you used C++? Then, this is equal too: if(statement one==true) { //actions } else if(statement two==true) { //actions } else if(statement three==true) { //actions } else if(statement four==true) { //actions } else { //actions } if(statement one==true) { //actions } else if(statement two==true) { //actions } else { //actions } Simple, eh? The first if: if(statement one==true) { *actions #Branch(:label name) } The else-if: if(statement==true) { *actions #Branch(:label name) } The else: *actions :label name Part 5: Ending words: I hope this thing made you wiser. At least it cleared up alot of foggy things for me... Questions, errors, full source of menu system (j/k), mail me: (redacted: email) -BP da Coder
