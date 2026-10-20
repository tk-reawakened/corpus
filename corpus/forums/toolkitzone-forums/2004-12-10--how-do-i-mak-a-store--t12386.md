---
kind: forum-thread
id: "toolkitzone-forums/12386"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "toolkit 2.x support"
skin: "phpbb2"
thread_id: "12386"
title: "how do i mak a store"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12386"
written: "2004-12-10T01:00:00"
last_post: "2005-01-17T09:48:00"
date_confidence: "exact"
captured: ["20050117155145"]
author: "game62690"
repliers: ["Levi", "jo_potato", "zyrshnikashnu", "tc", "Dont_Think_So"]
authors: ["game62690", "Levi", "jo_potato", "zyrshnikashnu", "tc", "Dont_Think_So"]
posts_present: 10
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_137652_amp_", captured: "20050117155145", sha256: "92fbd56df881318a3c59cc984bd39afdd6e7fa57944e9d26e514abd62057f451", wayback_url: "https://web.archive.org/web/20050117155145/http://www.toolkitzone.com/forums/viewtopic.php?p=137652&amp="}
links: []
---

# how do i mak a store

### game62690 · 2004-12-10 01:00 · #B137203

plz somebody help me im new just started making my game and i need to know how to mak a store

### Levi · 2004-12-10 01:36 · #B137238

You could use the built in shop command. Or are you looking for a more customizable version of a store?

### game62690 · 2004-12-10 02:35 · #B137297

i dont even know how to build a building let alone a store

### jo_potato · 2004-12-10 05:29 · #B137455

ugh. first, don't be a guest. it's really annoying knowing that toolkit users come in as guests.
but anyways:
Make an Easy Shop
1. make a shop after you BUILD TILES. using TILES, build a SHOP with the BOARD EDITOR. SOLIDIZE the SHOP and create a WARP TILE leading into it.
2. Make the inside of your SHOP using more TILES. make it look nice, then create an ITEM representing the SHOPKEEPER. this will need more TILES. now for the programming
i'm not a very good programming but its something like this:
#mwin("Hi! Welcome to the [yourshophere]")
#mwin("What would you like to buy?")
*list the items you need, and the costs. here are some suggestions...
#mwin("-1- Beer: 50 GP")
#mwin("-2- Potion: 50 GP")
#mwin("-3- [You get the idea.]")
#wait(key$) *waits for user keypress
*make a#if. i'll leave this to some other user to tell you how to do.

### zyrshnikashnu · 2004-12-10 21:04 · #B137652

'Tis true. It's all in the help files. Remember, always look in the help files before you ask a question here. Smile
Oh, and the default shop is called with the command "#CallShop." Look it up in the command reference. In fact, since I'm feeling generous, I'll do it for you:

**RPGCode Command Reference wrote:**

> #CallShop
> Name: Open shop window.
> Format: #CallShop(item1.itm, item2.itm, )
> This command opens a shop window where the player can buy and sell items. The arguments passed are literal values, ecah one is the filename of an item that the shopkeeper sells. The buying and selling prices of items are determined by the values set in the Item Editor.
> Example:
> #CallShop(sword.itm, shield.itm, grenade.itm)
> * Opens a shop window selling 3 items
> Related Commands:
> #GP

### tc · 2005-01-13 14:53 · #B155188

and what if the callshop program doesn't work Question Question

### zyrshnikashnu · 2005-01-13 23:59 · #B155353

CallShop isn't a program, it's a command. Just make and save the correct items, put the CallShop command in a program with the correct syntax (and save it), and then run. If you're still getting problems, put your code up here and we'll take a look.

### tc · 2005-01-14 07:20 · #B155527

**Code:**

```
#mwin("Shopkeeper: Hello there karel! i sells shit!")

#wait()

#callshop("cheese.itm","chicken.itm","wine.itm")
```

this is the program i use

### Dont_Think_So · 2005-01-14 23:44 · #B155694

Does it work when you test a program?

### tc · 2005-01-17 09:48 · #B156749

than he won't work, but i have made i new shop program.

**Code:**

```
//=======================================

//main menu

//=======================================

{

Mwin("do you want to buy, sell or leave?")

#mwin("1 - buy, 2 - sell, 3 - leave")

#wait(choice!)

}

//========================================

//buy stuff

//========================================

}

#if(choice!==1)

{

#Mwin("wat do you want to buy:")

#mwin("4 - shild for 10gp, 5- sword for 10gp, 6 - wizzard's shild for 9gp,3 - leave")

#wait(choise!)

}

//=======================================

// buy shild

//=======================================

}

#if(choise!==4)

{

#GiveItem(shild.itm)

#TakeGP(10)

#Mwin("You got a shild!")

#wait(a$)

}

//======================================

// buy sword

//======================================

}

#if(choise!==5)

{

#GiveItem(sword.itm)

#takeGp(10)

#mwin("you got a sword")

#wait(a$)

}

//=====================================

//buy wizard's shild

//=====================================

}

#if(choise!==6)

{

#GiveItem(wizardsshild.itm)

#takeGp(15)

#Mwin("you got a shild")

#wait(a$)

}

//=====================================

//sell

//=====================================

}

#if(choice!==2)

{

#Mwin("what do you want do sell?")

#Mwin("7 - shild for 5gp, 8 - wine for 5GP, 9- wizard's shild for 7gp, 3 - leave")

#wait(choise!)

}

//===================================

//sell shild

//===================================

}

#if(choise!==7)

{

#TakeItem(shild.itm)

#GiveGp(5)

#Mwin("you sold a shild")

#wait(a$)

}

//===================================

//sell sword

//===================================

}

#if(choise!==8)

{

#TakeItem(sword.itm)

#GiveGp(5)

#Mwin("you sold a sword")

#wait(a$)

}

//===================================

//sell wizard's shild

//===================================

}

#if(choise!==9)

{

#TakeItem(wizardsshild.itm)

#GiveGp(7)

#Mwin("you sold a shild")

#wait(a$)

}

//=================================

// end

//=================================

}

#if(choise!==3)

{

#Mwin("come back wen you changed your mind")

#wait(a$)

#end()

}
```
