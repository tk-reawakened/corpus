---
kind: forum-thread
id: "toolkitzone-forums/21695"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Advanced Coding"
skin: "phpbb2"
thread_id: "21695"
title: "Massive Variables..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=21695"
written: "2005-07-22T22:43:00"
last_post: "2005-08-11T02:31:00"
date_confidence: "exact"
captured: ["20051018072025", "20060108234822", "20060108235642", "20060108235931", "20060109003533", "20060109011059"]
author: "JJ12121616"
repliers: ["Dont_Think_So", "p90m16mp5a4"]
authors: ["JJ12121616", "Dont_Think_So", "p90m16mp5a4"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_236519_amp_3Bsid_43c8c512fdf4dc06c2b9174cf5a65c4a", captured: "20060109011059", sha256: "ec96f22165c8dcb502c4919017871255499c9053574de05fdcc988aef8feb74d", wayback_url: "https://web.archive.org/web/20060109011059/http://www.toolkitzone.com/forums/viewtopic.php?p=236519&amp%3Bsid=43c8c512fdf4dc06c2b9174cf5a65c4a"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_236994_amp_3Bsid_43c8c512fdf4dc06c2b9174cf5a65c4a", captured: "20060108235931", sha256: "469eafb52a1849dfd254aab16a42f488fbd4748640a7863fb8ec25256c2f17a8", wayback_url: "https://web.archive.org/web/20060108235931/http://www.toolkitzone.com/forums/viewtopic.php?p=236994&amp%3Bsid=43c8c512fdf4dc06c2b9174cf5a65c4a"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_237249_amp_3Bsid_43c8c512fdf4dc06c2b9174cf5a65c4a", captured: "20060108234822", sha256: "80e406d47b2c5d84de7d0ad0c1ee148036ce10797d4ce0b88b86e1d590e617fb", wayback_url: "https://web.archive.org/web/20060108234822/http://www.toolkitzone.com/forums/viewtopic.php?p=237249&amp%3Bsid=43c8c512fdf4dc06c2b9174cf5a65c4a"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_244074_amp_3Bsid_43c8c512fdf4dc06c2b9174cf5a65c4a", captured: "20060108235642", sha256: "ab6d44773785217df2d30ab0b932b954709a6a289238e54e965bb5cf79cc0404", wayback_url: "https://web.archive.org/web/20060108235642/http://www.toolkitzone.com/forums/viewtopic.php?p=244074&amp%3Bsid=43c8c512fdf4dc06c2b9174cf5a65c4a"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_244180", captured: "20060109003533", sha256: "02cf8fce482863c2915fe1a933f33960a69206f42ff9ea464986985babfa81b1", wayback_url: "https://web.archive.org/web/20060109003533/http://www.toolkitzone.com/forums/viewtopic.php?p=244180"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_244180_amp_3Bsid_7cde889a94523dc3911efb6795047320", captured: "20051018072025", sha256: "819a5cc792f996fccca0f31de8918faec3d50fa32544a8be8a6138e875fa1ae2", wayback_url: "https://web.archive.org/web/20051018072025/http://www.toolkitzone.com/forums/viewtopic.php?p=244180&amp%3Bsid=7cde889a94523dc3911efb6795047320"}
links:
  - {url: "http://www.toolkitzone.com/stuff/files/101/CLinkedList.zip", status: "captured", local: "wayback/toolkitzone.com/stuff/files/101/CLinkedList.zip"}
---

# Massive Variables...

### JJ12121616 · 2005-07-22 22:43 · #B236519

I'm am Currently making a card game with the tk. im making it with a customiseable deck (Where is spellcheck when you need it). Each player has a 60 card deck. Each card has about 10 things to store. You also have a hand of 5 and a battle field of 5 with an extra zone ( you will see soon enough.)
71*10*2=1420 Variables, for just cards!!!
Can any one tell me a quick way to make all of these varaibles and be able to keep up with all of them? Is there a certain command to make it easyer?

### Dont_Think_So · 2005-07-23 23:11 · #B236994

Arrays and maps - quick and painless variable organization Smile. If you need help using arrays and maps, feel free to ask here.
<Edit>
This may also be a good place to release my CLinkedList classes:
<http://www.toolkitzone.com/stuff/files/101/CLinkedList.zip>
I would post an example but it yells at me when I try... just look at the bottom of each of those files Wink

### JJ12121616 · 2005-07-24 16:06 · #B237249

well, school me.
maps are the things with [ and ] in the variables but easy come easy go.

**Code:**

```
array->append(3)  //array[0] = 3

array->append(3)  //array[1] = 3
```

Does that mean...

**Code:**

```
Cardnumber->append(3)  //Cardnumber[0] = 3

Cardnumber->append(3)  //Cardnumber[1] = 3
```

And What would these equal?

**Code:**

```
Cardnumber->append(1)

Cardnumber->append(2)
```

And How do i Change the 0 in " Cardnumber[0] = 3 "

### p90m16mp5a4 · 2005-08-10 23:12 · #B244074

Uh.. Linked lists are hard even for me to understand :)
Like in Yu-Gi-Oh, wich I'm guessing is the game you're trying to copy, you would want to make a class.
Class Trap Card(effect$, type$)
{
run(effect$)
run(type$)
}
I never seem to remember how to make classes in RPGcode, but I think iti's like this:
Trap Card TrapHole(effectList.prg, counter.prg)
{
public:
//lol, nothing to put..
}

### Dont_Think_So · 2005-08-11 02:31 · #B244180

**JJ12121616 wrote:**

> well, school me.
> maps are the things with [ and ] in the variables but easy come easy go.
>
> **Code:**
>
> ```
> array->append(3)  //array[0] = 3
>
>
> array->append(3)  //array[1] = 3
> ```
>
> Does that mean...
>
> **Code:**
>
> ```
> Cardnumber->append(3)  //Cardnumber[0] = 3
>
>
> Cardnumber->append(3)  //Cardnumber[1] = 3
> ```
>

Yep.

**Quote:**

> And What would these equal?
>
> **Code:**
>
> ```
> Cardnumber->append(1)
>
>
> Cardnumber->append(2)
> ```
>

Well, if you put those after the above commands:
Cardnumber[2] = 1
Cardnumber[3] = 2

**Quote:**

> And How do i Change the 0 in " Cardnumber[0] = 3 "
>

Cardnumber[whatever!] = 3. You change it with the buttons on your keyboard Wink
The advantage of linked lists is that you can delete() something from the middle and all of the elements afterwards will get shifted, without having to step through each of them manually. You can also link parts of the list to another, like in the example, so a list of 1, 2, 3 becomes 1, 2, 3, 2, 3, 2, 3...
