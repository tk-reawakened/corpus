---
kind: forum-thread
id: "toolkitzone-forums/16547"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "16547"
title: "anyone know the include file for..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=16547"
written: "2005-03-18T06:29:00"
last_post: "2005-03-18T22:49:00"
date_confidence: "exact"
captured: ["20050320051310", "20050329203208", "20050329203627", "20050330235938", "20050330235947"]
author: "Dominea"
repliers: ["God", "Colin"]
authors: ["Dominea", "God", "Colin"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_182128_amp_", captured: "20050329203627", sha256: "bb3df8edde1d75f00209143fa84e651d3158da97561ff16854ccd7453dd0c4ea", wayback_url: "https://web.archive.org/web/20050329203627/http://www.toolkitzone.com/forums/viewtopic.php?p=182128&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_182133", captured: "20050329203208", sha256: "8a97090c9372f31f9faea39bca793c06a8a9e9ee233b100e528487bb7fcedfa2", wayback_url: "https://web.archive.org/web/20050329203208/http://www.toolkitzone.com/forums/viewtopic.php?p=182133"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_182133_amp_", captured: "20050320051310", sha256: "5d001f50fb9264d8d277778e406608bde66e3d0b0cb2f11ea334f3bfdf73a029", wayback_url: "https://web.archive.org/web/20050320051310/http://www.toolkitzone.com:80/forums/viewtopic.php?p=182133&amp"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_182349_amp_", captured: "20050330235938", sha256: "07f7b80f15a07acd3744f0d841c586bafa8ce6640b3c02b1dcdf0e6da7b22989", wayback_url: "https://web.archive.org/web/20050330235938/http://www.toolkitzone.com/forums/viewtopic.php?p=182349&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_182420_amp_", captured: "20050330235947", sha256: "c7f24929cd4a8de9d97b8a76aa3be0fda84594442d41ea4402546683cde5a12a", wayback_url: "https://web.archive.org/web/20050330235947/http://www.toolkitzone.com/forums/viewtopic.php?p=182420&amp="}
links:
  - {url: "http://msdn.microsoft.com/library/default.asp?url=/library/en-us/sysinfo/base/gettickcount.asp", status: "external", local: null}
---

# anyone know the include file for...

### Dominea · 2005-03-18 06:29 · #B182128

GetTickCount();
I cant seem to figure out what include that contains.. I have tried cstdlib and ctime but im at a loss.
Help would be appreciated.

### Dominea · 2005-03-18 07:28 · #B182133

Ahh dont worry about it. I decided to use clock() instead.

### God · 2005-03-18 20:46 · #B182349

Well, for furture reference use MSDN and look at the very bottom it tells what needs to be linked to and what header it is defined in.
<http://msdn.microsoft.com/library/default.asp?url=/library/en-us/sysinfo/base/gettickcount.asp>

**MSDN wrote:**

> Requirements
> Client Requires Windows XP, Windows 2000 Professional, Windows NT Workstation, Windows Me, Windows 98, or Windows 95.
> Server Requires Windows Server 2003, Windows 2000 Server, or Windows NT Server.
> Header
> Declared in Winbase.h; include Windows.h.
> Library
> Link to Kernel32.lib.
> DLL Requires Kernel32.dll.

### Colin · 2005-03-18 22:49 · #B182420

Just #include <windows.h>, Dommy.
If you're worried about bloat, do a...
#define WIN32_LEAN_AND_MEAN
