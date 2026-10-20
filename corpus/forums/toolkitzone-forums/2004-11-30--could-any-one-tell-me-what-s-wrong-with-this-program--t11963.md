---
kind: forum-thread
id: "toolkitzone-forums/11963"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "toolkit 2.x support"
skin: "phpbb2"
thread_id: "11963"
title: "Could any one tell me what's wrong with this program?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11963"
written: "2004-11-30T22:43:00"
last_post: "2004-12-21T20:47:00"
date_confidence: "exact"
captured: ["20050114191645"]
author: "n/a"
repliers: ["Unelemented", "psx dude", "Dont_Think_So"]
authors: ["n/a", "Unelemented", "psx dude", "Dont_Think_So"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_134311_amp_", captured: "20050114191645", sha256: "19ea0462db29dc407e2f712e7cc75b5749839faabdc2f49b86a5a753cd723d35", wayback_url: "https://web.archive.org/web/20050114191645/http://www.toolkitzone.com/forums/viewtopic.php?p=134311&amp="}
links: []
---

# Could any one tell me what's wrong with this program?

### n/a · 2004-11-30 22:43 · #B132258

I'm trying to make a Magic item store, yet I am troubled by this program.
Shop window
Shitaka Magic store
#mwin("Owner:TEE-HEE A custumer, Hi welecome to Shitaka magic store!")
#wait(a$)
#MWinCls
:top
#Prompt(" 1 Items, 2 codes, 3 Lets chat, 4 nevermind "$)
#wait
#If($=="1")
{
!)
#callshop("Potion1.itm","Mage's blood1.itm")
#Wait(a$
#MWinCls
{
#If($=="2")
#MWin("Aww, sorry! We're sold out! Try Vixston town, they should have some!")
#Wait(a$
#MWinCls
}
#If($=="3")
{
#MWin("#Mwin("Owner: Wow, your on a adventure?! Shoot! I sure wish I could join you")
#system.pause()
#Mwin("Owner: But I have to help my grandma's magic store running!"
#system.pause()
#Mwin("Inari: Umm, how do you know I on a adventure?")")
#Wait(a$)
#MWinCls
}
#Done!=1
}
#If($=="4")
{
#MWin ("Okay, Bye Bye then, PLEASE come again! ^_^")
#Wait(a$)
#MWinCls
#Done!=1
#end()
}
I'm a novice and this is my frist RPG. Would anyone mind replying, I would be very greatful. ^_^v

### Unelemented · 2004-11-30 23:22 · #B132333

first off
#prompt should look like

**Code:**

```
#Prompt(" 1 Items, 2 codes, 3 Lets chat, 4 nevermind ", a!)*you didnt put in a veriable :shock:
```

the first wait needsto be #wait()
your #if statements should be

**Code:**

```
{

#If(a!=="1") *no veriable #if doesnt work :shock:

{

#callshop("Potion1.itm","Mage's blood1.itm")

#Wait()

#MWinCls

}

{
```

if im wrong someone else correct me but i think that should work Very Happy

### psx dude · 2004-12-03 05:20 · #B134035

Im a novice rpg coder myself but ill give it a shot to fix ur code.
it may not display the ^_^ but i dont know.
Shop window
Shitaka Magic store
#mwin("Owner:TEE-HEE A custumer, Hi welecome to Shitaka magic store!")
#wait(a$)
@
#delay(1)
#mwin("1 - Items")
#mwin("2 - Codes")
#mwin("3 - Let's chat")
#mwin("4 - Nevermind")
#wait(choice!)
#mwincls()
#If(choice!==1)
{
#callshop("Potion1.itm","Mage's blood1.itm")
#wait(a$)
#mwincls()
}
#If(choice!==2)
{
#MWin("Aww, sorry! We're sold out! Try Vixston town, they should have some!")
#Wait(a$)
#MWinCls()
}
#If(choice!==3)
{
#MWin("#Mwin("Owner: Wow, your on a adventure?! Shoot! I sure wish I could join you")
#delay(1)
#Mwin("Owner: But I have to help my grandma's magic store running!")
#delay(1)
#Mwin("Inari: Umm, how do you know I on a adventure?")
#Wait(a$)
#MWinCls()
}
#If(choice!==4)
{
#MWin ("Okay, Bye Bye then, PLEASE come again! ^_^")
#Wait(a$)
#MWinCls
}
#end()

### psx dude · 2004-12-03 05:27 · #B134038

**psx dude wrote:**

> Shop window
> Shitaka Magic store
> #mwin("Owner:TEE-HEE A custumer, Hi welecome to Shitaka magic store!")
> ~#wait(a$)~
> @
> #delay(1)
> #mwin("1 - Items")
> #mwin("2 - Codes")
> #mwin("3 - Let's chat")
> #mwin("4 - Nevermind")
> #wait(choice!)
> #mwincls()
>

i ran this code and i found something wrong. ill use ~'s to point out wat to not put in the code. take the #wait(a$) out or the prg will have to wait for the user to hit a key then it will do the delay of one second.

### Dont_Think_So · 2004-12-03 06:18 · #B134047

*Ding ding* Order up!
One steaming hot program, fresh out of the oven.

**Code:**

```
#mwin("Owner:TEE-HEE A custumer, Hi welecome to Shitaka magic store!")

#MWinCls

#MWin(" 1 Items, 2 codes, 3 Lets chat, 4 nevermind ")

#Done!=0

#While(Done!==0) * This way we keep going until the user presses 1,2,3 or 4

{

#wait(Input$)

#If(Input$=="1")

{

#callshop("Potion1.itm","Mage's blood1.itm")

#Wait(a$)

#MWinCls

#Done!=1 *We're done here!

}

#If(Input$=="2")

{

#MWin("Aww, sorry! We're sold out! Try Vixston town, they should have some!")

#Wait(a$)

#MWinCls

#Done!=1 *We're done here!

}

#If(Input$=="3")

{

#MWin("#Mwin("Owner: Wow, your on a adventure?! Shoot! I sure wish I could join you")

#system.pause()

#Mwin("Owner: But I have to help my grandma's magic store running!")

#system.pause()

#Mwin("Inari: Umm, how do you know I on a adventure?")

#Wait(a$)

#MWinCls

#Done!=1 *We're done here!

}

#If(Input$=="4")

{

#MWin ("Okay, Bye Bye then, PLEASE come again! ^_^")

#Wait(a$)

#MWinCls

#Done!=1 *We're done here!

}

}
```

### n/a · 2004-12-03 23:09 · #B134300

I'm sorry, but the program given seems to not work. Is it just my computer? And all the stuff you guy's posted were correct?
When I tested it, I recieved a rectangular white box on my screen that I could not escape from. Inwhich, I had to shut down my whole computer.
6_6

### Dont_Think_So · 2004-12-03 23:26 · #B134311

If that white, rectangular box is at the top of teh screen, then your mwin doesn't have a graphic. Make sure mwin.jpg is in your Bitmap folder, or make your own MWin.

### n/a · 2004-12-21 20:47 · #B143700

...Oh yeah, Thanks ^o^*
I found a way without the problems. ^_^
