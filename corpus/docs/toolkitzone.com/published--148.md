---
kind: doc
id: "toolkitzone.com/148"
site: "toolkitzone.com"
title: "Published"
original_url: "http://www.toolkitzone.com/library.php?doc=148&highlight="
written: "2007-01-25"
date_confidence: "day"
updated: "2007-01-25"
captured: ["20060208122812", "20060209095952", "20070308231700", "20070313074149"]
author: "Colin"
repliers: []
authors: ["Colin"]
comments_present: 0
f_author: "Colin"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_amp_3Bdoc_148", captured: "20060208122812", sha256: "faf02b4e6f962cf114f69781c65d56c6e94151a87c30ad849c3690a6c6da6647", wayback_url: "https://web.archive.org/web/20060208122812/http://toolkitzone.com/library.php?mode=read&amp%3Bdoc=148"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_148", captured: "20060209095952", sha256: "074ac8ba60b9e487788ede8b1e11dfbf4d29a9d2edbaf9fabdbb5c0ea438832e", wayback_url: "https://web.archive.org/web/20060209095952/http://www.toolkitzone.com:80/library.php?mode=read&view=cadd&doc=148&PHPSESSID=6c1f0d3aa43a19d10f2020f481c20c7a"}
  - {path: "wayback/toolkitzone.com/library.php__doc_148_highlight_", captured: "20070308231700", sha256: "10808805a677e44d70f70a5d284115eb1318961720ab4e16703fd74817e7ad3c", wayback_url: "https://web.archive.org/web/20070308231700/http://www.toolkitzone.com:80/library.php?doc=148&highlight"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_148", captured: "20070313074149", sha256: "89c39514bef0cc977c5321305d46d566594d3865bca976aefc009dae4b7cf94a", wayback_url: "https://web.archive.org/web/20070313074149/http://www.toolkitzone.com/library.php?mode=read&doc=148"}
---

# Published

Browse
TK3 Amelioration VIII ? Copy Constructing
For those of you who remember me promising a battle system, I know that it has been weeks. A variety of things needed to be discussed before we could code it ? more things than I had originally counted on. Today, unfortunately, is no exception. next week, but probably not, we?ll think about that battle system. This article covers a very important object oriented programming concept, and therefore is a must read if you plan to understand the battle system. *Maybe*
As you may know, a is a function whose job is to initialize the state of an object. The constructor can take arguments passed to it from the creator. Constructors that take only one parameter are . They are used to cast data to the type of your class. Cast constructors can be useful in making classes feel more ?natural? without overloading operators that can sometimes produce ambiguous results. Consider the following example. **constructor** **cast constructors**
class CString
public
CString(str$) { $ = str$ } method m_str
operator$() { ( $) } method returnMethod m_str
private
$ m_str
method test(CString str)
str) show(
wait()
mwincls
test( "Hello, world!")
When is called, passing in a string literal, a ?to be destroyed at the end of the line?of type is constructed from which saves the string passed in to its member. Later, it casts this object to type string in order to display it. Remember, this object will be destroyed when the line reaches its end, as it is only temporary. It is important to understand that objects that are directly constructed are merely temporary. Consider the following: test() **temporary object** CString CString::CString() *all*
test( "Hello, world!")) CString(
That line is directly equivalent to the one seen earlier. Next, observe this line:
str = "Hello, world!") CString(
Even the object created on the right-hand-side is temporary. The object on the left-hand-side is created by copying that on the right. First, it looks for a cast constructor that takes the type of the object itself?a ?and if one exists, it is called. However, if one doesn?t exist, the left-hand-side?s object is created by simply copying the values of the right-hand-side?s members to a new object. In this case, that works. In many cases, it works. Do trick yourself into coding redundant copy constructors. **copy constructor** *not*
That said, there are indeed some cases in which a copy constructor is required for execution of copying to succeed. The following is an example of code which will work: *not*
class CCanvas
public
(x!, y!) method CCanvas
! = (x y!) m_cnv createCanvas
! = x! m_width
! = y! m_height
pixel(x!, y!) (x!, y!, !) } method { setPixel m_cnv
draw(x!, y!) ( !, x!, y!) } method { drawCanvas m_cnv
~ () { ( !) } method CCanvas killCanvas m_cnv
private
! m_cnv
! m_width
! m_height
cnv = (50, 50) CCanvas
cnv ->pixel(5, 5)
cnv ->draw(0, 0)
wait()
Running this code provides you with no error messages, but a blank screen. Why? In the line that creates the canvas object, the left-hand-side is created via copying (as seen above). The problem lies in the fact that the canvas handle is copied over, but when the right-hand-side is destroyed at the end of the line, that very same canvas handle is killed. This can be remedied by providing a copy constructor:
method ( !) CCanvas CCanvas rhs
! = -> ! m_width rhs m_width
! = -> ! m_height rhs m_height
! = !, !) m_cnv createCanvas m_width m_height
-> !, 0, 0, !, !, !) drawCanvas rhs m_cnv m_width m_height m_cnv
This function performs a ?one that uses logic (direct copies being )?by creating a new canvas the size of the right-hand-side and then drawing its canvas onto our new one. Thus, copying the canvas, but leaving us with a new handle. If you code a copy constructor, you also need to provide an assignment operator. There are two integral differences between the two, however. The assignment operator must check to make sure it?s not being to itself, and clean up before copying. An assignment operator for the above class could be coded like this: **deep-copy** **shallow**
method operator=( !) CCanvas rhs
// setting to self Prevent
(this! ~= !) rhs
// up Clean
!) killCanvas m_cnv
// Now just copy over
! = -> ! m_width rhs m_width
! = -> ! m_height rhs m_height
! = !, !) m_cnv createCanvas m_width m_height
-> !, 0, 0, !, !, !) drawCanvas rhs m_cnv m_width m_height m_cnv
In conclusion, for many simple classes a shallow copy is more than sufficient. Whatever you do, don?t add a copy constructor . Evaluate your logic to decide whether possible flaws exist. Look for code that allocates and frees memory (dynamic arrays have this behavior too, though it?s not as apparent) for a sign that a copy constructor is needed. Good luck and hopefully, I?ll see you next week! *just because*
that is very complicated
Quick Jump
Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
Keyword(s)
All Categories Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
**Published**
January 16th, 2005
**User Rating**
No votes cast.
**Views**
Who's Online: , , , , , , , , , , , , , , , , , , , [Acra](community.php?user=5400) [Bagel](community.php?user=4798) [Colin](community.php?user=226) [DarkElite](community.php?user=580) [Diinn](community.php?user=15882) [Doc_Wellsy](community.php?user=36) [EB](community.php?user=84) [Icbim](community.php?user=3770) [jpsmtm](community.php?user=2476) [Juice](community.php?user=7931) [kainismine](community.php?user=15078) [Montai](community.php?user=39) [Occasionally_Correct](community.php?user=94) [purexhalegames](community.php?user=15862) [Reck](community.php?user=536) [Rydath](community.php?user=5633) [slipknot42388](community.php?user=9204) [StealthArcher](community.php?user=15959) [Tetsuo](community.php?user=598) [yaim0310](community.php?user=14246)
