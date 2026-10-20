---
kind: forum-thread
id: "toolkitzone-forums/8201"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "games"
skin: "phpbb2"
thread_id: "8201"
title: "Game Section issues"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=8201"
written: "2004-09-04T12:51:00"
last_post: "2004-09-04T18:39:00"
date_confidence: "exact"
captured: ["20050120115953"]
author: "Dragonmaster"
repliers: ["Dragonmaster[ul]", "Xavier"]
authors: ["Dragonmaster", "Dragonmaster[ul]", "Xavier"]
posts_present: 9
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_87394_amp_", captured: "20050120115953", sha256: "1346fafae88da13d7fc3affbc0e042466bdd376b9a6583c02cb0dbd0eea49fe3", wayback_url: "https://web.archive.org/web/20050120115953/http://www.toolkitzone.com/forums/viewtopic.php?p=87394&amp="}
links: []
---

# Game Section issues

### Dragonmaster · 2004-09-04 12:51 · #B87226

Im trying to add/update images to my game section, but I cant find the image, and I cant find the add option either. Not sure, maybe I'm blind. BTW im still getting Line 7 error.

### Dragonmaster[ul] · 2004-09-04 12:56 · #B87230

Ok here is what Im thinking your line 7 problem is. document.body.offsetWidth will throw an error when the BODY element has not been parsed. I think you will need to use call this script within the body tag.

### Xavier · 2004-09-04 14:01 · #B87247

Works for me, I just created a game profile and added an image and it all works fine.
The code has not been changed for several months, so it's not like it could have been moved recently.
Remember, to handle images you click on "games" on the account bar (next to profile) and then click images.

### Dragonmaster · 2004-09-04 15:31 · #B87266

Here is what I am getting
Parse error: parse error in /home/pfxcarty/domains/toolkitzone.com/public_html/mygames/images_update.php on line 70

### Xavier · 2004-09-04 15:37 · #B87268

Ah, nice catch. Fixed.
Good to know people are reporting these bugs, in the past no one ever said anything and it took weeks before they got reported.

### Dragonmaster · 2004-09-04 15:40 · #B87269

also it seems like the line 7 error only happens on the forums. If I go anywhere else its fine.

### Xavier · 2004-09-04 15:44 · #B87270

I think I have fixed that now, tracked it down to not the menu resize code by code that prevents topics stretching the screen.
Tell me if it no longer errors on you now.

### Dragonmaster · 2004-09-04 18:36 · #B87392

Looks like you got it. Here are two more things.
Logging in seems to be more difficult now. I think there use to be a login link at the top now, thats not really there anymore.
The "links" link is gone. Im not sure if it was meant to be gone, but it was a useful resource for me.

### Xavier · 2004-09-04 18:39 · #B87394

Links page is being re-coded.
