---
kind: forum-thread
id: "toolkitzone-forums/12648"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "12648"
title: "Posible bug, did anyone else mentino this before?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12648"
written: "2004-12-15T05:24:00"
last_post: "2004-12-20T03:16:00"
date_confidence: "exact"
captured: ["20050119211516"]
author: "Levi"
repliers: ["Serge", "Occasionally_Correct", "matt72186", "Rueben", "nOObified", "Dont_Think_So"]
authors: ["Levi", "Serge", "Occasionally_Correct", "matt72186", "Rueben", "nOObified", "Dont_Think_So"]
posts_present: 9
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_140068_amp_", captured: "20050119211516", sha256: "88ee24b8fb659002d1f2c219b50db0dc143e63e73057f32c4fbe86a0a0073c2a", wayback_url: "https://web.archive.org/web/20050119211516/http://www.toolkitzone.com/forums/viewtopic.php?p=140068&amp="}
links: []
---

# Posible bug, did anyone else mentino this before?

### Levi · 2004-12-15 05:24 · #B140021

Okay The following statements activate an else statement that is suppose to be used.
#If(x1y[a!]!==0)
{
#MWin("You're in")
a! ++
#If(c!==2)
{
}
}
Else()
{
#MWin("You're in")
}
I think that when the first if statement is interrupted by teh second the else is associated with the second if. The if being false will activivate the else statement.

### Serge · 2004-12-15 06:13 · #B140035

Err, why don't you just give the second if it's own else?
I don't see the problem. I'm pretty sure it's how it's supposed to be.

### Levi · 2004-12-15 06:49 · #B140044

Well I'm no fool. Tried that. Didn't work. I just think its a small error. Something easily fixed. I've tried it many ways, the only way to over come it is to change the else to its own if statement in the old fashion of TK2.
Definatly not how its suppose to be. The second if is officially ended and then so is the first if allowing the else to be associated with the original if. However that doesn't seem to be the case. It's like it wasn't designed for nesting if statements.

### Occasionally_Correct · 2004-12-15 07:00 · #B140049

I don't really understand what your problem is. I tested it and it runs as expected, for me.
The first if statement is true (and is executed), so the else statement is automatically false (and is not executed). Is there any more code, or is that it?

### Levi · 2004-12-15 07:06 · #B140051

The problem is that when the second if statement evaluates to false the else statement for some reason deploys.
In the code given if you put #wait(a$) at the bottom you'll see two You're in messages appear. Or at least that's what I'm experiencing.
The code given was a simplified version of someone else's problem. They posted it in the RPGCode section. I belive the user is Zio.
Here's the code they sent.

**Code:**

```
While(FogInnerY! < 39)

{

#If (X1Y[FogInnerY!]! == 0)

   {

   FogInnerY!++

   #SetImage("cover1.bmp",Fogx!,Fogy!,13,13)

   Fogx! = Fogx! + 12

   Fogloopx!++

   #If(Fogloopx! == 3)

      {

      Fogloopx! = 0

      Fogx! = Fogx! + 3

      }

   }

#Else()

   {

   #If(X0Y[FogInnerY!]! = 0)

      {

      #SetImageTransparent("CoverInner4.bmp",fogx!,fogy!,13,13,255,0,255)

      }

   FogInnerY!--

   #If(X1Y[FogInnerY!]! = 0)

      {

      #SetImageTransparent("CoverInner2.bmp",fogx!,fogy!,13,13,255,0,255)

      }

   FogInnerY! = FogInnerY! + 2

   #If(X1Y[FogInnerY!]! = 0)

      {

      #SetImageTransparent("CoverInner3.bmp",fogx!,fogy!,13,13,255,0,255)

      }

   FogInnerY!--

      #If(X2Y[FogInnerY!]! = 0)

      {

      #SetImageTransparent("CoverInner1.bmp",fogx!,fogy!,13,13,255,0,255)

      }

   Fogx! = Fogx! + 12

   }

}
```

It had the same effect. I made the simpler model in hopes of rebuilding it from the ground up to find the problem. I found that second if statement.

### matt72186 · 2004-12-15 08:09 · #B140068

I see what you mean, yeah this is a problem, here's what I tested

**Code:**

```
Fade(1)

ColorRGB(255, 255, 255)

a! = 0

If (a! == 0)

{

   MWin("Test")

   If (a! == 1)

   {

   }

}

Else ()

{

   MWin("Test")

}

Wait()
```

It outputs Test twice, even though it should only show it once.

### Rueben · 2004-12-17 15:28 · #B141085

Finally, people are starting to see my problems. For the record, I've also had problems where no if/else commands within while loops are activated, no matter how much you insist your code is correct. Smile

### nOObified · 2004-12-20 03:03 · #B142389

**Quote:**

> I've also had problems where no if/else commands within while loops are activated,
>

I've also encountered this. And fixed the problem by using Switch/Case instead of If/Then. I'm starting to like Switch/Case more anyways, and can't really see a use for ever using IF unless it's just a one time thing.

### Dont_Think_So · 2004-12-20 03:16 · #B142401

That's a bug that's been fixed.
