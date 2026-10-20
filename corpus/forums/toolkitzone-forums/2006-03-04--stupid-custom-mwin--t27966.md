---
kind: forum-thread
id: "toolkitzone-forums/27966"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "27966"
title: "Stupid custom mwin..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27966"
written: "2006-03-04T14:01:00"
last_post: "2006-03-04T14:13:00"
date_confidence: "exact"
captured: ["20060327193608"]
author: "Lisha"
repliers: ["DrakeLord"]
authors: ["Lisha", "DrakeLord"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_303379_amp_3Bsid_eb921d85f60f19d58fa43ba91e785f5b", captured: "20060327193608", sha256: "7029d43faf701f90a1772e032e72710f715c3a7b8fe486ba45dbad4a207d3611", wayback_url: "https://web.archive.org/web/20060327193608/http://toolkitzone.com/forums/viewtopic.php?p=303379&amp%3Bsid=eb921d85f60f19d58fa43ba91e785f5b"}
links: []
---

# Stupid custom mwin...

### Lisha · 2006-03-04 14:01 · #B303375

I'm trying to code my custom mwin and I've got to say it isn't working out well. When I try to test it, I get this message (which it won't let me copy) saying that my setImage commands need 5 data elements? What the heck does that mean?? Confused I'm so confuzzled. And frustrated, too. Here's my method:

**Code:**

```
method cmwin(pic$, line1$, line2$, line3$, line4$, line5$, line6$)

{

   //save screen

   saveScreen()

   setImage("pic$" 0, 150, 303, 607)

   setImage("mwin.png" 0, 150, 740, 240)

   text(3, 1, line1$)

   text(3, 2, line2$)

   text(3, 3, line3$)

   text(3, 4, line4$)

   text(3, 5, line5$)

   text(3, 6, line6$)

   wait()

   restoreScreen()

}
```

And I know that probably all the placings of stuff are wrong. I was just going to fix those through trail and error, but, well, since I can't trial... Laughing

### DrakeLord · 2006-03-04 14:12 · #B303378

You need a comma after the "pic$" and "mwin.png". It was being read as only 4 data elements because you forgot the comma.

### Lisha · 2006-03-04 14:13 · #B303379

Oh. Heheh. Laughing I knew it would be something stupid like that... But thanks!! You saved me a lot of grief.
EDIT- Oh dammit stupid mwin is screwed up again. See how in the code I have the pic$ variable? That's for the profile image. And it isn't working. I get this black box the size of what the image is supposed to be, but the image itself it not there. Anyone know what's wrong?
EDIT AGAIN - I figured it out. It was just a case of misplaced quotation marks. Again. Laughing
