---
kind: forum-thread
id: "toolkitzone-forums/23561"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Newbie Haven"
skin: "phpbb2"
thread_id: "23561"
title: "GET ITEMS OFF BOARD"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23561"
written: "2005-09-16T14:23:00"
last_post: "2005-09-19T14:10:00"
date_confidence: "exact"
captured: ["20060112140722"]
author: "kyle_cliffe"
repliers: ["Phalanxia", "Scott92002000", "ahriman"]
authors: ["kyle_cliffe", "Phalanxia", "Scott92002000", "ahriman"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_258513_amp_3Bsid_44c3971f221152c0fd4b3b8b39ccf396", captured: "20060112140722", sha256: "bef8c0ece2b4744eddeaca4ad27cd8e123088fe35dc33060e2fe24b28cf94d07", wayback_url: "https://web.archive.org/web/20060112140722/http://www.toolkitzone.com/forums/viewtopic.php?p=258513&amp%3Bsid=44c3971f221152c0fd4b3b8b39ccf396"}
links: []
---

# GET ITEMS OFF BOARD

### kyle_cliffe · 2005-09-16 14:23 · #B257734

hi people ive put an item on the board which is a boss & set it to conditional & not always active but the character jus walks slowly throught it & then stops how do u use the erase item command because i no u need the item num but i dont think it worked, or maybe a put the rong num.can sum1 tell me how u find the number cause iam not sure its the rite one

### Phalanxia · 2005-09-16 14:47 · #B257745

First things first: use proper grammar and spelling so we can actually read it. Nothing annoys me more than having to read a long paragraph with loads of spelling mistakes just because the authour was too lazy.

### kyle_cliffe · 2005-09-16 17:58 · #B257793

ok its just iam used to writing like that

### Scott92002000 · 2005-09-16 20:38 · #B257847

**kyle_cliffe wrote:**

> can sum1 tell me how u find the number cause iam not sure its the rite one
>

step 1: open board with item
step 2: click on the RPG Code button
step 3: click "item menu"
step 4: find the item you want and write down the item number

### kyle_cliffe · 2005-09-17 06:05 · #B257964

ok thanks.do you have to write the word item or just the number

### Scott92002000 · 2005-09-17 20:27 · #B258109

the proper code for erasing an item is:

**Code:**

```
//this destroys item #1

DestroyItem(1)
```

### kyle_cliffe · 2005-09-18 08:01 · #B258237

ok thanks.i put the amount of times the item can be used on board as conditional variable which is using it once, but when that happenes,after the item dissapears the character cant walk throught the tile or he walks through the tile very slowley

### ahriman · 2005-09-19 14:10 · #B258513

**kyle_cliffe wrote:**

> ok thanks.i put the amount of times the item can be used on board as conditional variable which is using it once, but when that happenes,after the item dissapears the character cant walk throught the tile or he walks through the tile very slowley
>

That happens to me. That's why I don't use items in cutscenes. I add a new character, move it around as needed, and at the end of the program, I remove him from the party.(delete him, and then erase him.)
