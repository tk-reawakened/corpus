---
kind: forum-thread
id: "toolkitzone-forums/12451"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "12451"
title: "anyone need help?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12451"
written: "2004-12-11T14:03:00"
last_post: "2005-01-04T05:41:00"
date_confidence: "exact"
captured: ["20050117155253"]
author: "word32"
repliers: ["jackdam", "Darkhope", "Disrupter", "Bad Kids", "Zio", "matt72186", "Nanukimo", "darkdragonkillr", "garnetrising"]
authors: ["word32", "jackdam", "Darkhope", "Disrupter", "Bad Kids", "Zio", "matt72186", "Nanukimo", "darkdragonkillr", "garnetrising"]
posts_present: 15
pages_present: [1]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 2, start: 16, end: 30, url: "http://toolkitzone.com/forums/viewtopic.php?t=12451&start=15", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_137989_amp_", captured: "20050117155253", sha256: "6031fdfb6fd47aa96dd83fee5e5ec2ae9289ddfcaa481ea6c6edd3bd3f2e33cd", wayback_url: "https://web.archive.org/web/20050117155253/http://www.toolkitzone.com/forums/viewtopic.php?p=137989&amp="}
links: []
---

# anyone need help?

### word32 · 2004-12-11 14:03 · #B137989

cause i'll help with anything.

### jackdam · 2004-12-28 23:08 · #B147326

Wow some ofering help:S
I need help
i have created an enemy on toolkit 3.5 and i want to put him on my board so wen a character is walkin around, at a random time he it comes up with the battle screen. Is there any code that does this?
jack

### Darkhope · 2004-12-29 13:20 · #B147566

Ummmm I know this may be alot but have you seen a Tactics battle system tutorial anywhere? Razz

### Disrupter · 2004-12-29 21:42 · #B147796

**Quote:**

> I need help
> i have created an enemy on toolkit 3.5 and i want to put him on my board so wen a character is walkin around, at a random time he it comes up with the battle screen. Is there any code that does this?
>

Well you could have a thread running (a thread is a program that runs simutainiously with either other programs or the main engine) that checks a random number and if that number is correct the player fights the enemy.
use the commands random() and fightnenemy.
As for exactly using the thread. Well that depends, you could have it simply check once when the player enters the board, or you could have it on a timer and chick every few minutes the player is on the board.
I havent looked at TK3s editors much (outside of rpgcode) so im not sure if the board editor still takes items with multitasking programs. If thats the case, you would just use that as your thread. What I mean is, create an item with a multitasking program that calls the program which randomly determines if you fight the enemy...
If ya have any questions ask.

**Quote:**

> Ummmm I know this may be alot but have you seen a Tactics battle system tutorial anywhere?
>

No, unfortuantely i dont believe so. The thing about battle systems is once you can program one, you can probably program any. Knowing how to code a FF style turn based system and a Tactics style turn based system isnt all that different. Its really just a matter of changing a few methods around in the player and enemy classes. Just change how you draw the screen, when you draw the screen, when the player and enemy go, and exactly what they do when they go. I know it SOUNDS like your changing everything. But with classes, youd really be using the same basic foundation for your code and just changing maybe 10-20 percent of it.
Perhaps when im finished with my BS ill throw together a quick tatics one. Really, the hard part is all managing your data. If your using other variables then the ones the TK internal system provides, youll need to make files outside the TK and read them in.
Just knowing how to make a BS is the tricky part, making different kinds isnt that hard. Though turnbased is a lot easier then realtime obviously.

### Bad Kids · 2004-12-29 22:29 · #B147829

ask william about tatical bs's he is making one for his game.

### Darkhope · 2004-12-29 23:53 · #B147886

Who is William?? How do you make it so the charecter has a selected range like in the Tactics battle system?

### word32 · 2004-12-30 23:04 · #B148463

ok, i don't know what the hell a tactics battle system is, but if you can tell me what it is i'll help

### Zio · 2004-12-31 10:41 · #B148775

Final Fantasy Tactics Battle System....Iso battlesystem.....Move ment bassed on terrain....very good game...too tired to fill in blanks.....hope that helped a little.

### Darkhope · 2004-12-31 12:58 · #B148800

Final fantaasy doesnt have the ONLY tactics system. Anyway a Tactics sytem is a sytem that has turn based and realtime combined. I tihnk it actually pretty cool myself. You have the option to move around in a selected range of tiles or you can choose to attack with a selcted range of tiles or you can use magic/ special ability defend skip turn ect. If you ever played final fantasy tactics you will know what I am saying....Also you must have a good AI code for the monsters so they can choose wich is best.... Surprised

### word32 · 2005-01-01 02:47 · #B149069

i see.......
well i hope this helps:
We'll use
A few methods
lots of #If's
#Createitem
#PutItem
#Moveitem
--------------------------
Step 1::Board Setup
Create your board that you will be fighting on.
(i called it battle board)
#Send ("BattleBoard.brd",10,10,0)
Create your enemy as an item
#Createitem ("EnemyBitch.itm",poser!)
#Putitem ("Poser!",10,11)
--------------------------
sorry i have to go, it'll take me a few days to make the rest
--------------------------
Word32

### matt72186 · 2005-01-01 02:49 · #B149071

Here, can you help me... I can't get these programs to work, see if you can fix them...

**start.prg wrote:**

>
> **Code:**
>
> ```
> #Include "timedate.prg"
>
>
>
>
>
> timeTracker = DayNight()
>
>
> timeTracker->setTimeDuration(5, 60)
>
>
> startTime()
> ```
>

**timedate.prg wrote:**

>
> **Code:**
>
> ```
> method startTime()
>
>
> {
>
>
>    timeTracker->refStart() = 1
>
>
>    timeTracker->refTimer() = Thread("timeThread.prg", 1)
>
>
> }
>
>
>
>
>
> method stopTime()
>
>
> {
>
>
>    timeTracker->refStart() = 0
>
>
>    KillThread(timeTracker->refTimer())
>
>
> }
>
>
>
>
>
> class Time
>
>
> {
>
>
>    public:
>
>
>       ////////////////////////////////////
>
>
>       // Initialize the Properties
>
>
>       ////////////////////////////////////
>
>
>       method Time()
>
>
>       {
>
>
>          setTime(0, 0, 0)
>
>
>          setTimeDuration(60, 60)
>
>
>
>
>
>          myStart! = 0
>
>
>       }
>
>
>
>
>
>       method Time(tHour!, tMinute!, tSecond!)
>
>
>       {
>
>
>          setTime(tHour!, tMinute!, tSecond!)
>
>
>          setTimeDuration(60, 60)
>
>
>
>
>
>          myStart! = 0
>
>
>       }
>
>
>
>
>
>       method Time(tHour!, tMinute!, tSecond!, lHour!, lMinute!)
>
>
>       {
>
>
>          setTime(tHour!, tMinute!, tSecond!)
>
>
>          setTimeDuration(lHour!, lMinute!)
>
>
>
>
>
>          myStart! = 0
>
>
>       }
>
>
>
>
>
>       ////////////////////////////////////
>
>
>       // Display Time as a String
>
>
>       ////////////////////////////////////
>
>
>
>
>
>       method operator$()
>
>
>       {
>
>
>          theHour$ = CastLit(theHour! = refHour())
>
>
>          theMinute$ = CastLit(theMinute! = refMinute())
>
>
>          theSecond$ = CastLit(theSecond! = refSecond())
>
>
>
>
>
>          For(digit! = 10; digit! < refLengthHour(); digit!*=10)
>
>
>          {
>
>
>             If(theMinute! < digit!)
>
>
>             {
>
>
>                theMinute$ = "0" + theMinute$
>
>
>             }
>
>
>          }
>
>
>
>
>
>          For(digit! = 10; digit! < refLengthMinute(); digit!*=10)
>
>
>          {
>
>
>             If(theSecond! < digit!)
>
>
>             {
>
>
>                theSecond$ = "0" + theSecond$
>
>
>             }
>
>
>          }
>
>
>
>
>
>          theTime$ = theHour$ + ":" + theMinute$ + " " + theSecond$
>
>
>          ReturnMethod(theTime$)
>
>
>       }
>
>
>
>
>
>       ////////////////////////////////////
>
>
>       // Modify the Values of Properties
>
>
>       ////////////////////////////////////
>
>
>
>
>
>       method setTime(tHour!, tMinute!, tSecond!)
>
>
>       {
>
>
>          refHour() = tHour!
>
>
>          refMinute() = tMinute!
>
>
>          refSecond() = tSecond!
>
>
>       }
>
>
>
>
>
>       method setTimeDuration(lHour!, lMinute!)
>
>
>       {
>
>
>          refLengthHour() = lHour!
>
>
>          refLengthMinute() = lMinute!
>
>
>       }
>
>
>
>
>
>       method passSecond()
>
>
>       {
>
>
>          refSecond()++
>
>
>
>
>
>          If(refSecond() >= refLengthMinute())
>
>
>          {
>
>
>             refSecond() = 0
>
>
>             refMinute()++
>
>
>          }
>
>
>
>
>
>          If(refMinute() >= refLengthHour())
>
>
>          {
>
>
>             refMinute() = 0
>
>
>             refHour()++
>
>
>          }
>
>
>       }
>
>
>
>
>
>       ////////////////////////////////////
>
>
>       // Access the Properties
>
>
>       ////////////////////////////////////
>
>
>
>
>
>       method refHour()
>
>
>       {
>
>
>          ReturnMethod(&timeHour!)
>
>
>       }
>
>
>
>
>
>       method refMinute()
>
>
>       {
>
>
>          ReturnMethod(&timeMinute!)
>
>
>       }
>
>
>
>
>
>       method refSecond()
>
>
>       {
>
>
>          ReturnMethod(&timeSecond!)
>
>
>       }
>
>
>
>
>
>       method refLengthHour()
>
>
>       {
>
>
>          ReturnMethod(&lengthHour!)
>
>
>       }
>
>
>
>
>
>       method refLengthMinute()
>
>
>       {
>
>
>          ReturnMethod(&lengthMinute!)
>
>
>       }
>
>
>
>
>
>       method refStart()
>
>
>       {
>
>
>          ReturnMethod(&myStart!)
>
>
>       }
>
>
>
>
>
>       method refTimer()
>
>
>       {
>
>
>          ReturnMethod(&myTimer!)
>
>
>       }
>
>
>
>
>
>    private:
>
>
>       timeHour!
>
>
>       timeMinute!
>
>
>       timeSecond!
>
>
>
>
>
>       lengthHour!
>
>
>       lengthMinute!
>
>
>
>
>
>       myStart!
>
>
>       myTimer!
>
>
> }
>
>
>
>
>
> class Date: Time
>
>
> {
>
>
>    public:
>
>
>       ////////////////////////////////////
>
>
>       // Initialize the Properties
>
>
>       ////////////////////////////////////
>
>
>       method Date()
>
>
>       {
>
>
>          setDate(0, 0, 0)
>
>
>          setDateDuration(12, 30, 24)
>
>
>       }
>
>
>
>
>
>       method Date(dYear!, dMonth!, dDay!)
>
>
>       {
>
>
>          setDate(dYear!, dMonth!, dDay!)
>
>
>          setDateDuration(12, 30, 24)
>
>
>       }
>
>
>
>
>
>       method Date(dYear!, dMonth!, dDay!, lYear!, lMonth!, lDay!)
>
>
>       {
>
>
>          setDate(dYear!, dMonth!, dDay!)
>
>
>          setDateDuration(lYear!, lMonth!, lDay!)
>
>
>       }
>
>
>
>
>
>       ////////////////////////////////////
>
>
>       // Display Date as a String
>
>
>       ////////////////////////////////////
>
>
>
>
>
>       method operator$()
>
>
>       {
>
>
>          theYear! = refYear! + 1
>
>
>          theMonth! = refMonth() + 1
>
>
>          theDay! = refDay() + 1
>
>
>
>
>
>          theDate$ = CastLit(theMonth!) + "/" + CastLit(theDay!) + "/" + CastLit(theYear!)
>
>
>          ReturnMethod(theDate$)
>
>
>       }
>
>
>
>
>
>       ////////////////////////////////////
>
>
>       // Modify the Values of Properties
>
>
>       ////////////////////////////////////
>
>
>
>
>
>       method setDate(dYear!, dMonth!, dDay!)
>
>
>       {
>
>
>          refYear() = dYear!
>
>
>          refMonth() = dMonth!
>
>
>          refDay() = dDay!
>
>
>       }
>
>
>
>
>
>       method setDateDuration(lYear!, lMonth!, lDay!)
>
>
>       {
>
>
>          refLengthYear() = lYear!
>
>
>          refLengthMonth() = lMonth!
>
>
>          refLengthDay() = lDay!
>
>
>       }
>
>
>
>
>
>       method passDay()
>
>
>       {
>
>
>          If(refHour() >= refLengthDay())
>
>
>          {
>
>
>             refHour() = 0
>
>
>             refDay()++
>
>
>          }
>
>
>
>
>
>          If(refDay() >= refLengthMonth())
>
>
>          {
>
>
>             refDay() = 0
>
>
>             refMonth()++
>
>
>          }
>
>
>
>
>
>          If(refMonth() >= refLengthYear())
>
>
>          {
>
>
>             refMonth() = 0
>
>
>             refYear()++
>
>
>          }
>
>
>       }
>
>
>
>
>
>       ////////////////////////////////////
>
>
>       // Access the Properties
>
>
>       ////////////////////////////////////
>
>
>
>
>
>       method refYear()
>
>
>       {
>
>
>          ReturnMethod(&dateYear!)
>
>
>       }
>
>
>
>
>
>       method refMonth()
>
>
>       {
>
>
>          ReturnMethod(&dateMonth!)
>
>
>       }
>
>
>
>
>
>       method refDay()
>
>
>       {
>
>
>          ReturnMethod(&dateDay!)
>
>
>       }
>
>
>
>
>
>       method refLengthYear()
>
>
>       {
>
>
>          ReturnMethod(&lengthYear!)
>
>
>       }
>
>
>
>
>
>       method refLengthMonth()
>
>
>       {
>
>
>          ReturnMethod(&lengthMonth!)
>
>
>       }
>
>
>
>
>
>       method refLengthDay()
>
>
>       {
>
>
>          ReturnMethod(&lengthDay!)
>
>
>       }
>
>
>
>
>
>    private:
>
>
>       dateYear!
>
>
>       dateMonth!
>
>
>       dateDay!
>
>
>
>
>
>       lengthYear!
>
>
>       lengthMonth!
>
>
>       lengthDay!
>
>
> }
>
>
>
>
>
> class DayNight: Date
>
>
> {
>
>
>    public:
>
>
>       ////////////////////////////////////
>
>
>       // Initialize the Properties
>
>
>       ////////////////////////////////////
>
>
>       method DayNight()
>
>
>       {
>
>
>          setDayNight(6, 18)
>
>
>          setLight(-50, 50)
>
>
>       }
>
>
>
>
>
>       method DayNight(hDay!, hNight!)
>
>
>       {
>
>
>          setDayNight(hDay!, hNight!)
>
>
>          setLight(-50, 50)
>
>
>       }
>
>
>
>
>
>       method DayNight(hDay!, hNight!, lDay!, lNight!)
>
>
>       {
>
>
>          setDayNight(hDay!, hNight!)
>
>
>          setLight(lDay!, lNight!)
>
>
>       }
>
>
>
>
>
>       ////////////////////////////////////
>
>
>       // Modify the Values of Properties
>
>
>       ////////////////////////////////////
>
>
>       method setDayNight(hDay!, hNight!)
>
>
>       {
>
>
>          refHourDay() = hDay!
>
>
>          refHourNight() = hNight!
>
>
>          If(refHourDay() < refHourNight())
>
>
>          {
>
>
>             refHourRange1() = refLengthDay() - refHourNight() + refHourDay()
>
>
>             refHourRange2() = refHourNight() - refHourDay()
>
>
>          }
>
>
>          If(refHourDay() > refHourNight())
>
>
>          {
>
>
>             refHourRange1() = refLengthDay() - refHourDay() + refHourNight()
>
>
>             refHourRange2() = refHourDay() - refHourNight()
>
>
>          }
>
>
>       }
>
>
>
>
>
>       method setLight(lDay!, lNight!)
>
>
>       {
>
>
>          refLightDay() = lDay!
>
>
>          refLightNight() = lNight!
>
>
>          If(lNight! > lDay!)
>
>
>          {
>
>
>             refLightDay() = lNight!
>
>
>             refLightNight() = lDay!
>
>
>          }
>
>
>          refLightRange() = lDay! - lNight!
>
>
>       }
>
>
>
>
>
>       ////////////////////////////////////
>
>
>       // Access the Properties
>
>
>       ////////////////////////////////////
>
>
>       method refHourDay()
>
>
>       {
>
>
>          ReturnMethod(&hourDay!)
>
>
>       }
>
>
>
>
>
>       method refHourNight()
>
>
>       {
>
>
>          ReturnMethod(&hourNight!)
>
>
>       }
>
>
>
>
>
>       method refLightDay()
>
>
>       {
>
>
>          ReturnMethod(&lightDay!)
>
>
>       }
>
>
>
>
>
>       method refLightNight()
>
>
>       {
>
>
>          ReturnMethod(&lightNight!)
>
>
>       }
>
>
>       method refHourRange1()
>
>
>       {
>
>
>          ReturnMethod(&hourRange1!)
>
>
>       }
>
>
>
>
>
>       method refHourRange2()
>
>
>       {
>
>
>          ReturnMethod(&hourRange2!)
>
>
>       }
>
>
>
>
>
>       method refLightRange()
>
>
>       {
>
>
>          ReturnMethod(&lightRange!)
>
>
>       }
>
>
>
>
>
>       method refLightInc1()
>
>
>       {
>
>
>          ReturnMethod(&lightInc1!)
>
>
>       }
>
>
>
>
>
>       method refLightInc2()
>
>
>       {
>
>
>          ReturnMethod(&lightInc2!)
>
>
>       }
>
>
>
>
>
>    private:
>
>
>       hourDay!
>
>
>       hourNight!
>
>
>       hourRange1!
>
>
>       hourRange2!
>
>
>
>
>
>       lightDay!
>
>
>       lightNight!
>
>
>       lightRange!
>
>
>       lightInc1!
>
>
>       lightInc2!
>
>
> }
> ```
>

**timeThread.prg wrote:**

>
> **Code:**
>
> ```
> #Include("timedate.prg")
>
>
>
>
>
> while(1)
>
>
> {
>
>
>    timeTracker->passSecond()
>
>
>    timeTracker->passDay()
>
>
>
>
>
>    timeTracker->refLightInc1() = timeTracker->refHourRange1() / timeTracker->refLightRange()
>
>
>    timeTracker->refLightInc2() = timeTracker->refHourRange2() / timeTracker->refLightRange()
>
>
>
>
>
>    If(timeTracker->refHourDay() < timeTracker->refHourNight())
>
>
>    {
>
>
>       // Is it daytime
>
>
>       If(timeTracker->refHour() >= timeTracker->refHourDay() && timeTracker->refHour() < timeTracker->refHourNight())
>
>
>       {
>
>
>          ambientred! = ambientgreen! = ambientblue! = timeTracker->refLightDay() - timeTracker->refLightInc1() * (timeTracker->refHour() - timeTracker->refHourDay())
>
>
>       }
>
>
>
>
>
>       // Is it nighttime
>
>
>       If(!(timeTracker->refHour() >= timeTracker->refHourDay() && timeTracker->refHour() < timeTracker->refHourNight()))
>
>
>       {
>
>
>          If(timeTracker->refHour() >= timeTracker->refHourNight())
>
>
>          {
>
>
>             ambientred! = ambientgreen! = ambientblue! = timeTracker->refLightNight() + timeTracker->refLightInc2() * (timeTracker->refHour() - timeTracker->refHourNight())
>
>
>          }
>
>
>          If(timeTracker->refHour() < timeTracker->refHourNight())
>
>
>          {
>
>
>             ambientred! = ambientgreen! = ambientblue! = timeTracker->refLightNight() + (timeTracker->refLengthDay() - timeTracker->refHourNight() + timeTracker->refHour())
>
>
>          }
>
>
>       }
>
>
>    }
>
>
>
>
>
>    If(timeTracker->refHourDay() > timeTracker->refHourNight())
>
>
>    {
>
>
>       // Is it nighttime
>
>
>       If(timeTracker->refHour() >= timeTracker->refHourNight() && timeTracker->refHour() < timeTracker->refHourDay())
>
>
>       {
>
>
>          ambientred! = ambientgreen! = ambientblue! = timeTracker->refLightNight() + timeTracker->refLightInc2() * (timeTracker->refHour() - timeTracker->refHourNight())
>
>
>       }
>
>
>
>
>
>       // Is it daytime
>
>
>       If(!(timeTracker->refHour() >= timeTracker->refHourNight() && timeTracker->refHour() < timeTracker->refHourDay()))
>
>
>       {
>
>
>          If(timeTracker->refHour() >= timeTracker->refHourDay())
>
>
>          {
>
>
>             ambientred! = ambientgreen! = ambientblue! = timeTracker->refLightDay() - timeTracker->refLightInc1() * (timeTracker->refHour() - timeTracker->refHourDay())
>
>
>          }
>
>
>          If(timeTracker->refHour() < timeTracker->refHourDay())
>
>
>          {
>
>
>             ambientred! = ambientgreen! = ambientblue! = timeTracker->refLightDay() - timeTracker->refLightInc1() * (timeTracker->refLengthDay() - timeTracker->refHourDay() + timeTracker->refHour())
>
>
>          }
>
>
>       }
>
>
>    }
>
>
>
>
>
>    ForceRedraw()
>
>
>
>
>
>    Delay(1)
>
>
> }
> ```
>

So can you help oh wise one?

### Bad Kids · 2005-01-03 01:34 · #B150225

whoa lots of code 4 a simple timer. I'm too lazy to check it but I know they are ways to make that alot smaller! *Checks* Arg! Classes need to learn that >:/ . I think u can amke a timer with like only 10 lines of code. *Edit* looks again o it's a calender type thing. Got to see Word2 fix this Smile.

### Nanukimo · 2005-01-03 20:10 · #B150549

you could always help me i have a post on custiminsation forum. my code isint working the way it should, if u have any input be much appreicated Razz

### darkdragonkillr · 2005-01-04 03:30 · #B150833

i was wondering if there was anyway to make a prg that could let the player fish, mine, etc.

### garnetrising · 2005-01-04 05:41 · #B150909

**darkdragonkillr wrote:**

> i was wondering if there was anyway to make a prg that could let the player fish, mine, etc.
>

I think with a bit of patience and enough programming skill something like fishing or mining would be possible to code. If you give me a day, I could probably put together a very basic version of such a code. Smile

> [!missing] gap:16-30 · http://toolkitzone.com/forums/viewtopic.php?t=12451&start=15 · never-captured
> Page 2 of 2 was not recovered.
