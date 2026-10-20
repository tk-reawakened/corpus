---
kind: forum-thread
id: "toolkitzone-forum/44316"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "44316"
title: "A Common Problem Without The Common Solution"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=44316"
written: "2009-12-27T09:00:00"
last_post: "2010-01-01T20:51:00"
date_confidence: "exact"
captured: ["20100101204959", "20100101205117", "20100101205146", "20100101205220", "20100101205316", "20100101205327", "20100101205338"]
author: "rpg gamer 17"
repliers: ["cuthalion", "armaniac", "Prism", "Dylan RPG", "Euix", "Grindalf"]
authors: ["rpg gamer 17", "cuthalion", "armaniac", "Prism", "Dylan RPG", "Euix", "Grindalf"]
posts_present: 15
pages_present: [1, 2]
pages_total: 2
posts_per_page: 10
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_487618", captured: "20100101204959", sha256: "fbe227ee4b7f3421fd428f317075adc46aac94766133590df2c0ad19c5a28823", wayback_url: "https://web.archive.org/web/20100101204959/http://toolkitzone.com/forum/viewtopic.php?p=487618"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_487631", captured: "20100101205338", sha256: "383f992a2f5fe689dd517c89a1be0814758c77f2506045509d584d383ea2e935", wayback_url: "https://web.archive.org/web/20100101205338/http://toolkitzone.com/forum/viewtopic.php?p=487631"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_487640", captured: "20100101205220", sha256: "5dec9330b084030a6546e1f1420fc8303231e815b962c95d3704afe9452f5d8c", wayback_url: "https://web.archive.org/web/20100101205220/http://toolkitzone.com/forum/viewtopic.php?p=487640"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_44316", captured: "20100101205146", sha256: "13a17628bc3195d7728772014e731d8758c8b91633eadafb12aa68f61405132b", wayback_url: "https://web.archive.org/web/20100101205146/http://toolkitzone.com/forum/viewtopic.php?t=44316"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_44316_start_0", captured: "20100101205316", sha256: "c435f7884a409e1ee511f395b4c906f5937edde8ae131e64463e405be2138a6b", wayback_url: "https://web.archive.org/web/20100101205316/http://toolkitzone.com/forum/viewtopic.php?t=44316&start=0"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_44316_start_10", captured: "20100101205117", sha256: "e55c1bad7024a89d0b098e056b2230d54544166149c1073462da8c670546e38e", wayback_url: "https://web.archive.org/web/20100101205117/http://toolkitzone.com/forum/viewtopic.php?t=44316&start=10"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_44343", captured: "20100101205327", sha256: "b6cccae09c7ea32d2b0e27d57ab6855acb4bf132d4ab1457dc4ae38a1cdea0ce", wayback_url: "https://web.archive.org/web/20100101205327/http://toolkitzone.com/forum/viewtopic.php?t=44343"}
links:
  - {url: "http://codebible.toolkitzone.com/index.php?title=Category:Canvases", status: "captured", local: "wayback/toolkitzone.com/codebible.toolkitzone.com/index.php__title_Category_3ACanvases"}
  - {url: "http://codebible.toolkitzone.com/index.php?title=Get", status: "never-captured", local: null}
  - {url: "http://tk3.toolkitzone.com/help/?page=19", status: "captured", local: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_19"}
  - {url: "http://tk3.toolkitzone.com/help/?page=19#itempath", status: "captured", local: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_19"}
  - {url: "http://tk3.toolkitzone.com/help/?page=19#playerpath", status: "captured", local: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_19"}
  - {url: "http://tk3.toolkitzone.com/help/?page=19#setimageadditive", status: "captured", local: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_19"}
---

# A Common Problem Without The Common Solution

### rpg gamer 17 · 2009-12-30 05:08 · #K487600

**Sizing and resizing a canvas. UPDATED**

I've have a really old message window that I am going to spend tomorrow rewriting.
It is a type writer message window that uses symbols to indicate pauses and line breaks. It isn't attached to a canvas and uses savescreen and restorescreen in order to remove it from the screen. There is a option menu that I might have trouble with editing as well. I have not programmed in RPG Code in quite a while but I have been using C++ for the past some odd months.
I don't know how to explain what I'm doing because I don't really know my self.
Here is the program:

**Code:**

```
/*

NOTE:

//<-- means the comment was added recently.

*/

function cmwin(speaker, text)

{

   savescreen(Mwin); //save the screen

   RenderNow(true);

   fontsize(20);

   font("Times New Roman");

   getres(width, height);

   setimagetransparent("mwin.jpg", width/4-5, height/4-20, width/4+5, 25, 255, 0, 0);

   setimagetransparent("mwin.jpg", width/4-5, height/4, width/2+5, 120, 255, 0, 0);

   x = 1;

   y = 0;

   displaytext = "";

   extrawidth = 0;

   speed = ".02"; //<-- use to have a 'type faster key' that edited the string. I made it a string?

   pixeltext(width/4, height/4-20, speaker);

   delay(.5);

   until(x >= len(text)+1) //... What?

   {

      character = charAt(text, x);

      if(character == "|") //advance to next row //<-- OMG!! this was commented!

      {

         y++;

         character = "";

         extrawidth = 0;

      }

      elseif(character == "#") //pause for a few seconds //<-- this one was too! :D

      {

         delay(castnum("0."+charAt(text, x+1)));

         character = "";

         x++;

      }

      if(extrawidth+gettextwidth(charAt(text, x+1)) >= width/2-10) //<-- I D K??

      {

         y++;

         extrawidth = 0;

      }

      if(y > 4) //<-- Refresh if over 4?

      {

         setimagetransparent("continue arrow.png", width/4-15+width/2, height/4+110, 15, 10, 255, 0, 0);

         wait();

         setimage("mwin.jpg", width/4-5, height/4, width/2+5, 120);

         y = 0;

         extrawidth = 0;

         speed = ".02";

      }

      displaytext += character;

      pixeltext(width/4+5+extrawidth, 120+5+20*y, character);

      extrawidth += gettextwidth(character);

      delay(castnum(speed)); //<-- delay for next letter

      x++;

   }

   setimagetransparent("continue arrow.png", width/4-15+width/2, height/4+110, 15, 10, 255, 0, 0);

}

function cmwincls() //<-- pause for clicks or presses and restore the screen

{

   ClearBuffer();

   while(keypress == "" || mousex == 0 && mousey == 0)

   {

      Mouseclick(mousex,mousey,true);

      keypress = get();

   }

   ClearBuffer();

   restorescreenarray(Mwin);

}

function options(options, &selected)

{

   savescreen(commandmenu);

   fontsize(20);

   font("Times New Roman");

   getres(width, height);

   number = 0;

   num = 0;

   cnum = 0;

   total = 0;

   width = 0;

   oldwidth = 0;

   selecting = 0;

   opwidth = width;

   split(options, "|", Option[]); //<-- '|' means new line

   loop = 1;

   while(loop == 1) //<-- I love this while loop! LMAO

   {

      if(Option[total] ~= "") //<-- I wonder how it ends?

      {

         width = gettextwidth(Option[total]);

         if(width > oldwidth)

         {

            opwidth = width;

            oldwidth = width;

         }

         else

         {

            //oldwidth stays the same value //<-- then why is this here?

         }

         total++;

      }

      else

      {

         loop = 0; //<-- Your kidding right?

      }

   }

   key = "";

   selected = cnum;

   while(key ~= "ENTER" && key ~= " ")

   {

      setimage("mwin.jpg", width/2+opwidth/2, height/4+125, opwidth+35, 20*total+5);

      for(num = 0; num < total; num++)

      {

         pixeltext(width/2+opwidth/2+30, height/4+125+20*num, Option[num]);

      }

      setimagetransparent("arrow continue.png", width/2+opwidth/2+2, height/4+130+20*cnum, 15, 10, 255, 0, 0);

      key = get();

      if(key == "UP")

      {

         cnum--;

         if(cnum < 0)

         {

            cnum = total-1;

         }

      }

      if(key == "DOWN")

      {

         cnum++;

         if(cnum >= total)

         {

            cnum = 0;

         }

      }

      selected = cnum;

   }

   restorescreenarray(commandmenu);

}
```

I edited it a little. I tried to leave it in it's original state.
How would I get the total height and width of the canvas? I think, in the code above, I'm taking a 4th of the height and width of the screen off the image and leaving it at that. I want to resize the canvas depending on how many lines the message window holds. The canvas will be drawn to another canvas and moved up and down to imitate 'scrolling'.
I have a feature that I am going to need help with implementing. I want to be able to 'click past' the type writer. I want to press ESC during the type writing and the rest of the text to show up.

### cuthalion · 2009-12-30 21:45 · #K487620

**Sizing and resizing a canvas. UPDATED**

For the "click past" thing, just type the text using a while loop that checks both whether the text is finished typing and whether the ESC key has been pressed. I believe [get](http://codebible.toolkitzone.com/index.php?title=Get) is the function you'll need. When the loop is finished, check if the text was finished. If it wasn't, finish it all in one go.
I don't know of any way to get a canvas's size (other than recording it in a variable when you first create the canvas) or to resize a canvas (though you can draw a canvas at a different size, stretching or shrinking it). Here are the [canvas commands](http://codebible.toolkitzone.com/index.php?title=Category:Canvases) in the standard release. I think there is a plugin that adds more commands, possibly including what you're looking for.
For scrolling using that method, you'll be erasing the canvas, then redrawing it in another location.

### rpg gamer 17 · 2009-12-31 03:12 · #K487631

**Sizing and resizing a canvas. UPDATED**

I have been having a little mental problem. I can't think and I have a headache that hits hard every now and then. Anyways, I am going to spend today taking medications and tomorrow if the pain resides. I'll begin the operation.
About the width and height of the canvas:
EDIT: I figured out a way. It's not efficient but it will do.
About the scrolling.
There are going to be two canvases.
One will be the background of the canvas
One will be the message.
The background will be drawn over with an image
The message window will be drawn transparently to the background using an offset position.
EDIT:
I spent all night working on this thing.
Here is the method and a test code.
It uses the keydown function.

**Code:**

```
autolocal(true);

RenderNow(true);

//New Message window

Global(cmwinLine); //current line of the message window

Global(cmwincnvX); //Info on the BGK canvas

Global(cmwincnvY);

Global(cmwincnvWidth);

Global(cmwincnvHeight);

Global(cmwincnvBGK);

Global(cmwincnvBGKImage)

Global(cmwincnvTx); //info on the text canvas

Global(cmwincnvTy);

Global(cmwincnvTwidth);

Global(cmwincnvTheight);

Global(cmwincnvTEXT);

function CMwinBKG(Image,x,y,width,height) //set the BKG canvas

{

   cmwincnvX = x;

   cmwincnvY = y;

   cmwincnvWidth = width;

   cmwincnvHeight = height;

   cmwincnvBGK = createcanvas(width, height);

   cmwincnvBGKImage = Image;

}

function CMwinResetBKG() //update the BKG canvas

{

   GetFontSize(ftSize);

   GetRes(scnWidth, scnHeight);

   if(cmwincnvX == 0) { cmwincnvX = scnWidth/6; }

   if(cmwincnvY == 0) { cmwincnvY = ftSize; }

   if(cmwincnvWidth == 0) { cmwincnvWidth = scnWidth-scnWidth/3; }

   if(cmwincnvHeight == 0) { cmwincnvHeight = cmwincnvTheight+40; }

   if(!(cmwincnvBGK == 0)) { KillCanvas(cmwincnvBGK); }

   if(cmwincnvBGKImage == "") { cmwincnvBGKImage = "mwin.jpg"; }

   cmwincnvBGK = createcanvas(cmwincnvWidth, cmwincnvHeight);

   setImage(cmwincnvBGKImage, 0, 0, cmwincnvWidth, cmwincnvHeight, cmwincnvBGK);

   //This method is mainly to set defaults and get rid of the lingering text from last CMwin use. defaults are not used and they must be set using the CMwinBGK() command. Using the above will only allow two lines of text to be shown.

}

function CMwinResetTEXT(Text) //update the text canvas

{

   cnvTempTEXT = cmwincnvTEXT;

   cnvTempHeight = cmwincnvTheight;

   txtLength = len(Text);

   GetFontSize(ftSize);

   GetRes(scnWidth, scnHeight);

   getcolor(clrR, clrG, clrB);

   if(cmwincnvTx == 0) { cmwincnvTx = 5; }

   if(cmwincnvTy == 0) { cmwincnvTy = 0; } //for sentimental reasons.

   if(cmwincnvTwidth == 0) { cmwincnvTwidth = cmwincnvWidth-5; }

   cmwincnvTheight = ( cmwinLine+GetTextWidth(Text)/cmwincnvWidth+1 )*ftSize; //update text canvas height

   cmwincnvTEXT = createcanvas(cmwincnvTwidth, cmwincnvTheight); //create new canvas with new height

   if(!(cnvTempTEXT == 0))

   {

      drawcanvas(cnvTempTEXT, 0,0, cmwincnvTwidth, cnvTempHeight, cmwincnvTEXT);

      KillCanvas(cnvTempTEXT); //kill the temp

   }

   //probably more complicated than what needs to be. I am still unclear on what I might be doing. I believe I am just resizing the canvas, and scooting the text in a few pixels.

}

function CMwin(Text)

{

   //declare a few variables

   ltrX = 0; //letter offset

   txtLength = len(Text);

   GetFontSize(ftSize);

   GetRes(scnWidth, scnHeight);

   getcolor(clrR, clrG, clrB);

   CMwinResetBKG(); //reset

   CMwinResetTEXT(Text); //reset

   if(cmwinLine == 0) { ltrX = 20; } //indent first line

   colorRGB(clrR, clrG, clrB);

   until(ltr == txtLength) { letters[ltr]; ltr++; } //I D K

   split(Text, "", letters[]); //split

   for(ltr = 1; ltr <= txtLength; ltr++) //Start a typing loop

   {

      if(cmwincnvTx+ltrX+GetTextWidth(letters[ltr]) >= cmwincnvTwidth && !(letters[ltr] == " ")) //word wrap

      {

         cmwinLine++; ltrX = 0; //no indent, no offset

      }

      pixeltext(ltrX, ftSize*Global(cmwinLine), letters[ltr], cmwincnvTEXT); //set the current letter

      if(keyDown("Space") == 0) { Delay(0.04); } //delay

      ltrX += GetTextWidth(letters[ltr]); //advance offset

      drawCanvastransparent(cmwincnvTEXT, cmwincnvTx, cmwincnvTy, 0, 0, 0, cmwincnvTwidth, cmwincnvTheight, cmwincnvBGK); //set

      drawCanvas(cmwincnvBGK, cmwincnvX, cmwincnvY, cmwincnvWidth, cmwincnvHeight, cnvRenderNow); //set

      drawCanvas(cnvRenderNow, 0, 0); //show

   }

   cmwinLine++;

}

function CMClear()

{

   cmwinLine = 0; //back to line one

   KillCanvas(cmwincnvBGK); //no previous BGK

   KillCanvas(cmwincnvTEXT); //clear the 'text cache'

   GetRes(scnWidth, scnHeight);

   getcolor(clrR, clrG, clrB);

   colorRGB(0, 0, 0);

   FillRect(0,0,scnWidth,scnHeight,cnvRenderNow); //remove the canvases from the screen

   drawCanvas(cnvRenderNow, 0, 0);

   colorRGB(clrR, clrG, clrB);

}

//test code: don't read it test it!

font("Times New Roman");

fontsize(20);

colorRGB(255, 255, 255);

CMwinBKG("mwin.jpg",10,10,350,350);

CMwin("RPG Gamer 17:");

CMwin("My Message Window Test.")

CMwin("I am quite surprised this message window actually works. I am not the smartest one. ^.^ Hold the space bar to make this type faster.");

CMwin("The text is wrapped to the next line if the message gets too long. I personally find this fascinating. I can run on and on about me and me and my cat and more me and I don't have to figure out where to pause and move the the next line or even when to put a period!");

CMwin("Wonderful, Is it not?");

CMwin("Press the Enter key to continue.");

until(keyDown("enter") == true) { }

CMClear();

CMwin("Downfalls:");

CMwin("You have to set the width and height of the canvas. I hope to add a 'scrolling' or paging feature so I only have to call CMwinBKG in the start program.");

CMwin("Anyways, Thank you for all your help and advice. If you see something I can shorten or improve, feel free to give me a shout. I tried to sneak the appearance of shortness but adding separate functions.");

CMwin("Press the Enter key to exit.");

until(keyDown("enter") == true) { }

CMClear();
```

Some of my if statements might look weird. I kept getting syntax errors for some odd reason. That was the only way they would work for me.
Tell me if it's not the case for you.

### armaniac · 2009-12-31 17:42 · #K487639

**A Question On the Zelda Battle System**

To ease myself back into the coding world, I've been working on a simple game using zombies and the Zelda BS. The dillemma I've encountered are as follows:
1) I created a program that, when acticated, should restore the player's HP to full. Unfortunately, it seems to do absolutely nothing when it is run. In addition, programs that reduce the player's HP show no signs of taking effect.
2) Since the menu is full of bugs, my game doesn't use it. I'm creating a program to save the game from the field when acticvated. Could someone tell me the proper code to create such a file or point me in the direction of a place that can?
I'd appreciate answers from anyone familiar with the programs I'm using or able to help me out in some way. It is very much appreciated, and don't worry- my questions will quickly become less n00bnish. ^^

### Prism · 2010-01-01 07:48 · #K487682

**Y hullo thar...**

Hey. Joined a while ago, been stalking for a while, typical noob. I'll just say "Hi, I'm Prism, nice to meet you all" and continue.
So after messing around with the toolkit a bit, I've been doing quite a bit of programming. I'm about to start on a battle system, and could use a little bit of help, because I'm not sure where to start.
First off, how would you create a smooth, non-laggy battle system in a general way? At first, I thought of making boards for battles, changing the characters' sprites, having them push()ed around the board to attack when it's their turn, create more sprites for arrows or spells that would also be push()ed, blah blah blah. Unfortunately, that seems like it would be extremely slow. Is there a faster way?
Another way I thought was to just set down a bitmap(), paste some animations of characters and enemies, and do stuff that way, but I'm not sure if that would involve more work.
I know these systems are TOTALLY and UTTERLY up to the person to decide how they work, and they are UBER customizable, but I was just wondering what would be the simplest way to create a clean-cut system.
EDIT: And you know what, while I'm at it, I have sort of the same question with the menu system. Would you paste an image of your menu, then just use lots of SaveScreen()s and cursors and whatnot when diving further through menus, then just restoring them? Or would I use loops and all that jazz? I can see how both would work, but I wasn't sure which would work better.
EDIT 2: And just to keep it all in one topic, I have another thing. Is it possible to have an image fade in, wait a moment, then fade out WHILE allowing the player to continue to move? To be specific, zone into a certain area, have the area's name fade in in a top corner, stay about a second or two, then fade out, but let the player move while all that's happening.
Thanks. Wink

### cuthalion · 2010-01-01 20:39 · #K487720

**Y hullo thar...**

Hi, welcome to Toolkitzone! You did the right thing by keeping all your questions in one thread.
1. I recommend you make a menu system first. It'll get you more used to loops and canvases and whatnot. See #2. Once you're ready, do some forum searches on the subject until you find a few explanations on how to make a battle system, since it's been asked before.
2. I would recommend using canvases and loops. See the codebible link in my signature, and look in the Library for articles on how to use canvases. Also see the other stuff in my sig, especially Marz's tutorial and the codebible.
3. Threads, I believe. Do a few forum searches on threads until you find someone asking what they are or how they work, etc. Basically, they're programs that run in the background while your dudes are walking around doin' stuff.

### rpg gamer 17 · 2010-01-01 20:51 · #K487724

**Y hullo thar...**

Look in the [function reference](http://tk3.toolkitzone.com/help/?page=19) or the code bible for the below:
createitem, putitem, eraseitem, destroyitem, putplayer, eraseplayer
These should make things easier. You kept saying sprite so I am guessing your using the board editor sprite creator thingy.
Using the push command is not recommended for long range movement. Unless you have a specific path you want to take.
I recommend looking into: [playerpath](http://tk3.toolkitzone.com/help/?page=19#playerpath) and [itempath](http://tk3.toolkitzone.com/help/?page=19#itempath)
Here is a code that will move player 1 from there current position to tile 5,5.

**Code:**

```
playerPath(playerHandle[[0], tkMV_PATHFIND, 5, 5);
```

Notice that I took off 'flags |' in front of tkMV_PATHFIND seen in the links above.

**Prism wrote:**

> create more sprites for arrows or spells that would also be push()ed
>

That would be one way to do it. I am a fan of cnvRenderNow. I am pretty sure I would of made an image fly across the room instead. Your item ideal sounds easier.
If your going to set a faded image. Your going to need [setimageadditive](http://tk3.toolkitzone.com/help/?page=19#setimageadditive). This will show the image at a certain percent.
You would need to use a thread to allow the player to move. Make sure you use killthread(threadID). I don't know if you can kill the thread in the thread. Try a combination of getthreadid(thisID) and killThread(thisID). I've only made like 2 in my life time. So I'm not the best at this.

### Dylan RPG · 2009-12-27 09:00 · #K487494

Hello everyone, name's Dylan. I've been lurking about this site for some time now, playing around with the Toolkit off and on. I've only just now begun to actually teach myself the programming to get more serious about it.
Anyway, I was wondering if someone could help me out with this issue I've been having. I'm sure someone can. Before I describe it though, I would like to communicate the following:
--I have done many searches on these forums looking for similar issues, and all of the solutions I have found don't work for me. I have also checked for solutions in the guide and troubleshooting that is included in the Toolkit.
--This problem occurs not just in my own project, but with the demo project that comes with the Toolkit.
I've got the white box problem. Yeah, that one. No, not the one for regular tiles on the board that can be solved with layers. The one where player characters show up with white boxes around them. I have already (a)made sure the backgrounds of the tiles I'm using are transparent, (b), made sure the transparent color is selected in each frame of the animations, (c)tried setting the toolkit and the engine to run as administrator.
I am using Windows 7. This problem did not occur back when I had XP. It may not have even occured when I was using Vista. Anyway I've tried it on a different computer (also running on 7) and the same problem is there. I'm guessing it's a Windows 7 compatibility issue?
I've also downloaded the unofficial patch for the latest version of the Toolkit (which is the one I'm using). No luck.
So ... how do I fix this? Why are all my characters walking around with white boxes behind them?
Any help would be grealy appreciated. Thanks Smile

### Dylan RPG · 2009-12-27 21:17 · #K487505

Yeah, that's true, I've heard others say they have no problems with Windows 7.
Thank you for the quick reply. Smile
I wonder what it could be? Especially since I've reproduced the error on two very different computers. It doesn't seem to make sense does it?

### Dylan RPG · 2009-12-28 01:29 · #K487513

Well, at home on my personal desktop, where the problem first occured, I was using a computer that ran originally on Vista. I noticed the Toolkit issue when I upgraded to 7.
The computer I'm currently using, which exhibits the same problem, is new and came with 7.
At home on the original computer it's running on Windows 7 Professional.
This computer is running on Windows 7 Home Premium.
It's a little disconcerting that the common denominator so far is myself. They are two different computers on different versions of an OS, with different graphics cards, and so on.
I don't know. I'm determined to fix it though.

### Dylan RPG · 2009-12-28 07:57 · #K487536

I believe I did the complete install. I didn't keep anything of mine from the old OS.

### Euix · 2009-12-28 15:21 · #K487542

I think this has more to do with graphics hardware than Windows 7, personally. The engine works fine for me; although I can confirm that I do experience the white box issue around sprites. The problem with assuming that Windows 7 is a common denominator, is that I believe this problem has also been associated with older versions of Windows, particularly the Windows 9x family.
Although, it may also be a problem with the GDI implementation in Windows 7, although since GDI has been modified with hardware acceleration in mind in the newer version of Windows, it may still be hardware related.
I would try updating graphics card drivers, or disabling excessive hardware acceleration if possible. You could even try tweaking graphics hardware configuration settings, then see if that helps. A lot of cards permit you to set application-specific settings.

### Dylan RPG · 2009-12-30 06:01 · #K487601

I have the latest drivers with my graphics card. I'll look into those other ideas, thanks.
There is an interesting aspect of this issue which I neglected to mention (I had forgotten).
There is one way in which the white box does not appear, and the transparency effect translates just fine: when the animation is set to 64 x 64. Of course in this circumstance only the top left corner of my character shows up when you run the game, but perhaps this exception means something?

### Grindalf · 2009-12-30 15:45 · #K487612

probably a silly question but have you tried running the game in fullscreen mode?
I had a similer probelm with 3.0.6 and running in fullscreen fixed it.

### Dylan RPG · 2009-12-30 19:19 · #K487616

Yes, I've ran it in full screen mode Smile I'm afraid that doesn't work for me.
Another note: my tiles have transparent pixels where they should be, but as soon as it comes down to making the animation and choosing the transparent color, it acts as though those pixels are white (RGB: 255, 255, 255). So something is being lost between the tile and the animation.
