---
kind: forum-thread
id: "toolkitzone-forums/9644"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "support &amp; discussion"
skin: "phpbb2"
thread_id: "9644"
title: "[rpgcode] problems"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=9644"
written: "2004-10-03T12:25:00"
last_post: "2004-10-08T14:10:00"
date_confidence: "exact"
captured: ["20050109004430"]
author: "Spyder"
repliers: ["Xavier", "Colin", "matt72186"]
authors: ["Spyder", "Xavier", "Colin", "matt72186"]
posts_present: 9
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_107049_amp_", captured: "20050109004430", sha256: "8ed177e5b631ee881aa4fb91125361139f5ea0f2b8aaaa56fde67c8f484c876d", wayback_url: "https://web.archive.org/web/20050109004430/http://www.toolkitzone.com/forums/viewtopic.php?p=107049&amp="}
links: []
---

# [rpgcode] problems

### Spyder · 2004-10-03 12:25 · #B104273

Something is wrong with the [rpgcode] command on these forums. It puts a line break after every line, which is very annoying.

### Xavier · 2004-10-03 12:33 · #B104275

Seems to be very much browser specific, Firefox I believe. Report it to Matt, since he developed it and I have not touched the actual class coded.
I also noticed it messes up with comment indenting and the use of ! and ; in if/while/for statements.
Work, Matt, work! Wink

### Spyder · 2004-10-03 13:29 · #B104278

Heh, yes. I didn't realize it was a browser specific thing though, but I did report it at MS as well. Matt's had some stuff going on the past few days, so work wasn't progressing as fast as about a week or two ago, when he stayed up for like four days straight coding all sorts of stuff, after which his step-dad took his internet away for a day or two Confused Didn't stop him from setting up a virtual PHP server on his comp though Razz

### Colin · 2004-10-03 15:12 · #B104305

**Xavier wrote:**

> Seems to be very much browser specific, Firefox I believe. Report it to Matt, since he developed it and I have not touched the actual class coded.
> I also noticed it messes up with comment indenting and the use of ! and ; in if/while/for statements.
> Work, Matt, work! Wink
>

You did the line breaking yourself, so don't deny it Wink
Considering Matt called your implementation, "butchered", I doubt he wants to help make it worse Razz
Bah.
Here's my opionion:
+ Remove double-spacing
+ Remove line numbers
..and it'll be good.

### Xavier · 2004-10-03 17:24 · #B104357

Actually, he got it wrong. He didn't know we use his second version, which puts line numbers in itself. All I did was change the style.
As for line breaking/double-spacing, again - it's all done by his script. The only other source of the problem may be because of PHPBB's own initial parsing. I'll get his latest release and see, but unless he has released an update recently...
In fact, the only thing my implementation does is replace indent (/t) with five spaces - at bbcode level, not his class. The rest is simply sent through his parser.
But I understand how you kids got confused.

### matt72186 · 2004-10-08 05:56 · #B106972

Sorry about that, I fixed the problem with line-breaks, so that should be all good. I'll add an option to disable line numbers in a sec, so if you wanna disable them you can. Double-spacing isn't part of the script, I think it's the way the forums parse the message, anyway I'll look into all of that, I also noticed it has a problem with the $ sign in variables, I got some time tonight, so I'll play with it a bit.

### matt72186 · 2004-10-08 06:18 · #B106977

Well I added more options, you can set what to use as tabs, you can enable/disable line numbers, and fixed the line-break bug. I don't know what's going on with the $ sign, I don't have anything here... maybe it's the forum parsing that's messing those up...

### Xavier · 2004-10-08 12:14 · #B107032

Thank you Matt.
And KSNiloc, I expect a full written apology in the mail tomorrow. Wink

### matt72186 · 2004-10-08 14:10 · #B107049

Hmm... other than those problems (that I just fixed) and excluding the $ sign problem, is there anything else messing up here?
Yeah the double-lines is annoying, but as Xavier said it's something to do with BBCode parsing, you can fix that by removing "white-space:pre;" from the styling, and then convert your tabs to spaces defined by & nbsp ;
I used the pre so that tabs would show up correctly, but it also parses \n as a newline, and apparently PHPBB takes \n and adds <br /> and another \n to it
