---
kind: doc
id: "toolkitzone.com/54"
site: "toolkitzone.com"
title: "When I run the Toolkit Editor, it doesn\u0092t work. How do I fix this?"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=54"
written: "2005-09-04T19:25:00"
date_confidence: "exact"
updated: null
captured: ["20060612052826", "20060612052826"]
author: "Marz"
repliers: []
authors: ["Marz"]
comments_present: 0
f_author: "Marz"
f_date: "September 4, 2005, 7:25 pm"
f_description: "First version of Marz's Editor FAQ, featuring many of the common questions concerning the editor and creating your game in general. Questions include; \"How do I make my character fight more than 1 enemy?\" and \"When my character moves on the board, it\u0092s surrounded in white. What\u0092s wrong?\"."
f_section: "Toolkit 3.x"
f_title: "Editor FAQ"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_54", captured: "20060612052826", sha256: "e26a3bb9622afc7bb6e269e0837ae84960f084afc3545e410554fbf64a0b0049", wayback_url: "https://web.archive.org/web/20060612052826/http://toolkitzone.com/library.php?mode=read&doc=54"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_54-a82ca0", captured: "20060612052826", sha256: "e26a3bb9622afc7bb6e269e0837ae84960f084afc3545e410554fbf64a0b0049", wayback_url: "https://web.archive.org/web/20060612052826/http://www.toolkitzone.com/library.php?mode=read&doc=54"}
---

# When I run the Toolkit Editor, it doesnt work. How do I fix this?

** Frequently Asked Questions
Version 1.0 Editor
Welcome to version 1 of the Editor FAQ. If you would like to add any questions to this for the next version, please leave it as a comment. Thank you.
**When I run the Toolkit Editor, it doesnt work. How do I fix this?**
Try deleting everything (Program Files> Toolkit 3), and then reinstalling the latest version. If the problem persists, you may need to ask for help on the forums as you may be missing a file or something on your hard drive.
**Can I make an MMORPG with the Toolkit?**
To make this answer simple, no.
**How big can my sprites be?**
Any size you want. You determine the size of your characters when you make their animations in the animation editor, which allows you to create huge animations. Of course, you dont want your sprite to be too big, so keep that in mind.
**How do I let my character move from one board to another?**
There are two ways to do this. The first way is quite simple. When the character reaches the end of the board, and you want him to move onto the beginning of the next board, all you have to do is go to Board Settings > Board Information (in the menu), and then set the following:
![](library/images/docs/740.JPG)
Northern link is the board to send the character to when he reaches the top edge of the board, southern is bottom edge, et cetera.
**How do I put people other than the main character on the board?**
These other people are called Non-playable characters (NPCs). In the toolkit, they are handled as Items (*.itm). First, you have to have the animations for these items completed (just as you would your main character), then youd have to create a board driven item. See below for more information:
![](library/images/docs/741.JPG)
**How do I make these NPCs talk?**
This is a little bit harder. First, you must create a program in the program editor. This is where you will place the code that makes the character talk: MWin(This is line 1!) //Places text MWin(This is line 2!) //Places text Wait(a$) //Waits for the user to press a button on the keyboard MWincls() // clears the text written MWin(Hey its line 1 again!) // Places text Wait(a$)
**How do I make Boss Fights? How do I make the character fight a specific enemy?**
You have to use the RPG Code command: fightEnemy(). Heres how:
fightEnemy("boss.ene", "background.bkg")
In this case, the character will fight the enemy that was saved as boss.ene, and he will fight them on the background given by background.bkg.
**How do I make my character fight more than 1 enemy?**
Use the same code, except this time add another enemy in the parameters:
fightEnemy("Vampz.ene", "Delano.ene", "background.bkg")
**How do I just make the character fight random enemies?**
Follow this step-by-step to help you do this:
Step 1: Select the 'Edit Enemies' box from the right hand side of the screen.
Step 2: Give it a name, and fill in the remaining fields. Max Health Points is how much HP the enemy will have. Special Move Power will determine how many magic or special moves your enemy can have. Fighting Power will determine how much damage will be inflicted on the player. Defense Power is the number of defense points the enemy has.
Step 3: Select 'Player can run from enemy' only if you want the player to be able to run away.
Step 4: Select the 'Graphics' button from the top right hand of the screen. To make the enemy's size bigger, click on the arrows you see at the top left hand side.
Step 5: Hit the 's' button on your keyboard. If you don't have a tileset of your own, select 'Char.tst' and select a graphic to place in a box.
Step 6: Exit the graphics editor and save the enemy. Then click add enemy to game. Double click on Enemy 0: None, and select your enemy. Give him any skill level that is not 0.
Step 7: For 'chances of getting in a fight' type in a number (for test purposes use 2).
Step 8: Go to the board editor. Click on 'Board Settings' from the menu at the top, and then select the Board Information. Click on the 'Battle Options' tab.
Step 9: Select fighting is permitted on this board. For the skill level, use the level you used from Step 6. If you have a background, click on the 'Background' button and use it.
**When my character moves on the board, its surrounded in white. Whats wrong?!**
When in the animation editor, look at the little information panel at the bottom. Make sure you select the correct Frame Transparent Color. See below for more details.
![](library/images/docs/739.JPG)
**What are tile bitmaps?**
Tile-bitmaps are images made out of tiles. The reason these are useful are so that you can create animations for sprites and other stuff (swaying grass, buzzing bees, etc). Another way you can use tile-bitmaps (not their intended use) is as a way to set down large amounts of tiles at once.
For example, if you have a tree that is 8 tiles wide and 8 tiles long, then its a pretty big pain in the ass to place all 64 tiles every time you want to show that tree on the Board Editor. However, if you place those 64 tiles in a tile bitmap, and then create a single-frame animation, and then place that animation for an item, all you have to do every time you want a tree is place that item on the board. Genius? Lets go over it again:
1. Save large amount of tiles as tile bitmap
2. Make a single frame animation
3. Create a new item (i.e. tree.itm), and give it the single frame animation
4. In the board editor, set the item wherever you want the large amount of tiles to appear.
corim123
September 6, 2005, 7:58 am
nice newb pack!
RPGLand2000
September 9, 2005, 7:57 pm
Of course, you can do a online game, it's just nigh-impossible.
Paper
October 6, 2005, 4:15 pm
How do I take screenshots of a toolkit game?
First version of Marz's Editor FAQ, featuring many of the common questions concerning the editor and creating your game in general. Questions include; "How do I make my character fight more than 1 enemy?" and "When my character moves on the board, its surrounded in white. Whats wrong?".
Jun 7, '06
Apr 5, '05
Jan 26, '05
Dec 23, '04
Dec 12, '04
Jun 14, '05
Jan 6, '05
Dec 29, '04
Dec 22, '04
Dec 17, '04
