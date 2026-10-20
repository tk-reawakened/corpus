---
kind: forum-thread
id: "toolkitzone-forums/30422"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Newbie Haven"
skin: "phpbb2"
thread_id: "30422"
title: "how do you make credits at the end?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=30422"
written: "2006-06-10T17:30:00"
last_post: "2006-06-11T20:50:00"
date_confidence: "exact"
captured: ["20060612042539"]
author: "munkeeboi"
repliers: ["DrakeLord", "ddl2829", "THeanimeguy", "Malegnis"]
authors: ["munkeeboi", "DrakeLord", "ddl2829", "THeanimeguy", "Malegnis"]
posts_present: 14
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_326639", captured: "20060612042539", sha256: "b020114e250bdc4ecba8b2e8ffcf3fd060c904f49e72510c302ef53ed99ae182", wayback_url: "https://web.archive.org/web/20060612042539/http://www.toolkitzone.com/forums/viewtopic.php?p=326639"}
links: []
---

# how do you make credits at the end?

### munkeeboi · 2006-06-10 17:30 · #B326332

can some one tell me how to make credits? i really dont know how to Embarassed

### DrakeLord · 2006-06-10 18:20 · #B326341

Well, what kind of credits?
If you want credits that are just...there. Like no movement or anything, just create a program with a bunch of Text() or PixelText() in it.
Scrolling text, that moves up or down, I have no idea.
Text that fades in and out, you could probably do something like this:

**Code:**

```
colorrgb(50,50,50)

Text(1,1,"munkeeboi")

delay(0.3)

colorrgb(100,100,100)

Text(1,1,"munkeeboi")

delay(0.3)

colorrgb(150,150,150)

Text(1,1,"munkeeboi")

delay(0.3)

colorrgb(200,200,200)

Text(1,1,"munkeeboi")

delay(0.3)

colorrgb(250,250,250)

Text(1,1,"munkeeboi")

delay(3)

colorrgb(200,200,200)

Text(1,1,"munkeeboi")

delay(0.3)

colorrgb(150,150,150)

Text(1,1,"munkeeboi")

delay(0.3)

colorrgb(100,100,100)

Text(1,1,"munkeeboi")

delay(0.3)

colorrgb(50,50,50)

Text(1,1,"munkeeboi")

delay(0.3)
```

But for some reason, I'd think that'd be a poor way of doing.
But anyway, there's not much to it. Just a bunch of text and stuff.

### ddl2829 · 2006-06-10 20:35 · #B326363

i submitted a method to the resources titled scrolling text, it has a good one you can use. only problem: it only scrolls one line at a time

### THeanimeguy · 2006-06-10 21:04 · #B326375

Too lazy to do the code, but wouldn't drawing a canvas with all of the text on it work. Then you could clear the screen and move it up a bit, clear the screen and move it up a bit. You'd probably (almost definetly) end up having to use -'s on the Y axis, but it should still work. If somebody ISNT too lazy to do the code right now maybe they want to draw it up for the kid?
Or an even crazier idea: Give the main player invisible animations, then load a board with a bitmap of the credits. Have a code forcing the player up. It'll look like it's scrolling credits!

### ddl2829 · 2006-06-10 21:20 · #B326377

**theanimeguy wrote:**

> If somebody ISNT too lazy to do the code right now maybe they want to draw it up for the kid?
>

fine... here:

**Code:**

```
cnv! = createcanvas(640,480)

y! = 480

y2!= 500

y3! = 520//yes these are off the screen - make sure they are 20 pixels apart when you add more

:goup

y! = y!-1

y2! = y2!-1

y3! = y3!-1 //changing this will increase the speed. -2 will double, -3 will triple, ect.

clear(cnv!)

pixeltext(1,y!,"name blah blah",cnv!)

pixeltext(1,y2!,"blah blah",cnv!)

pixeltext(1,y3!,"blah blah more",cnv!)

drawcanvas(cnv!,0,0)

if(y3! = 0)

{

branch(:out)

}

branch(:goup)

:out

killcanvas(cnv!)

end()
```

it does not flicker. just continue to add more with the y3,y4,y5, ect.[/quote]

### THeanimeguy · 2006-06-10 21:37 · #B326379

Note: My second idea DOES work, and it is kind of cool because it's less work, just more bulky. A few things you may want to note with my second idea: You should set the On Entering Board Program to this:

**Code:**

```
viewbrd("BOARD WITH SCROLLING.brd")

putplayer("PLAYER HANDLE", 1, 1, 1)

Push("South, South, ect. (your total Y Axis minus 1)", "PLAYER HANDLE")
```

And make sure your player step is set to something unresonably low, 3-4 steps per seconds should do it.

### ddl2829 · 2006-06-10 21:41 · #B326380

the way i programmed it works too
there, happy animeguy!?

### THeanimeguy · 2006-06-10 23:28 · #B326394

Are you high or something? Lol, you take my idea, and then responding to another one of my ideas you call it your idea. ( This may sound like an insult, it really isn't. I'm just saying it's kinda funny you would word it like that. )

### ddl2829 · 2006-06-10 23:30 · #B326395

**THeanimeguy wrote:**

> Are you high or something?
>

damn, how did you know!?

### Malegnis · 2006-06-11 07:17 · #B326500

**ddl2829 wrote:**

>
> **theanimeguy wrote:**
>
> > If somebody ISNT too lazy to do the code right now maybe they want to draw it up for the kid?
> >
>
> fine... here:
>
> **Code:**
>
> ```
> cnv! = createcanvas(640,480)
>
>
> y! = 480
>
>
> y2!= 500
>
>
> y3! = 520//yes these are off the screen - make sure they are 20 pixels apart when you add more
>
>
> :goup
>
>
> y! = y!-1
>
>
> y2! = y2!-1
>
>
> y3! = y3!-1 //changing this will increase the speed. -2 will double, -3 will triple, ect.
>
>
> clear(cnv!)
>
>
> pixeltext(1,y!,"name blah blah",cnv!)
>
>
> pixeltext(1,y2!,"blah blah",cnv!)
>
>
> pixeltext(1,y3!,"blah blah more",cnv!)
>
>
> drawcanvas(cnv!,0,0)
>
>
> if(y3! = 0)
>
>
> {
>
>
> branch(:out)
>
>
> }
>
>
>
>
>
> branch(:goup)
>
>
>
>
>
>
>
>
> :out
>
>
>
>
>
> killcanvas(cnv!)
>
>
>
>
>
> end()
> ```
>
> it does not flicker. just continue to add more with the y3,y4,y5, ect.
>

this code is efficient, but branch is outdated and it shouldent be used.
i would ue this inctead

**Code:**

```
cnv! = createcanvas(640,480)

y! = 480

y2!= 500

y3! = 520

While(done!~=true)

{

   y! = y!-1

   y2! = y2!-1

   y3! = y3!-1 //changing this will increase the speed. -2 will double, -3 will triple, ect.

   clear(cnv!)

   pixeltext(1,y!,"name blah blah",cnv!)

   pixeltext(1,y2!,"blah blah",cnv!)

   pixeltext(1,y3!,"blah blah more",cnv!)

   drawcanvas(cnv!,0,0)

   if(y3! = 0)

   {

      done!=true

   }

}

killcanvas(cnv!)

end()
```

### THeanimeguy · 2006-06-11 13:03 · #B326542

**ddl2829 wrote:**

>
> **THeanimeguy wrote:**
>
> > Are you high or something?
> >
>
> damn, how did you know!?
>

So are you HIGH, or are you SOMETHING? Never really answered, just said 'how did you know!?'

### ddl2829 · 2006-06-11 17:24 · #B326583

**THeanimeguy wrote:**

>
> **ddl2829 wrote:**
>
> >
> > **THeanimeguy wrote:**
> >
> > > Are you high or something?
> > >
> >
> > damn, how did you know!?
> >
>
> So are you HIGH, or are you SOMETHING? Never really answered, just said 'how did you know!?'
>

something that is high. there
and malegnis, i used branch cause the program is really short and branch is easy to understand. plus, unlike in a long program, you can use branch here cause your not gonna search forever for where it branches to

### THeanimeguy · 2006-06-11 18:24 · #B326607

**ddl2829 wrote:**

>
> **THeanimeguy wrote:**
>
> >
> > **ddl2829 wrote:**
> >
> > >
> > > **THeanimeguy wrote:**
> > >
> > > > Are you high or something?
> > > >
> > >
> > > damn, how did you know!?
> > >
> >
> > So are you HIGH, or are you SOMETHING? Never really answered, just said 'how did you know!?'
> >
>
> something that is high. there
> and malegnis, i used branch cause the program is really short and branch is easy to understand. plus, unlike in a long program, you can use branch here cause your not gonna search forever for where it branches to
>

You're NEVER supposed to use branch. And by telling a noob to use branch you're already screwing up. It doesn't matter how appropriate it is at the time. Unless you have a good understanding of RPGcode you should never use Branch(). And even then it's frowned upon.

### Malegnis · 2006-06-11 20:50 · #B326639

**ddl2829 wrote:**

>
> **THeanimeguy wrote:**
>
> >
> > **ddl2829 wrote:**
> >
> > >
> > > **THeanimeguy wrote:**
> > >
> > > > Are you high or something?
> > > >
> > >
> > > damn, how did you know!?
> > >
> >
> > So are you HIGH, or are you SOMETHING? Never really answered, just said 'how did you know!?'
> >
>
> something that is high. there
> and malegnis, i used branch cause the program is really short and branch is easy to understand. plus, unlike in a long program, you can use branch here cause your not gonna search forever for where it branches to
>

just saying, espicialy to a new RPG code programmer, branch is a bad habbit.
