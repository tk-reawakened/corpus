---
kind: forum-thread
id: "toolkitzone-forum/34450"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "34450"
title: "Weights program *solved*"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=34450"
written: "2006-12-31T05:27:00"
last_post: "2006-12-31T06:20:00"
date_confidence: "exact"
captured: ["20070320195618"]
author: "Fire"
repliers: ["rpg gamer 17"]
authors: ["Fire", "rpg gamer 17"]
posts_present: 3
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_369142", captured: "20070320195618", sha256: "fa16439c63ff45f22357f4ffa437f92be70f7017cf6fed159987b5b8ca222d00", wayback_url: "https://web.archive.org/web/20070320195618/http://toolkitzone.com/forum/viewtopic.php?p=369142"}
links: []
---

# Weights program *solved*

### Fire · 2006-12-31 05:27 · #K369142

I'm having trouble with this. It's a program where you lift weights to gain Exp, but i can't get it to work.

**Code:**

```
mwin("Do you want to lift weights?")

wait

mwincls

mwin("1-Yes")

mwin("2-No")

wait

mwincls

if("1")

{

mwin("How long?")

wait

mwin("3-5 seconds")

mwin("4-9 seconds")

wait

mwincls

}

if("2")

{

end

}

if("3")

{

mwin("Okay")

wait

delay("5")

giveExp("you.tem",10)

mwin("You have gained 10 Exp")

wait

mwincls

end

}

if("4")

{

mwin("Okay")

wait

delay(10)

giveExp("you.tem",10)

mwin("You have gained 20 Exp")

wait

mwincls

end

}
```

### rpg gamer 17 · 2006-12-31 05:43 · #K369151

you need () at the end of wait and mwincls...
i commented it a little...

**Code:**

```
mwin("Do you want to lift weights?")

mwin("1-Yes")

mwin("2-No")

wait(get$) //return a variable (get$) to be checked by the if's

mwincls()

if(get$ == "1")  // the == means equal to... so if get$ equal to 1

{                //run this block of code.

 mwin("How long?")

 mwin("1-  3-5 seconds")

 mwin("2-  4-9 seconds")

 wait(time$)  //return a value to be checked by the if's

 mwincls()

 if(time$ == "1")

 {

  mwin("Okay")

  wait()

  delay(5)    // delay doesnt need quote in it

  giveExp("you.tem", 10)

  mwin("You have gained 10 Exp")

  wait()

  mwincls()

  end()

 }

 elseif(time$ == "2")

 {

  mwin("Okay")

  wait()

  delay(10)

  giveExp("you.tem", 20)

  mwin("You have gained 20 Exp")

  wait()

  mwincls()

  end()

 }

}

elseif(get$ == "2")  //elseif is good practice

{

 end()

}
```

this should work..

### Fire · 2006-12-31 06:20 · #K369158

Thanks it works now
