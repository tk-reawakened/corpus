---
kind: page
id: "tk3.toolkitzone.com/tk3.toolkitzone.com/help/?page=18.6"
site: "tk3.toolkitzone.com"
title: "— — Reserved Variables and Constants RPGCode Language Features"
original_url: "http://tk3.toolkitzone.com/help/?page=18.6"
written: null
date_confidence: "unknown"
updated: null
captured: ["20071209044756"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_18.6", captured: "20071209044756", sha256: "70bdb1cd48707cbe2d7ac878ee389a674596bc5a0d44be8228024f29a2d03029", wayback_url: "https://web.archive.org/web/20071209044756/http://tk3.toolkitzone.com/help/?page=18.6"}
---

# — — Reserved Variables and Constants RPGCode Language Features

Contents
Reserved variablesReserved constants
Reserved variables
There are a number of variables and constants that the RPGToolkit's engine automatically creates when you start your game which pertain to various things like players and boards. Each are accessible independently, though there are function alternatives to retrieving and setting some of them (the preferred way).
Players:
— returns the handles (names) of any player in your party. is a value between 0 and 4 (0 is the first player, 1 is the second, et cetera). playerHandle[index] index
— returns the coordinate of any player in your party currently on the board. is a value between 0 and 4. Alternatively, the function can be used to obtain this value and others. playerX[index] *x* index playerLocation()
— returns the coordinate of any player in your party currently on the board. is a value between 0 and 4. Alternatively, the function can be used to obtain this value and others. playerY[index] *y* index playerLocation()
— returns the layer of the board that the player is currently on. is a value between 0 and 4. Alternatively, the function can be used to obtain this value and others. playerLayer[index] index playerLocation()
Boards:
— returns the fight background of the current board. boardBackground
— returns the fighting skill of the enemies on the current board. boardSkill
— returns the titles assigned to the board layers. is a value between 0 and the number of layers on the board. boardTitle[index] index
— returns the board constants. is a value between 0 and the number of constants set for the board. constant[index] index
— returns the filename of the music that is playing on the current board. music
— returns the handles of the threads on the board. is a value between 0 and however many threads have been set. threads[index] index
Miscellaneous:
— returns or sets the ambient RGB colors. The values can range from -255 to 255. Alternatively, the function can be used to set these. If it is not used, you must call before the ambient color changes take affect. ambientRed, ambientGreen, ambientBlue setAmbientLevel() forceRedraw()
— returns the handle of a canvas which can be rendered on and off using the function. cnvRenderNow renderNow()
— returns the total game time in seconds. gameTime
Reserved constants
Flags:
— Direction constants returned by the and functions. tkDIR_N, tkDIR_S, tkDIR_E, tkDIR_W, tkDIR_NW, tkDIR_NE, tkDIR_SW, tkDIR_SE [playerDirection()](?page=19#playerdirection) [itemDirection()](?page=19#itemdirection)
— Used for clearing queued movements. See: , , , , or . tkMV_CLEAR_QUEUE [playerStep()](?page=19#playerstep) [itemStep()](?page=19#itemstep) [push()](?page=19#push) [pushItem()](?page=19#pushitem) [playerPath()](?page=19#playerpath) [itemPath()](?page=19#itempath)
— Used to pause thread execution until movement stops. See: , , , , , , or . tkMV_PAUSE_THREAD [playerStep()](?page=19#playerstep) [itemStep()](?page=19#itemstep) [push()](?page=19#push) [pushItem()](?page=19#pushitem) [playerPath()](?page=19#playerpath) [itemPath()](?page=19#itempath) [playerStance()](?page=19#playerstance) [itemStance()](?page=19#itemstance)
— Used for pathfinding to a location. See: or . tkMV_PATHFIND [playerPath()](?page=19#playerpath) [itemPath()](?page=19#itempath)
— Used to make a sprite walk along a waypoint path. See: or . tkMV_WAYPOINT_PATH [playerPath()](?page=19#playerpath) [itemPath()](?page=19#itempath)
— Used to link a sprite to a waypoint path. See: or . tkMV_WAYPOINT_LINK [playerPath()](?page=19#playerpath) [itemPath()](?page=19#itempath)
Target and source handles:
There are two special handles called "target" and "source", which refer to the currently selected player, item, or enemy. For example, in battle you may use the following code to show the HP of the : *target*
hp = getHp("target");
mwin(hp);
wait();
mwincls();
If this code was attached to a special move that the player used, "source" would refer to the player using it and "target" would refer to the enemy being hit by it. Many other functions accept "target" and "source" as the given handle.
