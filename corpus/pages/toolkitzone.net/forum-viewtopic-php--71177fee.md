---
kind: page
id: "toolkitzone.net/toolkitzone.net/forum/viewtopic.php?p=435152"
site: "toolkitzone.net"
title: "Code:"
original_url: "http://www.toolkitzone.net/forum/viewtopic.php?p=435152"
written: null
date_confidence: "unknown"
updated: null
captured: ["20080402103939"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.net/forum/viewtopic.php__p_435152", captured: "20080402103939", sha256: "d73dcc1dfc6f56f302213b1794263a69e7217656b5d56545897963d886d669ec", wayback_url: "https://web.archive.org/web/20080402103939/http://www.toolkitzone.net/forum/viewtopic.php?p=435152"}
---

# Code:

Sending a parameter to a thread
What I want to do is call multiple instances of the same thread, but pass different parameters to each of them. A simple example would be if I had a program, MyThread.prg
**Code:**
```
//MyThread.prg local(cnvBS) = createCanvas(cnvBSWidth, cnvBSHeight) rendernow("on") while (loop == true) { setImage(graphic, 0, 0, xSize, ySize, cnvBS) drawCanvas(cnvBS, xloc, yloc, cnvBSWidth, cnvBSHeight, cnvRenderNow) }
```
How would I go about sending this thread the variables for: graphic xSize ySize cnvBSWidth cnvBSHeight xloc yloc I don't really know how to go about setting these variables so I could have two of these threads going at once. I can do it easily if I just create MyThread1.prg, and MyThread2.prg and just set the values:
**Code:**
```
//MyThread1.prg local(xSize) = 32 local(ySize) = 64 local(cnvBSWidth) = 100 ...
```
**Code:**
```
//MyThread2.prg local(xSize) = 132 local(ySize) = 164 local(cnvBSWidth) = 300 ...
```
But this is grossly inefficient. Anyone got any suggestions? Thanks
[![](images/avatars/625094848457cf1f58da78.gif)](profile.php?mode=viewprofile&u=14726)
I haven't actually tested this command out, but it seems to be what you're looking for. All you have to do is have a function in your thread that sets your variables, and have the tellThread command call that function.
<http://tk3.toolkitzone.com/help/?page=19#tellthread>
________________+++_--_=-_-_-_+_--===_==---_=----_---==_-====_+++________________
**Coming Soon: , Website: , Learn RPG Code: Chase_Engine [Enter-Key.net](http://www.enter-key.net) [Read This Tutorial!](http://www.toolkitzone.com/library.php?doc=328)**
Yea, I'm familiar with tellthread. But it only runs a function inside the thread I want to run. That means, I have to write dozens of stupid little functions to set each variable case... That just feels rather inefficient. But, I suppose it's a potential workaround. Thanks EDIT: A side note. I can't seem to find the answer in the search... If I start a thread from another program, i.e.
**Code:**
```
tid = thread("MyThread.prg",0)
```
It appears the thread doesn't start to run until the program that called it quits... I am trying to run 1 program that would create several threads in the background during the program's execution, then at the end, kill the threads. But the threads don't appear to run until the main program ends... which is totally defeating the purpose...
[![](images/avatars/625094848457cf1f58da78.gif)](profile.php?mode=viewprofile&u=14726)
tellThread is more versatile than that...
**Code:**
```
// MyThread.prg local(xSize); local(ySize); local(cnvBSWidth); local(init) = false; local(loop) = true; until (init) {} local(cnvBs) = createCanvas(cnvBSWidth, cnvBSHeight); renderNow(true); while (loop) { setImage(graphic, 0, 0, xSize, ySize, cnvBS); drawCanvas(cnvBs, xLoc, yLoc, cnvBSWidth, cnvBSHeight, cnvRenderNow); }
```
**Code:**
```
// Program that creates thread function threadBS(xSize, ySize, cnvBSWidth) { local(threadID) = thread("MyThread.prg", 0); tellThread(threadID, "xSize = " + xSize); tellThread(threadID, "ySize = " + ySize); tellThread(threadID, "cnvBSWidth = " + cnvBSWidth); tellThread(threadID, "init = true"); return threadID; } firstInst = threadBS(32, 64, 100); secondInst = threadBS(132, 164, 300);
```
One problem is I can't seem to pass strings to the thread, also that functions won't access the program's local variables, either the variables in functions are global or they are local to the function. I'm pretty sure tellThread (from my tests so far) is basically just the RPGCode command, but relevant to threads. It will run code in threads that are local to the instance of that particular thread.
________________+++_--_=-_-_-_+_--===_==---_=----_---==_-====_+++________________
**Coming Soon: , Website: , Learn RPG Code: Chase_Engine [Enter-Key.net](http://www.enter-key.net) [Read This Tutorial!](http://www.toolkitzone.com/library.php?doc=328)**
I suppose I *wasn't* familiar enough with tellthread... Thanks again.
[![](images/avatars/625094848457cf1f58da78.gif)](profile.php?mode=viewprofile&u=14726)
Threads are for executing code over RPG Toolkits regular gameplay multitasking (ie when no program is executing). Just like when sprites stop moving when you run a program, so do the threads. I suppose you could setup all the threads, give back control to the RPG Toolkit Engine while the threads are executing, then have one master thread decide when to execute another program that will kill all of them. All you'd have to do is make sure the player cannot walk (unless you want him to be able to). All of the sprites' walking programs will run too.
________________+++_--_=-_-_-_+_--===_==---_=----_---==_-====_+++________________
**Coming Soon: , Website: , Learn RPG Code: Chase_Engine [Enter-Key.net](http://www.enter-key.net) [Read This Tutorial!](http://www.toolkitzone.com/library.php?doc=328)**
Wait, so I can't have a thread executing at the same time as another program? I suppose that's probably why things aren't working as I want them to. I worry the master thread concept will be too slow. Oh well... Btw, I added a few debugger lines in the thread
**Code:**
```
debug(true) until (init) {} local(cnvBs) = createCanvas(cnvBSWidth, cnvBSHeight); debugger("StatsLoaded")
```
But the debugger doesn't appear and no graphics appear either (I added a line to set the graphic variable) This is probably why I keep giving up on threads every time I start looking at them again. Thanks though.
[![](images/avatars/625094848457cf1f58da78.gif)](profile.php?mode=viewprofile&u=14726)
It'll work if you use tellThread to set init to be true. The only catch is you have to use tellThread from another thread for it to work, because it won't execute in a non multitasking program.
________________+++_--_=-_-_-_+_--===_==---_=----_---==_-====_+++________________
**Coming Soon: , Website: , Learn RPG Code: Chase_Engine [Enter-Key.net](http://www.enter-key.net) [Read This Tutorial!](http://www.toolkitzone.com/library.php?doc=328)**
Sending a parameter to a thread
