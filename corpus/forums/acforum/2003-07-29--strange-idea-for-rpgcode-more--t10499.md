---
kind: forum-thread
id: "acforum/10499"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "10499"
title: "Strange idea for RPGCode...(more)"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=10499"
written: "2003-07-29T22:20:00"
last_post: "2003-07-31T11:53:00"
date_confidence: "exact"
captured: ["20030917071151", "20030917072059", "20030917072103", "20030917072131", "20030917072204", "20030917072207", "20030917072339", "20030917072412"]
author: "ersuis"
repliers: ["kronical", "forsakenmarz", "helpmyspacebarsbroke", "asimir", "dan"]
authors: ["ersuis", "kronical", "forsakenmarz", "helpmyspacebarsbroke", "asimir", "dan"]
posts_present: 8
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_10499", captured: "20030917072103", sha256: "6382a2e4cdbc6bf980f0a76c21cbe85fced096a86fcfd1b7586492fd5092a4ae", wayback_url: "https://web.archive.org/web/20030917072103/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=10499"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_10500", captured: "20030917072059", sha256: "ea8715108873ec6f595c98cd7ca1e324338ceb8493bae0f7bc284d013d867c8b", wayback_url: "https://web.archive.org/web/20030917072059/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=10500"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_10501", captured: "20030917072207", sha256: "c887846b700dccff7bf21af7257e81a109f50fe66991738c324bfde880bdff03", wayback_url: "https://web.archive.org/web/20030917072207/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=10501"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_10502", captured: "20030917072131", sha256: "2f08fb8625d772c83a474c783a1dd4b92429fba414f1b0e8daab0f0335dfb292", wayback_url: "https://web.archive.org/web/20030917072131/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=10502"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_10504", captured: "20030917072204", sha256: "d238cd0cf57f3cf22079ddb2d7a4440b6d10b8df2b0fbed9617c1a07e1a49d8b", wayback_url: "https://web.archive.org/web/20030917072204/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=10504"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_10508", captured: "20030917071151", sha256: "701299e752017f4b7b83db1756749afe2045b646768493eeb067c0c476859d1d", wayback_url: "https://web.archive.org/web/20030917071151/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=10508"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_10512", captured: "20030917072339", sha256: "16102ea3734f176386d54eb787a1cf90110576a79e7d7ab1ff885e1117040c29", wayback_url: "https://web.archive.org/web/20030917072339/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=10512"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_10514", captured: "20030917072412", sha256: "81bda3bcc21ae0ceb41e52143784e0b728e706f39c67bddf6f7f809c2153a7af", wayback_url: "https://web.archive.org/web/20030917072412/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=10514"}
links:
  - {url: "http://cywh.com/disc.php?forum=124", status: "external", local: null}
  - {url: "http://cywh.com/sites/retrogamer/sngamesbanner.jpg", status: "external", local: null}
  - {url: "http://gamestudio43.mysticsoftware.net", status: "captured", local: "wayback/mysticsoftware.net/gamestudio43.mysticsoftware.net/index-92ba12"}
  - {url: "http://www.dc-3.co.uk/", status: "external", local: null}
  - {url: "http://www.ebproductions.co.uk/files/starocean/tkchoice.png", status: "external", local: null}
  - {url: "http://www.mozilla.org/products/firebird/", status: "external", local: null}
  - {url: "http://www.sngames.tk", status: "external", local: null}
  - {url: "http://www.sourceforge.net", status: "external", local: null}
---

# Strange idea for RPGCode...(more)

### ersuis · 2003-07-29 22:20 · #A1002-10499

That's a bit of a carryover from C++... namespaces. A namespace basically is a collection of variables and functions.
So how does this come into play with RPGCode? Well, you could define your own namespace with identical functions to RPGCode, like so perhaps:
namespace myGame
{
someGameVariable$
anotherVariable!
method mwin(inText$)
{
*// Put some code here
}
}
This would create an identical mwin function that you could use. Then, perhaps by doing something like so:
usingNamespace myGame::mwin
You could define it so that the system uses your Mwin function instead of the default Mwin.
Another possible use is keeping name conficts from when you use other people's code. Developers could start wrapping their custom battlesystems and and menus into namespaces so that there's no way that their variables would conflict with the variables for your game.
Another use could be for plugin developers. Currently, plugin developers have to be pretty knowledge about all the other plugins to make sure they don't export an RPGCode command with the same name. Add some type of extern command, wrap the plugin functions in the namespace, perhaps like so:
namespace ErsuisMiscPlugin
{
*// Tells the system that we want the GetTickCount in the
*// plugin id'ed as ErsuisMiscPlugin.
extern(ErsuisMiscPlugin.GetTickCount)
}
namespace KaptansPlugin
{
extern(KaptansPlugin.GetTickCount)
}
myMethod()
{
*// Gets the tick count in namespace ErsuisMiscPlugin
ErsuisMiscPlugin::GetTickCount(ticks!)
*// Gets the tick count in namespace KaptansPlugin
KaptansPlugin::GetTickCount(moreTicks!)
}
My $.02. :)

---

-Curt

[Ditch Internet Explorer. Get Mozilla Firebird.](http://www.mozilla.org/products/firebird/)
[SourceForge.net - Need free software? Check the projects here.](http://www.sourceforge.net)

### kronical · 2003-07-29 24:09 · #A1002-10500

**Hmm (more)**

That would be pretty useful... but too complex for RPG Code. Its better to keep RPG Code as simple as it is now... Unless there is a way to simplify namespaces

---
**TK...**
TK1 - Dos
TK2 - Visual Basic
TK3 - C++
TK4 - Three Demensional (3D)
TK5 - 3D, PC or Console
TK6 - 3D Virtual Reality

---
AIM: kronspik
MSN: (redacted: email)
EMAIL: (redacted: email)

---

The Toilet Man

Kronical

Daddy look! A real live loser!

### ersuis · 2003-07-29 24:18 · #A1002-10501

**How much simpler can you get? :p -nt-**

---

-Curt

[Ditch Internet Explorer. Get Mozilla Firebird.](http://www.mozilla.org/products/firebird/)
[SourceForge.net - Need free software? Check the projects here.](http://www.sourceforge.net)

### kronical · 2003-07-29 28:04 · #A1002-10502

**Well... (more)**

#usenamespace(test)
#cheese(var2$)
#namespace test
{
#var! = 29
#var2$ = "Goodness"
#method cheese(a$)
{
#mwin("Cheesy")
}
}

---
**TK...**
TK1 - Dos
TK2 - Visual Basic
TK3 - C++
TK4 - Three Demensional (3D)
TK5 - 3D, PC or Console
TK6 - 3D Virtual Reality

---
AIM: kronspik
MSN: (redacted: email)
EMAIL: (redacted: email)

---

The Toilet Man

Kronical

Daddy look! A real live loser!

### forsakenmarz · 2003-07-29 29:06 · #A1002-10504

**erm... why complicate things so?**

Btw, I thought you were done with the TK? Or is there some secret game that none of us know about.
--------------------------------------------
Maybe, just maybe, a TK resource site is coming soon
--------------------------------------------
A special thanks to Sophia for the avatar, visit her site [here](http://gamestudio43.mysticsoftware.net)!

### helpmyspacebarsbroke · 2003-07-30 24:11 · #A1002-10508

**nO need to complicate a simple system.**

The title says all.

### asimir · 2003-07-30 26:55 · #A1002-10512

**too complicated for the TK**

RPGCode is nice and simple as it is.
if you put in some of the more complicated aspects of programming like that, i can imagine lots of people thinking its too hard and just giving up with the TK
i suppose it would be useful for some situations, but i think that for most of the time it's needlessly complicated
[![](http://cywh.com/sites/retrogamer/sngamesbanner.jpg)](http://www.sngames.tk)

[![Toolkit Choice Awards!](http://www.ebproductions.co.uk/files/starocean/tkchoice.png)](http://cywh.com/disc.php?forum=124)

### dan · 2003-07-31 11:53 · #A1002-10514

**Tis a good idea.. :) -nt**

**Dan**
**CoreGDE (Game Development Engine):**
Release: N/A
Next Release Date: Soon.
Website: [Here](http://www.dc-3.co.uk/)
