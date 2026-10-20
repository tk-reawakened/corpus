---
kind: forum-thread
id: "toolkitzone-forums/30530"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "30530"
title: "Animation File"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=30530"
written: "2006-06-13T19:31:00"
last_post: "2006-06-14T15:35:00"
date_confidence: "exact"
captured: ["20060628062515"]
author: "SuperIsoRPG"
repliers: ["phantom_x1986", "Colin", "Khin"]
authors: ["SuperIsoRPG", "phantom_x1986", "Colin", "Khin"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_327389_amp_3Bsid_7d08da24988c57a13ad3b528728759c8", captured: "20060628062515", sha256: "853d3a08c233dc5058b0ff5d72fd066bad2ca216e8e1bf2875c4068828dcb5d3", wayback_url: "https://web.archive.org/web/20060628062515/http://toolkitzone.com/forums/viewtopic.php?p=327389&amp%3Bsid=7d08da24988c57a13ad3b528728759c8"}
links: []
---

# Animation File

### SuperIsoRPG · 2006-06-13 19:31 · #B327243

Alright, i found the syntax of ANM files. The problem is that when you open them in RPG Toolkit, you get a message saying:
"the following is not a valid animation file", i re-tested this by copying and pasting all the code in one animation file into another file, and the same problem occurs. Why specifically does this happen (someone with a good knowledge of TK internal workings may know)

### phantom_x1986 · 2006-06-13 19:59 · #B327256

Sounds like a nasty error. When does this occur so I can try to avoid it?

### Colin · 2006-06-14 02:48 · #B327389

You can't copy a raw file using notepad (or line by line file writing!). The result would be to convert each character into a byte. Anyway, it's not something you want to do.

### Khin · 2006-06-14 06:53 · #B327434

Yeah sometimes I just wanted to edit the animation file in a text editor coz' I'm just changing a few letters for each of the pics I used. I found out that it can't be done that way Confused

### phantom_x1986 · 2006-06-14 12:30 · #B327474

**Colin wrote:**

> You can't copy a raw file using notepad (or line by line file writing!). The result would be to convert each character into a byte. Anyway, it's not something you want to do.
>

I knew that, even though I've actually done it with a board.

### SuperIsoRPG · 2006-06-14 15:35 · #B327491

**Colin wrote:**

> You can't copy a raw file using notepad (or line by line file writing!). The result would be to convert each character into a byte. Anyway, it's not something you want to do.
>

I really do want to do it as it will vastly speed up the animation process for me. How would you go around doing it?
would a textbox in a VB document using MSCommonDialog saving ANM files work?
is their such a thing as a raw file editor Confused, that just changed the data contained within the file itself?
EDIT: ha! i've managed to find a program that does go into toolkit files on a text based level and keeps them working!
Hurray for Colin discouraging me, if he hadn't, i would have just give up
