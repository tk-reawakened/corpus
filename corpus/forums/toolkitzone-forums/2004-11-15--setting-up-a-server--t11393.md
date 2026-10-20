---
kind: forum-thread
id: "toolkitzone-forums/11393"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "computing & technology"
skin: "phpbb2"
thread_id: "11393"
title: "Setting up a server..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11393"
written: "2004-11-15T23:41:00"
last_post: "2004-11-16T10:53:00"
date_confidence: "exact"
captured: ["20041226222418"]
author: "zzz"
repliers: ["Dont_Think_So", "sivart", "matt72186", "Dan", "Spyder", "Randy"]
authors: ["zzz", "Dont_Think_So", "sivart", "matt72186", "Dan", "Spyder", "Randy"]
posts_present: 11
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_125832_amp_", captured: "20041226222418", sha256: "5328311f7c630a9fedaaa2d09ca895cc63c8a386ac7bb61c4c9d517c7b95f1c7", wayback_url: "https://web.archive.org/web/20041226222418/http://www.toolkitzone.com/forums/viewtopic.php?p=125832&amp="}
links:
  - {url: "http://httpd.apache.org", status: "external", local: null}
  - {url: "http://www.apache.org", status: "external", local: null}
  - {url: "http://www.mysql.com", status: "external", local: null}
  - {url: "http://www.php.net", status: "external", local: null}
  - {url: "http://www.xitami.com,", status: "external", local: null}
---

# Setting up a server...

### zzz · 2004-11-15 23:41 · #B125687

Ok, i got a few questions for setting up a server to host a site...
1)what prg do i need
2) i need to be on 24/7 right? (to be it up)
3) does it make the net run slow
meh, thats all i can think, cuz if i could, i wanna run a server off my schools connection...

### Dont_Think_So · 2004-11-15 23:55 · #B125694

[www.xitami.com,](http://www.xitami.com,) or maybe its .org... something like that.

### sivart · 2004-11-15 23:57 · #B125695

1)no idea , finish the game first Razz
2)Yes
3)Think so

### matt72186 · 2004-11-16 00:15 · #B125717

**sivart wrote:**

> 1)no idea , finish the game first Razz
> 2)Yes
> 3)Think so
>

Answers all right, answer to #1...
[www.apache.org](http://www.apache.org)

### Dan · 2004-11-16 00:29 · #B125723

If your server is a web server and you want a decent one, you'll need to set yourself up with [Apache](http://httpd.apache.org), [PHP](http://www.php.net) and [MySQL](http://www.mysql.com).
Unless you know what you are doing though, it's not easy at all and I wouldn't recommend running a live server off your home computer anyway.

### Dont_Think_So · 2004-11-16 00:57 · #B125728

Xitami is made for beginners. You literally install it and let it run.

### zzz · 2004-11-16 01:27 · #B125736

**Dan wrote:**

> If your server is a web server and you want a decent one, you'll need to set yourself up with [Apache](http://httpd.apache.org), [PHP](http://www.php.net) and [MySQL](http://www.mysql.com).
> Unless you know what you are doing though, it's not easy at all and I wouldn't recommend running a live server off your home computer anyway.
>

not off my home, check my first mesage, it says off my school Razz

### Spyder · 2004-11-16 02:15 · #B125747

You could get in some serious trouble for that. Besides, it probably won't even work. Your school probably uses routers and firewalls; things that will make setting up a server quite difficult unless you have access to them.

### Randy · 2004-11-16 03:17 · #B125779

Yeah it's not going to work at school because you have to have port 80 open, and unless your school's IT department consists of bumbling idiots, that port is not going to be open.

### Dont_Think_So · 2004-11-16 04:03 · #B125788

Xitami uses any port. Razz
Im using port 6010 right now, though the server isn't running. I changed it because I wanted only people who knew about it to actually try connecting on that port.

### Spyder · 2004-11-16 10:53 · #B125832

You would have to type :6010 after the address though, which would make things complicated for the average user because they have no idea what that means. I'm pretty sure Apache can use any port as well, but if your going to have an HTML server, your best using the default port 80.
