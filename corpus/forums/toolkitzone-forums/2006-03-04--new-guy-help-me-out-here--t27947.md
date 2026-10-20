---
kind: forum-thread
id: "toolkitzone-forums/27947"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "27947"
title: "New Guy...Help me out here..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27947"
written: "2006-03-04T00:15:00"
last_post: "2006-03-04T17:38:00"
date_confidence: "exact"
captured: ["20060326114154", "20060327193602"]
author: "Fingerz91"
repliers: ["I_Cant_Believe_Its_Me", "Z3R0", "Axiom", "DrakeLord"]
authors: ["Fingerz91", "I_Cant_Believe_Its_Me", "Z3R0", "Axiom", "DrakeLord"]
posts_present: 11
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_303372_amp_3Bsid_eb921d85f60f19d58fa43ba91e785f5b", captured: "20060327193602", sha256: "ea084d3e2872b8b07680dd6a1a4f803bf7cf0ed7108621c740104d7a801a249c", wayback_url: "https://web.archive.org/web/20060327193602/http://toolkitzone.com/forums/viewtopic.php?p=303372&amp%3Bsid=eb921d85f60f19d58fa43ba91e785f5b"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_303432_amp_3Bsid_625e6cafa1b9e1f5ed86dc13c3188a17", captured: "20060326114154", sha256: "e954b291c37c026763691d029db268f5039461506d0f02af4b2ec1bca54d6913", wayback_url: "https://web.archive.org/web/20060326114154/http://toolkitzone.com/forums/viewtopic.php?p=303432&amp%3Bsid=625e6cafa1b9e1f5ed86dc13c3188a17"}
links:
  - {url: "http://www.toolkitzone.com/index.php?id=30", status: "captured", local: "wayback/toolkitzone.com/index.php__id_30"}
---

# New Guy...Help me out here...

### Fingerz91 · 2006-03-04 00:15 · #B303238

I like the basic tile set that is given upon installation of TKZ, but I need monsters, ect..
Can you help?

### I_Cant_Believe_Its_Me · 2006-03-04 00:26 · #B303242

<http://www.toolkitzone.com/index.php?id=30>
That would be the resources which can be found at the top. Just take the tileset out of the downloaded folder and place it into your game's tile folder.

### Fingerz91 · 2006-03-04 02:43 · #B303277

I cant get my character to go from board to board Crying or Very sad . I want him to go to the east border, and go to the 2nd level of my game, but it will not work. I have read the quick start guide.
Thanks for your help!

### Z3R0 · 2006-03-04 02:46 · #B303278

warp(board$.brd, x,y,l) I believe is the program.

### I_Cant_Believe_Its_Me · 2006-03-04 02:49 · #B303280

**Z3R0 wrote:**

> warp(board$.brd, x,y,l) I believe is the program.
>

Or you can just go into the board settings (while editing the first board) and set the eastern board link to the second board made.
That will let you move to the next board made when you reach the eastern end of the first board.

### Axiom · 2006-03-04 03:12 · #B303284

I can figure out going to the edge of the map... but how do you work stairs?
I say the warp Area link under RPG code but I am obviously not doing something right since he jumps to the new board... but he ends up in a border tile.. not the tile he supposed to end up in.
Hep Me batman!

### I_Cant_Believe_Its_Me · 2006-03-04 03:20 · #B303286

**Axiom wrote:**

> I can figure out going to the edge of the map... but how do you work stairs?
> I say the warp Area link under RPG code but I am obviously not doing something right since he jumps to the new board... but he ends up in a border tile.. not the tile he supposed to end up in.
> Hep Me batman!
>

The batman thing was funny Razz
Well, lets see. I'm not too good of a programmer but me being a boards guy I do know how to work a warp program.
When you set a warp tile it asks for four main things:
1.)Board File
2.)X coordinations
3.)Y coordinations
4.)Layer
To find the x and y coordinations just simply open the board you wanna warp to and move your mouse over to where you want your guy to appear when he warps. When your mouse is hovering right over it, look down at the bottom right (in the current tile box) of the board editor and you should see a number like (for example) "10,8". So go back to the other board where you're setting the warp tile and put in the "X" box the first number, which is 10. Then in the "Y" box you enter the second number, which is 8. That way your character will then appear on that exact spot. The layer doesnt really matter not unless the tile your character will appear on is on another layer, then you might wanna change it to that layer.
And yes, you can use multiple warp tiles just incase you were wondering.

### DrakeLord · 2006-03-04 13:48 · #B303372

And if you are, for some reason, counting it yourself, remember to count from the top-left. Wink

### Fingerz91 · 2006-03-04 15:46 · #B303403

Here is EXACTLY what I am doing...
Opening start board
Going to board settings>board information>setting the eastern(right) link to lvl2 board.*All tiles are normal*
Going to lvl2 board and setting the western(left) link to start board. *All tiles are normal*
Start the game. NOTHING WORKS!
I hope I'm not being to annoying, Im used to making games with gamemaker, so I do have a bit of game programming backround, Im just not used TK yet

### I_Cant_Believe_Its_Me · 2006-03-04 16:56 · #B303422

**Fingerz91 wrote:**

> Here is EXACTLY what I am doing...
> Opening start board
> Going to board settings>board information>setting the eastern(right) link to lvl2 board.*All tiles are normal*
> Going to lvl2 board and setting the western(left) link to start board. *All tiles are normal*
> Start the game. NOTHING WORKS!
> I hope I'm not being to annoying, Im used to making games with gamemaker, so I do have a bit of game programming backround, Im just not used TK yet
>

Ah, you forgot to set your characters start position. You can do this by going under "board settings" and clicking "set player position". Just click where you want him to start and walla. If its still not working then you may need to go to "edit main file" and set the start board or something. It could be either one of the two but note: You do need to set both in order for your character to appear on the board and be able to control him.
And your not being annoying, dont worry. You just started so you're expected to have alot of questions Wink

### Fingerz91 · 2006-03-04 17:38 · #B303432

It worked, THANKS A MILLION! Also, my friend and I are a little experienced with game programming via GameMaker. We saw RPGToolkit and knew it to be a MUST USE! We are trying to create a seiries of games, each varying in graphics ect. the first game will be very basic, the second, a little more complicated, and so on until we reach 3-D Wink . I feel that this way, we can use the most out of TK while taking baby steps to learn the ins and out of the program.
Thank for being so supportive, and I will be sure to come back if I have any more questions via this post or somewhere else on the forum
