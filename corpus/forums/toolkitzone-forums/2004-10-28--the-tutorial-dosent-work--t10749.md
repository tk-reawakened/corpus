---
kind: forum-thread
id: "toolkitzone-forums/10749"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "editor help"
skin: "phpbb2"
thread_id: "10749"
title: "The tutorial dosent work"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10749"
written: "2004-10-28T16:42:00"
last_post: "2004-12-05T20:00:00"
date_confidence: "exact"
captured: ["20050115140450"]
author: "Knght of hope"
repliers: ["Nick", "RetroGamer", "ASDF", "rpgmaster24", "RDX(not logged)", "Caliber Mengsk", "Mystinar"]
authors: ["Knght of hope", "Nick", "RetroGamer", "ASDF", "rpgmaster24", "RDX(not logged)", "Caliber Mengsk", "Mystinar"]
posts_present: 9
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135160_amp_", captured: "20050115140450", sha256: "a87eaa8b5ad7eb76ea950d0ff3e73e1b6338b98ca2d55b58ca39fc36a0e36102", wayback_url: "https://web.archive.org/web/20050115140450/http://www.toolkitzone.com/forums/viewtopic.php?p=135160&amp="}
links:
  - {url: "http://www.toolkitzone.com", status: "captured", local: "wayback/toolkitzone.com/index"}
  - {url: "http://www.toolkitzone.com,", status: "external", local: null}
---

# The tutorial dosent work

### Knght of hope · 2004-10-28 16:42 · #B118293

My wont it work? I click on it and up pops a box wit "tutorial", press ok and bye bye box. so whts up?

### Nick · 2004-10-29 01:39 · #B118569

Apparently, sir, you don't share the same sense of humor the dev team does Very Happy
Actually it was just cbm being lazy. The next release is to have a complete tutorial in it. In the meantime, I'll just keep on copying/pasting my own.

**Quote:**

> //Page 1, Introduction
> Welcome to RPG Toolkit 3! Like most people, you're probably wondering how this whole thing works and if it'll be hard. Well, that's what this tutorial is for.
> First you should learn a bit about the layout. This big screen with everything is called the IDE, or Integrated Development Environment. Up on top you can see some universal tool buttons. From the left to right, there's new file, Edit Main File, Open, Save, Save All Files, The Bard (Media Player), [www.toolkitzone.com,](http://www.toolkitzone.com,) Online Chat Room, Config, Edit Tileset, and Test run Game. Above it are the text toolbars, which will change depending upon which editor you have open.
> On the left is the blank Tools box. It will show different buttons for each editor. On the right are some accessories. The folder opens a little filebrowser of all your game's files. The blank page opens a TK2 style "New" toolbar, andthe black box opens a tileset browser.
> The rest of this tutorial will show you how to make a basic game, including a player who walks around and some RPG Code. Yes, there's that -code- word again. But don't worry, it's very easy.
> //Page 2, Step 1
> The first thing you need to do is start a new game. Go up to the File button in the top-left corner, and click New Game. A dialog will appear. Simply enter the name for your game (anything is fine) and click "Setup my Game!" Some files will be tossed around and you'll see your game's Main Project File. This editor lets you change some primary options and setup for your game. I would turn off "Enable Joystick," as it's rather slow. You can leave everything else as it is. Make sure to Save by clicking the Blue Disk up on the toolbar.
> When you setup your game, it created some files. You currently have a blank character and blank board, and that's about it. Click the folder on the right to see your game's folders. Expand "Boards" by double clicking on it. Double click start.brd to open it.
> //Page 3, Step 2
> Okay, so you have a blank board here. Boards are the maps your players walk around on. They're made up of tiles, which are little images (32x32 pixels to be exact). This board has some grass, but you need some content. Let's make a house or something. First you should maximize the TK and board editor just for convenience. Click the black square on the right to open the Tileset browser. Click the folder icon on the top right of this dialog, and open "Default.tst." A bunch of tiles will popup. Just click one to select it, then click on the board where you want to put it. Do something basic like make a little house. When you're done where you're house, go up to Board Settings and click "Set Player Position." This option defines where the player appears when you start the game, so click where you want the player to start. Now click the Blue disk to save, and the green arrow to test run. The Translator (Game Engine) will open up. Start a new game, and walk around or something. Close it when you're done.
> //Page 4, Step 3
> Now you probably noticed that your player can walk over the house, right? Don't worry, that's something we'll fix next. Return to the board editor. On the Tools (left), click the icon that shows a lock with a blue arrow pointing to it. This is called the Tile Type Lock. You use it to define how each tile acts when the player walks on or around it. You might also want to turn on the grid (top left button) so you can see easier. You'll see that right now everything has a gray arrow over it. That means it's "Normal," so the player can walk over it. You want to make the house Solid. On the bottom of the Board editor, you see a Tile Type box showing a bunch of colored arrows. Click the Blue one. That's Solid. Now click the tiles on your board where you want the tiles to be solid (Player can't walk on it). The other TileType you'll use a lot is Under. Click the Pink arrow. Under Tiles mean the player can go behind the tile, which is good for walls or something. On the back of the house, where you could have the player run behind the house, make those tiles Under. Now Save your board (Blue Disk) and test run again (Green arrow).
> //Page 5, Step 4
> Now your board works like a real game. ^^ But it's so plain, you want more to your game, right? Let's make an NPC that talks to you.
> An NPC, or Non-Playing-Character, are little people in your game that make it seem more alive or further the plot around. Turn on the Draw Lock in the board editor (The lock with slider, next to the Tile Type Lock), and close the board editor. Also close the tile browser.
> Back to that blank screen. Go up to the little blank page button in the top-left of the screen, and click the arrow pointing down next to it. You'll get a dropdown menu. Click "RPG Code Program."
> You just made a new (Blank) RPG Code Program. These are essentially text files, but they contain a series of commands that tell the engine what to do. It's pretty simple, it just runs each command one step at a time. You're going to make a really basic script that will make an NPC Talk to you.
> In your new (blank) program, put in the following text:
> Mwin ("Hello, I'm Mr NPC Man")
> Wait
> Let me explain those. MWin (Message Window) simply shows a message window and says whatever text you entered. Wait waits for the player to press a key. Click the Blue Disk to save it, and name it NPC.prg. Go ahead and close the program editor.
> //Page 6, Step 5
> Now that you have a basic script, you need to use it. It's just there right now. Go up to the New Icon (blank page) and create a new Item.
> "Item" is a bit of a misleading name. It really should be called Object. Items can be anything from a sword on the ground to a NPC or even a creature. For the Handle, just name it "NPC" or something. Check the box marked "Board Driven," then click the Edit box next to it. For "Program to run when item is picked up," click Browse, select NPC.prg and click Okay. Now click the Graphics button. You really only need something for "Rest," as your NPC won't be walking around. So highlight the "Rest" frame. This shows some options for animations. Click Browse, and select Start_s.anm. Then click Okay. Save your item, with the blue disk, and call it NPC.itm. Close the Item Editor.
> //Page 7, Step 6.
> Next we'll put the item in your game. Go over to the folder icon and open up Start.brd again (Boards will probably already be expanded since you opened it last). On the very top of the screen, select RPG Code and then Set Item.
> Click Okay on the dialog, then click where on the board you want the NPC to be. A dialog will appear showing some minor options about this item. Click Browse and Select "NPC.itm," then just click Set Item. Save your board and test run your game. Once in-game, walk up to your NPC and he'll say whatever you typed in the RPGCode Program. Pretty l33t, no?
> //Page 8, Step 7.
> The last thing I'll show you how to do is make another board that you can walk to.
> Close the board editor, then go up to New > new Board. First thing you need to do is resize the board. Go up to Boart Settings on top, and open Board Information. Click the "Size Tab" and make your board 20x15, by pressing the up and down arrows next to the appropriate box. Click okay. Your board will resize itself. Open the tile browser (black square on the right), it should automatically show default.tst. If it doesn't, you know what to do. Select the first tile, the Grass tile. On the toolbar on the left, select the Flood Fill tool (Bucket of paint spilling over). Click anywhere on the board and it will all beome grass. Click the Draw Lock tool (Lock with slider). Now just make up another scene similar to the last one. Like you did with your first board, change the tiletypes of each tile to whatever you want (Solids and all). Once you're finished with your second board, we need to link it to your first. Go up to Board Settings on the top, then Board Information.
> Since this will be a board south of your first board, you want to be able to get to the first board by walking up on this board. So for the Northern Link, Browse and select Start.brd. Click Okay, and save your board as board2.brd.
> Open up the filebrowser and open up Start.brd again. Go up to Board Settings > Board Information, and for the SOUTHERN Link, select Board2.brd. Click okay and save your board. Then Testrun your game. Walk to the south of the board you're on and you'll go to the next map. Walk back and you'll return to the first map.
> //Page 8, Closing.
> So now you've made a game, albiet small, it's a game. There is a lot more you should read and do before really creating your game. Just play around with the board editor and learn how it works. Also, in the main IDE, go up to Help and run the Table of Contents.This is a detailed help file that will tell you almost everything you need to know about the TK. It's outdated, but most of its points are still valid. There is also the RPG Code Command Reference and RPG Code Primer. Both of these documents will really help you to get started in learning RPG Code.
> Also, check out <http://www.toolkitzone.com> online and join the community. You can ask for help there (Always check the help files first), make suggestions, or just talk about whatever. You'll find a lot of people there willing to help you.
>

And of course after reading this and the help files, you're welcome to ask questions here.

### RetroGamer · 2004-10-29 01:47 · #B118571

That avatar picture thing you have scares me Sad
that tutorial is fresh... snip

### ASDF · 2004-11-01 02:34 · #B119832

Thanks for the tutorial

### rpgmaster24 · 2004-11-10 21:07 · #B123497

8O What's goin on here? Dancin' Pickle man everywhere!? Oh, well, it gave me a tutorial, I guess it's cool.... or is it?

### RDX(not logged) · 2004-11-10 22:52 · #B123572

BAD PICKLE ... BAD!
Laughing
RDX

### Nick · 2004-11-10 23:53 · #B123619

That pickle was a pornstar before he became a dancer.

### Caliber Mengsk · 2004-11-11 00:07 · #B123629

... I feel sorry for the sheep and goats that stared with him Nick... ^_~ hehehe.

### Mystinar · 2004-12-05 20:00 · #B135160

Nick, your avatar is making me paranoid.
