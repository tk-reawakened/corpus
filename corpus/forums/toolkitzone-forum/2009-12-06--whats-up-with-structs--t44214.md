---
kind: forum-thread
id: "toolkitzone-forum/44214"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "44214"
title: "Whats up with Structs?"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=44214"
written: "2009-12-06T16:37:00"
last_post: "2009-12-12T08:03:00"
date_confidence: "exact"
captured: ["20100101210209"]
author: "Hawkeye"
repliers: ["Occasionally_Correct", "Euix", "cuthalion"]
authors: ["Hawkeye", "Occasionally_Correct", "Euix", "cuthalion"]
posts_present: 7
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_44214", captured: "20100101210209", sha256: "c02370c6cdeda7abdcfa7972f00be286a37a421fa40d167ee117a53353c5e2e6", wayback_url: "https://web.archive.org/web/20100101210209/http://toolkitzone.com/forum/viewtopic.php?t=44214"}
links:
  - {url: "http://en.wikipedia.org/wiki/Interface_%28computer_science%29", status: "external", local: null}
  - {url: "http://rpgtoolkit.cvs.sourceforge.net/viewvc/rpgtoolkit/vc/trans3/rpgcode/yacc.txt?revision=1.35&view=markup#l_735", status: "external", local: null}
---

# Whats up with Structs?

### Hawkeye · 2009-12-06 16:37 · #K486137

Uhm... so I am currently putting my UI system on hold to develop an OOP IDE in VB. So anyways... I never ever use structs, and I really had no idea what they were. So I figured I should still put them in my dev app, and I was wondering something...
Why is it that classes can't have public variables only private, yet structs can have either? And Colin said in another post that structs and classes were internally the same, except for their default scope... Anyone know?

### Occasionally_Correct · 2009-12-06 19:50 · #K486143

That's right. Classes and structs [are the same thing](http://rpgtoolkit.cvs.sourceforge.net/viewvc/rpgtoolkit/vc/trans3/rpgcode/yacc.txt?revision=1.35&view=markup#l_735), and the only difference is the default scope. I'm pretty sure structs were originally modeled after C structs (they didn't have methods), but it's been so long that I don't properly remember now. Razz
Classes can have public variables. It might have been an error in past versions, but it's fully allowed in 3.1.0.
An [interface](http://en.wikipedia.org/wiki/Interface_%28computer_science%29) keyword was added at the same time as classes and structs, but it was undocumented and no longer exists. (Just some trivia. Razz)

### Hawkeye · 2009-12-08 04:21 · #K486195

Hmm... well I've been doing some testing and it seems like structs can have public or private methods as well as a constructor (just saying since I didn't know... =P ) and pub/priv variables. However I can't seem to be able to create public variables when creating classes. It's not a huge deal as can just use functions to return data, but I was just wondering why this is.
And is there any work-arounds for the "include" statement completely messing up classes? (besides running the library at the beginning of the game and the running the start prg...) Thanks =)

### Euix · 2009-12-08 08:16 · #K486202

The reason you may not be able to create public variables within classes likely has to do with the developer's bias; in this case it was Colin. I am fairly certain that Colin held an unwavering belief that encapsulation was an inexcusable property of object-oriented programming; therefore he forced encapsulation on developers by disallowing public scope for variadic class members.
Basically, it's possible that Colin doesn't believe in public variables within class definitions; therefore, it is not allowed.
That may not be the case, but it certainly makes sense. The philosophy of encapsulation roughly describes that the internal implementation of a class should remain hidden from developers, because the implementation does not matter (explicitly), and developers should not rely on an implementation that may or may not change in the future; instead, developers should rely on the functionality and/or outcome of an object. Essentially, encapsulation preserves modularity and scalability, among other things.
Encapsulation is generally a good thing, and it's often called data hiding because it hides context-specific implementation details (members, implementation-specific functions, etc).
On the other side, structures are just user-defined data types, in the loosest sense. A data structure is an arbitrary grouping of data constructs; the data simply exists to be manipulated. Allowing scope on a data structure produces a side-effect that gives structures the ability to store and encapsulate state.
A very simple difference between structures and classes, is that structures cannot inherit from other structures; this is obvious because structures are not considered objects. Objects have intrinsic properties, and inherit qualities from other objects, and hold state. Structures hold and manipulate data.
It's not really that simplistic, but it helps in understanding the fundamental differences. Structures are meant for data manipulation, objects are stateful and maintain relationships; structures cannot inherit other classes, or implement interfaces, etc.

### cuthalion · 2009-12-08 16:51 · #K486225

Does adding mwin(NewC->pubvar) also work?
Edit: Yes, I'm really that lazy.

### Hawkeye · 2009-12-12 07:59 · #K486746

Yeah basically Jakyboy, I was just wondering why that wasn't working. It's not really that big of deal (I am also a firm believer of data-hiding and encapsulation). I normally never have a use for public variable members anyways... bu was just wondering.
@Euix didn't you make a few RPGCode editors a while back?

### Euix · 2009-12-12 08:03 · #K486747

**Hawkeye wrote:**

> Didn't you make a few RPGCode editors a while back?
>

I have made quite a few, yes. I believe they have all been removed from the Files section due to being outdated and incompatible with recent breaking changes made with RPGCode.
Here is a short list:
- EuixCode
- EuixCode2
- VorteX 4
There may have been more, but that's all I remember of the editors I actually released. Right now I am working on repairing engine bugs, and pushing out an official bug-fix release.
