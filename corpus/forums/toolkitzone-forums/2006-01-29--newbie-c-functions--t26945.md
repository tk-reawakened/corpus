---
kind: forum-thread
id: "toolkitzone-forums/26945"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Programming"
skin: "phpbb2"
thread_id: "26945"
title: "Newbie, C++ functions"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=26945"
written: "2006-01-29T05:21:00"
last_post: "2006-01-30T06:46:00"
date_confidence: "exact"
captured: ["20060215220016", "20060218113948"]
author: "Bartuc"
repliers: ["Zap!", "Notsosuperhero"]
authors: ["Bartuc", "Zap!", "Notsosuperhero"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_293386_amp_3Bsid_a26286c7c30be0d7005dbefa31f6e465", captured: "20060215220016", sha256: "3cefa1343ff515aaa792332ce0dc6b64a0fdfbb028e9a61ab5366415603e6eec", wayback_url: "https://web.archive.org/web/20060215220016/http://www.toolkitzone.com/forums/viewtopic.php?p=293386&amp%3Bsid=a26286c7c30be0d7005dbefa31f6e465"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_293638_amp_3Bsid_c8a8ee9a55e1d9ae96da323162465370", captured: "20060218113948", sha256: "5c1057ac4dc4b20e51b6731bdb3569a98d1eb9b0043360920e4c599b7fe1b9c8", wayback_url: "https://web.archive.org/web/20060218113948/http://www.toolkitzone.com/forums/viewtopic.php?p=293638&amp%3Bsid=c8a8ee9a55e1d9ae96da323162465370"}
links:
  - {url: "http://cplusplus.com/doc/tutorial/functions.html", status: "external", local: null}
---

# Newbie, C++ functions

### Bartuc · 2006-01-29 05:21 · #B293336

Im just getting started in learning C++. This may sound like a stupid question, so sry, but are functions in C++ the same as methods in toolkit?

### Zap! · 2006-01-29 06:41 · #B293356

You can think of a function in the same way as a method.
I'll show you a code sample of each:

**RPG Code wrote:**

>
> **Code:**
>
> ```
> method myMethod ()
>
>
> {
>
>
>     Text("Hey!")
>
>
> }
> ```
>

**C++ wrote:**

>
> **Code:**
>
> ```
> void myFunction ()
>
>
> {
>
>
>     printf("Hi!");
>
>
> }
> ```
>

The big difference between the two is that in C++, in order to return say, an integer, you would have to declare the function with the keyword "int" rather then the keyword "void". As "void" means no return and "int" means int return.
In RPG Code though, you can return whatever value you want with the Method keyword. Also, all C++ functions end with a semi-colon.
And you can then use myFunction(); later on in your code, just like you can use myMethod() later on in the RPG Code program file.

### Notsosuperhero · 2006-01-29 08:40 · #B293386

This should help
<http://cplusplus.com/doc/tutorial/functions.html>
That will explain alot.

### Bartuc · 2006-01-30 06:46 · #B293638

ok, i get it now. Thank you for the help
