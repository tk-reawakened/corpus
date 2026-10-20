---
kind: forum-thread
id: "toolkitzone-forum/44706"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "44706"
title: "Who is using Object Oriented code?"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=44706"
written: "2010-03-07T12:44:00"
last_post: "2010-03-12T01:23:00"
date_confidence: "exact"
captured: ["20100313191554", "20100313191600"]
author: "raymondsmindjob"
repliers: ["ASHBAD_ALVIN", "Wolf", "necromancer13", "Akura_TheDragonBlader"]
authors: ["raymondsmindjob", "ASHBAD_ALVIN", "Wolf", "necromancer13", "Akura_TheDragonBlader"]
posts_present: 7
pages_present: [3]
pages_total: 3
posts_per_page: 10
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 10, url: "http://toolkitzone.com/forum/viewtopic.php?t=44706", reason: "never-captured"}
  - {page: 2, start: 11, end: 20, url: "http://toolkitzone.com/forum/viewtopic.php?t=44706&start=10", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_492046", captured: "20100313191554", sha256: "a9d1091a1e6913daddb5d9664252edb176e40d28da58bc78dc2537c2f9b3cd48", wayback_url: "https://web.archive.org/web/20100313191554/http://www.toolkitzone.com/forum/viewtopic.php?p=492046"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_492052", captured: "20100313191600", sha256: "fcd1af076475ac121a2ffc9566151f69aeb88b6707e364e27b9dd71b48e9739f", wayback_url: "https://web.archive.org/web/20100313191600/http://www.toolkitzone.com/forum/viewtopic.php?p=492052"}
links: []
---

# Who is using Object Oriented code?

### raymondsmindjob · 2010-03-11 03:11 · #K492023

**Solid objects?**

Hello, as we all know I am dumb about stuff...
When I attempt to draw vectors, I cannot get anything else to happen.
When I click on the board tools, I cannot select the Draw vectors option in the toolbar, or change any other options. There is a line I can type in but I have no idea what to put there exactly?
An I missing an option setting somewhere, I am obviously overlooking something simple.

### ASHBAD_ALVIN · 2010-03-11 12:23 · #K492029

**Solid objects?**

when you select the vectors tool, are you then hitting the pencil tool? If not, all you will do is select vectors. The pencil tool is in the set of buttons right below the main buttons.

### Wolf · 2010-03-12 01:23 · #K492052

**Solid objects?**

To draw vectors, just click the vector tools button (or press v on your keyboard), click the pencil button (or d on your keyboard), and then click on your board to draw the vectors.

> [!missing] gap:1-10 · http://toolkitzone.com/forum/viewtopic.php?t=44706 · never-captured
> Page 1 of 3 was not recovered.

> [!missing] gap:11-20 · http://toolkitzone.com/forum/viewtopic.php?t=44706&start=10 · never-captured
> Page 2 of 3 was not recovered.

### ASHBAD_ALVIN · 2010-03-07 12:44 · #K491900

**Johnstein wrote:**

> What the code does is first makes the variable, my2Darray, into an array object of 10 elements.
> so you can use my2Darray[2], etc.
> Now, the loop loops from 0 to 9 (10 elements) and turns each element of my2Darray into ANOTHER array object of 10 elements.
> so now, my2Darray[2] has 10 elements. my2Darray[2][0], my2Darray[2][1], ..., my2Darray[2][9].
> But my2Darray[3], my2Darray[4], ... etc ALSO have 10 members each.
> So in the end, after the looping, each of your original array elements each are themselves an array of 10 elements. Thus, in the end, you have my2Darray[0][0] to my2Darray[9][9], which is in effect, a 2D, 10x10 array.
>

Thanks, Johnstein. You're really helpful.
Sorry, 10 minutes after I posted asking for an explanation, jackyboy sent me a message explaining it.
But wioth both of your guy's help, I get it now. Thanks a ton Very Happy

### necromancer13 · 2010-03-07 16:24 · #K491907

I've never understood classes clearly, although Imma see this "CArray" that you speak of. I always use arrays for player stats, enemy stats, actually I use arrays for everything now that I think about it.

### ASHBAD_ALVIN · 2010-03-07 16:25 · #K491908

**necromancer13 wrote:**

> I've never understood classes clearly, although Imma see this "CArray" that you speak of. I always use arrays for player stats, enemy stats, actually I use arrays for everything now that I think about it.
>

I personally like using classes for stats much better.
I mostly get OOPRPG code, and it is quite useful

### Akura_TheDragonBlader · 2010-03-11 22:57 · #K492046

My characters, items, and enemies(when I get to it, haven't touched it since '09) are all use classes. Considering how many variables make up each character(I forget the exact number, sixty-something, I think), OOP makes it a lot easier to manage it all.
They aren't that hard to understand once you get into it.
