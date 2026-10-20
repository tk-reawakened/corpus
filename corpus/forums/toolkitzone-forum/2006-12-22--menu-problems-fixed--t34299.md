---
kind: forum-thread
id: "toolkitzone-forum/34299"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "34299"
title: "Menu Problems... - Fixed!"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=34299"
written: "2006-12-22T04:13:00"
last_post: "2006-12-23T03:22:00"
date_confidence: "exact"
captured: ["20070301160730", "20070301160740"]
author: "RainboKat"
repliers: ["k-hos", "rpg gamer 17", "Desh"]
authors: ["RainboKat", "k-hos", "rpg gamer 17", "Desh"]
posts_present: 9
pages_present: [1]
pages_total: 2
posts_per_page: 10
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 2, start: 11, end: 20, url: "http://toolkitzone.com/forum/viewtopic.php?t=34299&start=10", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_367387", captured: "20070301160730", sha256: "54016e64c80948c7ef99d827f22f9a541cabe72f5da1f3f49ea4e51570aabd68", wayback_url: "https://web.archive.org/web/20070301160730/http://www.toolkitzone.com/forum/viewtopic.php?p=367387"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_367654", captured: "20070301160740", sha256: "0fc0a48d9857a890371733ca3609d9ad026af8a1c79610bb8b71c9ae6fe955d1", wayback_url: "https://web.archive.org/web/20070301160740/http://www.toolkitzone.com/forum/viewtopic.php?p=367654"}
links: []
---

# Menu Problems... - Fixed!

### RainboKat · 2006-12-22 04:13 · #K367376

Well, I've attempted making a custom menu, and I'm doing okay except that it won't recognize any other characters in the party. My code will recognize the first character in the party, but not anyone else. I don't think that there's anything wrong with my code, spelling-wise, and the pertinent parts are below.
I've tried adding the second character to the party both before and inside the method "CMenuMain()", and in "CM PlayerData.prg", but nothing works. My test variable is "partyNum!", which reads how many character's names exist. For just one character in the party, it reads 1. But no matter which character I add, partyNum! only reads 1. If I could get it to read 2, then I'd know that I'd messed up on spelling somewhere, but I don't think that's it because partyNum! will not read 2.

**Code:**

```
addPlayer("tina.tem")

Include("CM PlayerData.prg")

Method CMenuMain()

{

   //Some code.....

   //Get player stats for players 0 to 4.

   For(a!=0;a!~=5;a!++){CMLoadPlayer2(a!)}

   For(a!=0;a!~=5;a!++){CMLoadMainStats(a!)}

   drawCanvas(MenuCanvas!, 0, 0, 608, 608)

   //Some more code....

}

CMenuMain()
```

CM PlayerData.prg

**Code:**

```
Method CMLoadPlayer2(x!)

{

   //getting character stats

   name[x!]$=playerHandle[x!]$

   If(name[x!]$~="")

   {

      partyNum!++

   }

}

Method CMLoadMainStats(x!)

{

   If(name[x!]$~="")

   {

      yImage!=30+70*x!

      setImage("player_MENUgraphic.png", 170, yImage!, 64, 64, MenuCanvas!)

   }

}
```

### k-hos · 2006-12-22 04:29 · #K367379

This is what I use :
#If(playerHandle[0]$~= "")
{
GetDP(playerHandle[0]$,Dp!)
GetFP(playerHandle[0]$,Ap!)
GetHP(playerHandle[0]$,Hp!)
GetMaxHp(playerHandle[0]$,MaxHp!)
GetSMP(playerHandle[0]$,SMP!)
GetMaxSMP(playerHandle[0]$,MaxSMP!)
GetLevel(playerHandle[0]$,lv!)
Text(2,7.9,"Level:<lv!>")
Text(2,6.9,"<playerHandle[0]$>")
Text(2,8.9,"HP:<MaxHP!>/<Hp!>")
Text(2,9.9,"SMP:<MaxSMP!>/<SMP!>")
Text(2,10.9,"DEF: <Dp!> ")
Text(2,11.9,"ATK: <Ap!> ")
}
Do this for all the players.
As for your code I didnt notice anything wrong with it...

### rpg gamer 17 · 2006-12-22 04:44 · #K367383

humm...
you can combined the methods and the getting of the player stats in to one for loop.

**Code:**

```
Method CMenuMain()

{

 //Some code.....

 For(a! = 0; a! ~= 5; a!++)

 {

  If(playerhandle[a!]$  ~= "")

  {

   //Get stats for playerhandle[a!]$

   yImage! = 30 + 70 * a!

   setImage("player_MENUgraphic.png", 170, yImage!, 64, 64, MenuCanvas!)

   partyNum!++

  }

 }

 drawCanvas(MenuCanvas!, 0, 0, 608, 608)

 //Some more code....

}
```

i cant test it (no toolkit on the computer im using) and i dont know if the methods where required for your menu to work but theres my 2 cents.
try adding more then 2 character. Confused idk... Smile

### RainboKat · 2006-12-22 05:00 · #K367387

Oh dear, that is a bit of cleaner code, isn't it? Very Happy At the moment, I like using seperate code for them because I don't have to scroll up and down all the time in the first one just to edit things in the player-info code.
Thanks, K-hos. I am doing that for the characters, but the method isn't getting anything after the first player, so I was just focusing on the fact that the name doesn't come up at all. Smile
I've added up to 4 characters to the party (so that there were 5 people in the party), and nothing was different. I know that the For loop is working because I used to have a variable called c! that increased one every time CMLoadPlayer2(x!) was used. I called c! and it came up as 5. So, for whatever reason, the code goes through the motions but refuses to recognize any of the stats for anyone after the first player.

### k-hos · 2006-12-22 06:01 · #K367392

I tested your code and I couldnt get it to work ether. I dont get what your trying to do that you couldnt do with
#If(playerHandle[0]$~= "")(you do know that you change the 0 to a 1 for player 2 right?)
because it will display whatever you want it to, like the name:text (1,1,<playerHandle[0]$>)
Pleas tell what your trying to accomplish

### Desh · 2006-12-22 14:22 · #K367421

When you add a player to the party shouldnt you increase x! by 1 so it doesnt overwrite the name of the player in the array.

### RainboKat · 2006-12-23 02:28 · #K367654

That's what the For() loop is there for. I rewrote the code similar to what rpggamer17 had, and it still didn't work. I know that this ought to work, since it works in a different program that I have.
The code from that program looked like this:

**Code:**

```
Method LoadPlayer(x!)

{

   name[x!]$=playerHandle[x!]$

   GetHP(playerHandle[x!]$,hp[x!]!)

   GetMaxHP(playerHandle[x!]$,mhp[x!]!)

   GetSMP(playerHandle[x!]$,mp[x!]!)

   GetMaxSMP(playerHandle[x!]$,mmp[x!]!)

   GetFP(playerHandle[x!]$,fp[x!]!)

   GetDP(playerHandle[x!]$,dp[x!]!)

}
```

Now, in the program that's used in, the method is used 5 times, with x!=0 up to x!=4. I copied that code over into my menu program, but it still doesn't work. Only the first player's name, health, etc. is recognized. The code doesn't find any stats (name, health, etc.) for any player that is added to the party at the very beginning of the code.
Neither a For() loop worked nor simply calling the method five times, as below. Name[1]$ through Name[4]$ (and other stats) are still just blanks.

**Code:**

```
For(a!=0;a!~=5;a!++){LoadPlayer(a!)}

LoadPlayer(0)

LoadPlayer(1)

LoadPlayer(2)

LoadPlayer(3)

LoadPlayer(4)
```

### k-hos · 2006-12-23 03:01 · #K367666

first off you need to do this to your methods: LoadPlayer(x!=1),Instead of just using 1
And second when you do other stuff its going to be hell when trying to be specific
So I sagest making 5 methods and just calling them

### rpg gamer 17 · 2006-12-23 03:22 · #K367675

**k-hos wrote:**

> first off you need to do this to your methods: LoadPlayer(x!=1),Instead of just using 1
> And second when you do other stuff its going to be hell when trying to be specific
> So I sagest making 5 methods and just calling them
>

loadplayer(1) is the samething as loadplayer(x!=1)
if your having trouble with coding, i suggest the same thing.

> [!missing] gap:11-20 · http://toolkitzone.com/forum/viewtopic.php?t=34299&start=10 · never-captured
> Page 2 of 2 was not recovered.
