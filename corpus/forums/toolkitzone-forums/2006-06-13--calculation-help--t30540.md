---
kind: forum-thread
id: "toolkitzone-forums/30540"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "RPG Code"
skin: "phpbb2"
thread_id: "30540"
title: "Calculation Help"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=30540"
written: "2006-06-13T22:22:00"
last_post: "2006-06-15T00:31:00"
date_confidence: "exact"
captured: ["20060627062802"]
author: "forensixman"
repliers: ["Colin", "Bad Kids", "Malegnis", "peace", "Levi", "UltimaWizard"]
authors: ["forensixman", "Colin", "Bad Kids", "Malegnis", "peace", "Levi", "UltimaWizard"]
posts_present: 15
pages_present: [1]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 2, start: 16, end: 30, url: "http://toolkitzone.com/forums/viewtopic.php?t=30540&start=15", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_327385_amp_3Bsid_a1a05948c06fffdb9634aaf9bfbd77e0", captured: "20060627062802", sha256: "73aebe4bced88fbeb0fed54ccf8da46d3bef48527a8a502e784263aecb7e81f5", wayback_url: "https://web.archive.org/web/20060627062802/http://toolkitzone.com/forums/viewtopic.php?p=327385&amp%3Bsid=a1a05948c06fffdb9634aaf9bfbd77e0"}
links:
  - {url: "http://img103.imageshack.us/img103/7675/experience4vw.png", status: "external", local: null}
  - {url: "http://img150.imageshack.us/img150/4062/simplified5bx.png", status: "external", local: null}
  - {url: "http://img91.imageshack.us/img91/8238/function4hn.png", status: "external", local: null}
---

# Calculation Help

### forensixman · 2006-06-13 22:22 · #B327320

Hrmmm - I have been frying my brain on trying to figure a formula for the following scenario:
The experience value of my player increases by 1.5 for each level up and starts at 20, so the experience needed at level 1 to level up is 20, whereas at level 2 it is 30. (20 * 1.5 = 30). I am trying to figure a way to calculate the total experience that the player has earned throughout the entirety of the game. The formula needs to be able to allow me to enter the level of the player so it can calculate. Could somebody help me figure this out?

### Colin · 2006-06-14 00:47 · #B327367

![](http://img103.imageshack.us/img103/7675/experience4vw.png)
where x is the level. So, in RPGCode,

**Code:**

```
experience! = 20 + 1.5^(level! - 1)
```

### Bad Kids · 2006-06-14 00:58 · #B327368

**Colin wrote:**

> ![](http://img103.imageshack.us/img103/7675/experience4vw.png)
> where x is the level.
>

whats with you, and using images for equations?

### Colin · 2006-06-14 00:59 · #B327369

The fancy TeX maths font is awesome.

### forensixman · 2006-06-14 02:22 · #B327383

Thanks Colin. You are pretty much god... Wink

### Malegnis · 2006-06-14 02:28 · #B327385

God of RPG toolkit forums maybe lmao
i think this formual (yes i am defying the great colin)
this is how the increases go....
21
21.5
22.25
23.375
25.0625
27.59
31.39
37.085
45.628
58.4433 <--level ten
so 38 exp to gain ten levels?
maybe i figured it wrong..
this is what i did, i! being the players level.

**Code:**

```
for(i!=1; i!<100; i!++)

{

   mwin(20+1.5^(i!-1)

   mwin(i!)

   wait()

   mwincls()

}

```

### peace · 2006-06-14 07:01 · #B327436

**Malegnis wrote:**

> God of RPG toolkit forums maybe lmao
> i think this formual (yes i am defying the great colin)
> this is how the increases go....
> 21
> 21.5
> 22.25
> 23.375
> 25.0625
> 27.59
> 31.39
> 37.085
> 45.628
> 58.4433 <--level ten
> so 38 exp to gain ten levels?
> maybe i figured it wrong..
> this is what i did, i! being the players level.
>
> **Code:**
>
> ```
> for(i!=1; i!<100; i!++)
>
>
> {
>
>
>    mwin(20+1.5^(i!-1)
>
>
>    mwin(i!)
>
>
>    wait()
>
>
>    mwincls()
>
>
> }
>
>
>
>
>
>
> ```
>

this code should work:

**Code:**

```
exp! = 20

for(i!=1; i!<100; i!++)

{

m! = (i! - 1) * 1.5

if (i! > 1)

{

exp! = exp! * m!

}

mwin(exp!)

wait()

mwincls()

}
```

### Malegnis · 2006-06-14 07:23 · #B327438

wow 279 mil for tenth level! thats worse than dnd, but yeah thanks for clearing that up for me.

### forensixman · 2006-06-14 14:32 · #B327486

Do I need to hold your hand in this? You guys aren't calculating correctly because it is not going to take 279 million experience points to level up! Look at this non-equation calculation:
20 To get to level 2
20 * 1.5 = 30 Level 3
30 * 1.5 = 45 Level 4
45 * 1.5 = 67.5 Level 5
67.5 * 1.5 = 101.3 Level 6
101.3 * 1.5 = 151.9 Level 7
151.9 * 1.5 = 227.9 Level 8
227.9 * 1.5 = 341.9 Level 9
341.9 * 1.5 = 512.9 Level 10 (not 10 million)
Anyways, there is your math lesson for the day!! Wink
@Malegnis - and Colin is god of everything so shut ur face!! ;D

### Malegnis · 2006-06-14 20:56 · #B327581

**peace wrote:**

> this code should work:
>
> **Code:**
>
> ```
> exp! = 20
>
>
> for(i!=1; i!<100; i!++)
>
>
> {
>
>
> m! = (i! - 1) * 1.5
>
>
> if (i! > 1)
>
>
> {
>
>
> exp! = exp! * m!
>
>
> }
>
>
> mwin(exp!)
>
>
> wait()
>
>
> mwincls()
>
>
> }
> ```
>

that said 10 mil

### Levi · 2006-06-14 22:04 · #B327615

That's very true Malegnis but if you'll notice his equations are a bit different from those given out previously.
He has
m = (i! -1) * 1.5
What they offered was putting 1.5 to the power of something.
m = 1.5^(i!-1)
This completely changes the outcome of the equation.
1.5^0 = 1
1.5^1 = 1.5
1.5^2 = 3
1.5^3 = 3.375 and so on.
Add this to current experience points would look like this.
Exp is 20 to start with so we'll start there. Associated i! numbers appear in brackets before each result to know what power 1.5 was calculated to.
[0] 20 * 1 = 20
[1] 20 * 1.5 = 30
[2] 20 * 3 = 60
[3] 20 * 3.375 = 67.5
Each number in the brackets actually refers to the i! minus 1 so those should be level 1 = 20 level 2 = 30 and so on just as was mentioned before. A little mistake like what was presented could have disasterous effects. In fact let's look at those effects shall we?
1.5 * 0 = 0 : 20 * 0 = 0
STOP!! Problem already, this says exp! is suppose to be multiplied by 0. This is only stopped but a fortunate if statement that prevents it from getting to the exp! variable. So we continue.
1.5 * 1 = 1.5 : 20 * 1.5 = 30 //So far so good. Level 2 is at level 30.
1.5 * 2 = 3 : 20 * 3 = 60 //again right on.
1.5 * 3 = 4.5 : 20 * 4.5 = 90// Wow, way off. And here our trouble begins. exp! will constantly get higher and higher until we reach the millions which is absolutley absurd.
How's that for an explination huh? Who's your friend? Not like those freaks who love to "yell" at others. Hope this helps in your comprehension.

### Colin · 2006-06-14 23:06 · #B327653

Sorry, forensixman, I misunderstood what you wanted. If the problem is still open (which I believe it is), I do believe this is the proper function:
![](http://img91.imageshack.us/img91/8238/function4hn.png)
Which simplifies to:
![](http://img150.imageshack.us/img150/4062/simplified5bx.png)
Or, in RPGCode,

**Code:**

```
experience! = 20 * 1.5 ^ (level! - 1)
```

I hope that helps. It works for all of your sample data.

### UltimaWizard · 2006-06-14 23:38 · #B327683

I use the following for EXPTNL code:
y = 8x ^ 2 + 25
Where:
--x: Current EXP TNL
--y: New EXP TNL
[Edit]: Had to remove the RPGCode version because a smiley appeared. Sad
Thus:
------------------------------------------------------
[Level] [Exp TNL] [Total EXP]
------------------------------------------------------
Lv. 1 -- 33 -- 33
Lv. 2 -- 67 -- 100
Lv. 3 -- 97 -- 197
Lv. 4 -- 153 -- 350
Lv. 5 -- 225 -- 575
Lv. 6 -- 313 -- 888
Lv. 7 -- 417 -- 1305
Lv. 8 -- 537 -- 1842
------------------------------------------------------
The EXP TNL raises at a very steady rate, but it still has roughly a square-root-function relationship. Further, it's just enough to prove challenging for the player to achieve, yet reasonable enough that it dosen't take forever to level up. Smile

### Malegnis · 2006-06-14 23:52 · #B327687

ok seeing as how DnD is god of all roleplaying games. i thought i would post their formula

**the epic level handbook wrote:**

> simply add your current level times 1000 XP (your level basicly) to the experience poins required for your current level.
>

so...

**Code:**

```
expneeded!=1000

x!=level

expneeded!=level!*1000+expneeded!
```

### Colin · 2006-06-15 00:31 · #B327702

The problem with that definition is that it is like my initial function definition
![](http://img91.imageshack.us/img91/8238/function4hn.png)
in that it is recursive. I have, however, simplified the geometric series. Because I have definitively solved the problem, you can stop posting now, as additional information will not be useful.

> [!missing] gap:16-30 · http://toolkitzone.com/forums/viewtopic.php?t=30540&start=15 · never-captured
> Page 2 of 2 was not recovered.
