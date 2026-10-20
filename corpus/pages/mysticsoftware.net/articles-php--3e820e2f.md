---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/articles.php?article=17&category=3&mode=1"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/articles.php?category=3&mode=1&article=17"
written: null
date_confidence: "unknown"
updated: null
captured: ["20050221082806"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/articles.php__category_3_mode_1_article_17", captured: "20050221082806", sha256: "a5da9e0ddfdb60295d41719b42031921b8b45414c51738fdc88173776706ee29", wayback_url: "https://web.archive.org/web/20050221082806/http://www.mysticsoftware.net/articles.php?category=3&mode=1&article=17"}
---

# Mystic Software

***************** *Recursion tutorial* ***************** ******By BP****** ***************** Part 1: Introduction Part 2: Basic uses Part 3: My first recursitive program Part 4: Advanced uses Part 5: Closing words Part 1: Introduction Welcome to my tutorial on recursion. What is recursion, you may wonder. It's simple. In RPGCode and other proramming languages, when a method calls itself. It's like an elegant loop, with other words. I must, however warn you, recursion in RPGCode is NOT for the unexperienced! Part 2: Basic uses You can use recursion anywhere in a program, and is a lot better then using labels(spaghetti code), a lot more readable, and stable. I haven't compared the speed, but I think the difference in speed between labels and recursion, is pretty low. Part 3: My first recursive program: #FontSize(15) #SayHello(10) #Method SayHello(num!) { #Mwin("Hello World! Count:
") #num!=num!-1 #If (num! < =10) { #SayHello(num!) } } #Wait Copy and paste this into the RPGCode-editor, and run the program. It will i.e. put "Hello World! Count: 10" in the message window, and it will count from 10 to 1. How? It's simple. It's because of the method SayHello. It recives 10 in num, and puts hello and the num! in the message window. Then it subtracts 1 from 10, and num! is now 9. Since 9 is bigger or equal to 1, it will run method SayHello (itself) again, with 9 as the argument. Method SayHello then recives 9 as a num, prints hello world and 9 to the screen, subtracts 1, and sends 8 to itself. Sounds easy? Well, this command sure is... Part 4: Advanced uses Now that you've learnt the basics, It' time to move on. Recursion can be used for lot of things, for example a banking program. I will not put any recursive programs here yet, but if anyone mails me at bpetter@webmail.no, I can answer questions(if I have the answers). Part 5: Closing Words Hopefully, this tutorial made you a litte wiser. There are some things you should note about recursion in RPGCode, the functions use the same variables. In C++, all function variables are different, even if they have the same way. But hopefully, we'll find way. -BP
