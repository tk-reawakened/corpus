---
kind: forum-thread
id: "toolkitzone-forums/17438"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "17438"
title: "Java for thought anyone? :P Assist if you can..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=17438"
written: "2005-04-06T02:19:00"
last_post: "2005-04-06T05:59:00"
date_confidence: "exact"
captured: ["20050408043909"]
author: "Ross L."
repliers: ["khin"]
authors: ["Ross L.", "khin"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_190977_amp_", captured: "20050408043909", sha256: "a5097078b67d8a7dbf8e59b96e754e69703887f8066e62760597253b8cb6111d", wayback_url: "https://web.archive.org/web/20050408043909/http://www.toolkitzone.com/forums/viewtopic.php?p=190977&amp="}
links: []
---

# Java for thought anyone? :P Assist if you can...

### Ross L. · 2005-04-06 02:19 · #B190977

I am trying to make a simple application in Java and I am getting some object expected errors when I go to compile it. Here is my code:

**Code:**

```
/**

 * @(#)Bounce.java

 *

 * Sample Applet application

 *

 * @Ross B. Leland

 * @version 1.00 03/15/05

 */

import java.awt.*;

import java.applet.*;

public class Bounce extends Applet implements Runnable{

   private Thread   ticker;

   private boolean   running = false;

   public void run() {

      while (running){

         repaint();

         try {

            ticker.sleep(1000/15);

         }   catch (InterruptedException e) {}

      }

   }

   public synchronized void start () {

      if (ticker == null   ||   !ticker.isAlive()) ;

         running = true;

         ticker = new Thread(this);

         ticker.setpriority(Thread.MIN_PRIORITY + 1);

         ticker.start();

      }

   }

   public synchronized void stop () {

      running = false;

   }

   private Rectangle   bounds;

   private Ball      ball;

   private int         width, height;

   public void init() {

      width = width = size().Width;

      height = size().height;

   bounds = new Rectangle(width, height);

      // Initialize Ball position and velocity

      ball = new Ball(width / 3f, height /4f, 1.5f

                  2.3f, 12, Color.blue);

   }

   public void paint (Graphics g) {

      if (offscr == null) {

         offscreenImage = createImage(width, height);

         offscr = offscreenImage.getGraphics();

      }

      // Draw checkerboard background

      int x2 = width >> 1;

      int y2 = height >> 1;

      offscr.setColor(Color.gray);

      offscr.fillRect(0, 0, x2, y2);

      offscr.fillRect(x2, y2, width - x2, height -y2);

      offscr.setColor(Color.white);

      offscr.fillRect(x2, 0, width - x2, height - y2

      offscr.fillRect(0, y2, x2, y2);

      ball.move(bounds);

      ball.drew(offscr);

      g.drawImage(offscreenImage, 0 0, null);

   }

}
```

Please help if you can! Thanks!
BTW I get errors on lines 35, 40, 41, 43, and twice on 70.

### khin · 2005-04-06 04:55 · #B191052

From what I see, there's no definition for the Ball class.
Also, the objects offscreenImage and offscr are not declared..or maybe i just couldn't see them...
Here's a bouncing ball program from me. It's not as high-level as the one you have, mainly because i tried keeping it as basic as possible(least use of objects)...

**Code:**

```
import java.awt.*;

import java.applet.*;

class Ball{

   public static final int    DIR_EAST = 0,

                        DIR_WEST = 1,

                        DIR_NORTH = 2,

                        DIR_SOUTH = 3; //--direction constants

   private int speed; //--ball's linear velocity

   private Point direction; //--direction 0 = eastward/southward, 1 = westward/northward

   private Color color; //--color

   private int diam; //--ball's diameter

   private Point loc; //--ball's location

   public Ball(){}

   public Ball(Color c, int spd, Point dir, Point loca, int d){

      color = c;

      loc = loca;

      direction = dir;

      speed = spd;

      diam = d;

   }

   /* Make the ball move based on a given boundary*/

   public void move(Rectangle bounds){

      /*change the location based on the direction*/

      if(direction.x == DIR_EAST) loc.x += speed;

      else if(direction.x == DIR_WEST) loc.x -= speed;

      if(direction.y == DIR_NORTH) loc.y -= speed;

      else if(direction.y == DIR_SOUTH) loc.y += speed;

      /*check to see if the boundary has been reached*/

      if(loc.x + diam >= bounds.width || loc.x <= bounds.x)direction.x = 1 - direction.x; //reverse horizontal direction

      if(loc.y + diam >= bounds.height || loc.y <= bounds.y)direction.y = (1 - direction.y) + 4; //reverse vertical direction

   }

   /* Draw the ball on the specifies graphics object*/

   public void draw(Graphics off){

      off.setColor(color);

      off.fillOval(loc.x, loc.y, diam, diam);

   }

}

public class Bounce extends Applet implements Runnable{

   Rectangle bounds;

   Ball myBall;

   Thread runner;

   Image offImage;

   Graphics off;

   public void start(){

      if(runner == null){

         runner = new Thread(this);

         runner.start();

      }

   }

   public void stop(){

      if(runner != null){

         runner.stop();

         runner = null;

      }

   }

   public void run(){

      while(true){

         myBall.move(bounds);

         repaint();

         try{

            Thread.sleep(10);

         }catch(Exception e){}

      }

   }

   public void update(Graphics g){

      paint(g);

   }

   public void init(){

      myBall = new Ball(Color.RED, 5, new Point(Ball.DIR_EAST, Ball.DIR_SOUTH), new Point(20, 20), 20);

      bounds = new Rectangle(0, 0, size().width, size().height);

      offImage = createImage(size().width, size().height);

      off = offImage.getGraphics();

   }

   public void paint(Graphics g){

      off.setColor(new Color(20, 200, 200));

      off.fillRect(0, 0, size().width, size().height);

      off.setFont(new Font("Comic Sans", Font.BOLD, 15));

      off.setColor(new Color(255, 0, 0));

      off.drawString("Bouncing Ball", 10, 30 );

      myBall.draw(off);

      g.drawImage(offImage, 0, 0, this);

   }

}
```

### Ross L. · 2005-04-06 05:12 · #B191056

Thanks! When I went to compile it, worked fine. It gave me an error when I went to execute it though. "Exception in thread "main" java.lang.NoSuchError: main" Any ideas?

### khin · 2005-04-06 05:46 · #B191068

That's an applet. Applets need a web browser to be run.
So in short you gotta make a wenpage first then attach the applet there. Here's an example:

**Code:**

```
<HTML>

<HEAD>

</HEAD>

<BODY BGCOLOR="000000">

<CENTER>

<APPLET

   code   = "Bounce.class"

   width   = "500"

   height   = "300"

   >

</APPLET>

</CENTER>

</BODY>

</HTML>
```

It might not work with WinXP though...coz' it rejects the <applet> tag. You may want to use the <embed> or <object> tags...

### Ross L. · 2005-04-06 05:59 · #B191071

YAY!! You fixed it!! *bear hug* Ok now on to the next few items. I should probably work on GUI design soon...
