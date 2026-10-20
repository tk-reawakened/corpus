---
kind: doc
id: "toolkitzone.com/173"
site: "toolkitzone.com"
title: "CSurface"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=173"
written: "2005-01-30T18:58:00"
date_confidence: "exact"
updated: null
captured: ["20051212225332", "20060209183120", "20070302062259", "20070308231710"]
author: "Colin"
repliers: []
authors: ["Colin"]
comments_present: 0
f_author: "Colin"
f_date: "January 30, 2005, 6:58 pm"
f_description: "Creating fluid animated is something oft required in programming. Unlike its predecessor, TK3 provides you with relatively simple ways to accomplish one such technique \u0096 backbuffering."
f_title: "Backbuffering"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_173", captured: "20051212225332", sha256: "5672d53b3fd865032ab4580bd8c92ecd3d075b4a2219e07f654046301b3509d8", wayback_url: "https://web.archive.org/web/20051212225332/http://www.toolkitzone.com:80/library.php?mode=read&doc=173&PHPSESSID=6c1f0d3aa43a19d10f2020f481c20c7a"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_173", captured: "20060209183120", sha256: "2adc013d15b250bb11a750cf7794ce39cf4bc9dc910b048b3d6c21a1f0e99893", wayback_url: "https://web.archive.org/web/20060209183120/http://www.toolkitzone.com:80/library.php?mode=read&view=cadd&doc=173&PHPSESSID=6c1f0d3aa43a19d10f2020f481c20c7a"}
  - {path: "wayback/toolkitzone.com/library.php__doc_173", captured: "20070302062259", sha256: "175fdb576d3d1b313288d759f623dace9698f93ce60e13222b9dddf060c53903", wayback_url: "https://web.archive.org/web/20070302062259/http://www.toolkitzone.com/library.php?doc=173"}
  - {path: "wayback/toolkitzone.com/library.php__doc_173_highlight_", captured: "20070308231710", sha256: "eb16f99aadec7720b138d3d20cb23dca2def093de4d20a2d3f6d7394e441a449", wayback_url: "https://web.archive.org/web/20070308231710/http://www.toolkitzone.com:80/library.php?doc=173&highlight"}
---

# CSurface

TK3 Amelioration IX – Backbuffering
Creating fluid animated is something oft required in programming. Unlike its predecessor, TK3 provides you with relatively simple ways to accomplish one such technique – . When creating animation in RPGCode, one problem you’ll frequently notice is flicker. Restoring the screen then drawing again, for example, produces a slight “flash”. The solution to this is to only draw . **backbuffering** *once*
Backbuffering involves drawing all animation to an off-screen area then blitting that surface forward. This is often referred to as a . While this is simple in theory, it is comparatively difficult to implement. This week’s document will take you through the mechanics of a flipping chain and creating a reusable class. **flipping chain** **surface**
The challenge as one might say, is to move a foreground image (preferably with a transparent area) over a background without flickering. A flickery version of this can be coded as follows:
local(
local( rx!
local( ry!
getRes( rx!, ry!
i! = 0; i! < ry!; i!++
clear()
setImage( "mwin.jpg", 50, 50, 400, 100
setImageTransparent( "arrow.gif", i!, i!, 50, 20, 255, 255, 255
A problem described earlier, however, is present here; since three things are drawn to the screen, a flicker is present between each. In the RPGToolkit3, off-screen surface functionality is provided through . If we clear, then set the two images onto a canvas, followed by drawing the actual canvas, we can eliminate the flicker: **canvases**
local(
local( rx!
local( ry!
local( cnv!
getRes( rx!, ry!
cnv! = createCanvas( rx!, ry!
i! = 0; i! < ry!; i!++
clear( cnv!
setImage( "mwin.jpg", 50, 50, 400, 100, cnv!
setImageTransparent( "arrow.gif", i!, i!, 50, 20, 255, 255, 255, cnv!
drawCanvas( cnv!, 0, 0
killCanvas( cnv!
However, three problems remain with this code. It is not ; such a snippet must be coded for every animation sequence. Its speed, or lack thereof, is also appalling; the images are being drawn at every iteration when they only need to be drawn once. Finally, the system illustrated does not properly express the relationships of the surfaces. Conceptually speaking, the surfaces are having things drawn them, and then the (the visible area) is having a backbuffer it. Something along the lines of the following code is desirable: **reusable** *to* **primary surface** **flipped** *onto*
primary = CPrimary()
backbuffer! = primary->getAttachedSurface()
bkg = CImage( "mwin.jpg", 400, 100
arrow = CImage( "arrow.gif", 50, 20
i! = 0; i! < ry!; i!++
backbuffer->clear()
backbuffer->blt( bkg!, 50, 50
backbuffer->bltTransparent( arrow!, i!, i!, 255, 255, 255
primary->flip()
arrow->release()
bkg->release()
primary->release()
Of course, in actual application the primary surface and backbuffer would likely be created in a start program and not killed until closing (i.e. waiting for termination so trans3 can call the deconstructor). As , we will arrange the shown classes into a hierarchy: [previously discussed](http://toolkitzone.com/library.php?mode=read&doc=62)
- is the root of all surface objects. It harbors functionality for a generic surface whose functionality can, and will, be extended. **CSurface**
- , being a type of surface, represents the visible portion of the screen. A backbuffer surface is attached to it and can be flipped onto it, thus creating a flipping chain. **CPrimary**
- is a surface specialized for caching a single image which can be then be blitted onto any other surface. **CImage**
Before we code the above classes, let us formularize which methods they will contain. The generic surface needs to handle creating and destroying a canvas, as well as providing a blitter (and possibly several drawing functions). A primary surface has to have another surface within it (the backbuffer) which it will control. An image surface, being the simplest of all, will only have to load an image onto its canvas. We will code the following functions:
**CSurface**
method CSurface::CSurface()
method CSurface::CSurface( CSurface rhs!
method CSurface::CSurface( width!, height!
CSurface’s constructor creates a canvas of the specified width and height, a canvas, or creates one the size of the screen. [copies](http://toolkitzone.com/library.php?mode=read&doc=148)
method CSurface::operator=( CSurface rhs!
The assignment operator allows the surface to be logically set to another. That is, the right-hand-side will be physically copied to the surface.
method CSurface::blt( CSurface source!, x!, y!
The method blits another surface the surface at the coordinates specified. blt() *to*
method CSurface::bltTransparent( CSurface source!, x!, y!, r!, g!, b!
This method transparently blits a source surface the surface. That is, it does not copy pixels of the specified color. *to*
method CSurface::clear()
Calling this method clears the surface.
method CSurface::~CSurface()
The deconstructor frees the canvas it has created, thus preventing any memory leakage.
**CPrimary: CSurface**
method CPrimary::CPrimary()
method CPrimary::CPrimary( CPrimary rhs!
CPrimary’s constructor will seamlessly creates the backbuffer associated with the visible area.
method CPrimary::operator=( CPrimary rhs!
The assignment operator logically copies both the attached surface and the surface itself.
method CPrimary::getAttachedSurface()
The method obtains the internal backbuffer (of type CSurface) so you can use it as you would any other surface. The surface be released. getAttachedSurface() *should not*
method CPrimary::flip()
This method flips the backbuffer onto the primary surface, thus making it visible. When used properly, it is the key to flipping chains.
method CPrimary::~CPrimary()
The deconstructor will free the backbuffer associated with the surface, any pointers you might have to it will become invalid.
**CImage: CSurface**
method CImage::CImage( fileName$, width!, height!
This constructor loads an image of the specified width and height onto the surface.
Given our descriptions and prototypes above, the actual classes are easy to code. While I recommend you try to code it yourself, my version can be found (granted, it’s a little slow – but we’re working on that for 3.06). Backbuffering, while it may appear complicated at first, is a simple concept. Abstracting it to fit its conceptual layout further eases its use. Good luck setting up your own animations, and hopefully I’ll see you all next week! [here](http://toolkitzone.com/stuff/files/226/backbuffering.prg)
Levi
January 31, 2005, 2:17 am
Wow. The price one pays for flicker-less animation. I've only experienced something like this once. Except it was very different. QBasic. They had screen pages. You print to an invisible page and then print the results onto the viewable page. A lot less coding, still slow and not always reliable. But shorter. Also had to wait for the screen redraw, that was a pain. I could never remember the right wait code and had to find it all over again. Well enough ranting from me, good job. I like this one. Not to say I didn't like the others, I just happened to like this one as well.
Alex0Xander
January 31, 2005, 3:27 pm
=P I sense a problem with many of these articles. As you may know, many a member of this here community is either below the age of maturity, understanding, and vocabulary building, or just getting to it. SO if you guys could tone down the technical talk and fancy wording, I think it would be for the best. Certainly is not necessary, is it? Either way, top notch job. ;]
**Column**
Toolkit 3.x > TK3 Amelioration
Creating fluid animated is something oft required in programming. Unlike its predecessor, TK3 provides you with relatively simple ways to accomplish one such technique  backbuffering.
**Past Columns**
Feb 28, '05
Feb 13, '05
Feb 7, '05
Jan 16, '05
Jan 2, '05
Feb 28, '05
Feb 13, '05
Feb 7, '05
Jan 16, '05
Jan 2, '05
