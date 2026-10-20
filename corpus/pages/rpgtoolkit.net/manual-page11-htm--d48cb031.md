---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/manual/page11.htm"
site: "rpgtoolkit.net"
title: "[ ]Toolbars"
original_url: "http://rpgtoolkit.net/manual/page11.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20120618020341"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/manual/page11.htm", captured: "20120618020341", sha256: "76a4815890c64c8e3e5c82b9b24805763d395a97575f69ceab7cfdac0574ad20", wayback_url: "https://web.archive.org/web/20120618020341/http://rpgtoolkit.net/manual/page11.htm"}
---

# [ ]Toolbars

Tile Bitmap Basics
A tile bitmap (*.tbm) is a rectangle of tiles grouped together much like a board, and used to construct an image that is split between tiles, for instance a player frame that is 64x32 pixels in size. Tile bitmaps can be used like standard image files in many Toolkit image commands, and can be used for (*.bkg) and frames. [battle backgrounds](pageed_background.htm) [animation](page10.htm)
Most important is their use in animations, since a tile bitmap is the only way of putting multiple tiles in an animation frame. In this way, a tile bitmap must be created for each frame of the animation.
To create a tile bitmap, firstly set the image to the required size using the size option in the lower toolbar. Next, select the required tiles through the "Select Tile" button in the left-hand toolbar, or through the tileset browser in the right-hand toolbar, and click the image to set the tile. Note that tile bitmaps are stored in the \Bitmap folder rather than the \Tiles folder.
Around The Editor
The square in the middle of the screen is the tile bitmap, which defaults to 1x1.
Toolbars
Grid On/Off - Toggles a tile grid on the image.
Redraw - Redraws the tile bitmap - occasionally this may be required when graphics are not automatically updated.
Select Tile - Opens a window where you can select the tile or tileset you want to place. You can also select tiles through the tileset browser in the right-hand toolbar.
Draw Lock - Select for placing tiles on the bitmap.
Eraser - Erases tiles.
Tile Lighting - Sets the shading level for the current tile. Use the slider to increase or decrease the lightness (-255 to +255), and click the colour box above to select a hue.
Size - Specifies the height and width of the tile bitmap, in tiles. Enter values in the boxes and hit "Enter" to update the image.
Current Tile - Displays the currently selected tile, tool and co-ordinate.
