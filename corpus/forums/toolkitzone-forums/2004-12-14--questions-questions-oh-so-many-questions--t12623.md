---
kind: forum-thread
id: "toolkitzone-forums/12623"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12623"
title: "Questions, questions, oh so many questions"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12623"
written: "2004-12-14T21:58:00"
last_post: "2004-12-18T01:05:00"
date_confidence: "exact"
captured: ["20041228072557"]
author: "Village Idiot"
repliers: ["Metallic Ego", "Dont_Think_So"]
authors: ["Village Idiot", "Metallic Ego", "Dont_Think_So"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139671_amp_", captured: "20041228072557", sha256: "eb9e2e713132bb3e0b122aadf9c6f757f47d36dc11253787085541660360d0d9", wayback_url: "https://web.archive.org/web/20041228072557/http://www.toolkitzone.com/forums/viewtopic.php?p=139671&amp="}
links: []
---

# Questions, questions, oh so many questions

### Village Idiot · 2004-12-14 21:58 · #B139671

This is probably going to make some of you more experienced programmers laugh until you pee yourselves, but how am i to go about creating a custom battle system? You might ask what my idea is, and if you do (probably not, but here it is anyway) i was thinking of something like the one in Super Mario RPG for SNES. It had a Timed Hit system-- you hit a button at a certain time during your attack, and you inflict more damage... by the same token, if you hit a button while you were being hit, you took less.
Obviously, i'm not sure how to do this. I'm as confused as a hungry baby in a topless bar.

### Metallic Ego · 2004-12-15 22:56 · #B140275

I'm sure this is possible with the Toolkit. Simply use the Get command. It calculates the time it takes for the player to hit a key. It is similar to the Wait command in a way, because it waits for the user to press a key. But, however, the program doesn't stop and wait for a key press. The rest of the program will still execute even before a key press.
Here's how Get would work:
ENTER$ = Get(5000)
*Waits 5 seconds for the player to press the ENTER key.
It would take a try or two, but I'm sure the battle system you described could be improvised in the Toolkit.

### Village Idiot · 2004-12-16 19:33 · #B140622

Thanks a lot, man. Now... how would you do that? Would you include the rpgcode program in the special move? I wanted it to be right as the graphics showed the strike. So it'd have to be something like
#Delay(1)
ENTER$=Get(1000)
*attack damage or status effects here
Or something like that?

### Metallic Ego · 2004-12-18 00:32 · #B141269

You have the general idea down. However, I'm not sure if #Get is capable of calculating how much time is took for the player to press a key, but give the player a certain amount of time to press a key.
You could do something like this:
ENTER$ = Get(500)
*Waits half a second for a key press
*If my memory from using the Toolkit a year ago is correct, 1 is stored in
*the variable of a key if it is pressed. This checks to see if ENTER was
*pressed
If(ENTER$ = "1")
{
Kill(ENTER$)
ENTER$ = Get(400)
If(ENTER$ = "1")
{
Kill(ENTER$)
ENTER$ = Get(300)
*This cycle is repetetive, depending on how many times you want the
*player to press a key
That code gives the user half a second to press a key. If it's pressed, the player is required to press it again, however, they have less time to press it, making the player have to rapidly press a key.
You might have to experiment with it a little, but I believe that's what you could do...

### Dont_Think_So · 2004-12-18 01:05 · #B141277

No, it's actually like this:
Something$ = Get(500)
MWin("You pressed: " + Something$)
Wait()
