---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/uploads/jlpsmeths.prg"
site: "mysticsoftware.net"
title: ""
original_url: "http://www.mysticsoftware.net/uploads/jlpsmeths.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041011095428"]
author: null
repliers: []
authors: []
comments_present: 0
duplicate_of: "mysticsoftware.net/mysticsoftware.net/resources/jlpsmeths.prg"
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/uploads/jlpsmeths.prg", captured: "20041011095428", sha256: "011bf91d74305c4e9ea17f5c942e24991c5c60da27cbb7191d8933fbd05f73d7", wayback_url: "https://web.archive.org/web/20041011095428/http://www.mysticsoftware.net/uploads/jlpsmeths.prg"}
---

# (untitled)

") #Wait(a$) } *no wait command needed! ************** *custom after battle program *Instructions: *text$ : mwin text to pop up *midiplay$ : midi file to play *itemyn$ : whether you recieve an item or not (Y or N) *if itemyn$ is 'y', then type in the item to give in 'item$' #Method aftbat(text$,midiplay$,itemyn$,item$) { #MidiPlay(midiplay$) #MWin(" ") #If(itemyn$=="y") { #Giveitem(item$) } #Wait(a$) } *no wait command needed *************** *multiple items *instructions: *item$ : item to give *amount! : amount of that item #Method mulitm(item$,amount!) { #For(it!=1; it! < =amount!; it!=it!+1) { #GiveItem(item$) } } ***************** *custom inn *instructions: *name$ : name of inn *price! : price to stay *midi$ : midi file to play while sleeping *time! : time to sleep (just type '3' if you don't get it) #Method cinn(name$,price!,midi$,time!) { #GetGP(gold!) #MWin("Hi! welcome to inn!") #Wait(a$) #MWin("Staying the night costs ya only gp!") #MWin("What d'ya say?") @ #MWin("Press 1 for YES or 2 for NO") #Wait(opt!) #MWINCLS() #If(opt!==1) { #If(gold! =price!) { #MWin("alrighty then!") #Wait(a$) #MWincls() #MidiPlay(midi$) #ColorRGB(0,0,0) #Inn() #Delay(time!) #MWin("rest alright?, i hope so, come back again!") #Wait(a$) #MWINCLS() #end() } #If(opt!==2) { #MWin("fine then!") #Wait(a$) #MWinCls() #end() } } *******************
