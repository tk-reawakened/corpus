---
kind: forum-thread
id: "toolkitzone-forums/12294"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12294"
title: "who is kind enough to Train an Amateur?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12294"
written: "2004-12-07T23:30:00"
last_post: "2004-12-08T03:11:00"
date_confidence: "exact"
captured: ["20041227100025"]
author: "Kasai_Ryane"
repliers: ["TheCPPFreak220", "Chamgorie Chanbear", "Dark_sage"]
authors: ["Kasai_Ryane", "TheCPPFreak220", "Chamgorie Chanbear", "Dark_sage"]
posts_present: 10
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_136360_amp_", captured: "20041227100025", sha256: "dc87caea87f1500f3400886547b1e8e0eeda5d55e5fa09c6ec512389649c2286", wayback_url: "https://web.archive.org/web/20041227100025/http://www.toolkitzone.com/forums/viewtopic.php?p=136360&amp="}
links: []
---

# who is kind enough to Train an Amateur?

### Kasai_Ryane · 2004-12-07 23:30 · #B136197

wel...i've spent around 10 hours of time with RPGcode, and i havecloe to to know prgrm language experience. Im curious if anyone is will to tutor me(im also reading the tutorials) when they have spare time. Tutorials are great, but they dont tell you what you are doing wrong and how to fix it, and i dont want to spend my life posting here..i want to become very good with RPGcoding, and fix the problems myself. so if anyone is kind enough to tutor me, please notify me. AIM=Kasai_Ryane
~thx, kasai

### TheCPPFreak220 · 2004-12-07 23:33 · #B136201

I could help, I'm not that bad at it.
TheCPPFreak220@hotmail.com

### Kasai_Ryane · 2004-12-07 23:37 · #B136207

thx, lemme eat dinner. ill reply then

### Chamgorie Chanbear · 2004-12-07 23:51 · #B136219

By the way, what happened to the tutorials? I can't find them in the Library except for a couploe of Character tutorials.

### Kasai_Ryane · 2004-12-08 00:13 · #B136227

great! thanks for offering, msg me on Kasai Ryane, on aol instant messenger. and as for the online tutorials, im unsure. i use the program's tutorial.

### TheCPPFreak220 · 2004-12-08 00:33 · #B136232

Not shure what you mean

### Kasai_Ryane · 2004-12-08 01:59 · #B136299

ok...well. what is your AIM screen name if you have one? that way i can contact you, other than these forums. and if you dont feel like commiting to occasional help, if you could just proof read this, because i've tested and retested it and i cant figure out what is wrong. then again maybe trying to put a while loop inside another was a bad idea...:d

**rpgcode:**

```

```

### TheCPPFreak220 · 2004-12-08 02:11 · #B136312

Ok, i do not have AIM, but i do have msn, which i amalmost always on. It's TheCPPFreak220@hotmail.com
You did not post any code.

### Kasai_Ryane · 2004-12-08 02:40 · #B136343

thanks! I added you to my contacts, and mine is sschrembeck@hotmail.com.
and here is the code...somehow i forgot to put it in, sry.

**rpgcode:**

```
*this program was designed to give the player to pay a small fee to change the

*window color scheme to one of three preset choices

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

putting a while loop inside another while loop most definatly did not work out

### Dark_sage · 2004-12-08 03:11 · #B136360

You have this

**rpgcode:**

```
If(response$ == "1")

{

     GetGp(money!)

     If(money!&amp;gt;=100)

     {

          TakeGP(150)

          WincolorRGB(255, 255, 255)

          BorderColor(0, 0.0)

          Wait(a$)

          done2! = 1

     }

     If(money!&amp;lt;100)

     Mwin("sorry, you dont have enough money")

     done2! = 1

}
```

Shoudn't be this

**rpgcode:**

```
If(response$ == "1")

{

     GetGp(money!)

     If(money!&amp;gt;=100)

     {

          TakeGP(100)

          WincolorRGB(255, 255, 255)

          BorderColor(0, 0.0)

          Wait(a$)

          done2! = 1

     }

     If(money!&amp;lt;100)

     Mwin("sorry, you dont have enough money")

     done2! = 1

}
```

because you said Black and White is 100 gp arn't you takeing away 150
