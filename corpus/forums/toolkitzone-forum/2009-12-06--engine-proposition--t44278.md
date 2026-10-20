---
kind: forum-thread
id: "toolkitzone-forum/44278"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "44278"
title: "Engine Proposition"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=44278"
written: "2009-12-06T16:37:00"
last_post: "2009-12-25T04:20:00"
date_confidence: "exact"
captured: ["20100101205759", "20100101205854", "20100101205905"]
author: "Hawkeye"
repliers: ["Occasionally_Correct", "Euix", "cuthalion", "Calacruf", "SuperIsoRPG", "z3ro", "UltimaWizard"]
authors: ["Hawkeye", "Occasionally_Correct", "Euix", "cuthalion", "Calacruf", "SuperIsoRPG", "z3ro", "UltimaWizard"]
posts_present: 18
pages_present: [1, 3]
pages_total: 3
posts_per_page: 10
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 2, start: 11, end: 20, url: "http://toolkitzone.com/forum/viewtopic.php?t=44278&start=10", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_486747", captured: "20100101205905", sha256: "99e005db34c5188693c7d7d2d89c808a71f25169a0704e0b7ee8f0c9aa5d2c3d", wayback_url: "https://web.archive.org/web/20100101205905/http://toolkitzone.com/forum/viewtopic.php?p=486747"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_44278_start_0", captured: "20100101205854", sha256: "886246d3b1639ee81d3b5f6c0c042ff186a3abb12a5c200d15bc41782a4d3510", wayback_url: "https://web.archive.org/web/20100101205854/http://toolkitzone.com/forum/viewtopic.php?t=44278&start=0"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_44278_start_20", captured: "20100101205759", sha256: "700d06cadf969bbcefba320e53d5ba6bbc2765a32ff5ec2c7b556a6f986236c6", wayback_url: "https://web.archive.org/web/20100101205759/http://toolkitzone.com/forum/viewtopic.php?t=44278&start=20"}
links:
  - {url: "http://en.wikipedia.org/wiki/Interface_%28computer_science%29", status: "external", local: null}
  - {url: "http://rpgtoolkit.cvs.sourceforge.net/viewvc/rpgtoolkit/vc/trans3/rpgcode/yacc.txt?revision=1.35&view=markup#l_735", status: "external", local: null}
---

# Engine Proposition

### Hawkeye · 2009-12-06 16:37 · #K486137

**Whats up with Structs?**

Uhm... so I am currently putting my UI system on hold to develop an OOP IDE in VB. So anyways... I never ever use structs, and I really had no idea what they were. So I figured I should still put them in my dev app, and I was wondering something...
Why is it that classes can't have public variables only private, yet structs can have either? And Colin said in another post that structs and classes were internally the same, except for their default scope... Anyone know?

### Occasionally_Correct · 2009-12-06 19:50 · #K486143

**Whats up with Structs?**

That's right. Classes and structs [are the same thing](http://rpgtoolkit.cvs.sourceforge.net/viewvc/rpgtoolkit/vc/trans3/rpgcode/yacc.txt?revision=1.35&view=markup#l_735), and the only difference is the default scope. I'm pretty sure structs were originally modeled after C structs (they didn't have methods), but it's been so long that I don't properly remember now. Razz
Classes can have public variables. It might have been an error in past versions, but it's fully allowed in 3.1.0.
An [interface](http://en.wikipedia.org/wiki/Interface_%28computer_science%29) keyword was added at the same time as classes and structs, but it was undocumented and no longer exists. (Just some trivia. Razz)

### Hawkeye · 2009-12-08 04:21 · #K486195

**Whats up with Structs?**

Hmm... well I've been doing some testing and it seems like structs can have public or private methods as well as a constructor (just saying since I didn't know... =P ) and pub/priv variables. However I can't seem to be able to create public variables when creating classes. It's not a huge deal as can just use functions to return data, but I was just wondering why this is.
And is there any work-arounds for the "include" statement completely messing up classes? (besides running the library at the beginning of the game and the running the start prg...) Thanks =)

### Euix · 2009-12-08 08:16 · #K486202

**Whats up with Structs?**

The reason you may not be able to create public variables within classes likely has to do with the developer's bias; in this case it was Colin. I am fairly certain that Colin held an unwavering belief that encapsulation was an inexcusable property of object-oriented programming; therefore he forced encapsulation on developers by disallowing public scope for variadic class members.
Basically, it's possible that Colin doesn't believe in public variables within class definitions; therefore, it is not allowed.
That may not be the case, but it certainly makes sense. The philosophy of encapsulation roughly describes that the internal implementation of a class should remain hidden from developers, because the implementation does not matter (explicitly), and developers should not rely on an implementation that may or may not change in the future; instead, developers should rely on the functionality and/or outcome of an object. Essentially, encapsulation preserves modularity and scalability, among other things.
Encapsulation is generally a good thing, and it's often called data hiding because it hides context-specific implementation details (members, implementation-specific functions, etc).
On the other side, structures are just user-defined data types, in the loosest sense. A data structure is an arbitrary grouping of data constructs; the data simply exists to be manipulated. Allowing scope on a data structure produces a side-effect that gives structures the ability to store and encapsulate state.
A very simple difference between structures and classes, is that structures cannot inherit from other structures; this is obvious because structures are not considered objects. Objects have intrinsic properties, and inherit qualities from other objects, and hold state. Structures hold and manipulate data.
It's not really that simplistic, but it helps in understanding the fundamental differences. Structures are meant for data manipulation, objects are stateful and maintain relationships; structures cannot inherit other classes, or implement interfaces, etc.

### cuthalion · 2009-12-08 16:51 · #K486225

**Whats up with Structs?**

Does adding mwin(NewC->pubvar) also work?
Edit: Yes, I'm really that lazy.

### Hawkeye · 2009-12-12 07:59 · #K486746

**Whats up with Structs?**

Yeah basically Jakyboy, I was just wondering why that wasn't working. It's not really that big of deal (I am also a firm believer of data-hiding and encapsulation). I normally never have a use for public variable members anyways... bu was just wondering.
@Euix didn't you make a few RPGCode editors a while back?

### Euix · 2009-12-12 08:03 · #K486747

**Whats up with Structs?**

**Hawkeye wrote:**

> Didn't you make a few RPGCode editors a while back?
>

I have made quite a few, yes. I believe they have all been removed from the Files section due to being outdated and incompatible with recent breaking changes made with RPGCode.
Here is a short list:
- EuixCode
- EuixCode2
- VorteX 4
There may have been more, but that's all I remember of the editors I actually released. Right now I am working on repairing engine bugs, and pushing out an official bug-fix release.

### Euix · 2009-12-18 05:49 · #K487108

I am almost done fixing the bugs plaguing the current version of the engine, and I was wondering what the community thought about an idea I had for the next official release.
After this initial bug-fix release, I intended to dismantle the current graphics engine, and write a new hardware-accelerated engine from scratch, a graphics engine that supported:
- Hardware-accelerated rendering
- 32-bit RGBA graphics support
- Dynamic lighting
- Pixel Shading
- Ambient Lighting
... and a number of other features. The new graphics engine would be built off of a 3D graphics API; however, that does not mean the engine will support 3D graphics. This simply means that the TK would take advantage of modern graphics hardware, by simulating 2D graphics with ridiculously fast 3D rendering techniques.
The engine would benefit with increased frame rates, fast image rendering, alpha blending, and a number of other useful features. Through extensions to RPGCode, features like dynamic lighting could become possible, where game developers can control spot lights placed on a board; just imagine flickering lamp posts, moving spot-lights, and you'll get the picture.
I was planning on beginning work after I released the bug-fixes, but since jackyboy has covered the most important ones, should I wait until the new graphics engine is complete? To some people this post may not make any sense, but I am fairly certain that the current bugs aren't necessarily hampering development.
Let me know what you think! Please don't offer any suggestions in this topic; suggestions should be saved for another day.

### Euix · 2009-12-18 07:07 · #K487114

Honestly, I do not know why I even suggested that now... so, this topic is now open for graphics engine suggestions, at least. Sometimes I wonder if I should be sleeping instead of coming up with ridiculous ideas.
My initial thought was that I didn't really have much time, and waiting around to finish the bug-fix release, properly test the release, update the repository, and finally package the release would take up a considerable amount of time, and there would probably be bugs caused by other changes to the engine that wouldn't be discovered until people started hammering the engine.
Besides, some of these bug-fixes require proper changes, such as the thread speed bug. The engine needs a multitasking scheduler, not simply multiplying the amount of instruction units executed per frame, because that's ridiculously arbitrary and it doesn't scale well on older hardware.
Anyway, I am just going to release the bug-fixes and see how that goes; I have a lot of big plans for the engine, I just don't know if I have the time?

### Calacruf · 2009-12-18 08:59 · #K487116

**Euix wrote:**

> 32-bit RGBA graphics support
>

!!!!!!!!!!

### SuperIsoRPG · 2009-12-18 13:15 · #K487119

Yeah I agree. The graphics engine is seriously antiquated, and definitely is one of the major things that means big projects just don't get finished. Of course, it's fit for purpose in terms of doing old-school SNES style project, but I think people are a lot more ambitious now. It's also very good that you've got a clear way forward with it rather than just putting forward that it need s to be improved.
I'm thinking that good features would be a handling for board textures in the same vein as Age of Empires style games to compliment the existing features of tiles and images. I suppose this would also encompass integrated handling of water, which I think is another one of the tricky bits to handle in the bigger more ambitious projects. Anyway, best of luck.

> [!missing] gap:11-20 · http://toolkitzone.com/forum/viewtopic.php?t=44278&start=10 · never-captured
> Page 2 of 3 was not recovered.

### z3ro · 2009-12-21 00:11 · #K487267

**G_Dragon wrote:**

> How does making the engine linux friendly sound? Very Happy
>

I support this. I use both Linux and Windows 7, so it would be nice to start a project in one and have the possibility to pick it up in another, and to design it for both.

### SuperIsoRPG · 2009-12-21 01:19 · #K487269

I don't use TK but I do use and use Linux. It would open up another "market" if it were to be cross platform.

### cuthalion · 2009-12-21 02:19 · #K487272

Was it mostly the graphics engine that was preventing Linux compatibility?

### Euix · 2009-12-21 14:18 · #K487280

While cross-platform Toolkit 3 might sound awesome, the engine is nowhere near prepared to be ported to another operating system. There are Windows-specific functions and technologies used throughout the engine, in many places, and there would be a lot of refactoring required to swap those parts out with something more portable.
Basically, the graphics engine is the first step. The graphics engine is completely Windows dependent, as it relies mostly on GDI and DirectX.
Anyway, if you are going to post a suggestion, porting the engine to Linux should not be one of them. What functionality do you guys want that doesn't necessarily involve hundreds of hours of development, cross-compilation, and beta testing on multiple platforms?

### Occasionally_Correct · 2009-12-21 14:23 · #K487281

So much for not being a suggestion topic, eh? Razz

### cuthalion · 2009-12-21 20:16 · #K487295

Haha I was just wondering if it was a graphics engine problem or if it was the whole thing. Got my answer. But since I use Windows 99% of the time anyway... Razz
Simultaneous animations would be nice. Currently, you have to do it frame-by-frame (not hard, just annoying) using a buffer and such to get two anims going at the same time.

### UltimaWizard · 2009-12-25 04:20 · #K487420

**Bagel wrote:**

> I think it would be nice if the graphics engine was redone. That really hasn't been a priority in unofficial fixes so it would be a much needed upgrade.
>

I agree. Alpha blending alone would do so much for the TK.
