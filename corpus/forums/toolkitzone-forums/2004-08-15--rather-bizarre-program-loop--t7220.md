---
kind: forum-thread
id: "toolkitzone-forums/7220"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "7220"
title: "Rather bizarre program loop"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7220"
written: "2004-08-15T20:25:00"
last_post: "2004-08-15T21:44:00"
date_confidence: "exact"
captured: ["20040925162009"]
author: "khaldore"
repliers: ["Colosseus"]
authors: ["khaldore", "Colosseus"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_76126_amp_", captured: "20040925162009", sha256: "135aa73cd5f5206a23ed17361c9b45765fcbaa5de03c0e33c1eb444350db16bf", wayback_url: "https://web.archive.org/web/20040925162009/http://www.toolkitzone.com/forums/viewtopic.php?p=76126&amp="}
links:
  - {url: "http://www.toolkitzone.com/stuff/files/2400/donkey.png", status: "never-captured", local: null}
---

# Rather bizarre program loop

### khaldore · 2004-08-15 20:25 · #B76062

Well, here I am with yet another program that's being difficult... let me post the program in here, since I've commented in it where the trouble is:

**Code:**

```
#AutoCommand

intro!=0

PutPlayer("Khaldore", 11, 16, 1)

PutPlayer("Reslin", 10, 17, 1)

Stance(10, "Reslin")

PutPlayer("Eryn", 11, 17, 1)

Stance(10, "Eryn")

PutPlayer("Lylia", 12, 17, 1)

Stance(10, "Lylia")

MWin("Eryn:  Khaldore, do you know why we were summoned here?")

@

Wait(a$)

MWin("Khaldore:  No idea... but we oughta talk to the Elder.")

Wait(a$)

MWinCls

ErasePlayer("Reslin")

ErasePlayer("Eryn")

ErasePlayer("Lylia")

Push("N", "Khaldore")

Delay(0.2)

Push("N", "Khaldore")

Delay(0.2)

Push("N", "Khaldore")

Delay(0.2)

Push("N", "Khaldore")

Delay(0.2)

Push("N", "Khaldore")

Delay(0.2)

Push("N", "Khaldore")

Delay(0.2)

Push("N", "Khaldore")

Delay(0.2)

Push("N", "Khaldore")

Delay(0.2)

Push("N", "Khaldore")

Delay(0.2)

Push("N", "Khaldore")

PutPlayer("Reslin", 10, 7, 1)

Stance(10, "Reslin")

PutPlayer("Eryn", 11, 7, 1)

Stance(10, "Eryn")

PutPlayer("Lylia", 12, 7, 1)

Stance(10, "Lylia")

***As you'll read later, the program loops back here for some reason...***

MWin("Elder:  Ah, I'm glad to see the four of you. I'm sure you're wondering")

MWin("         why you've been called here.")

Wait(a$)

MwinCls

MWin("Lylia:  You could say that... so why are we here?")

Wait(a$)

MWinCls

PushItem(1, "W")

PushItem(1, "W")

MWin("Elder:  Have any of you heard of the Vortex?")

@

Wait(a$)

MWin("Reslin:  Only in legends... it's rumored to take souls to their final")

MWin("          resting place, correct?")

Wait(a$)

MWinCls

PushItem(1, "E")

PushItem(1, "E")

MWin("Elder:  Yes and no... we, the Jexaru, thought much the same thing for")

MWin("         centuries. As it turns out, we were very, very wrong.")

@

Wait(a$)

MWin("Khaldore:  How so?")

Wait(a$)

MwinCls

MWin("Elder:  There is a Vortex that takes souls... but only to feed its hunger.")

MWin("         After eons, though, it seems souls aren't enough to satisfy it.")

MWin("         Twenty years ago, it began appearing on the surface, destroying")

MWin("         everything and everyone in its path.")

Wait(a$)

MwinCls

MWin("Eryn:  So what does this have to do with us?")

@

Wait(a$)

MWin("Lylia:  Yeah... that doesn't explain why you brought us here.")

Wait(a$)

MWinCls

MWin("Elder:  Most of the people that encounter the Vortex are either devoured,")

MWin("         or turned into mindless beasts and creatures from fantasy stories.")

Mwin("         We spent decades searching for a group immune to the effects of the")

MWin("         Vortex, and you four are all who we found.")

Wait(a$)

MWinCls

Mwin("Khaldore:  Meaning what?")

@

Wait(a$)

MWin("Elder:  You four are Kyron's only hope, but be warned... one of you will not")

MWin("         survive the journey ahead, though I can't tell you why.")

Wait(a$)

MwinCls

MWin("Reslin:  You can't, or you won't?")

@

Wait(a$)

MWin("Elder:  Sadly, I indeed meant can't... for I truly don't know. Please,")

MWin("         forgive me, but only the four of you together can help Kyron")

MWin("         now. Take this equipment and money... it is all I can do to help.")

@

StartEquip()

Wait(a$)

MWin("---You received basic equipment and 100gp.---")

Wait(a$)

MWinCls

MWin("Elder:  There is a castle town just north of here called Hargon... you may")

MWin("         be able to find more information and supplies there. Good luck, and")

Mwin("         please be careful, for all our sakes.")

Wait(a$)

MWinCls

ErasePlayer("Reslin")

ErasePlayer("Eryn")

ErasePlayer("Lylia")

Push("S", "Khaldore")

Delay(0.2)

Push("S", "Khaldore")

Delay(0.2)

Push("S", "Khaldore")

Delay(0.2)

Push("S", "Khaldore")

Delay(0.2)

Push("S", "Khaldore")

Delay(0.2)

Push("S", "Khaldore")

Delay(0.2)

Push("S", "Khaldore")

Delay(0.2)

Push("S", "Khaldore")

Delay(0.2)

Push("S", "Khaldore")

Delay(0.2)

Push("S", "Khaldore")

PutPlayer("Reslin", 10, 17, 1)

Stance(10, "Reslin")

PutPlayer("Eryn", 11, 17, 1)

Stance(10, "Eryn")

PutPlayer("Lylia", 12, 17, 1)

Stance(10, "Lylia")

MWin("Eryn:  So I guess we have to save the world, huh?")

@

Wait(a$)

MWin("Khaldore:  Looks that way... we'd better get going.")

Wait(a$)

MwinCls

ErasePlayer("Reslin")

ErasePlayer("Eryn")

ErasePlayer("Lylia")

intro!=1

***This is where the program loops back to my first comment...***

***Any ideas why?  I've tried both #End and #Done here, but***

***nothing seems to be working...***

Done

Method StartEquip()

{

   GiveItem("clothing.itm")

   GiveItem("woodsword.itm")

   GiveItem("clothing.itm")

   GiveItem("shortstaff.itm")

   GiveItem("clothing.itm")

   GiveItem("woodmace.itm")

   GiveItem("clothing.itm")

   GiveItem("dagger.itm")

   Equip("Khaldore", 5, "clothing.itm")

   Equip("Khaldore", 4, "woodsword.itm")

   Equip("Reslin", 5, "clothing.itm")

   Equip("Reslin", 4, "shortstaff.itm")

   Equip("Eryn", 5, "clothing.itm")

   Equip("Eryn", 4, "woodmace.itm")

   Equip("Lylia", 5, "clothing.itm")

   Equip("Lylia", 4, "dagger.itm")

   GiveGP(100)

}
```

As you can read by the comment lines, the program loops back nearly to the beginning. However, it doesn't loop the #Push commands, nor the other grapnic bits, only the #MWin calls. It oughta run only once at the start of a new game, then give control over to the player after that, but... anyhow, if you can help me figure this out, I'd be grateful, as always. Very Happy
Khal
PS - I know the way I use #Push there is kinda drawn out... but if I didn't #Delay it, he'd zip up the screen like a roadrunner on speed. Odd, though, is that the actual walking speed of my characters is just fine... Also, that wordwrap on some lines is due to the window size here. Razz
_________________
Current Project: Ageless (Demo 1.0)
Completion: 45%
Custom Menu: 50%
Characters: 75%
My game may not be that good, but I'm proud of it.
![](http://www.toolkitzone.com/stuff/files/2400/donkey.png)

### Colosseus · 2004-08-15 20:54 · #B76084

Try this:
#AutoCommand
intro!=0
while (intro! == 0)
{
PutPlayer("Khaldore", 11, 16, 1)
PutPlayer("Reslin", 10, 17, 1)
Stance(10, "Reslin")
PutPlayer("Eryn", 11, 17, 1)
Stance(10, "Eryn")
PutPlayer("Lylia", 12, 17, 1)
Stance(10, "Lylia")
MWin("Eryn: Khaldore, do you know why we were summoned here?")
@
Wait(a$)
MWin("Khaldore: No idea... but we oughta talk to the Elder.")
Wait(a$)
MWinCls
ErasePlayer("Reslin")
ErasePlayer("Eryn")
ErasePlayer("Lylia")
Push("N", "Khaldore")
Delay(0.2)
Push("N", "Khaldore")
Delay(0.2)
Push("N", "Khaldore")
Delay(0.2)
Push("N", "Khaldore")
Delay(0.2)
Push("N", "Khaldore")
Delay(0.2)
Push("N", "Khaldore")
Delay(0.2)
Push("N", "Khaldore")
Delay(0.2)
Push("N", "Khaldore")
Delay(0.2)
Push("N", "Khaldore")
Delay(0.2)
Push("N", "Khaldore")
PutPlayer("Reslin", 10, 7, 1)
Stance(10, "Reslin")
PutPlayer("Eryn", 11, 7, 1)
Stance(10, "Eryn")
PutPlayer("Lylia", 12, 7, 1)
Stance(10, "Lylia")
MWin("Elder: Ah, I'm glad to see the four of you. I'm sure you're wondering")
MWin(" why you've been called here.")
Wait(a$)
MwinCls
MWin("Lylia: You could say that... so why are we here?")
Wait(a$)
MWinCls
PushItem(1, "W")
PushItem(1, "W")
MWin("Elder: Have any of you heard of the Vortex?")
@
Wait(a$)
MWin("Reslin: Only in legends... it's rumored to take souls to their final")
MWin(" resting place, correct?")
Wait(a$)
MWinCls
PushItem(1, "E")
PushItem(1, "E")
MWin("Elder: Yes and no... we, the Jexaru, thought much the same thing for")
MWin(" centuries. As it turns out, we were very, very wrong.")
@
Wait(a$)
MWin("Khaldore: How so?")
Wait(a$)
MwinCls
MWin("Elder: There is a Vortex that takes souls... but only to feed its hunger.")
MWin(" After eons, though, it seems souls aren't enough to satisfy it.")
MWin(" Twenty years ago, it began appearing on the surface, destroying")
MWin(" everything and everyone in its path.")
Wait(a$)
MwinCls
MWin("Eryn: So what does this have to do with us?")
@
Wait(a$)
MWin("Lylia: Yeah... that doesn't explain why you brought us here.")
Wait(a$)
MWinCls
MWin("Elder: Most of the people that encounter the Vortex are either devoured,")
MWin(" or turned into mindless beasts and creatures from fantasy stories.")
Mwin(" We spent decades searching for a group immune to the effects of the")
MWin(" Vortex, and you four are all who we found.")
Wait(a$)
MWinCls
Mwin("Khaldore: Meaning what?")
@
Wait(a$)
MWin("Elder: You four are Kyron's only hope, but be warned... one of you will not")
MWin(" survive the journey ahead, though I can't tell you why.")
Wait(a$)
MwinCls
MWin("Reslin: You can't, or you won't?")
@
Wait(a$)
MWin("Elder: Sadly, I indeed meant can't... for I truly don't know. Please,")
MWin(" forgive me, but only the four of you together can help Kyron")
MWin(" now. Take this equipment and money... it is all I can do to help.")
@
StartEquip()
Wait(a$)
MWin("---You received basic equipment and 100gp.---")
Wait(a$)
MWinCls
MWin("Elder: There is a castle town just north of here called Hargon... you may")
MWin(" be able to find more information and supplies there. Good luck, and")
Mwin(" please be careful, for all our sakes.")
Wait(a$)
MWinCls
ErasePlayer("Reslin")
ErasePlayer("Eryn")
ErasePlayer("Lylia")
Push("S", "Khaldore")
Delay(0.2)
Push("S", "Khaldore")
Delay(0.2)
Push("S", "Khaldore")
Delay(0.2)
Push("S", "Khaldore")
Delay(0.2)
Push("S", "Khaldore")
Delay(0.2)
Push("S", "Khaldore")
Delay(0.2)
Push("S", "Khaldore")
Delay(0.2)
Push("S", "Khaldore")
Delay(0.2)
Push("S", "Khaldore")
Delay(0.2)
Push("S", "Khaldore")
PutPlayer("Reslin", 10, 17, 1)
Stance(10, "Reslin")
PutPlayer("Eryn", 11, 17, 1)
Stance(10, "Eryn")
PutPlayer("Lylia", 12, 17, 1)
Stance(10, "Lylia")
MWin("Eryn: So I guess we have to save the world, huh?")
@
Wait(a$)
MWin("Khaldore: Looks that way... we'd better get going.")
Wait(a$)
MwinCls
ErasePlayer("Reslin")
ErasePlayer("Eryn")
ErasePlayer("Lylia")
intro!=1
}
Done
Method StartEquip()
{
GiveItem("clothing.itm")
GiveItem("woodsword.itm")
GiveItem("clothing.itm")
GiveItem("shortstaff.itm")
GiveItem("clothing.itm")
GiveItem("woodmace.itm")
GiveItem("clothing.itm")
GiveItem("dagger.itm")
Equip("Khaldore", 5, "clothing.itm")
Equip("Khaldore", 4, "woodsword.itm")
Equip("Reslin", 5, "clothing.itm")
Equip("Reslin", 4, "shortstaff.itm")
Equip("Eryn", 5, "clothing.itm")
Equip("Eryn", 4, "woodmace.itm")
Equip("Lylia", 5, "clothing.itm")
Equip("Lylia", 4, "dagger.itm")
GiveGP(100)
}

### khaldore · 2004-08-15 21:15 · #B76102

Cram the whole works into a #While loop, eh.... never thought about that, I'll have to give it a shot. Thanks Smile
_________________
Current Project: Ageless (Demo 1.0)
Completion: 45%
Custom Menu: 50%
Characters: 75%
My game may not be that good, but I'm proud of it.
![](http://www.toolkitzone.com/stuff/files/2400/donkey.png)

### Colosseus · 2004-08-15 21:25 · #B76112

Heh, np... Lemme know if it worked, then Smile

### khaldore · 2004-08-15 21:44 · #B76126

No such luck with #While... it's still doing the same as before. Confused I'm wondering if it's where I have the program located, maybe. I tacked it into the end of the History() method so it would run when it needed to... should I have placed it elsewhere?
_________________
Current Project: Ageless (Demo 1.0)
Completion: 45%
Custom Menu: 50%
Characters: 75%
My game may not be that good, but I'm proud of it.
![](http://www.toolkitzone.com/stuff/files/2400/donkey.png)
