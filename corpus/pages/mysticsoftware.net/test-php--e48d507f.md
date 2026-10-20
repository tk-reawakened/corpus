---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=files/noadicursor.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=files/noadicursor.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040818023644"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_files_2Fnoadicursor.prg", captured: "20040818023644", sha256: "7189bfb5492db8e1b5c726557e6e4d47827388cc736a6f36d1ef5a5edd60e26c", wayback_url: "https://web.archive.org/web/20040818023644/http://www.mysticsoftware.net/test.php?mode=6&file=files%2Fnoadicursor.prg"}
---

# Mystic Software

#Cursor(cursor.bmp,24,24,0,0,96,96,24) #method cursor(pic$,width!,height!,x!,y!,endx!,endy!,move!) { #savescreen() #s!=1 #sy!=y! #setimagetransparent(pic$,x!,y!,width!,height!,0,128,128) #while(s!=1) { :choose #wait(i$) { #if(i$~="UP") { #if(i$~="DOWN") { #if(i$~="RIGHT") { #if(i$~="LEFT") { #if(i$~="ENTER") { #branch(:choose) } } } } } #ry!=y!+height! #rx!=x!+width! #restorescreen(x!,y!,rx!,ry!,x!,y!) #if(i$="DOWN") { #ty!=y!+move! #if(y!
