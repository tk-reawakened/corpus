---
kind: forum-thread
id: "acforum/19389"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "19389"
title: "Fishing Program"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=19389"
written: "2002-08-17T30:04:00"
last_post: "2002-08-18T21:04:00"
date_confidence: "exact"
captured: ["20020829000130", "20020829001355", "20020901015525"]
author: "imakerpgsnow"
repliers: ["mystery"]
authors: ["imakerpgsnow", "mystery"]
posts_present: 3
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_19389", captured: "20020829000130", sha256: "ec2133b18368d5fdb07ebf7f58354fb7224fa6aa5b23e194bf6f0ddc93719670", wayback_url: "https://web.archive.org/web/20020829000130/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=19389"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_19400", captured: "20020829001355", sha256: "f9e35ada872c3f93fcb5c8dfc0ed1f0d39b7b110fb9957866a8d73a7de8aface", wayback_url: "https://web.archive.org/web/20020829001355/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=19400"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_19425", captured: "20020901015525", sha256: "62e8975cdbf656d5995f6a4ae757778859ba79ac73b98307957ecf59f8f60b42", wayback_url: "https://web.archive.org/web/20020901015525/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=19425"}
links: []
---

# Fishing Program

### imakerpgsnow · 2002-08-17 30:04 · #A1001-19389

Any1 have some sort of a fishing program. Some way to make a mini game where you could fish.
Even a program that just randomly grants you a fish or not when you walk up to water and "cast your line out into the water" would be nice.
Plz help so that I can go make RPGs now!
A camp without fire, is like a fire without wood.

### mystery · 2002-08-18 16:01 · #A1001-19400

**I have on but...(more)**

I'm going to have it custom in my game, sorry.
But, there is a way to make one-- kind of like this.
#Mwin("Cast rod?")
@
#Mwin("Yes) 1")
#Mwin("No) 2")
#Done!=0
#While(Done!==0)
{
#Wait(Cast!)
#If(Cast!==1)
{
#Mwincls
#Mwin("Okay!")
#Wait(a$)
#Mwincls
#NewPlyr("Fishing")
#PutPlayer("Fishing",x!,y!,layer!)
#Random(100,Fish!)
#If(Fish!>= 50)]
{
#Mwincls
#Mwin("You caught a fish!")
#Wait(a$)
#Giveitem("Fish")
#NewPlyr("RegularGuy")
#Done!==1
}
#If(Cast!==2)
{
#Mwincls
#Mwin("Okay then.")
#Wait(a$)
#Done!==1
}
}
In my game, I have different types of fish, different weights, and different lures, bait, and flies.
Good Luck! And I hope that helps!
???Mystery???

### imakerpgsnow · 2002-08-18 21:04 · #A1001-19425

**Thanks!**

After a good 45 minutes of tinkering with your program and several others that work with it, Players can now fish at a pond in my RPG! Thanks!
A camp without fire, is like a fire without wood.
