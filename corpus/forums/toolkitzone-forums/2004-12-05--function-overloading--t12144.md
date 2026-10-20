---
kind: forum-thread
id: "toolkitzone-forums/12144"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "12144"
title: "Function Overloading"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12144"
written: "2004-12-05T01:40:00"
last_post: "2004-12-06T05:22:00"
date_confidence: "exact"
captured: ["20050115140658"]
author: "Colin"
repliers: ["Dont_Think_So", "Compugeek", "Koh Wei Zane", "Levi", "Occasionally_Correct"]
authors: ["Colin", "Dont_Think_So", "Compugeek", "Koh Wei Zane", "Levi", "Occasionally_Correct"]
posts_present: 9
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135418_amp_", captured: "20050115140658", sha256: "fef16bbec9207642e80dfa680c6d0916e4da3f770560403de1088e7a45ae2bbb", wayback_url: "https://web.archive.org/web/20050115140658/http://www.toolkitzone.com/forums/viewtopic.php?p=135418&amp="}
links: []
---

# Function Overloading

### Colin · 2004-12-05 01:40 · #B134774

**Code:**

```
method test(x$) {mwin("hello: " + x$)}

method test(x!) {mwin("hello: " + CastLit(x! * 2))}

method test() {mwin("hello, world!")}

test("here!") // Shows "hello: here!"

test(5)     // Shows "hello: 10"

test()     // Shows "hello, world!"

wait()

mwincls()
```

This allows you to have methods that have the same name but different parameter lists - far superior to default values. I'll see what I can do about that '...' thing, DTS, but this isn't bad Razz

### Dont_Think_So · 2004-12-05 02:02 · #B134780

Yes! I assume you've uploaded the new binary Smile
<Edit> Hey, Colin, is your system time set to 2002? Razz

### Colin · 2004-12-05 02:51 · #B134797

It's the only way I can keep using my Office 2003 Beta Smile

### Dont_Think_So · 2004-12-05 02:59 · #B134800

Heh, I personally prefer Open Office, mainly because it's free and you don't have to resort to cheap tricks to keep using it Razz
But that's off-topic Smile

### Compugeek · 2004-12-05 04:49 · #B134845

**Colin wrote:**

> It's the only way I can keep using my Office 2003 Beta Smile
>

So does this mean that I can do the same with VB Express and/or my Office 2k3 trial? Only Microsoft would leave a loophole that obvious Rolling Eyes
To stay on topic, nice job! Wink

### Koh Wei Zane · 2004-12-05 05:37 · #B134860

Norton left that bug out too.

### Levi · 2004-12-05 06:48 · #B134942

Most have...Others who didn't you simply need to keep the clock from changing from when you load it so that it doesn't get suspicious. Which is very hard to do sometimes.
Indeed function overloading would be nice to have. Never had a use for it myself seeing as how each function has a specific name for a specific task, and I tend to make them long and descriptive. Lots of typing but no confusion. But I know many who would love to have this. Indeed, wonderful job.

### Occasionally_Correct · 2004-12-05 13:52 · #B135048

Hurrah!
I can now have my optional parameters. Razz

### Colin · 2004-12-06 05:22 · #B135418

In order to further enhance function overloading (and just functions in genreal), I've added the ability for your function parameters to specifiy the type of object they want. Like so:

**Code:**

```
class COne

{

public:

   method one() {mwin("In COne")}

}

class CTwo

{

public:

   method two() {mwin("In CTwo")}

}

class CThree: CTwo

{

   // Empty derived class (just for testing - you

   // won't typically make empty classes)

}

class CFour: CThree

{

   // Another empty derived class

}

method test(COne x) {x->one()}

method test(CTwo x) {x->two()}

p = COne()

t = CTwo()

j = CThree()

f = CFour()

test(p) // Shows "In COne"

test(t) // Shows "In CTwo"

test(j) // Shows "In CTwo"

test(f) // Shows "In CTwo"

p->release()

t->release()

j->release()

f->release()

wait()

mwincls()
```
