---
kind: forum-thread
id: "toolkitzone-forums/7207"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "7207"
title: "a on screen stats and map?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7207"
written: "2004-08-15T14:41:00"
last_post: "2004-08-15T14:57:00"
date_confidence: "exact"
captured: ["20040925162240"]
author: "guest 2"
repliers: ["Colosseus"]
authors: ["guest 2", "Colosseus"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_75852_amp_", captured: "20040925162240", sha256: "23107c3c92ab3fb61a1c29c00c7397167b1e9e13ca9df6e264d0d6d916af6552", wayback_url: "https://web.archive.org/web/20040925162240/http://www.toolkitzone.com/forums/viewtopic.php?p=75852&amp="}
links: []
---

# a on screen stats and map?

### guest 2 · 2004-08-15 14:41 · #B75844

would it be possible to have a on screen map and show the cherectors stats or something like that during gameplay? if so how?

### Colosseus · 2004-08-15 14:57 · #B75852

I've tried it before... AFAIK, it cannot be done. The screen is refreshing for every move, clearing any images drawn on-screen, so you'd have to encapsulate a SetImage function inside a loop that is running all the time... However, never-ending loops makes the engine stop there. So it will update the image, however the player will be unable to move or do anything.
