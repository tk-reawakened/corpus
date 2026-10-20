---
kind: file
id: "toolkitzone.com/502"
site: "toolkitzone.com"
title: "Like the creator of the Toolkit says, it\u0092s mostly mathematical!"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=502"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041108064550", "20041113114852", "20041114145105"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_502", captured: "20041108064550", sha256: "146b55d2d84b760e73441b42fb72e87cb4235d01220c7da3db121202e2718949", wayback_url: "https://web.archive.org/web/20041108064550/http://www.toolkitzone.com/fileman.php?id=3&file=502"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_502", captured: "20041113114852", sha256: "85babffe8b46e7f9b04a987bf69eb85862d07dc1781cb2cafb611fdced98f754", wayback_url: "https://web.archive.org/web/20041113114852/http://www.toolkitzone.com/fileman.php?id=10&file=502"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_502", captured: "20041114145105", sha256: "e231dffc3f1b4ab451ae13781033bbc35aaef9674f05b6d41119551b24c2423e", wayback_url: "https://web.archive.org/web/20041114145105/http://www.toolkitzone.com/fileman.php?id=5&file=502"}
---

# Like the creator of the Toolkit says, its mostly mathematical!

R
P G C o d e h e l p f o r b e g i n n e r s
Hi, and thanks for downloading my little advice document on the world of RPG Code! I was new to this concept 6 months ago too, so I know how complicated it all seems at first!
To aid simplicity, there wont be any very complicated programs in here (sorry to advanced users!), but for those needing a kick-start; hopefully thisll do the job.
**
Contents
- Basics
- #Mwin is your friend!
- #If
- Where now?
- Conclusion
**
Basics
So what actually is RPG Code? Well, to put it basically, its a form of language that the computer can understand. This does mean that you need to learn another language! But dont worry, like everything with computers, its logical.
Firstly: The difference between # and *.
If the computer sees the symbol # it will look for a command to perform. Its that simple, its the part that follows it thats difficult!
Whenever writing any command for the computer, always, always, always put a # in front of it!
* on the other hand makes the computer ignore that particular line. This is helpful if you want to put an instruction there. E.g.
#Mwin(" Hello") *says hello
Ignore the bit before it, but the piece of text after the star wont appear anywhere in the program when you run it. Its just helpful when reminding yourself of what a command does!
What are commands? This is like a posh term for an instruction to give the computer.
What do the signs $ and ! mean? These symbols represent a "unknown" term. A $ means a letter or wordy term, a! means a numerical value  a number.
**
#Mwin is your friend!
This tiny little command "#Mwin("")" is probably the most fundamental of them all. Plus its the easiest!!! All it does is display a message window at the top of your game screen. You can then insert text, variables, almost anything! Master the Mwin, and youre on the road to RPG Code success!
One thing about #Mwin, it never works alone. It usually has two partners in crime! One is #Wait(a$) and the other is #MwinCls(). These two commands are very basic, but essential.
Look at this typical conversation framework.
#Fontsize(16)
#Mwin(" Welcome to the world of RPG Code!")
#Wait(a$)
#Mwincls()
Lets look at the individual commands.
Firstly theres the command . This does exactly what it sounds like it should do; sets the font size at 16. Simple! The reason I like to put this in is because text always appears really small on my screen, so I make it bigger so I can read it easier! #Fontsize(16)
Next we see our little friend #Mwin(" Welcome to the world of RPG Code! ")
This puts the text within the brackets into a message window at the top of the screen. Be careful though, if the text is too big for the box, itll vanish off to the side. Use the green arrow at the top of the Editor to give your program a test run and see if its all working. If not, simply put in another line of #Mwin("") and put the overflow text in there.
The next command was mentioned earlier, and thats . The definition of this command is that the computer will wait for the user to press any key on the keyboard, number or letter. #Wait(a$)
More adventurous users might consider using:
#system.pause() instead. This command will wait until the user presses the Enter key on the keyboard. Note: this doesnt work on the Toolkit Version 3.
Next comes the last command I mentioned, and thats . This clears the message window of any text. (IMPORTANT NOTE: It doesnt clear the window from the screen.) Use this command when the box is full of text so more can be added. #MwinCls()
When one character stops speaking and another one starts, clear the message window to make it clearer that another person is talking.
Top Tip -
And that is the basics of conversations!
**
#If
This tiny little command is usually the biggest problem for beginners to RPG Code. It is however, one of the best commands you can use, and adds enormous flexibility to your game.
#If is used for when you want the player to choose something. That bits easy, its writing all that in thats the hard bit. Before beginning to write the #If command, we need to understand what Variables are.
Variables
Remember when we were using #Wait(a$) and I said that the a$ bit meant any key on the keyboard? The a$ a variable. The $ sign signifies a letter or wordy term, and this generally means a keypress.
Variables can be used when you want to say something like this. "I can either poke the old man with a stick or talk to him." Its easy enough to say that out loud, but writing it in RPG Code language is a bit more difficult.
Open up your toolkit and start the Program Editor. Open the program called "poke.prg" in the folder containing this tutorial.
There should be on the screen the Editor displaying this:
#Fontsize(16)
#Mwin("What should I do with this old man?")
#Wait(a$)
#Mwincls()
#Mwin(" 1- Poke him with a stick.")
#mwin(" 2- Talk to him.")
Firstly, start with #Wait(a$). What were asking here is if you want to poke him with a stick, press 1. If you want to talk to him, press 2. Add the wait command at the bottom of the program. Like so:
#Fontsize(16)
#Mwin("What should I do with this old man?")
#Wait(a$)
#Mwincls()
#Mwin(" 1- Poke him with a stick.")
#Mwin(" 2- Talk to him.")
#Wait(a$)
Right, now we have to write this #If command. The basic framework for #If is this:
#If( the condition that needs to be met)
#Commands that you want to be performed
In our example here, the condition to be met is the user pressing either number key 1 or number key 2.
We write that like this: #If(a$= ="1")
Lost? Dont worry, lets look at it step by step.
First . Thats explained earlier, so thats ok. #If
Next This line is more difficult, but follow its logic. Its basically saying, if the keypress (a$) is exactly equal to "1". The one does need to be in speech marks to show its a key. Also, you do need to put in two = signs. Without them, it wont work. (a$= ="2")
Got it? Now all we need to is insert that line into our program. It should now look like this:
#Fontsize(16)
#Mwin("What should I do with this old man?")
#Wait(a$)
#Mwincls()
#Mwin(" 1- Poke him with a stick.")
#mwin(" 2- Talk to him.")
#Wait(a$)
#If(a$= ="1")
Remember the { sign after the #If.
Now to give the computer some commands to perform if you did press one. Write something along the lines of:
#Mwin(" Old Man: Ow! Did you have to do that?")
#wait(a$)
#mwincls()
Then add the closing } mark to end that #If command.
It should now look like this:
When writing in the brackets, put #Mwincls() first so that the message window doesnt become confused.
Top Tip 
#Fontsize(16)
#Mwin("What should I do with this old man?")
#Wait(a$)
#Mwincls()
#Mwin(" 1- Poke him with a stick.")
#mwin(" 2- Talk to him.")
#Wait(a$)
#If(a$= ="1")
#Mwincls()
#Mwin(" Old Man: Ow! Did you have to do that?")
#wait(a$)
#mwincls()
Good news people, your half way there! Now we need to write the command for if the user pressed 2.
Juts underneath the last sequence, write the framework as before with the #If but in the a$ = = bit, write "2" instead of 1.
Also, in the { } brackets type something like:
#Mwin(" Old Man: I dont wanna talk. ")
#wait(a$)
#mwincls()
Try it now on your Editor. Scroll down when your finished to see if you were right.
#Fontsize(16)
#Mwin("What should I do with this old man?")
#Wait(a$)
#Mwincls()
#Mwin(" 1- Poke him with a stick.")
#mwin(" 2- Talk to him.")
#Wait(a$)
#If(a$= ="1")
#Mwincls()
#Mwin(" Old Man: Ow! Did you have to do that?")
#wait(a$)
#mwincls()
#If(a$= ="2")
#Mwincls()
#Mwin ("Old Man: I dont wanna talk.")
#wait(a$)
#mwincls()
Did you get it? If not, go back and see where you went wrong.
Give your program a test run! Hit the big green arrow at the top of the editor to give your program a test!
Now save it as: "my first if.prg" for future reference!
The #If command can lead to all sorts of things in your game, its essential for mini-games, shops, menus, questions, everything! If you can master this piece of RPG Code, then youve almost mastered RPG Code.
**
Where Now?
So youve mastered Mwins and got If down to a tee, where do you go next? Well, anywhere! RPG Code has almost unlimited possibilities, so almost anything you want in your game is writable!
Ive found that writing mini-games is huge fun, and look very complicated when they actually arent! If youve had quite a bit of experience with RPG Code, try writing a drinking game where the characters drink tolerance is a random number between 1 and 100, and every drink has a drink hit value. If the drink hit is less than the tolerance, then they survive for the next round. If the drink hits more, they pass out aand wake up on another board with 1HP and 1SMP.
Little things like that are great fun to do, and do test your knowledge of programming. Have fun experimenting.
If your ever lost, look in the RPG Code Help menu. This is really helpful for finding the exact right code for the job.
**
Conclusion
I hope this tutorial has been helpful to new comers. I know its a bit brief and only tackles two commands, but Ive found that if you can use them, the rest kinda falls out into your lap.
Enjoy playing with RPG Code!
Thanks for reading.
*
Twin Keyblade
