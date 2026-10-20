---
kind: page
id: "toolkitzone.com/toolkitzone.com/toolkit.php?faq="
site: "toolkitzone.com"
title: "FAQ"
original_url: "http://www.toolkitzone.com/toolkit.php?faq="
written: null
date_confidence: "unknown"
updated: null
captured: ["20070219132941"]
author: null
repliers: []
authors: []
comments_present: 0
f_about: "No matter your skill level, at one point or another, you will experience some sort of trouble. Here are the most frequently occurring problems and their remedies."
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/toolkit.php__faq_", captured: "20070219132941", sha256: "4d1b0bcc8dcc89e4bf9f00e5c493e8ced693552d835486d5f37d0cc4ba310ef3", wayback_url: "https://web.archive.org/web/20070219132941/http://www.toolkitzone.com:80/toolkit.php?faq"}
---

# FAQ

Frequently Asked Questions
This is a collection of common questions on the Toolkit and game-making. Technical problems can be found separately in . If you can't find what you're looking for, then please post a question in the support forums at . This list is under constant revision; feel free to submit your questions (with answers) in the same forums. [Technical Issues](http://tk3.toolkitzone.com/help/?page=25) [ToolkitZone](http://toolkitzone.com/)
GeneralEditorRPGCodeGameplay [Open Source and Development](http://tk3.toolkitzone.com/help/?page=23#section_5)
General
Can I use the Toolkit to create an online game or MMORPG (massive, multiplayer online RPG)?
Generally speaking, no. Technically it is possible through , but it has not yet been achieved. More information can be found in a TKZ article . [plugins](http://tk3.toolkitzone.com/help/?page=18.4#adv.e) [here](http://toolkitzone.com/library.php?mode=read&doc=88)
Can I play/edit a Toolkit version 2 game with Toolkit version 3?
Yes—although you may have to edit some parts of your programs and remake some of your game files.
To start, copy your game files from your Toolkit2Game folder to the Toolkit3Game and the main game file from Toolkit2Main to Toolkit3Main—make sure you keep a copy of the old files in case anything goes wrong. As a precaution, open your game files in the TK3 editor and resave them to convert their format to TK3; specifically for character, item, board and animation files (tiles and programs do not require conversion). You may find in the case of characters and items you need to reconstruct the file completely.
With your programs, you will find that some commands have been removed or upgraded for TK3—watch for the debugger when testing them for information on upgrading.
Editor
I made a (insert object here) but it doesn't work!
This is quite a common complaint, and a lot of the time it's due to the object not being saved before test-running the game. Try hitting "Save All" in the toolbar before testing. It might not always be the case though! Of course, you should consult the relevant editor help page too.
How do I make walking graphics for characters/items/enemies?
In TK3, movement graphics have to be created using (*.anm). One animation has to be created for each direction (that you want the player/item to move in) or action. To make an animation, load its editor and click the white box to add an image for the first frame. Use the toolbar buttons to add more frames. [Animations](http://tk3.toolkitzone.com/help/?page=10)
How do I place more than one tile in an animation frame?
Each frame can only hold one "image", so you need to make an image out of the tiles you want in the frame—a . To make a tile bitmap (*.tbm), load its editor and resize the image to the required dimensions. Then add tiles to it as you would the board editor. Tile bitmaps can be selected as images for animation frames. [Tile Bitmap](http://tk3.toolkitzone.com/help/?page=11)
How do I make an NPC walk around?
In Tk3, an NPC (non-player character) is an Item with walking graphics. After creating and animating the NPC, check the "Board Driven" option to let this item be active on a board and click the corresponding "Edit". For "Program to run while item is on board" select "wander.prg" for basic wandering, or you can write a more complex routine using the PushItem() command and a loop. Then place the item on a board (RPGCode > Set Item in the board editor).
How do I make a door that sends the player to another board?
As well as directional links, players can also move between boards using Warp Tiles (and the Send() command). To make a door, first make the origin and target boards (e.g., the outside and inside areas of a house) and remember the location where you want the player to appear (x, y and layer). On the origin board, go to RPGCode > Set Warp Tile and click the tile on the board that corresponds to the door, then fill out the details of the target location in the window that appears. Note that this is only a "one-way" connection and you must add another Warp Tile if you want the door to work in reverse.
I've made a warp tile, but nothing happens when I walk on it!
There are several possibilities:
- Check you saved the board before testing.
- Check that the target board exists and the details were typed in correctly.
- Check that the Warp Tile has been set that the player is walking on. *on the same layer*
- If your player appears at the edge or corner of a board, check the target coordinates of the warp tile (warp tiles are just standard programs of the form warpxxx.prg where xxx is a number)
RPGCode
Is the TK2 * comment still valid?
To a degree.
The comment used in TK1–2, *, was picked by Christopher B. Matthews when long term development was not a consideration. It managed to stay throughout all TK2 releases because of that version's simple line-by-line RPGCode parser. With the introduction of a much more elaborate, less restrictive, parser in recent TK3 releases, the *, due to it being the multiplication operator, can no longer be successfully understood as well as in TK2. For whole-line comments, it will continue to function in the foreseeable future, but we recommend consistent usage of the far superior // comment.
What's this I hear about not using branch?
Because performs an unconditional jump to what could possibly be a whole other area of a program, it creates illogical, unreadable, and unmaintainable code. It is generally regarded as a very poor programming practice, and is never required in favour of more friendly language features (e.g., ). A more detailed answer can be found in the famous essay , by Edsger W. Dijkstra. *branch* [loops *while*](http://tk3.toolkitzone.com/help/?page=18.2#con.while) [*Go To Statement Considered Harmful*](http://acm.org/classics/oct95)
Gameplay
I've made a board and a player, but when I test-run my game, my player and/or board doesn't appear!
My player moves really slowly; what's wrong?
Player speeds are dependent on a number of factors. Firstly, as of all players and items can have individual speeds assigned to them in the Graphics window of their editors. The value here is a delay, in seconds, rather than a speed so lower numbers correspond to faster movement. A value of between 0.05 and 0.2 is recommended, but you can set any value you wish. [3.0.5](http://tk3.toolkitzone.com/help/?page=29#3.0.5)
This is an absolute value and the Toolkit will endeavour to move the object as this speed on all machines. However, it may be the case that your pc is unable to match this speed, in which case it will run them as close to it as possible. A way to gauge the performance of your pc is through the frames-per-second rate (fps) of the engine. This can be seen in windowed mode by enabling the option in the of the . A low fps (< 20) is indicative of the pc running at maximum capacity. [graphics tab](http://tk3.toolkitzone.com/help/?page=3#graphics) [Main File Editor](http://tk3.toolkitzone.com/help/?page=3)
One other option that you may be tempted to use is GameSpeed(), and its main file option. One cause of slow movement may be the fact this is set to a low value; set it at zero for unaffected gameplay. If your pc is running at capacity, increasing GameSpeed() won't have any effect on movement.
What's GameSpeed() for then, if it should be set at zero?
The idea of GameSpeed() is that it gives the players a mechanism for altering the speed of your game. For instance, you could create a menu option with a graphic slider, or a run-time program with associated keys to increase or decrease the setting.
Open Source and Development
Where can I download the source code?
The SourceForge page, , contains the latest official sources. The current development source can be found . [sourceforge.net/projects/rpgtoolkit](http://sourceforge.net/projects/rpgtoolkit) [here](http://tk3.toolkitzone.com/source)
May I sell my game made with Toolkit 3?
You are free to sell games you make in the RPG Toolkit (Version 3.0.x). You must, however, give credit for the use of the RPG Toolkit itself. You must either own all resources used in your game or have full permission from the author of the resources to use them in a commercial product.
No matter your skill level, at one point or another, you will experience some sort of trouble. Here are the most frequently occurring problems and their remedies.
Frequently asked questions.![TBD](templates/default/images/icons/more.gif) **[1. FAQ](toolkit.php?faq)**
