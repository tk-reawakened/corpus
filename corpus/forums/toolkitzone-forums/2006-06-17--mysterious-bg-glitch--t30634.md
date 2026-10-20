---
kind: forum-thread
id: "toolkitzone-forums/30634"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "30634"
title: "Mysterious BG Glitch..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=30634"
written: "2006-06-17T02:25:00"
last_post: "2006-06-20T05:35:00"
date_confidence: "exact"
captured: ["20060629082932"]
author: "UltimaWizard"
repliers: ["Colin", "Khin", "SuperIsoRPG", "Maria", "Bad Kids", "RayIsMe"]
authors: ["UltimaWizard", "Colin", "Khin", "SuperIsoRPG", "Maria", "Bad Kids", "RayIsMe"]
posts_present: 15
pages_present: [1]
pages_total: 3
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 2, start: 16, end: 30, url: "http://toolkitzone.com/forums/viewtopic.php?t=30634&start=15", reason: "never-captured"}
  - {page: 3, start: 31, end: 45, url: "http://toolkitzone.com/forums/viewtopic.php?t=30634&start=30", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_328940_amp_3Bsid_497143305248e29d431accf0730516d1", captured: "20060629082932", sha256: "474015828bcb280dc8badf34321d7bb7b23d570c91fecdc7c48a739d6bc69435", wayback_url: "https://web.archive.org/web/20060629082932/http://www.toolkitzone.com/forums/viewtopic.php?p=328940&amp%3Bsid=497143305248e29d431accf0730516d1"}
links:
  - {url: "http://tk3.toolkitzone.com/bugs/", status: "captured", local: "wayback/toolkitzone.com/tk3.toolkitzone.com/bugs/index"}
  - {url: "http://www.toolkitzone.com/index.php?id=46", status: "captured", local: "wayback/toolkitzone.com/index.php__id_46"}
  - {url: "http://www.toolkitzone.com/stuff/files/5278/Debug%20Screenie%201.png", status: "never-captured", local: null}
  - {url: "http://www.toolkitzone.com/stuff/files/5278/Debug%20Screenie%202.png", status: "never-captured", local: null}
---

# Mysterious BG Glitch...

### UltimaWizard · 2006-06-17 02:25 · #B328338

I've found...aah...a mysterious background glitch that I wouldn't have thought would happen.
The background in the following shot is a 640x832 256-color .png image rendered in Blender. The resolution for the game I'm testing it in, Ander's Journey, is 640x480. I rendered the board to be larger than the resolution on the y-axis so that the player would be able to walk along it. Here's the board:
![](http://www.toolkitzone.com/stuff/files/5278/Debug%20Screenie%201.png)
...however, when I take one step down to the part of the board that would constitute the bottom of the board, this happens:
![](http://www.toolkitzone.com/stuff/files/5278/Debug%20Screenie%202.png)
Is this a known TK bug, or what's going on with this?

### Colin · 2006-06-17 03:32 · #B328355

<http://tk3.toolkitzone.com/bugs/> ("board backgrounds disappear sometimes")
If you find an problem, there's a good chance it has been found before. Check the bug list.

### Khin · 2006-06-17 10:18 · #B328397

Oh I see you weren't around when we were pummeled with complaints about H:F boards "turning to white or black". Wink
Caliber Mengsk has an unofficial bugfix for this. Go bug him about it.

### SuperIsoRPG · 2006-06-17 14:38 · #B328430

Dangit! i've just run into this bug to. Where is the bugfix?

### UltimaWizard · 2006-06-17 18:22 · #B328468

Must be Caliber Mengsk's Trans3 rewrite. Razz
Thanks for the info, all.

### Colin · 2006-06-17 19:25 · #B328486

I'm pretty sure Caliber Mengsk did not rewrite tk3. I was convinced it was Delano and I who were doing that.

### Maria · 2006-06-18 04:52 · #B328583

**UltimaWizard wrote:**

> Must be Caliber Mengsk's Trans3 rewrite. Razz
> Thanks for the info, all.
>

**Colin wrote:**

> I'm pretty sure Caliber Mengsk did not rewrite tk3. I was convinced it was Delano and I who were doing that.
>

learn to read colin

### Bad Kids · 2006-06-18 05:14 · #B328596

not smart to tell colin how to read... Wink but than again surrival of the smartest.

### Colin · 2006-06-18 05:15 · #B328599

He didn't rewrite trans3 either. He uncommented three lines in it. I can see how this would be confused with actual work (e.g. a rewrite). I'll be sure to clarify my sarcastic replies in the future.

### Maria · 2006-06-18 05:16 · #B328600

a patch. thats good enough for me lol

### UltimaWizard · 2006-06-19 15:29 · #B328894

Ok, then...so where is it that I may find this patch?

### Maria · 2006-06-19 16:20 · #B328896

<http://www.toolkitzone.com/index.php?id=46>

### UltimaWizard · 2006-06-19 20:39 · #B328940

Alrighty.
@TK admins: you should definently add portions of this topic to the Sticky topic at the top so that until that mysterious date you release TK3.0.7 rolls around, you won't have to worry too much about referencing the buglist and CM's Trans3 patch. Smile
Or you could let me help beta-test 3.0.7. Wink

### RayIsMe · 2006-06-20 05:22 · #B329083

**Colin wrote:**

> Evil or Very Mad I can see how this would be confused with actual work... Evil or Very Mad
>

Yes, commenting out three lines of code doesn't seem like a huge change. But, tracking down those three lines of code in the hundreds that comprise trans3.exe is something that I consider "work".
It wasn't a walk in the park, anyway...

### Colin · 2006-06-20 05:35 · #B329085

To be fair, I believe Delano knew why it wasn't working, as evidenced by his comments about the lines that he commented. He had a reason for a commenting them, I'm sure, and it's explained in his comment above them. Whether he still swears by that comment, I do not know, but it was indeed documented.

> [!missing] gap:16-30 · http://toolkitzone.com/forums/viewtopic.php?t=30634&start=15 · never-captured
> Page 2 of 3 was not recovered.

> [!missing] gap:31-45 · http://toolkitzone.com/forums/viewtopic.php?t=30634&start=30 · never-captured
> Page 3 of 3 was not recovered.
