---
kind: forum-thread
id: "acforum/19396"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "19396"
title: "What is a \"plugin\""
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=19396"
written: "2002-08-18T12:38:00"
last_post: "2002-08-18T23:11:00"
date_confidence: "exact"
captured: ["20020829001326", "20020829001343", "20020901015845"]
author: "Grandpa"
repliers: ["ersuis"]
authors: ["Grandpa", "ersuis"]
posts_present: 3
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_19396", captured: "20020829001326", sha256: "339334c621b21a289605d8d79274cd8245786fc0b60a0883dbcf1dee109f7619", wayback_url: "https://web.archive.org/web/20020829001326/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=19396"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_19398", captured: "20020829001343", sha256: "91047166b89a8a8511d100806ea96332fb6729ee3529d79733a2fbbde501bad4", wayback_url: "https://web.archive.org/web/20020829001343/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=19398"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_19426", captured: "20020901015845", sha256: "d6fd90bf3f9f5bbfaad63a850d466ace42bf7791b0b3538a4b02a03e961e143c", wayback_url: "https://web.archive.org/web/20020901015845/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=19426"}
links:
  - {url: "http://www.thelaironline.com", status: "external", local: null}
---

# What is a "plugin"

### Grandpa · 2002-08-18 12:38 · #A1001-19396

Hello, I am new at this computer stuff. I am trying to make a game for my grandson. What is a "plugin" how could it help me, where do I get them, and how do I use it? Thanks Grandpa

### ersuis · 2002-08-18 15:37 · #A1001-19398

**A plugin is...(more)**

A dll written in another computer language. Plugins for the RPGTK usually just add new RPGCode commands for things like getting enemy information or putting graphics on the screen.
To use them, I suggest both downloading the multiplug available here (rpgtoolkit.com) and the plugin itself (pretty much all plugins can be found at mrgoldsoft.mysticsoftware.net). After the multiplug is downloaded, unzip and copy tkplugx to your Toolkit2/Plugin folder. Rename it to tkplug0, and go into the main file for your game. In the Plugin section of the main file, enable tkplug0. Now you can use as many plugins as you want, as the multiplug will automatically see if you have any other plugins in your Plugin folder, and it'll handle all the enabling for you. To install another plugin, just copy it to your Plugin folder.
Using them is easy, too. Most plugins come with a readme that includes all the commands available in the plugin. Just call those commands as you would any normal RPGCode command.
-Ersuis
: : : [thelaironline.com](http://www.thelaironline.com) : : :
Just visit it. ;)

### Grandpa · 2002-08-18 23:11 · #A1001-19426

**tThank you for your assistance.**

I appreciate your assistance -- Next I attempt "programming!" as my grandson says -- " A way we go, let the fun began
