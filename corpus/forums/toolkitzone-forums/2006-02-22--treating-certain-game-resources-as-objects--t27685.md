---
kind: forum-thread
id: "toolkitzone-forums/27685"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "27685"
title: "Treating certain game resources as objects?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27685"
written: "2006-02-22T12:08:00"
last_post: "2006-02-22T18:07:00"
date_confidence: "exact"
captured: ["20060305160426"]
author: "Euix"
repliers: ["Sander", "TK Game Boy"]
authors: ["Euix", "Sander", "TK Game Boy"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_300710_amp_3Bsid_41a8f0424612fd95602078968b75364d", captured: "20060305160426", sha256: "30fab92af129ecf6958ff77b9d203b063d876129223c86e29fb11158c84cdf14", wayback_url: "https://web.archive.org/web/20060305160426/http://toolkitzone.com/forums/viewtopic.php?p=300710&amp%3Bsid=41a8f0424612fd95602078968b75364d"}
links: []
---

# Treating certain game resources as objects?

### Euix · 2006-02-22 12:08 · #B300633

I feel adding some sort of support like this would be great - to treat certain game resources (like tiles, animations, players) as in-game objects that can be manipulated with RPGCode.
An example:

**Code:**

```
Ghost = Game.Boards[Boards.Current].Items[0]

Ghost.Opacity = 50
```

Of course, that's treating an item on the current board as an RPGCode object which has certain/specific properties (namely opacity so we can "ghostify" the ghost. Could even use RPGCode to somewhat rapidly change the opacity to emulate "flickering").
All game resources should have at least a few common properties, so all of the objects could derive from a base class.
This would make the Toolkit much more flexible and powerful, and would provide means of doing things that would otherwise take a series of Get/Set RPGCode commands or a plugin. The object-oriented nature of the resources would allow for some neat things like object cloning and dynamic size, color, and orientation changes.
Imagine being able to shade players and tiles using an RPGCode thread. It could be possible to develop some nice effects, like dynamic lighting.
Watch this topic for updates.
Update: One idea I have is possibly the creation or development of Managed RPGCode - a sort of feature that would group commands and objects into namespaces, and allow more control and flexibility over objects. Commands now are just part of a global namespace, and could be more organized.
note: This would call for a new code structure (namespace)

**Code:**

```
// Showing an example of Managed RPGCode

Graphics.Screen.Clear()

Graphics.Color.Set(255, 0, 0)

Graphics.DrawRectangle(0, 0, 200, 200)

Graphics.Font.Name = "Verdana"

Graphcis.Font.Size = 13

Graphics.DrawText(10, 10, "Managed RPGCode")
```

I plan on writing a document giving a good framework and structure for RPGCode commands - keep watching.

### Sander · 2006-02-22 13:51 · #B300655

There's been some discussion about this stuff, and I believe the devers decided to implement this at some point. Not for 3.0.7, though.

### TK Game Boy · 2006-02-22 18:07 · #B300710

**Sander wrote:**

> There's been some discussion about this stuff, and I believe the devers decided to implement this at some point. Not for 3.0.7, though.
>

What a shame. The stuff Euix said sounds awesome.
