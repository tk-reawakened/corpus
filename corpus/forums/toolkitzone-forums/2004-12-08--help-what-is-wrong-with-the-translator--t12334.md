---
kind: forum-thread
id: "toolkitzone-forums/12334"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "12334"
title: "HELP what is wrong with the translator"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12334"
written: "2004-12-08T22:03:00"
last_post: "2004-12-08T22:36:00"
date_confidence: "exact"
captured: ["20050116235200"]
author: "phishit"
repliers: ["Compugeek", "Colin", "Dont_Think_So"]
authors: ["phishit", "Compugeek", "Colin", "Dont_Think_So"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_136625_amp_", captured: "20050116235200", sha256: "285909181e20c6d4a4a160415d5ba28e9d3f9ad7a19e36bdd1b388d280cedbb7", wayback_url: "https://web.archive.org/web/20050116235200/http://www.toolkitzone.com/forums/viewtopic.php?p=136625&amp="}
links:
  - {url: "http://rpgtoolkit.com", status: "captured", local: "wayback/rpgtoolkit.com/index"}
---

# HELP what is wrong with the translator

### phishit · 2004-12-08 22:03 · #B136608

Ok whenever i go into the game translotr to play the game errors keep coming up. A couple days ago it was fine, but now the text from the 'start' program comes up, and an error saying:
A runtime error has occured....
Code: 372
Description: Failed to load control 'MMControl' from mci32.ocx. Your version of mci32.ocx may be outdated. Make sure you are using the version of the control that was provided with your application.
You can continure working without any problems. But, you may wish to report this bug at <http://rpgtoolkit.com>
Now like i said this didnt happen a few days ago, but just to be absoutely sure nothing got deleated or anything, i downloaded TK3.04 AGAIN and the error STILL comes up.
Please help, i am going to cry.

### Compugeek · 2004-12-08 22:14 · #B136612

Hmm, you most likely updated your computer or installed another program which put an older version of that control on your computer. This is not a problem with the TK itself. You may want to search Google or Microsoft.com for a newer version to download.

### Colin · 2004-12-08 22:23 · #B136616

You're mistaken. Want to know why? I removed the function that shows error messages like that from tk 3.x.
Are you sure you're using 3.04?

### Dont_Think_So · 2004-12-08 22:30 · #B136620

Why would you remove an error handler? Razz

### Colin · 2004-12-08 22:34 · #B136623

It didn't handle errors. It just showed a box whose errors can often be safely ignored, anyway.

### phishit · 2004-12-08 22:36 · #B136625

Oh thank you It finally works now, I download both mci whatever and tk3.04 in a NEW folder. I dont know why it did that but thanks again
