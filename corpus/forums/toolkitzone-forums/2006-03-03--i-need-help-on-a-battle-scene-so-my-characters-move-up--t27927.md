---
kind: forum-thread
id: "toolkitzone-forums/27927"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "27927"
title: "I need help on a battle scene so my characters move up...."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27927"
written: "2006-03-03T08:06:00"
last_post: "2006-03-08T13:13:00"
date_confidence: "exact"
captured: ["20060322170825"]
author: "femi"
repliers: ["Demon Lord Tyrus", "drcrazy4", "legomaster88", "DrakeLord"]
authors: ["femi", "Demon Lord Tyrus", "drcrazy4", "legomaster88", "DrakeLord"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_303038_amp_3Bsid_0b9ff2a54ae64666702328762c23c168", captured: "20060322170825", sha256: "1fe567d0dfbdd3c008de6a30fb093e6998a67f4395aea1b91c09956ddb9cb29d", wayback_url: "https://web.archive.org/web/20060322170825/http://toolkitzone.com/forums/viewtopic.php?p=303038&amp%3Bsid=0b9ff2a54ae64666702328762c23c168"}
links: []
---

# I need help on a battle scene so my characters move up....

### femi · 2006-03-03 08:06 · #B303035

help me with this code so tthis scene is fixed
mwin("Ken: Kai!")
wait()
mwin("Kai: Ken come on we don't have much time.
push("Kai","Ken", N, N,N,N )
scene ends???? Very Happy
any help on this one lads?

### Demon Lord Tyrus · 2006-03-03 08:25 · #B303038

What is the actual problem?
Also, you cant put two characters in one push command I dont think
IE
Push("Ken", N,N,N,N)
Push("Kai", N,N,N,N)
Instead of
push("Kai","Ken", N, N,N,N )

### drcrazy4 · 2006-03-03 12:44 · #B303070

look up multirun in the help guide.

### legomaster88 · 2006-03-03 14:17 · #B303082

your mwin needs an ending quoteation mark and closing parentheses, for 1. As previously mentioned, I'd like to assure that two players [bold]cannot[/bold] be in one push() command.

### femi · 2006-03-04 07:12 · #B303335

my codes screwed...

### DrakeLord · 2006-03-04 13:38 · #B303370

No it isn't. Here. I fixed it up:

**Code:**

```
mwin("Ken: Kai!")

wait()

mwin("Kai: Ken come on we don't have much time.")

wait() //You might want this

mwincls() //and this.  Not sure though.

mulitrun() //To have both Kai and Ken run at the same time

{

   push("N,N,N,N","Kai") //You need to have the direcetions,

   push("N,N,N,N","Ken") //then the character

}
```

Tada!

### femi · 2006-03-06 15:27 · #B303845

Cheers darlord i'll test the code now Very Happy

### DrakeLord · 2006-03-08 13:13 · #B304337

Oops I spelled it wrong.
Change mulitrun() to multirun()
Embarassed
