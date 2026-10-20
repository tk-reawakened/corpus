---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/extend/plugins/jackyboys-misc/"
site: "rpgtoolkit.net"
title: "September 14th, 2009"
original_url: "http://rpgtoolkit.net/extend/plugins/jackyboys-misc/"
written: "2009-09-14"
date_confidence: "day"
updated: null
captured: ["20110504035317"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/extend/plugins/jackyboys-misc/index", captured: "20110504035317", sha256: "b30c9d6e8cc3490f82bb06dcb2b1a9a6c47ea0fe77a36b2a4648784ee4df26d0", wayback_url: "https://web.archive.org/web/20110504035317/http://rpgtoolkit.net/extend/plugins/jackyboys-misc/"}
---

# September 14th, 2009

[![jackyboy](thumb/80/community/images/avatars/upload/1418298804b3fb83022279.jpg)](member/jackyboy/)
Released
**September 14th, 2009**
Viewed times **405**
Downloaded times **205**
Developed by jackyboy
Jackyboy's Misc
**Provides a wide array of functions requested by the community.**
1. About
2. Reference
3. Examples
Provides functions for;
- Set/get the background image/color for a board
- Save a canvas as an image file
- Get the filename for an item on a board
- Rotate a canvas
- Get the number of item slots being used on a board
- Get the board's width/height
- Get an image's width/height
- Get a canvas width/height
- Get the experienced required for the player to progress to the next level
- A function to determine if the game is running as a standalone exe
- Mathematical functions: atan, acos, and asin
- Get item by index
changeBoardBkg("Filename");
Changes the board's background image..
changeBoardRGB(red, green, blue);
Changes the board's background color.
file = getBoardBkg();
Returns the current image used as the board's background image.
red = getBoardRed(); green = getBoardGreen(); blue = getBoardBlue();
Returns the amount of red/green/blue in the board's background color.
saveToBitmap(CanvasID, "Filename");
Saves a canvas to an image file.
file = getItemFilename(itemNumber);
Will return the filename of an item on the board.
rotateCanvas(SrcCnv, x, y, angle[, DestCnv]);
Rotates a canvas and draws it to the screen or optionally to another canvas.
items = countBoardItems();
Counts the number of items loaded into slots on the board.
handle = getItemByIndex(Index)
Retrieves the handle of item at a specific index number.
width = boardWidth(); height = boardHeight();
Returns the current width/height of the board in tiles.
width = getImageWidth("Filename"); height = getImageHeight("Filename");
Returns the width/height of an image in pixels.
width = getCanvasWidth(CanvasID); height = getCanvasHeight(CanvasID);
Returns the width/height of a canvas.
exp = expToNextLevel(UserID);
Returns how much EXP is needed before the next level-up.
pct = percentToNextLevel(UserID);
Returns the current EXP as a percentage of next level.
deg = aTan(x);
Returns the inverse tangent in degrees.
deg = aTan2(x, y);
Returns the arctangent of Y/X in degrees.
deg = aCos(x);
Returns the inverse of cosine in degrees.
deg = aSin(x);
Returns the inverse of sine in degrees.
degrees = toDegrees(x);
Converts radians to degrees and returns the result.
radians = toRadians(x);
Converts degrees to radians and returns the result.
{"twitter":[{"text":"Site is up and running, seems any initial problems are solved. See you on the forums :)","date":"Thursday at 2:55pm"},{"text":"New site is online but many of you will see a white screen, it's a problem with the PHPBB software. Trying to fix it, stay patient :)","date":"Thursday at 2:17pm"},{"text":"Site is online, little initial bug so apologies to those in the first 5 minutes who wondered why everything was broke :) Should be okay now.","date":"Thursday at 1:50pm"}]}
