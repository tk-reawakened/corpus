---
kind: forum-thread
id: "toolkitzone-forum/38416"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "38416"
title: "Your Input: Editor Improvements"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=38416"
written: "2007-11-15T23:34:00"
last_post: "2007-11-16T22:51:00"
date_confidence: "exact"
captured: ["20071117092924"]
author: "SuperIsoRPG"
repliers: ["Auron", "k-hos", "Asimir", "Sharmandra"]
authors: ["SuperIsoRPG", "Auron", "k-hos", "Asimir", "Sharmandra"]
posts_present: 7
pages_present: [2]
pages_total: 2
posts_per_page: 10
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 10, url: "http://toolkitzone.com/forum/viewtopic.php?t=38416", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_421248", captured: "20071117092924", sha256: "e4c0e0e7304d2200326a9dd68abf3bc560f173877c6bc62da83a63bd2866995f", wayback_url: "https://web.archive.org/web/20071117092924/http://www.toolkitzone.com/forum/viewtopic.php?p=421248"}
links: []
---

# Your Input: Editor Improvements

> [!missing] gap:1-10 · http://toolkitzone.com/forum/viewtopic.php?t=38416 · never-captured
> Page 1 of 2 was not recovered.

### SuperIsoRPG · 2007-11-15 23:34 · #K421187

Basically, a while back, Shao made an animation batch program. The way it worked was that you loaded a template animation, and it made copies it modified for all directions and for a list of characters. I wrote a version of it in RPG Code recently as Shao's program didn't take into account frame delay. Basically, it would be nice to see an integrated batch animator, as putting in animations frame by frame is somewhat a bore.
The process would consist of a template frame, then selecting which parts of the file name were to be changed in the batch process (i.e, if the west view of a character was "c_w.bmp", it would replace the "w" with the other 8 different directions in different files, however, the other part "C" could also be replaced by different names of files or whatever.

### Auron · 2007-11-16 00:44 · #K421193

Part of Editor: Background
I was thinking that it would be nice if the background editor allowed you to make the background in the background editor, like how it was in TK2. Although still keeping the advances that TK3 has brought to it.
Adding an airbrush tool to the tile editor would be nice for those who use the whole toolkit for their game.
The default character and enemy editors could use some work as well. But I don't know what kinda of stuff I'd want there, so that will have to wait.
About the syntax highligting thing, what I meant was something like this.
variables you declare should be a certain color (i.e. pink, like it was in 3.0.6)
quotes should be green or something
If, while and for blocks can be the general color(i.e. blue)
Acutally since comments are green, then make the quotes red or whatever.
They don't have to be those colors, I'm just trying to give some examples. Also, trying to clear up what I meant by better syntax coloring.

### k-hos · 2007-11-16 03:24 · #K421247

Part of Editor: Help files
-More detail on how functions are to be used.
-Sort them as to what they do

### Asimir · 2007-11-16 03:30 · #K421248

**G_Dragon wrote:**

> Ctrl+ Scrolling the scroll wheel- Zoom
>

That's a great idea. I'll implement it right now.
...
There, it's done, and I automatically updated the TK on your computer to have it. Give it a try Smile

**k-hos wrote:**

> Part of Editor: Help files
> -More detail on how functions are to be used.
> -Sort them as to what they do
>

Colin removed the usefulness from the function reference in the name of progress.

### Auron · 2007-11-16 22:08 · #K421351

Acutally the RPGCode help files could use more descriptions and examples of the keywords for RPGCode.

### Sharmandra · 2007-11-16 22:16 · #K421352

**k-hos wrote:**

> Part of Editor: Help files
> -More detail on how functions are to be used.
> -Sort them as to what they do
>

Didn't they actually used to be that way?

### k-hos · 2007-11-16 22:51 · #K421359

**Sharmandra wrote:**

>
> **k-hos wrote:**
>
> > Part of Editor: Help files
> > -More detail on how functions are to be used.
> > -Sort them as to what they do
> >
>
> Didn't they actually used to be that way?
>

Yep, 3.06s help was vary explanatory about what said function did.
And every function was groped as to what they did, which was quite nice if you knew what you wanted to do but not what to use.
the help was helpful Razz
