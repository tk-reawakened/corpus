---
kind: forum-thread
id: "toolkitzone-forums/12116"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "12116"
title: "Include Command Not Working"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12116"
written: "2004-12-04T14:12:00"
last_post: "2004-12-05T18:47:00"
date_confidence: "exact"
captured: ["20050115140606"]
author: "Mystinar"
repliers: ["Colin", "Dont_Think_So", "oblivious_casualty", "Serge"]
authors: ["Mystinar", "Colin", "Dont_Think_So", "oblivious_casualty", "Serge"]
posts_present: 12
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135121_amp_", captured: "20050115140606", sha256: "6ac1c9d95aeb6d5b65b2cd327e9842023b43c7710ab6c8df2d05f9fd17177181", wayback_url: "https://web.archive.org/web/20050115140606/http://www.toolkitzone.com/forums/viewtopic.php?p=135121&amp="}
links: []
---

# Include Command Not Working

### Mystinar · 2004-12-04 14:12 · #B134522

I have been trying to develope a battle system, and the include command will not work. I set it up so that it includes a program that sets up the enemy's attributes, and then when it returns to the battle system program, all the variables for the enemy attributes are empty! I've never encountered a problem like this. Anyone else encountering such a problem?
EDIT: Just for the record, I am running the RPGtoolkit on a 500mhz Gateway with Windows XP.

### Colin · 2004-12-04 17:55 · #B134576

Including a program just gives you access to its methods. And in 3.05, globals and classes.

### Dont_Think_So · 2004-12-04 21:03 · #B134668

Exactly as Colin said. You need to put all of the stats into a method, then include the program and call the method whenever you need it.

### Mystinar · 2004-12-05 13:49 · #B135046

Been there, done that. Still doesn't work.

### Colin · 2004-12-05 16:40 · #B135080

I don't know how else to say this - loose code from the program will not run; this seems to be a common, but difficult to explain, misconception.

### oblivious_casualty · 2004-12-05 16:45 · #B135082

did you try implicit include?

### Colin · 2004-12-05 16:46 · #B135084

Using the '.' just calls the include command, for the record.

### Mystinar · 2004-12-05 17:40 · #B135090

I've tried just about everything. Here is a mockup of the programs.
***Enemy Setup Program
*Set Enemy Name
*Set Enemy HP
*Set Enemy MP
*Set Enemy Attributes
*Set Enemy Elemental resistance modifiers
*Set Enemy Status Immunities
*Set Enemy Status Auto-Effects
**Basically, the program does nothing but setup variables
***Enemy Setup Test Program
*Include Enemy Setup Program
*Run Enemy Setup Command
*Calculate Enemy Exp value
**Exp is calculated by the program, since enemies will have variable
**statistics, allowing for natural differences between members of the
**species. Specific enemies will not have random statistics.
*Display Enemy Name
*Display Enemy HP
*Display Enemy MP
*Display Enemy Exp value
Essentially, it seems like all variables set in a method are local to it only, unless they are specifically called out in the method's variable brackets. This problem is quite serious. I will try once more to get it to work. If it doesn't, then I'll know something is wrong with the toolkit and not my programming.

### Colin · 2004-12-05 17:43 · #B135091

You can use global() to force globals, but I doubt that's your problem. Try posting your code.

### Mystinar · 2004-12-05 18:03 · #B135094

I actually tried global. Doesn't work at all. I even tried this:
Method SetupEnemyVitals (EnemyHP!, EnemyMP!, Enemy_mHP!, Enemy_mMP!)
{
a! = Random(100)
EnemyHP! = 100 + a!
a! = Random(10)
EnemyMP! = 15 + a!
Kill(a!)
Enemy_mHP! = EnemyMP!
}
And then I do this in the main program.
Include("Enemy.prg")
SetupEnemyVitals (EnemyHP!, EnemyMP!, Enemy_mHP!, Enemy_mMP!)
ExpCalc(EnemyExp!) *Custom Method that calculates EXP based on enemy statistics
Text(1,1,Enemy_mHP!)
Text(1,2,Enemy_mMP!)
Text(1,3,EnemyExp!)
I'm doing nothing wrong. Is it compatibity issues with Windows XP?

### Serge · 2004-12-05 18:16 · #B135102

Well I think I know what your problem is...
You're using the input parameters wrong. You only need those if you have a value previous to the function that you want to modify or change or use in an equation, and from the looks of it this is the method that is supposed to set those values in the first place.
Try this:

**Code:**

```
Enemy.prg:

Method SetupEnemyVitals ()

{

EnemyHP! = 100 + Random(100)

EnemyMP! = 15 + Random(10)

Enemy_mHP! = EnemyMP!

}

Main:

Include("Enemy.prg")

SetupEnemyVitals()

debugger(castLit(enemyHP!))

debugger(castLit(enemyMP!))

debugger(castLit(enemy_mHP!))

wait()
```

By the way, you won't have compatibility issues with XP. The toolkit works best on XP.

### Mystinar · 2004-12-05 18:47 · #B135121

I think I may have tried that already, but I'll see about it.
Edit: Okay, it still will not work. By the way, check this out. Something I did.

**rpgcode:**

```
Method eSetup()

{

     EnemyHP! = 100 + Random(100)

     mHP! = EnemyHP!

     Text(1, 1, "Health: &lt;Enemy_mHP!&gt; / &lt;EnemyHP!&gt;")

     Clear()

}

Text(1, 1, "Health: &lt;Enemy_mHP!&gt; / &lt;EnemyHP!&gt;")
```

Funny thing. It displays the the variables within the method brackets, but outside, they just display this "Health: / ".
Even using the global command doesn't work. Any variable created inside the method brackets remains valueless outside of them.
I think there really may be a bug in the Toolkit.
EDIT 2: Okay, I got the methods working. ReturnMethod command Razz
