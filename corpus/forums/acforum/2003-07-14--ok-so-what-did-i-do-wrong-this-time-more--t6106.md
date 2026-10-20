---
kind: forum-thread
id: "acforum/6106"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "6106"
title: "OK, so what did I do wrong this time?! |more...|"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=6106"
written: "2003-07-14T27:27:00"
last_post: "2003-07-15T09:50:00"
date_confidence: "exact"
captured: ["20030726102609", "20030731035424"]
author: "compugeek"
repliers: ["woozy"]
authors: ["compugeek", "woozy"]
posts_present: 2
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_6106", captured: "20030726102609", sha256: "05ad107e134ccf78562c5b19d6c919d1094f394dc8c0ebeca402f65011f1d8ce", wayback_url: "https://web.archive.org/web/20030726102609/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=6106"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_6116", captured: "20030731035424", sha256: "a08eada2d398a636fa296d5fdd3f39d5ea56007ad89f7f7b62891ebce792cd30", wayback_url: "https://web.archive.org/web/20030731035424/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=6116"}
links:
  - {url: "http://members.lycos.nl/zeoliteproductions//", status: "external", local: null}
  - {url: "http://www.tnation.i8.com//", status: "external", local: null}
---

# OK, so what did I do wrong this time?! |more...|

### compugeek · 2003-07-14 27:27 · #A1001-6106

I am aiming to get a program that makes me immune to certain programs on the board for a few seconds when I press a button in my game. (Basically, it's a very cheap Jump program.) So, I set J as a Run-Time key that activates a program shown below. Of course, when testing my game, none of the text shows up on-screen, and nothing at all happens except that my character freezes until I release the J button.
Never mind that. I just figured out that I set the wrong program (oops :). NOW, it makes the translator freeze when I press the J button. What am I doing wrong (now)?
#AutoCommand
If(Jump!>0)
{
End()
}
Jump!=1
GetTime(JumpStart!)
FontSize(18)
ColorRGB(0000ff)
Text(1,1,"Jump")
:start
GetTime(JumpTime!)
If(JumpTime!{
Branch(:start)
}
ColorRGB(000088)
Text(1,1,"Jump")
:after
GetTime(AfterTime!)
If(AfterTime!{
Branch(:after)
}
Jump!=0
compugeek

### woozy · 2003-07-15 09:50 · #A1001-6116

**Never worked with TK3 but...(m0re)**

the line
If(AfterTime!{
Branch(:after)
}
looks kinda weird for me, I think it should be
If(aftertime!=something)
{
branch(:after)
}
but maybe this is just some tk3 thingy.
You have to be happy with what you got... until you can get something better!
[Visit my site](http://members.lycos.nl/zeoliteproductions//)
[Visit Indy's site](http://www.tnation.i8.com//)
