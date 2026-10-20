---
kind: forum-thread
id: "toolkitzone-forums/22908"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Programming"
skin: "phpbb2"
thread_id: "22908"
title: "Help with VB Plugin SDK (TK 3.0.4+)"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=22908"
written: "2005-08-26T22:09:00"
last_post: "2005-08-27T18:29:00"
date_confidence: "exact"
captured: ["20051031004329", "20051107035140"]
author: "Dragen"
repliers: ["Colin", "Notsosuperhero"]
authors: ["Dragen", "Colin", "Notsosuperhero"]
posts_present: 11
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_250917_amp_3Bsid_cb94da1e2d09364c6250c0f48102d2e0", captured: "20051107035140", sha256: "ea985fafc707b05d22bacb1b80ffa8407179534efbab65c5ff9ac3738065407d", wayback_url: "https://web.archive.org/web/20051107035140/http://www.toolkitzone.com/forums/viewtopic.php?p=250917&amp%3Bsid=cb94da1e2d09364c6250c0f48102d2e0"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_251000_amp_3Bsid_9cb115aff7d3b8ba5814f106b2283f26", captured: "20051031004329", sha256: "ca80969ff9beb76bbfb18a7c15595b85002547527b64a926e63f810b4f598513", wayback_url: "https://web.archive.org/web/20051031004329/http://www.toolkitzone.com/forums/viewtopic.php?p=251000&amp%3Bsid=9cb115aff7d3b8ba5814f106b2283f26"}
links:
  - {url: "http://www.bloodshed.net/devcpp.html", status: "external", local: null}
---

# Help with VB Plugin SDK (TK 3.0.4+)

### Dragen · 2005-08-26 22:09 · #B250591

I just downloaded VB Plugin SDK (TK 3.0.4+) and I'm stupid... I can't figure out how to use it Sad I just need to know how to start and I should be able to pick up the rest... The problem is I don't know what files to edit or whatever....

### Colin · 2005-08-26 22:21 · #B250596

The readme tells you how to set up the plugin.
Actually making the plugin is easy if you know VB. modRpgCode, for example, has comments that show how to code RPGCode functions.

### Dragen · 2005-08-26 22:27 · #B250598

I've read the readme

**Colin's Readme wrote:**

> IF the plug's file is plug.dll, then...
> --in VB6
> Rename the project: plug
> Rename clsMain: clsPlug
> --in VB.NET
> Change the constant in modMisc (PROGRAM_ID) to
> "plug"
>

What's the project???
What file do I use to create/edit a plugin??

### Colin · 2005-08-26 22:49 · #B250607

Do you not know the programming language Visual Basic? If you don't, making a plugin is not a good way to learn.
You need Visual Basic 6.

### Dragen · 2005-08-26 23:53 · #B250629

Oh. OK! Embarassed
I haven't a clue about VB. I thought I'd just kinda pick it up, but hey...
Do you need any programs for C++?
EDIT:
All I want to do is edit a simple .dll plugin to perfect it to my specific needs. I just want something to do this with..

### Notsosuperhero · 2005-08-27 12:11 · #B250864

If you can't do it with Visual Basic, then your sure as hell not going to do it with C++. But if you mean a compiler, then [Dev C++](http://www.bloodshed.net/devcpp.html)

### Dragen · 2005-08-27 13:43 · #B250899

**Notsosuperhero wrote:**

> If you can't do it with Visual Basic, then your sure as hell not going to do it with C++. But if you mean a compiler, then [Dev C++](http://www.bloodshed.net/devcpp.html)
>

Will that let me edit a .dll file??

### Notsosuperhero · 2005-08-27 13:56 · #B250907

Not unless you have the source code for the DLL, or if you have a decompiler, which I will not link you with because its wrong to decompile someone elses DLL.

### Dragen · 2005-08-27 14:15 · #B250917

**Notsosuperhero wrote:**

> Not unless you have the source code for the DLL, or if you have a decompiler, which I will not link you with because its wrong to decompile someone elses DLL.
>

Oh.. ok. Is it still wrong if you give credit to them? Wink

### Notsosuperhero · 2005-08-27 18:25 · #B250997

yes, IMO. Unless they say that you could, but if that was the case they might as well just give you the code.

### Dragen · 2005-08-27 18:29 · #B251000

ok.
