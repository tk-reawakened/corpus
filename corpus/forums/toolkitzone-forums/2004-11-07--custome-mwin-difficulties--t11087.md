---
kind: forum-thread
id: "toolkitzone-forums/11087"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "customisation"
skin: "phpbb2"
thread_id: "11087"
title: "Custome Mwin Difficulties"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11087"
written: "2004-11-07T07:41:00"
last_post: "2004-11-11T01:28:00"
date_confidence: "exact"
captured: ["20050110143030"]
author: "Kabuki"
repliers: ["Gnarf", "Dont_Think_So", "Nick", "Asimir", "Alex0Xander"]
authors: ["Kabuki", "Gnarf", "Dont_Think_So", "Nick", "Asimir", "Alex0Xander"]
posts_present: 13
pages_present: [2]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 15, url: "http://toolkitzone.com/forums/viewtopic.php?t=11087", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_123681_amp_", captured: "20050110143030", sha256: "0f841e60228475520b3f152978be471f6853b5ad12ef28cb44dc60311aa94618", wayback_url: "https://web.archive.org/web/20050110143030/http://www.toolkitzone.com/forums/viewtopic.php?p=123681&amp="}
links:
  - {url: "http://img.photobucket.com/albums/v456/KabukiBlitz/Dark%20angel%20Designs/Amessup.jpg", status: "external", local: null}
---

# Custome Mwin Difficulties

> [!missing] gap:1-15 · http://toolkitzone.com/forums/viewtopic.php?t=11087 · never-captured
> Page 1 of 2 was not recovered.

### Kabuki · 2004-11-07 07:41 · #B122254

Thanks a ton!

### Gnarf · 2004-11-07 07:42 · #B122255

**Kabuki wrote:**

> Thanks a ton!
>

No problem, and I know it's sort of messy, but it's the best I could come up with, although, there might still be problems...
I hope not...

### Kabuki · 2004-11-07 07:46 · #B122259

am I suppose to put the #wait command in there and...
Error: Method not found!-- #mywin("Hello","How are","you?")
is it suppose to be mwin? or mywin or... Nvm I found the problem

### Gnarf · 2004-11-07 07:49 · #B122260

**Kabuki wrote:**

> am I suppose to put the #wait command in there and...
> Error: Method not found!-- #mywin("Hello","How are","you?")
> is it suppose to be mwin? or mywin or... Nvm I found the problem
>

No need for #wait...
#pause() method does it all.
In place of the #wait, just use #pause()
But before you can use it you need to include the file.prg with the #pause method, and I told you to save it as mwinmethod.prg so include that before use of #pause or #mymwin.
Like:

**Code:**

```
#include("mwinmethod.prg")
```

### Kabuki · 2004-11-07 07:52 · #B122261

Yes i've put that in there, and it has pause in it, do I have to put a another pause in? The #mymwin is doesn't work... it says I can not find that method.

### Dont_Think_So · 2004-11-07 07:55 · #B122263

Your sure you put #include("mymwin.prg") at the top of your program?

### Kabuki · 2004-11-07 08:04 · #B122264

yes... :
#Include("mwinmethod.prg")
#mymwin("Hello","how are","you?")
It says:
Error: can not find Method

### Dont_Think_So · 2004-11-07 08:10 · #B122266

err... this may sound stupid, but did you put the method in a file called mwinmethod.prg? Smile

### Nick · 2004-11-07 14:49 · #B122313

**Kabuki wrote:**

> I'm using tk 2.2, tk3 doesn't work on my computer... but let me try
> Edit: Still doing it...
>

Then why the hell are you posting in the Toolkit 3 forums?

### Asimir · 2004-11-07 19:33 · #B122403

**Code:**

```
#clear

#Mymwin("sdlkj","dfd","fdfd",10,10,"graphic.jpg")

#method mymwin(line1$, line2$, line3$, x!, y!, graphic)

{

#SaveScreen()

#SetImage("abbey1.gif", 10, 10, 50, 50)

#y!=y!+2

#text(2,y!,"Hello")

#y!=y!+2

#text(2,y!,"How Are")

#y!=y!+2

#text(2,y!,"You")

#while(enter_press!=0)

{

#wait(enter$)

#If(enter$="ENTER")

{

#RestoreScreen()

#Enter_Press!=1

}

}

}
```

### Kabuki · 2004-11-07 20:55 · #B122445

**Quote:**

> #clear
> #Mymwin("sdlkj","dfd","fdfd",10,10,"graphic.jpg")
> #method mymwin(line1$, line2$, line3$, x!, y!, graphic)
> {
> #SaveScreen()
> #SetImage("abbey1.gif", 10, 10, 50, 50)
> #y!=y!+2
> #text(2,y!,"Hello")
> #y!=y!+2
> #text(2,y!,"How Are")
> #y!=y!+2
> #text(2,y!,"You")
> #while(enter_press!=0)
> {
> #wait(enter$)
> #If(enter$="ENTER")
> {
> #RestoreScreen()
> #Enter_Press!=1
> }
> }
> }
>

Thank You

**Quote:**

> Then why the hell are you posting in the Toolkit 3 forums?
>

Because I use TK3 to do all the stuff for my game, Tiles boards, programs, ect... I would use it to make a game if it didn't do this when I tryed to make one:
![](http://img.photobucket.com/albums/v456/KabukiBlitz/Dark%20angel%20Designs/Amessup.jpg)

**Quote:**

> err... this may sound stupid, but did you put the method in a file called mwinmethod.prg?
>

Yes I'm positive, Thanks to Asimir it works now ^-^
Thanks for helping Gnarf.

### Alex0Xander · 2004-11-10 23:20 · #B123595

**Asimir wrote:**

>
> **Code:**
>
> ```
> #clear
>
>
> #Mymwin("sdlkj","dfd","fdfd",10,10,"graphic.jpg")
>
>
> #method mymwin(line1$, line2$, line3$, x!, y!, graphic)
>
>
> {
>
>
> #SaveScreen()
>
>
> #SetImage("abbey1.gif", 10, 10, 50, 50)
>
>
> #y!=y!+2
>
>
> #text(2,y!,"Hello")
>
>
> #y!=y!+2
>
>
> #text(2,y!,"How Are")
>
>
> #y!=y!+2
>
>
> #text(2,y!,"You")
>
>
> #while(enter_press!=0)
>
>
> {
>
>
> #wait(enter$)
>
>
> #If(enter$="ENTER")
>
>
> {
>
>
> #RestoreScreen()
>
>
> #Enter_Press!=1
>
>
> }
>
>
> }
>
>
> }
> ```
>

This may just sound stupid, but should'nt you put the variables withing the Text commands? like;

**Code:**

```
Text(2,y!,line1$)

y!=y!+2

Text(2,y!,line2$)

y!=y!+2
```

Confused

### Kabuki · 2004-11-11 01:28 · #B123681

LOL, I already added that myself. I ain't retarded... I made it work =p
