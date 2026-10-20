---
kind: forum-thread
id: "toolkitzone-forum/35194"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "35194"
title: "*Resolved* text() on top of an setimage? w/o translucent??"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=35194"
written: "2007-02-14T14:02:00"
last_post: "2007-02-14T22:37:00"
date_confidence: "exact"
captured: ["20070302170749"]
author: "decker666"
repliers: ["tc", "Xioyn", "zyrshnikashnu"]
authors: ["decker666", "tc", "Xioyn", "zyrshnikashnu"]
posts_present: 8
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_379828", captured: "20070302170749", sha256: "26adace13aa1e6b183fd52f3bb0efc0b4dc593a37afb11737c338f711303a2e7", wayback_url: "https://web.archive.org/web/20070302170749/http://www.toolkitzone.com/forum/viewtopic.php?p=379828"}
links: []
---

# *Resolved* text() on top of an setimage? w/o translucent??

### decker666 · 2007-02-14 14:02 · #K379816

this is really annoying me, what is it you need to do to make text(0,0, "hi!") appear on top of SetImage("Battle_Menu.bmp", 0, 320, 640, 150) im attempting to make a menu for a CBS and, without setting it translucent, i cannot make the text appear ON TOP OF the image...sometimes i can get it to show on top [with other programs i mean] without doing anything, others i just cant get them to set on top...helps appreciated

### tc · 2007-02-14 14:13 · #K379818

can you post your code, that could help figuring what the problem is

### decker666 · 2007-02-14 14:45 · #K379827

its very basic, i mean theres no TRUE reason that i can find as to why it wont show on top but here is how the code goes [code]CFight
Method CFight()
{
DrawMenu()
}
Method DrawMenu()
{
Text(0,0, "hi!")
SetImage("Battle_Menu.bmp", 0, 0, 640, 150)
}
its just that the text wont show over the image, i gtg now, typing from class will reply once home

### Xioyn · 2007-02-14 14:56 · #K379828

Wouldn't you just switch them around from what it looks like you put the text then the image on top but I don't use text right now

### tc · 2007-02-14 15:31 · #K379830

you see, that is the reasson why you should always post your code, most problems are something very silly, like putting the command in the wrong order

### decker666 · 2007-02-14 22:17 · #K379942

yes, im sure if that would work, it would solve my problem, BUT, it doesnt, does the exact same thing, image over the text

### zyrshnikashnu · 2007-02-14 22:20 · #K379947

It will. You're setting text and then putting an image over it. Why wouldn't the image come to the front?

### decker666 · 2007-02-14 22:37 · #K379954

... sorry...yes it does, i just found the problem, 0,0 coords for text in a method arnt onscreen >.<, i tried things lkie 3,5 and it shows up...heh sorry for the bother -feels very crunchy now-
