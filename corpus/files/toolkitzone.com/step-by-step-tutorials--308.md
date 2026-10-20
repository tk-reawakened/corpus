---
kind: file
id: "toolkitzone.com/308"
site: "toolkitzone.com"
title: "Step by Step Tutorials"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=308"
written: "2004-02-21"
date_confidence: "day"
updated: "2004-02-21"
captured: ["20051018035041", "20051031040943", "20051031044711", "20051105123222"]
author: "Marz"
repliers: []
authors: ["Marz"]
comments_present: 0
f_author_source: "Marz"
f_name: "Step by Step Tutorials"
f_submitted_by: "Marz"
f_version: "1.00"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_308", captured: "20051018035041", sha256: "22fa26b97f51383a71ae6b5fb1843b0271bb954b6a4a66218f9a971de65783af", wayback_url: "https://web.archive.org/web/20051018035041/http://www.toolkitzone.com/fileman.php?id=3&file=308"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_308", captured: "20051031040943", sha256: "d91e4ca57b2217270aecc2c7bd33305df2956869ca48e562691def07c64937db", wayback_url: "https://web.archive.org/web/20051031040943/http://www.toolkitzone.com/fileman.php?id=10&file=308"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_7_file_308", captured: "20051031044711", sha256: "5041777718604b2b7a8194736b82da46fa0c6c519fcd5dcebcbdfe7ad3b45475", wayback_url: "https://web.archive.org/web/20051031044711/http://www.toolkitzone.com/fileman.php?id=7&file=308"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_308", captured: "20051105123222", sha256: "f7748686eca974c0abb73e6a500bf2c6dafcc1b7df31302f058c93d50763c623", wayback_url: "https://web.archive.org/web/20051105123222/http://www.toolkitzone.com/fileman.php?id=5&file=308"}
---

# Step by Step Tutorials

Very nice "Step by Step Tutorials" to ease you through the process. In this case there are no terribly complicated topics discussed, but when I was a nooby I remember having problems with these same issues. Excellent job Marz.
**Step-by-Step Tutorials**
A load of step-by-step tutorials brought to you by Marz for your aid in doing the simple things with the Toolkit. This version is 1.00, and is compatible with the last version of TK2, but has not yet been tested with TK3. If you have any suggestions or would like to see another step-by-step tutorial, then don’t hesitate to email me at: (redacted: email)
Adding Enemies
: Select the 'Edit Enemies' box from the left hand side of the screen. **Step 1**
: Give it a name, and fill in the remaining fields. Max Health Points is how much HP the enemy will have. Special Move Power will determine how many magic or special moves your enemy can have. Fighting Power will determine how much damage will be inflicted on the player. Defense Power is the number of defense points the enemy has. **Step 2**
: Select 'Player can run from enemy' only if you want the player to be able to run away. **Step 3**
: Select the 'Graphics' button from the top right hand of the screen. To make the enemy's size bigger, click on the arrows you see at the top left hand side. **Step 4**
: Hit the 's' button on your keyboard. If you don't have a tileset of your own, select 'Char.tst' and select a graphic to place in a box. **Step 5**
: Exit the graphics editor and save the enemy. Then click add enemy to game. Double click on Enemy 0: None, and select your enemy. Give him any skill level that is not 0. **Step 6**
: For 'chances of getting in a fight' type in a number (for test purposes use 2). **Step 7**
: Go to the board editor. Click on 'Board Settings' from the menu at the top, and then select the Board Information. Click on the 'Battle Options' tab. **Step 8**
: Select fighting is permitted on this board. For the skill level, use the level you used from Step 6. If you have a background, click on the 'Background' button and use it. **Step 9**
Create an Item
The following Step By Step tutorial should be used to create an NPC, or an item that can walk.
: Open the item editor from the left of the screen. **Step 1**
: Select the 'Graphics' Button. **Step 2**
: Select the lower box of the first white rectangle. If you don't have another tileset, select 'Char.tst' **Step 3**
: Place the first front walking graphics in the first box. **Step 4**
: Rinse and repeat for the other boxes. **Step 5**
This next Step by Step tutorial should be used to create a simple item that doesn't move (e.g. a chest).
: Open the item editor from the left of the screen. **Step 1**
: Select the 'Graphics' Button. **Step 2**
: For the 'Standard Rest Graphic' select the lower box and using the tileset you have, select the graphic. **Step 3**
**NOTE: If you want to erase a graphic, do not replace it. Instead erase it by clicking on the blue and white eraser on the lower right hand side, and select the box you want to erase.**
Walking NPCs
: Select the option 'Board Driven' in the Item Abilities section of the item editor **Step 1**
: Beside the option, click 'edit' **Step 2**
: In the field "Program to run while item is on board" type in wander.prg **Step 3**
: Go to the board editor for where you want your NPC. **Step4**
: Under the 'RPG Code' menu select 'set item' **Step 5**
: Click on the starting position of the NPC on your board **Step 6**
: Browse and select the item you made (which is the NPC) **Step 7**
: Click 'Set Item' **Step 8**
Using Plugins
: Download the plugin. **Step 1**
: Unzip it if it's a zip file **Step 2**
: Put it in your toolkit Plugin Directory (e.g. C:\Program Files\Toolkit2\Plugin) **Step 3**
: Read the readme to learn how to use the plugin's commands. **Step4**
: Use any of the commands needed in your programs. **Step 5**
Talking NPCs
: Go to the program editor and create a program that displays text (for example: #MWin(“This is text”) and then save it. **Step 1**
: In the board editor under the 'RPG Code' menu select 'Item Menu' **Step 2**
: Double click on the NPC (or item) you want to display text. **Step 3**
: Click on advanced and for 'Activation program' browse for the program you wrote that makes your NPC talk (the one from Step 1). **Step 4**
**Browse Sections**
