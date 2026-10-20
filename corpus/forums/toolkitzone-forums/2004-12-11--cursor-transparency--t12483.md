---
kind: forum-thread
id: "toolkitzone-forums/12483"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "general chat"
skin: "phpbb2"
thread_id: "12483"
title: "Cursor Transparency"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12483"
written: "2004-12-11T23:26:00"
last_post: "2004-12-12T00:02:00"
date_confidence: "exact"
captured: ["20041227215238"]
author: "machsprinter"
repliers: ["Colin"]
authors: ["machsprinter", "Colin"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_138211_amp_", captured: "20041227215238", sha256: "432dbcae97db2a3239ee805bc28d8e6faf23a73b4b415b2e8859248e6007bf26", wayback_url: "https://web.archive.org/web/20041227215238/http://www.toolkitzone.com/forums/viewtopic.php?p=138211&amp="}
links: []
---

# Cursor Transparency

### machsprinter · 2004-12-11 23:26 · #B138189

How do I make a cursor transparent? When I load my own cursor it shows as a solid 32x32 tile. With that said, cursors smaller than 32x32 are automatically stretched to 32x32, even though the primers say that is optional.

### Colin · 2004-12-12 00:02 · #B138211

The second parameter defaults to stretching, you have to say no to make it not. Pure red (255, 0, 0) will be made transparent.
