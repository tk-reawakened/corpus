---
kind: forum-thread
id: "toolkitzone-forums/22767"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Programming"
skin: "phpbb2"
thread_id: "22767"
title: "Creating Executables with C++"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=22767"
written: "2005-08-22T19:33:00"
last_post: "2005-08-23T19:54:00"
date_confidence: "exact"
captured: ["20051031003814", "20051231085828", "20051231085852"]
author: "motar"
repliers: ["TheCPPFreak220", "Colin"]
authors: ["motar", "TheCPPFreak220", "Colin"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_249288_amp_3Bsid_d7a684e60b35a7ac1c69c08d08ce60c5", captured: "20051231085828", sha256: "168c1fca2f49c9cc14998ae46197c7ea76ba7e8fda40e5f1331b648db12b0de7", wayback_url: "https://web.archive.org/web/20051231085828/http://www.toolkitzone.com/forums/viewtopic.php?p=249288&amp%3Bsid=d7a684e60b35a7ac1c69c08d08ce60c5"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_249292_amp_3Bsid_d7a684e60b35a7ac1c69c08d08ce60c5", captured: "20051231085852", sha256: "a44363e18139db7588b5c3888cce93c34be899256a49674a25ecbfce7dc03926", wayback_url: "https://web.archive.org/web/20051231085852/http://www.toolkitzone.com/forums/viewtopic.php?p=249292&amp%3Bsid=d7a684e60b35a7ac1c69c08d08ce60c5"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_249473_amp_3Bsid_9cb115aff7d3b8ba5814f106b2283f26", captured: "20051031003814", sha256: "4f0d24367f71a1635bad0930a6937c173b219a0fdf69b4b6077c6899d37589e4", wayback_url: "https://web.archive.org/web/20051031003814/http://www.toolkitzone.com/forums/viewtopic.php?p=249473&amp%3Bsid=9cb115aff7d3b8ba5814f106b2283f26"}
links:
  - {url: "http://sourceforge.net/projects/rpgtoolkit/", status: "external", local: null}
  - {url: "http://tk3.toolkitzone.com/source", status: "never-captured", local: null}
---

# Creating Executables with C++

### motar · 2005-08-22 19:33 · #B249100

After doing a bit of work on my own RPG engine modeled after the toolkit, I discovered I'd run into a problem: I didn't know how to let the user create an executable of his or her game. Is there any function(or set of functions, class, structure, etc.) that allows you to bundle files into a .exe(say, in the default libraries that come with most compilers)?

### TheCPPFreak220 · 2005-08-23 03:43 · #B249288

look at the tk's source:
<http://sourceforge.net/projects/rpgtoolkit/>

### Colin · 2005-08-23 03:56 · #B249292

That's actually a useless reply, but I'd like to note that you won't find the up-to-date source there. Downloading the source packages is useless. They exist only for historical purposes.
<http://tk3.toolkitzone.com/source>

### motar · 2005-08-23 19:54 · #B249473

Er... well, when I said modeled after the TK, I just meant the engine would be sort of like it. I just wanted to know the typical way this would be done with C++, not necessarily how to do it through or with the Toolkit.
