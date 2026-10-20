---
kind: forum-thread
id: "toolkitzone-forums/12624"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12624"
title: "My attack code won't work."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12624"
written: "2004-12-14T23:26:00"
last_post: "2004-12-15T23:03:00"
date_confidence: "exact"
captured: ["20041228072353"]
author: "Megiddo"
repliers: ["Metallic Ego"]
authors: ["Megiddo", "Metallic Ego"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139711_amp_", captured: "20041228072353", sha256: "f985a993ce0241f92b22dfc26ffdef70c988dbf134c063dd2332abe261694cc1", wayback_url: "https://web.archive.org/web/20041228072353/http://www.toolkitzone.com/forums/viewtopic.php?p=139711&amp="}
links: []
---

# My attack code won't work.

### Megiddo · 2004-12-14 23:26 · #B139711

In order to have control over a special move's accuracy and damage, I wrote the following method:

**rpgcode:**

```
*Specify the power, the, accuracy, and the attack name.

Method DoAttack(power!, accuracy!, attackName$)

{

*A random number from 1 to 100 is chosen.

     ran1! = Random (100)

*Damage equals the attack power plus the source's FP minus the

*target's DP.

     damage! = -(power! + source[Fight]! - tarGet[defence]!)

     If(damage! &gt; 0)

     {

          damage! = 0

     }

     If(ran1! &gt;= 1)

     {

*Display a window confirming that the attack was perfromed.

          Delay(1)

*If the move did not miss...

          If(ran1! &lt;= accuracy!)

          {

*Give the target negative HP (that's why the value in

*the &lt;damage!&gt; variable is negative.)

               GiveHP("target", damage!)

*Display a message stating the damage done.

               MWin("Enemy takes &lt;damage!&gt; damage!")

               Delay(1)

          }

*If the attack missed...

          {

               MWin("The attack missed!")

               Delay(1)

          }

     }

*Kill the variables.

     Kill(ran1!, damage!, power!, accuracy!, attackName$)

}
```

After writing that method, I write this code into a program for my special move.

**rpgcode:**

```
Include("attackTemplate.prg") *attackTemplate is the filename that the

*above method is in.

DoAttack(25, 80, "Power Swipe")
```

Yet when I do the attack, I only see the animation. No messages. What's wrong? Please help me.

### Metallic Ego · 2004-12-15 23:03 · #B140290

Ah... Very simple!
I notice you use MWin()s in your method... Firstly, you forgot to use MWincls() to clear the message window after it is done showing. Also, I don't think one second is enough time for the player to read the message...
Instead of using MWin, you should use the Text() command. The message window is too big and blotchy too display in the middle of a battle. Just display Text somewhere at the top of the screen. That should work best.
