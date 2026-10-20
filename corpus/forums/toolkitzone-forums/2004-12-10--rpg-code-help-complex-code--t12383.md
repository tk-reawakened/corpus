---
kind: forum-thread
id: "toolkitzone-forums/12383"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "toolkit 2.x support"
skin: "phpbb2"
thread_id: "12383"
title: "RPG Code Help- Complex Code"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12383"
written: "2004-12-10T00:23:00"
last_post: "2004-12-11T23:09:00"
date_confidence: "exact"
captured: ["20050117155330"]
author: "bound4ct"
repliers: ["Levi", "marcos"]
authors: ["bound4ct", "Levi", "marcos"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_138187_amp_", captured: "20050117155330", sha256: "8b25151146d0b3b498da95d48be135c528e4f3bb73341cea86754c3842c09adb", wayback_url: "https://web.archive.org/web/20050117155330/http://www.toolkitzone.com:80/forums/viewtopic.php?p=138187&amp"}
links: []
---

# RPG Code Help- Complex Code

### bound4ct · 2004-12-10 00:23 · #B137172

I need help with a conversation between Inuyasha and Cloud. I am using this code to prompt the player to add Cloud to the party. If no, Cloud's next quote is different and the player is prompted again. This is my code:

**Code:**

```
#If(talkedtocloud! == 1)

{

#MWin("C'mon, Inuyasha! You can't beat the Rodent Squad")

#MWin("without me!")

#MWin("Take me with you!")

#Wait(a$)

#MWinCls()

#Prompt("Take Cloud with you?", cloud2$)

#If(cloud2$ == "yes")

{

#AddPlayer("cloud.tem")

#MWin("Cloud joined your party!")

#Wait(a$)

#DestroyItem(0)

#EraseItem(0)

#ForceRedraw()

}

#If(cloud2$ == "no")

{

#MWin("You're going to need me sooner or later...")

#Wait(a$)

}

}

#If(talkedtocloud == 0)

{

#MWin("Inuyasha, I heard that you are going to")

#MWin("take down the Rodent Squad. Do you need some help?")

#Wait(a$)

#Prompt("Allow Cloud to join your party?", cloud$)

#If(cloud$ == "yes")

{

#AddPlayer("cloud.tem")

#MWin("Cloud joined your party!")

#Wait(a$)

#DestroyItem(0)

#EraseItem(0)

#ForceRedraw()

}

#If(cloud$ == "no")

{

#MWin("Oh, poor, naive Inuyasha. You think that

#MWin("you can beat the Rodent Squad alone?")

#talkedtocloud!=1

#Wait(a$)

}
```

### Levi · 2004-12-10 01:35 · #B137237

Okay. What's the problem? Does it not work? Are there error messages? Or are you just making sure it'll work before actually trying it?
One thing I would suggest is that you prompt them for a number rather than text. There's not telling if the user will say Yes or YES or something like that. It won't catch it because its not the same as yes.
So it should be.
Mwin("1-Yes")
Mwin("2-No")
#Prompt("Allow Cloud to join your party?", cloud$)
If( cloud! == 1) {}
If( cloud! == 2) {}

### marcos · 2004-12-10 11:20 · #B137500

why the prompt? I think it would be easier with a wait(a$).

### Levi · 2004-12-10 11:35 · #B137502

Oh good point. I was just worried about player input rather than how they input.

### bound4ct · 2004-12-11 23:09 · #B138187

I can include information in the readme, but my problem is that the code isn't working when I talk to the character that the code is programmed into.
