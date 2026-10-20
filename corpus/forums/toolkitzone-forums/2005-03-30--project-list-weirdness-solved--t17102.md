---
kind: forum-thread
id: "toolkitzone-forums/17102"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "17102"
title: "Project List weirdness **Solved**"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=17102"
written: "2005-03-30T08:31:00"
last_post: "2005-04-07T10:32:00"
date_confidence: "exact"
captured: ["20050407222642"]
author: "khaldore"
repliers: ["Delano", "Janus"]
authors: ["khaldore", "Delano", "Janus"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_190933_amp_", captured: "20050407222642", sha256: "bdf88c2b998f752ec7ef35e5d7f6e523c143b47e41e551b0490a007c3322d50f", wayback_url: "https://web.archive.org/web/20050407222642/http://www.toolkitzone.com/forums/viewtopic.php?p=190933&amp="}
links:
  - {url: "http://toolkitzone.com/stuff/files/2400/projectlist.jpg", status: "never-captured", local: null}
---

# Project List weirdness **Solved**

### khaldore · 2005-03-30 08:31 · #B187718

After a rather lengthy search, I didn't see anyone else having this problem, so maybe I just screwed up somewhere. But...
I downloaded the 3-05-05 build a while ago, and recently started looking around to see what nifty stuff had been improved. To my surprise, I came across this:
![](http://toolkitzone.com/stuff/files/2400/projectlist.jpg)
Apparently I'm unable to open any of the folders to get at any of the project files, and the effect isn't corrected when loading other projects (such as demo.gam). Just thought I'd put this out here to see if anyone else had this happen.
Mike

### Delano · 2005-03-30 09:04 · #B187720

Strange, I've not seen that before. I can only suggest reinstalling, changing to an earlier build or hanging on for 3.0.6.

### khaldore · 2005-03-30 09:17 · #B187723

I'll likely re-install 3.05, then check it before and after the 3-05 build. Maybe it was simply something I did wrong, but I'll test it out and let you know. It simply struck me as odd. *shrugs* All else fails, though, I can wait on 3.06. My game progress right now is slow at best, so waiting won't kill me.
EDIT: Just did a uninstall/re-install of 3.05 *only* (no dev bulids... I even deleted the Program Files folder after moving my game folders elsewhere)... and the project list remains the same. I can still access the files through the 'Open File' button, as well as through the 'File' menu, but still... I don't recall this happening anytime before with 3.05. Confused

### khaldore · 2005-04-06 01:35 · #B190933

My apologies for bumping this, but with the release of 3.06, I thought it was warranted. I uninstalled 3.05, then proceeded to delete the Toolkit3 folder (after moving my project files). I then installed 3.06, and to my dismay, the project list remains the same as shown in the original post. I'm starting to think this is related to WinXP themes, or something... I disabled everything on here I could in order to reduce the amount of RAM used (128MB don't cut it anymore), so perhaps it's related... any ideas?
Mike

### Delano · 2005-04-06 10:32 · #B191099

Ah, got it. Check the file attributes (properties) of the folders - if "Archive" is selected, deselect it (and apply it to the folder but not the files contained). That should fix the problem for 3.0.6, I've properly fixed it so that it will recognise Archived folders in the future - sorry I didn't pick up on that first time round.

### khaldore · 2005-04-06 20:32 · #B191267

Well, there wasn't an 'Archive' selection in the properties, but mentioning it reminded me of something else that might be the cause. A few weeks ago, I applied NTFS compression to the entire hard drive (saved a whole 2GB... whee). I'm thinking that might have affected things, though other programs don't seem to notice. Anyhow, I've uncompressed the TK3 folder, so I'll let you know if it's fixed very shortly...
(time passes)
That was it, all right... I uncompressed the entire TK3 folder (and its contents), and everything looks fine. Thanks for the help, Delano... if you hadn't mentioned 'Archive' I likely wouldn't have remembered this. Very Happy
Mike

### Delano · 2005-04-07 09:10 · #B191499

Ah right - so something along those lines! I don't know much about ntfs - maybe it has the same kinda effect. Hopefully this fix will sort the problem for ntfs folders too.
Glad you got it working!

### Janus · 2005-04-07 10:32 · #B191516

**Delano wrote:**

> Ah right - so something along those lines! I don't know much about ntfs - maybe it has the same kinda effect. Hopefully this fix will sort the problem for ntfs folders too.
> Glad you got it working!
>

compressed is an attribute just like archive, so if you were doing anything based on the attributes of a file, then the problem and fix should be the same.
