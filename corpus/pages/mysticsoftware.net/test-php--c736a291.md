---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=files/savepoint.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=files/savepoint.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040910092920"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_files_2Fsavepoint.prg", captured: "20040910092920", sha256: "9aea54d998ca6d88f78450537c587669c3bb92f3cdf9d4a72a760ae103925e1d", wayback_url: "https://web.archive.org/web/20040910092920/http://www.mysticsoftware.net/test.php?mode=6&file=files%2Fsavepoint.prg"}
---

# Mystic Software

********************************************* **This program was created by me, Fireball,** **(Red XIII). You can put it on your game**** **as long as I\'m in the credits or*********** **somethin\'. So anyway, this program should** **work perfectly but if you find some kinda** **problem you can\'t fix (this is a pretty**** **simple program so I don\'t think you\'ll***** **have any problems) my AIM screen name is*** **FunkmastaB2000, or just go to:************* **"http://fireballgames.cjb.net". I don\'t**** **use Email much.To use this program********* **obviously just set it on a tile that******* **looks like a save point and turn the save** **ability off on the board. When the prog.*** **runs the save thing from the menu should*** **pop up when you pick "yes" and then just*** **type in the file name like on the menu and* **it\'ll save.******************************** ********************************************* **I finally relized how to make a save point* **work by looking at the programming on****** **Spyder\'s custom menu.********************** ********************************************* #MWin("You have reached a Save Crystal.") #Mwin("Would you like to save?") #MWin(" 1- Yes") #MWin(" 2- No") #ClearBuffer() :top #Wait(a$) #If(a$=="1") { #MwinCls() #topy!=125 #DirSav(saveto$) #If (saveto$~="") { #Save(saveto$) } #End } #If(a$=="2") { #MwinCls() #If (saveto$~="") { #Save(saveto$) } #end } #Branch(:top) #end
