---
kind: file
id: "toolkitzone.com/638"
site: "toolkitzone.com"
title: "Pic2RPG"
original_url: "http://www.toolkitzone.com/fileman.php?id=3&file=638"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040605042448", "20041106082002"]
author: "computerdude800"
repliers: []
authors: ["computerdude800"]
comments_present: 0
f_author_source: "Daniel Gillespie (Computerdude800)"
f_description: "written by John@aljo"
f_name: "Pic2RPG"
f_size: "58.9 kb"
f_submitted_by: "computerdude800"
f_version: "1.0"
f_website: "chronogames.com"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_638", captured: "20040605042448", sha256: "36b2a65d6c91bc621bcd84caa2ac04a40649f45707d0cab40eb9fe57bc930af8", wayback_url: "https://web.archive.org/web/20040605042448/http://www.toolkitzone.com/fileman.php?id=3&file=638"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_638", captured: "20041106082002", sha256: "eed79adee7d3d4cada3dcc7c594d8974102fb671a362aaa78ee49fe359070aae", wayback_url: "https://web.archive.org/web/20041106082002/http://www.toolkitzone.com/fileman.php?id=5&file=638"}
---

# Pic2RPG

**password**
**Pic2RPG**
If you really are hankering to do everything in rpgCode with no picture file support then here is your answer. Although not quite what I would consider coder friendly it does successfully create a picture into RPGCode.
posted by on 2004-06-01 17:16:09 [John@aljo](forums/profile.php?mode=viewprofile&u=76)
Some suggestions for this program would be to make the prg created into a method to make it easy to move the created picture around the screen, and also so give some compression logic to the picture. An example of this would be to use a line to draw all alike colors thus at points (if not using a jpeg format) would increase the speed of drawing significantly. also selection of a transparent color. One that the blitter will ignore when converting to rpgcode. If you really wanted to take the time to figure it out, I see the best way of drawing the picture is with rectangles instead of lines. This algorithm would be complicated but would draw the picture most likely the fastest. Just some suggestions. I created a program like this but far to buggy to put up here. was one of my first c++ programs. To see some of the results, check out the Shack's duck contest.
posted by on 2004-06-02 03:22:46 [Euix](forums/profile.php?mode=viewprofile&u=9)
He's right, you need to create some sort of algorithm to make the drawing faster. That, and who wants 100MB RPGCode programs just to draw an image? I think we'd rather use the actual image files themselves :P
posted by on 2004-06-02 16:27:14 [bK_Coder](forums/profile.php?mode=viewprofile&u=2129)
Hmm. The file gets really big. maybe you should check for pixels with the same colors coming after each other in a row of the picture "matrix". If two ore more comes, use DrawLine instead.
