---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=files/colors.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=files/colors.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040910092929"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_files_2Fcolors.prg", captured: "20040910092929", sha256: "9c43d16433764f9842aeea5801ca736c37b73e089f378a46f1338b9a6964517a", wayback_url: "https://web.archive.org/web/20040910092929/http://www.mysticsoftware.net/test.php?mode=6&file=files%2Fcolors.prg"}
---

# Mystic Software

**************************************************** * Matts Color Selector * **************************************************** #colors(100,100) *It will store the results in r! g! and b! *xpos! and ypos1a! variables is where you want to position the color selector #Method colors(xpos!,ypos1a!) { #endx!=xpos!+255 #textc!=endx!/8 #endx!=endx!+26 #ypos1!=ypos1a!+5 #ypos2a!=ypos1a!+10 #ypos2!=ypos1a!+15 #ypos3a!=ypos1a!+20 #ypos3!=ypos1a!+25 #ypos4a!=ypos1a!+30 #ypos4!=ypos1a!+35 #xpos2!=endx!+20 #textx!=xpos!+5 #textx!=textx!/8 #texty!=ypos1a!+55 #texty!=texty!/8 #textminx!=xpos!-5 #textmaxx!=xpos!+146 #textminy!=texty!*8-6 #textmaxy!=texty!*8+6 #textcy1!=ypos1!/8 #textcy2!=ypos2!/8 #textcy3!=ypos3!/8 #r!=0 #g!=0 #b!=0 #rx!=xpos! #gx!=xpos! #bx!=xpos! #exit!=0 #Fontsize(8) #ColorRGB(0,0,0) #Text(textx!,texty!,"Click Here to exit") #DrawLine(xpos!,ypos1!,endx!,ypos1!) #DrawLine(xpos!,ypos2!,endx!,ypos2!) #DrawLine(xpos!,ypos3!,endx!,ypos3!) #SaveScreen() #While(exit!==0) { #ColorRGB(255,0,0) #FillCircle(rx!,ypos1!,5) #ColorRGB(0,255,0) #FillCircle(gx!,ypos2!,5) #ColorRGB(0,0,255) #FillCircle(bx!,ypos3!,5) #ColorRGB(r!,g!,b!) #FillRect(endx!,ypos2a!,xpos2!,ypos4a!) #MouseClick(x!,y!) #if(x!>xpos!) { #if(x!ypos1a!) { #if(y!ypos1a!) { #if(y!ypos2a!) { #if(y!ypos3a!) { #if(y!textminx!) { #if(x!textminy!) { #if(y!
