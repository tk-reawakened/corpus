---
kind: forum-thread
id: "toolkitzone-forums/11844"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "11844"
title: "Help with some Variables and maths.."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11844"
written: "2004-11-27T23:06:00"
last_post: "2004-12-04T02:17:00"
date_confidence: "exact"
captured: ["20050114191929"]
author: "spitfire"
repliers: ["p90m16mp5a4", "Dont_Think_So"]
authors: ["spitfire", "p90m16mp5a4", "Dont_Think_So"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_134369_amp_", captured: "20050114191929", sha256: "f3d9011401e978a159778b43429aaadb66058c8e59c2c984dee3cf2f82c50bba", wayback_url: "https://web.archive.org/web/20050114191929/http://www.toolkitzone.com/forums/viewtopic.php?p=134369&amp="}
links: []
---

# Help with some Variables and maths..

### spitfire · 2004-11-27 23:06 · #B131007

**rpgcode:**

```
******************************

*#Setup_Kara_Initial()********

*Sets up Kara's initial stats*

******************************

Method Setup_Kara_Initial()

{

     Kara[name]$ = "Kara"

     Kara[MaxHP]! = 500

     Kara[HP]! = 250

     Kara[MaxMP]! = 80

     Kara[MP]! = 20

     Kara[Holy]! = 15

     Kara[Dark]! = 15

     Kara[Additive]! = 15

     Kara[Subtractive]! = 15

     Kara[Attack]! = 30

     Kara[Defence]! = 20

     Kara[Weapon]$ = "Magicks"

     Kara[Power]! = Kara[MaxHP]!+Kara[MaxMP]!+Kara[Holy]!+Kara[Dark]!+Kara[Additive]!+Kara[Subtractive]!+Kara[Attack]!+Kara[Defence]!

     Kara[TotalState]! = Kara[MaxHP]!+Kara[MaxMP]!

     Kara[State]! = Kara[HP]!+Kara[MP]

     If(Kara[State]! &lt; (.33*=Kara[TotalState]!))

     {

          Kara[State]$ = "Critical"

     }

     ElseIf(Kara[State]! &lt;(.66*Kara[TotalState]! &amp;&amp; &gt;(.33*=Kara[TotalState]!))

     {

          Kara[State]$ = "Stable"

     }

     ElseIf((Kara[State]! &lt;=(Kara[TotalState]! &amp;&amp; &gt;(.66*=Kara[TotalState]!))

     {

          Kara[State]$ = "Superior"

     }
```

What I want it to do is display what state the character is in... any help?

### spitfire · 2004-11-27 23:08 · #B131010

OK, I got it to work... lol now, any tips on my code?

### p90m16mp5a4 · 2004-12-04 02:16 · #B134367

I already posted on your previous one.. however I forgot that you were doing a whole array... so my post was kinda worthless... yep..
if you wanna show a variable you can use :
#show(var!/var$)
#mwin(" Heres my variable var! <var!>)
#text(5,5,"<var!>")
wait.. wheres your method closing bracket on line 37?

### Dont_Think_So · 2004-12-04 02:17 · #B134369

Tools->Indent Wizard. Hooray.
