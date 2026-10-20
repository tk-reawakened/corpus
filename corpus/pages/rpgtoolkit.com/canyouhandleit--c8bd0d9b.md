---
kind: page
id: "rpgtoolkit.com/rpgtoolkit.com/canyouhandleit/"
site: "rpgtoolkit.com"
title: "Now In Development"
original_url: "http://www.rpgtoolkit.com/canyouhandleit/"
written: null
date_confidence: "unknown"
updated: null
captured: ["20030402062709"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.com/canyouhandleit/index", captured: "20030402062709", sha256: "8b46f814f91947000f0182c1c483933786d1ba137ea4bae452caf3a3cdc4beee", wayback_url: "https://web.archive.org/web/20030402062709/http://www.rpgtoolkit.com/canyouhandleit/"}
---

# Now In Development

![tk3.jpg (12325 bytes)](images/tk3.jpg)
***Now In Development***
Version 3.0 of the RPG Toolkit Development System has been under heavy development all summer. TK3 is a true next-generation RPG development system with a focus on speed, graphics and flexibility. Like its predecessor, TK3 hopes to set a new standard in RPG development throughout the game creation community by offering users a unique development experience to help them bring their ideas to life.
***Modern Interface***
The main editor has seen a major overhaul since version 2. New features include:
[![MDI](images/mdi_small.jpg)](images/mdi_big.jpg)
You can open multiple files simultaneously
- Allows you to open and edit multiple files at once (such as the ability to edit 2 or more boards at a time). **MDI interface:**
- The various editors conform to the same basic design by locating tool palettes and additional features in the same locations. **Consistent interface:**
- Menus are consistent across the various editors. **Consitent Menus:**
***Modern Features***
TK3 sports several new features for creating modern games. New features include:
![isometric.jpg (8147 bytes)](images/isometric.jpg)
All tiles can render isometrically
[![boardedit_small.jpg (39291 bytes)](images/boardedit_small.jpg)](images/boardedit_big.jpg)
You can mix 2D and 3D boards in your game
[![sprites_small.jpg (19463 bytes)](images/sprites_small.jpg)](images/sprites_big.jpg)
You can have any number of sprites at any resolution
- All tiles can be displayed in the standard overhead 2D format, or in a 3D isometric format. Isometric tiles are automatically processed to increase their quality so they will render with the same detail as their 2D counterparts. **Isometric tiles:**
- Your game can have any combination of 2D or 3D isometric boards. And the board editor can do both, of course! **Isometric and 2D boards:**
- All movable objects (characters and NPCs) now use the Toolkit's animation format to represent movement animations. This means that you can have any number of animation frames for each movement. Additionally, characters can be any size you wish them to be. Further, you can define your own animation types for battles (for different special moves, or anything you want). **Sprites:**
- As with every release of the Toolkit, backwards compatibility is maintained. If you open a version 2 file, or one is opened while the game is playing, the Toolkit will automatically import it as a version 3 file. This means that animation files will automatically be created for all your characters an NPCs as they are opened. **Automatic importing:**
- As with vesrion 2, TK3 has the ability to display its interface in a wide range of languages. The initial release will be in English, and otjer languages will likely follow. **Multilingual:**
***Modern Engine***
The trans3 game engine is now beginning development. The old version 2 code is being largely re-written to accomodate the goals and requirements of TK3. Features include:
[![trans3_small.jpg (178766 bytes)](images/trans3_small.jpg)](images/trans3_big.jpg)
The trans2 engine has been largely re-written from the ground up to create trans3 -- a new engine that can meet the requirements of TK3 games.
- You can continue to work on your game with version 2. The transition to version 3 should go smoothly as the engine and the editor will be able to open all the version 2.20b stuff without any work from you. **Fully compatible with Version 2:**
- Written in entirely in C++, the new graphics subsystem can run entirely through DirectX 7 or the Windows GDI. Speed is the most important factor here, and DirectX delivers! **New graphics system:**
- The menu systems are being completely re-done to work with the new graphics system. **New menus:**
- The fighting system is being removed from the engine entirely, and it's being completely re-written. Instead, it will interface with the engine like a regular plugin would. This will give you the ability to plug in your own battle systems and even swap them while the game is runing. **Pluggable fights:**
- Toolkit 2 could extend its power with user-created plugins. TK3 will maintain the old plugin interface and add new callbacks to access the new graphics system directly. Further, manipluation of player and enemy data will be easier with TK3 plugins. **Updated plugin interface:**
- The main execution loop for TK3 is being completely re-done from the ground up. Mutlitasking will now proceed almost transparently. NPCs and players will be able to walk at the same time without pausing (and other nice things). **True multitasking:**
[![menu_small.jpg (22187 bytes)](images/menu_small.jpg)](images/menu.jpg)
The new menu system is provided by a plugin. Don't like the menu? Plug in another!
[![trans3under_small.jpg (49519 bytes)](images/trans3under_small.jpg)](images/trans3under_big.jpg)
trans3's graphic engine is modern and advanced. It sports fast offscreen buffers and quick on-screen translucency.
This is all very preliminary. The editor is nearly complete at this stage; I have worked on it all summer. I'm just beginning to work on the engine now-- I plan to work on it all this fall (at present, only the new graphics system is done. The other stuff is in the planning stages, but I'm very certain about how I will go about coding that stuff). I can't set a release date yet, but if all goes well, I may have a working alpha version by the end of the Fall. No promises, of course. I do this in my spare time, and I don't know what my schedule will be like this fall.
Anyway, stay tuned. It's bound to be a fun ride...
