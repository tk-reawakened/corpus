---
kind: forum-thread
id: "toolkitzone-forums/23064"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Advanced Coding"
skin: "phpbb2"
thread_id: "23064"
title: "Threading problem (Thread not starting)"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23064"
written: "2005-08-31T12:08:00"
last_post: "2005-09-01T17:19:00"
date_confidence: "exact"
captured: ["20051107040008"]
author: "blanel"
repliers: ["p90m16mp5a4"]
authors: ["blanel", "p90m16mp5a4"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_252854_amp_3Bsid_7cde889a94523dc3911efb6795047320", captured: "20051107040008", sha256: "6dc6f546bae7448c334b7fe8d8706f61c43000a8850997d3e324baf5e3fe2541", wayback_url: "https://web.archive.org/web/20051107040008/http://www.toolkitzone.com/forums/viewtopic.php?p=252854&amp%3Bsid=7cde889a94523dc3911efb6795047320"}
links: []
---

# Threading problem (Thread not starting)

### blanel · 2005-08-31 12:08 · #B252533

I posted this before but never got a good answer... Here I go again...
Ah well... Here goes... Be prepared for alot of code.

**Code:**

```
timeThread! = thread("c#_datetime.prg", true)
```

The above starts the time program that looks something like this:

**Code:**

```
method datetime(time$,date$)

done! = 0

while(done! == 0)

{

ytime!=gametime!+add_time!

CastInt(ytime!,sec!)

min!=sec!/60

CastInt(min!,min!)

secmin!=60*min!

sec!=sec!-secmin!

hour!=min!/60

CastInt(hour!,hour!)

minhour!=60*hour!

min!=min!-minhour!

day!=hour!/24

CastInt(day!,day!)

hourday!=24*day!

hour!=hour!-hourday!

week!=day!/7

castint(week!,week!)

dayweek!=week!*7

dayw!=day!-dayweek!

if(dayw!==0)

{

litday$=Sunday

}

if(dayw!==1)

{

litday$=Monday

}

if(dayw!==2)

{

litday$=Tuesday

}

if(dayw!==3)

{

litday$=Wednesday

}

if(dayw!==4)

{

litday$=Thursday

}

if(dayw!==5)

{

litday$=Friday

}

if(dayw!==6)

{

litday$=Saturday

}

day!=day!+1

year!=1

:TOP

if(day!>365)

{

day!=day!-365

year!=year!+1

leapyear!=0

}

if(day!>365)

{

day!=day!-365

year!=year!+1

leapyear!=0

}

if(day!>365)

{

day!=day!-365

year!=year!+1

leapyear!=0

}

if(day!>366)

{

day!=day!-366

year!=year!+1

leapyear!=1

branch(:TOP)

}

if(day!<=31)

{

daymod!=0

month!=01

litmonth$=January

abbmonth$=Jan

}

if(day!>31)

{

daymod!=31

month!=02

litmonth$=February

abbmonth$=Feb

}

if(leapyear!==1)

{

DIF!=60

}

if(leapyear!==0)

{

DIF!=59

}

if(day!>DIF!)

{

daymod!=DIF!

month!=03

litmonth$=March

abbmonth$=Mar

}

Apdif!=DIF!+31

if(day!>Apdif!)

{

daymod!=Apdif!

month!=04

litmonth$=April

abbmonth$=Apr

}

Madif!=Apdif!+30

if(day!>Madif!)

{

daymod!=Madif!

month!=05

litmonth$=May

abbmonth$=May

}

Judif!=Madif!+31

if(day!>Judif!)

{

daymod!=Judif!

month!=06

litmonth$=June

abbmonth$=Jun

}

Jldif!=Judif!+30

if(day!>Jldif!)

{

daymod!=Jldif!

month!=07

litmonth$=July

abbmonth$=Jul

}

Audif!=Jldif!+31

if(day!>Audif!)

{

daymod!=Audif!

month!=08

litmonth$=August

abbmonth$=Aug

}

Sedif!=Audif!+31

if(day!>Sedif!)

{

daymod!=Sedif!

month!=09

litmonth$=September

abbmonth$=Sep

}

Ocdif!=Sedif!+30

if(day!>Ocdif!)

{

daymod!=Ocdif!

month!=10

litmonth$=October

abbmonth$=Oct

}

Nodif!=Ocdif!+31

if(day!>Nodif!)

{

daymod!=Nodif!

month!=11

litmonth$=November

abbmonth$=Nov

}

Dedif!=Nodif!+31

if(day!>Dedif!)

{

daymod!=Dedif!

month!=12

litmonth$=December

abbmonth$=Dec

}

day!=day!-daymod!

castlit(month!,month$)

if(month!<10){#month$="0"+month$}

castlit(day!,day$)

if(day!<10){#day$="0"+day$}

castlit(year!,year$)

if(year!<10){#year$="000"+year$

branch(:doneyear)}

if(year!<100){#year$="00"+year$

branch(:doneyear)}

if(year!<1000){#year$="0"+year$}

:doneyear

date$=litday$+", "+day$+"/"+month$+"/"+year$

if(hour!>=12)

{

ampm$="pm"

}

if(hour!<=11)

{

ampm$="am"

}

if(hour!>=13)

{

hour!=hour!-12

}

if(hour!==0)

{

hour!=12

}

castlit(hour!,hour$)

castlit(min!,min$)

castlit(sec!,sec$)

if(hour!<10){#hour$="0"+hour$}

if(min!<10){#min$="0"+min$}

if(sec!<10){#sec$="0"+sec$}

time$=hour$+:+min$+:+sec$+" "+ampm$

ReturnMethod(date$)

ReturnMethod(time$)

}

}
```

This program works to be threaded. It does exactly what I want it to do which is just keep track of time so one can check the time on a clock somewhere in the game. The clock looks something like this and works fine:

**Code:**

```
mwin("The time is: <time$>")

mwin("The date is: <date$>")

wait()
```

Next comes the funny part... The part that stopped working when the Time Thread was implemented into the game. The guard:

**Code:**

```
id! = GetThreadID()

prg1! = 1

prg2! = 2

prg3! = 3

prg4! = 4

prg5! = 5

prg6! = 6

prg7! = 7

prg8! = 8

prg9! = 9

prg10! = 10

prg11! = 11

prg12! = 12

prg13! = 13

prg14! = 14

prg15! = 15

prg16! = 16

prg17! = 17

prg18! = 18

prg19! = 19

rcardpos! = 20

pos! = 0

done! = 0

Until(done!)

{

   PushItem(pos!, "w")

   putItem(prg2!, 12, 9, 1)

   putItem(prg4!, 11, 9, 1)

   putItem(prg5!, 11, 10, 1)

   putItem(prg6!, 10, 8, 1)

   putItem(prg7!, 9, 8, 1)

   putItem(prg8!, 8, 8, 1)

   PushItem(pos!, "w")

   putItem(prg2!, 1, 1, 1)

   putItem(prg6!, 1, 1, 1)

   PushItem(pos!, "w")

   putItem(prg4!, 1, 1, 1)

   putItem(prg5!, 1, 1, 1)

   putItem(prg6!, 1, 1, 1)

   putItem(prg7!, 1, 1, 1)

   putItem(prg9!, 8, 7, 1)

   putItem(prg10!, 7, 6, 1)

   PushItem(pos!, "w")

   putItem(prg8!, 1, 1, 1)

   putItem(prg11!, 7, 7, 1)

   putItem(prg12!, 7, 9, 1)

   putItem(prg13!, 6, 10, 1)

   PushItem(pos!, "w")

   putItem(prg9!, 1, 1, 1)

   putItem(prg10!, 1, 1, 1)

   putItem(prg11!, 1, 1, 1)

   putItem(prg12!, 1, 1, 1)

   putItem(prg13!, 1, 1, 1)

   PushItem(pos!, "s")

   putItem(prg14!, 7, 10, 1)

   putItem(prg15!, 8, 10, 1)

   ThreadSleep(id!, 3)

   putItem(prg16!, 6, 9, 1)

   putItem(prg17!, 6, 10, 1)

   putItem(prg18!, 5, 10, 1)

   PushItem(pos!, "w")

   putItem(prg14!, 1, 1, 1)

   putItem(prg15!, 1, 1, 1)

   ThreadSleep(id!, 3)

   putItem(prg16!, 1, 1, 1)

   putItem(prg17!, 1, 1, 1)

   putItem(prg18!, 1, 1, 1)

   PushItem(pos!, "e")

   putItem(prg19!, 8, 7, 1)

   putItem(prg1!, 8, 6, 1)

   putItem(prg2!, 9, 7, 1)

   putItem(prg3!, 9, 6, 1)

   PushItem(pos!, "n")

   putItem(prg2!, 1, 1, 1)

   putItem(prg19!, 1, 1, 1)

   PushItem(pos!, "n")

   putItem(prg4!, 7, 6, 1)

   ThreadSleep(id!, 3)

   putItem(prg1!, 1, 1, 1)

   putItem(prg3!, 1, 1, 1)

   putItem(prg4!, 1, 1, 1)

   PushItem(pos!, "w")

   putItem(prg5!, 5, 6, 1)

   putItem(prg6!, 6, 6, 1)

   putItem(prg7!, 6, 7, 1)

   ThreadSleep(id!, 3)

   putItem(prg5!, 1, 1, 1)

   putItem(prg6!, 1, 1, 1)

   putItem(prg7!, 1, 1, 1)

   PushItem(pos!, "w")

   putItem(prg9!, 6, 9, 1)

   putItem(prg10!, 6, 10, 1)

   PushItem(pos!, "s")

   putItem(prg9!, 1, 1, 1)

   PushItem(pos!, "s")

   PushItem(pos!, "e")

   putItem(prg10!, 1, 1, 1)

   putItem(prg11!, 8, 10, 1)

   putItem(prg12!, 9, 10, 1)

   PushItem(pos!, "e")

   putItem(prg11!, 1, 1, 1)

   putItem(prg12!, 1, 1, 1)

   PushItem(pos!, "n")

   putItem(prg13!, 8, 7, 1)

   putItem(prg14!, 8, 6, 1)

   putItem(prg15!, 9, 7, 1)

   putItem(prg16!, 9, 6, 1)

   putItem(prg17!, 11, 8, 1)

   PushItem(pos!, "e")

   putItem(prg13!, 1, 1, 1)

   putItem(prg14!, 1, 1, 1)

   putItem(prg15!, 1, 1, 1)

   putItem(prg16!, 1, 1, 1)

   putItem(prg17!, 1, 1, 1)

   putItem(prg18!, 12, 8, 1)

   putItem(prg19!, 13, 8, 1)

   PushItem(pos!, "e")

   putItem(prg1!, 12, 9, 1)

   PushItem(pos!, "e")

   putItem(prg18!, 1, 1, 1)

   PushItem(pos!, "e")

   putItem(prg1!, 1, 1, 1)

   putItem(prg19!, 1, 1, 1)

   PushItem(pos!, "e")

   PushItem(pos!, "n")

   PushItem(pos!, "e")

   putItem(prg2!, 15, 7, 1)

   putItem(prg3!, 16, 6, 1)

   putItem(prg4!, 16, 8, 1)

   ThreadSleep(id!, 3)

   PushItem(pos!, "w")

   PushItem(pos!, "s")

   putItem(prg3!, 1, 1, 1)

}
```

This worked great untill the time code was implemented. Pos! represents the actuall guard. All the different prgx! are discovery items... If you cross these items the guard see's you and the game is over. These programs move as the guard roams the board. All these Items are already placed on the board from before. They are already on the board. The "discovery items" and the guard all have this program attachted to them

**Code:**

```
#include("c#_pause.prg")

mwin("HALT! WHAT ARE YOU DOING HERE?")

pause()

mwincls()

mediastop()

bitmap("gameover.jpg")

mediaPlay("Gameover.mid")

delay(3)

mediastop()

until (done!)

{

   text(9, 15, "Load Game")

   text(27.4, 15, "Quit")

   cMap! = createCursorMap()

   cursorMapAdd(150, 260, cMap!)

   cursorMapAdd(480, 260, cMap!)

   res! = cursorMapRun(cMap!)

   killCursorMap(cMap!)

   switch (res!)

   {

      case (0)

      {

         file$ = dirSav()

         if (file$ ~= "CANCEL")

         {

            load(file$)

         }

         done! = true

      }

      case (1)

      {

         windows()

      }

   }

}
```

All worked great untill the time program came... I'm thinking of removing it so everything works again but if you nice people here on TKForums could find whats wrong I would be forever thankful. Embarassed
Sorry for all the code but I reconed it might be good to post everything relevant... Rolling Eyes
As i said before... Sorry for all the code...

### p90m16mp5a4 · 2005-09-01 17:19 · #B252854

My post is below, however I am posting my fixes up first:
The time program doesn't actually have a method, you forgot the { brace.
Your datetime method doesn't work, I removed the #method and just made it a thread. The time does not update. You need to comment your code.
That actually isn't alot of code, it is spaced out sort of well. I have read it all, and would only ask for some comments. My question, where are all these placed, and wich ones are threaded, if they are threaded, tell me how. I would reccomend erasing *all* other programs on the boards except the ones you are having problems with, until this is resolved. Honestly, do that. All items, threads, and programs should be removed from your workspace. Only keep the ones you are trying to fix.
