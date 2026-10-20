---
kind: forum-thread
id: "toolkitzone-forums/12478"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12478"
title: "How do you call Global Variables?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12478"
written: "2004-12-11T22:07:00"
last_post: "2004-12-11T22:30:00"
date_confidence: "exact"
captured: ["20041227215000"]
author: "stanleywuu"
repliers: ["Dont_Think_So"]
authors: ["stanleywuu", "Dont_Think_So"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_138171_amp_", captured: "20041227215000", sha256: "da92376fe464b165ef6845fb134a0fe1fd760c6e28b3669440d1a0791c75080e", wayback_url: "https://web.archive.org/web/20041227215000/http://www.toolkitzone.com/forums/viewtopic.php?p=138171&amp="}
links: []
---

# How do you call Global Variables?

### stanleywuu · 2004-12-11 22:07 · #B138157

I have a program called "stats.prg"
and I did this

**Code:**

```
playerStatsGraph[0]$="polarboystats.jpg"
```

But how do I access it from another program??
I tried include and I don't think the program recognized it as a global variable, I think it actually thinks it's a new variable, so no pic showed up.

**Code:**

```
SetImage(playerStatsGraph[0]$,66,145,394,129)
```

Then I tried

**Code:**

```
msgbox(playerStatsGraph[0]$)
```

Nothing showed up either
Even the colour in the program editor didn't change
Why??

### Dont_Think_So · 2004-12-11 22:11 · #B138161

Including() a program doesn't run the code that's inside, it allows you to run any methods that the program may have to offer.
That being said, you will have to put the variables inside a method, then call the method in your start program. Variables are global by default, so you don't have to do anything after that.

### stanleywuu · 2004-12-11 22:30 · #B138171

Um...as long as I include that prg now, the game just exits as soon as every line in start.prg is excecuted
What's wrong?
EDIT: Weirder thing is, after I delete both include and the line that runs the method, it works fine, and then if I add the include line back, it still works,
But it still will NOT work after I run the method then DELETED the line that runs the method.
Got it, it seems like I forgot to add the brackets when I called the method
