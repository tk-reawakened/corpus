---
kind: forum-thread
id: "toolkitzone-forums/6829"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced rpg code"
skin: "phpbb2"
thread_id: "6829"
title: "Image Manipulation"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=6829"
written: "2004-08-07T02:01:00"
last_post: "2004-08-07T02:01:00"
date_confidence: "exact"
captured: ["20040915043150"]
author: "Nick"
repliers: []
authors: ["Nick"]
posts_present: 1
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_71176_amp_", captured: "20040915043150", sha256: "4437b7a46f97794459222211e13c0e7a6ccc312c53236b774203ee9e9639bb7c", wayback_url: "https://web.archive.org/web/20040915043150/http://www.toolkitzone.com/forums/viewtopic.php?p=71176&amp="}
links:
  - {url: "http://saoghal.cywh.com/Stadsport/banner.gif", status: "external", local: null}
---

# Image Manipulation

### Nick · 2004-08-07 02:01 · #B71176

This is just an example sort of thing. Really has no practical use.
It draws an image (Put the filename, width and height in the method. Cannot define location, sorry. I'm lazy). Then it copies it and also makes a skewed copy. As I said it really doesn't have a practical use, but hey, it could be something to dig into deeper.

**Code:**

```
#CopyImage("Dog.jpg",100,70)

#wait

#Method CopyImage(image$,width!,height!)

{

#Setimage(image$,1,1,width!,height!)

#y!==1

#sety!=y!

#removey!=width!-1

#while(y!<=height!)

{

 #for(x!=1;x!<=width!;x!=x!+1)

 {

 #getpixel(x!,y!,r!,g!,b!)

 #colorrgb(r!,g!,b!)

 #setx!=x!+width!

 #setx!=setx!+20

 #sety!=sety!+1

 #setpixel(setx!,sety!)

 }

#y!=y!+1

#sety!=sety!-removey!

}

#y!=1

#while(y!<=height!)

{

 #for(x!=1;x!<=width!;x!=x!+1)

 {

 #getpixel(x!,y!,r!,g!,b!)

 #colorrgb(r!,g!,b!)

 #sety!=y!+height!

 #sety!=sety!+20

 #setpixel(x!,sety!)

 }

#y!=y!+1

}

}
```

Please excuse my inefficient coding as I just did it out of boredom.
_________________
![](http://saoghal.cywh.com/Stadsport/banner.gif)
