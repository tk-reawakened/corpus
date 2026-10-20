---
kind: doc
id: "toolkitzone.com/138"
site: "toolkitzone.com"
title: "Introduction"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=138"
written: "2005-01-08T07:13:00"
date_confidence: "exact"
updated: null
captured: ["20060405014104"]
author: "Occasionally_Correct"
repliers: []
authors: ["Occasionally_Correct"]
comments_present: 0
f_author: "Occasionally_Correct"
f_date: "January 8, 2005, 7:13 am"
f_description: "One of the more robust additions to the Toolkit in recent times has been the canvas functionality, but a lot of users are still unaware of it's capabilities. This week OC guides you the basic code to get you started."
f_title: "Understanding Canvases"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_138", captured: "20060405014104", sha256: "5ef84fad594113632e8fc20cc11e8b27689f99595f7f5d974e32496e5d210559", wayback_url: "https://web.archive.org/web/20060405014104/http://www.toolkitzone.com/library.php?mode=read&doc=138"}
---

# Introduction

Hi there. OC here, and today we'll be talking about canvases. Canvases are very useful things, especially if you want to go graphic-heavy in your games. They allow you to load images, text, shapes, and anything else that has to do with drawing into a canvas before displaying it on the screen. In their most basic form, they can act as a 'preloader' for graphics. Of course, that isn't all they can do. For example, you can constantly render things to the screen. You'll learn how to do that later. First, the basics... Consider the preceding code. All this does is creates a canvas, sets an image into the canvas, and then draws it to the screen. Not a very useful example, but it lets us learn a few things. First, we use the createCanvas() command to create a canvas. It's parameters specify the width and height of the canvas (640 by 480, respectively). It returns an ID (or 'handle') to hCnv!. This handle can be used to refer to the canvas you've just created. Next, we use the bitmap() command. It takes an extra parameter (the handle of a canvas) so you can draw it to a canvas. In this case, we use hCnv!, so it will draw the image to the canvas we just created. Finally, we draw the canvas to the screen with drawCanvas(). The first parameter, as you might expect, is the handle of the canvas to draw. The second and third are the x and y coordinates (in pixels) on the screen to draw to. You can also draw multiple things to a canvas at once. So, let's draw some text on the canvas, along with the graphics; This draws the image, "title.jpg" and some text to the canvas. Note that the image, or text, will not appear on the screen until you use the drawCanvas() command. This is an advantage over drawing images and text directly onto the screen, because that causes small delays between the image and each line of text being drawn. When drawing to a canvas, everything is loaded into the canvas, so it's all drawn simultaneously. Alright. Now that we've used our canvas, we'll get rid of it, since canvases take up memory. A simple task. All we do is use the killCanvas() command, using the canvases handle as the parameter, and then kill the variable used to store the handle. When you start a game, a canvas is automatically created for you. The handle to this canvas is stored in the cnvRenderNow! variable, and you can use that just as you used the hCnv! variable. The cnvRenderNow canvas is rather handy, however, since you can constantly rander it to the screen. When I say 'constantly render,' I mean that you're able to constantly draw the canvas, allowing you to create real-time life bars that stay on the screen, clocks, timers, anything that needs to constantly be redrawn or updated. How is this done? Well, all you have to do is draw the contents to the canvas, and then use the renderNow() command. It's worth noting that you never have to create or kill off this canvas. However, I'll show you how to clear it later. Take a look at the following code: The first line (renderNow("on")) turns on the rendering for the cnvRenderNow! canvas. It will now be constantly rendered to the screen. Next, we create an infinite loop (something you don't want to do unless you're threading this program). Inside the loop, we use the multiRun() command. The multiRun() command executes all commands within it's opening and closing braces before handing control to another thread, or the player. This is a simple example of how to create an in-game clock. If you want to clear this canvas, you'll need to use the clear() command. The clear() command can take a parameter - the handle of the canvas to clear. Like so: This, of course, is only the tip of the ice berg. Wherever you can use graphical interfaces, graphical real-time programs, or anything else that has to do with graphics or drawing, you can use canvases. I hope that this article as bettered your understanding and knowledge of canvases, and given you an idea or two. As always, if you have any comments or questions, you're welcome to PM me or post them here. **Understanding Canvases**
**Introduction**
**Creating a Canvas**
```
hCnv! = createCanvas(640, 480)
bitmap("title.jpg", hCnv!)
drawCanvas(hCnv!, 0, 0)
```
```
hCnv! = createCanvas(640, 480)
bitmap("title.jpg", hCnv!)
text(2, 4, "This is text!", hCnv!)
text(2, 5, "More text!", hCnv!)
drawCanvas(hCnv!, 0, 0)
```
```
killCanvas(hCnv!)
kill(hCnv!)
```
**The cnvRenderNow canvas**
```
renderNow("on")
while(0 == 0)
{
multiRun()
{
pixelText(10, 10, "The time is now:", cnvRenderNow!)
pixelText(10, 30, castLit(gameTime!), cnvRenderNow!)
}
}
```
```
//Create a canvas
hCnv! = createCanvas(100, 100)
text(2, 2, "Hello!", hCnv!)
drawCanvas(hCnv!, 0, 0)
//Now, clear the canvas
clear(hCnv!)
//Try drawing again - there's nothing in it!
drawCanvas(hCnv!, 0, 0)
//Kill off the canvas
killCanvas(hCnv!)
kill(hCnv!)
```
**Conclusion**
Marz
January 8, 2005, 1:00 pm
Nice tutorial. Now the masses finally know the "basics" of canvasses. Can we expect a follow-up tutorial?
Horizon
January 8, 2005, 1:22 pm
Sweet. I was wondering what the cnvrendernow! thing was :)
Occasionally_Correct
January 8, 2005, 1:37 pm
A follow up? Ooh, I smell canvas classes. :P Thanks for the comments!
Slasher
January 8, 2005, 6:47 pm
...Nice, indeed. I didn't even know it was on there -_-
Juggernaut
March 6, 2005, 3:37 pm
Now understanding canvases, I can get around all my battle system problems. Thanks!
**Column**
RPG Code > Tips & Tricks
One of the more robust additions to the Toolkit in recent times has been the canvas functionality, but a lot of users are still unaware of it's capabilities. This week OC guides you the basic code to get you started.
**Past Columns**
Feb 18, '05
Feb 11, '05
Jan 29, '05
Jan 15, '05
Dec 31, '04
Feb 18, '05
Feb 11, '05
Jan 29, '05
Jan 15, '05
Dec 31, '04
