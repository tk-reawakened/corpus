---
kind: forum-thread
id: "toolkitzone-forums/26965"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "26965"
title: "Help with getting an item's slot number."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=26965"
written: "2006-01-29T22:06:00"
last_post: "2006-02-05T00:17:00"
date_confidence: "exact"
captured: ["20060218123137"]
author: "TwinHamster"
repliers: ["slipknot42388", "DrJ", "DrakeLord", "zyrshnikashnu"]
authors: ["TwinHamster", "slipknot42388", "DrJ", "DrakeLord", "zyrshnikashnu"]
posts_present: 15
pages_present: [1]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 2, start: 16, end: 30, url: "http://toolkitzone.com/forums/viewtopic.php?t=26965&start=15", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_293617_amp_3Bsid_8af111ecf683ab6cee73498f96334cc2", captured: "20060218123137", sha256: "1270759a8f279f83f2c1d709cdcff46314b2c525ccde5adbbddc2ebf77370e37", wayback_url: "https://web.archive.org/web/20060218123137/http://www.toolkitzone.com/forums/viewtopic.php?p=293617&amp%3Bsid=8af111ecf683ab6cee73498f96334cc2"}
links: []
---

# Help with getting an item's slot number.

### TwinHamster · 2006-01-29 22:06 · #B293500

In one of my scripts, I'm trying to destroy an item after fighting it; however, I can't seem to find the item's slot number. I tried looking into the RPGcode menu on the board editor and then checking the item menu. I found that the item was listed as "item 4". So I tried the command [destroy item (4!)] only to find that it doesn't work. I've also tried removing the ! from the 4!, typing in the item's actual file name, the item's handle, but the system seems to just want to find a number. How do I get the item's slot number?
Any help would be appreciated.

### slipknot42388 · 2006-01-29 22:12 · #B293505

If you are using the defalt system for your Item's use
#destroyItem("potion.itm")
or #takeItem("potion.itm")
use one of those after the player uses the Item just make sure that inside the "" you have the item's file name that they will be using

### TwinHamster · 2006-01-29 22:31 · #B293509

The thing is, the item is being used as an NPC that was already on the board before any programs came along.
And I'm pretty sure that I've already tried using destroyitem-
Hmm...I might have forgetten those quotation marks. Uh...
[edit]:
Apparently that doesn't work either.
Here's the error message it gave:

**Code:**

```
Error: DestroyItem data element must be numerical!--

DestroyItem("squirrel with card.itm")
```

### DrJ · 2006-01-30 00:49 · #B293568

Use the item number. When you create the item you can set a slot number. Use this in your code.

### TwinHamster · 2006-01-30 03:21 · #B293613

I just made the npc a one type use npc. Thanks for the help though.

### DrJ · 2006-01-30 03:42 · #B293617

What do you mean a

**Quote:**

> I just made the npc a one type use npc.
>

Item numbers aren't hard at all!! If your using the board editor to set items, it will tell you what item is in what slot on the board editor. If you are using actuall code you can set the item yourself.
eg

**Code:**

```
createItem("soldier.itm", itemnum!)
```

That creates an item in slot itemnum! (which is 0 unless you declare otherwise).
then to erase and destroy item

**Code:**

```
eraseitem(itemnum!)

destroyitem(itemnum!)
```

Seriously it isn't that hard at all.

### TwinHamster · 2006-02-01 19:17 · #B294298

I created the item through the board editor. In the editor, there's an option where the item dies after it is used.
What don't you people get about the fact that the item is part of the board and not created through a code itself?

### DrakeLord · 2006-02-01 19:29 · #B294300

**TwinHamster wrote:**

> I created the item through the board editor. In the editor, there's an option where the item dies after it is used.
> What don't you people get about the fact that the item is part of the board and not created through a code itself?
>

Because a code to do so much more...

### DrJ · 2006-02-01 21:11 · #B294316

**TwinHamster wrote:**

> I created the item through the board editor. In the editor, there's an option where the item dies after it is used.
> What don't you people get about the fact that the item is part of the board and not created through a code itself?
>

Even if it is created with the board editor you can still use code to manipulate it.
It tells you the # of the item on the item menu in the board editor.

### TwinHamster · 2006-02-04 21:54 · #B295098

I have found the slot number when the item is created, but I can't use it.
And now when I try to use the create item command, it doesn't seem to work either.
Can I do this:
create item ("Squirrel.itm", 6)
to make the squirrel's slot number, 6.
Or do I have to, as topLizards did,
"createItem("soldier.itm", itemnum!)",
in which the slot number is stored in a variable?

### DrakeLord · 2006-02-04 22:22 · #B295114

It has to have the ! in it. You could have it 6! though. It doesn't have to be itemnum!.
I would be easier to remember that way.

### zyrshnikashnu · 2006-02-04 22:53 · #B295130

No, Drakelord, 6! would be incorrect. Since the value of the slot is 6, it should not be denoted as a variable. 6! is not the same as 6.
So, yes, TwinHamster, if this aspect of the item system of TK3 isn't messed up, you should be able to use 6 as the slot.

### DrakeLord · 2006-02-04 23:40 · #B295146

Oh...
In the helps file examples it had num!, so I thought it needed the !.

### zyrshnikashnu · 2006-02-04 23:51 · #B295150

"num!" is a variable. The data stored within the variable, for example 6, is not a variable. It's data. Razz

### DrakeLord · 2006-02-05 00:17 · #B295156

Oh...shows how much I know. Razz

> [!missing] gap:16-30 · http://toolkitzone.com/forums/viewtopic.php?t=26965&start=15 · never-captured
> Page 2 of 2 was not recovered.
