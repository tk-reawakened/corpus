---
kind: forum-thread
id: "toolkitzone-forums/10282"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "10282"
title: "Help with a program that actually allocates exp ..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10282"
written: "2004-10-18T05:33:00"
last_post: "2004-10-21T04:19:00"
date_confidence: "exact"
captured: ["20050109004625"]
author: "RDemusX"
repliers: ["Marc", "Akura_TheDragonBlader", "Dont_Think_So", "Alex0Xander", "Colin", "matt72186"]
authors: ["RDemusX", "Marc", "Akura_TheDragonBlader", "Dont_Think_So", "Alex0Xander", "Colin", "matt72186"]
posts_present: 11
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_114232_amp_", captured: "20050109004625", sha256: "1d37739cb2c0814c367a2311a9fde611937406c35efd5c8eb5da360a752960ff", wayback_url: "https://web.archive.org/web/20050109004625/http://www.toolkitzone.com/forums/viewtopic.php?p=114232&amp="}
links: []
---

# Help with a program that actually allocates exp ...

### RDemusX · 2004-10-18 05:33 · #B112423

In MOTM the exp you gain can be alloted to certain stats to increase those stats or decrease the mp needed to use a certain ability. I have everything working perfect except ... er ... hmm ... let me just post the damn code.

**Code:**

```
*This is the code for you to move the cursor around a calculator type image and select certain numbers*

***************** *Custom For MOTM*

***************** *Number Prompt*

#method numprompt(ques1$,ques2$,ques3$,ques4$,ques5$,ques6$,code$)

{

:top

#include("actualallocate.prg")

   #bold("on")

   #color(0)

   #fontsize(18)

   #npimage$ = "numprompt.gif"

   #npcur$ = "cursor.gif"

   #npimx! = 131

   #npimy! = 126

   #npcurx[1]! = 444

   #npcurx[2]! = 499

   #npcurx[3]! = 550

   #npcury[1]! = 160

   #npcury[2]! = 202

   #npcury[3]! = 245

   #npcury[4]! = 285

   #npimw! = 490

   #npimh! = 227

   #npcurw! = 27

   #npcurh! = 27

   #r! = 0

   #g! = 0

   #b! = 0

   #add! = 40

   #txslotx! = 13.75

   #txsloty! = 17.6

   #npsel1! = 2

   #npsel2! = 4

   #max! = 0

   #setimage(npimage$,npimx!,npimy!,npimw!,npimh!)

        #text(12,10,ques1$)

        #text(12,11,ques2$)

        #text(12,12,ques3$)

        #text(12,13,ques4$)

        #text(12,14,ques5$)

        #text(12,15,ques6$)

   #savescreen()

   #while(max! < 8)

   {

        #restorescreen()

        #setimageadditive(npcur$,npcurx[npsel1!]!,npcury[npsel2!]!,npcurw!,npcurh!,add!)

      #wait(a$)

      #if(a$ = "UP")

      {

         #if(npsel2! > 1)

         {

            #npsel2! = npsel2! - 1

         }

      }

      #if(a$ = "DOWN")

      {

         #if(npsel2! < 4)

         {

            #npsel2! = npsel2! + 1

         }

      }

      #if(a$ = "LEFT")

      {

         #if(npsel1! > 1)

         {

            #npsel1! = npsel1! - 1

         }

      }

      #if(a$ = "RIGHT")

      {

         #if(npsel1! < 3)

         {

            #npsel1! = npsel1! + 1

         }

      }

      #if(a$ = "ENTER")

      {

         #if(npsel2! = 4)

         {

            #if(npsel1! = 2)

            {

                                #kill(code!)

                                #kill(number!)

                                #branch(:top)

            }

         }

         #if(npsel2! = 1)

         {

            #if(npsel1! = 1)

            {

               #restorescreen()

               #number! = 7

               #text(txslotx!,txsloty!,number!)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code! = code! + number!

            }

         }

         #if(npsel2! = 1)

         {

            #if(npsel1! = 2)

            {

               #restorescreen()

               #number! = 8

               #text(txslotx!,txsloty!,number!)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code! = code! + number!

            }

         }

         #if(npsel2! = 1)

         {

            #if(npsel1! = 3)

            {

               #restorescreen()

               #number! = 9

               #text(txslotx!,txsloty!,number!)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code! = code! + number!

            }

         }

         #if(npsel2! = 2)

         {

            #if(npsel1! = 1)

            {

               #restorescreen()

               #number! = 4

               #text(txslotx!,txsloty!,number!)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code! = code! + number!

            }

         }

         #if(npsel2! = 2)

         {

            #if(npsel1! = 2)

            {

               #restorescreen()

               #number! = 5

               #text(txslotx!,txsloty!,number!)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code! = code! + number!

            }

         }

         #if(npsel2! = 2)

         {

            #if(npsel1! = 3)

            {

               #restorescreen()

               #number! = 6

               #text(txslotx!,txsloty!,number!)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code! = code! + number!

            }

         }

         #if(npsel2! = 3)

         {

            #if(npsel1! = 1)

            {

               #restorescreen()

               #number! = 1

               #text(txslotx!,txsloty!,number!)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code! = code! + number!

            }

         }

         #if(npsel2! = 3)

         {

            #if(npsel1! = 2)

            {

               #restorescreen()

               #number! = 2

               #text(txslotx!,txsloty!,number!)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code! = code! + number!

            }

         }

         #if(npsel2! = 3)

         {

            #if(npsel1! = 3)

            {

               #restorescreen()

               #number! = 3

               #text(txslotx!,txsloty!,number!)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code! = code! + number!

            }

         }

         #if(npsel2! = 4)

         {

            #if(npsel1! = 1)

            {

               #restorescreen()

               #number! = 0

               #text(txslotx!,txsloty!,number!)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code! = code! + number!

            }

         }

         #if(npsel2! = 4)

         {

            #if(npsel1! = 3)

            {

               #restorescreen()

               #number$ = " "

               #text(txslotx!,txsloty!,number$)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code! = code! + number!

            }

         }

      }

   }

#actualallocate()

}
```

Then this is another code ... The "actualallocate()":

**Code:**

```
*I have shortened it ... it only shows one working stat.

***************** *Custom For MOTM*

***************** *Actual Allocation To Stats*

#method actualallocate()

{

#include("allocate.prg")

#if(alloselc! = 1)

{

#if(xpheld[0]! > nhpxp[0]!)

{

#hpxp[0]! = hpxp[0]! + code!

#xpheld[0]! = xpheld[0]! - code!

}

}

#if(hpxp[0]! > nhpxp[0]!)

{

#random(100,num!)

#mhp[0]! = mhp[0]! + num!

#nhpxp[0]! = nhpxp[0]! * 2

}

#kill(code!)

#kill(number!)

#allocate()

}
```

Now the problem is that when the user selects 200 for the amount to distibute to the stat's exp ... it only gives that stat 2 and takes away from the exp 2. If the user picked 975 ... it should give the stat 975 exp. Instead it gives 21 exp and takes 21 exp.
What I want to know is HOW THE HELL DO I MAKE IT GIVE WHAT THE USER SELECTED! Damn I'm glad I got that off my chest. I have been messing with this for hours. Please somone help me out here. It has been a long while since I have asked for help.
RDX

### Marc · 2004-10-18 18:59 · #B112571

I'll look into it. If no one else gets the answere before me.

### Akura_TheDragonBlader · 2004-10-18 19:25 · #B112582

I think I've done something slightly similar. Not really, but I'll take a crack at it. Since I'm not sure what variables your using to allocate to the stat, I'll make up my own:

**rpgcode:**

```
exptotal$ = castlit(num1!) + castlit(num2!) + castlit(num3!)

castint(exptotal$, exptotal!)

statexp[whateverstatthisissupposedtobe]! + = exptotal!
```

Basically, you use(or convert to) strings or literal values for the selected numbers, combine them all into one string, convert that string to an integer, and finally add it to the stat's current exp. This might be complete crap, but I got it to work once, in a program that lets a user change TK2's border color, so I know this ought to work somehow.

### Dont_Think_So · 2004-10-18 22:24 · #B112698

I see you have a random in there... try again and select the same numbers. Are you getting different results?

### RDemusX · 2004-10-20 07:02 · #B113528

Hey thanx anyways guys. I figured it out I will post the code so you guys can see what I mean.

**Code:**

```
*This is when your allocating the exp. To make the numbers go side by side and actually work correctly I had to change the variables to literal and call for them as so. Then at the bottom of the program I had to #castnum(code$,code!) and it worked perfect.

*Here is the num prompt code:

***************** *Custom For MOTM*

***************** *Number Prompt*

#method numprompt(ques1$,ques2$,ques3$,ques4$,ques5$,ques6$,code$)

{

   :top

   #include("actualallocate.prg")

   #bold("on")

   #color(0)

   #fontsize(18)

   #npimage$ = "numprompt.gif"

   #npcur$ = "cursor.gif"

   #npimx! = 131

   #npimy! = 126

   #npcurx[1]! = 444

   #npcurx[2]! = 499

   #npcurx[3]! = 550

   #npcury[1]! = 160

   #npcury[2]! = 202

   #npcury[3]! = 245

   #npcury[4]! = 285

   #npimw! = 490

   #npimh! = 227

   #npcurw! = 27

   #npcurh! = 27

   #r! = 255

   #g! = 255

   #b! = 255

   #add! = 40

   #txslotx! = 13.75

   #txsloty! = 17.6

   #npsel1! = 2

   #npsel2! = 4

   #max! = 0

   #setimagetransparent(npimage$,npimx!,npimy!,npimw!,npimh!,r!,g!,b!)

   #text(12,10,ques1$)

   #text(12,11,ques2$)

   #text(12,12,ques3$)

   #text(12,13,ques4$)

   #text(12,14,ques5$)

   #text(12,15,ques6$)

   #savescreen()

   #while(max! < 8)

   {

      #restorescreen()

      #setimageadditive(npcur$,npcurx[npsel1!]!,npcury[npsel2!]!,npcurw!,npcurh!,add!)

      #wait(a$)

      #if(a$ = "UP")

      {

         #if(npsel2! > 1)

         {

            #npsel2! = npsel2! - 1

         }

      }

      #if(a$ = "DOWN")

      {

         #if(npsel2! < 4)

         {

            #npsel2! = npsel2! + 1

         }

      }

      #if(a$ = "LEFT")

      {

         #if(npsel1! > 1)

         {

            #npsel1! = npsel1! - 1

         }

      }

      #if(a$ = "RIGHT")

      {

         #if(npsel1! < 3)

         {

            #npsel1! = npsel1! + 1

         }

      }

      #if(a$ = "ENTER")

      {

         #if(npsel2! = 4)

         {

            #if(npsel1! = 2)

            {

               #kill(code$)

               #kill(number$)

               #branch(:top)

            }

         }

         #if(npsel2! = 1)

         {

            #if(npsel1! = 1)

            {

               #restorescreen()

               #number$ = "7"

               #text(txslotx!,txsloty!,number$)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code$ = code$ + number$

            }

         }

         #if(npsel2! = 1)

         {

            #if(npsel1! = 2)

            {

               #restorescreen()

               #number$ = "8"

               #text(txslotx!,txsloty!,number$)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code$ = code$ + number$

            }

         }

         #if(npsel2! = 1)

         {

            #if(npsel1! = 3)

            {

               #restorescreen()

               #number$ = "9"

               #text(txslotx!,txsloty!,number$)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code$ = code$ + number$

            }

         }

         #if(npsel2! = 2)

         {

            #if(npsel1! = 1)

            {

               #restorescreen()

               #number$ = "4"

               #text(txslotx!,txsloty!,number$)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code$ = code$ + number$

            }

         }

         #if(npsel2! = 2)

         {

            #if(npsel1! = 2)

            {

               #restorescreen()

               #number$ = "5"

               #text(txslotx!,txsloty!,number$)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code$ = code$ + number$

            }

         }

         #if(npsel2! = 2)

         {

            #if(npsel1! = 3)

            {

               #restorescreen()

               #number$ = "6"

               #text(txslotx!,txsloty!,number$)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code$ = code$ + number$

            }

         }

         #if(npsel2! = 3)

         {

            #if(npsel1! = 1)

            {

               #restorescreen()

               #number$ = "1"

               #text(txslotx!,txsloty!,number$)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code$ = code$ + number$

            }

         }

         #if(npsel2! = 3)

         {

            #if(npsel1! = 2)

            {

               #restorescreen()

               #number$ = "2"

               #text(txslotx!,txsloty!,number$)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code$ = code$ + number$

            }

         }

         #if(npsel2! = 3)

         {

            #if(npsel1! = 3)

            {

               #restorescreen()

               #number$ = "3"

               #text(txslotx!,txsloty!,number$)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code$ = code$ + number$

            }

         }

         #if(npsel2! = 4)

         {

            #if(npsel1! = 1)

            {

               #restorescreen()

               #number$ = "0"

               #text(txslotx!,txsloty!,number$)

               #savescreen()

               #max! = max! + 1

               #txslotx! = txslotx! + .75

               #code$ = code$ + number$

            }

         }

         #if(npsel2! = 4)

         {

            #if(npsel1! = 3)

            {

               #restorescreen()

               #number$ = " "

               #text(txslotx!,txsloty!,number$)

               #savescreen()

               #max! = 8

               #txslotx! = txslotx! + .75

               #code$ = code$ + number$

            }

         }

      }

   }

   #castnum(code$,code!)

   #actualallocate()

}

*Here is where I check every stat and add to it.

***************** *Custom For MOTM*

***************** *Actual Allocation To Stats*

#method actualallocate()

{

   #include("allocate.prg")

   #if(alloselc! = 1)

   {

      #if(xpheld[0]! > nhpxp[0]!)

      {

         #hpxp[0]! = hpxp[0]! + code!

         #xpheld[0]! = xpheld[0]! - code!

         #if(hpxp[0]! > nhpxp[0]!)

         {

            #random(100,num!)

            #mhp[0]! = mhp[0]! + num!

            #nhpxp[0]! = nhpxp[0]! * 2

            #hp[0]! = mhp[0]!

         }

      }

   }

   #if(alloselc! = 2)

   {

      #if(xpheld[0]! > nattxp[0]!)

      {

         #attxp[0]! = attxp[0]! + code!

         #xpheld[0]! = xpheld[0]! - code!

         #if(attxp[0]! > nattxp[0]!)

         {

            #random(5,num!)

            #att[0]! = att[0]! + num!

            #nattxp[0]!= nattxp[0]! * 2

         }

      }

   }

   #if(alloselc! = 3)

   {

      #if(xpheld[0]! > nmattxp[0]!)

      {

         #mattxp[0]! = mattxp[0]! + code!

         #xpheld[0]! = xpheld[0]! - code!

         #if(mattxp[0]! > nmattxp[0]!)

         {

            #random(5,num!)

            #matt[0]! = matt[0]! + num!

            #nmattxp[0]!= nmattxp[0]! * 2

         }

      }

   }

   #if(alloselc! = 4)

   {

      #if(xpheld[0]! > ndefxp[0]!)

      {

         #defxp[0]! = defxp[0]! + code!

         #xpheld[0]! = xpheld[0]! - code!

         #if(defxp[0]! > ndefxp[0]!)

         {

            #random(5,num!)

            #mdef[0]! = mdef[0]! + num!

            #ndefxp[0]!= ndefxp[0]! * 2

         }

      }

   }

   #if(alloselc! = 5)

   {

      #if(xpheld[0]! > nmdefxp[0]!)

      {

         #mdefxp[0]! = mdefxp[0]! + code!

         #xpheld[0]! = xpheld[0]! - code!

         #if(mdefxp[0]! > nmdefxp[0]!)

         {

            #random(5,num!)

            #mdef[0]! = mdef[0]! + num!

            #nmdefxp[0]!= nmdefxp[0]! * 2

         }

      }

   }

   #if(alloselc! = 6)

   {

      #if(xpheld[0]! > nspeedxp[0]!)

      {

         #speedxp[0]! = speedxp[0]! + code!

         #xpheld[0]! = xpheld[0]! - code!

         #if(speedxp[0]! > nspeedxp[0]!)

         {

            #random(5,num!)

            #speed[0]! = speed[0]! + num!

            #nspeedxp[0]!= nspeedxp[0]! * 2

         }

      }

   }

   #if(alloselc! = 7)

   {

      #if(xpheld[0]! > nmovexp[0]!)

      {

         #movexp[0]! = movexp[0]! + code!

         #xpheld[0]! = xpheld[0]! - code!

         #if(movexp[0]! > nmovexp[0]!)

         {

            #random(5,num!)

            #move[0]! = move[0]! + num!

            #nmovexp[0]!= nmovexp[0]! * 2

         }

      }

   }

   #if(alloselc! = 8)

   {

      #if(xpheld[0]! > nmwhitexp[0]!)

      {

         #mwhitexp[0]! = mwhitexp[0]! + code!

         #xpheld[0]! = xpheld[0]! - code!

         #if(mwhitexp[0]! > nmwhitexp[0]!)

         {

            #random(100,num!)

            #mwhite[0]! = mwhite[0]! + num!

            #nmwhitexp[0]!= nmwhitexp[0]! * 2

            #white[0]! = mwhite[0]!

         }

      }

   }

   #if(alloselc! = 9)

   {

      #if(xpheld[0]! > nmblackxp[0]!)

      {

         #mblackxp[0]! = mblackxp[0]! + code!

         #xpheld[0]! = xpheld[0]! - code!

         #if(mblackxp[0]! > nmblackxp[0]!)

         {

            #random(100,num!)

            #mblack[0]! = mblack[0]! + num!

            #nmblackxp[0]!= nmblackxp[0]! * 2

            #black[0]! = mblack[0]!

         }

      }

   }

   #if(alloselc! = 10)

   {

      #if(xpheld[0]! > nmredxp[0]!)

      {

         #mredxp[0]! = mredxp[0]! + code!

         #xpheld[0]! = xpheld[0]! - code!

         #if(mredxp[0]! > nmredxp[0]!)

         {

            #random(100,num!)

            #mred[0]! = mred[0]! + num!

            #nmredxp[0]!= nmredxp[0]! * 2

            #red[0]! = mred[0]!

         }

      }

   }

   #if(alloselc! = 11)

   {

      #if(xpheld[0]! > nmbluexp[0]!)

      {

         #mbluexp[0]! = mbluexp[0]! + code!

         #xpheld[0]! = xpheld[0]! - code!

         #if(mbluexp[0]! > nmbluexp[0]!)

         {

            #random(100,num!)

            #mblue[0]! = mblue[0]! + num!

            #nmbluexp[0]!= nmbluexp[0]! * 2

            #blue[0]! = mblue[0]!

         }

      }

   }

   #if(alloselc! = 12)

   {

      #if(xpheld[0]! > nmgreenxp[0]!)

      {

         #mgreenxp[0]! = mgreenxp[0]! + code!

         #xpheld[0]! = xpheld[0]! - code!

         #if(mgreenxp[0]! > nmgreenxp[0]!)

         {

            #random(100,num!)

            #mgreen[0]! = mgreen[0]! + num!

            #nmgreenxp[0]!= nmgreenxp[0]! * 2

            #green[0]! = mgreen[0]!

         }

      }

   }

   #kill(code!)

   #kill(number!)

   #allocate()

}
```

Just wanted to shoe you guys I figured it out and post it in case anyone wants to use it as reference.
Thanx,
RDX

### Alex0Xander · 2004-10-20 18:57 · #B113760

Always comment your code. It may be hell if you come back to it in a say a week and dont know where you left off or dont know what the hell it was your were trying to do.

### RDemusX · 2004-10-20 20:22 · #B113805

I appreciate the info Alexander, but if I commented all my code, it would take twice the amount of time writing it. I name all my variables uniquely for this purpose. Notice everything is #npimage$ , and npcur$ = and so on. #np = number prompt, so that way I know. All the stat varaibles are self explanitory.
Heh I used to comment all the time until, when I was using TK 2, my programs were getting ridiculously long. So I stopped to make room for more lines of code.
Thanx,
RDX

### Marc · 2004-10-20 20:42 · #B113812

And I was told that in TK2 commenting drasticaly slows the program down. Why? Because:
A) it has to parse all of the space
b) because it has to ignore each and every letter or sentaince
I may not be right, but that's how it seems.

### Colin · 2004-10-20 21:29 · #B113839

In TK3 comments aren't even read from the file.
Comment your heart out in tk3, yeah!

### RDemusX · 2004-10-21 02:11 · #B114130

Hmm ... I knew there was a reason that I LOVE TK 3 so damn much. No really, If you guys in the TK Dev team can get a few of the annoying bugs fixed by the next release, you will make a shit load of people happy (.IT formated music).
Thanx,
RDX

### matt72186 · 2004-10-21 04:19 · #B114232

Yes I love TK3 too... if it were a human being I'd so date it... *licks computer screen*
