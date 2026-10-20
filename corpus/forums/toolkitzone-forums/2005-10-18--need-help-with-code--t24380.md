---
kind: forum-thread
id: "toolkitzone-forums/24380"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Legacy Support"
skin: "phpbb2"
thread_id: "24380"
title: "Need help with code"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=24380"
written: "2005-10-18T02:07:00"
last_post: "2005-10-29T22:00:00"
date_confidence: "exact"
captured: ["20060112040228", "20060320052205", "20060323194236"]
author: "DarkMoon"
repliers: ["euixgraves"]
authors: ["DarkMoon", "euixgraves"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_265164_amp_3Bsid_b4534c849086ea60f22aa5790d1e69a7", captured: "20060112040228", sha256: "735079b550e8810027a0d2a5f803704c111344939dd327e31d19088c645a2385", wayback_url: "https://web.archive.org/web/20060112040228/http://toolkitzone.com/forums/viewtopic.php?p=265164&amp%3Bsid=b4534c849086ea60f22aa5790d1e69a7"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_267344", captured: "20060323194236", sha256: "9f605c08339abb73b90e0cb618fa85a97599a284eaff8b444f1eddd00de8b0a7", wayback_url: "https://web.archive.org/web/20060323194236/http://toolkitzone.com/forums/viewtopic.php?p=267344"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_267344_amp_3Bsid_06e0f790333e23d2463ff11405c7f78a", captured: "20060320052205", sha256: "a1db4c503810404f553fa1aa05a6b3068999815ba19fa2899b1baf5aa1a61c8e", wayback_url: "https://web.archive.org/web/20060320052205/http://toolkitzone.com/forums/viewtopic.php?p=267344&amp%3Bsid=06e0f790333e23d2463ff11405c7f78a"}
links: []
---

# Need help with code

### DarkMoon · 2005-10-18 02:07 · #B265164

I need help. I can't figure out how to to get a program that waits for the user to press a key. Before you say #Get or #Wait I need the program to run a method if there is no keypress after a certain amount of time. Anyone have a suggestion? I'm using TK2 so I thought I put it here instead of the coding section. Colin got angry with me for asking about things in TK2 last time. Confused

### euixgraves · 2005-10-29 22:00 · #B267344

AHh if they have a thread sleep in toolkit2 mabye u can use that
But i dunno somthing like that atleast like
if it would be on toolkit2
it would be like
#wait(a$)
#threadsleep(thread!,60) * for 60 seconds*
#if(a$ = "what ever key")
{
#killthread(thread!)
i dont even knonw if they have it on toolkit2 i dont use it
