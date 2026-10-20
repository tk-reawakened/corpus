---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/tutorials/coding/understanding-canvases/"
site: "rpgtoolkit.net"
title: "January 8th, 2005"
original_url: "http://rpgtoolkit.net/tutorials/coding/understanding-canvases/"
written: "2005-01-08"
date_confidence: "day"
updated: null
captured: ["20140613220533"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/tutorials/coding/understanding-canvases/index", captured: "20140613220533", sha256: "184c6267fadff6bbcf25b8b8030ed871f8dc63832f6fbe53a4e1aa36e0006626", wayback_url: "https://web.archive.org/web/20140613220533/http://rpgtoolkit.net/tutorials/coding/understanding-canvases/"}
---

# January 8th, 2005

Soapdish / Lotusware & k-hos
[![Occasionally_Correct](thumb/80/community/images/avatars/upload/94_1395111535.png)](member/occasionally-correct/)
Published
**January 8th, 2005**
Read times **957**
Written by Occasionally_Correct
Understanding Canvases
**One of the more robust additions to the Toolkit in recent times has been the canvas functionality, but a lot of users are still unaware of it's capabilities. This week OC guides you the basic code to get you started.**
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
