---
kind: forum-thread
id: "toolkitzone-forums/12517"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "12517"
title: "Visual Basic 6....again"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12517"
written: "2004-12-12T18:05:00"
last_post: "2004-12-12T20:16:00"
date_confidence: "exact"
captured: ["20041228072521"]
author: "sivart"
repliers: ["saberknight", "Colin"]
authors: ["sivart", "saberknight", "Colin"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_138568_amp_", captured: "20041228072521", sha256: "a2250c75387f59a66a12ef94a2f16033e8d72bb02701a54fec2dc82faaa0469f", wayback_url: "https://web.archive.org/web/20041228072521/http://www.toolkitzone.com/forums/viewtopic.php?p=138568&amp="}
links: []
---

# Visual Basic 6....again

### sivart · 2004-12-12 18:05 · #B138491

Hello , well i made my 2 person chat and its decent im working out smiles right now but one thing i thought of is being able to register... somehow storing registered passwords/usernames into a database so you cant connect if you dont have one ... could anyone help?

### saberknight · 2004-12-12 19:38 · #B138543

well as far as a remote database you could use mysql or ldap in which case i would use a seperate linux server to store the users however it sounds like you are making this product for small scale use so I would have to recommend storing the users in memory and then saving them to a file that could be loaded at server startup i made a vb.net chat server a while back and it worked well but it was for a low security intranet so i never added passwords however mysql (or other sql) or ldap are the professional ways of storing user data just in case you wanted to know if you use a database server and a chat server that is known as a 3 tiered architecture which is good for large use but for small scale use i would still recommend a 2 tiered architecture aka just store the users localy sorry i didn't include any code but im a vb.net programmer not a vb6 programmer

### Colin · 2004-12-12 19:59 · #B138556

Just have a remote serve that hosts all conversations, Sivart.

### sivart · 2004-12-12 20:16 · #B138568

Thats what im asking about how to do..
