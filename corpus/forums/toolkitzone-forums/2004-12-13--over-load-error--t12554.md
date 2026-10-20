---
kind: forum-thread
id: "toolkitzone-forums/12554"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "toolkit 2.x support"
skin: "phpbb2"
thread_id: "12554"
title: "over load error"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12554"
written: "2004-12-13T10:32:00"
last_post: "2004-12-14T00:38:00"
date_confidence: "exact"
captured: ["20050119034110"]
author: "Unelemented"
repliers: ["Dont_Think_So"]
authors: ["Unelemented", "Dont_Think_So"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139210_amp_", captured: "20050119034110", sha256: "1b5556addc46fefd8c9b71131455e9612857617ce1352c7c4358d2f7600f7a80", wayback_url: "https://web.archive.org/web/20050119034110/http://www.toolkitzone.com/forums/viewtopic.php?p=139210&amp="}
links: []
---

# over load error

### Unelemented · 2004-12-13 10:32 · #B138992

i get an overloaded error when i run this code and solder the items that i placed in the bottom bit of the code dont move

**Code:**

```
{

#mwin("Drunkie: Sit have one last drink.")

#mwin(" 1 = No  2 = Yes ")

#idone! = 0

#while(idone! == 0)

{

   #wait(q$)

   #if(q$=="1")

   {

   #mwincls()

   #mwin("Billar: No I'm good but thanks.")

   #wait()

   #mwincls()

   #idone!==1

   #end()

   }

#if(q$=="2")

{

#mwincls()

#mwin("Billar: Yeah one last drink.")

#wait()

#mwincls()

#PushItem(4,"n")

#EraseItem(4)

#Push("enn","Billar")

#send("bar1.brd", 10, 11, 1)

#ItemStep(5, 11, 4)

#Push("nnnnnen","Billar")

#mwin("Drunkie: So what are you leaving for?")

#wait()

#mwin("Billar: I'm going to join the Army.")

#wait()

#mwin("Drunkie: O.K. well you better head off.")

#wait()

#mwincls()

#mwin("Billar: Yeah I really should.")

#mwin("Don't get into any troble while I'm gone!")

#wait()

#mwin("Drunkie: Dont worrie I'll be fine.")

#wait()

#mwincls()

   #PutItem(5, 9, 11, 1)*must change coardanants for first solder

#wait()

#mwin("Billar: ???")

#mwin("Those arnt our solders ???")

#wait()

   #pushitem(5, "nn")*change coardanents here to for patron that gets killed

   #DestroyItem(1)*change value to the right slot

#mwin("Billar: Drunkie lets get him!")

#wait()

#mwincls()

#mwin("Drunkie: Lets go!")

#addplayer("drunkie.tem")

#wait()

   #pushitem(5,"nn")*solder steps foward two steps

   #wait()

   #putitem(6, 10, 11, 1)*second solder comes in

   #wait()

   #pushitem(6, "nnnn")*secondsolder steps up beside first one

   #wait()

   #fightsolders!==1

   #DestroyItem(5)

   #DestroyItem(6)

   #FightEnemy("Blachern warrior1.ene", "Blachern warrior1.ene", "back.bkg")

}
```

please help

### Dont_Think_So · 2004-12-13 23:22 · #B139162

The handle goes first in the Push command. Also, you don't need that extra { at the top...

### Unelemented · 2004-12-14 00:38 · #B139210

the first 3 push commands work like that
its from the second tabed command down that it comes up
the exact error message is
code: 6
Description: Overflow
