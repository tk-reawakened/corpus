---
kind: forum-thread
id: "toolkitzone-forums/11893"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "toolkit 2.x support"
skin: "phpbb2"
thread_id: "11893"
title: "Spec. Character Entry"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11893"
written: "2004-11-29T03:34:00"
last_post: "2004-11-30T01:54:00"
date_confidence: "exact"
captured: ["20050113181514"]
author: "Guest"
repliers: ["zeno", "marcos"]
authors: ["Guest", "zeno", "marcos"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_131884_amp_", captured: "20050113181514", sha256: "7018bd59dc270e7c7d5cdadf8ce90d64cd8539cef793500d3bc40f1b106231f0", wayback_url: "https://web.archive.org/web/20050113181514/http://www.toolkitzone.com/forums/viewtopic.php?p=131884&amp="}
links: []
---

# Spec. Character Entry

### Guest · 2004-11-29 03:34 · #B131415

I NEED to know how a specific character can activate a program...
Example : I Can change into any given character to walk around at any point of time.... But say " Rew " can Only Go Into A Bar .... I Just Changed Into Another Character And I Am Not Supposed To Go In The Bar .... I Change Into "Rew" And I Am Able To Go In The Bar !
HOW DO I MAKE IT SO SOME CHARACTERS CAN AND CANNOT DO THINGS ?????????[/rpgcode]

### zeno · 2004-11-29 21:40 · #B131714

set a variable like: #rewgointobar! = 1
Set this when Rew is your main player...otherwise if your other character is your main one then set this: #rewgointobar! = 0
under the program (going into the bar):

**rpgcode:**

```
if(rewgointobar! == 1)

{

     Send("bar.brd")

}

if(rewgointobar! == 0)

{

     Mwin("Rew can only go into this bar")

     Wait(a$)

}
```

### Guest · 2004-11-29 23:03 · #B131781

OMG! !!!!!! Thank You Soooo Much ! IT should work.

### marcos · 2004-11-30 01:54 · #B131884

zeno, your suggestion will work, but, how would you check if Rew is in the party? I have a suggestion for this, let's use a method "checkplayer" that can be used for any player, you just have to change what to do with the values you receive.

**Code:**

```
* calling the method

*change this if you want

#checkplayer("Rew", RewInParty!)

*after the method

#if(RewInParty!=0)

{

*rew isn't there, add some coding here*

}

#if(RewInParty!=1)

{

*rew's there, #send him in*

}
```

the method declaration, don't change it

**Code:**

```
#method checkplayer(playertocheck$, isinparty!)

{

#isinparty!=0

#for(pnum!=0;pnum!<=4;pnum!=pnum!+1)

{

#if(playerhandle[pnum!]$=playertocheck$)

   {

   #isinparty!=1

   }

}

#returnmethod(isinparty!)

}
```

So, what about it?
I'm gonna add it to the Resources, I guess.
