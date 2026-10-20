---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=uploads/FJwin.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=uploads/FJwin.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040912145337"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_uploads_2FFJwin.prg", captured: "20040912145337", sha256: "d3bf07535f59d8952f444ea2789b84bac590c5ee68a97f767515f4967a626051", wayback_url: "https://web.archive.org/web/20040912145337/http://www.mysticsoftware.net/test.php?mode=6&file=uploads%2FFJwin.prg"}
---

# Mystic Software

#Method FJwin(FaceGraphic$,speed!,slowtext$) { #If(SetMwin!=0) { #SaveScreen() #Texty!=2 #SetImageTranslucent("fjwin.bmp",1,1,575,100) #SetImage(FaceGraphic$,4,18,64,64) } #space$="" #xchange!=11 #charslow!=1 #ClearBuffer() #done!=0 #while(done!==0) { #charat(slowtext$,charslow!,textslow$) #charslow!=charslow!+1 #if(textslow$=="") { #done!=1 } #if(textslow$~="") { #if(skip$=="") { #Get(skip$) } #text(xchange!,texty!,textslow$) #if(skip$=="") { #if(textslow$~=space$) { #wav(click.wav) } #delay(speed!) } #xchange!=xchange!+1 } } #SetMwin!=1 #Texty!=Texty!+1 #ClearBuffer() #Method FJclr() { #RestoreScreen(0,0,607,101,0,0) #SetMwin!=0 }
