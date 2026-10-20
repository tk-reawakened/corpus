---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/manual/pageed_background.htm"
site: "rpgtoolkit.net"
title: "Background Basics"
original_url: "http://rpgtoolkit.net/manual/pageed_background.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20120618020652"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/manual/pageed_background.htm", captured: "20120618020652", sha256: "37c4f4b578676067a620472083601eca975a2c00c2abc932cad7ada07074edcc", wayback_url: "https://web.archive.org/web/20120618020652/http://rpgtoolkit.net/manual/pageed_background.htm"}
---

# Background Basics

A background file (*.bkg) is a component of the battle system that contains settings to "localise" battles to the current board, by displaying background images and music that reflect the current location. The style of the default battle system is such that the players get transported away from the board for the battle, and so the background image should be representative of the type of area depicted on the board. (This creates the opportunity to make, for instance, perspective backdrops for your battles, which is a popular trend.)
For random fighting, a single background can be specified per board (in > Board Settings); for programmed fighting a background can be set in each fight (through Fight() or FightEnemy() commands). [Board Editor](page4.htm)
Around the Editor
Image - The image file to display in the background. Standard image files are supported along with Tile Bitmaps, which can be used to make composite images from tiles (like boards, but without the attached information).
Background Fight Music - The music file to play for the duration of the fight.
Menu Sounds - A selection of sound effects can be specified for the listed actions.
