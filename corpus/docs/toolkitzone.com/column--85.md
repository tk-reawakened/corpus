---
kind: doc
id: "toolkitzone.com/85"
site: "toolkitzone.com"
title: "column"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=85"
written: "2004-12-10T19:00:00"
date_confidence: "exact"
updated: null
captured: ["20050222090720"]
author: "Occasionally_Correct"
repliers: []
authors: ["Occasionally_Correct"]
comments_present: 0
f_author: "Occasionally_Correct"
f_date: "December 10, 2004, 7:00 pm"
f_description: "This weeks topic for discussion is file input and output, useful for features such as custom save/load systems. Our resident code columnist OC takes you through the fundamentals as well as providing example code to help get you started."
f_title: "Using File I/O"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_85", captured: "20050222090720", sha256: "9ded1bf37886fc96a7c2ca31664b8c82bc7dcb6904729d63a23a5fc0fb9d96b1", wayback_url: "https://web.archive.org/web/20050222090720/http://www.toolkitzone.com/library.php?mode=read&doc=85"}
---

# column

RPG Code > Tips & Tricks
This weeks topic for discussion is file input and output, useful for features such as custom save/load systems. Our resident code columnist OC takes you through the fundamentals as well as providing example code to help get you started.
Hi there. OC here, with another article. Today, we'll be touching the surface of a subject known as file I/O. To begin with, what is file I/O? File I/O (Input/Output) allows you to read information from a file, and write information to a file (just like you would use Notepad to read and write text files). Manipulating file input and output can be a powerful tool when used correctly. It can be used for things like save/load systems (which will be covered in a later article), storing information in files and retrieving them for later use, and plenty of other things. So how do you use file manipulation? First, you need to start by opening a file. This can be done with one of four commands (openFileAppend, openFileBinary, openFileInput, and openFileOutput). Here's a short summary of the the different open file "modes" we'll be using: This mode opens a file, and allows you to write to that file. Anything you write to the file will be appended to the end of the file. If the file doesn't exist, it will be created. This mode opens a file, and allows you to retrieve information from that file. This mode opens a file, and allows you to write to that file. The difference between this and append mode is that you're overwriting whats already in the file (if anything) in this mode. If the file doesn't exist, it will be created. Now that you're familiar with the modes we'll be using, let's move on to a basic program that simply writes the users name into a file. This is a very simple program. First, we use . This takes two parameters; the file to open and the folder where the file should be located. Next, a prompt comes up and asks the user for their name. The name is then stored with , and we inform the user to check the 'Saved' folder. Finally, the file is closed with the command. If you run this program, you'll notice that the file 'test.txt' has been saved in the Saved folder, and it contains the name you typed in at the prompt. So far, all we've done is written a name to a file. A simple task. Now, let's do something a bit more difficult (but still easy). In this next example, we'll ask the user some miscellaneous questions, and save all of their answers with a method, then retrieve those answers with another method. Before we do the actual program, let's take a look at the methods. The first method, , takes four parameters: the file to write to, the folder where it's located, an array to write to the file, and the max index (the upper-bound) of the array. Starting from the top, we open the file in output mode. Next, we use a for loop. It's increment/condition variable ( ) serves as the current index of the array (the 'index' of the array is the number between the 's). Inside the for loop, we first create a temporary variable. It's value is the returned value of the command. The command looks for " " in (since the parameter is the name of the array (i.e.: " ")), and replaces it with " ". Why does it do that, though? Well, let's say that the parameter is " ", and the current (index) value is 1. The replace command is just like saying, "replace the in with , and return that to ". Okay, now is equal to " ". Now, we use the command. For those of you who don't know, the command can run any command, create variables, and things like that. It's very, very useful in this situation. Why? The parameter in the command is just like saying " ", because it runs whatever is typed in. Thus, the value of has been written to the file. It loops through until it reaches the maximum index, and then it kills the variables and closes the file, ending the method. Now, the second method. This method, instead of setting an array to a file, retrieves the entire file and stores it in an array. takes three parameters: the file to open, the folder where the file is located, and the array name. This method resembles the last. As before, we start out by opening the file. This time, we open it in input mode, so we can read information from the file. Next, we set up the variable , and assign the value -1 to it (it's assigned -1 because it's the index of the array, and we're counting from 0. It will equal 0 once we get to the until loop). Next, we create a variable for the until loop, and then enter the loop itself. Inside the loop, we increment . Next, we run through the process of using to store the actual array name inside (as discussed when we looked at the last method). Again, like the , we use the command. This time, we're using it to assign the current line in the file to the specified array (let's say we used " " as the value for , and is at 2). This line of code is just like saying, " ". Next, we use an if statement to check if the we've reached the end of the file. This is done by using the command (EOF stands for 'End Of File'). The command takes the filename as it's parameter, and returns 1 if the end of the file has been reached, and 0 if it hasn't (remember; if you supply a value for an if statement with no other condition, it just checks if the value is equal to 1). If we have reached the end of the file, it sets to 1, so we can break out of the loop. Otherwise, we keep going. When the loop ends, we return the maximum index of the array to the user, clean up the variables, and close the file. Finally, as promised, you'll get to see these two methods put to good use in a real example. If all that explanation made you forget, this example asks the user some questions, and then stores the answers in a file (using ). It then retrieves the answers, putting them in a new array ( ). If you run this program, you'll be attacked by prompts (five, to be exact). Each of the answers you supply are stored in the question[]$ array. This array is then passed as a parameter to , which sets each element in the array into the specified file (questions.txt). Next, we use to get all of the lines from the file and store them in the array. We then loop through each index of the array, showing it's contents. To see the answers in the actual file, go to the Saved folder and look for the file, "questions.txt." Well, that's it for today. I hope you enjoyed and learned something from this article. Remember; file I/O can add some interesting stuff to your games. And, like many other things, it can be applied in different ways. You could add more methods for further manipulation (such as copying one file to another), or even turn it into a class. Input is greatly appreciated. So if you have anything you'd like to say, please do! If there's a certain article you'd like to see in the future, you're welcome to PM me your ideas. **Using File I/O**
**Introduction**
**Append mode:**
**Input mode:**
**Output mode:**
```
//Open the file
openFileAppend("test.txt", "Saved")
//Get the users name
name$ = prompt("What's your name?")
//Write name$ into "test.txt"
filePrint("test.txt", name$)
mwin("Check the saved folder for test.txt!")
//Close the file
closeFile("test.txt")
```
openFileAppend() filePrint() closeFile()
**I/O Methods**
setFileArray()
```
method setFileArray(file$, folder$, array$, bound!)
{
//Open the file
openFileOutput(file$, folder$)
//Loop through the array
for(idx! = 0; idx! < = bound!; idx!++)
{
//Get the array contents
temp$ = replace(array$, "[]", "[idx!]")
//Set the array element into the file
RPGCode("filePrint(file$," + temp$ + ")")
}
//Clean up!
kill(idx!, temp$)
//Close the file
closeFile(file$)
}
```
idx!
replace() replace() array$ array$ array[]$ [idx!] array$ someArray[]$ idx! someArray[]$ [1] temp$ temp$ someArray[1]$
RPGCode() RPGCode() RPGCode() filePrint(file$, someArray[1]$) someArray[1]$
getFileArray()
```
method getFileArray(file$, folder$, array$)
{
//Open the file for reading
openFileInput(file$, folder$)
//Create an array index variable
idx! = -1
//Create the loop variable
done! = 0
until(done!)
{
//Increment the index variable
idx!++
//Put the array name into a temp. variable
temp$ = replace(array$, "[]", "[idx!]")
//Set the data in the file into the array
RPGCode(temp$ + "= fileInput(file$)")
//Check if we're at the end of the file
if(fileEOF(file$))
{
//If so, break out of the loop
done! = 1
}
}
//Return the index of the array
returnMethod(idx!)
//Clean up!
kill(idx!, done!, temp$)
//Close the file
closeFile(file$)
}
```
idx!
idx! replace() temp$
setFileArray method RPGCode() newArray[]$ array$ idx! newArray[2]$ = fileInput(file$)
fileEOF() fileEOF() done!
**The new example**
setFileArray() using getFileArray()
```
//Ask the user a bunch of questions;
question[0]$ = prompt("What's your name?")
question[1]$ = prompt("How old are you?")
question[2]$ = prompt("What's your phone number?")
question[3]$ = prompt("Do you like sandwiches?")
question[4]$ = prompt("Dogs, or cats?")
//Write the answers to a file
setFileArray("questions.txt", "Saved", "question[]$", 4)
//Now, retrieve the answers in a new array
bound! = getFileArray("questions.txt", "Saved", "data[]$")
//Loop through, showing the information
for(i! = 0; i! < = bound!; i!++)
{
show(data[i!]$)
}
wait()
```
setFileArray() getFileArray() data[]$
**Conclusion**
marcos
December 10, 2004, 7:13 pm
Good! It would be useful by saving characters like in Fallout.
Colin
December 10, 2004, 7:29 pm
My main suggestion would be to lose RPGCode(), it's a very evil command and not even required for anything (once we get classes, anyway). Good stuff. :)
marcos
December 10, 2004, 10:23 pm
Lose RPGCode()??? Change it to classes? NOOOO!
Occasionally_Correct
December 11, 2004, 3:00 am
He didn't exactly mean to take away RPGCode(), if that was your perception. :P He meant that, with the use of classes, the RPGCode() command isn't really needed. Of course, that's a whole discussion that I'm too lazy to get into right now. :P
William
December 11, 2004, 4:30 am
Really good work OC. Can't wait to read the save load part.. Thanks
Feb 18, '05
Feb 11, '05
Jan 29, '05
Jan 15, '05
Jan 8, '05
Feb 18, '05
rpg code > tips & tricks
Feb 11, '05
rpg code > tips & tricks
Jan 29, '05
rpg code > tips & tricks
Jan 15, '05
rpg code > tips & tricks
Jan 8, '05
rpg code > tips & tricks
