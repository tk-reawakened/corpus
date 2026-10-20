---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=files/worldbattle.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=files/worldbattle.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040910092900"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_files_2Fworldbattle.prg", captured: "20040910092900", sha256: "ed9c8b5df9340e45bda794ca0d86ab6affeb1ea21f914144e96b01d3fb29d769", wayback_url: "https://web.archive.org/web/20040910092900/http://www.mysticsoftware.net/test.php?mode=6&file=files%2Fworldbattle.prg"}
---

# Mystic Software

************ * World Map Battle Mapper 2.0 ************ * Wow, new version of this hard to name program. * What it does is sends the player into a battle, * with different enemy levels based on location, * and different backgrounds based on what type of * tile the player is standing on. It requires MrG\'s * Misc. Plugin Pack to use. I know I could make it * easier to understand if I used Leuf\'s Programmer\'s * Plugin, but I won\'t. So there. ************ * To use, set as the file you want to use during * fights. Also, change it to more appropriate values. * Especially the tile filenames. ************ #GetBoardName(Name$) ** Rename "World.brd" to whatever your world map\'s name is. #if(Name$=="World.brd") { #GetPlayerCoords(0,MyX!,MyY!) #GetBoardTile(MyX!,MyY!,1,TileName$) ** Rename these files to whatever you need them to be. Example, put the name of your grass tile in "Grass.tst1", and your fight background that goes with it in "Grass.bkg" #if(TileName$="Grass.tst1") { #BKGND$="Grass.bkg" } #if(TileName$="Forest.tst1") { #BKGND$="Forest.bkg" } #if(TileName$="Snow.tst1") { #BKGND$="Snow.bkg" } #if(TileName$="Water.tst1") { #BKGND$="Water.bkg" } #if(TileName$="Sand.tst1") { #BKGND$="Sand.bkg" } #if(TileName$="Hill.tst1") { #BKGND$="Hill.bkg" } ** Now for the fun part. These #if commands section the map into squares. Depending on which square the player is in, a different skill level of enemies fight him. If you\'re using a custom battle system, odds are you\'ll have to change something. Go ahead and change it however you need to. ** NOTE: I made this for a 19x11 map, AS AN EXAMPLE. Change the coordnates, and add new "squares" as you need to. #If(MyX!=>1) { #If(MyY!=>1) { #If(MyX!=<10) { #If(MyY!=<6) { ** This square has a board skill of one, and encompasses the coordnates from (1,1) to (10,6), as you can see. Feel free to change these to fit your map. #Fight(1,BKGND$) } } } } #If(MyX!=>11) { #If(MyY!=>1) { #If(MyX!=<19) { #If(MyY!=>6) { ** This square has a board skill of two, and encompasses the coordnates from (11,1) to (19,6), as you can see. Feel free to change these to fit your map. #Fight(2,BKGND$) } } } } #If(MyX!=>1) { #If(MyY!=>7) { #If(MyX!=<10) { #If(MyY!=<11) { ** This square has a board skill of three, and encompasses the coordnates from (1,7) to (10,11), as you can see. Feel free to change these to fit your map. #Fight(3,BKGND$) } } } } #If(MyX!=>11) { #If(MyY!=>7) { #If(MyX!=<19) { #If(MyY!=>11) { ** This square has a board skill of four, and encompasses the coordnates from (11,7) to (19,11), as you can see. Feel free to change these to fit your map. #Fight(4,BKGND$) } } } } } ** This last part is for what happens if the player is NOT on the world map. Remember to change the filename! #if(Name$~="World.brd") { #fight(BoardSkill!,BoardBackground$) }
