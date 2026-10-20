---
kind: forum-thread
id: "toolkitzone-forums/24083"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "24083"
title: "I added new features to the TK Board Editor"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=24083"
written: "2005-10-05T21:46:00"
last_post: "2005-10-06T10:06:00"
date_confidence: "exact"
captured: ["20060112035453"]
author: "Doc_Wellsy"
repliers: ["Chris Reeves", "Colin", "Delano"]
authors: ["Doc_Wellsy", "Chris Reeves", "Colin", "Delano"]
posts_present: 5
pages_present: [2]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 15, url: "http://toolkitzone.com/forums/viewtopic.php?t=24083", reason: "capture-failed"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_262827_amp_3Bsid_676513d1a6980aeb9bf37b2b4364333e", captured: "20060112035453", sha256: "11d01f7e9c45d432cefe29944565a195200052c97cbdc79f065ee3a225959cbb", wayback_url: "https://web.archive.org/web/20060112035453/http://www.toolkitzone.com/forums/viewtopic.php?p=262827&amp%3Bsid=676513d1a6980aeb9bf37b2b4364333e"}
links: []
---

# I added new features to the TK Board Editor

> [!missing] gap:1-15 · http://toolkitzone.com/forums/viewtopic.php?t=24083 · capture-failed
> Page 1 of 2 was not recovered.

### Doc_Wellsy · 2005-10-05 21:46 · #B262702

Nice one Chris, I think its great to see community members taking an active part in doing things for the TK. Sounds like some useful features, I'll be interested to try out your patch if you release it.

### Chris Reeves · 2005-10-05 21:56 · #B262709

Colin it's not about hiding the truth, it's just about being professional...You could have communicated what you wanted to say a lot better than you did, unless your command of the English language is weak, which I doubt. I thought you would know that considering you are the 'head of the household' here.
Instead of saying "your idea is silly", you could have said something like "the idea of using items to simulate partial transparency isn't an ideal approach to what you're trying to do. There's a better way." I know it's more typing, but I'm very sure you could pull it off. Since you're judging my feature (without even ever trying it) tell me a better way I could have gone about doing it without having to alter the engine. I didn't want to alter the engine because I KNEW that you all are changing it to C++.

### Colin · 2005-10-05 22:01 · #B262713

There probably isn't a way you could have done it better. But if your intention was for the feature to be incorporated into the official release, working for the short term is not a good idea. I had thought your idea was to do so, but if you just want to release this separately, it might be useful to some people.
I'm weary in general of forking the source and endorsing it by posting unofficial releases on this site. It creates confusion among users and makes upgrading more difficult. Perhaps in a latter version we can add some sort of a plugin system so that people can add all the features they want without modifying the core source and users can install plugins and keep their features when they upgrade the TK too.

### Chris Reeves · 2005-10-05 23:19 · #B262738

I understand what you're saying Colin, and I thought about the whole updating thing. That's why it really doesn't matter to me whether or not the features I added are incorporated in the official release. Perhaps I wasn't clear on my intent of this project. I originally did this for my own enrichment. I wanted a more user-friendly, more composer-friendly interface to work with when using the board editor until 3.07 comes out. After using the new tools for my game development I realized then that others could benefit from this as well, even if it's just for the short term. All I was intending on doing was releasing a patch for anyone who wants to update their 3.06. As soon as the update for 3.07 comes out users can always just uninstall the patch I made and then update it with the patch for 3.07.

### Delano · 2005-10-06 10:06 · #B262827

**Xavier wrote:**

>
> **William wrote:**
>
> > but I still respect him for creating the tk engine.
> >
>
> And you were around back in the day, right?
> Of course, unless you're speaking of .07 - to which Dizzy also has claim.
>

Nice to know when you're appreciated...!
Chris, submit it as an unofficial release. Yes, it might create some confusion, but 3.0.7 is a long way off and it will be useful in the short term. Maybe next time post about what you're doing before doing it - we may be able to help you out! Smile
