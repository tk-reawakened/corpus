---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=uploads/cursor.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=uploads/cursor.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040819081813"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_uploads_2Fcursor.prg", captured: "20040819081813", sha256: "40d2e47c8c7cf53e219c084828d884adc20ff938b38d16e7b683b93b6d9b1c67", wayback_url: "https://web.archive.org/web/20040819081813/http://www.mysticsoftware.net/test.php?mode=6&file=uploads%2Fcursor.prg"}
---

# Mystic Software

******************************************************************* ***************YUKI\'S CURSOR METHOD******************************** *cursorpic$: the name of the picture you want to use,************** * include the .bmp or waht everformat it is in********** *selection!: the amount of selections you want the user to********* * be able to make*************************************** *xspace: the X( or horizontal) space between cursor moves****** *yspace: the Y( or vertical) space between cursor moves******** *x! and y!: coordinates you want the cursor to start************** *cursorspot!: the spot the user hit enter at(note: starts at one)** * use this with if statments to determine what happens* ******************************NOTE********************************* * The transparent color for the cursor must be max red (255) * The cursor must be 32X32. if u wish to change this then to to**** * each area that has a setimagetransparent and change the size var* * The cursor can only go vertical, or horizontal at one time...**** * to make it only go horizontal set yspace! to 0******************* * to make it only go vertical set xpace! to 0********************** * if you dont do this then the cursor wont do anything************* *REPORT ANY BUGS TO I_YUKI_I@HOTMAIL>.COM*************************** ******************************************************************* #method cursor(cursorpic$,selection!,xspace!,yspace!,x!,y!,cursorspot!) { #savescreen() #cursorspot!=1 #xplace!=x! #yplace!=y! #xplacesize!=xplace!+32 #yplacesize!=yplace!+32 #setimagetransparent(cursorpic$,x!,y!,32,32,255,0,0) :cursorwrong #Wait(c$) #If(c$~="UP") { #If(c$~="DOWN") { #If(c$~="ENTER") { #If(c$~="LEFT") { #If(c$~="RIGHT") { #branch(:cursorwrong) } } } } } ************************ *******up/down********** ************************ #If(c$=="UP") { #if(xspace!~=0) { #Branch(:cursorwrong) } #if(xspace!=0) { #if(cursorspot!<=1) { #Branch(:cursorwrong) } #if(cursorspot!>1) { #restorescreen(xplace!,yplace!,xplacesize!,yplacesize!,xplace!,yplace!) #xplace!=xplace!-xspace! #yplace!=yplace!-yspace! #xplacesize!=xplace!+32 #yplacesize!=yplace!+32 #setimagetransparent(cursorpic$,xplace!,yplace!,32,32,255,0,0) #cursorspot!=cursorspot!-1 #branch(:cursorwrong) } } } #If(c$=="DOWN") { #if(xspace!~=0) { #Branch(:cursorwrong) } #if(xspace!=0) { #if(cursorspot!=>selection!) { #Branch(:cursorwrong) } #if(cursorspot!1) { #restorescreen(xplace!,yplace!,xplacesize!,yplacesize!,xplace!,yplace!) #xplace!=xplace!-xspace! #yplace!=yplace!-yspace! #xplacesize!=xplace!+32 #yplacesize!=yplace!+32 #setimagetransparent(cursorpic$,xplace!,yplace!,32,32,255,0,0) #cursorspot!=cursorspot!-1 #branch(:cursorwrong) } } } #If(c$=="RIGHT") { #if(yspace!~=0) { #Branch(:cursorwrong) } #if(yspace!=0) { #if(cursorspot!=>selection!) { #Branch(:cursorwrong) } #if(cursorspot!
