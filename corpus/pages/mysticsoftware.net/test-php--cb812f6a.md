---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=files/jukebox.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=files/jukebox.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040910092533"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_files_2Fjukebox.prg", captured: "20040910092533", sha256: "ced0e9e6d50a1b1f036842239753e3a1f763f0581129fb960df4322be3ef0dd8", wayback_url: "https://web.archive.org/web/20040910092533/http://www.mysticsoftware.net/test.php?mode=6&file=files%2Fjukebox.prg"}
---

# Mystic Software

*********************************************** ** Scott West\'s Juke Box ** Finished on 9-21-02 *********************************************** ** To use: where it says #song1$="" put in the filename of the ** song you want in the "" (keep the .mid extension) do the same for ** all the others untill the star line. #song1$="" #song2$="" #song3$="" #song4$="" #song5$="" #song6$="" #song7$="" #song8$="" #song9$="" #song10$="" #song11$="" #song12$="" #song13$="" #song14$="" *********************************************** #SetButton("Blank.bmp",0,0,0,130,30) #SetButton("Blank.bmp",1,0,40,130,30) #SetButton("Blank.bmp",2,0,80,130,30) #SetButton("Blank.bmp",3,0,120,130,30) #SetButton("Blank.bmp",4,0,160,130,30) #SetButton("Blank.bmp",5,0,200,130,30) #SetButton("Blank.bmp",6,0,240,130,30) #SetButton("Blank.bmp",7,140,0,130,30) #SetButton("Blank.bmp",8,140,40,130,30) #SetButton("Blank.bmp",9,140,80,130,30) #SetButton("Blank.bmp",10,140,120,130,30) #SetButton("Blank.bmp",11,140,160,130,30) #SetButton("Blank.bmp",12,140,200,130,30) #SetButton("Blank.bmp",13,140,240,130,30) #SetButton("Exit.bmp",14,280,0,130,30) *********************************************** #Text(4,2,song1$) #Text(4,5,song2$) #Text(4,9,song3$) #Text(4,12,song4$) #Text(4,15,song5$) #Text(4,19,song6$) #Text(4,22,song7$) #Text(15,2,song8$) #Text(15,5,song9$) #Text(15,9,song10$) #Text(15,12,song11$) #Text(15,15,song12$) #Text(15,19,song13$) #Text(15,22,song14$) *********************************************** #click!=0 #While(click!==0) { #MouseClick(x!,y!) #CheckButton(x!,y!,buttonnum!) #If(buttonnum!==0) { #Midiplay(song1$) } #If(buttonnum!==1) { #Midiplay(song2$) } #If(buttonnum!==2) { #Midiplay(song3$) } #If(buttonnum!==3) { #Midiplay(song4$) } #If(buttonnum!==4) { #Midiplay(song5$) } #If(buttonnum!==5) { #Midiplay(song6$) } #If(buttonnum!==6) { #Midiplay(song7$) } #If(buttonnum!==7) { #Midiplay(song8$) } #If(buttonnum!==8) { #Midiplay(song9$) } #If(buttonnum!==9) { #Midiplay(song10$) } #If(buttonnum!==10) { #Midiplay(song11$) } #If(buttonnum!==11) { #Midiplay(song12$) } #If(buttonnum!==12) { #Midiplay(song13$) } #If(buttonnum!==13) { #Midiplay(song14$) } #if(buttonnum!==14) { #click!=1 #ClearButtons() #ForceRedraw() }}
