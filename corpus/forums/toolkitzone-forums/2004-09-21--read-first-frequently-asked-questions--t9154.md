---
kind: forum-thread
id: "toolkitzone-forums/9154"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "editor help"
skin: "phpbb2"
thread_id: "9154"
title: "READ FIRST: Frequently Asked Questions"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=9154"
written: "2004-09-21T05:37:00"
last_post: "2004-12-31T19:15:00"
date_confidence: "exact"
captured: ["20050117154935"]
author: "Nick"
repliers: ["TheBmxMan", "Guest", "BMXer138902", "Guest79315", "spitfire", "bj", "ShinAsura", "araknidkid", "chritter"]
authors: ["Nick", "TheBmxMan", "Guest", "BMXer138902", "Guest79315", "spitfire", "bj", "ShinAsura", "araknidkid", "chritter"]
posts_present: 10
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_137326_amp_", captured: "20050117154935", sha256: "b5e9abc7a8d6667d9b36fe88f817fbd2d22477050c8f2a2f203257eab4344c29", wayback_url: "https://web.archive.org/web/20050117154935/http://www.toolkitzone.com/forums/viewtopic.php?p=137326&amp="}
links:
  - {url: "http://toolkitzone.com", status: "captured", local: "wayback/toolkitzone.com/index"}
---

# READ FIRST: Frequently Asked Questions

### Nick · 2004-09-21 05:37 · #B98090

:: I can't say this will be here forever, I just kinda slapped it up. If anyone has any Q/A's they'd like to add to this, simply reply (I don't mean just questions, questions and answers Razz). ::
A lot of these questions are from the RM2K/2K3 FAQ on GamingWorld, but they applied to TK as well. I know this is a long read, but we get asked these things a LOT and if you ask something answered here, it's not unlikely that you'll get bitched out, your question never answered, and you'll get pointed to this very topic.
Q: Question
A: Answer
-----------
Q: I'm trying to make a character/item/enemy using a tileset I used in TK2, but it won't let me!
A: For characters, make an animation (32x32 pixels in size), use your tiles for each frame in the animation. It only has to be two frames long, but can be whatever you like.
If you're trying to make an enemy bigger than 1 tile, you need to make a Tile Bitmap. Click New file > Tile Bitmap, and you set it up just like you would in TK2.
To make an animation, click new (Page icon) > Animation. Define the size and speed at the bottom, and click the blank frame to add in your own frames. Click Next to append to the next frame.
-----
Q: How do I make an NPC walk around?
A: Create an Item, giving it the walking graphics of the NPC you want. Check the box "Board Driven" and click Edit. For "Program to run while item is on board," select Wander.prg. Then simply set the item to your board and it'll wander around.
-----
Q: I'm importing my TK2 game, but when I try to run it, I get the debugger. What's wrong?
A: TK2 has a lot of commands that are setup differently from Tk3. Go through your code and look for obsolete commands like CharacterSpeed and ItemSpeed (Those are defined in the Character/Item graphics editor in 3.0.5+) or border colors.
-----
Q: I tried to converted my image to a tileset using the Tile Grabber, but when I go to use it, all the tiles are mixed up.
A: Tilesets are, by default, 9 Tiles in width. This makes it realign images that aren't made for that size. You can resize the Tileset window to make it match your image.
-----
Q: How do I make it so my player can walk into a door and go into a room without using Directional Board Links?
A: You need to use Warp Tiles. Find the x/y location of the tile you want to be at when you enter the room. Go to the board from which you'll enter this room, and go RPG Code > Set Warp Tile. Click the door, and a dialog will appear. Define the board you're ported to (Inside of the room) and the coordinates. Do the exact same thing but in reverse; Put a Warp Tile inside the room that warps outside to your specified location.
-----
Q: Can I make an online game?
A: Technically it's possible via plugin, but it's certainly not easy, and it would be pretty laggy.
-----
Q: Is it possible to play my TK game on a console?
A: No.
-----
Q: What do those acronyms/terms mean?
A: TK = Toolkit
CMS = Custom Menu System
CBS = Custom Battle System
DBS = Default Battle System
IDE = Integrated Development Environment
GUI = Graphical User Interface
-----
Q: How do you make a battle system?
A: Just like you would any other program. It's really not that hard, but if you don't even know where to start, your best bet is to work on coding other things first. Menu Systems can be good practice to maybe you could try doing that.
-----
Q: Can I edit the default battle system?
A: You can, but not in RPG Code. Find the source code on <http://toolkitzone.com>
-----
Q: I'm going to make a massive 3D Online Final Fantasy 14 mixed with ChronoTrigger and DBZ game with a team of 40 people, wanna join!?
A: No, and no you're not.
-----
Q: How do I make mini games?
A: Just like you would make any other program in RPG Code. Use some graphical commands to throw up a pretty interface, buttons, etc.
-----
Q: HELP HELP I JUST STARTED AND I HAVE NO IDEA WTF IM DOING!!!!11
A: Slow down, read the tutorial and the included Help Files. Play around in the editor and just experiment with what does what.
-----
Q: I went to import an animated GIF as an Animation but it only shows the first frame!
A: The whole point of Animations is to take the place of GIF by letting you use seperate images. Simply take apart the GIF using a tool of your choice (or use the original frames if you made it) and build the animation from that.
-----
Q: I can't make good tiles in the Tile Editor, what should I do?
A: The tile editor isn't very good for actual graphics. You may use it to get used to spriting/tile art, but you're better off in a commercial art program. If you're interested in Pixel Art you CAN use the Tile Editor, but even MSPaint is better. Other programs include Paint Shop Pro, the GIMP, and Adobe PhotoShop. Try them out and see what you like.
-----
Q: What's Pixel art?
A: Pixel Art is zooming in several hundred percent on an image and drawing it pixel by pixel. Not only can it be fun (if you're an art person anyway,hehe), but you can get excellent detail into even the smallest of images.
If your question isn't here, by all means, post it.

### TheBmxMan · 2004-10-04 21:09 · #B104970

man, if i knew how to f'in make one of those, holy s'it.

### Guest · 2004-10-12 14:41 · #B109290

hey im pretty new to this, and i can do most stuff but for some reason i cant make the backgrounds of my charecters/items or anythin else for that matter, transparent. any help!?

### BMXer138902 · 2004-10-13 04:15 · #B109655

im new at toolkit but i noticed a few bugs 1.i cant make or edit any rpg programs 2. the tutorial isnt working 3. i cant get into a battle 4. I CANT BUY ANY ITEMS!!!!!!!! PLEASE HELP!!!!!! Confused

### Guest79315 · 2004-10-16 14:04 · #B111364

This is a bit embarassing but I am running into these probloms.
1.I will create an enemy but it won't show up. I have put his difficulty level in and created the chances of running into the enemy but I never run into him in the game.
2.I have created 2 characters but only 1 will show up in the battles.
Can anyone help me solve these probloms?
I am using TK3.

### spitfire · 2004-10-21 20:11 · #B114539

**Guest79315 wrote:**

> This is a bit embarassing but I am running into these probloms.
> 1.I will create an enemy but it won't show up. I have put his difficulty level in and created the chances of running into the enemy but I never run into him in the game.
> 2.I have created 2 characters but only 1 will show up in the battles.
> Can anyone help me solve these probloms?
> I am using TK3.
>

Have you enabled fighting in the game? Check the Main File editor.

### bj · 2004-12-10 03:01 · #B137326

Plz help the defult battle wont work and yes i do have u can battle on

### ShinAsura · 2004-12-18 22:33 · #B141774

umm ok i need some help and im sorry if this has been posted elsewhere.Ok im sure everyone knows about the final fantasy character sets on this site(just the ff7 one).Whenever i make a character itll work in game but its still got that nippy blue background around the character.Now ive checked the box and told it to make that colour transparent but it basically didnt work.Any ideas?

### araknidkid · 2004-12-19 19:58 · #B142153

I have a question: I made a hand made animation for the main charcter walking south, cause the one the toolkit came with was bad. so i made all 4 frames, saved the animation, went to the charcter screen, and loaded the animations. This is perfect, i thoguht. Then when i play the game, everytime i try to mive the cHarcter south (the only animation i made, (hand made)), a pop up says something like the animation cannot be displayed, or something like that, so my hand made sprite for moving down isnt shown. what shood i do?

### chritter · 2004-12-31 19:15 · #B148904

I cant get the tilesets that I have downloaded off of the site resources area to work. Only the original ones included with the toolkit will work.
I downloaded the:
RPG Maker 2000 mini sets
Buildings (Extirior)
When I open the file nothing is shown under the tileset window.
