---
kind: forum-thread
id: "toolkitzone-forums/12314"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12314"
title: "A few of questions"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12314"
written: "2004-12-08T07:40:00"
last_post: "2004-12-11T02:03:00"
date_confidence: "exact"
captured: ["20041227215226"]
author: "Zio"
repliers: ["Dont_Think_So", "solaceinsilence", "Colin"]
authors: ["Zio", "Dont_Think_So", "solaceinsilence", "Colin"]
posts_present: 9
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_137782_amp_", captured: "20041227215226", sha256: "5b3fe81e3a3aef9505e51984ddd2c1ef5243e78a57d8e813354d6f0856050889", wayback_url: "https://web.archive.org/web/20041227215226/http://www.toolkitzone.com/forums/viewtopic.php?p=137782&amp="}
links: []
---

# A few of questions

### Zio · 2004-12-08 07:40 · #B136418

Question 1)
Will this work for displaying pics #setImage("pic<var!>.bmp",0,0,0,0) ?
Question 2)
Why, When i test run a program it runs fine, but when i test run the game
with the program threading it ignores the if commands?
Question 3)
Why does the transperent color on an image turn black when it's on a
board and is there a way around this?

### Dont_Think_So · 2004-12-08 22:29 · #B136619

1) No, you will have to do this:
#setimage("Pic" + Castlit(Var!) + ".bmp",0,0,0,0)
Var! is numerical, so you need to change it to literal before puting it in a string ("CastLit" does that). Also, < and > don't work in anything except MWin and Text.
2) That's a glitch in TK3.0.4. It has been fixed for the next release.
3) Another glitch in TK3.0.4. While this has also been fixed, an easy way to get around this is use 1,1,1 for black, then 0,0,0 for transparent. The difference is so small that you won't notice the difference.

### solaceinsilence · 2004-12-08 23:58 · #B136681

to build upon the anwser to the first question you have to assign what the name of the image is you want to the variable. look at this code

**rpgcode:**

```
var$ = myfilename.filetype

setImage("var$", 0, 0, 0, 0)
```

Like dont_think_so said, the variable you had was numerical (!) so we need to change it to a literal ($) variable. Literal is basically the same thing as a string. As you see from my code i assigned the file to the literal variable then "called" it in the #setImage() command. I hope that is what you where aiming to do. Smile

### Dont_Think_So · 2004-12-09 03:52 · #B136844

Also remember that you can't include variables in quotes and expect them to work Smile

### Zio · 2004-12-09 18:24 · #B137024

Ok thanks people.... i cast the number to a lit once in a test but it didn't work either... i guess i just gotta wait for the next version to come out until then i can hope my code is actually correct... ok now i'll work on some new prgs

### Dont_Think_So · 2004-12-09 22:26 · #B137118

CastLit works in the current version of the TK.

### Zio · 2004-12-11 00:03 · #B137742

Ok, I tried this just to test out what you said

**Code:**

```
If(x! < 50)

     {

          x!++

          HPpic$="hpbar inner"+CastLit(x!)+".bmp"

          SetImage(HPpic$,0,0,56,17)

          MWin("x = <x!>")

          MWin("HPpic = <HPpic$>")

          Wait()

     }
```

but it still doesn't work....can some one tell me what i'm doing wrong or if this just won't work.

### Colin · 2004-12-11 00:36 · #B137757

You need some spaces:
"" + CastLit(...) + ""
etc.
3.05 givs you more options where you put spaces.

### Zio · 2004-12-11 02:03 · #B137782

Thanks i figured it was something stupid...now to shorten down lots of code
