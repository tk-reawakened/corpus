---
kind: forum-thread
id: "acforum/15984"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "15984"
title: "I'm still dumb and need help (more)"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1000&mode=1&msg=15984"
written: "2002-02-04T15:11:00"
last_post: "2002-02-04T15:11:00"
date_confidence: "exact"
captured: ["20020211200202"]
author: "jakeao"
repliers: []
authors: ["jakeao"]
posts_present: 1
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1000_mode_1_msg_15984", captured: "20020211200202", sha256: "4366fd56b0a8923e5aea027e1f000e4db77113c48ee73551217c675375e17cfa", wayback_url: "https://web.archive.org/web/20020211200202/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1000&mode=1&msg=15984"}
links: []
---

# I'm still dumb and need help (more)

### jakeao · 2002-02-04 15:11 · #A1000-15984

I'm having trouble with this code.
after I press 1 or 2 it runs the program but then the debugger comes up and crashes the dang thing. (3 and 4 work jsut fine though) thanks for any help.
#wingraphic("window.bmp")
#font("data")
#fontsize(16)
#mwin("")
#Mwin(" bla bla bla")
#Wait(a$)
#MWinCls()
#mwin("")
#Mwin("bla bla bla")
#Wait(a$)
#done!=0
#While(done!==0)
{
#mwincls()
:main
#mwin("")
#Mwin(" 1 - comment on his hair.")
#Mwin(" 2 - ask who's in charge.")
#Mwin(" 3 - tell him off")
#Mwin(" 4 - continue on your adventure.")
#Wait(result$)
#mwincls()
#If(result$="1")
{
#mwin("")
#Mwin("bla bla bla")
#Wait(a$)
#MWinCls()
#mwin("")
#Mwin("bla bla bla")
#wait(a$)
#mwincls()
#done!=1
#Branch(:main)
}
#if(result$="2")
{
#mwin("")
#Mwin("bla bla bla")
#wait(a$)
#Mwincls ()
#mwin("")
#Mwin("bla bla bla")
#wait(a$)
#Mwincls()
#mwin("")
#Mwin("bla bla bla")
#wait(a$)
#Mwincls()
#mwin("")
#mwin(" bla bla bla")
#wait(a$)
#Mwincls()
#done!=1
#Branch(:main)
}
#if(result$="3")
{
#mwin("")
#Mwin("bla bla bla")
#wait(a$)
#Mwincls()
#mwin("")
#Mwin("bla bla bla")
#wait(a$)
#mwincls()
#mwin("")
#Mwin("bla bla bla")
#wait(a$)
#mwincls()
#mwin("")
#Mwin("bla bla bla")
#wait(a$)
#mwincls()
#mwin("")
#Mwin("bla bla bla")
#wait(a$)
#Mwincls()
#mwin("")
#Mwin("bla bla bla")
#wait(a$)
#mwincls()
#mwin("")
#mwin("bla bla bla")
#wait(a$)
#Mwincls()
#done!=1
}
#if(result$="4")
{
#mwin("")
#Mwin("bla bla bla")
#wait(a$)
#mwincls()
#mwin("")
#mwin("bla bla bla")
#wait(a$)
#mwincls()
#done!=1
}
}
