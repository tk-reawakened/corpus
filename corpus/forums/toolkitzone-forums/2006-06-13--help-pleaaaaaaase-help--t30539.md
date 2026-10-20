---
kind: forum-thread
id: "toolkitzone-forums/30539"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Newbie Haven"
skin: "phpbb2"
thread_id: "30539"
title: "HELP!!! PLEAAAAAAASE HELP!!"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=30539"
written: "2006-06-13T22:09:00"
last_post: "2006-06-14T07:56:00"
date_confidence: "exact"
captured: ["20060626232548"]
author: "Red_Riddle0"
repliers: ["Malegnis"]
authors: ["Red_Riddle0", "Malegnis"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_327317_amp_3Bsid_597b56f6b9102902c0f82a2cf1ec72c1", captured: "20060626232548", sha256: "44710c147d19aadc58c9bb3970d2ac91c8a63df74ab0730d9d110e57ae367d50", wayback_url: "https://web.archive.org/web/20060626232548/http://toolkitzone.com/forums/viewtopic.php?p=327317&amp%3Bsid=597b56f6b9102902c0f82a2cf1ec72c1"}
links: []
---

# HELP!!! PLEAAAAAAASE HELP!!

### Red_Riddle0 · 2006-06-13 22:09 · #B327317

Sorry to bother, but i can't find this on the Manual or on the Forums.
I'm trying to make an NPC walk and talk. Everythings alright, I use the wander prgram and a Mwin Code, and when I test my game, the NPC wanders, and when i touch it, the message appears. But after the message dissapears, the NPC doesn't move, it stands still. Does anybody know how to make the NPC walk again? Please! HELP ME!!!!!!!

### Malegnis · 2006-06-14 07:56 · #B327443

set program to run while item is on board to "wander.prg" and make sure you have a wait() or a pause() after your mwin.
