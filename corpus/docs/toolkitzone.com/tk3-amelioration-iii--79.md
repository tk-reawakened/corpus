---
kind: doc
id: "toolkitzone.com/79"
site: "toolkitzone.com"
title: "TK3 Amelioration III"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=79"
written: "2004-12-05T19:00:00"
date_confidence: "exact"
updated: null
captured: ["20060612033000", "20070309035934"]
author: "Colin"
repliers: []
authors: ["Colin"]
comments_present: 0
f_author: "Colin"
f_date: "December 5, 2004, 7:00 pm"
f_description: "As well as outlining and providing an example of the completely overhauled movement system coming in the next release, Colin also answers a few would-be frequently asked questions."
f_title: "Miscellanea"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_79", captured: "20060612033000", sha256: "eb1873328c0d6bc4aab007215680d485afadcd1c39f7b5a46417441b0331fb54", wayback_url: "https://web.archive.org/web/20060612033000/http://www.toolkitzone.com/library.php?mode=read&doc=79"}
  - {path: "wayback/toolkitzone.com/library.php__doc_79_highlight_", captured: "20070309035934", sha256: "63cced0e1cff8cc1d95cb07915be5dab8919d00fc5ad6009522259dcbf4ef526", wayback_url: "https://web.archive.org/web/20070309035934/http://www.toolkitzone.com:80/library.php?doc=79&highlight"}
---

# TK3 Amelioration III

**Miscellanea**
Being as it has been open the better part of this week, many of you have probably visited the . A number of the games available for download at this event were built with version three of the RPGToolkit; in itself, this represents incredible progression for the system  a year ago, youd be laughed at for attempting such a feat; a year ago, even the included demo didnt run. *Winter TK Expo*
I can remember downloading what was hyped to be an improvement over the previous version  only to find stability, features, friendliness all having lowered in quality. By now, however, TK3 has not only regained its stability, but also become, among other things, blessed with features, a competent multiple document editor, and obtained an object oriented internal scripting language. Just this one event is proof that TK3 is steadily improving and becoming more appealing to the user base  you.
After months of inactivity, release 3.02while it may not have accomplished muchbrought TK3 back to the playing field. Version 3.03 further stabilized the engine and editor, providing a notable board editor toolbar. All this was nothing compared to what was perhaps the most anxiously anticipated released of the TK  version 3.04; leaked betas, release delays and jaw-dropping features all added to the mystique of this release. As this developed, my main fear was, how can we possibly top this? Again, months later, I think weve managed to.
One of 3.05s exciting new features is a completely overhauled movement system. The smooth new system enables you set animations for an immobile sprite and to specify how long the sprite must not move to be regarded as idle. The much requested feature of setting a separate speed for each character has also been implemented. Even means for you to move multiple sprites simultaneously are available. This new system makes movement almost unquestionably better than that of its predecessor.
Using the multiRun construct, you can queue up movements for as many sprites as you wish  all to be run when the block finishes. A perfect example from the TKL demo:
multiRun
push("SSSSSSEE", " ") MrG
push("ENNNWWWWWWWNN", "Spyder")
Rather than taking turns, this enables and to truly move at once. In a thread, MrG Spyder push() executes a similar queuing effect, not stopping the program to push everything in the parameter brackets. This will be integral to making our battle system feel real-time. Well hear move about this when we assemble our battle system next time.
**Frequently Asked Questions**
The main body of the article was shorter than usual today because I wanted to answer some of the questions Ive received in detail. Hopefully this section will prevent frequently asked questions from becoming frequently answered. If you have questions you would like answered, join the masses and post a comment.
**Q** : I don't quite understand the relationship between a class and a derived class in RPG Code.
**A** : One way to think of inheritance is that the derived class a base class. If you are doing a lot of graphics programming, you might create a *is a kind of* CCanvas class. If you have specific of canvases, like cursors, then they could derive from our base canvas. You gain several advantages from this. For one, the base class default (without parameters) constructor and deconstructor are called before and after the derived class, respectfully. This means you can rely on *types* CCanvas to create and kill the canvas without worrying about having inaccessible canvases floating around. Another advantage is code reusability. The code functions like draw() execute should not be dependent on the type of canvas so the base class draw() function can be called and will execute correctly, preventing the recoding of this function. When you get used to object oriented programming, noticing situations where inheritance would serve a practical purpose becomes increasingly simpler.
**Q** : Im a little confused about abstraction.
**A** : Not so much a question as it is a statement, but, nonetheless, it warrants an answer. Simply, abstraction is the process that enables us to ignore details and focus on what is essential. In the answer above, by deriving our cursor canvas from CCanvas , we no longer need to worry about how the canvas is managed or even know generic taskslike drawing itare handled; what matters is our cursor is a canvas. Object oriented programming is great for creating highly abstracted entities via encapsulation  using functions to protect data. I find that whether or not you know what abstraction is, youre likely using it in some way; reevaluating what youve already coded will enable you to realize this.
**Q** : You lost me.
**A** : The more you do somethingbe it programming, or even playing an RPGthe better you become at it. If you dont understand something, try rereading the area that makes no sense, and dont ever hesitate to post a question  yours could be in this section next!
**Closing**
In the previous weeks, weve looked at structured and modern object oriented programming techniques. This week, we briefly overviewed the movement system. With any luck, itll all come together next week when we code our real-time battle system!
Montai
December 5, 2004, 7:10 pm
You guys are truly GODS! :p
Occasionally_Correct
December 5, 2004, 7:25 pm
Really good article, Colin. :)
OBCT
December 5, 2004, 7:30 pm
i think those last two questions were from me. i said those things to Colin a few days ago =P although i got a less friendly resposne...
John@aljo
December 6, 2004, 9:35 am
Indeed the new object oriented programming sounds much like a good thing comming along. Now if only the RPGCode part of tk 3.0.5 has stayed fast. I do expect a little slow down of course, but as everyone knows I use RPGCode exstensivly when creating my game and I stress the importance of it alot in this community. Oblivious_Casualty, Colin is indeed "less friendly" than we would hope but, never the less, his help on the TK is invaluable. With these articles coming out now I think he is actually for once showing the community that he cares about the community and not just about getting credit for doing a major part of the TK recode. One last note. I can finally feel that TK 3 will now feel like a totally differnt version from TK 2. With all the new additions, some changing so fast I can't seem to keep up with, It all feels like a new and exciting program to probe and discover.
Xavier
December 7, 2004, 6:02 pm
I think Johnno holds the record for the longest comments without line breaks in blogs, resources and library now :P
**Column**
Toolkit 3.x > TK3 Amelioration
As well as outlining and providing an example of the completely overhauled movement system coming in the next release, Colin also answers a few would-be frequently asked questions.
**Past Columns**
Feb 28, '05
Feb 13, '05
Feb 7, '05
Jan 30, '05
Jan 16, '05
Feb 28, '05
Feb 13, '05
Feb 7, '05
Jan 30, '05
Jan 16, '05
