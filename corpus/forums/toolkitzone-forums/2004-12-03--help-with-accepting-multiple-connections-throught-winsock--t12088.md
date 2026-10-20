---
kind: forum-thread
id: "toolkitzone-forums/12088"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "12088"
title: "help with accepting multiple connections throught winsock"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12088"
written: "2004-12-03T17:16:00"
last_post: "2004-12-04T21:39:00"
date_confidence: "exact"
captured: ["20041226222328"]
author: "sivart"
repliers: ["Colin", "Levi"]
authors: ["sivart", "Colin", "Levi"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_134688_amp_", captured: "20041226222328", sha256: "8b34356efa4b16d54eef65624ec91ce048632acd77e831e3793145ba3f317682", wayback_url: "https://web.archive.org/web/20041226222328/http://www.toolkitzone.com/forums/viewtopic.php?p=134688&amp="}
links: []
---

# help with accepting multiple connections throught winsock

### sivart · 2004-12-03 17:16 · #B134168

Hey , i made a simple 2 person chat system and i was wondering how you connect more then 2 people to it.... I read some tutorials , but they didnt really help much.. For a multiple connection , the server Re-Sends the data right? Anyway please help!
Thanks!
Travis

### Colin · 2004-12-04 05:20 · #B134445

You need a WinSock control array in which you can dynamically create new controls with the 'Load' keyword.

### sivart · 2004-12-04 17:38 · #B134565

Yea , im still completly lost..

### Levi · 2004-12-04 21:39 · #B134688

hey Sivart have you had any experience with arrays, regular variable arrays that is? If not then I think you ned to go over them to get the basic concept. Control arrays are like being able to create a new control at run-time, in the case of winsock to accept another connection. Only the application recieving the extra connections should have a control array.
That tutorial on winsockvb was fairly good at explaining this concept.
