---
kind: forum-thread
id: "toolkitzone-forums/21516"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Programming"
skin: "phpbb2"
thread_id: "21516"
title: "Help with graphics in c++"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=21516"
written: "2005-10-17T02:20:00"
last_post: "2005-10-20T08:53:00"
date_confidence: "exact"
captured: ["20051212022127"]
author: "Dominea"
repliers: ["Colin", "Marc", "Ersuis", "Levi"]
authors: ["Dominea", "Colin", "Marc", "Ersuis", "Levi"]
posts_present: 9
pages_present: [2]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 15, url: "http://toolkitzone.com/forums/viewtopic.php?t=21516", reason: "capture-failed"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_265058_amp_3Bsid_b4534c849086ea60f22aa5790d1e69a7", captured: "20051212022127", sha256: "1f3d00e36d2e5d7f2e14f37afad3aa65f9d2a044a3e7c9e0ebc234bdaf260108", wayback_url: "https://web.archive.org/web/20051212022127/http://toolkitzone.com/forums/viewtopic.php?p=265058&amp%3Bsid=b4534c849086ea60f22aa5790d1e69a7"}
links: []
---

# Help with graphics in c++

> [!missing] gap:1-15 · http://toolkitzone.com/forums/viewtopic.php?t=21516 · capture-failed
> Page 1 of 2 was not recovered.

### Dominea · 2005-10-17 02:20 · #B264936

**Quote:**

> It does demand respect, everyone seems to think that just cause its a Microsoft product its shit, IMO It looks alot cleaner than OpenGL which I like.
>

I personally like OpenGL better but its all good. Personally I think Direct DirectX could have been done without all the needed macro sizeof and LP_SOMETYPE shit but ya. SDL is a good start too bro.(plus you can tie it in with OGL.

### Colin · 2005-10-17 02:24 · #B264940

**Code:**

```
typedef struct tagSomething

{

   /* ... */

} SOMETHING, *LPSOMETHING;
```

People have been making structs this way for forty years. It might be a good time to notice the pattern.

### Marc · 2005-10-17 19:23 · #B265049

Indeed, Colin.
I prefer DirectX to openGL because, some of the computers that I've seen don't support/fully support openGL. But then again, I haven't fiddled with them.

### Dominea · 2005-10-17 20:14 · #B265053

**Colin wrote:**

>
> **Code:**
>
> ```
> typedef struct tagSomething
>
>
> {
>
>
>    /* ... */
>
>
> } SOMETHING, *LPSOMETHING;
> ```
>
> People have been making structs this way for forty years. It might be a good time to notice the pattern.
>

SOmetimes staying traditional isnt the best thing to do bro. C++ is the new language of choice for games not C.

### Colin · 2005-10-17 20:22 · #B265058

It isn't done that way because all programmers are afraid of new things. It is done that way because that is the best way to do it. I find pointer typedefs incredibly useful. You just showed that you knew nothing by talking about 'LP_SOMETYPE shit', so I hoped to help by illustrating the pattern.

### Dominea · 2005-10-19 02:55 · #B265468

oh yes I didnt know anything because I used an example. Sure Colin lets all bow down to the Programming Know it all that obviously doesnt understand that OOP is better than C. God I missed the arguments:)

### Ersuis · 2005-10-19 04:38 · #B265478

OOP is a paradigm.
C is a language.
They're not comparable at all.
At my uni, you can take courses on C++ and C fairly early in the computer science program, if you don't already know them. Do they teach you those where you are, or is it just code that you're supposed to copy from some other game's source?

### Levi · 2005-10-19 04:53 · #B265480

I wouldn't call him a programming know it all. He does however know quite a lot and is very proficient in what he does. So he stated an opinion, no need to get riled up about it.
I do however have question. Why are pointer typedefs so much better in certain cases over OOP? I mean you stated before that in C++ a struct is just another form of class or something along those lines. I can't recall exactly what was said.
But rather than this back and forth that seems to go on. Could you explain for those of us less knowledgeable as to why you deem them to be better, or as to why they just are better in this case/scenario.
I've found typedefs to be somewhat annoying while learning API because I keep mistaking a single data parameter in the function calls with the different types and structures one needs to use. So I went to VB where I wasn't forced to know any of that. (Yes I am lazy.)
So I'm just curious as to why it was done this way.

### Dominea · 2005-10-20 08:53 · #B265695

In C++ structs are just classes that are defaulted to public. All that Typedefing a struct in C is so you can create two keywords in one. Notice the SOMETHING and LPSOMETHING. One denotes the struct itself and one denotes a pointer to it. Thats pretty much all that does. I dont know if I have explained it that well but meh.
