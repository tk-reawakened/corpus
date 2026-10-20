---
kind: page
id: "tk3.toolkitzone.com/tk3.toolkitzone.com/help/?page=18.4"
site: "tk3.toolkitzone.com"
title: "local(exists!) / exists! = 1"
original_url: "http://tk3.toolkitzone.com/help/?page=18.4"
written: null
date_confidence: "unknown"
updated: null
captured: ["20050726075259", "20051225190153"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_18.4", captured: "20050726075259", sha256: "1cb64c5c9ddb70ca05feb425e92216b474b6f0a8011018a4a59ea84cf72fab7c", wayback_url: "https://web.archive.org/web/20050726075259/http://tk3.toolkitzone.com/help/?page=18.4"}
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_18.4_amp_3BPHPSESSID_1f00881e54d36f1701dbec8d7d52a795", captured: "20051225190153", sha256: "c564ec228dfaffcbb0a27dfcfbc23070a203ddf7f7c0364a5780f2e8d54419ef", wayback_url: "https://web.archive.org/web/20051225190153/http://tk3.toolkitzone.com/help/?page=18.4&amp%3BPHPSESSID=1f00881e54d36f1701dbec8d7d52a795"}
---

# local(exists!) / exists! = 1

Plugin SDK Downloads
Contents
Advanced Features
Advanced Features
RPGCode provides several advanced features to make your programs more powerful. These include implicit inclusion, arrays, plugins, and much more. RPGCode's advanced features can help make your programs more organized and readable, and also take your programming to a whole new level. The advanced features are described below:
Implicit Includes:
You've already seen how to use the Include() command. Now, let's take it a step further with implicit inclusion. You can always type in 'Include("System.prg")' at the beginning of all of your commands that use Pause(), or you can do it efficiently. Implicit inclusion is done by typing in the name of the .prg file that you want to use methods from, followed by a period, then the method name. Here's an example of calling the 'Pause()' method from the system.prg file:
// This is the same as using '#include "system.prg"'
mwin("Try pressing an arrow key!")
system.Pause() // Wait for a keypress, ignoring all arrow keys
mwincls()
Scope:
When you create a variable in a program, it automatically sets itself to "global scope". "Global scope" means that the variable can be accessed from any program in your game unless you Kill() it. That means that if you have a variable called 'box!' that stores the number 5 in one program, you can still access that same variable through a different program. This is because global variables stay in your computers memory until you Kill() them or your game is ended.
So, how do you make it so that your variables aren't always global? Well, there are two commands for this specific issue: when you want to create a variable of "local scope", all you need to do is use the Local() command. "Local scope" means that the variable can only be accessed by the program that it's created in, and it will be destroyed when the program ends, freeing up memory. Here's how you use the Local() command:
// Let's create a local variable called 'box' and
// assign it the value 5...
local(box!)
box! = 5
// Now, let's show the contents of this variable...
show(box!)
Once that program ends, the local variable 'box!' will be destroyed. If you try to access it through another program, the value will be 0 because the variable doesn't exist anymore.
The second command you can use is #autolocal. This command takes it a step further by making local scope the default scope for variables. That means that all variables created in a program will be local, unless you use the Global() command to create a global variable.
// Make all implicitly declared variables local...
#autolocal
x! = 2 // A local variable
y! = 8 // Another local variable
global(z!) // A global variable
Scope isn't restricted to "normal" variables, however. Classes and methods also have scoping rules of their own. For example, when you declare a Local() variable inside of a method, the variable is destroyed when the method ends. The same thing happens with the parameters of a method. They're destroyed when the method ends, making it easier for you (since you don't have to kill() them).
Arrays and Maps:
Beyond using variables with simple names, you can use arrays and maps. If you're familiar with other programming languages such as Java or C++, you should already know how to use an array. If that's not the case, then here's an example of using arrays:
var! = 5 // This is a normal variable
var[0]! = 5 // This is an array.
var[1]! = 7 // Another array.
As you can see, arrays are distinguishable by the square brackets (the [ and ]). Inside of the square brackets, you can either use a numeric variable or a number. The number or variable inside of the brackets is called the "index". Arrays are useful for storing lots of different information about the same thing, because you can use the same variable name over and over again, just with a different index number.
A new feature that was added into TK3 is the use of multi-dimensional arrays (sometimes referred to as multi-d arrays). Multi-dimensional arrays are the same as normal arrays, except they can hold more than one set of brackets. Here's an example of a multi-dimensional array:
var[0][0]! = 1
var[1][0]! = 2
var[0][1]! = 3
var[1][1]! = 4
This example uses two sets of brackets and stores a different value for each different array. The array index 0,0 hold the value 1. The index 1,0 holds 2; 0,1 holds 3; etc.. You can even use multi-dimensional arrays to make the positioned squares of a chess board:
for (i! = 0; i! < 7; i!++)
{
for (j! = 0; j! < 7; j!++)
{
board[i!][j!]! = 0
}
}
This example uses a For Loop to count the variable i! from 0 to 7. The value of i! is placed into the index of the array, so each index goes up to 8 (a chess board is 8 x 8 squares).
"Maps" are the same as arrays, except their index is made of text or "strings". A simple map looks like this:
array[0]$ = "Hi" // This is a normal array
map["name"]$ = "Bob" // This is a map
Remember: By convention, Arrays always start with the index number '0'. Maps, on the other hand can have any index as long as it's text.
Commands as Parameters
Sometimes when making programs, you want to speed up the process and in doing so, speed up the code itself. Using commands as parameters wherever needed is the perfect way to compliment your code with speed, efficiency, and a cool look. The addition of commands as parameters lets you use commands and equasions in commands which weren't possible in TK2. For example, let's say I wanted to get the length of a string and use it in the Left() command, to copy a certain amount of characters in one string to another. I could do this:
n! = length("Awesome")
n! -= 4
string$ = left("Awesome", n!) // Returns "awe" from "awesome"
Or, I could do it like this, using an inline command and equasion:
string$ = left("awesome", length("awesome")-4)
See? Using a command/equasion as the parameter, I was able to turn three lines of code into just one. How does that work, though? Well, since the Length() command returns a value, it uses the returned value from the command as the parameter, even though the returned value doesn't seem to be present. The equasion (-4) is just like typing 'n! -= 4'.
Plugins:
You can create your own RPGCode commands that are embedded into the toolkit, instead of creating methods, with the use of plugins. You can write plugins for the RPGToolkit with any programming language that supports COM, but the dominating programming language to write plugins for the Toolkit in is C++. To create plugins, you need to download the plugin SDK (Software Development Kit). At the time of this writing, there are two TK3 plugin SDK's; a C++ SDK, and a VB SDK. To add a plugin into your game, simply click the project editor and select the plugins tab. From here you will be able to add and remove plugins. Once you have added the plugin to the main file, you can use the commands that you have implemented into the Toolkit.
Error Handling:
With most things that you will try, there will be trial and error. Well, how do you handle an error? Do you shut down? Do you continue as normal? You will eventually face this same scenario in programming. If an error occurs in your program, a debug message will appear telling you what went wrong. This can help you fix your errors. Error handling gives you a way to change what happens when an error occurs, so you can control your programs even when there's an error. This, however, is not the main purpose of error handling. It can be used for debugging purposes, but it can also be used in more abstract ways. You'll see a basic example below. So, how do we set up error handling? Listen up carefully!
To use error handling, there are a few keywords you have to remember.
On Error Goto :labal_name
On Error Resume Next
As you can see, these don't resemble commands at all. However, they work the same. Let's take a look at a method for checking if a file has opened and closed correctly (rather, if it exists).
Method FileExists(file$, folder$)
{
// Declare the variable 'exists!'
local(exists!)
// Assume the file exists
exists! = true
on error goto :error
// Try to open the file. If it doesn't exist,
// it will cause an error.
openFileInput(file$, folder$)
// Close the file just in case it was opened, but
// don't trigger another error.
on error resume next
closeFile(file$)
// Return the result
returnMethod(exists!)
// End the method so the error handler isn't run
end()
:error
// If we get here, there was an error
exists! = false
resume next
}
Looks a little confusing, right? Don't worry, it's quite easy once you get the hang of it. Let's take a look at what it does line by line.
— This sets up your error handling. If there is an error on any line of code after this, it will branch to the label ':error'. — Creates a local variable. 1 will be returned if there was no error. — This opens the file. If there was an error opening the file, the method will automatically branch to the :error label. — By using this, we are saying that if we run into an error after this line, don't do anything about it and resume the next line of code as if there was no error. — Now, we return the value of open!. If there was an error, we branched to :error, changed exists! to 0, and then we used 'Resume Next'. Resume Next takes us back to the next line of code after the the line with the error (which is the ReturnMethod line. So we return the value 0, which means it failed). — Ends the method and takes us back to the main program. **On Error Goto :error**
**local(exists!) / exists! = 1**
**OpenFileInput(file$, folder$)**
**On Error Resume Next**
**ReturnMethod(exists!)**
**End()**
If you want, you can pop up the debug message window and give an error by using the Debugger() command. For information on how to use the debugger command, check the TK3 command reference.
When using error handling, make sure you only branch to a label inside of the method you're using. Never branch to an outside label (this will mess up your programs!) Also, do not indent your labels. They will not work if you do.
