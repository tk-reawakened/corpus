---
kind: doc
id: "toolkitzone.com/90"
site: "toolkitzone.com"
title: "Column"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=90"
written: "2004-12-12T18:54:00"
date_confidence: "exact"
updated: null
captured: ["20060612033039", "20070308200903"]
author: "Colin"
repliers: []
authors: ["Colin"]
comments_present: 0
f_author: "Colin"
f_date: "December 12, 2004, 6:54 pm"
f_description: "It's all about the next TK3 release today, as Colin outlines the key fixes and changes in the editor and engine such as the overhauled movement system and new class capabilities. A nice way to wet your appetite before the release later this month."
f_title: "Assembly Line"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_90", captured: "20060612033039", sha256: "602ae4f1043d45c203c2f040993d935d6efb7596237c82b2ee5b284c880c4b0a", wayback_url: "https://web.archive.org/web/20060612033039/http://www.toolkitzone.com/library.php?mode=read&doc=90"}
  - {path: "wayback/toolkitzone.com/library.php__doc_90_highlight_", captured: "20070308200903", sha256: "8277731ec50b297e3e50a3236e2aabdf42c8865ea8c0cdcc91e3bdbfcece454f", wayback_url: "https://web.archive.org/web/20070308200903/http://www.toolkitzone.com:80/library.php?doc=90&highlight"}
---

# Column

TK3 Amelioration IV
Assembly Line
As you may or may not know, 3.05 will likely be available in time for the holiday season. I dont know if the majority of the community feels the same way, but Im ever more excited than days before the release of version 3.04. This version is good news for everyone  designers and players alike. With any luck, this version will cast away doubt from ever the most sour of TK2 diehards. Why, you ask? It all boils down to stability, features.
I was originally intending to code to battle system today but I decided it would be in everyones best interest to have a copy of 3.05 at their disposal first. Instead, Ill list everything I find myself repeatedly saying on the TK3 forum. In the section below, I also list the new RPGCode commands  many of which we will use in said battle system. *Features*
Stability
The 3.04 release disappointed a lot of people in this area. Pushing players crashed the system, half the new commands didnt work, and even something a simple as refused to work on Windows9x  modular music worked nowhere, to boot. The upcoming release, however addresses all these problems  and more. *music*
A complete list of fixed bugs will likely be available in , but, since that isnt available yet, Ill list the status of bugs whose existence are often questioned. . *history.txt* **Again, these are just bugs that are frequently asked about**
- Trans3
- The message window could not always be successfully hidden with mwincls()
- The RPGCode debugger was buggy  ironic, I know
- RPGCode was unusually slow
- MIDIs and WAVs didnt work in Windows9x (or at least not unless compiled, reportedly)
- and friends caused trans3 to lock up Push()
- Literal variables could not contain the NULL character
- Modular music (*.it and company) would not play anywhere
- Plugins could not be sent variables (yes, this finally enables the multiplayer plugin to work in its entirety)
- Maths that mixed variables with constants did not work
- did not work itemLocation()
- Font styles didnt work
- Toolkit3
- Various windows (like the RPGCode quick reference) crashed when you attempted to move them
- RPGCode capitalizer removed
- Faster color coding in the RPGCode editor
- Problems with pasted code scrolling the window to the top
- Sometimes crashed for no apparent reason
- Tile editor sometimes opened multiple windows
- Tile editor didnt let you use the custom color chooser thingy
- RPGCode program file association didnt work
Features
The previous release was not without a huge selection of features  but paid dearly with its stability, or lack thereof. Version 3.04 provided you with an onslaught of powerful new RPGCode functions and features. It bestowed upon you an overhauled RPGCode editor, a new isometric tile system, tileset manager and an exe compiler. However, many of these things either refused to work altogether or put up so many blockades it should have. 3.05 offers you the best of both worlds, a happy medium, if you will:
- Trans3
- Every game can have a custom cursor  changeable at runtime
- Overhauled movement system
- and friends queue movements if called from a thread or within the new construct Push() multiRun
- Every sprite canand shouldhave its own movement speed
- is used to offset the speed of all sprites movements gameSpeed()
- Object oriented capabilities
- See the *RPGCode OOP Overview*
- New RPGCode commands
- drawCanvasTransparent ( !, x!, y!, r!, g!, b!, [, width!, height! [, !]]) cnv destCnv
- Draws a canvas using transparency
- / getTextWidth (text$) getTextHeight (text$)
- Get the width and height, respectfully, of a string of text rendered in the current style
- mouseCursor file$, x!, y!, r!, g!, b!)
- Changes the mouse cursor to an image or tile,  will remove the cursor, TK DEFAULT will restore the default cursor
- / playerSpeed num!, speed!) num!, speed!) itemSpeed
- Changes the speed of an item or player
- playerStance (num!, stance$) / (num!, stance$) itemStance
- Changes the stance of an item or player (note: does not render, you must call ) forceRedraw
- iif (condition, true, false)
- Evaluates a condition and returns either the true or the false part (which must be the same type)
- Toolkit3
- Overhauled sprite sheet forms (both player and item)
- Can set idle graphics and idling delay
- Individual sprite speeds settable
- Mouse cursor editor
- Can setup and preview your mouse cursor
- Any file format of image works (not just *.cur!)
- Set the hotspot and transparent color
- General
- The editors prompt to save unsaved work
Ending
The 3.05 release is just around the corner and I cant wait to see what the community thinks of it. Weve managed to lose 3.04s nasty pretense andwith any luckpeople will finally consider TK3 to not only be feature-rich, but also . If the release is out by next Monday (which it may or may not be, Ive got money on no), well code the battle system then. Im looking forward to putting 3.05 to the test, I hope you are too! Until next week! **stable**
Dont_Think_So
December 12, 2004, 8:40 pm
I seem to remember an autotiler by Shao... Also, I believe Delano added a few options to the board editor ("Program to run when entering board"). There are probably a few others, too :)
taco
December 12, 2004, 8:50 pm
Nice. I'll have to check it out when it's all done. I might even end up making a game in the thing :)
Raven Ryan
December 12, 2004, 8:56 pm
^ I'll probably learn from the FYOS.
Colin
December 12, 2004, 9:57 pm
I don't know much about the editor, DTS :P
IndustrialMusic
December 12, 2004, 10:24 pm
Hope he/they fix the Edit Enemy box problem. Cant wait to finally also use audio!!
Colin
December 12, 2004, 11:58 pm
"Edit enemy box problem" ?
IndustrialMusic
December 13, 2004, 12:34 am
yes....see my post in the Forums.....theres boxes missing.
EFX
December 13, 2004, 8:34 pm
Hmm... any possibility of animated Cursors (kinda like the FFXI "playonline" cursor).
solaceinsilence
December 14, 2004, 2:34 pm
Wow, you've got me all excited about some of these new RPGCode Commands! And the bug fixes are nice 2. Looking forward to the release, it would be a nnnniiiiicccceeee xmas present!
OBCT
December 19, 2004, 3:07 pm
"Push() and friends queue movements if called from a thread or within the new multiRun construct." I thought the purpose of multiRun was to allow things to happen simultaneously, not in a queue?
Dont_Think_So
December 19, 2004, 6:53 pm
It makes all of the commands run in order in a thread, before moving on to the next thread. It also makes all of the Push commands run at the same time.
Delano
December 23, 2004, 8:32 am
In terms of movement, the "queue" refers to the ability to give each player lists of movements that it runs "at it's leisure" rather than holding up the engine whilst it makes them.
**Column**
Toolkit 3.x > TK3 Amelioration
It's all about the next TK3 release today, as Colin outlines the key fixes and changes in the editor and engine such as the overhauled movement system and new class capabilities. A nice way to wet your appetite before the release later this month.
**Past Columns**
Feb 28, '05
Feb 13, '05
Feb 7, '05
Jan 30, '05
Jan 16, '05
Feb 28, '05
Feb 13, '05
Feb 7, '05
Jan 30, '05
Jan 16, '05
