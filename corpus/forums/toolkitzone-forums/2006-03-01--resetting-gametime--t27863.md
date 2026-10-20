---
kind: forum-thread
id: "toolkitzone-forums/27863"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "27863"
title: "Resetting Gametime..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27863"
written: "2006-03-01T02:51:00"
last_post: "2006-03-03T03:44:00"
date_confidence: "exact"
captured: ["20060320120704"]
author: "DrJ"
repliers: ["legomaster88", "zyrshnikashnu", "Dont_Think_So", "p90m16mp5a4"]
authors: ["DrJ", "legomaster88", "zyrshnikashnu", "Dont_Think_So", "p90m16mp5a4"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_302760_amp_3Bsid_c84d9a2fd42b977a29471d0321c5e164", captured: "20060320120704", sha256: "7ade0ae11a4a7eb4b0a7666454524b8bb95e2674d2b437796d8a865acf969ba4", wayback_url: "https://web.archive.org/web/20060320120704/http://toolkitzone.com/forums/viewtopic.php?p=302760&amp%3Bsid=c84d9a2fd42b977a29471d0321c5e164"}
links: []
---

# Resetting Gametime...

### DrJ · 2006-03-01 02:51 · #B302446

Is it possible to reset the game time?

### legomaster88 · 2006-03-01 15:05 · #B302526

try something to the effect of gametime1! = gametime! - gametime!
then whenever you want to show the gametime, use gametime1!.

### zyrshnikashnu · 2006-03-01 21:31 · #B302595

Why bother?
Legomaster, do you realize that "gametime!-gametime!" is zero? There's no point in performing the operation.
DrJ:
If you need some sort of reference time, just place something like "startGame! = gametime!" at the beginning of your game. From then on, find how many seconds have elapsed since the start by using "elapsed! = gametime!-startGame!".

### DrJ · 2006-03-02 03:33 · #B302717

I need to reset it though! Besides at the begining of the game gametime!=0. So all that code would do is find gametime!

### Dont_Think_So · 2006-03-02 05:30 · #B302758

Why do you need to reset it?

### DrJ · 2006-03-02 05:36 · #B302760

Im trying to make a realtime clock and after a day in the game I want to reset game time, so that I can restart gametime! for each day...

### zyrshnikashnu · 2006-03-02 21:28 · #B302821

Again, you can just use an index time. There's nothing special about a gametime! value of 0. To find out how much time has passed in the current day, you'd use the elapsed time junk I already showed you.

### p90m16mp5a4 · 2006-03-03 03:44 · #B302969

Then simply subtract a number in the clock area to show the gametime. This won't work with the default MS, and using #SetConstants on gametime! wont work either. So instead of showing GameTime!, show GameTime-time!
