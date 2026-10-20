---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=files/planetsiege.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=files/planetsiege.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040910092638"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_files_2Fplanetsiege.prg", captured: "20040910092638", sha256: "697a6d699bd708ab2c31251de79e153630e9962237348c309dde066f48202a17", wayback_url: "https://web.archive.org/web/20040910092638/http://www.mysticsoftware.net/test.php?mode=6&file=files%2Fplanetsiege.prg"}
---

# Mystic Software

Text Battle System - By Aaron Pierce *This is the X-treme Games Battle System *for the Game \'Planet Siege\'. It was designed *By Aaron Pierce, with special thanx to Triuken *of TKZ. And is copyrigt (c) X-treme Games and *SideWinder Technology Productions. *Make your enemy an Item, and make this his Activation *program. Make sure you chage the #destroyitem and *#eraseitem number to the memory slot that your bad guy item *is in. #MWin("Look out! It\'s an enemy!!") #MWin("What should you do!?!") @ #While(command!==0) { #MWin("1-Fight") #MWin("2-Run") #Wait(results$) #If(results$=="1") { #Random(4, fight!) #If(fight!==1) { #MWin("Ouch! You got hit!") #Wait(a$) #MwinCls() #ApplyStatus("Timothy Alexander", "NMEHit.ste") } #If(fight!==2) { #Mwin("Wow! You got \'im!") #EraseItem(0) #DestroyItem(0) #GiveGP(10) #Mwin("He dropped 10 GP!") #Wait(a$) #MwinCls() #ForceRedraw() #command!=1 #End() } #If(fight!==3) { #MWin("Ouch! You got hit!") #wait(a$) #MwinCls() #ApplyStatus("Timothy Alexander", "NMEHit.ste") } #If(fight!==4) { #MWin("Nice! Never knew what hit him!") #EraseItem(0) #DestroyItem(0) #GiveGP(45) #Mwin("WoW! He dropped 45 GP!") #Wait(a$) #MwinCls() #ForceRedraw() #command!=1 #End() } } #If(results$=="2") { #Random(4, run!) #If(run!==1) { #MWin("He blocked you escape!") #Wait(a$) #MwinCls() #ApplyStatus("TimAl.tem",NMEHit.ste) } #If(run!==2) { #fade(1) #Send("startboard.brd", 11,19,1) #Mwin("Got away safely!") #Wait(a$) #MwinCls() #command!=1 } #If(run!==3) { #MWin("You couldn\'t get away!") #wait(a$) #MwinCls() #ApplyStatus("TimAl.tem",NMEHit.ste) } #If(run!==4) { #fade(1) #Send("startboard.brd", 11,19,1) #Mwin("You got away!") #Wait(a$) #MwinCls() #command!=1 } } #EraseItem(0) #DestroyItem(0) #End()
