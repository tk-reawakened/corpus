---
kind: forum-thread
id: "acforum/996"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "996"
title: "Faster Music Playing (more)"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=996"
written: "2003-06-09T26:47:00"
last_post: "2003-06-09T27:53:00"
date_confidence: "exact"
captured: ["20030725050654", "20030725051145"]
author: "compugeek"
repliers: ["noadi"]
authors: ["compugeek", "noadi"]
posts_present: 2
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_996", captured: "20030725050654", sha256: "b79d040e48401822d8a3516e2a1ebfadb62e5ba4875c9dddc6aa4af832a1cdd7", wayback_url: "https://web.archive.org/web/20030725050654/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=996"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_998", captured: "20030725051145", sha256: "7c23f04f61a9a45b04fd4e8d391851dffa028dc419e902dcba1f5184de78f182", wayback_url: "https://web.archive.org/web/20030725051145/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=998"}
links:
  - {url: "http://diona.tk", status: "external", local: null}
  - {url: "http://flatface.net/~diona/media/link.gif", status: "external", local: null}
  - {url: "http://members.lycos.co.uk/diona/Media/npixel.gif", status: "external", local: null}
  - {url: "http://noadi-pixels.tk", status: "external", local: null}
---

# Faster Music Playing (more)

### compugeek · 2003-06-09 26:47 · #A1002-996

OK, this isn't about playing midis faster but about getting them started faster. I downloaded (yet another) program off of cNet, this one lets me decode midis into musical notation. I quickly tried it out using the preloaded midis from TK, and found that they did not start playing at the beginning of the first measure. I know that many people have criticized the large delay between the appearance of the screen and the poiint at which the music (finally) starts playing, so I found a solution that just might work. So, if anyone ever gets around to making any new music, please make sure to at least use pickup notes (for those of you who don't write music, this is basically saying to start on beat 3 instead of beat 1 so that you don't have any blank beats at the beginning of the midi). If you can't figure out how to insert them (like me), then try to find another way. Please edit the existing midis in the same way. This could speed up the start of the midi by a few seconds.
Another thought: In the final version of TK3, use the midis' titles as their file names, because they sound boring the way they are. For example, "VIP - title1.mid" should be changed to "Epoch.mid" and "VIP - Town3.mid" could be "QuietCity.mid".(I also found this out in my experiment.)
compugeek

### noadi · 2003-06-09 27:53 · #A1002-998

**That's not a TK problem (more)**

The delay is a result of the person composing the music like that, which is easily fixed with any midi editor. CBM has no control over this. And pickups create 2 beat lag time since you are starting on beat 3 not beat 1, people just need to start the song on the first measure not on the second or third.
Just rename the midis to have less boring filenames it takes seconds. I really don't know why it matters anyway what the filename is.
[![](http://members.lycos.co.uk/diona/Media/npixel.gif)](http://noadi-pixels.tk)
[![](http://flatface.net/~diona/media/link.gif)](http://diona.tk)
