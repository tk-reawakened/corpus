---
kind: forum-thread
id: "toolkitzone-forums/24065"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Computing &amp; Technology"
skin: "phpbb2"
thread_id: "24065"
title: "Flash question"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=24065"
written: "2005-10-04T20:00:00"
last_post: "2005-10-07T22:13:00"
date_confidence: "exact"
captured: ["20060111131835"]
author: "Tao-Kun"
repliers: ["Serge", "zzz", "SidZero", "Cypher"]
authors: ["Tao-Kun", "Serge", "zzz", "SidZero", "Cypher"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_263188_amp_3Bsid_4324174f595c7258485ba558b2f120f0", captured: "20060111131835", sha256: "38241b050faca68baad5d43726ed8466a0611ea8834d29d627445ad5f37252b3", wayback_url: "https://web.archive.org/web/20060111131835/http://www.toolkitzone.com/forums/viewtopic.php?p=263188&amp%3Bsid=4324174f595c7258485ba558b2f120f0"}
links:
  - {url: "http://www.flashkit.com", status: "external", local: null}
---

# Flash question

### Tao-Kun · 2005-10-04 20:00 · #B262395

By any chance, does anyone know how to get flash to increase or decrease a varible? I deicded to ask rather then going and beign learning the basic of flash.

### Serge · 2005-10-05 12:56 · #B262620

define the variable...
flashvariable=0;
then after the variable is defined...
flashvariable++;
or
flashvariable += 1;
or
flashvariable = flashvariable + 1;
all the same

### zzz · 2005-10-05 18:34 · #B262665

Any variable in any language acts virtualy in the same way Wink

### Tao-Kun · 2005-10-05 20:01 · #B262673

That brings me to two more questions:
Is it possible to get the value palced in the flashvalue and assign it to a toolkit vairble?
And how do I display the numeral varible in the flash movie?

### SidZero · 2005-10-07 03:30 · #B263056

**Tao-Kun wrote:**

> Is it possible to get the value palced in the flashvalue and assign it to a toolkit vairble?
> And how do I display the numeral varible in the flash movie?
>

As far as your first question, the only way I can think of to make an integrated Flash-Toolkit program is if they both manipulate a common outside file. I don't know if the toolkit can do this, but I'm positive that Flash can.
As far as your second question, just assign whatever numeric falue you want to display to a variable and set a dynamic text field to display the contents of that variable.
If you don't know how to do things, I would suggest poking around on [flashkit](http://www.flashkit.com), as they have all kinds of tutorials for all kinds of stuff.

### Cypher · 2005-10-07 22:13 · #B263188

**Tao-Kun wrote:**

> Is it possible to get the value palced in the flashvalue and assign it to a toolkit vairble?
>

Write a plugin like Triuky did Rolling Eyes
