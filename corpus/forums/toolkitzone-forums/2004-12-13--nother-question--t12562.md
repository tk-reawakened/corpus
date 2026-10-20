---
kind: forum-thread
id: "toolkitzone-forums/12562"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12562"
title: "'nother question"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12562"
written: "2004-12-13T17:08:00"
last_post: "2004-12-16T19:41:00"
date_confidence: "exact"
captured: ["20041228072824"]
author: "Village Idiot"
repliers: ["Levi", "stanleywuu", "Occasionally_Correct", "Chamgorie Chanbear", "Dont_Think_So"]
authors: ["Village Idiot", "Levi", "stanleywuu", "Occasionally_Correct", "Chamgorie Chanbear", "Dont_Think_So"]
posts_present: 15
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139749_amp_", captured: "20041228072824", sha256: "1d9f035a170b25f91d89e7deb879a34834901ee5f5c49cbbf82a65bddb6bf30a", wayback_url: "https://web.archive.org/web/20041228072824/http://www.toolkitzone.com/forums/viewtopic.php?p=139749&amp="}
links: []
---

# 'nother question

### Village Idiot · 2004-12-13 17:08 · #B139066

I must bother you people again, for I have yet another troublesome inquiry... how do i create a message window that displays a graphic of the person talking, like Chrono Cross?

### Levi · 2004-12-13 19:14 · #B139084

The way I've always seen it dowe is use a regular MWin window and then put an image or set an image. I don't remember the code but yeah just put the image on the window then use the text command to position the text exaclty.

### Village Idiot · 2004-12-13 20:42 · #B139097

You're speaking to a beginner at rpgcode. How do you position the text? Is there an rpgcode to set a margin or something? or can you make two MWins pop up, one with a picture and the other with text and position them accordingly? I'm gonna need a bit more assistance with this.

### stanleywuu · 2004-12-13 23:07 · #B139153

setimage(xposition!,yposition!,width!,height!)

### Levi · 2004-12-13 23:37 · #B139176

In your RPGCode Reference. There is a command called Text
I don't have the specifics with me but that's how you would position the text. Fool around with it to get the hang of what you're doing.

### stanleywuu · 2004-12-13 23:39 · #B139179

But text has some problem though because text position are based on the text size while all other things are based on the pixel coordinate
So you might wanna take a look at PixelText

### Village Idiot · 2004-12-14 17:01 · #B139531

PixelText? What's that? I feel like i should know this, but what is it?

### Occasionally_Correct · 2004-12-14 21:09 · #B139608

**Code:**

```
pixelText(x!, y!, text$)
```

It's a command that shows text on the screen at the specified x,y coordinates (the x and y coordinates are in pixels (hence, 'pixelText')).

### Levi · 2004-12-14 21:14 · #B139615

If you're using TK3 that is. I don't belive it exists for TK2.

### Village Idiot · 2004-12-14 21:52 · #B139663

That's a'ight. i have tk3.
Thanks for the code, people.
A little bit of background: I'm working on a game called "A Gamer's Dream." It starts out with two guys, Vince and Eric, playing video games together, and all of the sudden, there's a power surge and they get sucked in. So now they're in the game world without really knowing it. I haven't really developed the Ultimate Problem, as there is in every RPG, but I plan on using characters such as Bomberman, Link, Mario, and some from various Final Fantasies (credit given where due, of course). Tell me what you think.

### Chamgorie Chanbear · 2004-12-15 00:47 · #B139749

It's cheap. Yet at the same time, it seems kinda cool. It sounds like a well-used cliché. I'd play it. But try not to rely too much on the cameos. I'd say use your own originals as the main characters, and have the rest be NPCs, possibly even enemies. If you want, have the cameos be part-time allies normally, and put in a secret way to access some of them as team members like a cheat code. Or maybe an invisible door or having to reply to certain questions a certain way.
Example:
BOWFLEX5 - Play as Link.
FAIRYBOY - Play as Young Link
CHOCOHEAD - Play as Cloud
KOMBUCHA3 - Play as Mario
Example:
To access Link as a playable character, you must answer Kaepora's questions in a certain way. The questions and answers are as follows.
Q: Hello, young travellers. What do you seek?
A: A powerful ally.
Q: An ally of what sort?
A: An experienced warrior. A legendary hero.
Q: For what purpose is a new ally required?
A: [Enter villain's name here] must be stopped. But I fear we may not be powerful enough to do it alone.
Q: What would you say if I told you that I knew of such a man?
A: Please, guide me to him.
[Kaepora calls out to Link, who then walks onto the screen. A short conversation ensues in which Link agrees to join your team]
Just a few suggestions.

### Village Idiot · 2004-12-15 22:02 · #B140236

Thanks for the review. I was planning on making the cameos only part-time allies... i guess i forgot to mention that. I'm doing this game to get more coding experience so i can do a game or a series of games based on a couple books i've written.
I have another question: I plan on having Vince and Eric separated during the ordeal, and meet up later in the game. I want to go back and forth between the two adventures until they meet up and fight each other (which side the player controls will be based on a "Who's your favorite character" inquiry). From there, they'll join when attacked by a bigger, badder foe (then I'll call the playerswap window so the player can pick the team) and so on and so forth. My question is this: how do i switch back and forth between the two adventures? Would i have to use variables to call the character back and remove the other?

### Dont_Think_So · 2004-12-15 22:26 · #B140248

RemovePlayer()
and
RestorePlayer()

### Chamgorie Chanbear · 2004-12-16 02:07 · #B140402

Do you mean to have the play play both adventures? Like once you get to a certain part of Eric's quest you then switch to playing Vince's quest, which takes place at a different location?

### Village Idiot · 2004-12-16 19:41 · #B140626

Exactly, Chamgorie. I plan on starting with Vince. After a turning point in Vince's story, I'll put an Mwin that says "I wonder where Eric is..."
From there, it will be Eric's story. You'll get up to about the same amount of gameplay, then either they'll meet up and fight or i'll have it switch a couple more times and then fight. There will be a "Who's your favorite character" type inquiry. That determines which side you'll control, whether it be Vince's party, or Eric's. After this battle, they'll join as they get attacked by a huge monster (or a really bad ass little dude) with the losing party's members at half-health. I'll call the player swap screen so they can pick members from both parties to fight this big boss. From there, things will get much harder.
What do you think?
