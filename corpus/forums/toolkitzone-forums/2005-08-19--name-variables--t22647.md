---
kind: forum-thread
id: "toolkitzone-forums/22647"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Advanced Coding"
skin: "phpbb2"
thread_id: "22647"
title: "Name Variables"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=22647"
written: "2005-08-19T00:36:00"
last_post: "2005-08-27T00:28:00"
date_confidence: "exact"
captured: ["20051107041423", "20051231085440"]
author: "ddl2829"
repliers: ["RPGOtaku", "p90m16mp5a4", "drcrazy4"]
authors: ["ddl2829", "RPGOtaku", "p90m16mp5a4", "drcrazy4"]
posts_present: 25
pages_present: [1, 2]
pages_total: 2
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_248062_amp_3Bsid_e17fa422e9d087d9cfa2c188b393f318", captured: "20051231085440", sha256: "2d806fb88bfc9c89888cac15dbdc463b9f775b60761f27396af9cf815a8aee5a", wayback_url: "https://web.archive.org/web/20051231085440/http://www.toolkitzone.com/forums/viewtopic.php?p=248062&amp%3Bsid=e17fa422e9d087d9cfa2c188b393f318"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_250646_amp_3Bsid_7cde889a94523dc3911efb6795047320", captured: "20051107041423", sha256: "6ccf8da91b8e10f175ad26af5ef79533f9d9cefb551589c22d95ac920ba04e22", wayback_url: "https://web.archive.org/web/20051107041423/http://www.toolkitzone.com/forums/viewtopic.php?p=250646&amp%3Bsid=7cde889a94523dc3911efb6795047320"}
links: []
---

# Name Variables

### ddl2829 · 2005-08-19 00:36 · #B247713

how do i make a prompt appear at the beggining of the game, asking the players name and what they enter is the players name? this is what i tried.

**Code:**

```
prompt("what is your name?",dest$)

dest$ == playerhandle[0]

clear()

mwin("so your name is <playerhandle[0]$>?")

wait()

mwincls()
```

how do i make this work?

### RPGOtaku · 2005-08-19 01:28 · #B247723

Display dest$ instead of playerhandle[0]. Like this:

**Code:**

```
prompt("what is your name?",dest$)

dest$ == playerhandle[0]

clear()

mwin("so your name is <dest$>?")

wait()

mwincls()
```

At least, I think that's it.

### p90m16mp5a4 · 2005-08-19 19:45 · #B248021

You typod the code. you also used the wrong operator. The following is shown incorrect, followed by correct:
dest$ == playerhandle[0]
dest$ = playerhandle[0]$
'==' is equal to operator, checks for equivilance in two variables.
'=' assignment operator, assigns an entity to an entity :)

### ddl2829 · 2005-08-19 20:43 · #B248047

ill try that

### p90m16mp5a4 · 2005-08-19 20:44 · #B248048

Why try? I know it works :-)

### ddl2829 · 2005-08-19 20:46 · #B248050

it isnt working, can you post exact code that might do what i want?

### p90m16mp5a4 · 2005-08-19 20:52 · #B248055

lol.. you didn't say you wanted to put dest$ in playerhandle$. Im assuming you want that now.
playerhandle[0]$ = dest$.
wowo.. playerhandle[]$ is a CONSTANT variable. You aren't very clear.

### ddl2829 · 2005-08-19 20:53 · #B248056

i want dest$ to be the players name

### p90m16mp5a4 · 2005-08-19 20:56 · #B248059

ok.. i just remembered playerhandle[] is a constant. And, playerhandle[0]$ is nothing. The playerhandle[] is a numerical value, not literal.
To find out the name of your character, go to the character editor. There is a tab right above the first box, wich holds the player name.
The tab next to it, called "advanced", holds the player name variable. Just modify that from there.
Keep looking at the character editor, following my instructions if you cant find the advanced tab.
the window is kinda like:
|stats|-|advanced|
--stats-------------------|
|Playername [....... ]|
|starting xp [......... .. ]|
|................................. |

### ddl2829 · 2005-08-19 20:58 · #B248062

okay, i got the name i type to appear in the mwin but could you be a little more clear on what to do in the charascter file?

### p90m16mp5a4 · 2005-08-19 21:01 · #B248065

there are two tabs in the char editor.
Stats and Advanced
The stats tab is where you fill in the boxes
The advanced tab shows all the variables wich hold the things you just filled in
Of course, if you knew abouta tab, the tabs are always right next to each other. look for the stats tab, wich is 12 pixels above the word "stats"

### ddl2829 · 2005-08-19 21:04 · #B248068

im confused, what do i need to set those variables as, and what do i need to put the name as?

### p90m16mp5a4 · 2005-08-19 21:13 · #B248072

From the advanced tab, you can set them to any literal value. They are not constant.
Actually, it appears that that they typod the variable in the help file. playerhandle[0]$ does have the char name lol. Why would they typo it Smile
It probably isn't a typo, but it does contain the persons name. Odd, in the advanced tab the players name is also numerical. I am thinking that they are using numbers to identify the names. So, using a regular literal value wouldn't hurt it, I presume.

### ddl2829 · 2005-08-19 21:20 · #B248074

please be more specific. what do i have to set the things as? to get the above code to work, what do i have to change, or set the character variables and name as?

### p90m16mp5a4 · 2005-08-19 22:02 · #B248086

O..Ok.. I'll spell it out.
The characters name variable. I was wrong, the character name variable can be anything, as long as you have it as an array.
you can change the characters name anytime, by reassigning a value to that variable.
dishead$ // wont work
dishead[anything]$ // will work
dishead[anything]$ = ddl

### ddl2829 · 2005-08-19 23:29 · #B248115

still dont get it.

### p90m16mp5a4 · 2005-08-19 23:51 · #B248121

Look at my display picture.
The box next to the text "Character name variable:" shows the character name variable. Change it to anything, as long as the variable is an array.
dishhead$ // wrong
dishhead[name]$ //right.
In your program, write this:
prompt("whats yer name", dest$)
dishhead[name]$ = dest$
mwin("your new name is <dishhead[name]$>")
wait
In your menu, it will show whatever you typed into dest$

### ddl2829 · 2005-08-20 00:13 · #B248128

it doesnt show the name in the menu. do i put the array in the name part under stats, or what? what do i put for the name to make it work?

### p90m16mp5a4 · 2005-08-20 00:17 · #B248132

the name in the stats is the default name, if you properly typed the variable into the advanced section, it will show whatever is in the dishhead[name]$ variable. [name] to my knowledge doesn't have to be called [name], I dont really feel like testing it so just use dishhead[name]$, dont put your name in [name]. type dishhead[name]$ in the variable place.
if you have msn, ill send you the files so you can see.

### ddl2829 · 2005-08-20 00:25 · #B248134

it still isnt working. if i enter the name in stats as blank, it has a blank in the game. if i enter it as default it says default. i cant get it to work.

### p90m16mp5a4 · 2005-08-20 00:29 · #B248135

ROFL no, I did it right. here, let me send you the files if you have MSN.

### ddl2829 · 2005-08-20 00:34 · #B248137

i dont have msn but you can send them to yahoo right? if you can its (redacted: email)

### p90m16mp5a4 · 2005-08-20 00:38 · #B248140

DDL.tem
Advanced tab:
Name variable: mycar[n]$ uncheck the default box. // doesnt make a difference though
stats tab:
name: anything
ddl.prg:
mycar[n]$ = "DDL"
mwin("now press the menu!")
wait
new.brd:
set ddl.prg
yourgame.gam:
set starting board to new.brd and char to DDL.tem
Run the game then execute the program, press the menu key. If your name doesn't show up, nothing else I can do.

### drcrazy4 · 2005-08-23 08:51 · #B249344

Prompt("What is your name?",1[name$])
That should work but in the character editor just name the character 1

### ddl2829 · 2005-08-27 00:28 · #B250646

that didnt work, but i got the guy on the screen to move by deleting what was in there...
