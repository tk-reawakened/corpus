---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/tutorials/editor/marzs-how-to-guides/like/"
site: "rpgtoolkit.net"
title: "March 7th, 2009"
original_url: "http://rpgtoolkit.net/tutorials/editor/marzs-how-to-guides/like/"
written: "2009-03-07"
date_confidence: "day"
updated: null
captured: ["20110318071502"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/tutorials/editor/marzs-how-to-guides/like/index", captured: "20110318071502", sha256: "f03563a584388db7bf19664c9250702e7cd906389e3e886c73d41c8c2d79def3", wayback_url: "https://web.archive.org/web/20110318071502/http://rpgtoolkit.net/tutorials/editor/marzs-how-to-guides/like/"}
---

# March 7th, 2009

[![Marz](thumb/80/community/images/avatars/upload/86425383345de15b08496f.jpg)](member/marz/)
Published
**March 7th, 2009**
Read times **586**
Written by Marz
Marz's How To Guides
**A collection of "how to" guides for using the Toolkit, such as creating animations and enemies.**
1. How To: Create an Animation
2. How To: Create an Enemy
How To: Create an Animation
This guide shows you how to create an Animation in the RPG Toolkit. Animations are used for enemies, players, items, special moves, etc so they can be pretty damn important. This guide focuses on creating an animation for a sprite, but you should be able to use this tutorial to create any kind of animation. By the end of this tutorial you should know how to:
- Understand the basics of the Animation Editor
- Add/Remove frames in the Animation Editor
- Set a transparent colour for the animation
- Change how fast or slow the animation plays
Step 1 - Getting the Images
An animation is made up from a collection of images, tiles, or tile bitmaps.
If you made the graphics for the animation in something like MS Paint or Photoshop, copy those files then paste them into your game's Bitmap folder. If you are making a large game, it's probably a good idea to paste these images in another folder that's inside Bitmap. For example, if this animation is for a character called "Frap", you might make a folder inside Bitmap called "frap", and then paste those images. In terms of naming those images, it's probably a good idea to name them in the order you want them to be animated. So using our previous example of Frap, we would have his south walking animations labelled as: frap_south1.PNG, frap_south2.PNG, etc** 1a - Collection of Images
This really only applies if you are using an animation that is only a maximum 32x32 pixels wide. This is because tiles in the toolkit are limited to 32x32 pixels. If your animation is not already in tileset form (e.g. you downloaded the tileset animations from the Toolkit Zone) you will need to import the tiles using the Tile Editor.** 2a - Collection of Tiles
If your animation is more than 32x32 pixels but they are saved as tiles, then you can create a tile bitmap. This is the same as using an image in 1a except you create the image using tiles in the toolkit. To create a Tile Bitmap, click on File->New->Tile Bitmap and save the images in the Bitmap folder exactly as you would in 1a.** 3a - Collection of Tile Bitmaps
Step 2 - Setting up the Size
Load up the animation editor by going to File->New->Animation. The white square you see is what we will fill up with an image. First, on the bottom left hand side is the "Size" panel. Set the size of the animation to how big your character will be. It's a good idea to use multiples of 32. I choose 32x64. You should see the size of the white square change depending on what size you put in.
Step 3 - The First Frame
Click on the white square. You should see a window pop up.**
3a - Assuming you saved your files in the Bitmap folder as in Step 1, go there and find the first frame of the animation. Then select it. If you have everything saved in a tileset, go to the Tiles folder, find the tileset you saved the animation tiles in, and then click on the animation tile you want. If you did you should see something like this. That's a rabbit in case you were curious. If you did you should see something similar, except you should be using a size of 32x32.
**3b-**
**3a** **3b**
We're not done yet! Next we need to set the Transparent Colour. Notice how my character has pink all around him. I don't want that to show in the actual game, so in the middle of the bottom frame in the panel, click on and then click on any of the pink area in the background. *Frame Transparent Color* **Select**
Step 4 - Inserting the Next Frame
To insert another frame, on the left hand side there is a button labeled "Ins", click on it and a new white square should pop up in place of the old square. Don't worry, the old square with your character is still there. Now go to and do everything again. If the transparent colour is the same in all your picture files, then you don't need to select it every time. It's a good idea to check to make sure that the transparent colour is set though. When you're done adding frames, go to . **Step 3**
**Step 5**
Step 5 - Changing the Speed
So we're done adding frames, now test run the animation by pressing the shaped button on the left-hand side (the black one). If you feel the animation is going too fast or too slow, you can change that by going to the panel at the bottom and moving the slider towards Fast or Slow. Press play again to see the animation run again until you're satisfied. **Play** *Frame Delay*
* Note: For sprites, changing the animations speed does NOT change how fast a character walks in the game. It only changes how fast the animation plays WHILE he is taking a step.
Step 6 - Wrapping it Up
Okay, now we just need to save! Press Ctrl+S to save the animation file. Note that it gets saved in the "Misc" folder for your game. You may also want to create a new folder in there for your character. It's also recommended that you name the animation something meaninful. Using our previous example, I'd save the animation in a folder in Misc called "Frap" and give the animation the name "Frap_s".
Animation Editor Overview
![](vault/images/17_2.PNG)
The arrow keys on the top allow you to cycle through frames. You automatically start out with 1 frame. If you click the "Right" arrow and you are on the last frame, it will create a new frame (alternatively, you can press the "Ins" button to a new frame). You can press the delete button to delete the frame you are currently looking at. The "Play" button allows you to run a test run of your animation. **Circle 1**
*insert*
**Circle 2****
Displays the current frame. If no frame is there, then you see a white square. You can click on this area to select a picture or tile to put in the frame.
The size of your animation. If you choose a size that is bigger than the picture or tile you selected for the frames, then the RPG Toolkit will stretch the tile/image.** Circle 3
The speed of the animation. You can make the animation run very slowly or very quickly.** Circle 4
The transparent color of the frame. This is very important! If the transparent color is not set then you will see that color in the actual animation instead of, for example, grass.** Circle 5
This allows you to see where the frame's image is coming from. Also it allows you to add a sound effect to the animation.** Circle 6
How To: Create an Enemy
This guide shows you how to create an enemy in the RPG Toolkit. By the end of this guide you will know how to
- Use the basics of the Enemy Editor
- Give Experience and/or Gold to the player when he defeats an enemy
- Add an enemy to the RPG Toolkit's fight system
- Randomly encounter the enemy on specific boards
Step 1 - Enemy Editor
Open up the Enemy Editor by clicking on "Edit Enemy" on the right-hand toolbar.
![](vault/images/17_3.png)
There are three buttons on the very right hand-side of the RPG Toolkit Editor. Click on the second one. That is, click on the one below the "Folder" icon and above the "Black Square" icon. **Can't see the toolbar?**
Step 2 - Fill out the Fields
Now you must fill out the fields in front of you. The name of the enemy. When a fight starts with this enemy, they will start off with their Max Health Points as their Health for the battle. When a fight starts with this enemy, they will start off with the amount of Special Move Power you give them. Special Move Power is used for Special Moves, and works similar to Mana. The amount of fighting power the enemy has (aka "FP"). This is how strong the enemy's attacks are. The amount of defense power the enemy has (aka "DP"). This is how resistant the enemy is against incoming attacks.
**Basic Info**
**Max Health Points:**
**Special Move Power:**
**Fighting Power:**
**Defense Power:**
If you check this, then when the player encounters this enemy in a battle he can run away from the enemy if he wants. You will probably want to check this for most of your enemies, but not for Bosses. When the player runs away you have the option to run a program (a .prg file). This can be useful if, for example, you wanted to add a penalty for running away. For example, the player runs away but dropped 10 gold. You can give the player a chance to critically hit the enemy. Critical hits cause more damage than normal hits. If you want a 20% chance for the player to critically hit the enemy, then you would enter the value 5. How did I know this? Use this formula: 1/(Percent Chance to Hit in Decimal Form) = Value to enter A 20% chance is: 1/(0.20) = 5 A 15% chance is: 1/(0.15) = 6.67 A 23% chance is: 1/(0.23) = 4.38 Same as above, except this is the enemies chance to critically hit the player.** Fighting Conditions Player can run from this enemy:
**Program to run when player runs:**
**Chances of a critical hit on the enemy (1 in):**
*Note: If you leave the value at 0, the player cannot critically hit the enemy.*
**Chances of a critical hit on the player (1 in):**
Step 3 - Adding Graphics
Now we want to make the enemy have some animations in the battle. If you skip this step, then you will have an invisible enemy! Click on the "Graphics..." Button.
![](vault/images/17_4.PNG)
There are 5 default animation slots that need animations, each one is important: When nothing is happening in the battle (for example, when waiting between turns) this animation is played. When it is the enemy's turn, and it attacks, it uses this animation. When the enemy is attacked by the player, this animation is played. When the enemy uses a special move, this animation is played. If the player kills the enemy, this animation is played. To set the animations, click on each one individually, then click on "Browse" and select the animation file you want. Do this for each of the above. The only one you can skip is "Special Move" if the enemy doesn't use special moves anyway.
**Rest:**
**Attack:**
**Defend:**
**Special Move:**
**Die:**
![](vault/images/17_5.PNG)
When you are done, click on the "Okay" button.
Step 4 - Experience and Gold Rewards
When the player manages to defeat the enemy, we usually want to give him a reward like Experience so that the player can level up. Or gold, so that the player can buy new equipment. Click on the "Rewards..." button. How much experience should each character in the battle receive when the enemy dies? If this is a tough boss battle, you may give a lot of experience. If it's a week enemy near the beginning of the game, you may give a little experience. How much gold should be awarded to the player if he wins the battle? If he just beat an animal, maybe that animal doesn't carry gold so he doesn't get anything. If he just beat a thief, maybe the thief had lots of gold on him so the player will be rewarded a lot of gold. If you wanted the enemy to give more than just experience or gold, then you can use a program (a .prg file) to do it. For example, the program can give the player an item. When you're done, click on the "OK" button.
**Experience Gained:**
**GP Earned:**
**Program to run upon defeating enemy:**
Step 5 - Save the Enemy
Now save the enemy by pressing CTRL + S. Alternatively you can click on File then Save. Or you can click on the "Disk" icon on the top toolbar. Make sure to give the enemy file you are saving a meaningful name so that you remember what it is later. For example "pirate" is a good name but "enemy1" is a bad name. DO NOT CLOSE THE WINDOW AFTER YOU'RE DONE SAVING. If you did, don't worry, just open it back up again.
Step 6 - Adding the Enemy
You're not done yet! You still need to add the enemy to the game so that you can use it later. Now that you're done saving the enemy, click on "Add Enemy to Game..."
![](vault/images/17_6.PNG)
You should see a window similar to the above. Double click on the first slot that is empty. In my case, that slot is "Enemy 2: None". If this is your first enemy, you'll want to double click on "Enemy 0: None". Now select the enemy you just saved. "Enemy 0: None" should change to "Enemy 0: Vampz.ene" or whatever your enemy filename was from Step 5. Now, with Enemy 0 selected, enter an . This helps you differentiate between weak and strong enemies. If the enemy you are adding is a boss, you should give it a unique enemy skill level. Finally, before you select "OK", under fighting type select Random and then choose how often you want fights to happen. So when the player is walking around, he has a chance to encounter enemies. Again you can use this simple formula: 1/(Percent chance to get in a fight in Decimal Form) = Value to enter A 20% chance is: 1/(0.20) = 5 A 15% chance is: 1/(0.15) = 6.67 A 23% chance is: 1/(0.23) = 4.38 When you're done, press "OK" and then click on "save". Then exit the Main File Editor that was automatically opened up in front of you. You can now also close the Enemy Editor that you had opened earlier.
**Enemy Skill Level**
Step 7 - Enabling Fighting on a Board
Now we need to allow fighting on certain boards. For example, if the player is in a town he probably won't be getting attacked by wicked creatures. But he may get attacked by these wicked creatures in the forest. So open up the board where you want him to get attacked randomly as he walks around, and go to the Properties tab.
![](vault/images/17_7.PNG)
Now click on so that the player will actually have a chance of getting into a fight. Next, choose the you'd like for the board you're on. If you want to encounter the enemy we added in Step 6, then enter the same board skill. Finally, choose the Battle Background that the fight will be taking place in. When you're done, save the board. And you're done! **Enable fighting on this board** **board skill**
Drop an Item *[Optional]*
Do you want the enemy to drop an item (like a potion) when it is defeated? If so, open up an enemy you've created, click on "Rewards..." and in the field where it says type directly in there (don't hit Browse, just type the following): giveItem("potion.itm"); You must have the filename of the item in quotations. You must also include the extension. The above function assumes that you've made an item and saved it as . If you've made another item (like a mana potion, a sword, etc) simply put in the name of that item instead. What if you want to drop more than one item? giveItem("potion.itm"); giveItem("sword.itm"); giveItem("cape.itm"); Make sure each giveItem function is separated by a semicolon. **Program to run upon defeating enemy**
**potion**
{"twitter":[{"text":"Site is up and running, seems any initial problems are solved. See you on the forums :)","date":"Thursday at 2:55pm"},{"text":"New site is online but many of you will see a white screen, it's a problem with the PHPBB software. Trying to fix it, stay patient :)","date":"Thursday at 2:17pm"},{"text":"Site is online, little initial bug so apologies to those in the first 5 minutes who wondered why everything was broke :) Should be okay now.","date":"Thursday at 1:50pm"}]}
