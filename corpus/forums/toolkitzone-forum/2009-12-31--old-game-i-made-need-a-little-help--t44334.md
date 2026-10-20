---
kind: forum-thread
id: "toolkitzone-forum/44334"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "44334"
title: "Old game I made need a little help"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=44334"
written: "2009-12-31T01:29:00"
last_post: "2009-12-31T21:27:00"
date_confidence: "exact"
captured: ["20100101204508", "20100101204532", "20100101204544", "20100101204601"]
author: "slipknot_hellraiser"
repliers: ["rpg gamer 17", "cuthalion"]
authors: ["slipknot_hellraiser", "rpg gamer 17", "cuthalion"]
posts_present: 5
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_487628", captured: "20100101204544", sha256: "2c98f30518edbc4e59f13eef0cad53b935b7ed2536ac588714563dfa1b90e328", wayback_url: "https://web.archive.org/web/20100101204544/http://toolkitzone.com/forum/viewtopic.php?p=487628"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_487637", captured: "20100101204601", sha256: "2c98f30518edbc4e59f13eef0cad53b935b7ed2536ac588714563dfa1b90e328", wayback_url: "https://web.archive.org/web/20100101204601/http://toolkitzone.com/forum/viewtopic.php?p=487637"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_487643", captured: "20100101204508", sha256: "2c98f30518edbc4e59f13eef0cad53b935b7ed2536ac588714563dfa1b90e328", wayback_url: "https://web.archive.org/web/20100101204508/http://toolkitzone.com/forum/viewtopic.php?p=487643"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_44334", captured: "20100101204532", sha256: "2c98f30518edbc4e59f13eef0cad53b935b7ed2536ac588714563dfa1b90e328", wayback_url: "https://web.archive.org/web/20100101204532/http://toolkitzone.com/forum/viewtopic.php?t=44334"}
links: []
---

# Old game I made need a little help

### slipknot_hellraiser · 2009-12-31 01:29 · #K487628

Well if any of the few who did play my game (The Deal) they will remember the problem with the dealer offering less then what is actually on the board. Well the problem with this falls in the following code.

**Code:**

```
Method DealerOfferPrice()

{

 Kill(n)

 n = s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7] + s[8] + s[9] + s[10]/ p

 setbutton("",11,150,300,85,45)

 setbutton("",12,250,300,85,45)

 setImage("deal.png",150,300,85,45)

 setImage("no deal.png",250,300,85,45)

 round()

  Mymwin("The dealer has offered $<z>",1)

   mouseClick(x,y,0)

 press = checkButton(x,y)

 RestoreScreenArray(1)

 RestoreScreen()

  If(press == 11)

  {

   attackChannel = fmodPlayMedia(offer)

    delay(2)

     fmodClearChannel(attackChannel);

   mymwin("You took the deal worth $<z>",1)

   wait()

   mymwincls()

   mymwin("Lets see if you made a good deal",1)

   wait()

   mymwincls()

   setImagetransparent("case open.png",515,380,64,128,255,0,0)

   text(27.2,20.9,"<MainMoney>")

   If(MainMoney < z)

   {

    mymwin("You made a good deal",1)

    wait()

    mymwincls()

    quit = 1

   }

   ElseIf(MainMoney > z)

   {

    mymwin("Oh! Looks like you made a",1)

    mymwin("bad deal.",2)

    wait()

    mymwincls()

    quit = 1

   }

  }

  ElseIf(press == 12)

  {

   SaveScreen()

  attackChannel = fmodPlayMedia(noDeal)

  mymwin("You didn't take the deal.",1)

  wait()

  mymwincls()

  fmodClearChannel(attackChannel);

  RestoreScreenArray(1)

  RestoreScreen()

  done = false

  }
```

I have failed miserably at calculating the proper formula "I suck at math" to make the dealers price right.
Now to explain what n = s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7] + s[8] + s[9] + s[10]/ p) is doing. s[1-10] are numbers 100,300,600,900,1000,2000,3000,4000,6000,8000
I'm adding all the numbers together then dividing them by the number of cases left. after a case has been removed s[1-10] will be set to 0. so that case isn't added into the formula.
any help on coming up with a good way to insure the price is being offered properly, will be great.Hope I gave enough info, and not to confusing lol.

### rpg gamer 17 · 2009-12-31 03:25 · #K487632

First of all

**Code:**

```
n = s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7] + s[8] + s[9] + s[10]/ p
```

is

**Code:**

```
n = (s[10]/p) + s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7] + s[8] + s[9]
```

because of the order of operations.
You should use

**Code:**

```
n = (s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7] + s[8] + s[9] + s[10])/p
```

instead.

### slipknot_hellraiser · 2009-12-31 15:57 · #K487637

I haven't looked at this code for close to a year. If I remember correctly I just put that in there just to see if clearing the variable before it re added all the math together would fix the problem. But as I'm here still looking for a answer it didn't lol.

### slipknot_hellraiser · 2009-12-31 18:53 · #K487644

I'm not entirely sure why I made this a function but I did. This is where n & z are used.

**Code:**

```
function round()

{

   castInt(n,m);

   length = len(m);

   z = left(m, length - 1)

}
```

This code simply took the end number off making it appear smaller EX: 21000 the 0 on the end would be taken off making it 2100. This was my cheap way of making the TK round a number sense I still have no clue how lol.
I might just redo the whole system my coding for this game was rushed. I completed this game in like a week for my wifes website. So all the coding is just very unorganized. But I'm hoping to figure this thing out now so I don't have to do everything over Razz

### cuthalion · 2009-12-31 21:27 · #K487649

Er... well, that's not actually rounding. I think that's called "truncating", but don't quote me.
Here's rounding:

**Code:**

```
function round(number)

{

  return castInt(number + 0.5)

}
```

You can take the last digit off a number by doing this:

**Code:**

```
castInt(number / 10)
```
