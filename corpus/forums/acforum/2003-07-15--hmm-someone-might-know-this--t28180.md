---
kind: forum-thread
id: "acforum/28180"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "28180"
title: "Hmm... Someone might know this..."
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1000&mode=1&msg=28180"
written: "2003-07-15T22:31:00"
last_post: "2003-07-15T24:50:00"
date_confidence: "exact"
captured: ["20030730094805", "20030730095626", "20030730100027", "20030730143929", "20030730144554"]
author: "jasond."
repliers: ["cy", "john@aljo", "thomas"]
authors: ["jasond.", "cy", "john@aljo", "thomas"]
posts_present: 5
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1000_mode_1_msg_28180", captured: "20030730094805", sha256: "7641e3d604e7dc854dee4fd32226c612e10a8722fceeff9d3fb6db5347e4aa37", wayback_url: "https://web.archive.org/web/20030730094805/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1000&mode=1&msg=28180"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1000_mode_1_msg_28184", captured: "20030730095626", sha256: "82bd70845fc847b56e2aa2d6d00ce8aee5b1fb3f82ddb709bba0c15c3b7d444e", wayback_url: "https://web.archive.org/web/20030730095626/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1000&mode=1&msg=28184"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1000_mode_1_msg_28187", captured: "20030730100027", sha256: "34de7fb025a5695ae328fbd8ff4ac4d1e2e4274553aacba8d2ee647d1a34add9", wayback_url: "https://web.archive.org/web/20030730100027/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1000&mode=1&msg=28187"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1000_mode_1_msg_28193", captured: "20030730143929", sha256: "dd9acfaefa0f628ce5e2680fe82d272c269d918c400f8832bf9448e7ab8bdec7", wayback_url: "https://web.archive.org/web/20030730143929/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1000&mode=1&msg=28193"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1000_mode_1_msg_28197", captured: "20030730144554", sha256: "b42b1a61fe9b778d4a017ac432a3ade6a0a8bef0076b027d4aa6cf95fe4e7a2a", wayback_url: "https://web.archive.org/web/20030730144554/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1000&mode=1&msg=28197"}
links:
  - {url: "http://againsttcpa.com/", status: "external", local: null}
  - {url: "http://aljo.topcities.com", status: "external", local: null}
  - {url: "http://alliance4.us/~Razor/images/tda.png", status: "external", local: null}
  - {url: "http://gamestudio43.mysticsoftware.net", status: "captured", local: "wayback/mysticsoftware.net/gamestudio43.mysticsoftware.net/index-92ba12"}
  - {url: "http://www.cywh.com", status: "external", local: null}
  - {url: "http://www.cywh.com/AgainstTCPA-Log01Banner.gif", status: "external", local: null}
  - {url: "http://www.cywh.com/images/logo.jpg", status: "external", local: null}
---

# Hmm... Someone might know this...

### jasond. · 2003-07-15 22:31 · #A1000-28180

Hmm... Someone might know this...
I'm writing a Visual Basic program and I'm wondering if there is a way to force the MouseMove event of one control to fire when another has the focus.
Let me be more specific:
Say you have a label control on a form. You click (but don't release) the form and drag the cursor across label control. Ordinainary, the MouseMove event on label will not fire. I need to figure out how to force it to fire.
BTW: This post isn't entirely off topic, the proggie I'm making could be of use to TK users.
Thanks.
- Jason D.
Pubilc Declare Function DoAllMyWorkForMe Lib "iamlazy.dll" (ByVal Time as Long, ByVal Quality As Long) as Executable
MSN: jason_detchevery@hotmail.com
Website: I'm far too lazy to make one of those....yet.....

### cy · 2003-07-15 23:07 · #A1000-28184

**it should....**

but heres a few things....
MouseDown = when you have the mouse clicked but havent released
MouseUp = when you have released it
MouseMove = when the mouse is moving over the object.
there's not reason for it not to work. its gota be doing something your doing wrong. what you can do is go to the mousemove thing and higlight the first line with that red circle thing and then run it and try it. If it activates it, its something your doing wrong. If it doesnt, there's something wrong.
I havent used vb in a while, but im prety sure. If not their could be a drag option, but if im not mistaken, its for draging an object (like icon) onto the object.
-Cy-

[![](http://www.cywh.com/AgainstTCPA-Log01Banner.gif)](http://againsttcpa.com/)
[![](http://www.cywh.com/images/logo.jpg)](http://www.cywh.com)

### jasond. · 2003-07-15 23:19 · #A1000-28187

**Lol.....(more)**

I know what the Form_Mouse events and breakpoints are, hehe.
But still, this is the only code I have:
Private Sub Label1_MouseMove(Button As Integer, Shift As Integer, X As Single, Y As Single)
Static Fired As Long
Fired = Fired + 1
Label1.Caption = Fired
End Sub
And setting a breakpoint does nothing, it doesn't halt the program. If the mouse is pressed down on the form, then dragged across the label and released, the MouseMove event on the label *does not* fire, no matter what. It's not just my computer either. It must because the label does not have the focus, but you can't give labels the focus.
It's strange, but not too important now as I think I've figured out a more efficient way to code what I was doing anyway.
And yeah, the DragOver and DragDrop events are only for doing OLE Automation and stuff I believe.
Thanks anyway,
- Jason D.
Pubilc Declare Function DoAllMyWorkForMe Lib "iamlazy.dll" (ByVal Time as Long, ByVal Quality As Long) as Executable
MSN: jason_detchevery@hotmail.com
Website: I'm far too lazy to make one of those....yet.....

### john@aljo · 2003-07-15 24:00 · #A1000-28193

**by chance...**

do ya got a good tutorial to recomend for VB? besides google and MSDN :p

**[John@AlJo](http://aljo.topcities.com)**

codebase='http://active.macromedia.com/flash4/cabs/swflash.cab#version=4,0,0,0'
id='mrgad' width='184' height='188'>
width='184' height='188'
type='application/x-shockwave-flash'
pluginspage='http://www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash'>
Get the banner script here.
<script src='http://aljo.topcities.com/banners/banner.js'></script>
Thanks to sophia for the Avatar. Here is a link to her site. <http://gamestudio43.mysticsoftware.net>

### thomas · 2003-07-15 24:50 · #A1000-28197

**Ah.. so you want to be able to braw lines in your icon editor..**

Umm.. I don't know how..

---
Coming Soon: TK Assistant

---

![](http://alliance4.us/~Razor/images/tda.png)
Coming Feb. 2004
