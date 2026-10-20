---
kind: forum-thread
id: "toolkitzone-forums/10415"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "10415"
title: "Pointing fun with pointers... o_O"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10415"
written: "2004-10-20T22:18:00"
last_post: "2004-10-20T23:47:00"
date_confidence: "exact"
captured: ["20041226085445"]
author: "Zap!"
repliers: ["Colin"]
authors: ["Zap!", "Colin"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_113982_amp_", captured: "20041226085445", sha256: "2cee225da80731509b16acadb8b402572d72d9a3f9de120748b04d6d0fce0d02", wayback_url: "https://web.archive.org/web/20041226085445/http://www.toolkitzone.com/forums/viewtopic.php?p=113982&amp="}
links: []
---

# Pointing fun with pointers... o_O

### Zap! · 2004-10-20 22:18 · #B113881

Meh....dispite the topic subject which is irrelvant to an extent.....is it possible to set a pointer that will grab the Handle of another running program? Like, using the logic pointers point to a "unit" in memory I want one to point to a warcraft III "unit" and a speific one -- the handle.

### Colin · 2004-10-20 22:26 · #B113890

Win32 API is your friend -- especially this one:
FindWindow()

### Zap! · 2004-10-20 23:47 · #B113982

ohhh sweet thx I looked on MSDN and only found WM_ACTIVATE .. -_-
