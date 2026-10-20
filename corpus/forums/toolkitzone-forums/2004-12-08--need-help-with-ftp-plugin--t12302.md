---
kind: forum-thread
id: "toolkitzone-forums/12302"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "12302"
title: "Need help with FTP plugin"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12302"
written: "2004-12-08T02:08:00"
last_post: "2004-12-09T15:12:00"
date_confidence: "exact"
captured: ["20050116235320"]
author: "word32"
repliers: ["Levi", "Dont_Think_So", "Colosseus"]
authors: ["word32", "Levi", "Dont_Think_So", "Colosseus"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_136992_amp_", captured: "20050116235320", sha256: "aa3318bdcf933e76285ca260489219d1d1e6c592e0d0954a028a474d3cd6daa5", wayback_url: "https://web.archive.org/web/20050116235320/http://www.toolkitzone.com/forums/viewtopic.php?p=136992&amp="}
links: []
---

# Need help with FTP plugin

### word32 · 2004-12-08 02:08 · #B136308

i made the code:
#Prompt ("Enter your message.", text$")
#ftpconnect("ftp.biz.ly","fastcheats.biz.ly","**********")
#ftpopen("messages.txt")
#ftpread("message:")
#ftpread("text$")
#Ftpclose ()
And it says:
Error: Method not found!-- #ftpconnect("ftp.biz.ly","fastcheats.biz.ly","nickmarble")
Error: Method not found!-- #ftpopen("messages.txt")
Error: Method not found!-- #ftpread("message:")
Error: Method not found!-- #ftpread("text$")
Error: Method not found!-- #Ftpclose ()
And the plugin is installed
thanks in advance,
word32

### Levi · 2004-12-08 02:12 · #B136314

Are you testing the game or the just the program?
Because I'm not sure if TK3 fixed this or not but originally you could only test programs with plugins if you were runing the game itself.

### Dont_Think_So · 2004-12-08 02:21 · #B136326

Not only that, but several plugins don't work with TK3.

### Levi · 2004-12-08 02:23 · #B136330

Oh, good point. I don't use TK3 often or at all so I keep forgetting that one.

### word32 · 2004-12-09 00:30 · #B136698

Thanx i have TK2

### Colosseus · 2004-12-09 15:12 · #B136992

... Try it on TK3 then Razz
