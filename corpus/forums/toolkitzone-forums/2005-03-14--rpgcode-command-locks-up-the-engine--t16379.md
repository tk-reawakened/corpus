---
kind: forum-thread
id: "toolkitzone-forums/16379"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "16379"
title: "RPGCode command locks up the engine"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=16379"
written: "2005-03-14T15:40:00"
last_post: "2005-03-15T15:04:00"
date_confidence: "exact"
captured: ["20050325132129"]
author: "Akura_TheDragonBlader"
repliers: ["AlienDude", "Occasionally_Correct", "Colin"]
authors: ["Akura_TheDragonBlader", "AlienDude", "Occasionally_Correct", "Colin"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_180852_amp_", captured: "20050325132129", sha256: "df532e67d55765d1fd6b7a93bfdfe58fc715fa06f4b520bf9b853c1324b933b7", wayback_url: "https://web.archive.org/web/20050325132129/http://toolkitzone.com/forums/viewtopic.php?p=180852&amp="}
links: []
---

# RPGCode command locks up the engine

### Akura_TheDragonBlader · 2005-03-14 15:40 · #B180358

It was something I didn't see on the bug list, either. Unless what's in it has to do with anything:

**Code:**

```
Method ArraySwapLiteral(array$, index1!, index2!)

{

RPGCode("Local(tempholder$)="+array$+"["+index1!+"]$")

RPGCode(array$+"["+index1!+"]$="+array$+"["+index2!+"]$")

RPGCode(array$+"["+index2!+"]$=tempholder$")

}
```

It definately locks up when this method is called.

### AlienDude · 2005-03-14 16:56 · #B180381

Try this:

**Code:**

```
Method ArraySwapLiteral(array$, index1!, index2!)

{

RPGCode(tempholder$="+array$+"["+index1!+"]$")

RPGCode(array$+"["+index1!+"]$="+array$+"["+index2!+"]$")

RPGCode(array$+"["+index2!+"]$=tempholder$")

}
```

all vars declared in a method are local in nature.
they get deleted unless otherwise stated.
and i believe you can't assign Local(var) or GLobal(var) anything, you have to set thet up before you use it. i may be wrong on this.

### Occasionally_Correct · 2005-03-14 17:38 · #B180398

**Quote:**

> all vars declared in a method are local in nature.
>

Only the parameters are local to the method, and are destroyed when the method ends. Variables created in the method are set to whatever the default scope is (global is the toolkits default scope, but they should be local if you use #autolocal).
As for the locking up, I don't think it has to do with the RPGCode() command. This runs just fine:

**Code:**

```
RPGCode("show(62)")

RPGCode("wait()")
```

The method stops locking up Trans3 when you take out things like this:

**Code:**

```
"["+index1!+"]$"
```

In other words, when you stop mixing literal variables with numeric variables, it stops locking up. So just change that to something like this:

**Code:**

```
"[index1!]$"
```

The RPGCode() command handles the rest for you.

### Akura_TheDragonBlader · 2005-03-14 19:37 · #B180442

It works, except it seems to erase the second array value. I think it has to do with the first line. Can a Local() variable be assigned on the same line as it declared with the command?

### Occasionally_Correct · 2005-03-14 22:14 · #B180530

**Akura_TheDragonBlader wrote:**

> Can a Local() variable be assigned on the same line as it declared with the command?
>

Nope. Razz

### Colin · 2005-03-14 22:32 · #B180543

RPGCode() is not broken. Trust me.
Nonetheless, don't use it. There is not one time when it's needed. Think of one and I commend you!

### AlienDude · 2005-03-15 15:04 · #B180852

In this prog would you really NEED to encapsulate the lines inside this method in an RPGCode command, seeing as they really arent commands, just assignments? I will be attempting something similar in the future in an item/itembox management program im working on. That's why i am asking.
