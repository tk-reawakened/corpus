---
kind: forum-thread
id: "acforum/7476"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "7476"
title: "Can you debugg this to?"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=7476"
written: "2003-08-12T08:40:00"
last_post: "2003-08-12T15:41:00"
date_confidence: "exact"
captured: ["20030914134723", "20030914134755"]
author: "william"
repliers: []
authors: ["william"]
posts_present: 2
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_7476", captured: "20030914134723", sha256: "53ff5101d9f97413e516e5a74e64b69b583cfb04f4a23a176b29d99c0116ac88", wayback_url: "https://web.archive.org/web/20030914134723/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=7476"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_7479", captured: "20030914134755", sha256: "69204abbc3f3c5d4ede61eb42be0c062db76b928fd81d0741294dc2a00add293", wayback_url: "https://web.archive.org/web/20030914134755/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=7479"}
links: []
---

# Can you debugg this to?

### william · 2003-08-12 08:40 · #A1001-7476

#job! =1*take this away when program is in use
#done!=0
#While(done!=0)
{
#SetImageTransparent("Mwin.jpg",4,4,600,120,255,0,0)
#SetImage("bjorn.bmp",20,25,87,98)
#Text(6,1.5,"Name")
#Text(6,2.5,"Do you want to get some money very fast and easy")
#Text(6,3.5,"You just have to leave a message to one of my friend that I'am")
#Text(6,4.5,working with.")
#Text(6,2.5,"1- A message to Alvin, gives you 30 gold.")
#Text(6,3.5,"2- A message to Kevin, gives you 45 gold.")
#Text(6,4.5,"3- A message to Mark, gives you 65 gold.")
#Text(6,5.5,"4- No, I dont want to, maybe later.")
*Text end:
*--------------------------------------------------------------------------------
#Wait(q$)
#if (q$=="1")
{
#if (alvin! == 1)
{
#SetImageTransparent("Mwin.jpg",4,4,600,120,255,0,0)
#SetImage("bjorn.bmp",20,25,87,98)
#Text(6,1.5,"Name")
#Text(6,2.5,"")*You found him....
#Text(6,3.5,"")
#Text(6,4.5,"")
#system.pause()
}
#if (alvin! == 0)
{
#SetImageTransparent("Mwin.jpg",4,4,600,120,255,0,0)
#SetImage("bjorn.bmp",20,25,87,98)
#Text(6,1.5,"Name")
#Text(6,2.5,"")*He is in the next...
#Text(6,3.5,"")
#delay(5)
#wait()
}
#done! = 1
}
#if (q$=="2")
{
#if (kevin! == 1)
{
#SetImageTransparent("Mwin.jpg",4,4,600,120,255,0,0)
#SetImage("bjorn.bmp",20,25,87,98)
#Text(6,1.5,"Name")
#Text(6,2.5,"")*You found him....
#Text(6,3.5,"")
#Text(6,4.5,"")
#system.pause()
}
#if (kevin! == 0)
{
#SetImageTransparent("Mwin.jpg",4,4,600,120,255,0,0)
#SetImage("bjorn.bmp",20,25,87,98)
#Text(6,1.5,"Name")
#Text(6,2.5,"")*He is in the next...
#Text(6,3.5,"")
#delay(5)
#wait()
}
#done! = 1
}
#if (q$=="3")
{
#if (mark! == 1)
{
#SetImageTransparent("Mwin.jpg",4,4,600,120,255,0,0)
#SetImage("bjorn.bmp",20,25,87,98)
#Text(6,1.5,"Name")
#Text(6,2.5,"")*You found him....
#Text(6,3.5,"")
#Text(6,4.5,"")
#system.pause()
}
#if (mark! == 0)
{
#SetImageTransparent("Mwin.jpg",4,4,600,120,255,0,0)
#SetImage("bjorn.bmp",20,25,87,98)
#Text(6,1.5,"Name")
#Text(6,2.5,"")*He is in the next...
#Text(6,3.5,"")
#delay(5)
#wait()
}
#done! = 1
}
#if (q$=="3")
{
#SetImageTransparent("Mwin.jpg",4,4,600,120,255,0,0)
#SetImage("bjorn.bmp",20,25,87,98)
#Text(6,1.5,"Name")
#Text(6,2.5,"Come back later.")
#system.pause()
#done! = 1
}
}
Mr.B

### william · 2003-08-12 15:41 · #A1001-7479

**get profile$...**

Hi, whats the command to get the profile picture? Like I putt a picture of my character in the char deitor and then I want to have
the profile in my custom menu, but I dont want to use this command: #SetImage(bjorn.bmp,45,15,87,98)
Something like this I think:
#getprofile(Porfile$)
#SetImage(profile$,45,15,87,98)
Mr.B
