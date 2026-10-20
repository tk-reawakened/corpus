---
kind: forum-thread
id: "toolkitzone-forums/12207"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Site Discussion"
skin: "phpbb2"
thread_id: "12207"
title: "Beware the &quot;Slash Bug&quot;"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12207"
written: "2004-12-06T02:11:00"
last_post: "2004-12-06T16:06:00"
date_confidence: "exact"
captured: ["20041215093840", "20050115140400", "20050115140454", "20050115140746", "20051018062641", "20051029103322", "20051031072438"]
author: "Mystinar"
repliers: ["Xavier"]
authors: ["Mystinar", "Xavier"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135335_amp_", captured: "20050115140400", sha256: "f1358343d7cad3006c3408ae850491e4dabe22214b84b5f637bfb1a58069097b", wayback_url: "https://web.archive.org/web/20050115140400/http://www.toolkitzone.com/forums/viewtopic.php?p=135335&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135335_amp_3Bsid_7d88bca41c7b4ff4f702d9ad24ba307a", captured: "20051029103322", sha256: "7d80fbb62859d40b96efcdb4ff782e8934e16485068309ba74de421724144827", wayback_url: "https://web.archive.org/web/20051029103322/http://www.toolkitzone.com/forums/viewtopic.php?p=135335&amp%3Bsid=7d88bca41c7b4ff4f702d9ad24ba307a"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135515_amp_", captured: "20050115140746", sha256: "c7ac0440fecf1f247665d5cc2a8b7e0a1c609b8c2c032eedbdf4bfae0585b99b", wayback_url: "https://web.archive.org/web/20050115140746/http://www.toolkitzone.com/forums/viewtopic.php?p=135515&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135515_amp_3Bsid_7d88bca41c7b4ff4f702d9ad24ba307a", captured: "20051031072438", sha256: "d20e3dbbd28b8520a0feab47b2c6ee71933d170b65135c6803df888197c503c1", wayback_url: "https://web.archive.org/web/20051031072438/http://www.toolkitzone.com/forums/viewtopic.php?p=135515&amp%3Bsid=7d88bca41c7b4ff4f702d9ad24ba307a"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135539", captured: "20050115140454", sha256: "91eef1e6ecf5ecca91c401769ddfa1163c59b651230df3344bf6b4f6c42a5323", wayback_url: "https://web.archive.org/web/20050115140454/http://www.toolkitzone.com/forums/viewtopic.php?p=135539"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135539_amp_", captured: "20041215093840", sha256: "748d83755eac71feffb1171a470f261b77be41dc6ea996880b6b4984db6f6c21", wayback_url: "https://web.archive.org/web/20041215093840/http://www.toolkitzone.com/forums/viewtopic.php?p=135539&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135539_amp_3Bsid_7d88bca41c7b4ff4f702d9ad24ba307a", captured: "20051018062641", sha256: "4bd2ac1b35e8be6bdd3d695bed9af9b60b210f5f7c82ef01d650fbab1e45e422", wayback_url: "https://web.archive.org/web/20051018062641/http://www.toolkitzone.com/forums/viewtopic.php?p=135539&amp%3Bsid=7d88bca41c7b4ff4f702d9ad24ba307a"}
links: []
---

# Beware the &quot;Slash Bug&quot;

### Mystinar · 2004-12-06 02:11 · #B135335

Whenever you open a page to edit it, one or more slashes always appear before a apostrophe. It is quite annoying, and it is time consuming to delete them all.
EDIT: One more thing! They appear before quotation marks.

### Xavier · 2004-12-06 13:11 · #B135515

Want to be more specific where this happens? It's a common issue, and takes about 1 second to fix.
I checked the edit "game pages" page but it all seems fine there.
As for why they appear, it's neccessary to prevent strings escaping while sending them to the database as you obviously enclose them with ' or ". Now and again these protective slashes are not removed before being displayed on the screen.

### Mystinar · 2004-12-06 16:06 · #B135539

That seems to explain it. I could just copy and paste from my computer to avoid that.
