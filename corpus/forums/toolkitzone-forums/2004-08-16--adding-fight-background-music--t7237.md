---
kind: forum-thread
id: "toolkitzone-forums/7237"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "7237"
title: "Adding Fight Background Music"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7237"
written: "2004-08-16T00:08:00"
last_post: "2004-08-16T00:17:00"
date_confidence: "exact"
captured: ["20040925162224"]
author: "nova11"
repliers: ["Colosseus"]
authors: ["nova11", "Colosseus"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_76206_amp_", captured: "20040925162224", sha256: "94dd219e22b501a43a54dcef2c1fc064f44b2a91c7caec339269036c88c4897e", wayback_url: "https://web.archive.org/web/20040925162224/http://www.toolkitzone.com/forums/viewtopic.php?p=76206&amp="}
links: []
---

# Adding Fight Background Music

### nova11 · 2004-08-16 00:08 · #B76205

Another stuuuuupid n00b question from the Nova....
I was wondering, while setting up my very weird demo for Dragon's Gate, how i would add background music for a battle. Which is pretty startiforward i guess. I'd like to know how to get it for random battles, and battles i made a program for. Also, can it change with the battle? thanks

### Colosseus · 2004-08-16 00:17 · #B76206

If you're using the default BS, just choose a music file in the Background Music option in the Fight Background Editor. In code, you could use #MidiPlay() or #Mp3() or similar.
