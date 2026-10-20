---
kind: forum-thread
id: "toolkitzone-forums/10816"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "10816"
title: "Cross-Platform UDP library for C++"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10816"
written: "2004-10-30T16:02:00"
last_post: "2004-10-30T16:37:00"
date_confidence: "exact"
captured: ["20041226085857"]
author: "ArchGaden"
repliers: ["Colosseus"]
authors: ["ArchGaden", "Colosseus"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_119238_amp_", captured: "20041226085857", sha256: "33a0c641dac11b32b2617ba5fdac975a2976620d8e27699ca43da8d8f3c5a716", wayback_url: "https://web.archive.org/web/20041226085857/http://www.toolkitzone.com/forums/viewtopic.php?p=119238&amp="}
links: []
---

# Cross-Platform UDP library for C++

### ArchGaden · 2004-10-30 16:02 · #B119222

Does anyone know of a cross-platform UDP network library ? I'm still try to set a foundation for the MMORPG server..and I'm stuck on a decision between Overlapping I/O with completion ports or UDP. Completion ports are a windows NT feature..so if I go that route, things are very platform restrictive. UDP has potential to provide more portability, but I don't have enough Unix/Linux experience to work with things there... instead, I want to use a cross-platform code library instead of relying on API calls to do everything. I've got Overlapping I/O with TCP down, but potentially there are some advantages in using UDP that I want to look into.
I've only found one library that fits the needs, but the win32 implentation is barely documented. I scoured the net only to find a handful of forum posts that don't cover the topic in enough detail. Basically, this code library has the potential to work in win32, but there isn't enough interest for anybody to document how it can be done. They provide a corrupted VC++ .dsp file..not sure why they think a corrupt file is useful. A few people complained about it, but there was never a solution. Ultimately, I can't get rid of a slew of compiler errors that result from trying to use their code library. The fix for that is likely horribly simple..just a few compiler options need to be changed, but thats like finding the needles in the haystack.
Anyway..the library is called enet (http://enet.cubik.org/). If anyone can figure how to setup a basic project with that in VC++, it would be much appreciated. Or if anyone knows of another cross-platform UDP network library, I could try and attempt that. Otherwise, I have to implement everything with winsock, an amazingly well documented win32 library for network protocols, and any would be future linux users will have to suffer the shame of having a platform with poorely documented libraries.

### Colosseus · 2004-10-30 16:22 · #B119233

I don't know about any cross-platform libraries, but the Indy library for Delphy is amazing.

### ArchGaden · 2004-10-30 16:37 · #B119238

I finally got things to compile...after mucking around for about 4 hours yesterday and another 2 today, I figured out that the 'main' function had to be declared in a very specific way. Of course, that was documented anywhere...how cool is that ?
