---
kind: forum-thread
id: "toolkitzone-forums/11874"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "11874"
title: "Uhm... Some Maths, Operators, Variable Help...."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11874"
written: "2004-11-29T03:55:00"
last_post: "2004-12-01T11:42:00"
date_confidence: "exact"
captured: ["20050113181702"]
author: "matt72186"
repliers: ["Euix", "spitfire", "Dont_Think_So"]
authors: ["matt72186", "Euix", "spitfire", "Dont_Think_So"]
posts_present: 5
pages_present: [2]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 15, url: "http://toolkitzone.com/forums/viewtopic.php?t=11874", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_132798_amp_", captured: "20050113181702", sha256: "31be9b1ff9ee758eb712c93f5a4700a9aa733864dfc9d42c448d7579b00b8b4f", wayback_url: "https://web.archive.org/web/20050113181702/http://www.toolkitzone.com/forums/viewtopic.php?p=132798&amp="}
links: []
---

# Uhm... Some Maths, Operators, Variable Help....

> [!missing] gap:1-15 · http://toolkitzone.com/forums/viewtopic.php?t=11874 · never-captured
> Page 1 of 2 was not recovered.

### matt72186 · 2004-11-29 03:55 · #B131434

just to let you know

**Code:**

```
Zhak["TotalCondition"]! = Zhak["MaxHP"]! + Zhak["MapMP"]!

Zhak["Condition"]! = Zhak["HP"]! + Zhak["MP"]!

percCrit! = 0.33 * Zhak["TotalCondition"]!

percStable! = 0.66 * Zhak["TotalCondition"]!

if (Zhak["Condition"]! <= percCrit!){

  Zhak["Condition"]$ = "Critical"

}

elseif (Zhak["Condition"]! > percCrit! && Zhak["Condition"]! <= percStable!){

  Zhak["Condition"]$ = "Stable"

}

elseif (Zhak["Condition"]! > percStable!){

  Zhak["Condition"]$ = "Superior"

}
```

Has redudant checks, you can accomplish it with

**Code:**

```
Zhak["TotalCondition"]! = Zhak["MaxHP"]! + Zhak["MapMP"]!

Zhak["Condition"]! = Zhak["HP"]! + Zhak["MP"]!

percCrit! = 0.33 * Zhak["TotalCondition"]!

percStable! = 0.66 * Zhak["TotalCondition"]!

if (Zhak["Condition"]! <= percCrit!){

  Zhak["Condition"]$ = "Critical"

}

elseif (Zhak["Condition"]! <= percStable!){

  Zhak["Condition"]$ = "Stable"

}

elseif (Zhak["Condition"]! > percStable!){

  Zhak["Condition"]$ = "Superior"

}
```

Because if the first one doesn't work than in the second it is implied that Zhak["Condition"]! is greater than percCrit!

### Euix · 2004-11-29 21:59 · #B131727

I noticed that just as I was reading over this post to see if my reply helped.. stupid Euix. *smack*
That happens often, hah. Razz

### spitfire · 2004-12-01 01:31 · #B132492

ARRRGH!!!
Alright theres what I have right now. It still doesn't work....
Method CheckZhakCondition()
{
Zhak[TotalCondition]! = Zhak[MaxHP]! + Zhak[MaxMP]!
Zhak[Condition]! = Zhak[HP]! + Zhak[MP]!
percCrit! = 0.33 * Zhak[TotalCondition]!
percStable! = 0.66 * Zhak[TotalCondition]!
If (Zhak[Condition]! <= percCrit!)
{
Zhak[Condition]$ = "Critical"
}
ElseIf (Zhak[Condition]! <= percStable!)
{
Zhak[Condition] = "Stable"
}
ElseIf (Zhak[Condition]! > percStable!)
{
Zhak[Condition]$ = "Superior"
}
}
Then in the menu, I call the method... It shows the bkg image slowly fading in, and that's it. ARRGH!

### Dont_Think_So · 2004-12-01 02:14 · #B132535

I noticed there is a shocking lack of drawing commands in that method, could we see your whole code? Also, try using MWin to see if that was indeed set to the correct variable.
Further, I see that there is no $ in your Stable if.

### Euix · 2004-12-01 11:42 · #B132798

Also, it's not 'required', but you're suppose to put qoutes between the [] brackets when using maps.
ie.
arrayMap["Map"]!
arrayMap["Map"]$
instead of...
arrayMap[Map]!
arrayMap[Map]$
I think that would be a 'requirement' in 3.05, as maps with no qoutes may be confused with Object-type variables (variables with no symbol, used for classes). Razz
