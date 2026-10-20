---
kind: page
id: "rpgstudio.mysticsoftware.net/rpgstudio.mysticsoftware.net/ifcommands.htm"
site: "rpgstudio.mysticsoftware.net"
title: "If Commands"
original_url: "http://www.rpgstudio.mysticsoftware.net/ifcommands.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20050115125821", "20050115125821"]
author: "William"
repliers: []
authors: ["William"]
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/rpgstudio.mysticsoftware.net/ifcommands.htm", captured: "20050115125821", sha256: "0cc023fa293e41cfd546c73c1f281b76f3321022af9e06d0a7cccdafc92260e1", wayback_url: "https://web.archive.org/web/20050115125821/http://www.rpgstudio.mysticsoftware.net/ifcommands.htm"}
  - {path: "wayback/mysticsoftware.net/www.rpgstudio.mysticsoftware.net/ifcommands.htm", captured: "20050115125821", sha256: "0cc023fa293e41cfd546c73c1f281b76f3321022af9e06d0a7cccdafc92260e1", wayback_url: "https://web.archive.org/web/20050115125821/http://www.rpgstudio.mysticsoftware.net/ifcommands.htm"}
---

# If Commands

By William
Bjorn_djdj@hotmail.com
There is a lot of different if commands. That you can change, and create as you like to. The most popular is #if (sword!=1). Not the sword, but that kind of If command. There are also some commands like this:
#if (sword!=1)
*The program to run if you found a sword.
#GetGP(gold!)
#if (gold! > 10)
*The program to run if you have more then 10 GP.
As you see, you can do this on many different ways. But I will explain more about this later.
Step 1, how to open a chest:
All RPG games shall have secret chest or chest and boxes in castle or in houses. And there is different ways to do this. The default idea to do this is to. Right click on the board, RPG Code program, then you press Edit. Then brows the program, so you can find a sword. That program can be like this:
#GiveItem(sword.itm)
Now, its funny to have a chest that you can open. So put a opened chest on the screen. And after that, press on Advanced in the same window as you was in before. And then press on Brows on the Display Program As. And then put the closed chest there. And you shall now press on Conditional Activation. If you do that, then you can just open your chest once, and thats good. That was one way to do this. But I suggest you use one of these. They are much better, and funnier.
Write, or copy this command:
#if (sword!=1)
#Mwin(This chest is empty.)
#wait()
#MwinCls()
#if (sword!=0)
#Mwin(You found a sword.)
#wait()
#MwinCls()
#GiveItem(sword.itm)
#sword!=1
This is a good way to create a chest program. And the program isnt hard to understand. The #if (sword!=1) checks if the character found a sword. Not a item, it check after this command: #sword!=1. And if it cant find that command, then it skip it. But if it see a program like this: #if (sword!=0), then it run it because 0 is the same as, not found. You can also create a funnier program, like this:
#if (sword!=1)
#random(2,result!)
#if(result!=1)
#Mwin(This chest is empty.)
#wait()
#MwinCls()
#if(result!=2)
#Mwin(So bad luck, it was empty.)
#wait()
#MwinCls()
#if (sword!=0)
#Mwin(You found a sword.)
#wait()
#MwinCls()
#GiveItem(sword.itm)
#sword!=1
That is a way to make the game more realistic. So that the text is different.
You can also do it this way:
#Mwin(You found a sword.)
#Wait()
#MwinCls()
#GiveItem(sword.itm)
#change(empty.prg)
And the empty.prg shall have this information:
#Mwin(This is empty.)
#Wait()
#MwinCls()
You can also use the #Random command here.
Step 2, more or less then a number!:
Maybe you want to find three keys to open a door. Then its hard to use #if commands and a lot easier with < and >. So lets start.
#If (key!>2) *checks if the character have more then 2 keys (not 2).
#Mwin(You found all the three keys, you can enter!)
#Wait()
#MwinCls()
#If (key!<3) *checks if the character have less then 2 keys.
#Mwin(You need to find all keys!)
#Wait()
#MwinCls()
Thats a good way to do it. And you can use them to many other things to, you can check if you have enough GP or HP. Like this:
#GetGP(gp!)
#If (gp!>99) *checks if the character have more then 100 GP.
#Mwin(You have enough GP.)
#Wait()
#MwinCls()
#If (gp!<100) *checks if the character have less 100 GP.
#Mwin(You need more gold.)
#Wait()
#MwinCls()
That wasnt that hard to understand. You can do a lot with this kind of #if commands. And you can also make your own. This is just a simple example:
#profile$=profile.bmp
#SetImage(profile$, 10, 10, 100, 75)
#potions!=0
#Mwin(You have .)
#Wait()
#MwinCls()
#potions!=potions!+1
#Mwin(You have .)
#Wait()
#MwinCls()
#potions!=potions!+1
#Mwin(You have .)
#Wait()
#MwinCls()
You have two potions after this program. And you can change this as you like to. This was just a very simple beginning for all the newbies and for they who want to learn some basic skills with #if.
Thanks for reading this tutorial. MSN and Email:Bjorn_djdj@hotmail.com
