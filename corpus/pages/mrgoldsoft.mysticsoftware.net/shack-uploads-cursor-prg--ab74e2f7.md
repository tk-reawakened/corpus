---
kind: page
id: "mrgoldsoft.mysticsoftware.net/mrgoldsoft.mysticsoftware.net/shack/uploads/cursor.prg"
site: "mrgoldsoft.mysticsoftware.net"
title: ""
original_url: "http://mrgoldsoft.mysticsoftware.net/shack/uploads/cursor.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20030902192628"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/mrgoldsoft.mysticsoftware.net/shack/uploads/cursor.prg", captured: "20030902192628", sha256: "77a11cc3101abe3f4e7279b9d8a4810ac16f541620b893aae2cba83cd92318de", wayback_url: "https://web.archive.org/web/20030902192628/http://mrgoldsoft.mysticsoftware.net/shack/uploads/cursor.prg"}
---

# (untitled)

1) { #restorescreen(xplace!,yplace!,xplacesize!,yplacesize!,xplace!,yplace!) #xplace!=xplace!-xspace! #yplace!=yplace!-yspace! #xplacesize!=xplace!+32 #yplacesize!=yplace!+32 #setimagetransparent(cursorpic$,xplace!,yplace!,32,32,255,0,0) #cursorspot!=cursorspot!-1 #branch(:cursorwrong) } } } #If(c$=="RIGHT") { #if(yspace!~=0) { #Branch(:cursorwrong) } #if(yspace!=0) { #if(cursorspot!=>selection!) { #Branch(:cursorwrong) } #if(cursorspot!
