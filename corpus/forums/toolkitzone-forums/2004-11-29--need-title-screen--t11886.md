---
kind: forum-thread
id: "toolkitzone-forums/11886"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "art"
skin: "phpbb2"
thread_id: "11886"
title: "NEED TITLE SCREEN"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11886"
written: "2004-11-29T21:45:00"
last_post: "2004-12-02T21:16:00"
date_confidence: "exact"
captured: ["20050114191841"]
author: "seveneternal"
repliers: ["sivart", "Levi", "nova11", "nascarjake"]
authors: ["seveneternal", "sivart", "Levi", "nova11", "nascarjake"]
posts_present: 11
pages_present: [2]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 15, url: "http://toolkitzone.com/forums/viewtopic.php?t=11886", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_133695_amp_", captured: "20050114191841", sha256: "9b2720666e2581f38523bd0bdc2062a83fc138b51798b63310e7107f45c20a6d", wayback_url: "https://web.archive.org/web/20050114191841/http://www.toolkitzone.com/forums/viewtopic.php?p=133695&amp="}
links:
  - {url: "http://img100.exs.cx/img100/5491/cd-TitleScreen0000.jpg", status: "external", local: null}
---

# NEED TITLE SCREEN

> [!missing] gap:1-15 · http://toolkitzone.com/forums/viewtopic.php?t=11886 · never-captured
> Page 1 of 2 was not recovered.

### seveneternal · 2004-11-29 21:45 · #B131719

Hmm... I'll whip one up for you...
But I'm feeling rather lazy right now...
Maybe later... unless someone else would like to.
.......

### sivart · 2004-11-29 22:01 · #B131733

Try emailing your friend?

### Levi · 2004-11-29 22:14 · #B131739

Man I wish I could help. But given my history with trying to be artistically creative (see Title Screen post I made last week) I don't think that would work out.
though that intro image you had looks like it could make a cool title screen if you'd change a few things. MsPaint could actually do that for you as well.

### nova11 · 2004-11-29 22:35 · #B131763

If 7E dosent get one to you soon, I'll try. But his would be better....
Razz
////

### nascarjake · 2004-11-29 23:45 · #B131809

i have tried emailing him and his email is not set up, i called him and he has yet to get his computer from storage (why the heck its there i dont know)

### nascarjake · 2004-12-01 14:09 · #B132819

so 7E are you up to it? and for every one else here id like to ask you a question, i have the edit box feature, (a plugin found a mysticsoftware.com) and im trying to get it to where i can type in somthing hit a button and it read what i typed. you see there is two major codes that you have to worry about after you make an editbox, the showedit() and hideedit() you see there are limitations to the commands that will be done while the edit box is shown, these "hidden commands" include the wait() feature. So now it is not as simple as just wait(a$). so i need to know how to get an action button that will inturn hide the editbox so i can preform other tasks

### Levi · 2004-12-01 18:25 · #B132952

Couldn't you, this of course is spoke from not knowing exactly what you want, just make the program so that when the box pops up two buttons or actually just one button pop up and you do that whole loop thing checking if a click button event occurs? If the button is clicked then Hide the Edit box. That effectively puts you program into a haulting loop until you lower the editbox.

### nascarjake · 2004-12-02 00:40 · #B133260

yea see i could do that with the set button but i want to have the button on my keyboard, and set button doesnt do that, oh and is some one going to help me out with the title screen? im not tring to rush but you know its kinda holding my game up, i got almost every thing up. Thanks again u guys

### Levi · 2004-12-02 00:52 · #B133269

Oh, I've got it. Do a loop, an infinite loop. Then use the #Get command to continually check the keyboard buffer. Then have an if statement there
#if(a$ != "") { exit loop}
THat exit loop I know isn't a command but I'm rusty with my RPGCode.
But that would effectively wait for a key press and exit when one is done.
Sampel code:
#While(somevar! == 0){
#get(a$)
#if(a$ ~= ""){
exit loop
}
}
HideEditBox
Pseudocode of course.

### Levi · 2004-12-02 21:13 · #B133690

Okay. Not the best but I tried making a 3d holographic screen from one of your images. This is the result. I can change anything, add text, both flat and 3d text. Or you can tell me it sucks and to get out of here. Your choice Smile
![](http://img100.exs.cx/img100/5491/cd-TitleScreen0000.jpg)

### nascarjake · 2004-12-02 21:16 · #B133695

sure thats right if i use the get command BEFORE i use the edit box, cause it wont do that command but yea, that should work lets just hope that it works while i have the edit box selected, because you see the edit box is like the quick reply box you must click on it before you are allowed to type anything and i think that while your in the edit box it skips all the keybord buffer commands but im not sure so ill try it thank you for all your help, and maybe if your interested you and pm me and you could help me with the rest of the game, just a thought, thanks again
OH AND I JUST NOW SAW THAT TITLE SCREEN i dont know if you did that in paint or not but that is kool. If you didnt do that in paint is there any way you can put some 3d letters inthere? oh and lot to ask but lol i have a good imagenation and was wondering if you could annimate that, like it flipping down or somthing i dont know lol i know thats probly almost imposible unless i do it witch would be impossible cause i have paint and i hate it so yea lol. but yes i love the title screen and urge u to join my team PLZ lol i need you despertly. LOL
THANKS EVERY ONE
