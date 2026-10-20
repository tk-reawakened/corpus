---
kind: forum-thread
id: "toolkitzone-forums/5812"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "5812"
title: "A new plugin SDK project...I need help..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=5812"
written: "2004-07-16T04:21:00"
last_post: "2004-07-16T22:28:00"
date_confidence: "exact"
captured: ["20040920063127"]
author: "Levi"
repliers: ["Marc", "Ersuis"]
authors: ["Levi", "Marc", "Ersuis"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_60224_amp_", captured: "20040920063127", sha256: "05f2a41d86d95df573c8e38e496ecbac996c8104d76a61f92d005c0343ec35af", wayback_url: "https://web.archive.org/web/20040920063127/http://www.toolkitzone.com/forums/viewtopic.php?p=60224&amp="}
links:
  - {url: "http://img76.exs.cx/img76/421/Muahahahaha.jpg", status: "external", local: null}
  - {url: "http://img85.exs.cx/img85/3596/Niloc.gif", status: "external", local: null}
  - {url: "http://www.your-poetry.com/modules.php?name=News&file=article&sid=39971", status: "external", local: null}
---

# A new plugin SDK project...I need help...

### Levi · 2004-07-16 04:21 · #B59798

It has come to my attention that there are many out there with little to no access to the currect languages needed to create a plugin for the toolkit. VB, Delphi, MFC libraries for C++. Many can't get any of them for lack of money or time. So I decided it was time to look into an alternative way to program a plugin. But what language? Then it hit me, why a new language? Why not simply a new method? A new SDK?
But how would you make a new SDK? Suggest it to the team working on TK3? No I mean a new SDK for toolkit 2.2 or at least close to it. I mean creating a plugin using the current toolkit SDK that can access a plugin built upon a new SDK. I don't have it completely thought out yet but I do have a general idea. I'm trying to recruit people so that as a group effort we can come up with something.
Here is my current idea. The toolkit can send information and recieve it through its SDK. We set up our plugin to react to a query function in our new SDK to send all the relevant data in much the same fashion. Our SDK will be basically a clone of the original. It'll just be a little harder getting all the functions correct and down. We also need to make sure it can send and recieve data to a DLL that isn't made by the MFC libraries. If we can do this, the need for MFC will cease to exist. Just one quick compile and the dll we use as an intermediary will be made and useable by all C++ programmers.
I am a C++ beginner programmer by ability, but I have managed to create my own plugins for the toolkit before, it contained two commands Len(string, length) and Instr(startPos, string to search, string to searchfor, position). So I know a little about the original SDK and its capabilities.
Now my idea brings to mind many numerous problems but the two major ones are this. Can you give over control from an MFC made plugin to a regular DLL? And how will these two actively share correct and accurate information. Well naturally doing this will place great restraints on what you can and cannot do for a plugin command. But it would allow you to do more than you currently can without being able to program a plugin at all.
What do you think?
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

### Marc · 2004-07-16 04:27 · #B59799

Levi your wonderous!
I think It's a good idea. Most people that want to make plugins with C++ can't because we don't have the MFC librarys.
_________________
![](http://img85.exs.cx/img85/3596/Niloc.gif)
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### Ersuis · 2004-07-16 22:28 · #B60224

Go for it. Very Happy
I thought about doing something like that when I got stuck on my non-MFC VC++-not-required plugin SDK, but it seemed like a lot of work.
Go for it, though. It'd definately open up some avenues to a lot of people who can't afford (or don't want to download) the Microsoft compiler or want to use something else instead.
_________________
-Curt
