---
kind: forum-thread
id: "toolkitzone-forums/6959"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions &amp; bugs"
skin: "phpbb2"
thread_id: "6959"
title: "Placing text by pixels"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=6959"
written: "2004-08-10T04:33:00"
last_post: "2004-08-10T16:34:00"
date_confidence: "exact"
captured: ["20040921165629"]
author: "seveneternal"
repliers: ["Dont_Think_So", "Nick", "Marc", "KSNiloc"]
authors: ["seveneternal", "Dont_Think_So", "Nick", "Marc", "KSNiloc"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_72704_amp_", captured: "20040921165629", sha256: "a62aa325f497cd778c95824771066a7c3bd40ff63c7e374e237d7a9c511cb884", wayback_url: "https://web.archive.org/web/20040921165629/http://www.toolkitzone.com/forums/viewtopic.php?p=72704&amp="}
links:
  - {url: "http://img76.exs.cx/img76/421/Muahahahaha.jpg", status: "external", local: null}
  - {url: "http://saoghal.cywh.com/Stadsport/banner.gif", status: "external", local: null}
---

# Placing text by pixels

### seveneternal · 2004-08-10 04:33 · #B72537

Shouldn't there be a way to set text by pixels rather then rows?
_________________
Fake smiles.

### Dont_Think_So · 2004-08-10 05:06 · #B72548

Hmm... this should work:

**Code:**

```
#autocommand

x!=100

y!=100

getfontsize(fontsize!)

x!=x!/fontsize!+1

y!=y!/fontsize!+1

#text(x!,y!,"Look at me! I'm at pixels 100,100!")
```

If not, then remove the +1.
_________________
"I have succeded in all but one thing - failure" -Dont_Think_So
"Once upon a midnight dreary, while I websurfed, weak and weary,
...Over many a strange and spurious website of 'hot chicks galore',
...While I clicked my fav'rite bookmark, suddenly there came a warning,
...And my heart was filled with mourning, mourning for my dear amour.
..."'Tis not possible," I muttered, "give me back my cheap hardcore!" -
Quoth the server, "404"."

### Nick · 2004-08-10 05:42 · #B72565

Yeah, it's something like that. You can also stick a decimal in the number to be more exact.
_________________
![](http://saoghal.cywh.com/Stadsport/banner.gif)

### Marc · 2004-08-10 15:01 · #B72671

It would make aligning text and images much easier if based on pixels.
Edit: When the new relese comes out I will look into it.
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### KSNiloc · 2004-08-10 16:34 · #B72704

I already made PixelText(). I just forgot to tell OC, lol.
_________________
Pawn.
