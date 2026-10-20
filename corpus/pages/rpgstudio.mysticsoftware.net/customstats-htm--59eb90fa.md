---
kind: page
id: "rpgstudio.mysticsoftware.net/rpgstudio.mysticsoftware.net/customstats.htm"
site: "rpgstudio.mysticsoftware.net"
title: "Custom Stats"
original_url: "http://www.rpgstudio.mysticsoftware.net/customstats.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20050111132434", "20050111132434"]
author: "William"
repliers: []
authors: ["William"]
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/rpgstudio.mysticsoftware.net/customstats.htm", captured: "20050111132434", sha256: "6cfb2d0c1cebbfef85f5cad5978c4297ca8cabf480b49cc0b15635b0faa928d4", wayback_url: "https://web.archive.org/web/20050111132434/http://www.rpgstudio.mysticsoftware.net/customstats.htm"}
  - {path: "wayback/mysticsoftware.net/www.rpgstudio.mysticsoftware.net/customstats.htm", captured: "20050111132434", sha256: "6cfb2d0c1cebbfef85f5cad5978c4297ca8cabf480b49cc0b15635b0faa928d4", wayback_url: "https://web.archive.org/web/20050111132434/http://www.rpgstudio.mysticsoftware.net/customstats.htm"}
---

# Custom Stats

By William
(redacted: email)
I suggest you read my other tutorial about if commands on this site.
Something that is very popular is custom menu, battle and also stats. Stats is a very important thing in RPG games. So I will help you to start, with your own stats. So lets begin:
Step 1, What stat shall I use?:
There are a lot of different stat that you can come up with, and I will give you some examples for stats.
- Strength
- Defense
- Health
- Magic
- Wisdom
- Luck
Strength - This is the same as Fight Power (fp). And it works exactly the same.
Defense - This is the defense power. Need this to protect the character form enemies.
Health - You have health and you have max health. This is the hp level.
Magic - You need Magic (smp) to attack enemies with special moves.
New:
Wisdom - You need Wisdom to read books and other scrolls.
Luck - Much point on luck help you to find special items and gold.
That is some stats that I like, but you can create many more if you like to. So now we have the stats, so lets move on.
Step 2, Stat command:
This could be the difficult part for newbies. We will create the stats, but its not that hard.
First off all, we do this:
Create a character in the Edit Character window. But you cant create the luck and wisdom
so put this in the start.prg:
#Wisdom!=2 *The character start with 2 wisdom.
#Luck!=3 *The character start with 3 luck.
Now we have our custom stats in variables. So now we can use them in our game, nice!
But how do we use them?
Step 3, How to use them:
So how do we use wisdom? Do this:
#if (wisdom!>2)
#Mwin(You have to go to the cave to find the book!)
#Wait()
#MwinCls()
#if! (wisdom!<3)
#Mwin(Cposfrn spjoc sjsaofo!)
#wait()
#MwinCls()
You think this is crap, but it isnt. You start with two wisdom. And you need 3 or more to see the foreign man speak. If you have less then 3 then you cant understand his language. Thats a good way to use the stat wisdom. You can also use this to a book. So you need more then five to understand the text in the book. I will give you a example that is a bit better:
#if (wisdom!>4)
#Mwin(The secret password is Man from Marovia-)
#Wait()
#MwinCls()
#if (wisdom!<2)
#Mwin(Tde sefget padwwogd as Min fadm Maoidvi-)
#Wait()
#MwinCls()
#if (wisdom!<3)
#Mwin(The secget paswwogd as Min faom Maridva-)
#Wait()
#MwinCls()
So now you know how to use wisdom, and you use luck the same way. But you put the program on the board so when you step on it, then it runs. And then if you have more then 2 luck, then you gain 20 GP. You can do as you like to. Pretty good.
Step 4, finish:
This was just a small tutorial about custom stats, and I will make some update later. Thanks for reading this. MSN and Email: .(redacted: email)
