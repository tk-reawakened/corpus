---
kind: forum-thread
id: "toolkitzone-forums/12510"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "general chat"
skin: "phpbb2"
thread_id: "12510"
title: "i must be stupid.....please help"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12510"
written: "2004-12-12T15:49:00"
last_post: "2004-12-24T17:31:00"
date_confidence: "exact"
captured: ["20041227215446"]
author: "bam7767"
repliers: ["Angel of Death", "Dont_Think_So", "Guest", "Serge", "JJ12121616", "Doc_Wellsy", "meowy"]
authors: ["bam7767", "Angel of Death", "Dont_Think_So", "Guest", "Serge", "JJ12121616", "Doc_Wellsy", "meowy"]
posts_present: 11
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_138565_amp_", captured: "20041227215446", sha256: "54f7fd5eb00030f5bc657ff0db823634742e566001fe006f677007c36d94f02d", wayback_url: "https://web.archive.org/web/20041227215446/http://www.toolkitzone.com/forums/viewtopic.php?p=138565&amp="}
links: []
---

# i must be stupid.....please help

### bam7767 · 2004-12-12 15:49 · #B138433

i cant seem to figure out how to get the additional features for the toolkit to work properly. i dont know what to do. if anybody can help please reply Crying or Very sad

### Angel of Death · 2004-12-12 16:14 · #B138444

Additional features, kupo?

### Dont_Think_So · 2004-12-12 20:13 · #B138565

If you mean for TK2, then those features are not available.

### Guest · 2004-12-16 12:34 · #B140540

maybe your right, i might be trying the tk2 ones, when i said additional features i meant like battle systems, menus, the extra prgs that others made to get away from the default, if there was any confusion with that part, im just having a hard time with the coding i guess.

### Serge · 2004-12-16 14:11 · #B140555

Ohh, like code you downloaded from this site?
It's possible that some of it may not work, especially if you're using 3.04, because a lot of the programs are for tk2.
But tell us more about what exactly isn't working and we'll try to help you out.

### bam7767 · 2004-12-18 23:21 · #B141785

i just want to make my own battle systems, im having trouble figuring out how to make characters that talk, and move around and stuff, and im just plain having a tough time lol

### JJ12121616 · 2004-12-22 19:27 · #B144250

Quote
"
im having trouble figuring out how to make characters that talk
"
which chars do you wnat to speak PC's or NPC's
either way
#Mwin(" Me: im talking yay!")
#wait(a$)
#Mwin("Old man: Im 72 and talking!")
Quote
"
move around and stuff,
"
Create the graphics and save it as an item, then use #createitem()#pushitem() #destroyitem() etc.
Quote
"
make my own battle systems
"
theres a tutorial about battle systems and custom stats, try OC's custom stats tutorial
Quote
"
and im just plain having a tough time lol
"
read my signature and at least your positive at laughing at your self. Right now im makin a program to ice skate and slide so many squares and then stop or use brakes to slow & turn. I'm writing the prg out on paper first ; this will be my 4th time rewriting the thing because i found a flaw or a better way. Have I given up? well just about, but not really. just keep trying and read that RPGcode primer over and over. it will come to you

### Dont_Think_So · 2004-12-22 20:09 · #B144283

**bam7767 wrote:**

> i just want to make my own battle systems
>

This one is really tough for someone that's new; I suggest getting to know the editor a bit more before coding your own battle system.

**Quote:**

> im having trouble figuring out how to make characters that talk, and move around and stuff
>

I can help you with that.
To make a character walk
Arrow First, you draw your graphics (in paint, photoshop, the built in tile editor, or whatever you want, really). For simplicity, I will use the ones available with the TK (in char.tst).
Arrow Create a new animation using the animation editor.
Arrow For size, select "Other" and put in 32x32 (that's the size of the sprites in the examples, although yours can be whatever size you want).
Arrow Click the blank white space in the animation editor.
Arrow Select the image you want to use. In this case, we will use the old man from char.tst. Browse into the Tiles folder, then choose char.tst. Select the old man when he is facing South.
Arrow Now that you have opened up the char.tst file at least once, we can make things easier. On the right-hand side of the screen, you will see a small, black square on a button. Press this and it will permanently show the last tileset you opened.
Arrow On the top-left side of the animation editor, there is a play button and a Previous and Next button. Select Next.
Arrow Select the OTHER picture of the old man facing south.
Arrow To preview the animation, press the play button. You may want to adjust the speed using the sliding bar.
Arrow Name the animation whatever you think is appropriate, such as Man_south.anm.
Arrow Create a new animation, and repeat the process for all directions of the man's movement. Keep in mind that the process is now a lot shorter because you have the tileset open and ready for you on the right-hand side of the screen.
Arrow Now that you have all of the animations done, Open up the item editor.
Arrow Under the "Handle" field, type NPC (or anything really, it doesn't matter). Then check the "Board Driven" button on the left. This makes the item appear when you place it on a board. Now, click Graphics.
Arrow Double-click each individual slot that you want to assign (In this case, North, East, South, and West), and open the appropriate animation.
Arrow Save the item, such as man.itm.
Arrow Open up the board you want the person to appear on.
Arrow Click "RPGCode" menu at the top, then Set Item. Click where on the board you would like him to appear.
Arrow Select your man.itm,
Arrow Under Advanced, select the multitasking program. Set wander.prg as the program.
Arrow Save the board.
To make him talk
Arrow Make a program that has something like this:

**Code:**

```
MWin("I'm talking! Weeee!")

Wait()
```

Arrow Open up your board, and select "Edit Item" from the RPGCode menu.
Arrow Edit your man NPC.
Arrow Where it says "Activation Program", select the program you just made. Save the board.
Arrow Voila!

### Doc_Wellsy · 2004-12-22 22:58 · #B144449

Like DTS said - I wouldn't try anything complicated like a BS or menu yet - first of all, just try making a few boards and linking them together and getting your character to walk around - once you've done that, try getting some text up and make some people to talk to. Then I suggest spending some time on graphics and basic RPGCode before you start worrying about battle systems and things. Trust me - its quicker this way...

### Guest · 2004-12-24 17:19 · #B145122

thanks alot you guys. im glas that there are nice people here, i realy appriciate all of your help. if theres somethin i can do in return let meh know. il tell you when i get something good!

### meowy · 2004-12-24 17:31 · #B145129

Can u do art?
