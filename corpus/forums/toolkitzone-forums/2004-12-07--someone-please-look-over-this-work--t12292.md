---
kind: forum-thread
id: "toolkitzone-forums/12292"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12292"
title: "someone please look over this work"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12292"
written: "2004-12-07T22:35:00"
last_post: "2004-12-09T00:28:00"
date_confidence: "exact"
captured: ["20041227215407"]
author: "Kasai_Ryane"
repliers: ["solaceinsilence"]
authors: ["Kasai_Ryane", "solaceinsilence"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_136696_amp_", captured: "20041227215407", sha256: "82dadbeda73f7ace0fce59944c5b584e7772f2718cad9a89777265bbeef9e5f4", wayback_url: "https://web.archive.org/web/20041227215407/http://www.toolkitzone.com/forums/viewtopic.php?p=136696&amp="}
links: []
---

# someone please look over this work

### Kasai_Ryane · 2004-12-07 22:35 · #B136177

i've only spent about 10 semi concentrated hours with RPGcode so, im pretty new to it. i attempted to put a while loop in another while loop, it is a mess. someone please sort out how i might do this, keeping iin mind im still an amateur, thx
~Kasai

**rpgcode:**

```
Mwin("Welcome to the Customizing Shack")

Mwin("I am in charge of window color themes")

Mwin("Would you like to view the new color schemes for the message window?")

done! = 0

While(done! == 0)

{

     Prompt("", answer$)

*use this format to use typed in variables in text "&lt;variable name$&gt;!"

     If(answer$ == "yes")

     {

          MWin("Here is the selection")

          Wait(a$)

          MWin("1 :Black and White...100gp")

          MWin("2 :Frost...150gp")

          MWin("3 :Flame...150gp")

          Wait(response$)

          done2! = 0

          While(done2! == 0)

          {

               If(response$ == "1")

               {

                    GetGp(money!)

                    If(money!&gt;=100)

                    {

                         TakeGP(150)

                         WincolorRGB(255, 255, 255)

                         BorderColor(0, 0.0)

                         Wait(a$)

                         done2! = 1

                    }

                    If(money!&lt;100)

                    Mwin("sorry, you dont have enough money")

                    done2! = 1

               }

               If(response$ == "2")

               {

                    GetGp(money!)

                    If(money!&gt;=150)

                    {

                         TakeGP(150)

                         WincolorRGB(50, 50, 175)

                         BorderColor(175, 175.255)

                         Wait(a$)

                         done2! = 1

                    }

                    If(money!&lt;150)

                    Mwin("sorry, you dont have enough money")

                    done2! = 1

               }

               If(response$ == "3")

               {

                    GetGp(money!)

                    If(money!&gt;=150)

                    {

                         TakeGP(150)

                         WincolorRGB(175, 50, 50)

                         BorderColor(255, 175, 175)

                         Wait(a$)

                         done2! = 1

                    }

                    If(money!&lt;150)

                    Mwin("sorry, you dont have enough money")

                    done2! = 1

               }

          }

     }

     done! = 1

}

If(answer$ == "no")

{

     CallShop("maybe next time")

     done! = 1

}

}
```

### solaceinsilence · 2004-12-09 00:28 · #B136696

Try this code i fixed. I haven't tested it so try it and post back. But it should work. If there isnt anything you don't understand such as commands, check out the RPGReference under Help in the Toolkit. Smile Happy Coding...

**rpgcode:**

```
MWin("Welcome to the Customizing Shack")

MWin("I am in charge of window color themes")

MWin("Would you like to view the new color schemes for the message window?")

Done! = 0

While(Done! == 0)

{

     anwser$ = Prompt("Please enter yes or no.") *This will Prompt user for input and assign it

*to the anwser$ variable

     If(answer$ == "yes")

     {

          MWin("Here is the selection")

          MWin("1 :Black and White...100gp")

          MWin("2 :Frost...150gp")

          MWin("3 :Flame...150gp")

          Wait(response$)

          If(response$ == "1")

          {

               GetGP(money!)

               If(money! &gt;= 100) *If money is greater than OR equal to 100

               {

                    TakeGP(150)

                    WinColorRGB(55, 255, 255)

                    BorderColor(0, 0.0)

                    Wait()

               }

          }

          Else()

          {

               MWin("sorry, you dont have enough money")

          }

          If(response$ == "2")

          {

               GetGP(money!)

               If(money! == 10)

               {

                    TakeGP(150)

                    WinColorRGB(50, 50, 175)

                    BorderColor(175, 175.255)

                    Wait()

               }

          }

          Else()

          {

               MWin("sorry, you dont have enough money")

          }

          If(response$ == "3")

          {

               GetGP(money!)

               If(money! == 150)

               {

                    TakeGP(150)

                    WincolorRGB(175, 50, 50)

                    BorderColor(255, 175, 175)

                    Wait()

               }

          }

          Else()

          {

               MWin("sorry, you dont have enough money")

          }

     }

     done! = 1

}

Else()

{

     CallShop("maybe next time")

     done! = 1

}
```
