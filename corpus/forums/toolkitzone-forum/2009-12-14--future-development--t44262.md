---
kind: forum-thread
id: "toolkitzone-forum/44262"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "44262"
title: "Future development"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=44262"
written: "2009-12-14T07:00:00"
last_post: "2009-12-17T08:29:00"
date_confidence: "exact"
captured: ["20100101205520", "20100101205940"]
author: "Spyder"
repliers: ["z3ro", "Occasionally_Correct", "Euix", "cuthalion"]
authors: ["Spyder", "z3ro", "Occasionally_Correct", "Euix", "cuthalion"]
posts_present: 9
pages_present: [1, 2]
pages_total: 2
posts_per_page: 10
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_44262_start_0", captured: "20100101205940", sha256: "49e053991124b1163691e57568334a1429e19f4f87d88e04105007d795f0945a", wayback_url: "https://web.archive.org/web/20100101205940/http://toolkitzone.com/forum/viewtopic.php?t=44262&start=0"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_44262_start_10", captured: "20100101205520", sha256: "69d237a2e456fca1dba20bd7eb3203d9338af8de23c96c45daa1f4648a4c9bc5", wayback_url: "https://web.archive.org/web/20100101205520/http://toolkitzone.com/forum/viewtopic.php?t=44262&start=10"}
links:
  - {url: "http://en.wikipedia.org/wiki/BSD_license#3-clause_license_.28.22New_BSD_License.22.29", status: "external", local: null}
  - {url: "http://toolkitzone.com/vault/stuff/4618_tk3-developer-userbar.png", status: "captured", local: "wayback/toolkitzone.com/vault/stuff/4618_tk3-developer-userbar.png"}
  - {url: "http://toolkitzone.com/vault/stuff/4618_tk3-spectator-userbar.png", status: "captured", local: "wayback/toolkitzone.com/vault/stuff/4618_tk3-spectator-userbar.png"}
---

# Future development

### Spyder · 2009-12-14 07:00 · #K486928

Just curious as to the future development plans of the TK. Is the current version the final version? Is it just a matter of waiting for the right person to come along and begin developing?

### Spyder · 2009-12-14 07:17 · #K486930

Mostly just bugfixes for now then. Do you know if he plans to continue development to the point of new features, revamped GUI, that kind of thing? I think it's pretty odd that the first open-source release of the TK has barely been touched in 2 years... I mean I know it's a small (and shrinking...) community... but it still surprises me. I suppose 'any' progress at this point is a giant leap ahead from where it was going.

### z3ro · 2009-12-14 07:36 · #K486931

Unfortunately, it hasn't really been touched due to the majority of our new members being teenagers (and younger) who really have no idea what they're doing. The majority of older members (like myself) either don't have enough programming experience, time, or interest in it. Or, as in Colin's case, simply leave the community with no intent of continuing development or returning.
And from what I understand, further development on it is (hopefully) planned as soon as mostly (or all Razz ) bugs are found and squashed. Of course, I cannot speak for Euix or O_C, but that seems to be the case.

### Occasionally_Correct · 2009-12-14 07:58 · #K486932

**Spyder wrote:**

> I think it's pretty odd that the first open-source release of the TK has barely been touched in 2 years...
>

The Toolkit has been open source software since 2003 or 2004, unless by "first open source release" you mean the version 3.x line and not just 3.1.0.

**z3ro wrote:**

> Of course, I cannot speak for Euix or O_C,
>

I'm not doing any TK development. I'm a spectator. Razz

### Euix · 2009-12-14 19:49 · #K486940

Personally, I plan on investing whatever time I can into engine development. I won't dodge the truth: I wouldn't mind some recognition. At the moment, I am simply merging jackyboy's bug fixes, with fixes in the source code repository, and with my own personal repairs. All of the major bugs currently plaguing the engine have been accounted for.
All that is left is to fix a few remaining bugs, do some extensive testing, and then package the engine and have Xavier approve it as an official release.
As far as future development goes, I am mostly concerned about the engine at this point. I would love to work on the editor, but I am afraid I would only be interested in a complete rewrite in an entirely different programming language. Besides this, I don't have the development tools to work on the official editor.
I am going to focus on refactoring a large portion of the engine code, improve the stability and performance of RPGCode, and completely revise the graphics engine to something more modular, and vastly more powerful. The current engine is a mixture between DirectX technology, conventional graphics-manipulation algorithms, and Windows GDI programming. The graphics engine is certainly the weakest part of the engine, and is always going to get in the way of hobbyist game development.
If I can get the engine to a good point, I would be very interested in working on a modular editor using a managed programming language, such as Java or C#. Personally, I think the .NET Framework is the way to go, but everyone has different feelings about it.

### z3ro · 2009-12-14 20:51 · #K486945

Maybe you could put this user bar in your signature:
![](http://toolkitzone.com/vault/stuff/4618_tk3-developer-userbar.png)
<http://toolkitzone.com/vault/stuff/4618_tk3-developer-userbar.png>
Just something I whipped up in a few minutes when I read your post about recognition, Euix. I even made one for O_C! Very Happy
![](http://toolkitzone.com/vault/stuff/4618_tk3-spectator-userbar.png)
<http://toolkitzone.com/vault/stuff/4618_tk3-spectator-userbar.png>
Very Happy
*Thanks Euix for all of his hard work*

### Euix · 2009-12-14 21:05 · #K486948

z3ro,
That userbar is pretty snazzy; I'll include that in my signature! Also, thanks for the support. Not only is recognition nice, but I get a feeling that the engine I am helping to build is being used by a lot of people for inspiration, and in someway to help them realize their dreams, or push them in the right direction.
Also, of course, I sincerely enjoy programming, and the RPG Toolkit is an amazing way to practice and exercise my abilities.
Anyway, expect some interesting stuff in the future; assuming I have the time I need to do the work. In the mean time, please make sure that the community knows that I am fixing bugs, and I need to know everything wrong with the current engine. If everyone is using jackyboy's bug-fix, there is no easy way for me to know what bugs are fixed and what bugs are not fixed. So please have everyone look at the official bud report post in this forum, and post their engine bug observations.
Thanks!

### Occasionally_Correct · 2009-12-14 23:24 · #K486959

**furyX639 wrote:**

> The old license was more restrictive, and I think was based on the BSD license. The difference is that the GPL would allow forks so Euix and jackyboy's side builds are legal. The old license would have required that the changes were merged into the main source.
>

Yeah, the original license was the [BSD license](http://en.wikipedia.org/wiki/BSD_license#3-clause_license_.28.22New_BSD_License.22.29) (although it was called the "AC Open License"). The only difference was that derivative works fell under the derivative license, which had some extra stipulations: All derivative works (source or binary) could not be sold for a fee, and the source code must be publicly available. Branches and forks were legal under those terms. Smile

**z3ro wrote:**

> ![](http://toolkitzone.com/vault/stuff/4618_tk3-spectator-userbar.png)
>

Haha. Thanks. Razz

### cuthalion · 2009-12-17 08:29 · #K487046

Well, given the motivational power of recognition (for people like me and possibly Euix, it might even be called a necessity)...
GO EUIX!
