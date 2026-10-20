---
kind: forum-thread
id: "toolkitzone-forums/22932"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "22932"
title: "Help with IF statement for Flash movie!!"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=22932"
written: "2005-08-27T14:26:00"
last_post: "2005-08-27T18:23:00"
date_confidence: "exact"
captured: ["20051112075118"]
author: "Dragen"
repliers: ["Tao-Kun"]
authors: ["Dragen", "Tao-Kun"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_250920_amp_3Bsid_cb94da1e2d09364c6250c0f48102d2e0", captured: "20051112075118", sha256: "be58e3c4bae0f06f334cfdc8f58ddfa2da8412d281905d406317d14a808c771c", wayback_url: "https://web.archive.org/web/20051112075118/http://www.toolkitzone.com/forums/viewtopic.php?p=250920&amp%3Bsid=cb94da1e2d09364c6250c0f48102d2e0"}
links: []
---

# Help with IF statement for Flash movie!!

### Dragen · 2005-08-27 14:26 · #B250920

**Code:**

```
#SetFlashMovie(0, "Intro.swf", 0, 0, 1024, 768)

#SWF_SetLoop(0, 1)

#swfFSCommand[0]$="auto"

IsPlaying! = 1

MovieEnd! = 0

While(IsPlaying! == 1)

{

   If(a$ = "ENTER")

   {

      #SWF_Remove(0)

      IsPlaying! = 0

   }

   If(#MovieEnd! == 1)

   {

      #SWF_Remove(0)

      IsPlaying! = 0

   }

}

}

#Kill(IsPlaying!)

#Kill(#MovieEnd!)
```

Can anyone help me here???
My problem is that I can't figure out how to get both of my If statements to run at the same time. As it is at the moment only the

**Code:**

```
   If(#MovieEnd! == 1)

   {

      #SWF_Remove(0)

      IsPlaying! = 0

   }
```

will actually have any affect. If I change the first IF statement to

**Code:**

```
wait(a$)

   If(a$ = "ENTER")

   {

      #SWF_Remove(0)

      IsPlaying! = 0

   }
```

Then only this one will have any affect.
The second IF statement removes the flash movie once it's finished.
What I need is it to quit if you press enter during it playing and also quit at the end... It's probably really simple so please help!!

### Tao-Kun · 2005-08-27 17:25 · #B250964

If you need it to quit the game, just use #Dos() in the flash movie.
But mainly, I can not determain the problem without seeing the coding within the flash movie.
Also, remove that extra "}" at the end of the program. Its not needed. And that "#" before the varible. Most likely, its a problem in the flash movie, becuase if the "a$=="ENTER""Statement works, then surely the 2nd state ment will work as well.
Only in the flash movie will you use the "#" Sign. In the program, its not needed.

### Dragen · 2005-08-27 18:23 · #B250996

**Tao-Kun wrote:**

> If you need it to quit the game, just use #Dos() in the flash movie.
> But mainly, I can not determain the problem without seeing the coding within the flash movie.
> Also, remove that extra "}" at the end of the program. Its not needed. And that "#" before the varible. Most likely, its a problem in the flash movie, becuase if the "a$=="ENTER""Statement works, then surely the 2nd state ment will work as well.
> Only in the flash movie will you use the "#" Sign. In the program, its not needed.
>

I don't want it to quit the game (I should have phrased it better). I want the flash movie to be removed: #SWF_Remove(0).
The only code within the flash movie is

**Code:**

```
FSCommand("#MovieEnd! = 1")
```

On the last frame to connect with the below code and remove the video.

**Code:**

```
   If(#MovieEnd! == 1)

   {

      #SWF_Remove(0)

      IsPlaying! = 0

   }
```

Will it help if I say I'm using the flash plugin for TK3???
