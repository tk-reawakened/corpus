---
kind: doc
id: "toolkitzone.com/60"
site: "toolkitzone.com"
title: "column"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=60"
written: "2004-11-27T00:28:00"
date_confidence: "exact"
updated: null
captured: ["20041207034950", "20041216141802"]
author: "Asimir"
repliers: []
authors: ["Asimir"]
comments_present: 0
f_author: "Asimir"
f_date: "November 27, 2004, 12:28 am"
f_description: "The guest writer for the internetless Occasionally_Correct this week is Asimir, and here he outlines the basics of using methods to help add more robust features to your game such as custom message windows. Handy for all you beginners to intermediates."
f_title: "The Basics of Methods"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_60", captured: "20041207034950", sha256: "37a7497181d5c73ef3cd32c50173454f3a45334511f3f76799ae498432454700", wayback_url: "https://web.archive.org/web/20041207034950/http://www.toolkitzone.com/library.php?mode=read&doc=60"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_60", captured: "20041216141802", sha256: "f2146db052d284a743fea7561a4b644fd2e905b453b863636e53e0629f02a981", wayback_url: "https://web.archive.org/web/20041216141802/http://www.toolkitzone.com/library.php?mode=read&view=cadd&doc=60"}
---

# column

RPG Code > Tips & Tricks
The guest writer for the internetless Occasionally_Correct this week is Asimir, and here he outlines the basics of using methods to help add more robust features to your game such as custom message windows. Handy for all you beginners to intermediates.
Hello people and welcome to Occasionally_Correct's Tips & Tricks column. This is Asimir here, and I'm covering for OC this week as he currently has no online capabilities, and because Xavier offered me hugs, kisses and Boohbah related documents to do this. This weeks article will explain the basics of methods, and simultaneously teach you how to code a simple custom message window (mwin), which is something every TK game should have if my opinion is to be taken as fact. We won't be covering methods with return values though, as I have less than an hour until this has to be uploaded, so I don't really have time for that. Maybe OC will cover them sometime, or maybe not. I don't know as I'm not him. First, what is a method? I'm not actually asking you that, despite the question mark; I'm about to explain it. A method, put simply, is a piece of code which you can call with your own custom rpgcode command. Here's an example where you might need it, involving the aforementioned custom mwin. If you didn't like the default message window and wanted to make your own one, you could go about it something like this: (Please note that #s are used for compatibility with TK2. In TK3 the #s are not necessary) Use for this code, otherwise the last statement in the code will be incorrect. It's obviously slow and tedious to write out so many lines of code for something which you'll be doing a lot in the game. You can simplify it using a method. The syntax of the method is as follows: methodname should be replaced with the name you want your method to have, code should be replaced with the code you want the method to run, and parameters will be explained soon. You could write a method like this and save it as mwin.prg: Then the above piece of code could be shortened to this: Whenever trans3 (or trans2) reads #cmwin() in your code, it would recognise it as your method, and run your method. But it needs to know that your method exists before it can recognise it. That's what #include("mwin.prg") is for. As that program contains the #cmwin() method, trans3 (or 2) needs to read that file before it knows about the method. This code is far from optimal though. It can be still vastly improved using parameters in your method. Parameters are variables passed into the method. They allow the method to do something different when you call it with different parameters. Just like the way that #colorrgb(0,0,0) doesn't do exactly the same thing as #colorrgb(255,255,255) To make your method use parameters, you need to include the parameters in the method declaration. If our method was this: then every time the method is called, it would need one parameter, eg. #cmwin("Hello"). In this example, when the method is called, text$ would become "Hello". At the moment the method isn't doing anything with the variable though. In this method, we would want to use parameters for the text to be displayed in the message window. At font size 20, this window could fit 6 lines of text, so we will use 6 parameters. The variables set as parameters will then be used inside the method. Now the code can be greatly shortened to this: Notice that blank lines had empty strings sent to them ("") so that no text was put on that line. And I'll be finishing this article now, as I've covered the very basics of methods, shown you all you need to make a basic message window, and this article needs to be submitted quite literally now. Thanks for reading, and check back next week when OC should have his own contribution to his column. Bye now.
Tips & Tricks
*[Editor - Now, now...don't get R jealous again]*
```
#colorrgb(255,255,255)
#fontsize(20)
#setimage("mwin.gif", 0, 0, 600, 150)
#text(2, 2, "Hello")
#text(2, 3, "This is my custom message window")
#wait
#setimage("mwin.gif", 0, 0, 600, 150)
#text(2, 2, "This message window is lovely")
#text(2, 3, "It was made by Pezzer")
#wait
```
[these nifty graphics](http://www.toolkitzone.com/stuff/files/310/mwin.gif)
```
#Method methodname(parameters)
{
code
}
```
```
#method cmwin()
{
#colorrgb(255,255,255)
#fontsize(20)
#setimage("mwin.gif", 0, 0, 600, 150)
}
```
```
#include("mwin.prg")
#cmwin()
#text(2, 2, "Hello")
#text(2, 3, "This is my custom message window")
#wait
#cmwin()
#text(2, 2, "This message window is lovely")
#text(2, 3, "It was made by Pezzer")
#wait
```
```
#method cmwin(text$)
{
#colorrgb(255,255,255)
#fontsize(20)
#setimage("mwin.gif", 0, 0, 600, 150)
}
```
```
#method cmwin(text1$, text2$, text3$, text4$, text5$, text6$)
{
#colorrgb(255,255,255)
#fontsize(20)
#setimage("mwin.gif", 0, 0, 600, 150)
#text(2, 2, text1$)
#text(2, 3, text2$)
#text(2, 4, text3$)
#text(2, 5, text4$)
#text(2, 6, text5$)
#text(2, 7, text6$)
#wait
}
```
```
#include("mwin.prg")
#cmwin("Hello", "This is my custom message window", "", "", "", "")
#cmwin("This message window is lovely", "It was made by Pezzer", "", "", "", "")
```
R043482
November 27, 2004, 12:34 am
Excellent Work! Informative and Insightful! :P
the_slasher07
November 27, 2004, 12:51 am
Wow. Covers everything perfectly.
Colin
November 27, 2004, 2:00 am
Those who read my article might also note that methods allow further abstration of processes. :)
sivart
November 27, 2004, 4:37 pm
Awsome! Really good job with this , will there be a way for people to go back and read these?
Xavier
November 27, 2004, 5:26 pm
They are all in the library.
Tom Elliott
December 4, 2004, 8:07 pm
Thanks Asimir, great column, really made sense of something that had previously been confusing me, I'd love to see more of these columns on a regular basis.
**others in series**
Dec 3, '04
