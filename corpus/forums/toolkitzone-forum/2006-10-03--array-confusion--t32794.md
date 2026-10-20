---
kind: forum-thread
id: "toolkitzone-forum/32794"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "32794"
title: "Array Confusion"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=32794"
written: "2006-10-03T14:59:00"
last_post: "2006-10-04T12:56:00"
date_confidence: "exact"
captured: ["20070320195518"]
author: "kahless"
repliers: ["Levi", "Fire", "DrakeLord", "rpg gamer 17", "iFrog", "lordadonis", "Occasionally_Correct"]
authors: ["kahless", "Levi", "Fire", "DrakeLord", "rpg gamer 17", "iFrog", "lordadonis", "Occasionally_Correct"]
posts_present: 9
pages_present: [2]
pages_total: 2
posts_per_page: 10
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 10, url: "http://toolkitzone.com/forum/viewtopic.php?t=32794", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_352436", captured: "20070320195518", sha256: "6ddb3294c38c15e3b1b4889b95143fbe360aaa78b535a25527ed7a44aac72c22", wayback_url: "https://web.archive.org/web/20070320195518/http://toolkitzone.com/forum/viewtopic.php?p=352436"}
links: []
---

# Array Confusion

> [!missing] gap:1-10 · http://toolkitzone.com/forum/viewtopic.php?t=32794 · never-captured
> Page 1 of 2 was not recovered.

### kahless · 2006-10-03 14:59 · #K352409

One more stupid question, will this work for making global arrays?

**Code:**

```
Method initialize_variables()

{

Global(Char[0]!)

   Char[0]! = 2

For(count! = 1; count! < 21; count!++)

   {

      Global(Char[count!]!)

      Char[count!]! = 0

   }

Global(Plot[0]!)

Plot[0]! = 2

For(iPlotCount! = 1; iPlotCount! < 25; iPlotCount!++)

   {

      Global(Plot[iPlotCount!]!)

      Plot[iPlotCount!]! = 0

   }

For(iQuestCount! = 0; iQuestCount! < 15; iQuestCount!++)

   {

      Global(Quest[iQuestCount!]!)

      Quest[iQuestCount!]! = 0

   }

Global(iKarma!)

iKarma! = 50

iPartySize! = 4

}
```

### Levi · 2006-10-03 17:27 · #K352422

As far as I'm aware you can't use global() on arrays. I tried a while back and couldn't get the right combination.
global(MyArray!)
global(MyArray[]!)
global(MyArray[0]!)
Nothing ever seemed to work.

### Fire · 2006-10-03 18:38 · #K352436

**Quote:**

> what the crap does cut do? <-- everyone laughed at me in computer class when i asked that (including the teacher )
>

Hahahahaha
Cut deletes the selected area.

### DrakeLord · 2006-10-03 18:46 · #K352438

**Fire wrote:**

>
> **Quote:**
>
> > what the crap does cut do? <-- everyone laughed at me in computer class when i asked that (including the teacher )
> >
>
> Hahahahaha
> Cut deletes the selected area.
>

Sort of. It deletes the selected area, and copies it, so you can paste it with Ctrl+V.

### rpg gamer 17 · 2006-10-03 20:44 · #K352458

oh okay thxs.

### iFrog · 2006-10-03 23:19 · #K352501

**Fire wrote:**

>
> **Quote:**
>
> > what the crap does cut do? <-- everyone laughed at me in computer class when i asked that (including the teacher )
> >
>
> Hahahahaha
> Cut deletes the selected area.
>

Hahahaha
Cut removes an item from one area, taking it to the clipboard, where it can later be used in a paste command elsewhere. Wink

### lordadonis · 2006-10-03 23:45 · #K352513

**iFrog wrote:**

>
> **Fire wrote:**
>
> >
> > **Quote:**
> >
> > > what the crap does cut do? <-- everyone laughed at me in computer class when i asked that (including the teacher )
> > >
> >
> > Hahahahaha
> > Cut deletes the selected area.
> >
>
> Hahahaha
> Cut removes an item from one area, taking it to the clipboard, where it can later be used in a paste command elsewhere. Wink
>

I disagree! Cut is what happens when you slice someone up. Blood oozing every-which-way. Except on the computer. You slice that stupid document to pieces, allowing you to put pieces in other documents. And if you cut it up enough, your computer will start to ooze blood.... right before it crashes.
Clipboard, ha! That's the computer's retaliation technique. It savagely beats itself up with that board, so right when you need it most it crashes from the pain.

### kahless · 2006-10-04 12:36 · #K352627

As much as I like the Cut command, I must insist on staying with the topic.
Is there a way to make the variables Global without having to declare them as such? I haven't found the AutoLocal() command in Start.prg, but I think if I declare my arrays before then, they should be global by default. I just don't know how to autoglobalize, if you take my meaning.

### Occasionally_Correct · 2006-10-04 12:56 · #K352630

All variables default to global scope unless you specify otherwise. Just declare them normally and you should be fine. Smile
