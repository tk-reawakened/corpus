---
kind: forum-thread
id: "toolkitzone-forums/10421"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "10421"
title: "Moving on: Arrays and Objects"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10421"
written: "2004-10-20T23:34:00"
last_post: "2004-10-21T03:41:00"
date_confidence: "exact"
captured: ["20041226085655"]
author: "Serge"
repliers: ["Zap!", "Colin"]
authors: ["Serge", "Zap!", "Colin"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_114215_amp_", captured: "20041226085655", sha256: "3bce6271dc39c34283b103dd2d96361146cebaec0ded564e7131a59197fdefae", wayback_url: "https://web.archive.org/web/20041226085655/http://www.toolkitzone.com/forums/viewtopic.php?p=114215&amp="}
links: []
---

# Moving on: Arrays and Objects

### Serge · 2004-10-20 23:34 · #B113971

I'm trying to create an array that contains a bunch of objects, and edit them during gameplay.
Simplified, what I'm doing is something like this:

**Code:**

```
// at beginning of code

int arrayMax = 100;

int objectNum = 0;

ClassA objectArray[arrayMax];

// later on (this is where my program crashes)

objectNum++; // signifies there is a new object being created

objectArray[objectNum].function(someParameter);
```

Whenever I run it, it crashes, but I don't get an error when compiling.
I know I'm doing something wrong with the way I'm trying to use the array of objects, could someone explain it?

### Zap! · 2004-10-20 23:53 · #B113988

(this is a useless post by me now..... it wasnt a few minutes ago though!)

### Colin · 2004-10-21 00:55 · #B114062

You don't quite understand memory...

**Code:**

```
CSomeClass* x = new(CSomeClass[5]); // 5 CSomeClasses

// access those suckers, like so:

x[3].blah ...;

// make the array a thing of the past

delete [] x;
```

Edit: The reason it crashes - might I add - is because you can't make 'concrete' object arrays with non-constant upper bounds.

### Serge · 2004-10-21 01:21 · #B114085

**Quote:**

> But...I dont know do you use the Bullet function anywhere before this in the program?
>

Typo when putting on forum, sorry Razz fixed it.

### Colin · 2004-10-21 03:41 · #B114215

An update for you peeps, we've fixed the problem.
