---
kind: forum-thread
id: "toolkitzone-forums/17353"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "classes"
skin: "phpbb2"
thread_id: "17353"
title: "Classes and Threads...."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=17353"
written: "2005-04-04T18:14:00"
last_post: "2005-04-04T18:14:00"
date_confidence: "exact"
captured: ["20050406051642"]
author: "Allan@Aljo"
repliers: []
authors: ["Allan@Aljo"]
posts_present: 1
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_190246_amp_", captured: "20050406051642", sha256: "2155da18282b01b8a80828be1999bd869069618d1a6337eebeabbc71513dd661", wayback_url: "https://web.archive.org/web/20050406051642/http://www.toolkitzone.com:80/forums/viewtopic.php?p=190246&amp"}
links: []
---

# Classes and Threads....

### Allan@Aljo · 2005-04-04 18:14 · #B190246

Ok first let me put up my source....

**Code:**

```
////////////

weather.prg

///////////

Class Weather

{

   public:

      Method Weather()

      Method Weather(Weather rhs!)

      Method ~Weather()

      Method SetWeather(newweather$)

      Method RunWeather()

   private:

      currentweather$

      isweather!

      weathercnv[]!

      resx!

      resy!

}

Method Weather::Weather()

{

   currentweather$="clear"

   getres(resx!,resy!)

}

Method Weather::Weather(Weather rhs!)

{

   currentweather$=rhs->currentweather$

   resx!=rhs->resx!

   resy!=rhs->resy!

   isweather!=rhs->isweather!

}

Method Weather::~Weather()

{

}

Method Weather::SetWeather(newweather$)

{

   currentweather$=newweather$

}

Method Weather::RunWeather()

{

   rendernow("on")

   getRes(resx!, resy!)

   weathercnv[1]!=createcanvas(resx!,resy!)

   setimage("rain.gif",0,0,resx!,resy!,weathercnv[1]!)

   weathercnv[2]!=createcanvas(resx!,resy!)

   setimage("rain2.gif",0,0,resx!,resy!,weathercnv[2]!)

   weathercnv[3]!=createcanvas(resx!,resy!)

   setimage("rain3.gif",0,0,resx!,resy!,weathercnv[3]!)

   count!=1

   while(currentweather$~="clear")

   {

      show(currentweather$)

      show(resx!)

      wait()

      multiRun()

      {

         clear(cnvRenderNow!)

         drawcanvastransparent(weathercnv[count!]!,0,0,255,0,255,resx!,resy!,cnvRenderNow!)

      }

      //Threadsleep(0,1)

      count!--

      if(count!==4)

      {

         count!=1

      }

   }

}
```

As of now I know this has memory leaks... but that's not the ordeal at hand...

**Code:**

```
/////////

start.prg

/////////

#include "Weather.prg"

bweather=Weather()

bweather=Weather()

bweather->SetWeather("rain")
```

now I have a program threaded on a board that looks like this

**Code:**

```
//////////

thread.prg

/////////

#include "weather.prg"

bweather->RunWeather()
```

Ok here's my problem
I create a canvas and I'm mwining my resolution vars resx! and resy! as well as currentweather$ The first time through the while loop they show up.... the next time through the while loop I get a blank for currentweather$ and 0 for resx! and resy! I made resx! and resy! both local variables at one time... and they held. I also took the RunWeather() function and put it's contents in the thread itself like so

**Code:**

```
currentweather$="rain"

rendernow("on")

   getRes(resx!, resy!)

   weathercnv[1]!=createcanvas(resx!,resy!)

   setimage("rain.gif",0,0,resx!,resy!,weathercnv[1]!)

   weathercnv[2]!=createcanvas(resx!,resy!)

   setimage("rain2.gif",0,0,resx!,resy!,weathercnv[2]!)

   weathercnv[3]!=createcanvas(resx!,resy!)

   setimage("rain3.gif",0,0,resx!,resy!,weathercnv[3]!)

   count!=1

   while(currentweather$~="clear")

   {

      show(currentweather$)

      show(resx!)

      wait()

      multiRun()

      {

         clear(cnvRenderNow!)

         drawcanvastransparent(weathercnv[count!]!,0,0,255,0,255,resx!,resy!,cnvRenderNow!)

      }

      //Threadsleep(0,1)

      count!--

      if(count!==4)

      {

         count!=1

      }

   }
```

and I got it to stick... anyone got any suggestions?
