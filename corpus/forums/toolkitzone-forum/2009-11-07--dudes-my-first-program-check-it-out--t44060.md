---
kind: forum-thread
id: "toolkitzone-forum/44060"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "44060"
title: "Dudes, My first program -- check it out!"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=44060"
written: "2009-11-07T22:23:00"
last_post: "2009-11-11T22:59:00"
date_confidence: "exact"
captured: ["20100102024216"]
author: "Hallo1198"
repliers: ["playsoon", "cox470", "aurum34"]
authors: ["Hallo1198", "playsoon", "cox470", "aurum34"]
posts_present: 7
pages_present: [2]
pages_total: 2
posts_per_page: 10
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 10, url: "http://toolkitzone.com/forum/viewtopic.php?t=44060", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_484645", captured: "20100102024216", sha256: "34689f26405860c532e04b7eb0c5fcd0ec269176c69e47ee9d73188b73a8b98c", wayback_url: "https://web.archive.org/web/20100102024216/http://toolkitzone.com/forum/viewtopic.php?p=484645"}
links: []
---

# Dudes, My first program -- check it out!

> [!missing] gap:1-10 · http://toolkitzone.com/forum/viewtopic.php?t=44060 · never-captured
> Page 1 of 2 was not recovered.

### Hallo1198 · 2009-11-07 22:23 · #K484615

whoa thanks man. but the */ comments */ work pretty well, and are never misconcieved. the BYOND languag comments are like these, and apparently work in TKL3. Thanks so much for the feed beck on switches, I will implement them in version 1.2.0

### Hallo1198 · 2009-11-07 23:33 · #K484620

thanks jackyboy, but I just stated that i got lucky that the comments in BYOND are the same in TKL3. I never tried testing it like you said i must have. I just accidentally put it down, and it worked when I test ran it

### playsoon · 2009-11-08 13:39 · #K484645

I'm on Linux right now, so I can't test your program, but as I read it I noticed that you don't have a loop at the class selection part of the code. Meaning that whether or not I press a key between 1-8 the code is still going to continue on and skip the stats process.
You should put a while() or until() loop at the part of code for selecting a class so if another key other then 1-8 is pressed the program won't proceed to move on, instead it will ask the question repeatedly until 1-8 is pressed.
Or you could turn that part of code into a method. And if input does not equal the numbers 1-8 you have it call on the method to restart the choice process. This will also repeatedly ask the question until it's answered with one of the correct key presses.
Then it can move on to giving the stats and everything else.

### Hallo1198 · 2009-11-08 17:34 · #K484652

thanks playsoon, that's realy helpful. I will implement it soon. All of you are a great help to me Smile

### cox470 · 2009-11-10 19:36 · #K484875

Yeah it looks like something that'll get the job done.
I agree that the commentary as well as the "don't steal this"-disclaimers are very redundant and the code could be cleaned up a little but otherwise great work.
One thing that I can recommend for mwins and the closing thereof is to make only certain keys close the mwin. That way, the player doesn't close one by accident, with a directional key, for instance.
Also, you should check for spelling, Wink

### Hallo1198 · 2009-11-11 22:24 · #K484975

JUST changed the wait() function with the delay() function, incase the player skips over important points. delay()is SO COOL (just discovered it)
o.O

### aurum34 · 2009-11-11 22:59 · #K484977

i think it pauses the game when you use it on a thread, be aware of that
