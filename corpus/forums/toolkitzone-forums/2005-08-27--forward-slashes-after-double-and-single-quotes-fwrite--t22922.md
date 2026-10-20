---
kind: forum-thread
id: "toolkitzone-forums/22922"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Programming"
skin: "phpbb2"
thread_id: "22922"
title: "Forward slashes after double and single quotes, fwrite"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=22922"
written: "2005-08-27T05:35:00"
last_post: "2005-08-27T22:14:00"
date_confidence: "exact"
captured: ["20051018072937", "20060110132025", "20060110155534", "20060110155558", "20060110155622", "20060110155648", "20060110155713"]
author: "zzz"
repliers: ["Oyerth", "Colin"]
authors: ["zzz", "Oyerth", "Colin"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_250770_amp_3Bsid_7f5babc9aca7847049b203e8703039b5", captured: "20060110155534", sha256: "e021ed2d135c912f9ccc5e4e4115e0b5b266c3b1a6e736caea4ea75d7ae6e5d9", wayback_url: "https://web.archive.org/web/20060110155534/http://www.toolkitzone.com/forums/viewtopic.php?p=250770&amp%3Bsid=7f5babc9aca7847049b203e8703039b5"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_250778_amp_3Bsid_7f5babc9aca7847049b203e8703039b5", captured: "20060110132025", sha256: "2fc7bda8f771d2956f4ea142866b23f0ae27e781791f1371c78d35af82389a05", wayback_url: "https://web.archive.org/web/20060110132025/http://www.toolkitzone.com/forums/viewtopic.php?p=250778&amp%3Bsid=7f5babc9aca7847049b203e8703039b5"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_250787_amp_3Bsid_7f5babc9aca7847049b203e8703039b5", captured: "20060110155558", sha256: "9123822175eba909e7f747d0e7783d018dca1fc2622b0a17bdaf084ee0a8c7e1", wayback_url: "https://web.archive.org/web/20060110155558/http://www.toolkitzone.com/forums/viewtopic.php?p=250787&amp%3Bsid=7f5babc9aca7847049b203e8703039b5"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_250788_amp_3Bsid_7f5babc9aca7847049b203e8703039b5", captured: "20060110155622", sha256: "5e75f66b305ec89ace21ef81f7c330100fca4756f020afe4f6952221a9416f1a", wayback_url: "https://web.archive.org/web/20060110155622/http://www.toolkitzone.com/forums/viewtopic.php?p=250788&amp%3Bsid=7f5babc9aca7847049b203e8703039b5"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_251065_amp_3Bsid_7f5babc9aca7847049b203e8703039b5", captured: "20060110155648", sha256: "6face2a7b6aef64ef83ae6c6346500780b884e6efede60851812f2bc6a6434c8", wayback_url: "https://web.archive.org/web/20060110155648/http://www.toolkitzone.com/forums/viewtopic.php?p=251065&amp%3Bsid=7f5babc9aca7847049b203e8703039b5"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_251068_amp_3Bsid_7f5babc9aca7847049b203e8703039b5", captured: "20060110155713", sha256: "d28e12b14e31ce8ea1acbd758ea1dfea78a3821a0942314c471627fecd682480", wayback_url: "https://web.archive.org/web/20060110155713/http://www.toolkitzone.com/forums/viewtopic.php?p=251068&amp%3Bsid=7f5babc9aca7847049b203e8703039b5"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_251071_amp_3Bsid_9cb115aff7d3b8ba5814f106b2283f26", captured: "20051018072937", sha256: "961448825f50ed42ded9c09a6ea013fa9429a097b818d40e29784d04e87f15f8", wayback_url: "https://web.archive.org/web/20051018072937/http://www.toolkitzone.com/forums/viewtopic.php?p=251071&amp%3Bsid=9cb115aff7d3b8ba5814f106b2283f26"}
links: []
---

# Forward slashes after double and single quotes, fwrite

### zzz · 2005-08-27 05:35 · #B250770

Oi, I asked John about this, but he didn't know how to fix it.
When you use fwrite, after every double (") or single (') quote, it puts a forward slash (/). Is therer anyway to stop this?
I tried an array, and swiching /'s with a space, but it seems to do it while/after the fwrite.

### Oyerth · 2005-08-27 05:45 · #B250778

Try: set_magic_quotes_runtime(0);

### Colin · 2005-08-27 05:59 · #B250787

On the contrary, don't try that. Magic quotes may be evil, but they do add some security, especially in code where deliberate measures are not coded.
Run whatever you need to through stripslashes().

### zzz · 2005-08-27 06:00 · #B250788

Its set_magic_quotes_runtime(1); Thanks much, however Smile.
::goes on to complete web edting thing::
EDIT:
So stripslashes(); is more security? I'm all about saftey Razz.

### Oyerth · 2005-08-27 22:04 · #B251065

Yes, that's to turn it on. I was suggesting turning them off.

### zzz · 2005-08-27 22:07 · #B251068

Well, turning them on worked Razz.

### Oyerth · 2005-08-27 22:14 · #B251071

Which ment they were already off. Wink
