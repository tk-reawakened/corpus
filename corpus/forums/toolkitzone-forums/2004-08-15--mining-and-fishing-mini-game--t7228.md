---
kind: forum-thread
id: "toolkitzone-forums/7228"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "7228"
title: "Mining and fishing mini game."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7228"
written: "2004-08-15T21:58:00"
last_post: "2004-08-18T04:05:00"
date_confidence: "exact"
captured: ["20040928044542"]
author: "bradseguin"
repliers: ["The_Anonym0us", "rdemusx", "Danny 666"]
authors: ["bradseguin", "The_Anonym0us", "rdemusx", "Danny 666"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_77483_amp_", captured: "20040928044542", sha256: "a6f5394ae53b89549f13227ca7c56a19f39bb25812c3905e2100ddfa9bf54e09", wayback_url: "https://web.archive.org/web/20040928044542/http://www.toolkitzone.com/forums/viewtopic.php?p=77483&amp="}
links:
  - {url: "http://dontemailmeanycrap.com/avatar.gif", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v293/rdemusx/MOTM/newadbar.gif", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v293/rdemusx/newvid.gif", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v325/brent329/sw018.gif", status: "external", local: null}
  - {url: "http://mansionsofthemoon.myfreebb.com/index.php", status: "external", local: null}
  - {url: "http://mansionsofthemoon.tripod.com", status: "external", local: null}
  - {url: "http://overkill2013.geahost.com/Anti-Everything.png", status: "external", local: null}
  - {url: "http://thanian-nation.com/oy/asimir.jpg", status: "external", local: null}
  - {url: "http://vidoentertainment.com", status: "external", local: null}
---

# Mining and fishing mini game.

### bradseguin · 2004-08-15 21:58 · #B76138

Can somebody give me a fully coded version of this??
FISHING:
Check if user has item: "rod"
If he does not: You need a rod to fish.
If he does:
You use your rod and attempt to fish...
25% chance of:
recieved fish!- program ends, get item: fish
70% chance of:
you fail to catch anything- program ends.
5% chance of:
A fish pulls your rod into the water. lost item: rod.
- program ends.
and,
MINING:
Check if user has item: pickaxe
if he does not: You need a pickaxe to mine coal.
if he does:
You attempt to mine coal....
25% chance of:
You succesfully mine 1 coal ore.
program ends.
70% chance of:
You fail to retreave any coal. -program ends
5% chance of:
your pickaxe cracks, and is completly usless.- lost item, pickaxe.
-porgram ends.
And these will be two different programs.
Can somebody please please change all this into RPG code for me?
_________________
![](http://overkill2013.geahost.com/Anti-Everything.png)![](http://dontemailmeanycrap.com/avatar.gif)
![](http://img.photobucket.com/albums/v325/brent329/sw018.gif)
Wherever you see the evil monkey on the stairs pointing at you, you know I was there.

### The_Anonym0us · 2004-08-15 22:25 · #B76156

I'm writing it right now.

### bradseguin · 2004-08-15 22:27 · #B76158

thanks
_________________
![](http://overkill2013.geahost.com/Anti-Everything.png)![](http://dontemailmeanycrap.com/avatar.gif)
![](http://img.photobucket.com/albums/v325/brent329/sw018.gif)
Wherever you see the evil monkey on the stairs pointing at you, you know I was there.

### rdemusx · 2004-08-15 22:40 · #B76164

Fishing method

**Code:**

```
*use #fish() to call the command*

*make sure you #include("fish.prg") where you need the method to run*

#method fish()

{

#done! = 1

#while(done! = 1)

         {

         #itemcount("Rod",rod!)

         #if(rod! <= 0)

            {

            #mwin("You need a Fishing Rod to Fish here!")

            #wait(a$)

            #mwincls()

            #done! = 2

            }

        #if(rod! >= 1)

            {

            #mwin("You use the rod and begin to fish!)

            #wait(a$)

            #mwincls()

            #random(100,chance!)

            #if(chance! <= 5)

                {

                #mwin("The fish pulled the rod from your hands!")

                #mwin("Lost Fishing Rod!")

                #wait(a$)

                #mwincls()

                #takeitem("rod.itm")

                #done! = 2

                }

            #if(chance! <= 30)

                {

                #mwin("You caught a Fish!")

                #wait(a$)

                #mwincls()

                #giveitem("fish.itm")

                #done! = 2

                }

            #if(chance! <= 100)

                {

                #mwin("Not even A nibble!")

                #wait(a$)

                #mwincls()

                #done! = 2

                }

}

}

}
```

Mining Method

**Code:**

```
*use #mine() to call the command*

*make sure you #include("mine.prg") where you need the method to run*

#method mine()

{

#done! = 1

#while(done! = 1)

         {

         #itemcount("Pick Axe",pick!)

         #if(pick! <= 0)

            {

            #mwin("You need a Pick Axe to Mine here!")

            #wait(a$)

            #mwincls()

            #done! = 2

            }

        #if(pick! >= 1)

            {

            #mwin("You thrust the pick into the Earth!)

            #wait(a$)

            #mwincls()

            #random(100,chance!)

            #if(chance! <= 5)

                {

                #mwin("The pick cracks and becomes un-useable!")

                #mwin("Lost Pick Axe!")

                #wait(a$)

                #mwincls()

                #takeitem("pick.itm")

                #done! = 2

                }

            #if(chance! <= 30)

                {

                #mwin("You found a piece of coal!")

                #wait(a$)

                #mwincls()

                #giveitem("coal.itm")

                #done! = 2

                }

            #if(chance! <= 100)

                {

                #mwin("You find nothing in your search!")

                #wait(a$)

                #mwincls()

                #done! = 2

                }

}

}

}
```

That should work! Hope it helps!
RDX
_________________
![](http://img.photobucket.com/albums/v293/rdemusx/MOTM/newadbar.gif)
![](http://img.photobucket.com/albums/v293/rdemusx/newvid.gif)
VISIT WEBSITE: <http://mansionsofthemoon.tripod.com>
VISIT FORUMS: <http://mansionsofthemoon.myfreebb.com/index.php>
VISIT Vi D.O. ENT: <http://vidoentertainment.com>

### The_Anonym0us · 2004-08-15 22:48 · #B76168

**Code:**

```
******Fishing Program******

#ItemCount("fishing rod.itm", has_rod!)

#If(has_rod! = 0)

{

   #MWin("You need a fishing rod to fish.")

   #Wait()

   #Done

   }

#If(has_rod! > 0)

{

#Random(20, chance!)

#If(chance! = 1)

{

   #MWin("A fish pulls your rod into the water.")

   #Wait()

   #MWin("Lost item: Fishing Rod.")

   #Wait()

   #TakeItem("fishing rod.itm")

   #Done

   }

#If(chance! > 13)

{

   #Mwin("You fail to catch anything.")

   #Wait()

   #Done

   }

#MWin("Received fish.")

#Wait()

#GiveItem("fish.itm")
```

**Code:**

```
******Mining Program******

#ItemCount("pickaxe.itm", has_pick!)

#If(has_pick! = 0)

{

   #MWin("You need a pickaxe to mine coal.")

   #Wait()

   #Done

   }

#If(has_pick! > 0)

{

#Random(20, chance!)

#If(chance! = 1)

{

   #MWin("Your pickaxe cracks, and is completly usless.")

   #Wait()

   #MWin("Lost item: Pickaxe.")

   #Wait()

   #TakeItem("pickaxe.itm")

   #Done

   }

#If(chance! > 13)

{

   #Mwin("You fail to mine any coal.")

   #Wait()

   #Done

   }

#MWin("You succesfully mine 1 coal ore.")

#Wait()

#MWin("Received item: Coal Ore.")

#Wait()

#GiveItem("coal.itm")
```

### Danny 666 · 2004-08-18 04:05 · #B77483

can do i put fishing in my game?
_________________
![](http://thanian-nation.com/oy/asimir.jpg)
