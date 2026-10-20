---
kind: file
id: "toolkitzone.com/597"
site: "toolkitzone.com"
title: "XD Emu Pack"
original_url: "http://www.toolkitzone.com/fileman.php?id=3&file=597"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040619182756", "20060312090833"]
author: "DEXTER"
repliers: []
authors: ["DEXTER"]
comments_present: 0
f_author_source: "DEXTER"
f_description: "written by John@aljo"
f_name: "XD Emu Pack"
f_size: "3.5 kb"
f_submitted_by: "DEXTER"
f_version: "1.0"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_597", captured: "20040619182756", sha256: "971769a3b15cfcb39a9b4e575572d298d8d2216942232841f0a7d063e54c3f65", wayback_url: "https://web.archive.org/web/20040619182756/http://www.toolkitzone.com/fileman.php?id=3&file=597"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_597", captured: "20060312090833", sha256: "69b54cd4929d6b1e6140969ce7d80671318182063237d6413c2fbab78af9527b", wayback_url: "https://web.archive.org/web/20060312090833/http://www.toolkitzone.com/fileman.php?id=5&file=597"}
---

# XD Emu Pack

**password**
Some rather nice fades and other interesting methods. Also taught me something interesting, the fact that you can use a ? in the name of things in RPGCode. Very intresting indeed.
posted by on 2004-05-14 00:07:22 [Occasionally_Correct](forums/profile.php?mode=viewprofile&u=94)
Looks like you have a lot of methods there. Looks pretty good, but I did notice a few problems... - Your get player coords command is a little faulty. The variable to store the coords should come before the actual constants, not after them. - In GiveFP, you can't have handle$ in the angle backets then [fight]!. Doesn't work like that. You could try this though: #fpvar$ = "#" + handle$ + "[fight]!" #RPGCode(fpvar$) - Your GiveFP and GiveDP commands have the same name. Both are GiveFP, just thought I should point that out. ;) Other than that, good job.
