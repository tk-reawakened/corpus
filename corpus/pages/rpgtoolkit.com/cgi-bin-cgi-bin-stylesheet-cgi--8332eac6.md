---
kind: page
id: "rpgtoolkit.com/rpgtoolkit.com/cgi-bin/cgi-bin/stylesheet.cgi"
site: "rpgtoolkit.com"
title: "Current Release: 3.0.1"
original_url: "http://rpgtoolkit.com/cgi-bin/cgi-bin/stylesheet.cgi"
written: null
date_confidence: "unknown"
updated: null
captured: ["20031216211859"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/cgi-bin/stylesheet.cgi", captured: "20031216211859", sha256: "04d50fa5b518779f7c776709fd37f08fc68cce194242c45407a42c408eaeda31", wayback_url: "https://web.archive.org/web/20031216211859/http://rpgtoolkit.com/cgi-bin/cgi-bin/stylesheet.cgi"}
---

# Current Release: 3.0.1

Home of the Free RPG Toolkit Development System for the Creation and Play of your own RPG Games
Theme: v2 blueberry classic
December 11, 2003 - Putting a process in place.
I have received several requests to set up a CVS server for people who want to make changes to TK3. I already use a CVS server, but it's not a good idea to let just anyone make commits to the source tree. I'd like to code review things that go into the project first, which will ensure everything is on the up-and-up. To this end, I've written up some for you to follow if you have made changes and would liek to see them included in TK3. If everything is cool, I will commit the changes to CVS. In time, maybe others will be given commit-access to the CVS server. I'm very greatful for all the interest the open-sourcing of TK3 has generated so far.
December 7, 2003 - Making way for the future.
There are a couple of big announcements today. First of all, I have released a new version of the Toolkit, mostly with bug fixes, but also with the new sound system. Secondly, after much much [much] thought, I have decided to change the licensing scheme for Toolkit 3. It's going . In the long run, this will be much better for the Toolkit and the community than if I were to continue it on my own. I have written a document which explains my reasons for this very big decision. This has several implications. I'm no longer offering version 2 for registration purposes. I will fill the remainder of the Version 2 Powerhouse Orders, but beyond that, version 2 is being retired. Version 2 will not be open sourced, so don't ask about it. It would be unfair to the many people who have supported me by registering to open source version 2 as well (since they have also paid to see the source code).
November 11, 2003 - New server
Well, if you can read this, then the transition of the rpgtoolkit.com domain worked. I've moved the site onto my own server, because of the fiasco with the server company I was dealing with. I'm now using forms graciously hosted by Cy. You can get to the , but it will only be up for about one more month... The bug forum has been replaced with a Bugzilla database. This will make tracking bugs much easier. Now for some Toolkit news: Throughout the summer, I was exteremely busy with moving and my new job. That's why things were moving so slowly with the Toolkit. But things are stating to settle a bit and I've recently been able to get a lot of work done. This mostly includes bugfixes, but I've also been working at making the graphics engine more efficient. In the first couple of TK3 releases, I was still depending upon GDI to some extent for the graphics system. This has now been (mostly) resolved. Almost all calls now go directly through DirectX, meaning that the real bottleneck in the system (tile rendering) is now a lot faster. I have also replaced the multimedia subsystem. I no longer use ModPlug or the old mp3 OCX control. The new system uses (the same audio system developed for Sphere). This means that TK3 now supports OGG files, and surround sound. I'm going to continue to work away at the bugs and hopefully I'll have something for you all shortly.
October 19, 2003 - Forced onto new forums
Hi, everyone. We're permanently moving onto the new forums. You'll find their links to the left. This is the result of a disagreement I have been having with my webhost. You can read all about it in the General Forum . For those of you who loved the old forums, I'm sorry. For those of you who love the new forums, celebrate :) In any event, I'm sure things will carry on as normal.
![](http://fastcounter.linkexchange.com/fastcounter?913381+1826769)
The RPG Toolkit is an extremely flexible development system for creating Role Playing Games. The Standard Edition is absolutely free, and thousands of people worldwide are developing games with it. your own copy and start developing your dream game today! The Toolkit has a grass-roots community of RPG enthusiasts who are both helpful and extremely creative. Join the now! What is the RPG Toolkit?
- *Available in English*
- *Vorhanden auf Deutsch*
- *Disponible en français*
- *Disponible en español*
- *Disponibile in italiano*
My name is Christopher Matthews. I am a recent graduate of in Halifax, Nova Scotia, Canada (majoring in ). I have been developing the Toolkit for almost now. I am constantly working to improve the system and bring a better RPG experience to everyone who uses it. Who created the RPG Toolkit?
