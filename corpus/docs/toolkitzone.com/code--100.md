---
kind: doc
id: "toolkitzone.com/100"
site: "toolkitzone.com"
title: "Code:"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=100"
written: "2004-12-23T15:17:00"
date_confidence: "exact"
updated: null
captured: ["20060521152632"]
author: "Delano"
repliers: []
authors: ["Delano"]
comments_present: 0
f_author: "Delano"
f_date: "December 23, 2004, 3:17 pm"
f_description: "Official final list of fixes, changes and additions for the next release of the Toolkit, 3.0.5. Big thanks goes out to Colin and Delano for all their hard work, Occasionally Correct for his excellent help documents and also faero and Shao. Expect the release itself sometime in the very near future."
f_section: "Toolkit 3.x"
f_title: "Official 3.0.5 Changes"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_100", captured: "20060521152632", sha256: "29e740220e701f51b3ce7dbdd721cd25de5332c790f5fded069b7e5cb348d707", wayback_url: "https://web.archive.org/web/20060521152632/http://www.toolkitzone.com/library.php?mode=read&doc=100"}
---

# Code:

TK3 3.0.5 Release: Late December
This is the complete feature/fix list for the release of RPG Toolkit version 3.0.5. All items listed here are guarenteed to be present in the release, which is hopefully in the next few days.
Contributors for this release, in alphabetical order: Colin, Delano, faero, Occasionally_Correct, Shao.
Trans3
Bug Fixes + #Push/#PushItem moved objects too fast with no control of speed. + #ItemLocation sometimes returned wrong co-ordinates. + Boards smaller than the screen began centred, but jumped to the top/left of the screen when scrolling started. + Black boxes sometimes appeared for players/items when entering a new board. + 'Under' tile transluscency problems in pixel movement fixed. + Walking against a solid tile, the player didn't change direction (if he was facing a different direction to the wall). + #Bold/#Italics/#Underline fixed. + The message window could not always be successfully hidden with mwincls(). + The RPGCode debugger was buggy. + MIDIs and WAVs didnt work in Windows9x.
+ Literal variables could not contain the NULL character. + Modular music (*.it and company) would not play anywhere. + Plugins could not be sent variables enables the multiplayer plugin to work). + Maths that mixed variables with constants did not work. + Players/items without graphics displayed as black boxes / random bitmaps. + Memory leak in board background image drawing. + Loose code in #included programs ran sometimes. + end() within ifs and the like ran regardless of the construct's outcome. + Nestled if/else statements messed up. + true/false could be killed. + ' < ' and '>' didn't work in equations.
New Additions + Rewritten movement system [by Delano] + #MultiRun can now be used to make multiple items and players move at the same time. Movement begins after the closing bracket of #MultiRun. e.g.
**Code:**
```
MultiRun() { Push("n,n,ne,e,e,se,sw,w") PushItem(0, "w,w,w,sw,nw,n") PushItem(1, "s") }
```
All movement begins at the same time, and the program waits until the last item/player finishes moving to run the next line of the program after #MultiRun. + #Push/#PushItem in a thread no longer prevents other items/programs/players moving. For instance, you can program an npc to continuously walk a set path without interrupting player movement:
**Code:**
```
Until(forever!) { PushItem(0, "n,ne,e,se,s,sw,w,nw") }
```
**Code:**
```
PixelMovement(usePixelMovement$ [, usePixelPush$]) - usePixelMovement$ must be either "on" or "off" (as before). - usePixelPush$ must be either "on" or "off" (defaults to "off" and is ineffective in tile movement).
```
+ Custom resolutions In the main file, you can specify the dimensions you want the game to run at. Note that some graphics cards may not be able to handle all resolutions! + Custom cursors [by Colin] Every game can have a custom cursor, changeable at runtime. The cursor can be any image type, including tiles. The cursor can be altered through RPGCode using the new command:
```
MouseCursor(file$, x!, y!, r!, g!, b!) -Changes the mouse cursor to an image or tile. -file$: image to draw, "" will remove the cursor, "TK DEFAULT" will restore the default. - x!, y!: location of the hotspot on the tile. - r!, g!, b!: define the transparent colour on the image.
```
+ [by Colin] The entire OOP system has been rewritten with full object-orientated functionality. For a full overview, see "RPGCode OOP Overview" in the tkz library:
Object orientated programming (OOP) in RPGCode
<http://www.toolkitzone.com/library.php?mode=read&doc=64>
+ New RPGCode commands / operators
```
GetTextWidth(text$) / GetTextHeight(text$) - Return the pixel width or height, respectively, of the indicated string as rendered with the current font style. [by Shao] DrawCanvasTransparent(cnv!, x!, y!, r!, g!, b!, [, width!, height! [, destCnv!]]) - Draws a canvas using transparency. - cnv!: canvas to draw. - x!, y!: location to draw to. - r!, g!, b!: define the transparent colour on the canvas. - width!, height!: stretch the canvas to a certain size when drawing. - destCnv!: canvas to draw to, if omitted, canvas is drawn to the screen. PlayerSpeed(num!, speed!) / ItemSpeed(num!, speed!) - Changes the speed of an item or player num!. - speed!: Walk speed, set in seconds (recommended 0.05 to 0.20). PlayerStance(num!, stance$) / ItemStance(num!, stance$) - Changes the stance of an item or player (note: does not render, you must call forceRedraw()). iif(condition, true, false) [by faero] - Evaluates a condition and returns either the true or the false part (which must be the same type). setVolume(percent!) - Can now set the volume of music!
```
sivart
December 23, 2004, 7:32 pm
Sounds like 3.0.5 is going to rock!
zyrshnikashnu
December 23, 2004, 8:02 pm
Excellent. Just what I've been waiting for. *recalls thinking something similar for 3.0.4...*
Dont_Think_So
December 23, 2004, 9:25 pm
Something tells me there were some more features, but I can't remember any of them :P Looking awesome, I can't wait to try it out *cough*.
Raven Ryan
December 23, 2004, 9:29 pm
"+ Faster color coding in the RPGCode editor." I had been waiting for colour coding... Heh.
**real-time**
matt72186
December 23, 2004, 9:53 pm
Wow, good job guys. This release looks very promising; I can't wait for a release.
Colin
December 23, 2004, 10:44 pm
There already is realtime coloring.
Talyn
December 24, 2004, 5:02 am
The OOP support is what I'm looking forward to the most. RPGCode has become a programming language of considerable power since TK3 went open source.
William
December 24, 2004, 6:23 am
This is great. Thanks guys =) Merry Christmas
Mystinar
December 24, 2004, 12:33 pm
Has the MWin bug I mentioned been fixed?
nOObified
December 24, 2004, 12:49 pm
Nice work guys! Have a safe and happy holidays!
Colin
December 24, 2004, 4:14 pm
Yes. *Has the MWin bug I mentioned been fixed?*
arcticsalem
March 5, 2005, 5:50 pm
nice work. need to actually USE it now (lol)
Official final list of fixes, changes and additions for the next release of the Toolkit, 3.0.5. Big thanks goes out to Colin and Delano for all their hard work, Occasionally Correct for his excellent help documents and also faero and Shao. Expect the release itself sometime in the very near future.
Sep 4, '05
Apr 5, '05
Jan 26, '05
Dec 12, '04
Jun 6, '05
