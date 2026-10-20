---
kind: forum-thread
id: "toolkitzone-forums/11623"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "toolkit 2.x support"
skin: "phpbb2"
thread_id: "11623"
title: "I need a good tutorial for a TOTAL noob v. 2.x"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11623"
written: "2004-11-21T22:52:00"
last_post: "2004-12-02T23:12:00"
date_confidence: "exact"
captured: ["20050114191754"]
author: "m@"
repliers: ["sivart", "Brad"]
authors: ["m@", "sivart", "Brad"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_133832_amp_", captured: "20050114191754", sha256: "ca0b731ce38803075c1040d3f45001c6c9a8c7c6ff0d61d51cc92c13a5c32a03", wayback_url: "https://web.archive.org/web/20050114191754/http://www.toolkitzone.com/forums/viewtopic.php?p=133832&amp="}
links: []
---

# I need a good tutorial for a TOTAL noob v. 2.x

### m@ · 2004-11-21 22:52 · #B128106

I need a tutorial for rpg toolkit version 2 because i have neva used toolkit b 4 Sad Sad Sad Sad

### sivart · 2004-11-21 22:57 · #B128108

Hey Mat( i assume ) Welcome to TKZ theres lot's of tutorials with the tk on this site , also when you download the toolkit there's a tutorial and a command reference built in! Anyway if you need help with something more specific im sure someone around ehre would love to help. One suggestion , alot of games dont get off the ground so maybe you should try to make a simple game on your own before you get started making that dream game Razz Anyway , Welcome! (dont forget to register Razz Razz ) Also , i use TK2 mainly because im used to it. You might want to try the 3'rd Toolkit , its got many more features , its just a bit harder to get used to the interface

### m@ · 2004-11-21 23:13 · #B128113

thanx but where on this site can i get them?
p.s.
it iss mat

### Brad · 2004-12-02 23:12 · #B133832

Heres a tutorial I happened to find in the HELP menu on the toolkit.
Users Guide. 3
The Fast Track To Making an RPG.. 4
Main Menu.. 4
Creating A New Game. 4
Edit Tile. 4
Tiles in the RPG Toolkit 4
Colors and Pixels. 6
Tools That Make Your Job Easier. 14
Advanced Features. 29
Ways of Selecting Color 32
Color and Detail 40
Nifty Tools. 46
Tilesets. 64
Edit Board.. 80
Laying Tiles. 81
Tile Types. 84
Board Settings. 101
Board Information. 108
Board Background. 127
Set Player Position. 132
Playing with Light 136
Ambient Effects. 148
Light Color 151
Spot Lighting. 154
Gradients. 164
Layering. 168
RPGCode. 173
Items. 175
Warp Tiles. 179
Edit Character. 183
Player Stats. 184
Player Graphics. 191
Profile Image. 194
Walking Graphics. 199
Fighting Sounds. 207
Special Moves. 210
Equipment 217
Levels. 218
Edit Enemy.. 220
Basic Info and Fighting Conditions. 228
Enemy Graphics. 229
Special Moves and Weaknesses. 231
Tactics and AI 232
Rewards. 238
Animations. 242
Sounds. 243
Edit Background.. 244
Background Music and Media. 245
Background Image. 247
Edit Main File. 253
Basic Options. 254
Project Settings. 254
Startup Info. 254
RPGCode. 255
Action Keys. 256
Fight Options. 263
Day and Night 268
Graphics. 269
Plugins. 271
Edit Program.. 275
Commands and Stuff 277
Putting a program to work. 299
Run Options. 309
Useful RPGCode Commands. 314
Editing Events. 344
Edit Item.. 347
Handle. 348
Item Abilities. 348
Equipable. 349
Menu Driven. 355
Board Driven. 356
Battle Driven. 362
Graphics. 366
Other Options. 370
Edit Special Move. 376
Special Move Stats. 379
Special Effects and Uses. 379
Animated Tiles. 383
Animation Editor. 385
Transparent Color. 386
Status Effects. 386
General Info. 386
Effects. 389
Tileset Manager. 399
Creating a tileset with the Tile Editor. 400
Tileset Editor. 405
Tileset Characteristics. 408
Adding Lots of Files to a Tileset 415
Using the File Filter 418
Adding Files Visually. 421
Ripping Tiles. 423
Using Tilesets from RPGCode. 436
Edit Font.. 439
Using a Font From Your Game. 441
PakFiles. 448
PakFiles. 451
Playing Your Game. 453
Starting Trans2.exe. 455
The Startup Program.. 456
Autorun. 458
Game Controls. 463
The Internal Menu. 479
Item Submenu. 480
Equip Submenu. 481
Abilities Submenu. 489
Load/Save Buttons. 490
Customize Submenu. 490
Fighting. 493
The Fight Menu. 495
Command Menu. 498
Ending the Fight 510
Make it Work. 519
Setting Up a Game For Distribution.. 569
Users Guide
The Fast Track To Making an RPG
This manual is designed to step you through the process of creating your own RPG. It will take you into every detail of designing a game, and once youve read it through, you should be able to create a really cool game.
If youd like to get up and running very quickly, I suggest reading the enclosed tutorial.
If you want to just know the basics for now, you can create a very simple RPG. The minimum of things you must do to create an RPG with the Toolkit are:
1. Create at least one board and set the initial player position (see the Board Editor section)
2. Create at least one character with a full graphic set for walking (see the Character Editor section). You can use one of the included characters for now if you dont want to make a new one.
3. Create a Main File with the following information: The Menu activation key, the initial board file, and the initial character file. See the Main File section for info on this.
4. Run the game with the trans2.exe program. See the section on trans2.exe for info on this.
If you do these four things, youll have a basic game where the character can walk around. These basic files are created for you when you create a new game. You might want to do this first just to get a basic feel for the Toolkit, and then follow the manual step by step to see exactly how to make an in-depth RPG. Have fun!
Main Menu
Once the splash screen goes away, you will see the Main Menu screen, which has buttons that will take you to different places in the program.
Im not going to cover them in the order stated above. Rather, Ill cover each topic in the order that they should be covered. If youve never made an RPG game before with the Toolkit, then following the order of things throughout this manual will get you quickly on the road to doing so. This manual is more of a tutorial than a reference guide.
So, shall we begin our journey?
Creating A New Game
The very first thing we will do is create a new game. You can do this by clicking on the New button in the top-left hand corner of the Main Screen. This will pop up a new window. Just type in the name of the game youd like to create and hit Setup My Game!
See the tutorial for info on what exactly takes place when you create a new game.
Edit Tile
The first thing to do is create some tile graphics. Enter the Tile Editor by clicking on Edit Tile from the Main Menu. A new window will open up.
Right now you are ready to begin making a tile. But before doing that, I should probably explain what a tile is.
Tiles in the RPG Toolkit
Games that you make with the RPG Toolkit are referred to as tile based games. What this means is that nearly every graphic you see in that game- from a town scene to your characters graphic- is made up of one or more tiles.
A tile is just a little square graphic that you put together with other tiles to create a larger scene. Since every graphic is made up of tiles in your game, tiles are the core of every game you make. How your game looks depends entirely on the style of tiles that you create.
In the RPG Toolkit, a tile can be a graphic made up of 32x32 pixels or 16x16 pixels. Enough definitions. Lets make some tiles.
Colors and Pixels
The Toolkit supports 16 million colors- that is more than enough to reproduce photographic quality graphics.
When you enter the Tile Editor window, you will see a large white box on the left. This is called the Tile Form, and it is here that you create your own tiles. To the bottom right of the window is a smaller box. This is the Image Box, and shows you what your tile looks like to proper scale.
Notice that a grid divides the Tile Form up into 32 x 32 squares. This is a larger representation of the tile itself, which is 32 x 32 pixels in size.
Click on the large colored bar on the bottom of the window. This Color Bar provides you with quick access to lots of colors. When you click on a color in the Color Bar, you are selecting the color you want to use in the tile creation.
Once you have selected a color from the Color Bar, click anywhere on the Tile Form. Notice that the color you selected gets put on the Tile Form (and also on the scaled down Image Box). This is basically how you make tiles- just draw things on the Tile Form using different colors.
For now, just draw a simple figure or a scribble or something, so you can get the feel of the Tile Editor.
Tools That Make Your Job Easier
The Tile Editor is very similar to most painting programs. Along the right side of the window are a number of buttons that do different things. The buttons are as follows:
Pencil Tool  Used to draw the tile.
Eyedropper Tool  Used to capture colors off the tile.
Fill Tool  Used to flood fill parts of the tile.
Eraser  Used to erase pixels from the tile.
Line Tool  Used to draw lines.
Circle Tool  Used to draw circles.
Filled Circle Tool  Used to draw filled circles.
Rectangle Tool  Used to draw rectangles.
Filled Rectangle Tool  Used to draw filled rectangles.
Not very complicated stuff. You can easily survive in the Tile Editor using everything youve learned so far (obviously, you load and save tiles through the File menu up top). However, if youre interested in being a power user and using the Tile Editor to its fullest potential, the next section is for you! Remember- tiles are the backbone of your game. If you make awesome tiles, you will have awesome graphics.
Advanced Features
Like I said, the Tile Editor is really simple, but you probably want to use some of the better features that will make your tiles really good. A good place to start is color...
Ways of Selecting Color
Apart from clicking on the Color Bar to select colors, you may wish to select a very specific color that you just cant pinpoint on the Color Bar itself. There are two other ways of selecting color in the Tile Editor. You can find them under the Color menu at the top of the screen.
The first way of selecting a color is by using the Windows color selection dialog. Select this from the Color menu by choosing Select Color. This opens the color dialog.
If you choose to create a custom color, you can blend different intensities of Red, Green and Blue. By sliding the Red, Green and Blue sliders around, you can adjust the levels of each color component. All colors can be created by mixing red, green and blue (white is a mixture of all three at maximum intensity, black is the lowest intensity of all three, purple is an equal level of red and blue, etc).
The next way of selecting a color is DOS Palette. Select this from the Color menu. This opens up a window that gives you a palette of 256 colors. This is the standard DOS palette used by version 1.4. You can select a color by clicking on it, or by entering the color value in the box to the left (just like version 1).
Color and Detail
By default, all tiles you create are 32 x 32 pixels in size and use 16 million colors. If you are a version 1.4 user, you will know that version 1 uses 16 x 16 sized tiles with only 16 colors. Well, if for some reason you think that looks cool, you can change the color depth and detail of your tile by playing with the detail and color depth switches on the top right of the window. When you reduce the detail or color, it is a permanent change, so dont just do it haphazardly.
Often you can reduce the color of an image to 256 colors without much change. You may want to do this because a tile that uses only 256 colors takes up less disk space than one that uses 16 million colors. I dont really push it though, because you can get the best image quality from a tile with 16 million colors, and if the file size is a little bigger, who cares, right? You might want to reduce the color depth to 16 colors if you are especially crazy about disk space, but the tiles wont be pretty!
Reducing detail, though, can actually come in handy. I find that its good to start a tile off in 16 x 16 mode, draw the basic image and then increase the detail to 32 x 32. Once the detail is increased, I round out the edges and touch it up. This saves a lot of time when youre making a bunch of tiles.
If you are going to be opening tiles from a game made with version 1.4, you can increase the detail and color depth of the tile and spruce it up a lot. You dont have to change tiles made by version 1.4, though. Version 2 can handle them just fine when it comes down to using them.
Nifty Tools
Under the Tools menu are a bunch of really useful tools. You can Flip and Rotate your tile directly from the Tile Editor, which is really useful when making characters and other things that are symmetrical. (In case you havent figured it out, you flip and rotate the image using the Flip and Rotate commands from the Tools menu).
This can come in really handy when you are making a series of tiles that make up a larger image. For example, lets say you were making a bunch of carpet tiles. Well, you could draw the northwest corner of the carpet and then save it. Then youd just have to flip it to get the northeastern corner, and then you could rotate it to get the other two corners. This saves a lot of time, and you will quickly become addicted to it after using it.
There are more tools under the Effects submenu (Tools / Effects). These tools include effects like Blur, Skew and Texturize.
The Skew option allows you to skew the tile by slanting it on a 45-degree angle. It skews horizontally from left to right. If you want to skew in another direction, you can flip and rotate the tile first, and then skew it. Skewing is useful when creating 3d corners. For example, lets say you have created a brick tile. You can skew that tile so that its skewed vertically from top to bottom and bottom to top to create two corners. This looks really good when these tiles are used in games (i.e. the towers of the castle in the demo game uses this).
The Import... option allows you to convert a graphic to a tile. When you select Import from the menu, a new screen opens up and asks you to select a filename. Simply choose a file and hit the Import button to import the graphic. This method is good for importing pre-sized graphics (32x32). If you need to import an image that hasnt been properly sized, youll have to use the Grab option. After you import a tile, hit the Redraw button in the Tile Editor to show the new tile.
The Grab Tiles option is very similar to the import option. It allows you to import graphics ripped straight from a picture of any size. When you select Grab Tiles, a new window opens up with a button that allows you to select a graphic first. Just use this to load the file of your choice, and it will be displayed in the window. Now, you have to specify what part of the image you want to grab. You do this by clicking on the image itself. Click once to define the top left hand corner of the tile, and click again to define the bottom right hand corner of the tile. A blue box will be drawn showing you the selected area. Next, hit the Grab Tile button. The image will be captured, and you will be taken back to the Tile Editor. Hit Redraw in the Tile Editor to se the new tile.
Probably one of the most useful tools, Layer Tile allows you to blend two tiles together into one. Lets say you were making a Tree tile. Now, obviously, the tree will have grass behind it. But you have a separate grass tile made, and you dont want to have to draw it over again when you draw your tree. Well, Layer Tile takes care of this. Heres how:
First, draw your tree tile. Make sure you leave the white area white. The white areas in the Tile Editor represent the transparent area of the tile (unless you actually put the white color over it). Once your tree has been drawn, save it. Next open up your grass tile. Now, if you select Layer Tiles from the menu, you will be taken to a new window.
In this window, you can select the filename of the tile you want to Layer on top of the currently opened tile. So, select your tree tile. And now hit Layer. The tree tile will be placed over top of the grass. If you hit Redraw in the Tile Editor, you will see this.
Another option in the Layer Tiles window is Transparency Layer. If this is selected, then the two tiles will be blended together by mixing their colors. Try it!
The Texturize option simply applies texture to your tile. For example, when you draw a grass tile, youll probably just fill the screen with a color of green. Well, really grass is not flat green. By texturizing it, many shades of green will be placed on the image. Using Texturize in conjunction with Blur can help you create very realistic looking tiles. Most tiles in the demo game were created this way.
The Blur option just makes the tile slightly blurry. One word of caution, though: It will destroy all transparency information, so if you want the tile to have transparent portions, dont blur it!
The Light Source option allows you to apply shadows to the tile. When you select this option, a new window opens up with your tile on it. This window allows you to specify where obstructions on the tile are located. An obstruction is anything that doesnt allow light to pass through it, so when the light is applied, the obstructions will cast shadows.
You can define the areas of obstruction simply by clicking on the tile itself. The areas of obstruction will be highlighted.
Next, you can specify the source of the light and direction. Clicking on the Light Source circle to the left does this. The longer you make the line, the longer the shadows will be. When youre ready to cast the light over the tile, hit Apply Light. Then hit Redraw in the Tile Editor to see the new tile.
The last option in the Tools menu is Compression Options. This takes you to a new window that lets you turn file compression on or off. Compression can significantly decrease the file size of your tiles. This only works well if there are few colors in your tile, though. If there are many colors (as the result of importing graphics, texturizing or blurring), you should turn compression off. In this case, turning the compression off will actually make the file smaller.
Tilesets
The RPG Toolkit has two different ways of saving tiles. When you save your tile, it is automatically saved as a TST (tileset) file. Tilesets are used to store more than one tile in a single file.
You can create new tiles, and if you save them with the save .tst filename, they will be automatically appended to the end of the existing tileset.
The other way of saving tiles is by using the GPH format. This is an older format used to save individual tiles. If you want to save a tile this way, you must explicitly add the .gph extension at the end of the filename when you save it. GPH tiles work everywhere, but there are a few drawbacks:
The .gph file format is large. One tile can be as big as 11kb.
You will end up with hundreds of tiles in your \Tiles\ directory.
You will have to remember all of the filenames for these tiles.
To fix these problems, a new file format was introduced in Revision 4, called the Tileset (.tst) format. The new Tileset format has the following advantages:
The format is very small. It can be nearly 4x smaller than the .gph format.
You can put many tiles into one .tst file, so your \Tiles\ folder wont get crowded.
The .tst format is visual. When you open a tileset, a window is opened showing all the tiles in the file. To choose one, you just have to click on it. You dont have to remember hundreds of filenames.
As long as you use the default TST format, you will have all of these advantages.
When you want to load a tileset, just select the TST file. This will pop up a window showing you all the tiles in the set, and you will be able to click on the one you want to open. Its really easy, and its a lot faster than using .gph tiles.
Do yourself a favor. Use tilesets!!! Things will be much easier and faster for you. Also, any tiles that I release on my website are now stored in the .tst format. I am hoping to retire the old .gph format as it is no longer needed. You should try to do the same. On a final note, if you want to save all of your tiles into the .tst format, use the Tileset option in the main menu. You can flip ahead to the tileset section of this manual, too.
Edit Board
The next most important option is the Board Editor. It is here that you actually get to use your tiles and create scenes for your game. So, the first thing you want to do is select Edit Board from the Main Menu screen. This will open up the Board Editor window.
What is a board? Well, basically, its just one screen in your game. Each board is a different room in a dungeon, or it can be part of a much larger map. Basically, boards are what your player walks on and moves through throughout the game- all your boards together make up the game world.
So, lets make our first board. You will notice that the board editor has a large white area. This is the Board Form- and this is where you will see your board that is in progress. Above the Board Form are a number of buttons that let you do many things. Well, heres what they do...
Laying Tiles
Before doing anything, you may want to do this: click on the Grid button to turn the board grid on (5th from the left).
The first thing youll want to do is select a tile to draw with. Do this by clicking on the Select Tile button at the top of the screen, 4th to the left. (the more lazy of you can just hit the s key on the keyboard). This will open up a file selection window that lets you select the filename of the tile you want.
You can open up one of the tiles you just created, or open up one of the pre-made tiles that came with the Toolkit. In either case, once you open the tile of your choice, you should notice that the tile you just selected will be displayed in a little box at the top right of the screen. This box shows you your currently selected tile.
Now that you have a tile selected, just click on the Board Form, and the tile will be laid down on the board. Thats all there is to it! Just continue to lay down tiles to create a scene. You can select other tiles as well and use those, too. If you play your cards right, you can make very detailed screens only using a few different tiles!
Heres a good tip: if you are using tilesets instead of individual tiles (I recommend that you do), you can hit the L key to open up the last tileset you had opened. This speeds things up considerably.
Tile Types
OK, youve made a nice looking little scene, but now what? Well, first of all, you may think youre done, but youre not. There are a few more things you have to do to make a complete board. First of all is to set the Tile Types of each tile on the board.
Notice the row of colored triangles at the top of the screen. Theres also a little Toggle button. Above the Toggle button is some text that should say Tile Type: Normal. That means that all of the tiles that you just laid down were of type Normal. That means that the player can walk over top of any of those tiles just as if they were the floor. But hit Toggle once. Youll notice that now it says: Current Tile Type: Solid. That means that any tiles you lay down now will be of type Solid which means that the player cannot walk over those tiles- they act as walls, or barriers.
You can redraw the scene if you want making sure that any ground you draw is of type Normal and any walls are of type Solid, but there is a quicker way to set all the tile types of the board.
Hit the Type Lock button at the top of the screen (10th from the left). This will put you in Type Lock mode (before you were in Draw mode). This mode allows you to change the Types of your tiles without changing their graphics.
When you enter Type Lock mode, you will see that each tile will get a little colored arrow put over it. Each arrow tells you what type that tile is. All of the arrows should be gray at this point because gray means that they are type Normal.
Hit the Toggle button until the tile type is set to Solid. Now click on the board form. Notice that when youre in Type Lock mode, clicking on the tiles just changes the color of their arrows- it doesnt change the graphics themselves. So now you can click on all the walls and change the arrows blue. Blue arrows mean Solid.
You can go back to Draw mode by clicking on Draw Lock any time.
There are many different tile types. They are listed below:
Normal- The player can walk over this tile. This is for making the floor.
Solid- The player cannot walk over this tile. This is for making walls.
Under- The player walks underneath this tile. This is good for making arches, or anything else that the player can walk underneath.
North-South Normal- The player can walk over this tile if he steps on it from the north or south, but if he comes to it from the east or west, it acts as if it were solid.
East-West Normal- The player can walk over this tile if he steps on it from the east or west, but if he comes to it from the north or south, it will act as if it were solid.
Stairs to Layer n- This type transports the player to board layer n. This will be described more later on...
Board Settings
Probably the most important menu in the Board Editor is the Board Settings menu. Its here that you can set all of the boards important information. Inside this menu are three options:
Board Information
Board Background
Set Player Position
These options are explained below...
Board Information
This option lets you specify all of the pertinent information for the board that you are currently editing. Once you select this, a new window will open up showing you the current board information. You can edit all of it here.
The first thing to look at is the Directional Links, or Board Links. These allow you to specify where the player will go if he or she walks off of the edge of the current board. So, if a player walks north and comes to the top of the board, where will s/he go once they step one space further north? Well, another board will be loaded and the player will start on the southern edge of that board.
You can specify the north/south/east/west links by clicking on the buttons assigned for this. This will open up a file selection window. You can enter the name of a board that currently exists, or even one that you havent created yet (if you dont want there to be any link, just type None).
Heres something you should note: just because board A is linked to board B, this doesnt mean that board B is linked back to board A. So, if you make a northern link on a board, when you make that other board, its southern link should go back to the original board. If you dont understand this upon reading it for the first time, dont worry. Its kind of common sense and youll probably discover this on your own, anyway.
Also, in order for a link to work, the corresponding tile on the next board must not be solid. If it is, then the player wont be able to walk over it (i.e.- if the player walks from 1,1 and goes north, putting him at tile 1,11 on the next board, tile 1,11 must not be solid. Again, this is common sense).
The next thing of immediate interest is the boards background music (hit the Music tab). You can select any valid media type for this to be played as background music on the board. Well, whats a valid media type?
The Toolkit internally can play WAV, MIDI, MP3, MOD, XM, IT and other tracked music files. For any other media type, it will ask the operating system to play the file. If there is a program installed that can play that particular type of file, then that program will be used to play it.
If a player enters a board and the selected song is already playing, it will continue uninterrupted. Otherwise, the new song will be played. All songs are looped forever (they play over and over again).
The next thing to look at is the Battle Options tab. This allows you to specify whether or not fighting is permitted on this board. For some boards, you may wish to have players never get into fights (like in a town), but for others (a cave) the possibility of fighting should be open. If you want fights to be allowed, specify this by clicking in the check box.
If fighting is permitted, then you have to fill out two other things. First of all, you will have to fill out a Skill level. The skill level of the board is any number that you specify. This just means that if the skill level is 1, then the player can only fight enemies who are defined to be of skill level 1.
So, at the first of the game, you will want simple enemies, but by the end, the enemies should be more difficult. Adjusting the skill level allows you to control this. For more info on enemy skills, see the Edit Enemy section.
The other thing that you have to fill out is the Board Background File. This is the filename of a background file (*.bkg) over which the fight will take place. When the fight starts, the player is magically whisked away to the fight screen, and the Background File defines what that screen looks like. So, if your board is in a mountainous region, youd want the background to have mountains on it. For more info on this, see the Edit Background section.
Hit the Size tab to resize the board. The board can be really huge depending on the number of layers you want to use.
The Progress tab allows to disable saving from this board (so the player wont be able to save his progress on this board).
The Day/Night tab allows you to enable day and light settings for this board. You will see later on (in the Main File Editor section) that your game can have day and night. This section of the Board Info screen lets you turn day and night on for the board. Also, if day and night is turned on, you can set a custom board skill and background for nighttime (to fight harder enemies in the dark!).
Something else that you can edit from this screen is the Board Constant Value list. This is a list of ten numbers that the board saves in special variables to be used by RPGCode programs. For more information on variables and the constant values, see the section on Programming in RPGCode, specifically the Reserved Variables subsection.
The last thing that you can edit on this screen is the Board Layer Titles. These are the names of each of the eight layers on the board, and will be displayed when the player enters the board. The boards layers will be discussed more later on.
Board Background
This option allows you to set the background colors and graphics of the board and its border. When you select this option from the menu, a new window will pop up.
You can specify what images will be placed on the board and its border by clicking on the buttons provided. Alternately, you can also select the color of the border and the boards background here as well.
If you select a graphic that is larger than the display area for the board background, the image can be parallaxed. If parallaxing is enabled for your game, it will be used as a parallaxing background image (see more on parallaxing in the Edit Main File section).
Set Player Position
This is tremendously important if you are editing the first board of the game. Otherwise, its not very important at all. This allows you to specify where on the board the player starts. If you do not set this, the player will not be shown on the board when you play the game! (but only for the first board).
Just select this from the menu, and then click on the location where youd like the player to start.
Playing with Light
Color is everything when you are designing nice graphics. And along with color goes proper lighting and shading effects. One of the Toolkits greatest advantages is its ability to allow you to change the lighting effects on any tile on your board.
The simplest way to change the lighting effects of your tiles is to move the Tile Lighting slider bar at the top of the screen. This allows you to adjust the amount of white light cast on a tile. When you make it negative, the tiles get darker. When you make it positive, they get lighter, and when its zero, the tiles are the way they were created.
When you lay down tiles after adjusting the light level, you will see that they are shaded or lightened according to the current light level. This is especially good for making shadows. I generally put the Ambient Level down to -30 to lay down tiles to be used as shadows, then set it back to normal for anything outside of the shadow.
It takes longer to draw many tiles of different shades, so if you are making shadows, try to keep them all at -30, or some other constant level. Not only will it look more realistic, but your boards will draw faster as well.
Using the Tile Lighting slider bar is good for most lighting effects, but occasionally you will want to add different colored light and other effects to the board.
For the advanced options, select the Board Lighting menu at the top of the screen. This menu has the following options:
Ambient Effects
Light Color
Spot Lighting
These are explained below...
Ambient Effects
This allows you to set an overall lighting effect to the entire board. When you select this option, a new menu will pop up giving you a few different ambient effects to choose from. When you select one and hit Apply, the board will be shaded differently.
Light Color
By selecting this, you can specify the color of the light. You just have to edit the red green and blue components to create the desired light color. Now when you lay down tiles, they will have this light color applied to them.
Spot Lighting
This feature allows you to apply a spot light to the board. That is, a number of tile will be shaded a certain color to create the illusion of a spotlight. The light fades away as it gets further away from the source.
Before even thinking about using a spot light, you should have a complete board made and you should have it saved. That way, if you dont like the spotlight, you can use the saved copy.
The next thing you must do is select a light color. Do this by selecting Light Color from the Lighting Effects menu. OK, now were ready for a spotlight! Select this option from the menu.
This will open up a new window. This window allows you to set the spot light options. First of all, youll want to turn spot lighting On.
Next, specify the radius of the spotlight. This determines how large the spotlight will be (since a spotlight is circular, this is the radius of the circle, in tiles). Now specify the lights fade constant. This is the amount of fade the light has as it gets further away from the source. A good fade constant is something between 10 and 20. Now just hit OK.
Now you can apply your spotlight. Just click on the board where you wish to place your spotlight, and now hit Redraw. The spotlight has been applied!
Before editing the board more, make sure you turn spot lighting off!
Gradients
A final way to shade your board is by using gradients. You can create a gradient by hitting the Gradient button in the board editor (8th from the left). This will pop up a new window asking you what colors to use for the gradient. The two colors you choose will fade into each other across the length of the gradient.
Once you have chosen your colors and hit OK, you will be asked to click the top-left and bottom-right corners of the gradient on the screen. Once you have done this, the board will be redrawn with the new gradient shading.
Layering
The RPG Toolkit allows you to make use of up to 8 board layers. Whats this all about? Well, basically, a board is not limited to merely one flat surface. Rather, you can think of a board as being a three- dimensional surface, with 8 levels of height.
So far, we have been working exclusively on layer one. However, there may come a time when you wish to use more layers on your board. When would you do this? Well, lets say that you make a board that is a jungle scene. Perhaps you would like your player to be able to climb a tree and walk about on the branches above the rest of the board. So, you could use the layering feature to accomplish this.
Layering can be used for many more things, though. These range from blending graphics to creating airships that your player can use to fly above the landscape.
Lets start with the simplest application of layering, thoughusing it to represent multiple levels of height on your board. First of all, you will have to create a board on layer 1. Once thats done, change your tile type to Stairs to layer 2 and lay down that type on a certain tile.
Now, when your player steps on that tile, he or she will be transported onto layer two. This just means that the player will no longer use the tile type restrictions that are found on layer oneinstead, he will use the restrictions placed on layer two.
OK. So now you have created a way for your player to actually get onto layer two. Now, notice the drop down box at the top right of the board editor that says Layer One. Change this to Layer Two.
If all went well, the screen should go white. Dont worry! Your board hasnt been erased! You are now looking at layer two, which has nothing on it. If you want, you can switch back to layer one to see that Im telling the truth.
Anyway, now that you are on layer two, you can edit it much as you would layer one. However, before you do this, it is a good idea to hit the Draw all layers button. This will make layer one visible to you while you edit layer two.
First things firstchange the tile type to stairs to layer 1 and place a tile with this type in the same location as that stairs you placed on layer 1. Now, when your player is on layer one, and steps on the stairs, he will be transported to layer two. When he steps on the stairs again on layer two, he will be transported back to layer one.
The second layer should just be something like a ledgesomething that hangs over layer one and which the player can walk on. It would be stupid to fill up the screen so as to completely obscure layer one. Also, around the edges of the ledge, you should make solid tiles so that the player doesnt walk out into empty space, which will give the effect of walking on air.
When you are done with layer two, you can hit Draw all layers to see how the whole thing looks.
This is the most basic use of layering, and it is quite useful. However, there is another little trick that you can use layering for that will reduce the amount of time you spend drawing tiles. This is something which layering was never really designed to be used for, but it works, and a number of games on the internet have used this little trick
Lets say that you are drawing a scene on which there are grass tiles, but there are also trees that have grass behind them. In order to give the desired effect of having the grass underneath the tree, you could blend the tiles together with the Layering option in the Tile Editor. However, there is a better way.
What you can do is lay down the grass tiles on layer one, then switch to layer two and lay down the tree tiles over top of the grass tiles. As long as the tree tiles have transparent portions, you will see the grass through the trees. When you hit draw all layers, you will see how this works.
An important note: make sure that you set the tile type of the grass with the tree tiles above it to solid, otherwise you character will walk underneath the trees.
Also, if you are putting the trees over more than one type of tile on your board, you will have to use some more trickery to make it work properly. Lets say you had grass and dirt on your board, and you wanted trees on top of both. You have to change the lighting effect slightly between the trees on the grass and the trees on the dirt in order for them to draw properly. This is because the Toolkit will make a blind copy of the tree tiles over the whole board, grass and all. If you set the tree tiles that are on top of the dirt to ambient light level 1, it will force the Toolkit to redraw the tree tile over the dirt, and it will be barely noticeable to the eye.
RPGCode
One of the Toolkits most important features is its built in programming language, RPGCode. RPGCode lets the character talk to and interact with other characters in the game, as well as much, much more. Refer to the RPGCode section of the manual for a comprehensive tutorial on how to use it.
In order for RPGCode programs to be executed, the player must have to opportunity to run them from the board. And it is in the board editor where you set this up.
The Toolkit works by running RPGCode programs when the player steps on certain tiles. We have to tell it which tiles run programs. In order to do this, click on the RPGCode menu, and select Set Program. Now, click on the tile upon which you wish to place the RPGCode program. This will cause a new menu to pop up.
Now, the only thing that you really have to fill out is the Program File Name. You can set this by clicking on the Browse button. If this were the only thing that you filled out, then this program would be run each time the player stepped on this tile.
There are other options that will let you specify exactly when this program will get run and when it will not.
Under the Activation subheading, you can change the program to be Conditionally active. That is, it will only be run if a certain variable is equal to some value. You should probably change this variable name to something more descriptive. For more info on variables, see the RPGCode section of this manual. Also, after activation, you can cause that variable to be equal to something else. If you just want the program to be run once and for all time, just leave the defaults.
Next, you can change the Activation Type. By default, the program is activated simply by the player stepping on it. This is usually best for doors and things. But you can change it so that it will activate if the player presses the Activation Key. This is a key on the keyboard that is used to perform general function. When the player is facing the program and this key is pressed, the program is run. For more info on the activation key, see the Main File section of this manual.
Also, you can specify a graphic for this program. If the program is conditionally active, this graphic will not be displayed if the program is not active.
You need to use programs when placing doors on the board. You must use the RPGCode command #Send to do this (or you can use a Warp tile to auto-create the program). For more info, check out the RPGCode section
Items
Similar to RPGCode programs, Items can also be placed on the board. Items are a bit different, however. An item is pretty well anything that you want it to be. It can be an actual item that your character carries with him, but it can also be a town peasant wandering around a village.
If you want to place characters that walk around on your board, you have to do this with items (see the Item section for more info). In order to lay down an item, click on the RPGCode menu, and select Set Item. From here on in, it works almost identically to setting an RPGCode program. Im sure youre smart enough to figure it out.
Warp Tiles
A warp tile is a tile that send the player to another board when he steps on it. You can use a warp tile to create doors. To create a warp tile, select Set Warp Tile from the RPGCode menu. Then click on the tile where youd like to put it. This will pop up a new menu asking you where the tile should take the player. Fill in the board and the coordinates and hit OK. This automatically creates an RPGCode program for you that will act as a warp tile.
Edit Character
The character editor allows you to create players that you can use in your games. A character usually takes a lot of work to make. This is because of all the walking graphics you have to make for it. But well talk about that in a bit. First of all, lets get to the basics
Player Stats
Aside from a nice set of graphics that move around your screen, the player is a creature that contains a lot of information. After all, the player can fight, move around, talk to people, etc. How can we determine how strong he or she is in a fight? How can we determine how healthy he or she is? Well, on the main window of the Character Editor, we can set up the most important part of the characterthe statistics. Dont shy away in fear. This is actually quite painless.
Really, you only have to do a few things to set up the statistics of the player. First of all, type the players name in the Character Name field.
If you hit the Advanced tab, you will see that a bunch of things were just filled into boxes for you. These are variable names. They can be accessed and changed with RPGCode commands. If you are interested in this, skip ahead to the RPGCode section. Otherwise, dont worry about ityou dont have to know anything about RPGCode to create a character. Like I said, its all automated now.
Now, all you have to do is fill out several of initial values. These are values that the player will have when he or she first joins the game. The first option is the starting experience value (XP). In an RPG, experience is a measure of how many fights the player has been in. As the player fights more and more and gets further into the game, the experience level also increases. The experience level can be used to determine if a player can do particular moves, and it also determines when the players skills are upgraded. You can probably leave this value at zero, since the player has had no fighting experience when he or she starts the game. You can, however, change this if you wish. You may wish to if this is a player that joins the game far into the story. Generally, these characters start with a higher experience to match the other characters in the game.
The next value to fill out is the Starting Health value (HP). Each player has a health levelwhen that level reaches zero, the player is dead. So, in a fight, the higher the level of health that a player has, the better off he is. For a beginning character, 100 is a nice round value to start off with. Following this is a Maximum Health Value. You should probably set this at 100 as well. The maximum health level ensures that a player starting the game doesnt get a health of 99999999999, or something, which would make him virtually invincible. The maximum health increases as the players experience increases.
Next is the Defense Value (DP). This is a value, which determines how well a character can defend himself. For example, if an enemy attacks the player with an attack level of 100, and the player has a defensive level of 40, then the player will only suffer 60 damage. At the start of the game, a small number like 10 is appropriate.
Next is the Fight Value (FP). This is the value that determines how powerful the player is in a fight. If the player attacks an enemy and has a fight value of 200, and the enemy has a defensive value of 10, then the player will inflict 190 damage on the enemy. For the start of the game, a value like 60 is good.
Next is the characters special move power level. This determines how much special move power (SMP) the player has. The special move power is required to do special attacks, like magic attacks or healing moves. The more SMP a player has, the more he or she can use these special moves. A good starting value is 50, but if the player is a key magic user, then the value should probably be higher. Also, you must fill out the maximum SMP value. This is similar to the Maximum HP value.
Finally, you have to specify the players initial level. Level 1 is a good starting point. As the player builds experience, the Level will increase. Each time the level increases, the max HP, max SMP, FP, and DP also increase. For a player at the start of the game, like I said, a value of 1 is good. For a player that joins the game later on, a higher value would be appropriate.
Player Graphics
After the stats, the next most important thing about a character is its graphics. Without the graphics, you wouldnt be able to see the character on the screen! This is the most time consuming part of creating the character, and is one of the more time consuming parts of using the Toolkit.
Profile Image
The simplest graphic you can assign to the character is the profile image. The profile is the image that is show in the main menu when you select the character during the game. This is usually a picture of the players face.
The profile image can be a standard tile, but it can also be BMP, GIF or JPG format. In the last three cases, is must be 64x64 pixels in size. I suggest you use one of the last three, since the image would be much nicer looking.
To set the character profile, just hit the Profile button on the left side of the window, and select the graphic filename you wish to use.
Walking Graphics
The walking graphics are the frame by frame shots of the character for each movement he or she makes.
You can edit the player graphics by clicking on the Graphics button to the left. After a few seconds, a new window will pop up.
This screen should be initially empty. Your goal is to ultimately fill every one of those empty boxes with a graphic. Like I saidthis is time consuming!!! At the very basic level, you must draw at least 16 graphics just for the basic character animation.
Well, lets stop worrying and just do it. At the top of the window are rows of boxes underneath a heading called Standard Walking Graphics. Each of these boxes represents a frame of animation in the characters walking set.
The characters in the Toolkit have up to 4 frames of animation for each direction that they walk. You will notice that the walking graphics are grouped into four groups of four. Each group is intended to be the animation set for the character walking in a different direction.
Each frame is 64x32 pixels in size (thats two tiles stacked on top of each other). You can create tall characters by composing their graphics of two tiles each.
The first set is Front View. This animation set should be the one that the character does when walking southhe is facing you. In order to set graphics for each frame of animation, just click in one of the frames and you will be allowed to select a filename (it matters whether you hit chick the top or the bottom of a frame, as this will allow you to define one of two tiles for the animation frame, since players can be composed of two tile per frame).
Probably, you will have to leave the character editor for the time being and make a bunch of graphics in the tile editor. There are ways that you can limit the amount of drawing you have to do. Notice that the left and right view are complete opposites of each otheryou just have to draw one set, then flip each tile with the tile editor to get the next set. There are other shortcuts possible using the flip tool in the Tile Editor.
Once you have filled out all 16 boxes, hit the Animate! button to see your character walking. Great! Now youve got yourself a character that can walk around the screen.
There are some other graphics that you can fill out here, too. You can leave them for now, but eventually youll have to fill them in. All the other graphics have to do with the fighting animations for the character. Since you havent made any fighting stuff yet, you can ignore them. But you will have fights eventually and you wont be able to ignore them any longer.
So, there are four frames of animation available for each action possible in a fight. The fighting graphics should have the player doing something like swiping a sword. The defense graphics are used when the player gets hit. The special move graphics are used when the player uses a special move. The death graphics are used when the player dies.
The At rest graphic is the graphic used when the player is doing nothing during a fight.
Finally, there is one more set of graphics. The Custom Postures. There are 10 available slots for this. Custom postures allow you to create tiles for the character doing things like nodding his head, or whatever. These custom frames can be accessed using RPGCode to create custom actions. See the RPGCode section for more details.
Fighting Sounds
Also of interest in this screen are the fighting sounds. These are at the bottom of the screen. Here, you can specify a WAV file to be played when the player swipes his sword, gets hit, dies, or uses a special move in a fight sequence. To change them, just click in the boxes beside each description.
Special Moves
In a fight, the character can attack in a few different ways. He can use his standard physical attack (i.e. Using a sword, or even a fist). Or, he could use an item to hurt his enemy (like poison, or a bomb). But he can also use Special Moves.
Special Moves are a form of special attack that the player can perform that is usually more powerful than standard attacks. A special move might be a magical style attack. It could also be some special fighting style, like martial arts. Whatever the case, a special move is just thatspecial.
In a little bit, I will explain how to actually create these special moves, but for now well see how to set the character up so that he or she can use them. To edit the characters special moves, click on the Special Moves button in the Character Editor.
This will open up a new window. First of all, if you wish to let the player use special moves, click on Yes where is says Does this character use special moves?
Next, you must give the special moves a Name. In the box where is says Official Name of Special Move, type in the name of the special moves. This is usually the name of a certain class of special moves (i.e. White Magic, Martial Arts, etc.) The name can be whatever you want, but it should fit the special abilities of your character.
Once those things are out of the way, we can actually get down to selecting those moves which the player can do. There is a list below, with slots for up to 200 special moves. Just click on one of those slots, and hit Change Special Move. This will open up a file menu, where you can select a special move. Like I said, we will be making special moves later on, but once they are created, you can select them here.
You can set it up so that characters can only do special moves once they have gained enough experience to do so. Do this by first clicking on the special move slot you wish to edit, and then hit Special Move Info. This will open up another small menu.
In this new window, you can set the conditions under which the character can use this move. For example, lets say you had a character that could use fire, but could only use it if his experience was at least 800. Well, if you put 800 in the box, then thats how it will work.
Important: You can set a minimum experience, but the three conditions in this menu still have to be set. For example, you could set the minimum experience to be 800, but if the minimum level is still zero, then the player will still do this move, since his level will always be higher than zero. Make sure you set the other values to impossibly high amounts, so that only the condition you want met is used to determine if the player does the move or not.
The variable and its condition is a way to add a move to a player thorough RPGCode. Here you can specify a numerical variable to be checked. If that variable equals a certain value, then the player can do the move. For more info on this, see the RPGCode section.
Equipment
In a fight, a character can wear certain equipment that will improve his or her fighting and defensive ability. It stands to reason that a player wearing armor should sustain less damage than a player who is just wearing a leather coat. In the character editor, you can specify what body locations you can equip items on.
In the character editor, if you click on the Equipment button, a new window will open up.
This window is pretty simple. It allows you to decide what body parts equipment can be worn on. If you want your character to be able to wear a hat or a helmet, make sure Head is turned on.
Also, there is an accessory list. This allows you to add body parts that may not be there. For example, you could add Ring Finger to the list to allow the play to equip a ring. There are 10 accessory slots.
Levels
Setting the players level attributes sort of goes hand in hand with the player stats. But its a little simpler. When the players experience increases, it makes sense to reward the player with power ups of health and fighting power. As already discussed, that is what levels are for. When the player reaches a new level of development, his or her hp, dp and fp increase. If you click on the Levels button in the Character Editor, a new window will pop up.
There are some important things in this menu. First of all is the Initial Experience Required For Level Progression. This is the amount of experience the player must gain before progressing to the next level. If the player starts off at level 1, a good value for this is 100. This means that the player will have to gain 100 experience points before progressing to level 2.
The box that defines what the increase in the required experience is also very important. As the game progresses, each enemy should give progressively more experience (because they are more difficult). It wouldnt make sense if an enemy gave the character 1000 experience, and the player always needed 100 points to progressthe player would increase by 10 levels every battle! In order to offset this, the experience required for progression should increase as levels increase.
The value you specify here is the percentage by which the required experience increases from one level to the next. In other words, if you set this value to 10%, and the initial increase amount is 100, then once the character has made it to level 2, the experience required to get to level 3 will be 110 points. Then the experience required to get to level 4 will be 121, etc. A value like 10 is good. The default 2% is also good, but it may allow level progression to be too quick. Really, this depends upon the length of your game. The higher you make the number the longer your game will have to be to balance the extra time required by the character to progress his level.
Next you can specify what the maximum level is. The player cant increase forever, otherwise you might have an invincible character! 99 is used by most RPG games.
Next you can specify the percentage by which the max hp, dp, fp and spc power increases when the player reaches a new level. A value like 10% is good for this. A word of caution: make sure the percentage is high enough to actually make a difference. For example, lets say the players hp was 60, and it was to increase by a measly 1% when the level increases. 1% of 60 is 0.6 points. The Toolkit will round this down to 0. So the players health will NEVER increase! If the value is set to 10, then the player will go from 60 hp to 66 hp when his level increases. Much better!
Finally, you can specify an RPGCode program to run when the player levels-up. See the RPGCode section for more info on this.
Edit Enemy
Now we move into the darker realms of the RPG. The enemy. So far, we have created a character, decked him out with all the necessities for a big fight. But what has he been preparing for? Well, its time to create his worst nightmare
An RPG is not about fighting. RPGs generally are more of an interactive story. Fighting is a large part of that, but it is not the central feature as in most action games. An RPGs fighting system is what I call passive action. Whereas in an action game, the player is forced to fight because an enemy is coming towards him, in an RPG, the player is usually attacked by organized parties of enemies. You dont see the enemies coming. Rather, when you are attacked, you are swept away to a battle screen where the fight occurs.
In an action game, there is very little strategy. Usually, your goal is to whip out your biggest weapon and load your enemy full of bullets. In an RPG, a fight is far more strategic. While in an RPG, you can rip an enemy to pieces with an especially powerful move, this is usually not done because the players need to conserve their energy. Fights occur in groupsthere are usually a team of enemies and a team of good guys. Each individual in each group generally has its own specialties.
Enemies can be very diverse in the Toolkit. They can range from a wimpy little rat to a madman with the power to destroy the earth. And size doesnt matter. Why not give the rat the ability to destroy the earth? The player wouldnt see that coming!
Creating an enemy is very similar to creating a character. The only difference is that the computer controls an enemy, and since the player is only concerned with the enemy until it is dead, there is no need to bother with things such as level progression and such with an enemy. In other words, an enemy is a flash in the pan. While you may encounter the same enemy more than once, it never gets more powerful, like your characters do. The issue of enemy strength is dealt with as your character moves from one area to another. At the first of the game, the enemies should be fairly easy. As the player moves out into the world, the enemies should be more difficult.
In the final cave or dungeon, the player shouldnt encounter enemies from the start of the game. When the player moves to a new area, the old enemies stay there. So, the player is always encountering new enemies. Which means we have to make lots of enemies. And thats what the enemy editor is for.
Basic Info and Fighting Conditions
To start off with, click on Edit Enemy in the main menu to open up the enemy editor window. The immediate slots in this window allow you to edit the most basic aspects of the enemy. Fill in the enemys name, HP, SMP, FP and DP (for a detailed explanation of these stats, see the Character Editor section).
