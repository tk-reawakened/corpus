---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=uploads/specialbattle.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=uploads/specialbattle.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040819081254"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_uploads_2Fspecialbattle.prg", captured: "20040819081254", sha256: "abf20d9408fc015e21523828da72470cb1bcbe5f10dd8be995c4fdb6ff0a0da2", wayback_url: "https://web.archive.org/web/20040819081254/http://www.mysticsoftware.net/test.php?mode=6&file=uploads%2Fspecialbattle.prg"}
---

# Mystic Software

***************************************** *****HERE ARE THE INSTRUCTIONS*********** ***************************************** *Each board that you want to use this for *must have a different value of board *constant 1, if you want the whole *board to be the same skill level just *leave constant 1 = to 0, to declare an *area, just use the command: *#Area(x1!,y1!,x2!,y2!,bkg$,skilllevel!) *at the end of checking for areas you can *include a #Fight command to choose a fight *if the player isn\'t in an area, exclude this *line if you want the rest of the board to *be "no encounters". Questions or Comments? *Leave a thread on our forum at http://tk.icqs.com *or e-mail me (KSNiloc) at colinjamesfitzpatrick@hotmail.com ***************************************** *****HERE IS THE MAIN PROGRAM************ ***************************************** *put all board specifcations here: #If(Constant[1]!==1) { #Area(1,1,19,5,"mybkg.bkg",1) *declare areas #Area(1,6,19,11,"myotherbkg.bkg",2) #Fight(0,"normalbkg.bkg") *fight specifications *to start if the player isn\'t in a declared area, *don\'t include this line if you want "no encounters" *in the other areas. } *Board doesn\'t have split skill levels, *just start a normal fight: #Fight(boardskill!,boardbackground$) ***************************************** *****HERE IS THE AREA METHOD************* ***************************************** #Method Area(x1!,y!,x2!,y2!,bkg$,skill!) { #if(playerX[0]!>=x1!) { #if(playerY[0]!>=y1!) { #if(playerX[0]!<=x2!) { #if(playerY[0]!<=y2!) { #Fight(skill!,bkg$) } } } } }
