---
kind: page
id: "tk3.toolkitzone.com/tk3.toolkitzone.com/help/?page=12"
site: "tk3.toolkitzone.com"
title: "Special Move Basics"
original_url: "http://tk3.toolkitzone.com/help/?page=12"
written: null
date_confidence: "unknown"
updated: null
captured: ["20051027175048", "20070123120219"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_12_amp_3BPHPSESSID_16097a3a6f8dae38d835cae025f2adc4", captured: "20051027175048", sha256: "952432b3fc3d7da6b37e39adb976cb36085165fd9d3759fbf8d94ec503963447", wayback_url: "https://web.archive.org/web/20051027175048/http://tk3.toolkitzone.com/help/?page=12&amp%3BPHPSESSID=16097a3a6f8dae38d835cae025f2adc4"}
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_12", captured: "20070123120219", sha256: "f8bff3892d7bca9c55249c9e30f482c955571830cd513833082b68fa54d69119", wayback_url: "https://web.archive.org/web/20070123120219/http://tk3.toolkitzone.com/help/?page=12"}
---

# Special Move Basics

Special moves (*.spc) encompass such objects as spells and combat skills that aren't covered by items. And like items, special moves can be used in battles and from menus (depending on settings). For instance, a heal spell could be used in both cases, but you would only want an attack move to be available during battle. Generally the use of a special move (SM) should come at some "cost" to the player - this is drawn from the aptly named Special Move Power (or SMP) of the player, an attribute much like health that can be accessed by a range of commands such as GetSMP(), SMP(). If the player does not have the required SMP for a move (as specified below) he cannot make it!
The idea of special moves is that the player learns them over time; as they gain experience or levels or complete a specific task. Setting conditions for usage of SMs can be found in the Special Move window of the . SMs appear automatically in menus when these conditions are satisfied; there are no RPGCode commands required to "give" SMs to players. [Character Editor](?page=7)
Enemies can also use special moves - see the Special Moves window in the . Enemies can also be made specially susceptible (i.e., they do more damage than usual) to certain SMs by assigning them when creating the enemy. [Enemy Editor](?page=9)
Around the Editor
The SM file itself contains player-independent information as listed below, detailing the effects of the move on the target and source.
Name - The name of the Special Move (SM), used to list and refer to it.
Fight Power - The amount of damage inflicted upon the target by the move.
Amount of SMP Removed from target - Special Move Power the target loses from the move.
Special Move Power Consumption - Amount of SMP required to make the move.
Description - A short description of the move, which appears when "Info" is selected in the Abilities page of the default menu.
RPGCode Program - Program to run when the special move is made (optional).
Status Effect - The to apply (optional, in-battle only). [status effect](?page=13)
Animation - The animation to play when the move is made (optional, in-battle only).
Battle-driven - The SM can be used in battle (through the "Special Move" submenu that gets its name from Special Move window in the ). [Character Editor](?page=7)
Board-driven - The SM can be used on the board, from the menu (for instance, through Abilities in the default menu); for example a 'heal' spell between battles.
