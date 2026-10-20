---
kind: forum-thread
id: "toolkitzone-forums/30593"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Newbie Haven"
skin: "phpbb2"
thread_id: "30593"
title: "um...using mouse instead of keyboard..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=30593"
written: "2006-06-15T22:02:00"
last_post: "2006-06-18T23:18:00"
date_confidence: "exact"
captured: ["20060629082907"]
author: "TKFanBoy"
repliers: ["Scott92002000", "Maria", "Malegnis"]
authors: ["TKFanBoy", "Scott92002000", "Maria", "Malegnis"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_328740_amp_3Bsid_497143305248e29d431accf0730516d1", captured: "20060629082907", sha256: "1a9c4e73e631b30c33e41affa0e527f218dfee5db6e1052434ec1f4886b96bd0", wayback_url: "https://web.archive.org/web/20060629082907/http://www.toolkitzone.com/forums/viewtopic.php?p=328740&amp%3Bsid=497143305248e29d431accf0730516d1"}
links:
  - {url: "http://www.toolkitzone.com/fileman.php?id=3&file=1207", status: "captured", local: "wayback/toolkitzone.com/fileman.php__id_3_file_1207"}
---

# um...using mouse instead of keyboard...

### TKFanBoy · 2006-06-15 22:02 · #B327942

Hello guys, I'm starting over again,lol, haven't touched TK in a while
This time, I want to use mouse instead, the question is...how do I know when mouse clicks on the board or not? It's not like TK3 has things like tile_click, hehe

### Scott92002000 · 2006-06-15 22:06 · #B327946

**TKFanBoy wrote:**

> Hello guys, I'm starting over again,lol, haven't touched TK in a while
> This time, I want to use mouse instead, the question is...how do I know when mouse clicks on the board or not? It's not like TK3 has things like tile_click, hehe
>

no, but it does have

**Quote:**

> NAME: SetButton
> FORMAT: setButton(file$, pos!, x!, y!, width!, height!)
> This command places a button on the screen. In conjunction with the CheckButton and MouseClick commands, you can make working, clickable buttons for menus, and other things.
> - file$ is the filename of the button to set on the screen.
> - pos! is the 'slot' position to set the button in.
> - x!,y! are the x and y coordinates on the screen to place the button.
> - width!,height! are the width and height of button.
>
> **Code:**
>
> ```
> // Set the button...
>
>
> setButton("button1.jpg", 0, 10, 10, 100, 100)
>
>
> done! = false
>
>
> // Loop through while done! is equal
>
>
> // to it's inital value...
>
>
> while (!done!)
>
>
> {
>
>
>    mouseClick(mx!, my!)
>
>
>    dest! = CheckButton(mx!, my!)
>
>
>    // Check if a button was pressed
>
>
>    if (dest! == 0)
>
>
>    {
>
>
>       mwin("You pressed a button!")
>
>
>       wait()
>
>
>       mwinCls()
>
>
>       done! = true // Break out of the loop
>
>
>    }
>
>
> }
>
>
> clearButtons()
> ```

### TKFanBoy · 2006-06-15 22:49 · #B327972

oh, i get it
I'll put a huge while loop on every board,lol
thank you

### Maria · 2006-06-16 01:09 · #B328016

you could try...
this: <http://www.toolkitzone.com/fileman.php?id=3&file=1207>

### TKFanBoy · 2006-06-16 20:00 · #B328250

Lol, I got this, but I just didn't get the code, I couldn't see how it determines when you clicked the mouse
Now I thought things through...I have another question
What can I do about NPCs? I can't figure out any way to make an NPC to talk with a mouse unless I make it that they talk as long as my char touches them. There's no problem with that, but is it possible to make it so that I click on the NPC and activates the NPC program?

### Malegnis · 2006-06-17 19:38 · #B328494

im with you and i hate the damned keyboard.
so here is all you need.
1. something to make buttons (paint sux but it will work)
2.

**helpfiles wrote:**

> NAME: SetButton
> FORMAT: setButton(file$, pos!, x!, y!, width!, height!)
> This command places a button on the screen. In conjunction with the CheckButton and MouseClick commands, you can make working, clickable buttons for menus, and other things.
> - file$ is the filename of the button to set on the screen.
> - pos! is the 'slot' position to set the button in.
> - x!,y! are the x and y coordinates on the screen to place the button.
> - width!,height! are the width and height of button.
> Code:
>
> **Code:**
>
> ```
> // Set the button...
>
>
> setButton("button1.jpg", 0, 10, 10, 100, 100)
>
>
> done! = false
>
>
> // Loop through while done! is equal
>
>
> // to it's inital value...
>
>
> while (!done!)
>
>
> {
>
>
>    mouseClick(mx!, my!)
>
>
>    dest! = CheckButton(mx!, my!)
>
>
>    // Check if a button was pressed
>
>
>    if (dest! == 0)
>
>
>    {
>
>
>       mwin("You pressed a button!")
>
>
>       wait()
>
>
>       mwinCls()
>
>
>       done! = true // Break out of the loop
>
>
>    }
>
>
> }
>
>
> clearButtons()
> ```
>

3.

**helpfiles wrote:**

> NAME: Wait for mouse click
> FORMAT: mouseClick(x!, y![, wait!])
> This command waits for the user to click the mouse, storing the location in x,y. This command is like the Wait command, but the player has to click a button set with the SetButton command instead of pressing a key on the keyboard.
> - x!,y! are the returned x and y coordinates of where the user clicked.
> - wait! is an optional parameter. If it is set to 1, it will not wait for the user.
>
> **Code:**
>
> ```
> // Set the button...
>
>
> setButton("button1.jpg", 0, 10, 10, 100, 100)
>
>
> done! = false
>
>
> // Loop through while done! is equal
>
>
> // to it's inital value...
>
>
> while (!done!)
>
>
> {
>
>
>    mouseClick(mx!, my!)
>
>
>    dest! = CheckButton(mx!, my!)
>
>
>    // Check if a button was pressed
>
>
>    if (dest! == 0)
>
>
>    {
>
>
>       mwin("You pressed a button!")
>
>
>       wait()
>
>
>       mwinCls()
>
>
>       done! = true // Break out of the loop
>
>
>    }
>
>
> }
>
>
> clearButtons()
> ```
>

4.

**helpfiles wrote:**

> NAME: Check if a Button was pressed
> FORMAT: buttonNum! = CheckButton(x!, y!)
> This command checks if a button set with the SetButton command was pressed.
> - x!,y! are the x and y coordinates of the last mouse click on the screen.
> - buttonNum! is the returned value. If no buttons were pressed, buttonNum! is set to requal -1. Otherwise, it is set to the number of that button.
>
> **Code:**
>
> ```
> // Set the button...
>
>
> setButton("button1.jpg", 0, 10, 10, 100, 100)
>
>
>
>
>
> // Loop through while done! is equal
>
>
> // to it's inital value...
>
>
> done! = false
>
>
> while (!done!)
>
>
> {
>
>
>    mouseClick(mx!, my!)
>
>
>    dest! = CheckButton(mx!, my!)
>
>
>
>
>
>    // Check if a button was pressed
>
>
>    if (dest! == 0)
>
>
>    {
>
>
>       mwin("You pressed a button!")
>
>
>       wait()
>
>
>       mwinCls()
>
>
>       done! = true // Break out of the loop
>
>
>    }
>
>
> }
>
>
> clearButtons()
> ```
>

hope this helps you out

### TKFanBoy · 2006-06-18 23:18 · #B328740

AAh, thanks a lot, guys, I really appreciate it.
