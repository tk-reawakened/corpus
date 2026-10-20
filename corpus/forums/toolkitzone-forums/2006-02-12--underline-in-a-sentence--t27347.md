---
kind: forum-thread
id: "toolkitzone-forums/27347"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "27347"
title: "Underline in a sentence"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27347"
written: "2006-02-12T23:52:00"
last_post: "2006-02-13T00:16:00"
date_confidence: "exact"
captured: ["20060302022553"]
author: "nex666"
repliers: ["Lisha", "zyrshnikashnu"]
authors: ["nex666", "Lisha", "zyrshnikashnu"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_297340_amp_3Bsid_86f8eb59cc3e675cd63215a1fb19b293", captured: "20060302022553", sha256: "e1240c2d53d67c5bd815085530513ec6ad3055872f9d96b6e2568d9ae1175c92", wayback_url: "https://web.archive.org/web/20060302022553/http://toolkitzone.com/forums/viewtopic.php?p=297340&amp%3Bsid=86f8eb59cc3e675cd63215a1fb19b293"}
links: []
---

# Underline in a sentence

### nex666 · 2006-02-12 23:52 · #B297330

I'm just wondering if you can use an underline, just at the start of a sentence and continue on without underline.
This is using the pixeltext command.
Thanks in advance

### Lisha · 2006-02-13 00:02 · #B297334

I'm not sure what you're asking... you mean something like this?
No, don't touch that statue!
Only of course in RPGcode. Smile

### zyrshnikashnu · 2006-02-13 00:06 · #B297336

If you're using pixeltext, then you sure can. Just pixelText the underlined piece separate from the normal piece. For example...

**Code:**

```
underline("on")

pixelText(10, 10, "No,")

underline("off")

pixelText(20,10, "don't touch that statue!")
```

Just experiment with X values for the second piece until it looks natural.

### nex666 · 2006-02-13 00:16 · #B297340

Okay thanks, I wasn't sure of doing it that way, but I guess it works. Was wonder if there was a way you could just do it halfway through the sentence without having to split up sentences everywhere, but that's okay. I can make do with it ^__^
