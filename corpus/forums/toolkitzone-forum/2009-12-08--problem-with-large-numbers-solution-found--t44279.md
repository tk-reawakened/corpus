---
kind: forum-thread
id: "toolkitzone-forum/44279"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "44279"
title: "Problem with large numbers *solution found*"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=44279"
written: "2009-12-08T22:19:00"
last_post: "2009-12-28T19:27:00"
date_confidence: "exact"
captured: ["20100101205206", "20100101205414", "20100101205440", "20100101205509", "20100101205629"]
author: "Rithran"
repliers: ["cuthalion", "Wolf", "SuperIsoRPG", "Geep4W", "aurum34", "UltimaWizard"]
authors: ["Rithran", "cuthalion", "Wolf", "SuperIsoRPG", "Geep4W", "aurum34", "UltimaWizard"]
posts_present: 19
pages_present: [1, 2, 3]
pages_total: 3
posts_per_page: 10
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_486462", captured: "20100101205509", sha256: "1dd81aadd90661b55337a601a3c8407d137befe5370d6167a43153ac80d4704c", wayback_url: "https://web.archive.org/web/20100101205509/http://toolkitzone.com/forum/viewtopic.php?p=486462"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_487546", captured: "20100101205206", sha256: "2b7821c83e5c843ef380d0d1c5f5f69e05bea0d93e324173267ad84e893614a4", wayback_url: "https://web.archive.org/web/20100101205206/http://toolkitzone.com/forum/viewtopic.php?p=487546"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_44231", captured: "20100101205629", sha256: "3b1be0bbf72428fa438f370b56e7da9bb254daf1bf214e5915a16c6977afd22c", wayback_url: "https://web.archive.org/web/20100101205629/http://toolkitzone.com/forum/viewtopic.php?t=44231"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_44279_start_0", captured: "20100101205414", sha256: "063fab125dc631849efe6876a238e61f1c2f895592771589c3379b8f1a28b058", wayback_url: "https://web.archive.org/web/20100101205414/http://toolkitzone.com/forum/viewtopic.php?t=44279&start=0"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__t_44279_start_10", captured: "20100101205440", sha256: "480d7d9013daa478d58ba88df532853b465a39a7e077dc3a780db318d9749233", wayback_url: "https://web.archive.org/web/20100101205440/http://toolkitzone.com/forum/viewtopic.php?t=44279&start=10"}
links: []
---

# Problem with large numbers *solution found*

### Rithran · 2009-12-08 22:19 · #K486262

**Building with an AVI...**

Hey guys, I'm the new kid in town, Rithran. So I've got a small issue. I've been working on a little game project, and just to add a little flair I've made a few .avi files as cutscenes. The files were made with blender(Probably irrelivent). So I went to test to see if there would be any build errors if I were to add them. Sure enough there was. As soon as toolkit tries to build a executable file, it crashes. Being how my .AVI files range from 200 to 300 Mb, I'm guessing it has to do with that fact that they are too big for toolkit. If I'm right, what programs would suggest in order to compress them? If I'm wrong - which I doubt - what do you suppose the problem is?
I'd check on google, but I'm actually not sure what it is that I'm looking for... heh...

### cuthalion · 2009-12-09 00:10 · #K486275

**Building with an AVI...**

Remember that avi files are just sort of containers. Whether your computer can actually play an avi depends on how it was made, so it may be that blender used a codec the Toolkit doesn't support.
(Or it could be size like you said.)

### Rithran · 2009-12-10 00:05 · #K486462

**Building with an AVI...**

Yeah, Life would be simpler if you didn't have to worry about codec crap... but you do. Thanks for the info.

### Wolf · 2009-12-18 21:50 · #K487125

Okay, there's this really annoying problem the toolkit has when working with large numbers. Here's an example:

**Code:**

```
x = 1000000000 //one billion

y = 1000000001

var[x] = 2

var[y] = 2

var[x]--

mwin(var[x] + " " + var[y])

wait()

mwincls()
```

Okay, this is what's weird, instead of var[x] equalling 1 and var[y] equalling 2, var[x] equals 1 and var[y] equals 1. Is there any way of fixing/getting around this (other than using smaller numbers... I kind of need the large ones), and if so how? Thanks Very Happy

### Wolf · 2009-12-18 22:22 · #K487129

**jackyboy wrote:**

> What could you possibly be doing that requires a number like 1 billion in an array?
>

Well, I have a bunch of different classes in my game and each class uses a certain base number (like 10,000) and every additional item in that class uses the base number plus one more than the last item's number to record their health (player 1's units start at 10,000, player 2's units at 500,000, and player 3's units at 1,000,000, and buildings start at 1,000,000,000). Obviously that's alot of room, but I have alot of classes and, eventually, I want to add more plyers.

**jackyboy wrote:**

> Anyway I believe there is a limit on how large your array can be.
>

Wouldn't there be a way to change that though? (if there isn't a way, or if it would be way too hard, I suppose I could lower the limit from 10,000 to 100 or something)

### Wolf · 2009-12-18 22:40 · #K487131

Smile I meant class as in a unit class Smile

**jackyboy wrote:**

> So if you need 1000000001 subtract 1000000000 and get index 1 from that number. So you still use the base number but you have regular index numbers for the array in the class.
>

I've actualy aleady done that, but in my game every item needs to have a different button (so you can click on them to view thier health) and since you can only have one button with a value of 0, that wouldn't really work. So I guess I'll just lower the limit, thanks for the suggestions Very Happy

### SuperIsoRPG · 2009-12-18 23:53 · #K487132

It sounds like you want to use a multi-dimensional array, if I understand what you are attempting to do correctly. There really isn't a need in a TK game to have more than a billion objects in a single array.

### Geep4W · 2009-12-19 00:08 · #K487133

Like Iso said, just use a multi-dimensional array.
Follow a format like this array[player][stat].
You can have class[1][1] all the way to class[1][1000] if you wanted, then start back over with class[2][1].
You can even add a third demension.

### aurum34 · 2009-12-19 00:11 · #K487134

maybe you should use strings instead of numbers inside of the array (i´ve done it)
and if you want to add one you can make your own method like:

**Code:**

```
AddToString(&n)

{

  local(last)=right(n, len(n)-1)

  if(last==9) {n=left(n, len(n)-2)+"10"}

  else {n=left(n, len(n)-1)+(castint(last)+1)}

}
```

of course i´m just going blind here, it´s just a suggestion because you could easyly put larger numbers using strings instead of numbers.

**Code:**

```
x="10000000000000000"

y="10000000000000001"

var[x]=2

var[y]=2

var[x]--

debugger(var[x]+" "+var[y])
```

i hope this helps

### aurum34 · 2009-12-19 06:32 · #K487145

i´m with furyx, but let´s not call this algebra, let´s call it common sense or fifth grade maths Very Happy

### cuthalion · 2009-12-19 07:42 · #K487152

It's not necessarily common sense... at least, I don't think so. But then, everyone tells me I have no common sense.
I recommend multidimensional arrays. Or use a class. (The programming kind.)

### SuperIsoRPG · 2009-12-19 12:41 · #K487166

Whatever you do, don't use strings.
And classes are class.
See what I did there. Yeah.

### Wolf · 2009-12-19 22:06 · #K487185

I'd use a multi-dimensional array but since I'm using these values for button slot numbers, a multi-dimensional array wouldn't work (since setButton("", var[1][0], etc.) would be the same button as setButton("", var[2][0], etc); so I think the best option would be to lower the maximum values I have that way I wouldn't have numers like a billion). Thanks again for all the suggestions Very Happy
Just on a side note, if you debugger the number one billion it shows 100e + 009 (or something like that) and if you debugger one billion and one, it shows the same thing.

### Wolf · 2009-12-19 22:32 · #K487189

**jackyboy wrote:**

> How is var[1][0] the same as var[2][0]?
>

Well (correct me if I'm wrong), if they both equalled 0 then setButton("", var[1][0], etc.) would be the same button as setButton("", [2][0], etc.), so yes the arrays are different, but their values are still the same and since button slots only use the value of the arrays then they would be the same, wouldn't they?

**jackyboy wrote:**

> Luckily it still knows the 1 exists.
>

Yeah, it knows it exists, but if you decrement the variable (like I did with x), it acts like it doesn't.

### UltimaWizard · 2009-12-20 01:45 · #K487203

**furyX639 wrote:**

> If you need to use an index of 1 billion, you're doing it wrong.
>

Maybe he's writing an advanced astrophysics simulation in RPGCode... Confused
In any case, the problems may come from the fact that even double-precision floating points numbers have their limits on what values they can be. Perhaps the number variable type in RPGCode dosen't fit in the valid range of doubles (though if I'm not mistaken the upper bound for unsigned doubles is something to the tune of 3 billion.)

### Wolf · 2009-12-21 14:24 · #K487282

**jackyboy wrote:**

> You say you're using these values for button slot numbers. So how are you setting slot numbers that using a multi-dimensional array wouldn't work? setButton() doesn't return a slot so you have to set the array to hold the button slot number anyway. What's the difference between using var[10000] to hold player 1's slot number and using var[player][0] to hold player 1's slot number?
>

Waaaaiiit, so you're saying that you use a variable to hold the button's slot numer? Because I always thought that you set the button's slot number (the function reference makes it look that way... at least to me anyways)(that would be why a multi-dimensional array wouldn't work), but if not, then yes, I could (and will) use a multi-dimensional array.

**jackyboy wrote:**

> The multi-dimensional array allows you to use the first index to identify the class and the second index to use the number. You then set these to anything you want. Why would var[1][0] hold the same slot as var[1][1] when var[10000] doesn't hold the same slot as var[500000]? Given by your example base number 10000 is player 1 and 500000 is player 2. I use the number 1 to represent players and the second index to represent which player we're looking at.
>

Yeah, I knew that already.
So, just to be sure, you grab the button slot number, not set it, right?
Edit:
Okay, at the moment I have no idea if you set the button's slot number or you grab it, so for right now I'm assuming you set it (because that's how I've designed my code). Here's an explanation of what I've done with some of my code (so maybe you'll understand what I've said a bit better). First, I made some variables:

**Code:**

```
hV[1][1] = 10000 //ten thousand

hv[1][2] = 20000 //etc.

hV[2][1] = 500000 //five hundred thousand

hV[2][2] = 510000 //etc.

hV[2][1] = 1000000 //one million

hV[2][2] = 1010000 //etc.
```

One of the reasons for the numbers being so spread out is so that the button slots don't conflict. Then, whenever an item is created, I do this:

**Code:**

```
iH[hV[pT][uT]] = //the item's health

hV[pT][uT]++

//pT = player turn (either 1 or 2)

//uT = unit type (either 1 or 2)
```

Then, whenever you click on an item, it does something like this:

**Code:**

```
mW("Hp = " + iH[input])

//mW() is a message window function I made

//input grabs what button was clicked
```

And whenever an item gets attacked I do this:

**Code:**

```
iH[hV[eT][eU]] -= damage

//eT = enemy turn (either 1 or 2) same sort of thing as pT

//eU = enemy unit (eiter 1 or 2) same sort of thing as uT

//damage = the damage the other item inflicted
```

So the problem is, when large numbers are used in iH[] and iH[] gets decresed all the other iH[]'s with the same base value equal the one that got decreased, for example:

**Code:**

```
iH[1000000] = 3

iH[1000001] = 2

iH[1000000]-= 2
```

Now both iH[1000000] and iH[1000001] will equal 1.

### cuthalion · 2009-12-22 07:14 · #K487314

I got confused when I read what you're doing, so I'll just say this and hope it's relevant.
If you're offsetting things in one array (like blah[100], blah[500000], etc...) just split it into multiple arrays instead of sticking them all in one, not knowing how much space you need between them, and using arbitrarily high numbers.
Er... I'll try one more time to read what you're doing...
...nope, I got lost again. What do button slots have to do with anything? What do your array names mean? hV? eT? eU? pT? uT? You explained iH, at least. I'm 99% sure there's an easier way than what you're doing.
Edit: Reread once more.
You do indeed set the button slot for each button. You can also hold that in a variable by putting a number in a variable, then using the variable for the slot when you make the button. But what does this have to do with anything? You need a separate button for everything? You can't just kill and remake buttons as you need them? What are these buttons for? Why do you need each and every thing in your game to have a different button? (That's what it looks to me like you're trying to do.)
Please show your code for making the buttons. Better yet, just show everything...

### Wolf · 2009-12-22 14:16 · #K487317

**furyX639 wrote:**

> so you could just as easily have one start at 0, and another referenced at 500
>

I know, I already suggested that (that's probably what I'll end-up doing), but then some people suggested multi-dimensional arrays and some other stuff, so if I can get around lowering the numbers, I'd rather do that, but if not then I'll lower the numbers.

**cuthalion wrote:**

> If you're offsetting things in one array (like blah[100], blah[500000], etc...) just split it into multiple arrays instead of sticking them all in one, not knowing how much space you need between them, and using arbitrarily high numbers.
>

Okay, if I get what you're saying, I don't think that will work, here, let me explain. Okay, the reason I have buttons for every unit/item in the game is so that when I click on an item I can view its health, and the only information you can get from clicking on a button (as far as I know) is the button's slot number, so, whenever an item is created, I make a button with a unique slot number, make an array that holds the button's slot number (the hV[][] array), and then set the item's health, using the button slot number that I just got (i.e. iH[hV[][]] = 3). That way, whenever I click on an item, I can display its health. Do you get it now?
As for the variable names, I did say what they stand for (eT = enemy turn), so eT stands for enemy turn, eU stands for enemy unit, etc.

**cuthalion wrote:**

> Better yet, just show everything...
>

I don't think you want that (there's a huge amount of code associated with buttons and they're in alot of different programs), but here's the code I use to make a button.... well, the simplified code anyways:

**Code:**

```
Code:

//remember this? I just forgot to put the setButton() in

setButton("", hV[pT][uT], etc.)

iH[hV[pT][uT]] = //the item's health

hV[pT][uT]++
```

So do you see now why multi-dimensional arrays wouldn't work? Because no matter how many arrays I use, the same value is going to end-up in iH[]. So, yeah, I'm pretty sure the only way to make this work is to lower the values of the arrays, which I'm not too sad about doing, because I did leave an overly large amount of space (but that was done before I knew there was a limit on how large the numbers could be).

### Wolf · 2009-12-28 19:27 · #K487546

**zyrshnikashnu wrote:**

> You could probably make the whole thing context-sensitive.
>

Yeah, maybe, I've decided to just lower the range of the values though (instead of 10,000, 20,000, 30,000, it's: 10,000, 10,100, 10,200 etc.) this will allow me to keep the numbers under 1,000,000 thereby avoiding the problem. Thanks for all the suggestions though Very Happy
