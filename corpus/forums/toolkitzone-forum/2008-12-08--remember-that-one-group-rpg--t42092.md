---
kind: forum-thread
id: "toolkitzone-forum/42092"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "42092"
title: "Remember that one group RPG?"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=42092"
written: "2008-12-08T01:05:00"
last_post: "2008-12-19T03:36:00"
date_confidence: "exact"
captured: ["20081220004257", "20081220004451", "20081223014314", "20081223014425", "20081223014650"]
author: "Valence"
repliers: ["Euix", "seveneternal", "Montai", "Occasionally_Correct", "cuthalion", "k-hos", "Lotusware"]
authors: ["Valence", "Euix", "seveneternal", "Montai", "Occasionally_Correct", "cuthalion", "k-hos", "Lotusware"]
posts_present: 16
pages_present: [1]
pages_total: 7
posts_per_page: 10
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 2, start: 11, end: 20, url: "http://toolkitzone.com/forum/viewtopic.php?t=42092&start=10", reason: "never-captured"}
  - {page: 3, start: 21, end: 30, url: "http://toolkitzone.com/forum/viewtopic.php?t=42092&start=20", reason: "never-captured"}
  - {page: 4, start: 31, end: 40, url: "http://toolkitzone.com/forum/viewtopic.php?t=42092&start=30", reason: "never-captured"}
  - {page: 5, start: 41, end: 50, url: "http://toolkitzone.com/forum/viewtopic.php?t=42092&start=40", reason: "never-captured"}
  - {page: 6, start: 51, end: 60, url: "http://toolkitzone.com/forum/viewtopic.php?t=42092&start=50", reason: "never-captured"}
  - {page: 7, start: 61, end: 70, url: "http://toolkitzone.com/forum/viewtopic.php?t=42092&start=60", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_461842", captured: "20081220004257", sha256: "a9875f2d13830883cca9dd94c1a8002f3c9d7009592a459d343e1a7e33822a88", wayback_url: "https://web.archive.org/web/20081220004257/http://www.toolkitzone.com/forum/viewtopic.php?p=461842"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_461852", captured: "20081220004451", sha256: "cc9dc5703058c74cb8e699839c9d0753cef63877086895d15f6cbb09f66c939f", wayback_url: "https://web.archive.org/web/20081220004451/http://www.toolkitzone.com/forum/viewtopic.php?p=461852"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_42092", captured: "20081223014314", sha256: "bf3dfb20522e6ced85c0afa3286aaa06456d84b45d6350cbe0923cfa468b6021", wayback_url: "https://web.archive.org/web/20081223014314/http://www.toolkitzone.com/forum/viewtopic.php?t=42092"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_42227", captured: "20081223014425", sha256: "dd94b6b7df5bf4c71a6fdbb710112780fb0cfd6f9e7003a7352746437463e8e4", wayback_url: "https://web.archive.org/web/20081223014425/http://www.toolkitzone.com/forum/viewtopic.php?t=42227"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_42230", captured: "20081223014650", sha256: "a645a4a9bf9f2024ec262bfc24edfaf1191cfbd9b0d4ad0bce08f7177627e43b", wayback_url: "https://web.archive.org/web/20081223014650/http://www.toolkitzone.com/forum/viewtopic.php?t=42230"}
links:
  - {url: "http://www.toolkitzone.com/vault/stuff/14598_problimz.jpg", status: "never-captured", local: null}
  - {url: "http://www.toolkitzone.com/vault/stuff/39_Frap%20I%27oh.JPG", status: "never-captured", local: null}
  - {url: "http://www.toolkitzone.com/vault/stuff/39_i%27oh%20menu.jpg", status: "never-captured", local: null}
---

# Remember that one group RPG?

### Valence · 2008-12-18 05:44 · #K461762

**Help appreciated**

Edit: I'm an idiot Smile I solved my first problem, I need another set of "", for the last type().
Not quite sure what's wrong here. The function type stuff is my mwin; t The problem is probably in the if()'s.
I get the first error for some reason, not sure why. When I run out of money, I continue to buy the item, and have -GP. I have other copies of this program, only with different items, and some work perfectly. The rest have this problem. I don't quite understand why since, it's basically the same thing, only with different prices/items.Sad
![](http://www.toolkitzone.com/vault/stuff/14598_problimz.jpg)

**Code:**

```
function type(profile, line1, line2, line3, line4)

{

// ok put the image you want here

setImage("bmwin.png", 0, 0, 360, 64)

setImage(profile, 3, 3, 61, 61)

pixelText(65, 3, line1)

pixelText(65, 17, line2)

pixelText(65, 32, line3)

pixelText(65, 45, line4)

wait() // you can take this out if you want

}

// remove this line when your done testing it :D

type("virtual.png", "Virltual clerk:","Welcome.","What can I do for you?","")

mwincls()

wait(a$)

type("virtual.png", "1. = Blue sour skittle... 200","2. = Exit","","")

mwincls()

wait(a$)

a! = wait();

If (a! == 1)

{

getGP(am!)

If ( am! < 200)

{

type("virtual.png", "Virltual clerk:","You don't appear to have sufficient funding.","Sorry, I cannot accept Pokemon cards.")

wait();

mwincls();

}

else

{

giveItem("blue sour skittle.itm")

takegp(200)

type("virtual.png", "Virltual clerk:","Here you go .","Thank you, and come again.","")

wait();

mwincls();

push("S")

}

}

If (a! == 2)

{

type("virtual.png", "Virltual clerk:","We hope you visit us","again, in the near future.")

wait();

mwincls();

push("S")

}
```

Razz Razz

### Euix · 2008-12-18 06:10 · #K461765

**Help appreciated**

You are calling type() with four parameters when by definition it requires five. Specifically, the error occurs on line 45 as is stated by the translator. You made this mistake multiple times.

**Code:**

```
function type(string, string, string, string, string)
```

Please remove the type suffixes (!/$) from your variables, they are no longer required because of type inference. Also, you may want to do something like this:

**Code:**

```
 result = Wait();

switch (result) {

 case 1: {

  am = GetGp();

  if (am >= 200) {

   // Give item.

   // Take gold.

  } else {

   // Do not give item.

  }

 }

 // ...

}
```

### Valence · 2008-12-18 06:19 · #K461767

**Help appreciated**

**Euix wrote:**

> You are calling type() with four parameters when by definition it requires five. Specifically, the error occurs on line 45 as is stated by the translator.
>
> **Code:**
>
> ```
> function type(string, string, string, string, string)
> ```
>
> Please remove the type suffixes (!/$) from your variables, they are no longer required because of type inference. Also, you may want to do something like this:
>
> **Code:**
>
> ```
>  result = Wait();
>
>
> switch (result) {
>
>
>  case 1: {
>
>
>   am = GetGp();
>
>
>   if (am >= 200) {
>
>
>    // Give item.
>
>
>    // Take gold.
>
>
>   } else {
>
>
>    // Do not give item.
>
>
>   }
>
>
>  }
>
>
>  // ...
>
>
> }
> ```
>

Yeah, I realized that I messed up with parameters. Thanks, It's all fixed now. I can't reproduce the -GP thing again, so I will assume it will no longer happen. I'm kinda used to using !/$, since I coded a bit in 3.06, and haven't really done anything but play around with the board editor, and drawing until a few weeks ago.

### seveneternal · 2008-12-18 19:46 · #K461793

Montai was in it, and Horizon did some graphics.
Remember that?
.......

### Montai · 2008-12-18 20:03 · #K461794

Jewel of Destiny: Quest for I'oh? I still have all the files for that game. Razz

### Montai · 2008-12-18 20:36 · #K461798

Main menu skin:
![](http://www.toolkitzone.com/vault/stuff/39_i%27oh%20menu.jpg)
and my take on frap: <http://www.toolkitzone.com/vault/stuff/39_Frap%20I%27oh.JPG>
Shit, I might use this skin Razz Nah...

### Occasionally_Correct · 2008-12-18 21:04 · #K461801

I was a part of this. We had a private forum.

### cuthalion · 2008-12-18 21:48 · #K461811

**Occasionally_Correct wrote:**

> I was a part of this. We had a private forum.
>

Élitists.

### k-hos · 2008-12-19 01:58 · #K461837

**Outstanding Toolkit Contribution**

grats' dude
you deserve it!

### Montai · 2008-12-19 02:13 · #K461842

**TK Game Boy wrote:**

> ...
> That's not Frap. Confused
>

Back then, when that project was active, it was Frap. TKGB, I had a horribly drawn profile pic, and a horrible sprite to go off of. Get real....
EDIT: For the record, I was doing the Menu, Srites and tiles.......

### Lotusware · 2008-12-19 02:21 · #K461844

**Outstanding Toolkit Contribution**

jackybaby! wooo!

### seveneternal · 2008-12-19 03:36 · #K461852

**Outstanding Toolkit Contribution**

Woo. Congrats, jackyboy. Very Happy
.......

### Lotusware · 2008-12-08 01:05 · #K460085

**TK All Nighter - 27th of December**

Hello Asimir.
Group 1
(redacted: email)

### Lotusware · 2008-12-08 01:23 · #K460090

**TK All Nighter - 27th of December**

as long as everyone has fun thats all that matters

### k-hos · 2008-12-08 01:51 · #K460100

**TK All Nighter - 27th of December**

Group 1 so I can bug juice :3
(redacted: email)

### seveneternal · 2008-12-08 01:55 · #K460103

**TK All Nighter - 27th of December**

Group one please!
(redacted: email)
I think we should just have one large group. It probably won't be too crowded after taking into account the no-shows and the non-talkers.
.......

> [!missing] gap:11-20 · http://toolkitzone.com/forum/viewtopic.php?t=42092&start=10 · never-captured
> Page 2 of 7 was not recovered.

> [!missing] gap:21-30 · http://toolkitzone.com/forum/viewtopic.php?t=42092&start=20 · never-captured
> Page 3 of 7 was not recovered.

> [!missing] gap:31-40 · http://toolkitzone.com/forum/viewtopic.php?t=42092&start=30 · never-captured
> Page 4 of 7 was not recovered.

> [!missing] gap:41-50 · http://toolkitzone.com/forum/viewtopic.php?t=42092&start=40 · never-captured
> Page 5 of 7 was not recovered.

> [!missing] gap:51-60 · http://toolkitzone.com/forum/viewtopic.php?t=42092&start=50 · never-captured
> Page 6 of 7 was not recovered.

> [!missing] gap:61-70 · http://toolkitzone.com/forum/viewtopic.php?t=42092&start=60 · never-captured
> Page 7 of 7 was not recovered.
