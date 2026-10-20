---
kind: forum-thread
id: "toolkitzone-forums/11003"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "11003"
title: "Does anyone know how to return ResotreScreenArray() ?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11003"
written: "2004-11-05T02:26:00"
last_post: "2004-11-05T02:54:00"
date_confidence: "exact"
captured: ["20050109194400"]
author: "Dredogol"
repliers: ["matt72186"]
authors: ["Dredogol", "matt72186"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_121463_amp_", captured: "20050109194400", sha256: "f84878cfd41f1fa4db3163d95ca2dae1e6a6ee5f52fa5d1cdaef9b95ef7931be", wayback_url: "https://web.archive.org/web/20050109194400/http://www.toolkitzone.com/forums/viewtopic.php?p=121463&amp="}
links: []
---

# Does anyone know how to return ResotreScreenArray() ?

### Dredogol · 2004-11-05 02:26 · #B121450

Does anyone know how to return RestoreScreenArray as a ReturnMethod() as a return method?
Example:
Method Player3Movement(p3x1!,p3x2!,p3y1!,p3y2!,p3Forward$,p3r!,p3g!,p3b!, RestoreScreenArray(2))
{
If(p3Forward$ == "TRUE")
{
p3x2z!=p3x2!+1
p3y2z!=p3y2!+1
RestoreScreenArray(2, p3x1!,p3y1!,p3x2z!,p3y2z!, p3x1!,p3y1!)
ColorRGB(p3r!,p3g!,p3b!)
p3x1!=p3x1!-20
p3x2!=p3x2!-20
FillRect(p3x1!,p3y1!,p3x2!,p3y2!)
If(p3x1!<=130)
{
p3Forward$ = "FALSE"
}
}
If(p3Forward$ == "FALSE")
{
p3x2z!=p3x2!+1
p3x2z!=p3x2!+1
RestoreScreenArray(2, p3x1!,p3y1!,p3x2z!,p3y2z!, p3x1!,p3y1!)
ColorRGB(p3r!,p3g!,p3b!)
p3x1!=p3x1!+20
p3x2!=p3x2!+20
FillRect(p3x1!,p3y1!,p3x2!,p3y2!)
If(p3x2!>=795)
{
p3Forward$ = "DONE"
}
}
ReturnMethod(p3Forward$)
ReturnMethod(p3x1!)
ReturnMethod(p3x2!)
ReturnMethod(RestoreScreenArray(2))
}
As you can see, I have a ResotreScreenArray(2) as one of my parameters declaring the METHOD...but I don't know how to sepcify WHAT a DestoreScreenArray() is...
I know everything else are String and Varialbes, what WHAT on earth is a RestoreScreenArray() supposed to be???
If someone can answer this...I'll be very pleased, because I'll be able to make multpile animations move across my screen =)
Thanks for any suggestions...

### matt72186 · 2004-11-05 02:54 · #B121463

Don't cross-post topics or else
1) you will not be answered
2) you may be banned for several days
