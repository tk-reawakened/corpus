---
kind: forum-thread
id: "toolkitzone-forums/23416"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Programming"
skin: "phpbb2"
thread_id: "23416"
title: "I need help with Assembly"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23416"
written: "2005-09-11T02:45:00"
last_post: "2005-09-11T02:45:00"
date_confidence: "exact"
captured: ["20051018074104", "20051225210400"]
author: "TKFanBoy"
repliers: []
authors: ["TKFanBoy"]
posts_present: 1
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_256231", captured: "20051225210400", sha256: "aa71abeba08c88c429074961dc4f714a5633a0407580a459e7352ea6ed00e952", wayback_url: "https://web.archive.org/web/20051225210400/http://www.toolkitzone.com/forums/viewtopic.php?p=256231"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_256231_amp_3Bsid_2d4b9306af6d1b871ab294752492fbe1", captured: "20051018074104", sha256: "290f377592ef77163f45da42568b3178e214af88a7180c74c4c70b21f5be4a25", wayback_url: "https://web.archive.org/web/20051018074104/http://www.toolkitzone.com/forums/viewtopic.php?p=256231&amp%3Bsid=2d4b9306af6d1b871ab294752492fbe1"}
links: []
---

# I need help with Assembly

### TKFanBoy · 2005-09-11 02:45 · #B256231

Hi, I'm starting to learn assembly right now and I'm using MASM 6.15
now on the book I got, it says that sign flag would be 1 if the result of the operation is negative
HEre's my code

**Code:**

```
Title Add and Subtract, Version 2 (AddSub2.asm)

INCLUDE Irvine32.inc

.data

val1 BYTE 10h

val2 WORD 8000h

val3 DWORD 0FFFFh

val4 WORD 7FFFh

.code

main Proc

  mov ax, val2   ;ax is now 8000h

  add ax, 1h ; should be 8001h, and should be positive

  call DumpRegs

  exit

main ENDP

 END main
```

However, the result showed that SF = 1
Why's that?
Shouldn't it be zero because the result is positive?
