---
kind: forum-thread
id: "toolkitzone-forums/21748"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Advanced Coding"
skin: "phpbb2"
thread_id: "21748"
title: "My in game time system. Why isn't it working?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=21748"
written: "2005-07-24T17:13:00"
last_post: "2005-08-01T05:54:00"
date_confidence: "exact"
captured: ["20051101024243", "20051212120045", "20060108025156"]
author: "ericzgao"
repliers: ["Delano"]
authors: ["ericzgao", "Delano"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_237265_amp_3Bsid_cd40f59d332d617fd710433313591a8d", captured: "20060108025156", sha256: "f024fb6261e70e78fa5a2806ae313e41639f07112c4371159cf147f3c979df6a", wayback_url: "https://web.archive.org/web/20060108025156/http://www.toolkitzone.com/forums/viewtopic.php?p=237265&amp%3Bsid=cd40f59d332d617fd710433313591a8d"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_239496_amp_3Bsid_cd40f59d332d617fd710433313591a8d", captured: "20051212120045", sha256: "43cfa300e567dcad84af4c038328abb1e5d26dd7672a50f93069ba20cd7bf9d3", wayback_url: "https://web.archive.org/web/20051212120045/http://www.toolkitzone.com/forums/viewtopic.php?p=239496&amp%3Bsid=cd40f59d332d617fd710433313591a8d"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_240429_amp_3Bsid_7cde889a94523dc3911efb6795047320", captured: "20051101024243", sha256: "60058ea9dd56bb9bebd94c07b5b9acdfbf9eb8922cc95a17102fe6766b63b171", wayback_url: "https://web.archive.org/web/20051101024243/http://www.toolkitzone.com/forums/viewtopic.php?p=240429&amp%3Bsid=7cde889a94523dc3911efb6795047320"}
links: []
---

# My in game time system. Why isn't it working?

### ericzgao · 2005-07-24 17:13 · #B237265

This is my in-game time system, with my bank interest accumulation system implemented into it. It doesn't work when I thread it in a board, but it runs without any glitchs when I just test run it from the RPGCode editor. Can anybody help?

**Code:**

```
if (time!=0)

{

hour!=7

min1!=0

min2!=0

ampm!=1

time!=1

}

:branch

//note to reader:  * and // are both comment marks

*******************************************************************************************************

*Name:  In-game time system

*Description:

*   purpose is to add to game time

*   format:  hour! : min1! min2! ampm!

*   will play as loop

*   detains 1 second before playing over loop (thus, one second real time = one minute game time)

*Status:  complete

*******************************************************************************************************

delay(1)

//checks if min1! has to go up a number

if (min2!=9)

{

   //if yes, then it will check whether hour! has to go up a number

   if (min1!=5)

   {

      //if yes, it will check whether ampm! has to change value

      if (hour!=11)

      {

         //if yes, it will check whether ampm! = 1 or 2

         if (ampm!=1)

         {

            //if ampm!=1, then ampm! will change to 2

            //hour! will equal 12, min1! will equal 0, and min2! will equal 0

            //the program will end and loop over

            ampm! = 2

            hour! = 12

            min1! = 0

            min2! = 0

            branch(:end)

         }

         if (ampm!=2)

         {

            //if ampm!=2, then ampm! will change to 1

            //hour! will equal 12, min1! will equal 0, and min2! will equal 0

            //the program will end and loop over

            ampm! = 1

            hour! = 12

            min1! = 0

            min2! = 0

            branch(:end)

         }

      }

      if (hour! < 11 OR hour! > 11)

      {

         //if no, then it will check whether the time is 12 or not

         if (hour!=12)

         {

            //if yes, then hour! will equal one, min1!=0, and min2!=0

            //the program will end and loop over

            hour! = 1

            min1! = 0

            min2! = 0

            branch(:end)

         }

         if (hour!<11)

         {

            //if no, then hour!=plus 1, min1!=0, and min2!=0

            //the program will end and loop over

            hour! = hour! + 1

            min1! = 0

            min2! = 0

            branch(:end)

         }

      }

   }

   if (min1!<5)

   {

      //if no, then min1! will go up a number, and min2! will equal 0.  the program will end, and loop over

      min1! = min1! + 1

      min2! = 0

      branch(:end)

   }

}

if (min2!<9)

{

   //if no, then min1! will go up one number

   //the program will end and loop over

   min2! = min2! + 1

   branch(:end)

}

:end

time!=1

//if ampm!=1, then it will display as AM on the clock

if (ampm!=1)

{

ampm$ = "AM"

}

//if ampm!=2, then it will display as PM on the clock

if (ampm!=2)

{

ampm$ = "PM"

}

//bank system

   bank_interest_time! = bank_interest_time! + 1

   if (bank_interest_time! = 1440)

   {

      if (account1_type$="Savings")

      {

         interest1! = account1_amount! / 100

         interest1! = interest1! * bank_interest!

         account1_amount! = account1_amount! + interest1!

      }

      if (account2_type$="Savings")

      {

         interest2! = account2_amount! / 100

         interest2! = interest2! * bank_interest!

         account2_amount! = account2_amount! + interest2!

      }

      if (account3_type$="Savings")

      {

         interest3! = account3_amount! / 100

         interest3! = interest3! * bank_interest!

         account3_amount! = account3_amount! + interest2!

      }

      if (account4_type$="Savings")

      {

         interest4! = account4_amount! / 100

         interest4! = interest4! * bank_interest!

         account4_amount! = account4_amount! + interest2!

      }

      bank_interest! = random(10)

   }

//end bank system

//I took out the actual time display system.  If anybody wants to test it, you can go ahead and add your own, like a simple MWin or something.

branch(:branch)
```

### Delano · 2005-07-29 17:16 · #B239496

Not tested it, but Delay() isn't going to work very well in threads, because it pauses the whole engine rather than the program. Use ThreadSleep(id!, seconds!) instead, where id! is obtained from either your launching call or GetThreadId().
Secondly, the branches may cause you problems (and are considered bad practice) - you could lose :end pretty easily, and try replacing :branch with a constant while loop.

### ericzgao · 2005-08-01 05:54 · #B240429

thanks, delano Very Happy so there's the solution for it being clunky. well, i'll try out the thread sleep and thread wake stuff. also, thanks for reminding me whether i'm supposed to use while loops or branches in threads. i read about it a long time ago, and since the tk2 wander.prg used branch... well, nevermind. thanks.
