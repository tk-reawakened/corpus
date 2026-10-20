---
kind: doc
id: "toolkitzone.com/170"
site: "toolkitzone.com"
title: "Introduction"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=170"
written: "2005-01-29T10:44:00"
date_confidence: "exact"
updated: null
captured: ["20051226062032"]
author: "Occasionally_Correct"
repliers: []
authors: ["Occasionally_Correct"]
comments_present: 0
f_author: "Occasionally_Correct"
f_date: "January 29, 2005, 10:44 am"
f_description: "OC brings together two of the new RPG Code concepts, classes and canvases, to illustrate how such a combination can be used to bring more power, ease and organisation to using canvases."
f_title: "Canvases and Classes"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_170", captured: "20051226062032", sha256: "d4dd3f9e4917cd79d0a9a5fd32b2aa0d761b24ae528867daf847d9604753297f", wayback_url: "https://web.archive.org/web/20051226062032/http://www.toolkitzone.com:80/library.php?mode=read&doc=170&PHPSESSID=3a8877fdee63b0dcd9b5eb3ae54264d2"}
---

# Introduction

Hi there. OC here, continuing the topic of canvases. More so the topic of object oriented programming. What do the two have in common? To the normal TK user; nothing. To me; a canvas class. That's what we'll be making today: A class that handles canvases for us. Canvas classes are ideal for people who use a lot of canvases, since they allow for ease of use and organization. Canvas classes also make it easier to do other tasks like resizing the canvas. Now, let's take a look at what all this does. Firstly, we make the constructor. This takes two parameters: width! and height!, for specifying the width and height of the canvas. In the constructor, it sets the specified width and height to the m_width! and m_height! member variables. Then, it creates the canvas and stores it's handle in m_cnv!. Next, the copy constructor. If you don't know what a copy constructor is, please refer to . All we're doing here is copying over the member variables from the rhs ("Right Hand Side"), and creating a new canvas. After that's done, we copy the contents of the old canvas into the new one. Next, the destructor, which kills the canvas via the killCanvas() command. Then the overloaded assignment operator. This implementation of the assignment operator does practically the same thing as the copy constructor, except it's used for different reasons. The last two methods in the class emulate the bitmap() and drawCanvas() commands. More can be added if you'd like to use the various other drawing commands, of course. Now that you know how the class works (or assuming you do, anyway), let's move on to an example of how to put the class to work (assuming that the class is in a file called 'CCanvas.prg'). In this example, a few things are happening. First, you include the CCanvas.prg file, then make two instances of the CCanvas class. Each is sized to 100 (width) by 100 (height). Then, 'mwin.jpg' (which comes with the toolkit) is drawn to the canvas, and is then drawn to the screen at 1,1 (x,y). This is the fun part. cnv1 is assigned to cnv2, which calls the copy constructor, copying over the width/height of cnv1 and copies whats in the canvas. cnv2 is then drawn to the screen at 150,200 (x,y). Finally, both objects are killed off with the release() method. That's it for today. I hope you've learned from and enjoyed this article, however short it may be. There are plenty of other things you could add to this basic example of a canvas class (i.e.: the rest of the drawing commands, or the ability to resize the canvas). Comments, questions, or suggestions? I'm open to all input. **Canvases and classes**
**Introduction**
**The Class**
```
class CCanvas
{
public: method CCanvas {
m_width! = width!
m_height! = height!
m_cnv! = createCanvas } method CCanvas {
m_width! = rhs->m_width!
m_height! = rhs->m_height!
m_cnv! = createCanvas drawCanvas } method ~CCanvas {
killCanvas } method operator= {
if {
m_width! = rhs->m_width!
m_height! = rhs->m_height!
m_cnv! = createCanvas drawCanvas }
} method drawBitmap {
bitmap } method draw {
drawCanvas }
private:
m_cnv!
m_width!
m_height!
} //----------------------------------------
// CCanvas class
// Constructors/destructor
// Constructor (width!, height!) (m_width!, m_height!) // Copy Constructor (CCanvas rhs!) (m_width!, m_height!) (rhs->m_cnv!, 0, 0, m_width!, m_height!, m_cnv!) // Destructor (m_cnv!) //--------------------------------
// Overloaded operators
// Assignment operator (CCanvas rhs) (this! ~= rhs!) (m_width!, m_height!) (rhs->m_cnv!, 0, 0, m_width!, m_height!, m_cnv!) //--------------------------------
// Methods
// Draw a bitmap to the canvas (file$) (file$, m_cnv!) // Draw the canvas (x!, y!) (m_cnv!, x!, y!)
```
**Examples, examples**
```
#include cnv1 = CCanvas cnv2 = CCanvas cnv1->drawBitmap cnv1->draw cnv2 = cnv1 cnv2->draw cnv1->release cnv2->release // Include the necessary file "CCanvas.prg" // Create two instances of CCanvas (100, 100) (100, 100) // Draw to the canvas, then draw the canvas itself ("mwin.jpg") (1, 1) // Copy the first canvas over to the second // Draw the second canvas to a different area (150, 200)
```
**Conclusion**
Colin
January 29, 2005, 11:29 am
Assignment operator will leak memory -- it has to destroy the canvas first.
**Column**
RPG Code > Tips & Tricks
OC brings together two of the new RPG Code concepts, classes and canvases, to illustrate how such a combination can be used to bring more power, ease and organisation to using canvases.
**Past Columns**
Feb 18, '05
Feb 11, '05
Jan 15, '05
Jan 8, '05
Dec 31, '04
Feb 18, '05
Feb 11, '05
Jan 15, '05
Jan 8, '05
Dec 31, '04
