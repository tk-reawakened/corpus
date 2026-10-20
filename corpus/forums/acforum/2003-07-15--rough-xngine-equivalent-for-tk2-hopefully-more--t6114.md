---
kind: forum-thread
id: "acforum/6114"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "6114"
title: "Rough Xngine equivalent for TK2 (hopefully) - more"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=6114"
written: "2003-07-15T07:18:00"
last_post: "2003-07-15T13:54:00"
date_confidence: "exact"
captured: ["20030731035102", "20030731040159"]
author: "tigris-k"
repliers: ["khin"]
authors: ["tigris-k", "khin"]
posts_present: 2
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_6114", captured: "20030731035102", sha256: "95e3ddc91368e0038ddfd22606b5d41f350acd3c997f5eed2b123c6fa3037be5", wayback_url: "https://web.archive.org/web/20030731035102/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=6114"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_6120", captured: "20030731040159", sha256: "c941cd70481c9d27f301a7f15e53c2400f326fccd0bb6bb32f2d8485bc9949f2", wayback_url: "https://web.archive.org/web/20030731040159/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=6120"}
links: []
---

# Rough Xngine equivalent for TK2 (hopefully) - more

### tigris-k · 2003-07-15 07:18 · #A1001-6114

Hello,
Right now I am working through the mechanics of how I'll need to build (and build around) a quest engine similar to Daggerfall's Xngine for quest generation. What is supposed to happen is that each populated area will have a few potential quest givers, each on its own social faction (like commoner, merchant, nobility, scholar, etc) that when the player approaches to ask for work, if they are liked enough by the quest giver's social faction they will get a randomly chosen level-appropriate task or adventure to complete for reward and increase in reputation with that faction.
So here is the basic outline I've worked out so far which I'm sure is far from perfect:
On condition PLAYER APPROACHES QG(Quest Giver) FOR WORK
- QG checks if player already on quest for this faction
- - On condition YES, ON QUEST
- - - Tell Player they rock, but no new quest, END
- - On condition NO, NOT ON QUEST continue...
- QG checks player's reputation with QG's social faction
- On condition FACTION TOO LOW
- - Give player cheesy reply about how much they suck
- - Rare Chance: Offer demeaning quest to boost faction
- - END
- On condition FACTION GOOD ENOUGH
- - Pick One of subset of quests appropriate to level
- - Call Function to set up selected quest
- - Mark Player as ON QUEST
- - END
Of course, that's really rough and will hopefully get a lot more refined when I get to the actual coding. What I was wanting to ask about, is first if there are any obvious flaws in my logic or implementation that I'm not catching since I'd rather find out now than after I get a lot of work done building around it, and secondly, since the lack of sophisticated branching options will mean the quest selection process will be dependent on a separate #if statement for each quest possiblity (of course please correct me if I'm wrong), has anyone done any testing to get an idea of how many simple #if statements can be calculated per second, so as to know if there is an upper limit on how many quest options I should allow the program to choose from?
Thank you :)
Tigris-K

### khin · 2003-07-15 13:54 · #A1001-6120

**hmmm(more)**

what you're trying to do is ambitious,but don't take me wrong...i'm also implementing multiple #if selections since my rpg npcs will have emotions..move according to time,etc.
No,i haven't calculated how long it'll take for a lot if #if's to be tested,but it won't take long even if it's 20.
I need your site URLs to be included at my community links section.Please type in the complete URL of your site.
And also,choose from the following classification:
1.web-design
2.web-hosting
3.tk resource site
4.miscellaneous
if your site falls in multiple category,indicate them all.
tnx again:)

---
**Contacts**
E-mail: (redacted: email)
ICQ: 346048923
AIM aergheiz
Landline: (redacted: phone number)(I'm from the Philippines so this is a loooong distance call)
Mobile: (redacted: phone number)(txt or call me)

---
