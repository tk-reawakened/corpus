---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/library/rpgc_manual/chapter1.htm"
site: "mysticsoftware.net"
title: "Chapter 1: Getting Started"
original_url: "http://mysticsoftware.net/library/rpgc_manual/chapter1.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20020627000357"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/library/rpgc_manual/chapter1.htm", captured: "20020627000357", sha256: "d57b393d6eb6da36920bdd4f4b8caf38d99636c75487ef7b923da023a12c7cdd", wayback_url: "https://web.archive.org/web/20020627000357/http://mysticsoftware.net/library/rpgc_manual/chapter1.htm"}
---

# Chapter 1: Getting Started

Today you will learn how to...
Use the Edit Program screen in the RPG Toolkit to create and run programs
Use #Mwin to display characters to screen
Insert comments into your program
Use #Wait to pause your program
The Edit Program Screen
The Edit Program screen is where you can open, save, create, and run your RPGCode programs. To get to the Edit Program screen, open up your version of the RPG Toolkit, and click the button labeled Edit Program.
**
Graphic 1.1
![](Image1.gif)
*
Graphic 1.1: The RPG Toolkit main interface, with the Edit Program button circled. This is from Toolkit version 2.18.
A new screen should come up, with a window that looks like this:
**
Graphic 1.2
![](Image2.gif)
*
Graphic 1.2: The Program Editor. Main buttons have been labeled.
Much of this stuff is pretty self explanatory, but I'll explain it anyway. The 'New Program' button clears all code from the screen. With the open and save buttons, you can open and save your RPGCode programs files (*.prg's). The green arrow, 'Run Program', will run your RPGCode program. The 'Debug Program' button will assist you in taking all errors out of your program, provided you're using the Powerhouse edition of the Toolkit. Otherwise, it will bring up a screen telling you that it is disabled. The 'Event Editor' is an easy way to browse through what code does, and quickly insert it into your program. In the 'Code Editor', you enter the code for your program.
Your First Program
Now we will create our first RPGCode program. Open up the RPG Toolkit, then open up the Program Editor. In the 'Code Editor', type this in exactly as how it is shown. Don't worry about what everything in it does, we will explain it soon.
*Note: I have included line numbers in the code for easier readablity. Do not type in the line numbers.
**
Listing 1.1 The Hello World Program
-------------------------------------------------------------------------------------------------------------------------------
01: * This is your first RPGCode program!
02: #WinGraphic("mwin.jpg")
03: #Mwin("Hello World!")
04: #Wait(a$)
-------------------------------------------------------------------------------------------------------------------------------
Hello World! Output:
Now to explain what this program does. On line 1, you see the symbol, followed by text. This tells Trans2.exe, the RPG Toolkit game engine, to ignore anything past the on that line. #WinGraphic puts whatever graphic you specify in the quotes to be the message window graphic. If you're only seeing a black box, or getting an error for the #WinGraphic , make sure that you have mwin.jpg copied to your Toolkit2/Game/GameName/Bitmaps folder. It can be found in the Toolkit2/Game/Demo/Bitmaps folder.
#Mwin tells the game engine to display, in a message window, whatever is in quotes. In this case, it's displaying 'Hello World'. #Wait(a$) is the command to wait for the user to press a key. We'll talk about what is for later.
The Comment ( * )
Comments are good for helping yourself remember what a piece of code does three weeks after you've wrote it. It's also a good reminder to any other people who may be reading your code. Another good way to use it is to quickly take out chunks of code that you do not want, but may need again later.
To use a comment, just type the symbol, and then whatever you want commented out after it.
**
Listing 1.2 The Comment Program
-------------------------------------------------------------------------------------------------------------------------------
01: * This is commented out.
02: * And so is this.
03: * And this is too!
04: * What a silly program.
-------------------------------------------------------------------------------------------------------------------------------
Output: *Nothing*
Everything from line 1-4 is commented out. This is a useless program, but it demonstrates what a comment does.
The #Mwin and #MwinCLS() Commands
#Mwin will probably be your most often used command. #Mwin(variable$) displays whatever is in variable$ on screen. You can also use quotes around something, in place of using variable$
In the case you want to display a variable in a message window, you can either set it up as #Mwin(variable$) #Mwin(variable!) , depending on the variable type. Or, if you need to display a variable along with some text, you can set it up as #Mwin("You have gold!") . Variables will be explained more tomorrow.
**
Listing 1.3 The Message Window Program
-------------------------------------------------------------------------------------------------------------------------------
01: * The Message Window Program
02: #WinGraphic("mwin.jpg")
03: #Mwin("Hello world!")
04: #Mwin("Press a key to clear the message window!")
05: #Wait(a$)
06: #MwinCLS()
07: #Wait(a$)
-------------------------------------------------------------------------------------------------------------------------------
Hello world! Output:
Press a key to clear the message window!
On line 2, 'mwin.jpg' is used as the message window background. Line 2 and 3 display text to the message window. The program then waits for the user to press a key. On keypress, the message window is cleared with #MwinCLS() , and the program then waits for another keypress before exiting.
#Wait
#Wait command pauses your program and waits for a user to press a key. To use it, you type #Wait(variable$). variable$ is where the key you press on the keyboard is sent to. So, if you typed in a "2", a "2" would be recorded in variable$ . We'll talk more about variables tomorrow.
**
Listing 1.4 The Wait Program
-------------------------------------------------------------------------------------------------------------------------------
01: * The Wait Program
02: #WinGraphic("mwin.jpg")
03: #Mwin("Please type a letter:")
04: #Wait(letter$)
05: #Mwin("You typed !")
06: #Wait(a$)
-------------------------------------------------------------------------------------------------------------------------------
Please type a letter: Output:
You typed ! *(key you pressed)*
In this program, text is put into the message window, and then the program waits for a user to press a key with #Wait . On line 5, the key that the user pressed is printed in the message window. Line 6 makes the program wait for another keypress before exiting.
Setting the Message Window Graphic
You've learned how to print stuff to the screen, but what about getting a pretty message window background? The programs above have one, but when you try to have your own programs, they come out with a black background. This all comes down to the #WinGraphic command.
Using #WinGraphic , you can set the message window graphic. To do so, you use #WinGraphic variable$) , where variable$ is the name of the graphic with the extension, surrounded by quotes.
**
Listing 1.5 The Message Window Graphic Program
-------------------------------------------------------------------------------------------------------------------------------
01: * The Message Window Graphic Program
02: #WinGraphic("mwin.jpg")
03: #Mwin("If this on a blue/black background, you've done it!")
04: #Mwin("You've successfully set the #Mwin background!")
05: #Wait(a$)
-------------------------------------------------------------------------------------------------------------------------------
If this is on a blue/black background, you've done it! Output:
You've successfully set the #Mwin background!
As you can see, on line 2, the message window background is set to 'mwin.jpg'. On lines 3 and 4, text is displayed in the message window, and on line 5, the program waits for a keypress before ending.
Frequently Asked Questions
**
Q: Do I have to use the same capitalization as you do on your programs?
A: Not at all. RPGCode is not case sensitive, so feel free to capitalize the commands however you feel like. In this book, however, I use the most common way to write the commands.
**
Q: I used my own message window graphic, and now the size is screwed up! Is this an error in my programming?
A: No it is not. The message window graphic must be a certain size. Use the mwin.jpg graphic found with the Toolkit as a template for the size to set up your own graphic.
**Q: Can I use a variable that holds the name of the message window graphic instead of using just the name in the** **#WinGraphic command?**
A: Yes you can. Make sure that the variable is a literal ($), and that you do not surround the variable with quotation marks in the #WinGraphic command.
