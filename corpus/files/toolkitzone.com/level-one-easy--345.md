---
kind: file
id: "toolkitzone.com/345"
site: "toolkitzone.com"
title: "Level One: Easy"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=345"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041031024214", "20041105060014", "20041105110919"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_345", captured: "20041031024214", sha256: "2b93beb5a375208c3f7d1a8abfff1b9d9e396925183447364d4be06a7e0ba547", wayback_url: "https://web.archive.org/web/20041031024214/http://www.toolkitzone.com/fileman.php?id=3&file=345"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_345", captured: "20041105060014", sha256: "6d3e434156ca4b6a060e2e4700fde095836f64b9c75027cf6f19876282d46445", wayback_url: "https://web.archive.org/web/20041105060014/http://www.toolkitzone.com/fileman.php?id=10&file=345"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_345", captured: "20041105110919", sha256: "778f1055ed90b9fea5e0c2fe40e5f8ae4e14b18a61b02c6ce024661afc259479", wayback_url: "https://web.archive.org/web/20041105110919/http://www.toolkitzone.com/fileman.php?id=5&file=345"}
---

# Level One: Easy

After each section of this guide in which you learn a nice, large amount, I'll give you some glorious review exercises that you can use to test your knowledge. Try them out, see how many you can get right, and try again if you get it wrong. Remember; don't give up the first time your program doesn't work. Keep trying to figure out what's wrong with it first. Depending on how well you grasp the concepts in Unit 1, you can choose to start off with Level One (the easiest) questions, and work your way through. I have also included some hard questions. These questions require you to think just a little bit, and also teach you something new (in the HINT part of the question). If you can do that, you're doing great! If you can only do the level one questions, you're at "average". This means that you remember what I have taught you, and only what I have taught you. Meaning you can't apply your knowledge that well. But don't worry; we'll get more into "applying your knowledge" later. For those of you who don't know, this is how you create and run a program file written in RPG Code. Open up your Toolkit Editor, and then click on Program Editor. This is where you can write all the code you want! But wait, there's more. You can also "test" the code. You'll notice a green "play" button near the top, click on it so that you can test your program. Isn't that great? These are the answers for the level one questions. Only look at these once you have attempted these questions. If you can't do them, you have to read the unit over again. #score! = 0 *this will keep track of the score #questions! = 4 *I will be asking four questions. It's always a good idea to *set variables up for almost all numbers, so that you only *have to change one number when it comes to changing the # #bonus! = 0 *A variable for the bonus question #MWinCls() #MWin("Vampz is the head of Toolkitzone.") #Mwin(" 1- True") #MWin(" 2- False") #Wait(result$) #If (result$=="1") { #score! = score! + 1 } #If (result$=="2") { *Do nothing } #MWinCls() #MWin("Spyder wrote this TK Guide.") #Mwin(" 1- True") #MWin(" 2- False") #Wait(result$) #If (result$=="1") { *Do nothing } #If (result$=="2") { #score! = score! + 1 } #MWinCls() #MWin("Dan is as intelligent as a baboon.") #Mwin(" 1- True") #MWin(" 2- False") #Wait(result$) #If (result$=="1") { #score! = score! + 1 } #If (result$=="2") { *Do nothing } #MWinCls() #MWin("Marz is more intelligent than Dan.") #Mwin(" 1- True") #MWin(" 2- False") #Wait(result$) #If (result$=="1") { #score! = score! + 1 } #If (result$=="2") { *Do nothing } #bonus! = score!/questions! * 100 *Following BEDMAS, we divide their score by the number of *questions, and then multiply by 100. #MWinCls() #MWin("Great job! You finished the quiz! You're score is ") #MWin(" Review Exercises: Unit 1
***Level One: Easy***
- Create a program that will display the following text, "Hi, I'm a programmer!" on the first line.
- Create a program that does the same as the above program, except this time it will wait for the user to press a key, and then clear the screen, and then display the text, "I cleared the screen."
- Create a numerical variable, give it a name, and assign it a value of 2. Then assign it a value of 4 using the + sign.
***Level Two: Moderate***
- Display three lines of text, then when the user presses a key, clear the screen and display another three lines of text.
- Go back to the program you created in Level One (the first program), and this time, instead of putting the text in the #MWin, save it as a literal variable, and then display it.
- Create a question using the If statement that will ask the user if they like your program. If the user says yes, give them a pat on the back. If the user says no, insult them. Your message windows should not be cleared until the user presses a key on his keyboard.
***Level Three: Hard***
- 1. Create a quiz. Ask the user a series of true or false questions, for each answer they get correct, add one point to a variable, and display the next question. For each question they get wrong, do not add any points to the variable, and display the next question. At the end, tell them the score they got over the number of questions (e.g. You got 4/5 of the questions correct!). HINT: To display variables with a numerical value in the #MWin command, you have to surround them with < and >, for example: #MWin("
"). BONUS: Display the percentage that the user got right for bonus points!
***Level One Answers***
- #MWin("Hi, I'm a programmer") #Wait(a$) *Although I didn't specify it, it's always required you put #Wait(a$)
- #MWin("Hi, I'm a programmer") #Wait(a$) #MWincls() #MWin("I cleared the screen!") #Wait(a$)
- #name! = 2 #name! = name! + 2
***Level Two Answers***
- #MWin("This is the first line of text") #MWin("This is the second line of text") #MWin("This is the third") #Wait(a$) #MWincls() #MWin("This is the first line of text") #MWin("This is the second line of text") #MWin("This is the third") #Wait(a$)
- #text$ = "Hi, I'm a programmer" *Saves text to a variable #MWin(text$) *because text$ has a value that is already in quotation marks, I don't need to put *quotation marks around it in the #MWin command. #Wait(a$)
- #MWinCls() #MWin("Do you like my program?") #Mwin(" 1- It's pretty cool") #MWin(" 2- I hate it") #Wait(result$) #If (result$=="1") { #MWincls() #MWin("Yay! Thank you.") #Wait(a$) } #If (result$=="2") { #MWincls() #MWin("How dare you!?! Get out of my sight!") #Wait(a$) }
***Level Three Answer***
/ , or %") *Again, to display numerical variables in an MWin, you must *surround them with < and >. #Wait(a$)
