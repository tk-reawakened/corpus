---
kind: file
id: "toolkitzone.com/447"
site: "toolkitzone.com"
title: "Name is the command you give it. You could give it any name (DestroyA, DestroyB, Spin, lookatthatweirdguy, etc.)"
original_url: "http://toolkitzone.com/fileman.php?id=10&file=447"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041113121851", "20041113121851", "20041113121851", "20041114055801", "20060311072052", "20060311072052", "20060311072052"]
author: null
repliers: []
authors: []
comments_present: 0
f_format: "#Method methodname (parameters)"
f_name: "Name is the command you give it. You could give it any name (DestroyA, DestroyB, Spin, lookatthatweirdguy, etc.)"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_447", captured: "20041113121851", sha256: "6f969d4ba55bdac2a1662ce23e94347d07c3a1874fcb68af3282eaa3cd07a078", wayback_url: "https://web.archive.org/web/20041113121851/http://toolkitzone.com/fileman.php?id=10&file=447"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_447-1f1fcd", captured: "20041113121851", sha256: "6f969d4ba55bdac2a1662ce23e94347d07c3a1874fcb68af3282eaa3cd07a078", wayback_url: "https://web.archive.org/web/20041113121851/http://www.toolkitzone.com/fileman.php?id=10&file=447"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_447-c70518", captured: "20041113121851", sha256: "6f969d4ba55bdac2a1662ce23e94347d07c3a1874fcb68af3282eaa3cd07a078", wayback_url: "https://web.archive.org/web/20041113121851/http://toolkitzone.com/fileman.php?id=10&file=447"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_447", captured: "20041114055801", sha256: "2e04e00c03d8269751f253ae61ce7a9908c2dca10bf4dc107d01313128877182", wayback_url: "https://web.archive.org/web/20041114055801/http://toolkitzone.com/fileman.php?id=5&file=447"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_447", captured: "20060311072052", sha256: "0ddfe9350551138463fbc76e31e56baed1cf8819bb4026da7a97e014bb5c1f2d", wayback_url: "https://web.archive.org/web/20060311072052/http://toolkitzone.com/fileman.php?id=3&file=447"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_447-43f0bb", captured: "20060311072052", sha256: "0ddfe9350551138463fbc76e31e56baed1cf8819bb4026da7a97e014bb5c1f2d", wayback_url: "https://web.archive.org/web/20060311072052/http://www.toolkitzone.com/fileman.php?id=3&file=447"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_447-c17d29", captured: "20060311072052", sha256: "0ddfe9350551138463fbc76e31e56baed1cf8819bb4026da7a97e014bb5c1f2d", wayback_url: "https://web.archive.org/web/20060311072052/http://toolkitzone.com/fileman.php?id=3&file=447"}
---

# Name is the command you give it. You could give it any name (DestroyA, DestroyB, Spin, lookatthatweirdguy, etc.)

##### # # #### #### # # # # # # # # #### # #### # # # # ### # # # # # # # # # # # # #### ####
EXPLAINS
M M MMMMM MMMMM M M MMMMM MMMMM MMM MM MM M M M M M M M M M M M M MMM M MMMMM M M M M MM M M M M M M M M M M M M M M MMMMM M M M MMMMM MMMMM MMM By TKGB
****
A method is a helpfull command to use. Whether you use it for a single purpose or multitasking, it will help you out. Here is a small tutorial for #Method uses in version 2 of the TK.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#Methods described by CBM
CBM, who created the TK, explains it this way on the command reference:
***************************** *****************************
#Method Name: Define a method.
Format: #Method methodname (parameters)
The Method command allows you to define a method. Methods are like functions (see #Fbranch), but are much better reccommended. Using methods, you can infinitely expand the RPGCode language by creating your very own commands. Commands created with the #Method command work in the very same way as the built in commands, and for all porposes, are indistinguishable from the built in commands.
methodname is the name of the method you are defining. Essentially, the method´s name is the same as a command name. If you created a method called DrawHouse, you would call the method in the same way as you would call any command (#DrawHouse). You cannot replace the methodname with any variable.
The parameters are the variables that get passed to the method. It kind of hard to explain- it´s better if you actually see it, so look at the example below.
Unless a method is actually called, the method declaration and following block of commands is ignored by the RPGCode interpreter.
The #ReturnMethod command allows you to return values to the calling command. It´s a good idea to #Kill variables created inside the method when it´s done.
Example:
* Example displaying methods.
#WalkInCircle(“Frap’) *This calls the method ‘WalkInCircle´
*and passes the literal value “Frap’
*as a parameter.
#Add(1,1,result!) *This calls the method ‘Add´ and passes
*the values 1, 1, and result! (result! *is the destination variable, though, as
*we will see in the declaration).
*This is the actual method declaration for the ‘WalkInCircle´
*command.
*Notice that the parameter is wic_handle$. This means that when
*the command ‘#WalkInCircle(“Frap’)´ is performed, the value
*“Frap’ gets put into the variable wic_handle$
#Method WalkInCircle (wic_handle$)
#Push(“N’,wic_handle$)
#Push(“E’,wic_handle$)
#Push(“E’,wic_handle$)
#Push(“S’,wic_handle$)
#Push(“S’,wic_handle$)
#Push(“W’,wic_handle$)
#Push(“W’,wic_handle$)
#Push(“N’,wic_handle$)
#Kill(wic_handle$)
*This is the method declaration for the ‘Add´ command.
#Method Add (add1!, add2!, add_return!)
#add_return!=add1!+add2!
#ReturnMethod(add_return!)
*Returns add_return! to the calling command. (In this case,
* result! will get the same value as add_return!
#Kill(add1!)
#Kill(add2!)
#Kill(add_return!)
Related Commands:
#Include, #Kill, #ReturnMethod
***************************** *****************************
Kinda confused me the first time.
He goes throughly into methods in the primer:
***************************** ***************************** Creating Your Own Commands RPGCode2 allows you to create your own commands. This makes the language extremely flexible and infinitely expandable. Although there are 160+ built in commands, you may wish to create your own to make specific tasks easier. Apart from the built in commands, there is also a library of extended commands in the file system.prg.
In RPGCode, you define a new command with the #Method keyword. #Method defines a new method. A method is basically just a command- it works the same and looks the same. The general form of #Method is:
#Method methodname (parameter1, parameter2, ...)
Following the #Method declaration is a block of commands that tell the method what to do.
methodname is the name of the method. Basically, this is what the command will be called. If you want to make a command called ‘#Pause´, then the method name would be Pause.
The list of parameters allows you send variables to the method. We won´t worry about that right now.
The best way to understand methods is to actually see one. Here´s what I´ll use as an example:
There is a problem with the #Wait command. It will stop waiting for a keypress even if the user presses one of the arrow keys. This is usually OK, but usually when a player walks into a program, the buffer has a few more arrow presses, and the first few #Waits will be ignored. So I want to make a command that will just wait for the user to press a key, ignoring the arrow keys. So, I´ll make a method called ‘#Pause´:
#Method Pause()
#pause_done!=0
#While(pause_done!==0)
#Wait(pause_wait$)
#If(pause_wait$~=“UP’)
#If(pause_wait$~=“DOWN’)
#If(pause_wait$~=“LEFT’)
#If(pause_wait$~=“RIGHT’)
#pause_done!=1
#Kill(pause_done!)
#Kill(pause_wait$)
And there it is! Looks a little complicated, but it really isn´t. I´ll go over it step by step:
First of all, the #Method declaration tells us that the command name is Pause. It has no parameters (the empty brackets). Next, we set up a While-loop. pause_done! is the conditional variable- the While-loop will keep running as long as pause_done! is equal to zero. Next, we wait for a key press. If the user did press an arrow key, the #Wait command puts the text “UP/DOWN/LEFT/RIGHT’ into the variable. The next series of #If statements check if the key pressed was not equal to “UP’, “DOWN’, “LEFT’ or “RIGHT’. If they key pressed successfully survives these tests, pause_done! becomes equal to 1, which will break us out of the While-loop. If the user did press an arrow, pause_done! will not be set equal to 1, and the while loop will start again, thus waiting for a key press again. Once the While-loop is done, the last two commands (#Kill) delete the variables created by the method. It´s a good idea to #Kill method variables at the end of a method to reclaim memory.
OK, so how do you use this command? Simple:
#Pause()
Just like a regular command. But if you were making a program, where would the method declaration go? Well, here´s an example of a program which uses the #Pause command:
#MWinCls()
#MWin(“Try pressing an arrow key!!!’)
#Pause() *Pauses for key press, ignoring the arrows.
#Method Pause()
#pause_done!=0
#While(pause_done!==0)
#Wait(pause_wait$)
#If(pause_wait$~=“UP’)
#If(pause_wait$~=“DOWN’)
#If(pause_wait$~=“LEFT’)
#If(pause_wait$~=“RIGHT’)
#pause_done!=1
#Kill(pause_done!)
#Kill(pause_wait$)
The actual method declaration is ignore by the computer unless it is actually called. So, after the #Pause command has been executed, the program ends, because the computer ignores the entire method block.
Creating Libraries As you can see, a method declaration can take up quite a bit of space in your program. Wouldn´t you rather use your own methods without having to type them out every time they are to be used? Well, you can. You can do this by creating libraries.
A method library is just a regular .prg file that simply contains method declarations for a number of commands. For example, we could put the method declaration for #Pause into a file called “pause.prg’. We can call up this library from any program using the command #Include. Here´s an example of the same program but this time, the #Pause method declaration is in a file called “pause.prg’:
#Include(“pause.prg’) *Imports the ‘pause´ library.
#MWinCls()
#MWin(“Try pressing an arrow key!!!’)
#Pause() *Pauses for key press, ignoring the arrows.
This program sure is a lot smaller and nicer looking. The #Include command just opens up the file ‘pause.prg´ and gives you access to the methods in that file. We can therefore use the command #Pause(), because the method declaration for #Pause is stored in ‘pause.prg´.
Passing Parameters So far we´ve made a method that does not have any parameters (the brackets were empty). However, usually you will want to send information to your method. This is done by passing parameters to the method.
As an example, let´s consider a method called #Add, that jus adds two numbers together:
#MWinCls()
#MWin(“I´m about to call the #Add method...’)
#Add(2,8,mynum!)
#MWin(“The result is: “)
#Method Add (add_num1!,add_num2!,add_dest!)
#add_dest!=add_num1! + add_num2!
#ReturnMethod(add_dest!)
*Now to #Kill of the variables.
#Kill(add_num1!)
#Kill(add_num2!)
#Kill(add_dest!)
This small program demonstrates a method which accepts parameters. The function itself is sort of useless- it adds two numbers together. This could be done using regular variable addition, but it is good as an example.
Take a look at the calling command (the command that calls the method):
#Add(2,8,mynum!)
This command passes three parameters to the method: 2, 8 and mynum!. What happens to these parameters? Well, look at the method declaration:
#Method Add (add_num1!,add_num2!,add_dest!)
This also has three parameters, except that hey are all variables. The parameters inside the method must always be variables.
Anyway, the parameters in the calling command end up being put into the parameters of the method declaration. In other words, add_num!=2, add_num2!=8 and add_dest!=mynum!
As you can see, this is a handy way to send a method information. Also, notice my naming convention. I used the name of the method, then a underscore, then a descriptive name for each variable. I do this so that it is unquestionable that those variables in that parameter list belong to the #Add method. This way, if the #Add method were to call another method, the other method probably wouldn´t interfere with #Add´s variables. This is a good idea and you should do this!!! Otherwise, bugs can start running around your programs and you won´t even know what´s going on!
Now, look at the command I used in the #Add method: #ReturnMethod. This is used to pass information from the method back to the calling command. In the above case, I did this:
#ReturnMethod(add_dest!)
This command takes the parameter add_dest! and corresponds it back to the equivalent calling parameter. In other words, mynum!=add_dest! In this way, a method can send the command that called it some information. The calling command can do whatever it wants with that information. In the above program, I just printed mynum! out in the Message Window, showing the result of adding 2 and 8.
Using parameters and the #ReturnMethod command, you can make your own commands, and they will be entirely indistinguishable from regular commands. You can make your own libraries to do specific things (like a drawing library that draws houses on the screen, that sort of thing).
For more information about methods look in the command reference section and look up #Method and #ReturnMethod.
The System Library The Toolkit comes with a standard system library that has some methods in it that extend the RPGCode language beyond the 140+ built in commands. This file is called “system.prg’.
The system library has the #Pause command inside it that we talked about earlier. So, If you want to use the #Pause command, you have to #Include(“system.prg’) at the start of your program. You will notice that I have done this in the demo game that comes with the Toolkit.
You can open the system library in any text editor and examine it for yourself. Each method has a short description that says what it does and how to use it.
***************************** *****************************
Yeah! kinda confusing as well huh!? Well try reading it a couple of times and you might get it.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>What is #Method?
The #Method command might look complex but with a little experience, you will see the #Method command as your friend and not something you will keep in the shelf. So how is the desing:
#Method Name (parameter1,parameter2)
Ok so what is this? Well lets see-
*** #Method: This is the command. Like any command, it starts with '#'. This is to declare it a method so the computer will know that is what you want to access.
Name: Name is the command you give it. You could give it any name (DestroyA, DestroyB, Spin, lookatthatweirdguy, etc.)
(parameter1,parameter2): These are your parameters. They will be used to check for anything you might want to change. Parameters are variables that will do any task you wish. At the moment we will leave these aside. ***
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>How do you access a method?
A method can be access 3 ways:
1.) Use the #Include command. At every program you will want to put #Include() on top so the computer will know what you mean and detect the method.
2.)Write down the method underneath.
3.) (TKGB's recommendation) Write down the method along with the filename. Example: If your .prg file is called "My_Methods" and the method is called #Look(), then you will write this down: #My_Methods.Look().
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Creating methods
Now lets make methods. First decided on a name. Ill wait.
...
...
...
...
...
You done yet?
Ok now write this:
#Method [your method name]() (on the brackets write downt he name of the method).
Now put {} on the bottom. These will create a block so the computer will detect the commands neccessary.
Now what should go inside the {}? Well lets say that you wish to create a method that makes your character make a sound. Well first find a sound you wish to use and put it in the media folder then write this down. ********** { #Wav("") } **********
Write down the name of the .wav file on the brackets.
Ok now lets test it out. Open the demo game and save this method anywhere (my suggestion is putting it in the system.prg file since im using that as an example). Go to any of the NPC (non player characters) on the item editor and click board driven button, then click on set the .prg on the spot where you activate the NPC (should be underneath the "While on board"). Note the associated .prg file and open it with the Program editor. Underneath all of the commands (except for the #end command unless its inside an #If command), set the method (#system.[your method name]()). Save.
Run your game and find that char. The sound should appear when you are done.
HORRAY! You just created a method.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Parameters.
Well the method is all good and dandy but couldn't we just use the #Wav command alone?
Yes
Then why the #method?
Cause, what if we wanted to have more than just one sound?
What?
I'll teach you what I mean:
You don't need a method to make the sound appear, but what if we wanted other sounds to play when something else happens like if you talk to someone below another? Well here is where parameters come in.
Ok go and find 3 more sounds. Open the .prg and write this down: ********** { #If (playerX[0]!>0) { #Wav("") } #If (playerX[0]!>10) { #Wav("") } #If (playerX[0]!>20) { #Wav("") } #If (playerX[0]!>30) { #Wav("") } } **********
Remember to write down the name of the file on the brackets. Save. Now go and write down the method on other NPC character's .prg files. Now run.
The command should now play 1 or more sounds depending on how low the char is on the board. ***
Well this is nice and all but one prob.
Whats that?
WHAT THE HELL DO THIS HAVE TO DO WITH PARAMETERS?
I...Im getting to that:
Ok now what the example showed was that if a player was beneath a certain X coordinate, sounds will play and gives us control. Now how about extending the control. We want to play a sound depending on the NPC. Well then do this.
Go to the board editor and click on RPGCode>Item menu on the taskbar. Double click on a NPC. Press advance button. Now at the bottom there should be a variable section. Note the name of the variable (the one before the '=' mark). Im nowhere near my TK so lets assume the name is #variable[0]!.
Do this to 3 more NPC's.
Ok now go to your method and rewrite this down. ********** { #If (variable[0]!=1) { #Wav("") } #If (playerX[1]!=1) { #Wav("") } #If (playerX[2]!=1) { #Wav("") } #If (playerX[3]!=1) { #Wav("") } } **********
Save and run.
During the game, you should talk to each of the NPC. At first you will hear nothing but talk to them again. AH! Now They each make a different sound. ***
Excellent TKGB.
Why thank you!
But one thing is on my mind
Whats that?
WHAT ABOUT THE PARAMETERS?
OK...ok...let me get to that:
Ok now we have advance our command power but lets go the distance. Now we will use the parameters.
On the #Method put this down *** #Method [your method name](go!) ***
Now on the method name (#system.[your method name]()) Write down 1.
Now on the original method rewrite this down: ********** { #If (variable[0]!=1) { #If(go!==1) { #Wav("") } } #If (playerX[1]!=1) { #If(go!==1) { #Wav("") } } #If (playerX[2]!=1) { #If(go!==1) { #Wav("") } } #If (playerX[3]!=1) { #If(go!==1) { #Wav("") } } } **********
save. Run the game. Nothing has changed.
Ok now change the value of go! to 0.
Run the game. Ah, the sounds no longer are there.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Apply Knowldege
Ok now how does the method work. Well, the method should look like this: ********** #Method [your method name](go!) { #If (variable[0]!=1) { #If(go!==1) { #Wav("") } } #If (playerX[1]!=1) { #If(go!==1) { #Wav("") } } #If (playerX[2]!=1) { #If(go!==1) { #Wav("") } } #If (playerX[3]!=1) { #If(go!==1) { #Wav("") } } } **********
When the method is declared, nothing happens. But when it is set such as #system.[your method name](1), the commands underneath the block obey. If the sounds should happen depend on whether the current method that the .prg detects has the go! value equaling to 0 or 1.
The parameters should be variables and ONLY variables. Remember that.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#MethodReturn?
I don't know what this does. If you do, contact me.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>So thats it?
Yup. Here are some suggestions:
1.)Read the reference and primer and study them. 2.)Practice making methods without paremeters first. 3.)Study up on useful commands such as #If and #While. 4.)Download other methods and use them even if its just for one minute or two.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Tadah!
Well thats it. Wish to contact me? E-mail plz: (redacted: email)
TKGB
- o L ____ \__/
