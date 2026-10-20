---
kind: forum-thread
id: "toolkitzone-forums/11234"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "11234"
title: "2 Important Questions..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11234"
written: "2004-11-11T03:20:00"
last_post: "2004-11-11T16:24:00"
date_confidence: "exact"
captured: ["20050110142813"]
author: "forsaken"
repliers: ["RDemusX"]
authors: ["forsaken", "RDemusX"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_123901_amp_", captured: "20050110142813", sha256: "2df394decb24c8c943ac3cd1015baaa07adba4e95cbef1e276f992b8d5f980c8", wayback_url: "https://web.archive.org/web/20050110142813/http://www.toolkitzone.com/forums/viewtopic.php?p=123901&amp="}
links: []
---

# 2 Important Questions...

### forsaken · 2004-11-11 03:20 · #B123727

I have 2 questions that i find important...
1) how do you change camera views?
2) to make a custom shop do i need to have a custom menu and if not how could i make a custom shop.

### RDemusX · 2004-11-11 03:31 · #B123733

1.) As we all know ... 3D is not possible with the TK. However ... I have been working my ass off to make it as realistic of an illusion as possible. I use 3D rendered bkg's for my boards. To change "CAMERA VIEWS" I have to make 4 copies of the board. It is alot of work but it works.
Another problem with the "CAN'T BE 3D" is that when the character goes further up on a board he is actually going to get smaller. I have also bypassed this problem too. It is kinda jumpy but it works. I make a bunch of the same player graphics and make each set smaller. Then on the board set it to #newplayer, as the character walks away from the "VIRTUAL CAMERA"
2.) The custom shop thing would not be hard at all. You will need graphics for your shops bkg, as well as the shopkeepers graphics. If it is cursor based you would need a cursor graphic as well. All the items in your game would need thier own stats and programs. It is alot of work but it can be done. Me and alot of others here have done it. Whatever you do just start with the graphics and then go to the programming. You will need to use arrays, as well as a bunch of your own custom methods. It really depends on how detailed you want your shop program to be. To just make a real shitty one would not be much work at all. If you are looking to make people turn thier heads ... then I say ... GO ALL OUT.
Good Luck.
RDX

### forsaken · 2004-11-11 03:34 · #B123735

thanks and do u have any idea on how i could get started on making a item shop all i really had for an idea was my own bg... the normal buy / sell stuff but it also has images for it.

### RDemusX · 2004-11-11 04:28 · #B123762

I don't use the cursor map command in TK 3. I have problems with it. I use my old way of making a cursor move. But here ya go this is an example of a shop that sells one item. Of course you would want to build on that.

**Code:**

```
***main shop window***

#method shop(item1$,item2$,item3$)

{

#include("buy.prg")

#include("sell.prg")

#mwin("What can I help you with today?")

#bkg$ = "yourbkgfilename.gif"

#cursor$ "yourcursorfilename.gif"

#bkgx! = 0

#bkgy! = 0

#selcurx! = 200

#selcury[1]! = 25

#selcury[2]! = 50

#selcury[3]! = 75

#bkgw! = 640

#bkgh! = 480

#selcurw! = 75

#selcurh! = 25

#select! = 1

#done! = 1

#setimage(bkg$,bkgx!,bkgy!,bkgw!,bkgh!)

#savescreen(0)

#while(done! = 1)

         {

         #restorescreen()

         #setimageadditive(cursor$,selcurx!,selcury[select!]!,selcurw!,selcurh!,add!)

         #wait(a$)

         #if(a$ = "UP")

             {

             #if(select! > 1)

                 {

                 #select! = select! - 1

                 }

             }

         #if(a$ = "DOWN")

             {

             #if(select! < 3)

                 {

                 #select! = select! + 1

                 }

             }

***SO FAR WE HAVE MADE A CURSOR THAT MOVES UP AND DOWN***

***NOW WE WILL PLACE THE ITEMS AND FIND OUT IF YOU HAVE***

***ENOUGH GOLD TO PURCHASE THEM***

***THE ABOVE PROGRAM IS GONNA BE USED TO MAKE A SELECTION***

***EITHER BUY, SELL, OR EXIT ... HERE IS HOW WE MAKE THAT HAPPEN*

       #if(a$ = "ENTER")

           {

           #if(select! = 1)

               {

               #buy()

               *this is a method that you will write for the player to buy*

               }

           #if(select! = 2)

               {

               #sell()

               *this is a method that you will write for the player to sell*

               }

           #if(select! = 3)

               {

               #done! = 2

               #restorescreenarray(0)

               }

           }

       }

}
```

***THAT WILL BE THE MAIN SHOP PROGRAM***
***NEXT WE NEED TO MAKE A METHOD THAT LET'S YOU BUY ITEMS***

**Code:**

```
***BUYING METHOD***

***YOU NEED TO MAKE A CURSOR THAT MOVES LIKE WE DID IN THE***

***MAIN PROGRAM. I AM LEAVING THAT TO YOU TO SHORTEN THIS***

#if(a$ = "ENTER")

    {

    #if(select! = 1)

        {

        #mwin("You want to buy a <item1$> ?")

        #wait(a$)

        #mwincls()

        #getgp(gp!)

        #if(gp! => 50)

            {

            #mwin("Thank You!")

            #takegp(50)

            #giveitem("potion.itm")

            #wait(a$)

            #mwincls()

            }

        #if(gp! > 50)

            {

            #mwin("You don't have enough gold ... SORRY!")

            #wait(a$)

            #mwincls()

            }

        }
```

You would do this for all the items. It is pretty self explanitory how you would sell items as long as you see how you bought them.
I hope this helps
RDX

### forsaken · 2004-11-11 04:42 · #B123766

thanks alot
edit: im trying it in tk3 but dont seem to be working properly.

### forsaken · 2004-11-11 05:00 · #B123775

ive tried testing it and it cant even get past the method shop(item1$, item2$, item3$)

### RDemusX · 2004-11-11 16:24 · #B123901

You would first have to save the method as something like ... shop.prg.
Then in the program that you want to start the shop you would do this:

**Code:**

```
#include("shop.prg")

#shop(item1$,item2$,item3$)
```

The #include will bring that long program for the shop and actually place it in the calling of the shop program.
When you type #shop(item1$,item2$,item3$)
You are actually putting
#shop("potion.itm","antidote.itm","pheonixdown.itm")
or whatever you want your items in that particular shop to be sold.
Those are just variables that you can choose to change anytime you call the shop program.
RDX
