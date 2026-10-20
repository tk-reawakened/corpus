---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/resources/cursor.prg"
site: "mysticsoftware.net"
title: ""
original_url: "http://mysticsoftware.net/resources/cursor.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20221201091752"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/resources/cursor.prg", captured: "20221201091752", sha256: "77a11cc3101abe3f4e7279b9d8a4810ac16f541620b893aae2cba83cd92318de", wayback_url: "https://web.archive.org/web/20221201091752/http://mysticsoftware.net/resources/cursor.prg"}
---

# (untitled)

1) { #restorescreen(xplace!,yplace!,xplacesize!,yplacesize!,xplace!,yplace!) #xplace!=xplace!-xspace! #yplace!=yplace!-yspace! #xplacesize!=xplace!+32 #yplacesize!=yplace!+32 #setimagetransparent(cursorpic$,xplace!,yplace!,32,32,255,0,0) #cursorspot!=cursorspot!-1 #branch(:cursorwrong) } } } #If(c$=="RIGHT") { #if(yspace!~=0) { #Branch(:cursorwrong) } #if(yspace!=0) { #if(cursorspot!=>selection!) { #Branch(:cursorwrong) } #if(cursorspot!
