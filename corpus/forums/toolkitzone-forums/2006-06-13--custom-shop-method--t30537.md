---
kind: forum-thread
id: "toolkitzone-forums/30537"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "RPG Code"
skin: "phpbb2"
thread_id: "30537"
title: "custom shop method"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=30537"
written: "2006-06-13T21:33:00"
last_post: "2006-06-15T04:00:00"
date_confidence: "exact"
captured: ["20060627020818"]
author: "darkangel"
repliers: ["DarkMoon", "Levi"]
authors: ["darkangel", "DarkMoon", "Levi"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_327373_amp_3Bsid_4a6f1d5a00106d33697c82f76115a18b", captured: "20060627020818", sha256: "216c43eafd9f9374e41f31c83991ad312e8c867826e3ff7acc4fa04febc85b78", wayback_url: "https://web.archive.org/web/20060627020818/http://toolkitzone.com/forums/viewtopic.php?p=327373&amp%3Bsid=4a6f1d5a00106d33697c82f76115a18b"}
links: []
---

# custom shop method

### darkangel · 2006-06-13 21:33 · #B327305

ok, here is the shop method:

**Code:**

```
method shop(item1$, item2$, item3$, item4$, item5$, item6$)

{

mwin("SHOPKEEPER: Hello and welcome. What would you like to do?")

wait()

mwin("1-SHOP")

mwin("2-LEAVE")

wait(answer$)

if (answer$ == "1")

{

mwin("Ok, what would you like to buy?")

wait()

pixeltext(64, 192, "<item1$>")

pixeltext(64, 212, "<item2$>")

pixeltext(64, 232, "<item3$>")

pixeltext(64, 252, "<item4$>")

pixeltext(64, 272, "<item5$>")

pixeltext(64, 292, "<item6$>")

done! = false

while (!done!)

{

   cMap! = createCursorMap()

   cursorMapAdd(59, 192, cMap!)

   cursorMapAdd(59, 212, cMap!)

   cursorMapAdd(59, 232, cMap!)

   cursorMapAdd(59, 252, cmap!)

   cursorMapAdd(59, 272, cmap!)

   cursorMapAdd(59, 292, cmap!)

   res! = cursorMaprun(cMap!)

   killCursorMap(cMap!)

switch (res!)

{

   case (0)

   {

      gp! = getgp()

      cost! = getitemcost(item1$)

      if(gp! >= cost!)

   {

      mwin("SHOPKEEPER: Ok, Here is your <item1$>!")

      wait()

      mwincls()

      giveitem(item1$)

      takegp(cost!)

      done! == true

   }

      elseif(gp < cost)

   {

      mwin("SHOPKEEPER: You dont have enough money!")

      wait()

      mwincls()

      done! == true

   }

   case (1)

   {

      gp! = getgp()

      cost! = getitemcost(item2$)

      if(gp! >= cost!)

   {

      mwin("SHOPKEEPER: Ok, Here is your <item2$>!")

      wait()

      mwincls()

      giveitem(item2$)

      takegp(cost!)

      done! == true

   }

      elseif(gp! < cost!)

   {

      mwin("SHOPKEEPER: You dont have enough money!")

      wait()

      mwincls()

      done! == true

   }

   case (2)

   {

      gp! = getgp()

      cost! = getitemcost(item3$)

      if(gp! >= cost!)

   {

      mwin("SHOPKEEPER: Ok, Here is your <item3$>!")

      wait()

      mwincls()

      giveitem(item3$)

      takegp(cost!)

      done! == true

   }

      elseif(gp! < cost!)

   {

      mwin("SHOPKEEPER: You dont have enough money!")

      wait()

      mwincls()

      done! == true

   }

   case (3)

   {

      gp! = getgp()

      cost! = getitemcost(item4$)

      if(gp! >= cost!)

   {

      mwin("SHOPKEEPER: Ok, Here is your <item4$>!")

      wait()

      mwincls()

      giveitem(item4$)

      takegp(cost!)

      done! == true

   }

      elseif(gp! < cost!)

   {

      mwin("SHOPKEEPER: You dont have enough money!")

      wait()

      mwincls()

      done! == true

   }

   case (4)

   {

      gp! = getgp()

      cost! = getitemcost(item5$)

      if(gp! >= cost!)

   {

      mwin("SHOPKEEPER: Ok, Here is your <item5$>!")

      wait()

      mwincls()

      giveitem(item5$)

      takegp(cost!)

      done! == true

   }

      elseif(gp! < cost!)

   {

      mwin("SHOPKEEPER: You dont have enough money!")

      wait()

      mwincls()

      done! == true

   }

   case (5)

   {

      gp! = getgp()

      cost! = getitemcost(item6$)

      if(gp! >= cost!)

   {

      mwin("SHOPKEEPER: Ok, Here is your <item6$>!")

      wait()

      mwincls()

      giveitem(item6$)

      takegp(cost!)

      done! == true

   }

      elseif(gp! < cost!)

   {

      mwin("SHOPKEEPER: You dont have enough money!")

      wait()

      mwincls()

      done! == true

   }

   }

   if(answer$ == "2")

   {

      mwin("SHOPKEEPER: Ok, come again!")

      wait()

      mwincls()

      end()

   }

   }
```

here is the armor shop program:

**Code:**

```
include("shopmethod.prg")

shop("bronze platebody", "steel platebody", "gold platebody", "", "", "")
```

i dont know how to make it so it will read the item file as .itm! it doesnt read the items as .itm, it reads them without the .itm.
thanks.

### DarkMoon · 2006-06-14 01:33 · #B327373

Try adding the .itm extension.
Like so:

**Code:**

```
include("shopmethod.prg")

shop("bronze platebody.itm", "steel platebody.itm", "gold platebody.itm", "", "", "")
```

### darkangel · 2006-06-14 20:20 · #B327571

ok, i fixed it. but now, when i select bronze platebody on the cursor map, everything works fine. but when i select steel or gold platebody, it ends the program! omfg! here is the code for the method.

**Code:**

```
method shop(item1$, item2$, item3$, item4$, item5$, item6$)

{

   if(item1$ ~= "")

   {

   name1$ = getitemname(item1$)

   cost1! = getitemcost(item1$)

   }

   if(item2$ ~= "")

   {

   name2$ = getitemname(item2$)

   cost2! = getitemcost(item2$)

   }

   if(item3$ ~= "")

   {

   name3$ = getitemname(item3$)

   cost3! = getitemcost(item3$)

   }

   if(item4$ ~= "")

   {

   name4$ = getitemname(item4$)

   cost4! = getitemcost(item4$)

   }

   if(item5$ ~= "")

   {

   name5$ = getitemname(item5$)

   cost5! = getitemcost(item5$)

   }

   if(item6$ ~= "")

   {

   name6$ = getitemname(item6$)

   cost6! = getitemcost(item6$)

   }

   mwin("SHOPKEEPER: Hello and welcome. What would you like to do?")

   wait()

   mwin("1-SHOP")

   mwin("2-LEAVE")

   wait(answer$)

   if (answer$ == "1")

   {

   mwin("Ok, what would you like to buy?")

   wait()

   mwincls()

   pixeltext(64, 192, "<name1$>")

   pixeltext(64, 212, "<name2$>")

   pixeltext(64, 232, "<name3$>")

   pixeltext(64, 252, "<name4$>")

   pixeltext(64, 272, "<name5$>")

   pixeltext(64, 292, "<name6$>")

   done! = false

   while (!done!)

      {

      cMap! = createCursorMap()

      cursorMapAdd(59, 192, cMap!)

      cursorMapAdd(59, 212, cMap!)

      cursorMapAdd(59, 232, cMap!)

      cursorMapAdd(59, 252, cmap!)

      cursorMapAdd(59, 272, cmap!)

      cursorMapAdd(59, 292, cmap!)

      res! = cursorMaprun(cMap!)

      killCursorMap(cMap!)

      switch (res!)

         {

            case (0)

            {

            gp1! = getgp()

            if(gp1! >= cost1!)

            {

            mwin("SHOPKEEPER: Ok, Here is your <name1$>!")

            wait()

            mwincls()

            giveitem(item1$)

            takegp(cost1!)

            done! = true

            }

            elseif(gp1! < cost1!)

            {

            mwin("SHOPKEEPER: You dont have enough money!")

            wait()

            mwincls()

            done! = true

            }

            case (1)

            {

            gp2! = getgp()

            if(gp2! >= cost2!)

            {

            mwin("SHOPKEEPER: Ok, Here is your <name2$>!")

            wait()

            mwincls()

            giveitem(item2$)

            takegp(cost2!)

            done! = true

            }

            elseif(gp2! < cost2!)

            {

            mwin("SHOPKEEPER: You dont have enough money!")

            wait()

            mwincls()

            done! = true

            }

            case (2)

            {

            gp3! = getgp()

            if(gp3! >= cost3!)

            {

            mwin("SHOPKEEPER: Ok, Here is your <name3$>!")

            wait()

            mwincls()

            giveitem(item3$)

            takegp(cost3!)

            done! = true

            }

            elseif(gp3! < cost3!)

            {

            mwin("SHOPKEEPER: You dont have enough money!")

            wait()

            mwincls()

            done! = true

            }

            case (3)

            {

            gp4! = getgp()

            if(gp4! >= cost4!)

            {

            mwin("SHOPKEEPER: Ok, Here is your <name4$>!")

            wait()

            mwincls()

            giveitem(item4$)

            takegp(cost4!)

            done! = true

            }

            elseif(gp4! < cost4!)

            {

            mwin("SHOPKEEPER: You dont have enough money!")

            wait()

            mwincls()

            done! = true

            }

            case (4)

            {

            gp5! = getgp()

            if(gp5! >= cost5!)

            {

            mwin("SHOPKEEPER: Ok, Here is your <name5$>!")

            wait()

            mwincls()

            giveitem(item5$)

            takegp(cost5!)

            done! = true

            }

            elseif(gp5! < cost5!)

            {

            mwin("SHOPKEEPER: You dont have enough money!")

            wait()

            mwincls()

            done! = true

            }

            case (5)

            {

            gp6! = getgp()

            if(gp6! >= cost6!)

            {

            mwin("SHOPKEEPER: Ok, Here is your <name6$>!")

            wait()

            mwincls()

            giveitem(item6$)

            takegp(cost6!)

            done! = true

            }

            elseif(gp6! < cost6!)

            {

            mwin("SHOPKEEPER: You dont have enough money!")

            wait()

            mwincls()

            done! = true

            }

         }

      }

   }

   if(answer$ == "2")

   {

      mwin("SHOPKEEPER: Ok, come again!")

      wait()

      mwincls()

      end()

   }

}
```

and here is the code for the armor shop:

**Code:**

```
include("shopmethod.prg")

shop("bronze platebody.itm", "steel platebody.itm", "gold platebody.itm", "", "", "")
```

so, can ne1 fix my problem?

### Levi · 2006-06-14 22:19 · #B327630

For every open codeblock bracket "{" you need a closing one "}"
You never closed your case(0)'s code block. In fact you didn't close any of the code blocks.
Here's what your code looks like fully indented.

**Code:**

```
switch (res!)

         {

            case (0)

            {  // start case code block

                gp1! = getgp()

                if(gp1! >= cost1!)

                { // start if case code block

                    mwin("SHOPKEEPER: Ok, Here is your <name1$>!")

                    wait()

                    mwincls()

                    giveitem(item1$)

                    takegp(cost1!)

                    done! = true

                 } // end if code block

                 elseif(gp1! < cost1!)

                { //start else codeblock

                    mwin("SHOPKEEPER: You dont have enough money!")

                    wait()

                    mwincls()

                    done! = true

                }// end if code block

            case (1)

             { //Start case cod block....wait...where's the code block ending for case 0?
```

Just add those endings and it should work fine.
Oh, by the way...your constant creation of variables for the same darn thing (gp1!, gp2!, gp3!) very redundant and it wastes memory. You should only use one gp variable each time. And kill all of your randomly made variables at the end of your shop usage. Just a thought.

### darkangel · 2006-06-15 04:00 · #B327772

thank you sooo much guys! Problem solved!
