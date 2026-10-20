---
kind: doc
id: "toolkitzone.com/179"
site: "toolkitzone.com"
title: "Expand"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=179"
written: "2005-02-07T11:25:00"
date_confidence: "exact"
updated: null
captured: ["20051212225439", "20060209100034", "20070302062309", "20070308231722"]
author: "Colin"
repliers: []
authors: ["Colin"]
comments_present: 0
f_author: "Colin"
f_date: "February 7, 2005, 11:25 am"
f_description: "The speed of RPGCode is only criticized, and justifiably so. Even the simplest of scripts seem to lag beyond belief. While the language could use some serious optimization, you are not without things you can do to improve the speed of your code. If you find your code running slower than you like, then this is the mini-series to read."
f_title: "Optimizing RPGCode, Part I"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_179", captured: "20051212225439", sha256: "0319ce20c277ae4d97dc7d4dbcd432967b99446d9f0b6f8bf3a072b858c916c8", wayback_url: "https://web.archive.org/web/20051212225439/http://www.toolkitzone.com/library.php?mode=read&doc=179"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_179", captured: "20060209100034", sha256: "316b9e287a7790f19c46fe0e56bc0c7e8160df752bcef6f9bfc4275eb661393b", wayback_url: "https://web.archive.org/web/20060209100034/http://www.toolkitzone.com:80/library.php?mode=read&view=cadd&doc=179&PHPSESSID=6c1f0d3aa43a19d10f2020f481c20c7a"}
  - {path: "wayback/toolkitzone.com/library.php__doc_179", captured: "20070302062309", sha256: "7675a1dde89a902418ce55fa1d0b5ea44986c2107cb5968941a271dcc2694d99", wayback_url: "https://web.archive.org/web/20070302062309/http://www.toolkitzone.com/library.php?doc=179"}
  - {path: "wayback/toolkitzone.com/library.php__doc_179_highlight_", captured: "20070308231722", sha256: "9edae83fa00223328994064ad823406767bd1b8b731e61eb490bd29eb4327039", wayback_url: "https://web.archive.org/web/20070308231722/http://www.toolkitzone.com:80/library.php?doc=179&highlight"}
---

# Expand

TK3 Amelioration X  Optimizing RPGCode, Part I
The speed of RPGCode is only criticized, and justifiably so. Even the simplest of scripts seem to lag beyond belief. While the language could use some serious optimization, you are not without things you can do to improve the speed of your code. This article will not only cover what you can do to increase speed, but myths about often falsely perceived boosters. If you find your code running slower than you like, then this is the mini-series to read.
**Use *iif***
Perhaps the most important group of tricks is the ability to notice optimization is possible. Redundant checks, loops, excessive variable manipulation  all these things are undesirable. Well be taking a look at many code snippets and examining exactly why they run slowly. The first thing to watch out for is pieces like this:
...
func
else
func
Such a code snippet can be condensed using an : *iif*
func iif(..., x, y
The marvels of said cannot easily be described. A general rule is something like this: if you have that only contains one line, attempt to shorten it. *iif* an *if*
**Expand**
Expand out bracketed areas running, as well as performing any mathematics, etc. Consider the following: *before*
!((x + 4 + 1 ) == 3)) { ... }
First, we can add the 4 and the 1:
!((x + 5 ) == 3)) { ... }
Next, we can factor in the logical NOT:
(x + 5 ) ~= 3) { ... }
Finally, well subtract 5 from both sides:
if ( ~= -2) { ... }
The latter version will run considerably faster, so be sure to perform all factorization, evaluation at design time.
**Dont Worry About Methods**
Sure, on TK2 using a method could cost you ages of processing time. TK3, however, is not the same, so do use methods. Lets look at precisely how minute the difference is:
! = 0; ! < 99; + ) { !++ } g_var
Time: About 188 milliseconds.
! = 0; ! < 99; + ) { () } func
method () { } func
Time: About 230 milliseconds.
Alas, the method calling is slower than another instruction (adding in the above case), but this is not large enough to worry anyone. Slower users may notice a light difference, but organization is, in my opinion, more important than such an insignificant quantity of milliseconds. *slightly*
**Dont Worry About Division**
Back in the days of Assembly, using or was sinful. In RPGCode, this is no longer the case. All mathematical operations (even exponentials) will evaluate at the same speed. This is because its the parsing of the lines that uses the vast majority of the time. Please, dont go out of your way to eliminate division, multiplication with complex series of shifts (I doubt anyone did this, but the point still stands). *MUV* *DIV* *exactly*
**More to Come**
These basic, common-sense, optimizations are extremely important to the speed of your programs. However, more complex situations do exist (frequently, in fact) and are not covered here. Next week, well explore optimizing much more complicated programs, and ideas.
UltimaWizard
June 8, 2005, 1:07 pm
Even for me, a decent newbie, this seems newbie-ish. I'll reserve judgement, though, for your other Optimization tutorials. In any case, I did finally figure out what Iif is for! thanks!
**Column**
Toolkit 3.x > TK3 Amelioration
The speed of RPGCode is only criticized, and justifiably so. Even the simplest of scripts seem to lag beyond belief. While the language could use some serious optimization, you are not without things you can do to improve the speed of your code. If you find your code running slower than you like, then this is the mini-series to read.
**Past Columns**
Feb 28, '05
Feb 13, '05
Jan 30, '05
Jan 16, '05
Jan 2, '05
Feb 28, '05
Feb 13, '05
Jan 30, '05
Jan 16, '05
Jan 2, '05
