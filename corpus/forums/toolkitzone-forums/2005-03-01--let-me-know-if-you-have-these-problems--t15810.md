---
kind: forum-thread
id: "toolkitzone-forums/15810"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "15810"
title: "Let me know if you have these problems ;)"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=15810"
written: "2005-03-01T02:43:00"
last_post: "2005-03-14T17:02:00"
date_confidence: "exact"
captured: ["20050325131906"]
author: "Codester"
repliers: ["oblivious_casualty", "Delano", "Colin", "Sander", "AlienDude"]
authors: ["Codester", "oblivious_casualty", "Delano", "Colin", "Sander", "AlienDude"]
posts_present: 14
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_180384_amp_", captured: "20050325131906", sha256: "5a3c31cad51404d2a49dde24c2c18a0e19138c813ee2f6de49d429980db848bc", wayback_url: "https://web.archive.org/web/20050325131906/http://toolkitzone.com:80/forums/viewtopic.php?p=180384&amp"}
links:
  - {url: "http://colin.mysticsoftware.net", status: "external", local: null}
---

# Let me know if you have these problems ;)

### Codester · 2005-03-01 02:43 · #B173589

Hi there. I've been experiencing these problems with the latest intermediate 3.06 release, 2005-02-26. I'm using Windows 98, and have 256MB of RAM, and a 1.6Ghz processor. I'm trying to figure out if these are bugs or not before I submit a report to the developers. Just trying to see if other users have these problems.
In the toolkit editor:
* Copy and Paste don't work at all in the Toolkit Editor for me.
I thought this bug was fixed, but apparently the fix didn't work
for me. One interesting thing is, if I copied something from
Notepad to another instance of Notepad, then copied something
from the program editor, and pasted it in notepad, the thing
I copied from gets pasted there. I think, for me, it is not
writing to the copy & paste buffer at all. Worked for me in
RPG Toolkit 3.04 and 3.05, though.
* Also, sometimes indented commands in the program editor get
wrapped when it's not the end of the line.
* The cursor blinks in windows for some reason.
When testing the game:
* After the first battle, animations slow down somewhat, both in
pixel mode, and in tile mode.
* In all cases, pixel mode runs more slowly than tile mode.
* Also, the DirSav() command. It usually doesn't respond, and I have
to use ESC, sometimes it locks up and I have to wait. In any case I
have to try again an erratic number of times before I can pick what
file I want to load or save.
* Include() locks up the translator in built (EXE) files, when testing
uncompiled programs, it works just fine.
Problems I believe are caused by tk3menu.dll:
* From the internal menu system, the same DirSav() problem is
experienced, except when you save something, it saves it, then keeps
looping and asking you what file to save to over and over again. I have
to say cancel to stop. When I load from the internal menu system, I
have to press esc, cause it locks up. Then, it just returns me to the
game, and doesn't load!!! I coded a custom main menu, and Load()
works there, so I think it is the internal menu system which has problems.
Are any of you having any of the same problems? Are you not having some of these problems?
That's it for now.

### oblivious_casualty · 2005-03-01 03:55 · #B173635

pixel movement is supposed to be slower than tile movement in all instances because you don't move as far in one push.
although after changing boards when testing my game, the movement slows to a crawl, but the fps rises.

### Codester · 2005-03-02 05:55 · #B174160

**oblivious_casualty wrote:**

> pixel movement is supposed to be slower than tile movement in all instances because you don't move as far in one push.
> although after changing boards when testing my game, the movement slows to a crawl, but the fps rises.
>

Thanks for telling me that about pixel mode. I decided to see if I could reproduce the problem you were having with pixel mode slowing down when boards change. To do this, I had to create a second test board. While creating the board, I discovered two problems with the board editor. But, more on that later. I tried directional links, sending the player directly to the other board, and tried both these things with the Push() in pixel increments option on and off. Changing boards didn't seem to slow down pixel movement for me. Are you testing the latest 2005-02-26 release extracted into a folder where you installed 3.05? 'Cause that's how I have it set up. Also, what version of Windows do you have? I'm using Win 98.
BTW, here's the problems I found in the board editor:
More Problems!
* Flood fill in the board editor is acting very weird. It acts like the
Delete Layer option, except it doesn't erase programs, items, or tile
type data. Also, when you point the mouse over the paint bucket icon in
the toolbar, the label "Eraser" pops up. Hmmm...
* Like I said, flood fill acts like the Delete Layer option, but when you
click Delete Layer, it doesn't work at all! It doesn't have any effect on anything.
That's all I have to say for now.

### Delano · 2005-03-02 17:13 · #B174244

Thanks Codester, your descriptions of the problems are very useful!
- Copy / Paste are working for us (well, me at least) so it might be a Win98 thing. Has it worked in previous builds? It's interesting that it's worked in 3.0.5...
- The cursor blinks in windows? Which windows? All the time? When you move it? When you move it over certain things?
- When you say animations slow down after fighting, do you mean movement in general? What happens to the fps in this time?
- Pixel movement is a little slower; you can compensate by setting individual movement speeds for each character in the character editor (although if you have a low fps you may not be able to increase the speed from what it is now).
- DirSav() - it doesn't respond as in it doesn't show a Save window, or it locks up after saving? Saving and Loading work for me, although I do experience the looping problem in the default menu.
- Board flood fill - when you say it behaves like Delete Layer, you mean it erases all the tiles on the layer? Does the flood fill work for you in the Tile Editor? If not, then it's probably a Win98 problem, but we can provide an alternative possibly. And as for Delete Layer itself, it appears the code was never written for it; might be a remnant of tk2.
obct, we'll talk about your problem. Razz

### Codester · 2005-03-03 08:41 · #B174630

Thanks Delano. Also, thanks for noticing the topic subject. "Let me know if you have these problems" should be the name of it. Oops. Fixed now.

**Quote:**

> - Copy / Paste are working for us (well, me at least) so it might be a Win98 thing. Has it worked in previous builds? It's interesting that it's worked in 3.0.5...
>

* Well, it didn't work in 2005-02-21, but I haven't downloaded any earlier intermediate builds.
I'll download some other intermediate builds for 3.0.6 later and try them out, after I get
some sleep.

**Quote:**

> - The cursor blinks in windows? Which windows? All the time? When you move it? When you move it over certain things?
>

* The cursor blinks both when moving in certain spots and when sitting in these spots, but
mostly when the cursor is sitting over these certain spots. I call these spots "blink zones".
It blinks in the work area, and the right half of the left toolbar. It also blinks in the top
toolbar, and the right toolbar, except when Project List, New, or Current Tileset is open.
NOTE: I can have the tip of the cursor in one of the blink zones, and the cursor will blink.
It doesn't matter what window is open, these zones on the screen almost always make the cursor
blink, with a few exceptions like the space between the work area and the bottom toolbar of
the board editor makes it blink but the bottom toolbar doesn't. Secondly, the work area zone
never causes cursor blinking when a dialog box is open (e.g. Create New Project, Open, etc.),
but the other zones still cause it when a dialog box is open. Also, in the tile editor, the
space between the work area and the bottom toolbar doesn't make it blink, and neither does
the bottom toolbar for the tile editor. This could all be explained better with images. Maybe
in the future, when I have posted 100 posts, I'll be able to upload the images I have into
"my stuff" which show these exceptions in more detail. This explanation will have to do for
now.

**Quote:**

> - When you say animations slow down after fighting, do you mean movement in general? What happens to the fps in this time?
>

* All player and item movement on the board get slowed down. Both in tile mode and pixel in mode, after a
battle, it slows down a lot. Did I say somewhat? I meant a lot. Slowed down tile mode is, of
course, faster than slowed down pixel mode. Also, I've noticed that when you change to another
board, things go back to the normal speed again. When you change back to the board that you
had the battle on, things stay at the normal speed. Does fps mean frames per second? I don't
know how to tell that. How do you check what fps you are running at?

**Quote:**

> - Pixel movement is a little slower; you can compensate by setting individual movement speeds for each character in the character editor (although if you have a low fps you may not be able to increase the speed from what it is now).
>

* Thanks for the tip!
I'll get to the rest of your questions after I get some sleep.

### Codester · 2005-03-05 04:52 · #B175683

Update:
I am now testing with the 2005-03-02 build.
* Copy/Paste problem update. Copy/Paste stopped working for me in the 2005-02-19 build. It
worked before in the 2005-02-11 and 2005-02-18 builds.
* The slowing down after the first battle problem got fixed in the 2005-03-02 build! Very Happy
I found the fps option too. It was in plain sight the whole time, and I didn't even see it.
And now, the rest of your questions:

**Quote:**

> - DirSav() - it doesn't respond as in it doesn't show a Save window, or it locks up after saving? Saving and Loading work for me, although I do experience the looping problem in the default menu.
>

* DirSav() just causes the cursor to disappear when it doesn't work. I press the esc key,
and the cursor appears, but that's it. I have to just keep hitting that save button and esc
over and over until the save window pops up. When I do pick the filename to save, it doesn't
lock up. Sometimes, though, DirSav() works right away, the first time. See More Problems!
at the end of this post for why this happens.
* Also, I said loading in the default menu system doesn't work good either, first the DirSav()
problem is encountered, and then after you pick which file to load, all it does is make
the cursor disappear. Then I have to press enter a few times, then esc a few times, or
something like that, then wait, but it does work, the reason why I said it didn't before
was because of a problem. See More Problems! at the end of the post.

**Quote:**

> - Board flood fill - when you say it behaves like Delete Layer, you mean it erases all the tiles on the layer? Does the flood fill work for you in the Tile Editor? If not, then it's probably a Win98 problem, but we can provide an alternative possibly.
>

* Board flood fill erases all tiles on the layer in all cases, except when I fill a group
of tiles, let's say grass, with the same type of tile (grass), nothing happens. In the
tile editor, flood fill works, except when dealing with transparency. See More Problems!
for this transparency problem.

**Quote:**

> And as for Delete Layer itself, it appears the code was never written for it; might be a remnant of tk2.
>

* Aha! Well, I suppose that will have to wait until 3.0.7.
More Problems!
In the toolkit editor:
* I've had a tile editor flood fill problem when dealing with transparency, since 3.0.4.
Flood fill worked perfectly in 3.0.3c. Let's see, when the entire tile is transparent,
filling it with another color works correctly. However, let's say I drew a rectangle,
or any shape, in any color, completely enclosing a certain area of transparency. I
fill the transparent area inside that shape, and it gets filled correctly. The
transparency outside the shape, however, gets filled with a random color. Also, when I
draw a shape, enclosing a transparent area completely, and fill the outside transparent
area, the area inside the shape gets filled with a random color. Weird.
In the translator:
* I know why DirSav() works right away sometimes, and not right away other times, it's
because the window "This game was created with RPG Toolkit 3" gets left open when the next
instance of trans3 is started. When it isn't left open DirSav() doesn't work right away,
when it is, it works right away. Also, when it isn't left open, Load works, but when it is
left open Load doesn't work. I've noticed that this window doesn't pop up by itself, it runs
minimized, which is the reason why it doesn't always get closed. It stopped popping up by
itself in 3.0.5.
* I think I found out what some of Eternal EoN's problem is caused by in the topic "Redirect
is broken in 3.06 periodical build". I am experiencing this problem too, though it's not
Redirects. Whenever I use If() in an external method, trans3 freezes, and an hourglass just
sits there. Note that in system.pause() there is no If() statement. Here's a couple of short
demo programs which further illustrate my theory. (Copy/Paste don't work in the toolkit
editor for me, so I had to retype them by hand.)
First, the startup program is very simple.

**rpgcode:**

```
thisvar! = 0

extmethod.extmethod()
```

Then, there is another little program named extmethod.prg.

**rpgcode:**

```
Method extmethod()

{

     If(thisvar! == 0)

     {

          Text(1, 1, "thisvar! is equal to zero.")

     }

}
```

In fact, the Text() statement probably isn't even needed. Just to be sure, I took it out,
tried it again, and yep, same thing. It is not a problem with variables, I tried this, see,
replacing the If statement with a Text statement.

**rpgcode:**

```
Method extmethod()

{

     Text(1, 1, "thisvar! is equal to &lt;thisvar!&gt;")

}
```

Note: I tried to use < and > in the rpgcode tag and, after posting, it
put &lt; and &gt; there. Also, When ampersands are put in there,
after posting, they are replaced with &amp;.
The above example worked just fine. By the way, I am not experiencing the problem that
Eternal EoN had when actually running the game. Redirects work fine for me there too.
That's it for now.

### Colin · 2005-03-05 18:46 · #B175904

Don't use [ rpgcode ]; use [ code ].
Good show tracking that bug down to if (and other conditionals). It's fixed now. If you'd like to confirm, try the latest build [here](http://colin.mysticsoftware.net).

### Codester · 2005-03-06 01:48 · #B176114

I am happy to say that If() now works in external methods for me! Very Happy
One more problem down. Thanks for the tip about [ code ].

### Codester · 2005-03-07 05:50 · #B177013

Update:
I was testing out the 2005-03-05 further, and I noticed that the player doesn't show up on the board. There is no shadow,
black graphic, or anything as to even indicate his presence. All I see is just the green grass tile. During this time, the fps rises
upward, it hesitates sometimes, and even drops back down a little, but it ultimately rises, then after awhile, it stops going up
or down. This happens when everything is not moving. Normally, it would keep rising, but go down if something moved alot,
and when things were still, it would rise. Also, now when I press a movement key, or when an item moves, trans3 locks up,
an hourglass just sits there, and I can only press Ctrl+Alt+Del. I did notice that programs's graphics do not get displayed, all
I can see where they should be is the grass tile. When items are still, they aren't displayed either. when they are still, all I
can see where they should be is the grass tile. I tried running the demo game that comes with the toolkit using 2005-03-05's
build. Exactly the same thing happened.

### Colin · 2005-03-07 05:53 · #B177016

Well, I guess our graphic 'fixes' backfired, eh? ;)

### Sander · 2005-03-07 16:55 · #B177154

I'm having none of those problems with the 2005-03-05 build.

### Colin · 2005-03-07 22:47 · #B177235

Yeah, but you're not on the evil Windows 9x.

### Delano · 2005-03-08 14:34 · #B177603

**Colin wrote:**

> Well, I guess our graphic 'fixes' backfired, eh? Wink
>

Well it might not be so bad...
Best to stick with the penultimate build for the moment if you're getting that problem.

### AlienDude · 2005-03-14 17:02 · #B180384

Hmmm for some reason, the board gfx, still showed up for him, but now for me. they worked for 3.0.4, albeit very slow.
