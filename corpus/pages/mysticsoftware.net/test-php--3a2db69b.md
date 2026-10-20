---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=files/nihwindow.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=files/nihwindow.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040910092844"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_files_2Fnihwindow.prg", captured: "20040910092844", sha256: "1aef85dc8323b4a868a4e0a8dee13b4268cef9578b2139f7dbddb13c996de774", wayback_url: "https://web.archive.org/web/20040910092844/http://www.mysticsoftware.net/test.php?mode=6&file=files%2Fnihwindow.prg"}
---

# Mystic Software

*It\'s a centered, translucent message window program. *Not bad. Try it out! #nwin("line1 text") #wait #nwincls() #method nwin(text$) { #fontsize(18) #bold("on") #x! = 100 #y! = 0 #if(lines!==0) { #savescreen() #setimagetranslucent("mwin.jpg",x!,y!,360,150) #text(8,2,text$) #lines! = 1 #branch(:b) } #if(lines!==1) { #text(8,3,text$) #lines! = 2 #branch(:b) } #if(lines!==2) { #text(8,4,text$) #lines! = 3 #branch(:b) } #if(lines!==3) { #text(8,5,text$) #lines! = 4 #branch(:b) } #if(lines!==4) { #text(8,6,text$) #lines! = 5 #branch(:b) } #if(lines!==5) { #text(8,7,text$) #lines! = 6 #branch(:b) } :b } #method nwincls() { #restorescreen(100,0,460,150,100,0) #lines! = 0 }
