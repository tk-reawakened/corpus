---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=files/1-9prompt.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=files/1-9prompt.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20051103143917"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_files_2F1-9prompt.prg", captured: "20051103143917", sha256: "42ffaff4abd436e7a54c6c357f60a19b3de9f4bfd2ce177620e31b0f291463b8", wayback_url: "https://web.archive.org/web/20051103143917/http://www.mysticsoftware.net/test.php?mode=6&file=files%2F1-9prompt.prg"}
---

# Mystic Software

*********************** ******1-9 prompt******* *****by: kronical****** ********************************************************* ***********************Reference************************* *red!/green!/blue! - The color of the title text *loc_x!/loc_y! - The "x" and "y" position of the prompt(by tile) *text$ - The text(question that you want the prompt to show) *returnedkey! - The 1-9 number that the player selected is stored in this variable #oneprompt(255,0,0,5,5,"What number am i thinking of?") ********************************************************* #method oneprompt(red!,green!,blue!,loc_x!,loc_y!,text$) { #mwincls #forceredraw() #colorRGB(0,0,0) #fillrect(10,10,800,100) #colorRGB(red!,green!,blue!) #text(5,2,text$) #colorRGB(255,255,255) #done!=0 #savescreen #while(done!=0) { #restorescreen() #if(key$="ENTER") { #done!=1 #end } #CastNum(key$,key!) #if(key!>=1) { #returnedkey! = key! #text(loc_x!,loc_y!,key!) } #if(key!=0) { #text(loc_x!,loc_y!,returnedkey!) } #if(done!=0) { #wait(key$) } } #kill(red!) #kill(green!) #kill(blue!) #kill(text$) #kill(done!) #kill(loc_x!) #kill(loc_y!) }
Order it Today!
