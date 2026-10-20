---
kind: forum-thread
id: "toolkitzone-forums/11121"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "11121"
title: "Want a challenge?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11121"
written: "2004-11-14T08:01:00"
last_post: "2004-11-30T04:56:00"
date_confidence: "exact"
captured: ["20050113181425"]
author: "Dont_Think_So"
repliers: ["p90m16mp5a4", "Moo Of Doom"]
authors: ["Dont_Think_So", "p90m16mp5a4", "Moo Of Doom"]
posts_present: 6
pages_present: [2]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 15, url: "http://toolkitzone.com/forums/viewtopic.php?t=11121", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_131965_amp_", captured: "20050113181425", sha256: "a485e95e200a5b332a6c6647603f92797e43c4efd8be6095000e80d36cd95787", wayback_url: "https://web.archive.org/web/20050113181425/http://www.toolkitzone.com/forums/viewtopic.php?p=131965&amp="}
links:
  - {url: "http://www.mysticsoftware.net", status: "captured", local: "wayback/mysticsoftware.net/index-572c95"}
---

# Want a challenge?

> [!missing] gap:1-15 · http://toolkitzone.com/forums/viewtopic.php?t=11121 · never-captured
> Page 1 of 2 was not recovered.

### Dont_Think_So · 2004-11-14 08:01 · #B125055

I made a round method a loooong time ago... it's in my method pack at [www.mysticsoftware.net](http://www.mysticsoftware.net)
Among a few other things.

### p90m16mp5a4 · 2004-11-21 03:31 · #B127884

Hey you guys! I cannot thank everyone enough for your input!
After playing with this yesterday I understand how much you can use variables, in anything! My eyes opened up like a man coming out of a six week coma!
First off I didn't understand really what any of you were saying.. so I tried my process step by step.. testing each individual entity before putting it together.
I could go into detail but... im sure it would bore everyone, anyways heres my code! it actually works!
And i didn't rip off, or copy what you guys wrote on the boards, cuz like i said i didn't understand it :'( But i completely do now.
#MWin("Click your character now!")
#Delay(.5)
#MouseClick(PX!, PY!)
#MWin("Click where ya wanna go")
#Delay(.5)
#MouseClick(DX!, DY!)
#Pnx! = px!/32
#pny! = py!/32
#CastInt(pnx!, pfx!)
#CastInt(pny!, pfy!)
#dnx! = dx!/32
#dny! = dy!/32
#CastInt(dnx!, dfx!)
#CastInt(dny!, dfy!)
#PathFind(pfx!,pfy!,dfx!,dfy!,TusHP$)
#Push(tusHP$, "Frap")
#MWinCls()
#Return
Thanks again guys for helping me up this big step in programming!

### Moo Of Doom · 2004-11-26 19:27 · #B130518

**Colin wrote:**

> Or use something to this effect to annoy the player less:
>
> **Code:**
>
> ```
> //--------------------------------------------------
>
>
> // Round the number passed in
>
>
> //--------------------------------------------------
>
>
> method round(numIn!)
>
>
> {
>
>
>
>
>
>    // Cast to an integer
>
>
>    roundInt! = CastInt(numIn!)
>
>
>
>
>
>    // Compute the difference
>
>
>    roundDiff! = numIn! - roundInt!
>
>
>
>
>
>    // Check which way to round
>
>
>    if (roundDiff! >= 0.5)
>
>
>    {
>
>
>       // Round up
>
>
>       toRet! = roundInt! + 1
>
>
>    }
>
>
>    else
>
>
>    {
>
>
>       // Round down
>
>
>       toRet! = roundInt!
>
>
>    }
>
>
>
>
>
>    // Return what we've calculated
>
>
>    returnMethod(toRet!)
>
>
>
>
>
>    // Clean up
>
>
>    kill(roundInt!, roundDiff!, toRet!)
>
>
>
>
>
> }
> ```
>
> I've seen people do so many things for something so simple-- even truiken looked for the decimal with string manipulation. Razz
>

I think you could even go one better:

**rpgcode:**

```
//--------------------------------------------------

// Round the number passed in

//--------------------------------------------------

method round(numIn!)

{

// Add 0.5

     toRound! = numIn! + 0.5

// Cast to an integer

     roundInt! = CastInt(toRound!)

// Return what we've calculated

     returnMethod(roundInt!)

// Clean up

     kill(toRound!, roundInt!)

}
```

Very Happy

### Dont_Think_So · 2004-11-27 06:59 · #B130851

Yes, but my round method works in TK2 (of course you should be using TK3, seeing as you're in this forum), and rounds to odd numbers such as to the nearest 100th or 908th. You never know what people would need. Smile

### Moo Of Doom · 2004-11-27 07:43 · #B130867

**Dont_Think_So wrote:**

> Yes, but my round method works in TK2 (of course you should be using TK3, seeing as you're in this forum), and rounds to odd numbers such as to the nearest 100th or 908th. You never know what people would need. Smile
>

Hmm... let's see if my method works for that...

**rpgcode:**

```
//--------------------------------------------------

// Round the number passed in

//--------------------------------------------------

method round(numIn!, toNearest!)

{

// Divide by rounding factor

     toRound! = numIn! / toNearest!

// Add 0.5

     toRound! = toRound! + 0.5

// Cast to an integer

     roundInt! = CastInt(toRound!)

// Multiply by rounding factor

     toRet! = roundInt! * toNearest!

// Return what we've calculated

     returnMethod(toRet!)

// Clean up

     kill(toRound!, roundInt!, toRet!)

}
```

I think that works. Tell me if it does.
Syntax is
round(3.586980, 0.125)
to round to the nearest eighth.

### p90m16mp5a4 · 2004-11-30 04:56 · #B131965

uh.. why would you want to round the number when you can just do it in the #if syntax or on a single line..
