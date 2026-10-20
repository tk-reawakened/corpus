---
kind: forum-thread
id: "toolkitzone-forums/6006"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "6006"
title: "Visual BASIC .NET cost too much..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=6006"
written: "2004-07-20T00:21:00"
last_post: "2004-07-21T18:43:00"
date_confidence: "exact"
captured: ["20040920063139"]
author: "Master Tamer"
repliers: ["KSNiloc", "Marc", "Dan", "-*khaos*-"]
authors: ["Master Tamer", "KSNiloc", "Marc", "Dan", "-*khaos*-"]
posts_present: 13
pages_present: [2]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 15, url: "http://toolkitzone.com/forums/viewtopic.php?t=6006", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_62933_amp_", captured: "20040920063139", sha256: "dcab6f2cbd4322fd16502565b315c25eef5fa84383c14723e2fb3353a4c2fb12", wayback_url: "https://web.archive.org/web/20040920063139/http://www.toolkitzone.com/forums/viewtopic.php?p=62933&amp="}
links:
  - {url: "http://archive.dc-3.co.uk/", status: "external", local: null}
  - {url: "http://forums.aeronic.net", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v491/Diddums/banner.png", status: "external", local: null}
  - {url: "http://img76.exs.cx/img76/421/Muahahahaha.jpg", status: "external", local: null}
  - {url: "http://img85.exs.cx/img85/3596/Niloc.gif", status: "external", local: null}
  - {url: "http://mr-diddums.tk", status: "external", local: null}
  - {url: "http://www.dc-3.co.uk/stuff/getfirefox.png", status: "external", local: null}
  - {url: "http://www.freewebs.com/khaosking", status: "external", local: null}
  - {url: "http://www.geocities.com/tamexplayer/antimastertamer.PNG", status: "external", local: null}
  - {url: "http://www.hilaryduff.com", status: "external", local: null}
  - {url: "http://www.mozilla.org/products/firefox", status: "external", local: null}
  - {url: "http://www.mr-diddums.tk", status: "external", local: null}
  - {url: "http://www.rpgadev.com", status: "external", local: null}
  - {url: "http://www.rpgadev.com/header1.jpg", status: "external", local: null}
---

# Visual BASIC .NET cost too much...

> [!missing] gap:1-15 · http://toolkitzone.com/forums/viewtopic.php?t=6006 · never-captured
> Page 1 of 2 was not recovered.

### Master Tamer · 2004-07-20 00:21 · #B61964

it's still downloading.
_________________
MMORPG creation
[![](http://www.rpgadev.com/header1.jpg)](http://www.rpgadev.com)
[![](http://www.geocities.com/tamexplayer/antimastertamer.PNG)](http://www.hilaryduff.com)
![](http://img85.exs.cx/img85/3596/Niloc.gif)

### KSNiloc · 2004-07-20 18:07 · #B62459

**Word2 wrote:**

> Thankyou for telling me, you could have done that right away and save up the argueing.
> Edit: So that you can rest assured all I wanted was to add this:
>
> **Code:**
>
> ```
> Case "^":
>
>
>                         numberuse(t + 1) = numberuse(t) ^ numberset(t + 1)
> ```
>
> SO that you can do exponential operations.
> I'm sure some where along the line I will have to add to it or somthing.
>

You'll have to modify a number of other subs as well, silly.
_________________
[![](http://img.photobucket.com/albums/v491/Diddums/banner.png)](http://mr-diddums.tk)

### Marc · 2004-07-20 18:54 · #B62504

**KSNiloc wrote:**

>
> **Word2 wrote:**
>
> > Thankyou for telling me, you could have done that right away and save up the argueing.
> > Edit: So that you can rest assured all I wanted was to add this:
> >
> > **Code:**
> >
> > ```
> > Case "^":
> >
> >
> >                         numberuse(t + 1) = numberuse(t) ^ numberset(t + 1)
> > ```
> >
> > SO that you can do exponential operations.
> > I'm sure some where along the line I will have to add to it or somthing.
> >
>
> You'll have to modify a number of other subs as well, silly.
>

I know that and shortly I will be working on that. I added one new variables
RPGCodeSetSmNumVar and it gave me a cannot find thing. I don't see where I didn't define it, perhaps you could answere this for me.
_________________
![](http://img85.exs.cx/img85/3596/Niloc.gif)
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### KSNiloc · 2004-07-20 19:11 · #B62516

Ah. LOOK! I don't WANT YOU messing with the TK. :S

**Code:**

```
Declare Function MyFunction Lib "actkrt3.dll" (parameters)
```

_________________
[![](http://img.photobucket.com/albums/v491/Diddums/banner.png)](http://mr-diddums.tk)

### Marc · 2004-07-20 19:30 · #B62530

**KSNiloc wrote:**

> Ah. LOOK! I don't WANT YOU messing with the TK. :S
>
> **Code:**
>
> ```
> Declare Function MyFunction Lib "actkrt3.dll" (parameters)
> ```
>

Either way it's up to Vampz to accept the changes. So...
I did that.

**Code:**

```
Declare Function RPGCSetSmNumVar Lib "actkrt3.dll" (ByVal varName As String, ByVal value As Double, ByVal heapID As Long) As Long
```

_________________
![](http://img85.exs.cx/img85/3596/Niloc.gif)
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### KSNiloc · 2004-07-20 22:22 · #B62595

And of course, it needs to be exported from actkrt3.dll AND needs the APIENTRY keyword in its declaration.
_________________
[![](http://img.photobucket.com/albums/v491/Diddums/banner.png)](http://mr-diddums.tk)

### Marc · 2004-07-21 00:12 · #B62610

That is included. Here is the source for that perticular "feature".

**Code:**

```
/*

 Set small numaricle  var

 pstrVarName - name of variable

dValue - value of var

The reason I added this was because I am tired of slowing

down the program with a simple number like 1 this way

you can hold some space and be abit faster*/

int APIENTRY RPGCSetSmNumVar(char* pstrVarName, short int dValue, HEAP_HANDLE heap)

{

   RPGCODE_HEAP* p = heapHandleToPtr(heap);

   if (pstrVarName == NULL || p == NULL)

      return 0;

   std::string strVarName = pstrVarName;

   p->numVars[strVarName] = dValue;

   return 1;

}
```

_________________
![](http://img85.exs.cx/img85/3596/Niloc.gif)
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### KSNiloc · 2004-07-21 03:27 · #B62687

No.
You need to export it from actkrt.def and list it in the API list.
You're hopeless. Razz
_________________
[![](http://img.photobucket.com/albums/v491/Diddums/banner.png)](http://mr-diddums.tk)

### Dan · 2004-07-21 10:47 · #B62788

It does download a great deal of the installation I believe.
_________________
Dan
[Aeronic.net](http://forums.aeronic.net) :: [RPG Toolkit Archive](http://archive.dc-3.co.uk/)
[![](http://www.dc-3.co.uk/stuff/getfirefox.png)](http://www.mozilla.org/products/firefox)

### -*khaos*- · 2004-07-21 12:40 · #B62812

**Master Tamer wrote:**

> This program is taking forever to Install! It's been installing for 2 hours and it's only 1/20 done!
>

so it will take about 40 hours to get it done Razz
_________________
[Khaos Sofware](http://www.freewebs.com/khaosking)
Screw Asimir, he changed the image that my avatar is from. Sad
[![](http://img.photobucket.com/albums/v491/Diddums/banner.png)](http://www.mr-diddums.tk)

### Marc · 2004-07-21 15:01 · #B62851

**KSNiloc wrote:**

> No.
> You need to export it from actkrt.def and list it in the API list.
> You're hopeless. Razz
>

You said DLL and that was what made the actkrt3.dl. I iwll look and modify that then pester you again.l
_________________
![](http://img85.exs.cx/img85/3596/Niloc.gif)
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### Dan · 2004-07-21 15:06 · #B62853

...but not in this thread, you'll pester him in private, right?
This thread has nothing to do with your development of the TK, it's about Visual Studio
Now, back on topic, please...
_________________
Dan
[Aeronic.net](http://forums.aeronic.net) :: [RPG Toolkit Archive](http://archive.dc-3.co.uk/)
[![](http://www.dc-3.co.uk/stuff/getfirefox.png)](http://www.mozilla.org/products/firefox)

### Master Tamer · 2004-07-21 18:43 · #B62933

**Dan wrote:**

> ...but not in this thread, you'll pester him in private, right?
> This thread has nothing to do with your development of the TK, it's about Visual Studio
> Now, back on topic, please...
>

It's about time someone said that.
_________________
MMORPG creation
[![](http://www.rpgadev.com/header1.jpg)](http://www.rpgadev.com)
[![](http://www.geocities.com/tamexplayer/antimastertamer.PNG)](http://www.hilaryduff.com)
![](http://img85.exs.cx/img85/3596/Niloc.gif)
