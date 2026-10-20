---
kind: forum-thread
id: "toolkitzone-forums/7026"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "7026"
title: "VC++ 6 Question [Resolved]"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7026"
written: "2004-08-11T23:35:00"
last_post: "2004-08-13T15:17:00"
date_confidence: "exact"
captured: ["20040923105824"]
author: "Marc"
repliers: ["KSNiloc", "Master Tamer", "gcn_zelda", "Levi"]
authors: ["Marc", "KSNiloc", "Master Tamer", "gcn_zelda", "Levi"]
posts_present: 13
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_74684_amp_", captured: "20040923105824", sha256: "073c55d77aebffd428b720fc7cb93688b80880a8f3540f431536005dde7acdb1", wayback_url: "https://web.archive.org/web/20040923105824/http://www.toolkitzone.com/forums/viewtopic.php?p=74684&amp="}
links:
  - {url: "http://cywh.com/ot/", status: "external", local: null}
  - {url: "http://img76.exs.cx/img76/421/Muahahahaha.jpg", status: "external", local: null}
  - {url: "http://img85.exs.cx/img85/3596/Niloc.gif", status: "external", local: null}
  - {url: "http://rpgtoolkithole.000k2.com/images/antianti.png", status: "external", local: null}
  - {url: "http://www.mg.geahost.com/small_theproject.gif", status: "external", local: null}
  - {url: "http://www.mozilla.org/products/firefox/", status: "external", local: null}
  - {url: "http://www.your-poetry.com/modules.php?name=News&file=article&sid=39971", status: "external", local: null}
---

# VC++ 6 Question [Resolved]

### Marc · 2004-08-11 23:35 · #B73571

What kind of project type would I use for OpenGL in Microsoft Visual C++ 6?
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### KSNiloc · 2004-08-11 23:37 · #B73573

Standard Application... same as any other non activeX application.
_________________
Pawn.

### Marc · 2004-08-11 23:49 · #B73582

Yes very helpfull, I actualy know which out of the many files to choose from to use.
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### Master Tamer · 2004-08-11 23:54 · #B73589

word2!
You told me not to learn openGL, then you go do it!
_________________
![](http://img85.exs.cx/img85/3596/Niloc.gif)

### Marc · 2004-08-11 23:57 · #B73592

I'm learning for my sake sheesh!
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### KSNiloc · 2004-08-11 23:59 · #B73593

YOU MAKE A STANDARD APPLICATION!
There's no challange here.
Add a reference to OpenGL and you're good to go.
_________________
Pawn.

### gcn_zelda · 2004-08-12 00:06 · #B73597

Yeah. Just use a blank source file...
_________________
.:: [Get Firefox!](http://www.mozilla.org/products/firefox/)::.
.:: [Off-Topicness!](http://cywh.com/ot/)::.
.::(redacted: email)::.
[
![](http://www.mg.geahost.com/small_theproject.gif)
![](http://rpgtoolkithole.000k2.com/images/antianti.png)

### Marc · 2004-08-12 00:25 · #B73603

But arnt those blank projects just text Confused
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### Master Tamer · 2004-08-12 00:30 · #B73610

yes, WORD2; I dont care if your name is MARC!
_________________
![](http://img85.exs.cx/img85/3596/Niloc.gif)

### gcn_zelda · 2004-08-12 00:35 · #B73612

Uh... You could write a program in Notepad and compile it without an IDE. VC++ is just an IDE, even though it has a compiler.
_________________
.:: [Get Firefox!](http://www.mozilla.org/products/firefox/)::.
.:: [Off-Topicness!](http://cywh.com/ot/)::.
.::(redacted: email)::.
[
![](http://www.mg.geahost.com/small_theproject.gif)
![](http://rpgtoolkithole.000k2.com/images/antianti.png)

### Marc · 2004-08-12 18:50 · #B74092

Ok, for doing OpenGL What are you supposed to link to?
I linked to OPENGL32.lib and it cleared most of my errors.
But I still have 1 left.

**Quote:**

> -----------------Configuration: ddsa - Win32 Debug--------------------
> Linking...
> ddsa.obj : error LNK2001: unresolved external symbol _gluPerspective@32
> Debug/ddsa.exe : fatal error LNK1120: 1 unresolved externals
> Error executing link.exe.
> ddsa.exe - 2 error(s), 0 warning(s)
>

Anyone know what other librarys I might need to link to?
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### Levi · 2004-08-13 04:29 · #B74504

There is a game development website with many good tutorials on the use of OPENGL. I belive its called GameDev or something like that. Tutorials on this are very easy to find, everyone wants to do it now adays.
_________________
Levi
"Darkness hides the light
Darkness keeps me from it
Darkness is my life
Darkness I am in it"
"Light and Darkness my life is filled with thee
Light and Darkness my life my destiny
Light and Darkness both my life they share
Light and Darkness does no one care"
Quotes from "Who I am" by Levi
<http://www.your-poetry.com/modules.php?name=News&file=article&sid=39971>

### Marc · 2004-08-13 15:17 · #B74684

Ok, thanks. I found what I needed.
glu32.lib and opngl32.lib where the librarys needed.
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)
