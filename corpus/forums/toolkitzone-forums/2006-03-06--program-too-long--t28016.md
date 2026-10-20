---
kind: forum-thread
id: "toolkitzone-forums/28016"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Editor"
skin: "phpbb2"
thread_id: "28016"
title: "Program too long?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=28016"
written: "2006-03-06T02:56:00"
last_post: "2006-03-06T19:07:00"
date_confidence: "exact"
captured: ["20060320134353"]
author: "Conman3880"
repliers: ["DrakeLord"]
authors: ["Conman3880", "DrakeLord"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_303881_amp_3Bsid_7661bbbbb86e5246ab8babb6f36bbb96", captured: "20060320134353", sha256: "2f2f4d7838e3602fb59ebe3210dc5c4591f40d64b3b9a3c4ccc5e4d4028d7c5a", wayback_url: "https://web.archive.org/web/20060320134353/http://toolkitzone.com/forums/viewtopic.php?p=303881&amp%3Bsid=7661bbbbb86e5246ab8babb6f36bbb96"}
links: []
---

# Program too long?

### Conman3880 · 2006-03-06 02:56 · #B303803

I have a long RPGcode program, and the text flows off the textbar before the text bar gives the next section of text. Am I making sense? What do I do? If it's in the users guide, could you tell me which section? Thank you much.

### DrakeLord · 2006-03-06 03:06 · #B303805

Well, assuming you're using the default mwin, you have to use mwincls() after about 4 lines. That is if you have your font size at 20.
Use it like this:

**Code:**

```
mwin("Bob: What do you want to do?")

mwin("Joe: I dunno.  What do you wanna do?")

mwin("Bob: I don't know.  What do you want to do?")

mwin("Joe: I dunno.  What do you wanna do?")

wait()

mwincls()

mwin("Bob: I don't know.  What do you want to do?")

mwin("Joe: I dunno.  What do you wanna do?")

mwin("Bob: I don't know.  What do you want to do?")

mwin("Joe: I dunno.  What do you wanna do?")

wait()

mwincls()

mwin("Bob: I don't know.  What do you want to do?")

mwin("Joe: I dunno.  What do you wanna do?")

mwin("Bob:........nevermind....")

wait()

mwincls()
```

That will make it so it'll clear the mwin so you can add more text.
Hope that helped.

### Conman3880 · 2006-03-06 19:07 · #B303881

thankie =)
