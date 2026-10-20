---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=uploads/smudgeymethodz.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=uploads/smudgeymethodz.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040819081159"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_uploads_2Fsmudgeymethodz.prg", captured: "20040819081159", sha256: "9a718253b7e03a324f90fa465aff49b35ccd4846bd67247ab314a30c1e7e427c", wayback_url: "https://web.archive.org/web/20040819081159/http://www.mysticsoftware.net/test.php?mode=6&file=uploads%2Fsmudgeymethodz.prg"}
---

# Mystic Software

************************************************ *** Here\'s a good method that lockes a door **** *** and the player will not be able to get **** *** in unless he has a key item. **** ************************************************ #Method LockedDoor() { #If(key1.itm!=0) { #Mwin("Dan: Damn its locked cant get in!") #Wait(a$) #Mwin("Dan: I probably need a") #ColorRGB(0,0,255) #Mwin("Dan: Key") #ColorRGB(255,255,255) #Push("s", "Daniel") } #If(key1.itm!=1) { #Mwin("I\'ll just use my key") #wait(a$) #Send (itemshop.brd,10,9,1) } #end }
