---
kind: forum-thread
id: "toolkitzone-forums/12598"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12598"
title: "How do I perform multiplication?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12598"
written: "2004-12-14T17:26:00"
last_post: "2004-12-14T23:19:00"
date_confidence: "exact"
captured: ["20041228072804"]
author: "Megiddo"
repliers: ["Z", "Caliber Mengsk", "Levi", "Colin", "Dont_Think_So"]
authors: ["Megiddo", "Z", "Caliber Mengsk", "Levi", "Colin", "Dont_Think_So"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139707_amp_", captured: "20041228072804", sha256: "836bbe2ecf289564621cdd5494188a0d0bc6ec3a46d9625a149f2ad7b14cdf33", wayback_url: "https://web.archive.org/web/20041228072804/http://www.toolkitzone.com/forums/viewtopic.php?p=139707&amp="}
links: []
---

# How do I perform multiplication?

### Megiddo · 2004-12-14 17:26 · #B139538

The program cannot tell multiplication apart from comments. What do I do? Both multiplication and comments use the * symbol.

### Z · 2004-12-14 19:53 · #B139582

I don't know if the toolkit supports multiplacation Sad but you have to ask Colin about that, but i don't think if it does it would ude * because that always signals a cooment,no matter what

### Caliber Mengsk · 2004-12-14 20:08 · #B139588

it is still the *. You just have to make sure it is between two numbers with a space between it and the numbers.
EXAMPLE:

**rpgcode:**

```
yourvar! = 56 * 32
```

That would be working correctly even if the RPGcode command on the site shows it wrong. just makesure you have the spaces there.
For comments (as to not mix up multiplication and comments) use a double slash. like this:
//
So, it would be something like:

**rpgcode:**

```
yourvar! = 56 * 32 //see ----- commented
```

EDIT:
Ok, isn't showing right on the site, but if you were to copy and paste it to the RPG code editor and move to another line, it would work right.

### Levi · 2004-12-14 21:18 · #B139622

Yeah, even in TK2 * worked for multiplication. And would try to multiply your comments if you had it after a variable declaration.
#a! = 2 * this is a comment
Would multiply 2 and this is a comment
#a$ = "Hello" *this is a comment
Would yield "Hellothis is a comment"
After things like
#show(a!) *comments work fine
It's only after you set a variable equal to something in TK2 that you didn't want the comment on the same line.

### Colin · 2004-12-14 22:31 · #B139690

Comments don't work like that in TK3, though.
function(x) * comment
Would call...
(function(x))->operator*(comment)
Which isn't likely what you intended.

### Dont_Think_So · 2004-12-14 23:19 · #B139707

The solution: use //.
