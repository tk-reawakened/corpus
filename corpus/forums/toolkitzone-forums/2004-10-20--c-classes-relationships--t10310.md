---
kind: forum-thread
id: "toolkitzone-forums/10310"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "10310"
title: "C++, classes, relationships..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10310"
written: "2004-10-20T02:39:00"
last_post: "2004-10-20T14:40:00"
date_confidence: "exact"
captured: ["20041226085913"]
author: "Serge"
repliers: ["gcn_zelda", "blackpanther6389", "khin"]
authors: ["Serge", "gcn_zelda", "blackpanther6389", "khin"]
posts_present: 5
pages_present: [2]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 15, url: "http://toolkitzone.com/forums/viewtopic.php?t=10310", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_113598_amp_", captured: "20041226085913", sha256: "20bf73d7a95a1bb47891c0b7cb6bfebff917a86ddce9bb5033fcaec00d91d63c", wayback_url: "https://web.archive.org/web/20041226085913/http://www.toolkitzone.com/forums/viewtopic.php?p=113598&amp="}
links: []
---

# C++, classes, relationships...

> [!missing] gap:1-15 · http://toolkitzone.com/forums/viewtopic.php?t=10310 · never-captured
> Page 1 of 2 was not recovered.

### Serge · 2004-10-20 02:39 · #B113454

**Quote:**

> What we need is the technique called 'reference passing'. Pointers can also be used, but i find this a better way, plus i don't have to use the -> operator(laziness). Putting an '&' sign before the object variable denotes that we ARE NOT passing a COPY of the object, instead we are passing the MEMORY ADDRESS of the object. Long story short, we are passing the OBJECT ITSELF.
> Code:
> void ClassB::SomeFunction(ClassA&x, int x);
> Using the above prototype, it will be clearly understood that the memory location of the object will be taken(not a copy of the value), hence, any change we make to 'x' shall reflect to the object that we passed in our 'main()' function, wich is object 'z'.
>

Okay, I think I get it Very Happy
so in the ClassA&x, its declaring a reference to the memory address of an object of ClassA, righto? The ClassA before the &x is what confused me, I guess.
Thanks a ton, KSNiloc and especially Khin.

### gcn_zelda · 2004-10-20 02:39 · #B113455

He's in Junior High Wink

### blackpanther6389 · 2004-10-20 02:41 · #B113458

If you are talking about KSNiloc, then damn, I need to do some studying, I thought I was smart, but in comparison with KSN, I dont even tread water. Embarassed

### khin · 2004-10-20 05:56 · #B113515

Yeah, KSN is right. I just wanted to be more explicit. Good thing he pointed that out.
Oh and blackpanther, nobody taught me C++ too. I just learned C in 3rd year college(my professor sucks by the way), and i self-studied C++. I also self-studied Java and VB.
Lazy teachers can also bring out the best in us, i figured. That way we will be eager to learn things and stand on our own rather than depending on them. Sometimes they teach wrong stuff too Smile
The ClassA before the '&' is the data type. It's part of the generic function declaration. You need a data type then a variable plaveholder. Putting ClassA just tells the compiler to expect data of type ClassA and therefore allocate enough space to 'x' so it could 'catch' the incoming parameter properly.
Yeah, i thought KSN was a genius too, i wasn't wrong. Man, you could even teach my 20-year old students here Smile

### blackpanther6389 · 2004-10-20 14:40 · #B113598

I know. I can learn a lot from you guys I love listening to intelligent people. You guys have inspired me to just go off on my own and teach myself C++ forget my teacher.
