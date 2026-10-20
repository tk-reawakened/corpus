---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=files/dtsstats.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=files/dtsstats.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040818023736"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_files_2Fdtsstats.prg", captured: "20040818023736", sha256: "1f720830938880d1b10dae44812bf6273887f63048111de2b3421f6a8d09ce58", wayback_url: "https://web.archive.org/web/20040818023736/http://www.mysticsoftware.net/test.php?mode=6&file=files%2Fdtsstats.prg"}
---

# Mystic Software

*Ok, now this command allows you to give any amount to *any stat you make up. Now, you can have stamina, dexterity, *and the like. negative values take away from the stat *Example: *#givestat("Tano","Mind",2) *Look! Your two thingies smarter!!! #method givestat(player$,stat$,amount!) { #comm$="#custstat"+player$+stat$+"!=custstat"+player$+stat$+"!+amount!" #rpgcode(comm$) } *This grabs the value of a custom stat and puts it in a variable. *Pretty straight forward. *Example: *#givestat("Tano","Mind",2) *#getstat("Tano","Mind",mind!) *#mwin("Hey you have smartness now!!!") *#wait #method Getstat(player$,stat$,deststat!) { #comm$="#deststat!=custstat"+player$+stat$+"!" #rpgcode(comm$) #returnmethod(deststat!) } *This next method Sets a stat. So... you can make your IQ 2 *instead of adding 2. *example: *#setstat("Tano","Mind",2) *#mwin("HAHA! You now have an IQ of 2!!! Stupid!!!") *#Wait #method setstat(player$,stat$,value!) { #getstat(player$,stat$,tempstatval!) #value!=value!-tempstatval! #givestat(player$,stat$,value!) } *These methods below are used EXACTLY the same way as the above *stats, but use literal variables. This way, you can use names, descriptions, etc. #method setstatlit(player$,stat$,value$) { #comm$="#custstat"+player$+stat$+"$="+value$ #rpgcode(comm$) } #method Getstatlit(player$,stat$,deststat$) { #comm$="#deststat$=custstat"+player$+stat$+"$" #rpgcode(comm$) #returnmethod(deststat$) } *EXAMPLE #setstat("Tano","IQ",2) #setstat("Frap","IQ",7) #getstat("Tano","IQ",myiq!) #getstat("Frap","IQ",myiq2!) #mwin("You now have an IQ of, and Frap has! IDIOT!") #wait(a$) #givestat("Tano","IQ",300) #getstat("Tano","IQ",myiq!) #givestat("Frap","IQ",250) #getstat("Frap","IQ",myiq!) #mwin("Congrats, you have just gotten through harvard.") #mwin("You now have an IQ of, and Frap has.") #wait(a$)
