---
kind: page
id: "rpgstudio.mysticsoftware.net/rpgstudio.mysticsoftware.net/howtostart.htm"
site: "rpgstudio.mysticsoftware.net"
title: "How to Start"
original_url: "http://www.rpgstudio.mysticsoftware.net/howtostart.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20050113151102", "20050113151102"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/rpgstudio.mysticsoftware.net/howtostart.htm", captured: "20050113151102", sha256: "4ef8f297ea5f3d9d2392bc1ceb02dd79db3719eac8ddc573221cffc12e1fcdf0", wayback_url: "https://web.archive.org/web/20050113151102/http://www.rpgstudio.mysticsoftware.net/howtostart.htm"}
  - {path: "wayback/mysticsoftware.net/www.rpgstudio.mysticsoftware.net/howtostart.htm", captured: "20050113151102", sha256: "4ef8f297ea5f3d9d2392bc1ceb02dd79db3719eac8ddc573221cffc12e1fcdf0", wayback_url: "https://web.archive.org/web/20050113151102/http://www.rpgstudio.mysticsoftware.net/howtostart.htm"}
---

# How to Start

This is a tutorial that guide you step by step, how to start creating a game. This is created by William: .bjorn_djdj@hotmail.com
Step 1, Download and extract:
First of all, go to http://www.rpgtoolkit.com and download toolkit 2 or 3. I suggest you download toolkit 2. Its easier to use. And choose a folder there you want to put the zip file. Then when youve downloaded the file, double click on the setup.exe file and zip it up. Put it in the C:/Program/Toolkit or C:/Program Files/Toolkit folder. Choose what ever you want. Now you have it on your computer and lets begin. By the way, if it doesnt work. Then run regocx file. And try again. I have a lot of pictures in this tutorial and thats because one picture tell you more then thousands words.
Step 2, Start a Project:
So what shall your game be about. I suggest you name it Warrior War. Press on:
![](howtostart_files/image002.jpg)
The file button in the right corner. Now choose New Project. And name it Warrior War.
Like this:
![](howtostart_files/image004.jpg)
And press Setup My Game!. Now you see the main file, but just press on this button:
![*](howtostart_files/image006.jpg)
We will change things there later. Now, I suggest that you draw your own tiles. Or you can use the default, but thats not fun. So I will learn how to draw nice tiles in 20 minutes. Open the Tile Editor. And now you will see a window like this:
![](howtostart_files/image008.jpg)
So I will learn you how to draw trees, house and grass. Its very easy. So grab the Pencil Tool. And draw a tree, like this:
![](howtostart_files/image010.jpg)
It doesnt need to look good in the beginning, but it will look better soon. Now grab a lighter green color and use the Flood Fill Tool. And also draw some simple details. Like this:
![](howtostart_files/image012.jpg)
Now we have a tree, but it need grass. So grab another green color that you like to the grass, and use the Flood Fill Tool again. Like this:
![](howtostart_files/image014.jpg)
Now, save the tree as world.tst. And use the Capture Color tool, and grab the grass color. And press on new tile! Now grab the Flood Fill Tool once again and fill the screen with it. And save it in the same file as the tree, in world.tst. Like this:
![](howtostart_files/image016.jpg)
So now you have grass and a tree. Now you need some nice flowers. So pick a red color, and draw some flowers, and do also use some yellow color in the flower, like this:
![](howtostart_files/image018.jpg)
And save it in the world.tst. If you press L and open the world.tst. Then youll se this window:
![](howtostart_files/image020.jpg)
It tells you what tiles you have. Now you have a tree, grass and some flowers. Nice! But we need a house. So press on New Tile again. And grab a black color. And draw the house, something like this:
![](howtostart_files/image022.jpg)
And save it in world.tst. And now, press Tools and Flip, and then save it again. Now grab the brown color with Capture Color. And press on New Tile. Now draw a door like this:
![](howtostart_files/image024.jpg)
And save it to in the world.tst file. Now we will draw the roof. So press on New Tile and grab a grey color. Like this:
![](howtostart_files/image026.jpg)
The finish house will look like this:
![](howtostart_files/image028.jpg)
Pretty nice. But its not finish, we need a character. Thats the hard part to draw. So we will make it very simple and you can change it later. We shall not forget, this is a 20 minutes training. So grab a black color and draw it all like this, and dont forget to save it in a new file, char.tst:
![](howtostart_files/image030.jpg)
You can see that the character is walking, so you the flip button and save it.
![](howtostart_files/image032.jpg)
Now the character is walking south. So grab the skin color and draw it over the face, like this:
![](howtostart_files/image034.jpg)
And use the flip button again. Hes now moving north. This is hard to draw the character is walking east and west. But do it like this:
![](howtostart_files/image036.jpg)
I grabbed the Eraser. And now we will change it. Like this:
![](howtostart_files/image038.jpg)
And use the flip button. And dont forget to save it in char.tst. Now do this:
![](howtostart_files/image040.jpg)
And use the flip button. And save it. Now we have a character walking south, north, west and east. Thats so great. We are now finish with the graphic.
Step 3, Character:
Open the Edit Character. Now do the same as I did:
![](howtostart_files/image042.jpg)
And save it. Now open Graphics, and do this:
![](howtostart_files/image044.jpg)
Now save the character!
Step 4, Start Program and Main File:
Open Edit Program. And open the program start.prg. This will be pretty hard for you to understand if you are a newbie. But you can open the code and you can read and try to understand. There are a few comments. You can change things like the character speed and such. But change the name on start.prg to nostart.prg and create a new program called start.prg. Copy this codes and paste it in the new start.prg program:
#CharacterSpeed(1) *The character speed is now on level 1.
#SmartStep("off") *If the char is walking to a solid tile, then he stays there.
Now open the Edit Main File. Like this:
![](howtostart_files/image046.jpg)
And press on startup info and change the character to William.tem. Now, press:
![*](howtostart_files/image006.jpg)
Step 5, edit board:
Open Edit Board. And then you see this window:
![](howtostart_files/image048.jpg)
Then press on L or in the gray circle to open your tiles. Now grab the grass and fill the board with it The board size is 19*11. And you can change the board size in, Board Settings/Board Information/Size. But use the default size now. After the board have grass on it. Now grab some trees, and press on the blue button so you get the tile SOLID.
There is three tile options that you should know:
1. Normal  The character can walk on this, use this for grass.
2. SOLID  The character cant walk throw this, use this for trees.
3. UNDER- The character walk under this, it could be a roof.
Also put one house on the board, like this:
![](howtostart_files/image050.jpg)
This looks pretty nice. Dont you think so. Now save it as start.brd. And pres on Board Settings, and Set Player Position. And put the position right outside the house. And press this button or F5 to test the game:
![*](howtostart_files/image052.jpg)
Step 6, Talk:
Did it work, I think so. But if a error comes up, then run the regocx file in the toolkit folder.
But maybe you want a NPC (none played character) to talk. Then change the color on your character like this:
![](howtostart_files/image054.jpg)
And save it in the char.tst file. Now open Edit Item, its the same as Edit NPC. And do this:
![](howtostart_files/image056.jpg)
![](howtostart_files/image058.jpg)
You shall name the NPC NPC. And press on the Graphic and put the new NPC graphic like I did. And now open the Edit Program and copy this:
:topwander *Take a position in the program
#Wander("target") *The NPC is moving random, south, north, east and west.
#Branch(:topwander) *Goes to the taken position in the top of this program.
Now save it as wander.prg. Now create a new program, and copy this to the program:
#Mwin(NPC: Hi, my name is Artimus and Im a NPC.) *The NPC talk.
#Mwin(William: Hi, my name is William and Im using toolkit.) *The char talk.
#wait() Wait until the player press a key.
#MwinCls() *clear the message window.
Save this program as, text-npc1.prg. Open the Edit Board again and open start.brd. Right click on a NORMAL place on the board, and then press (Item: Edit). Then press Browse and grab the npc.itm file. And then press advanced and put the text-npc1.prg in the activation program. Now test run the game! Go to the NPC and then the screen will look like this:
![](howtostart_files/image060.jpg)
Thats great. Now you know how to draw graphic, how to create small programs, how to create NPC and characters and some more. But maybe you know, you made a program, called wander. You shall use that program if you want the NPC to walk, but we skip that now. You can learn that later. Because now you have a small game, maybe your first. But maybe you want to fight. Then do this:
Step 7, Fight:
Create a new program and copy this to the program:
#FightEnemy(goblin.ene, bkg .bkg)
And save it as battle.prg. Now open the Tile Editor and draw a goblin. Like this:
![](howtostart_files/image062.jpg)
Save it in the char.tst file. Now open Edit Enemy. And do the same as this picture:
![](howtostart_files/image064.jpg)
Now open graphics. And put the enemy graphic there like this:
![](howtostart_files/image066.jpg)
Save it again. Now open the start board, right click on a NORMAL place on the screen. And press on (RPG Code Type: Edit). Then press Browse and open the battle.prg. Then press Advanced and then Browse. And choose the Goblin tile in char.tst. Then press Set Program and Return to Editor. Now open the Edit Background, and fill the screen with grass, and save it as bkg. Now test run your game and step forward to the enemy.
That was pretty fun to fight against the enemy. I think you understand how to fight, use the mouse or use the arrow key to move up and down. So now you can talk with a NPC and fight against a Enemy. But now you want a larger world. Then keep reading.
Step 8, Send:
Its not so hard to send the character, for example: into the house. Just do this. Open the #Edit Board. Then press RPG Code, and then Set Warp Tile. But before you do this, you have to create the inside of the house. It take some time to create a house inside, so I will show you a example, how you could create them, called tiles:
![](howtostart_files/image068.jpg)
It took med 15 minutes to make these tiles, and its enough for a simple house. So now, how do we send the player into this house. Uhm Okey, if you hold your mouse over the board, then youll see two numbers in the left corner, on the picture above you can see 6,1. The red circle is 6,1. And the blue circle is 7,7. So hold the mouse over your door. It shall be the black circle on this picture above. Then you can see a number, for example: 6,9. Then you have to remember that number, 6,9. Now save this board as house.brd. And open the start.brd. Now press on RPG Code and then Set Warp Tile. Now youll see a window like this:
![](howtostart_files/image070.jpg)
Do like I did, dont forget 6,9 and the layer shall (always) be 1. And the house.brd, so you will be send into the house. Now press OK. And test the game.
But how can you see what tiles are Solid, Normal and Under? Press this button:
![](howtostart_files/image072.jpg)
![](howtostart_files/image074.jpg)
Blue  SOLID
Grey  NORMAL
Pink  UNDER
Remember that, its important. And now do the same but you shall come out to the start board. Use the warp file. If you like to change a warp tile, then open the program editor and open the warp tile, it could be named: warp00000000.prg.
Now you know almost every thing to create a simple and funny game. The best thing should be to read the tutorial. Then press the help button on the top of the screen:
![](howtostart_files/image076.jpg)
This was it. I think you can create a good game now. This tutorial is created by William.Bjorn_djdj@hotmail.com
2004-05-19
