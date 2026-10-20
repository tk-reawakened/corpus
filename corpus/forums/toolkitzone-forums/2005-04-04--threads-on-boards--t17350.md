---
kind: forum-thread
id: "toolkitzone-forums/17350"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "17350"
title: "Threads on boards"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=17350"
written: "2005-04-04T16:48:00"
last_post: "2005-04-04T22:33:00"
date_confidence: "exact"
captured: ["20050406051849", "20051031045408", "20051107045825"]
author: "Allan@Aljo"
repliers: ["Dont_Think_So"]
authors: ["Allan@Aljo", "Dont_Think_So"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_190226_amp_3Bsid_fd0775e609cae9ad7a4bc6d1ec8e2450", captured: "20051107045825", sha256: "c93fcbe06cc8a724f9f52370fdd4171b431f193c3dc3285c1e3fbde6439d8ff4", wayback_url: "https://web.archive.org/web/20051107045825/http://www.toolkitzone.com/forums/viewtopic.php?p=190226&amp%3Bsid=fd0775e609cae9ad7a4bc6d1ec8e2450"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_190387", captured: "20051031045408", sha256: "ace86bc15b72a8c3413971702f4b1fcd236814cd0b09b0f44d2f4e6bfac88593", wayback_url: "https://web.archive.org/web/20051031045408/http://www.toolkitzone.com/forums/viewtopic.php?p=190387"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_190387_amp_", captured: "20050406051849", sha256: "4750d0b72e0a334ab8534ef20e87b3e1be0ef50029609a24927bb5261c8bb79c", wayback_url: "https://web.archive.org/web/20050406051849/http://www.toolkitzone.com/forums/viewtopic.php?p=190387&amp="}
links: []
---

# Threads on boards

### Allan@Aljo · 2005-04-04 16:48 · #B190226

I know this proably simple but what is the manipulation varible for the thread initiated using the board editor's threading function.

### Dont_Think_So · 2005-04-04 22:31 · #B190386

It doesn't exist, so far as I know. There may be a command to get the ID of the thread it's being called in, but you would have to check the reference for that...
I recommend instead creating a program that would use createThread, then set that as the "Program to run on entering board".

### Allan@Aljo · 2005-04-04 22:33 · #B190387

yeah there is a gettheadid... I found it
