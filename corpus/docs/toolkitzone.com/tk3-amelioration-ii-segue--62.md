---
kind: doc
id: "toolkitzone.com/62"
site: "toolkitzone.com"
title: "TK3 Amelioration II \u0096 Segue"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=62"
written: "2004-11-28T18:56:00"
date_confidence: "exact"
updated: null
captured: ["20041216140652", "20050410054345", "20060208122806"]
author: "Colin"
repliers: []
authors: ["Colin"]
comments_present: 0
f_author: "Colin"
f_date: "November 28, 2004, 6:56 pm"
f_description: "Colin begins to explore the world of object orientated programming and its part in the future of RPG Code, using a custom battle system project that will be developed over the coming weeks to help illustrate the key concepts."
f_title: "Segue"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_62", captured: "20041216140652", sha256: "b84400c2ea6374b8a1ed2a2e4fa8ca98be93b49470627d3c7f8c13beecb1a3a9", wayback_url: "https://web.archive.org/web/20041216140652/http://www.toolkitzone.com/library.php?mode=read&view=cadd&doc=62"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_62", captured: "20050410054345", sha256: "929217e13e06f229d022af53eecb07539e89243b5d68f199296492a648344bc7", wayback_url: "https://web.archive.org/web/20050410054345/http://www.toolkitzone.com/library.php?mode=read&doc=62"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_amp_3Bdoc_62", captured: "20060208122806", sha256: "eacce48ce8ef6317ce7f6f7483a0771ec4f1d41fb637b556096f05f532f3f71d", wayback_url: "https://web.archive.org/web/20060208122806/http://toolkitzone.com:80/library.php?mode=read&amp;doc=62"}
---

# TK3 Amelioration II  Segue

S is truly a great word. While it may not provide insight into the content of the article, after reading, Im sure you too will agree it is fitting. As we all know, TK 3.05 is hopeful for a December release date. This release features the introduction of several new key features, additional stability, massive speed increases, and many a bug fix. Over the next few weeks I intent to kill several birds with one stone by talking about object oriented programming (OOP), elaborating on the overhauled sprite movement, illustrating threading, all in the form of a . *egue* real-time battle system
The following articles will not only teach how to code the battle system, but also how to apply the knowledge to future projects. Well address common concerns like how to keep track of troublesome numbers of globals, for the pioneer  where to begin, and how to maintain a project as large as a battle system.
When some people think of programming, they think of quickly and ruthlessly coding of a program, often with only a basic idea of what they hope to achieve. Mark my words; this is not something you want to be doing. The reality of programming is that the actual coding should be one of the least complicated parts of the experience  perhaps the most time consuming, but certainly not difficult. When you sit down and code without planning, you unknowingly make coding the most difficultalbeit the onlyphase in the process.
Almost all programming languages, throughout the years, have enabled you to create your own procedural abstraction, often by providing you with means to create functions; fewer languages allow you to create your own data abstraction, though. Even languages like C, which did just this, really just gave coders a way to group related pieces of information. Consider this VB (if you dont know VB, thats okay, there wont be many VB examples) Person type:
Type Person
As String strFirstName
As String strLastName
As Long lngStreet
As Long lngHouseNumber
As Long lngLocation
End Type
While it may look as if youve created a new type, in reality you have not. Programmers will still directly access the contents of the type, no additional abstraction has occurred. If you decided to implement the address as a string in the future, you would have to manually change every piece of code that uses Person . You could remedy this by coding new functions that manipulate Person
Public Sub As Person, As String, As String) personSetName ByRef thePerson ByVal strFirstName ByVal strLastName
= thePerson.strFirstName strFirstName
= thePerson.strLastName strLastName
End Sub
To many programmers, however, this may seem like additional work for no reason  in reality, it prevents re-writing if the name were to become one variable in the future  and will circumvent using the function by accessing the variables directly, thus defeating the purpose and preventing the abstraction from taking place. Languages like VB and C cause the programmer to think of data and procedural abstraction as very different things when in fact, they are integrally linked.
A previously popular method of program design was a . First think, What task does my program perform? Next, you contemplate, What processes make up this task? Finally, you decide, What data do these processes operate on? After answering these questions, youd proceed to code your program  all the while, thinking of data and procedures as unconnected. top-down approach
Encapsulation is a process that enforces abstraction by protecting the data with interface functions. A common tactic was to provide callers only with indexes to entities, thereby forcing them to call functions to manipulate the data. This procedure took more coding effort, however, and was not used as often as it should have been. In a movement to resolve this problem, , later to be known as C++, was created. C++, and other object oriented languages of its time, allowed the coder to define an enhanced typea classin which the data and the functions could be declared centrally, the data accessible to the class own functions. Using this concept, we could re-write the person type. (Note that Ill be using RPGCode for examples from here on in; document covers the syntax of classes in RPGCode.) *C With Classes* *only* [this](http://www.toolkitzone.com/stuff/files/226/RPGC3.rtf)
class CPerson
public
( $, $) method setName firstName lastName
$ = $ m_firstName firstName
$ = $ m_lastName lastName
() { ( $)} method getFirstName returnMethod m_firstName
() { ( $)} method getLastName returnMethod m_lastName
() { ( $ + " " + $)} method getName returnMethod m_firstName m_lastName
private
$ m_firstName
$ m_lastName
Classes successfully abstract, providing encapsulation, by the creator to use its interface methods. It is for this reason that you should . There are several relationships that your programs active entitiesits classescan harbor. , one such relationship, means that one class another class. Another type, , means that one class another class  a circle having a center point is a good example. Classes are the key point to unlocking the power of object oriented programming. *forcing* never have public variables in a class Inheritance *is a kind of* composition *has*
When you want to build an object oriented program, first ask yourself, What are the active entities in my program? A dealerships database may require a truck and a van class. Not many entities will be this obvious, however. An image editor may require a complex number class. A banking program may require withdraw and deposit classes. An operating system may require a process class. Our battle system may require players and enemy classes.
The next step is to answer, What are the relationships between these entities? Trucks and vans are cars, complex numbers and integers are numbers, withdrawing and depositing are transactions, players and enemies are both fighters. When you have established all the relationships, you should create a hierarchy. Here you can see a fictitious battle system hierarchy (ours will be fine tuned along the way):
Battle System
Battle System Objects
Fighter
Player
ii. Enemy
Move
Magic
Different magic
ii. Special
Different specials
iii. Physical
Regular
Strong
Fierce
iv. Item
Different items
It is a common practice to derive all of one projects classes from a single class (even MFC derives from CObject) and the class will tie the others together (using composition). Items can be created easily by deriving a class from the item class, as with magic and specials; this makes the battle system simple to maintain. *Battle System*
I plan to take a break from talking about coding and focus on some other integral elements of the battle system. How well move the sprites simultaneously is a question some people surely want answers to. All this and more, next week!
machsprinter
November 28, 2004, 7:41 pm
After the 3rd paragraph I was completely lost on what you were talking about.
Colin
November 28, 2004, 11:13 pm
I was referring to something I talked about . I intend to build the articles on one another, though this may not be a good idea :) [last time](http://www.toolkitzone.com/library.php?mode=read&doc=36)
matt72186
November 28, 2004, 11:30 pm
I don't quite understand the relationship between a class and a derived class in RPG Code other than the derived class inherits everything from the parent class and then adds on to it, so a Fraction is both a Number and a Fraction then right, just a special instance of Number. Other than that is there anything special about derived classes other than a method of organization? Also is there an unlimited amount of classes that can derive each other? So I can have a extend b, which extends c, and that extends d... and so on, so in essence a is also b, c, d, ...
Colin
November 28, 2004, 11:43 pm
Yes, the deriving can go on forever. Be careful, however, because if multiple bases are derived from the same class, incorrect calling of methods may occur. A derived class a base class. An example might be if you have CRealNumber. You can have functions that take real numbers as parameters and all they need to know is that they are real numbers. They don't care what kind of real number it is, that is not important.
*is a kind of*
Mystinar
December 5, 2004, 7:51 pm
I am still confused. But I am trainable. I can learn. Perhaps this will help with the battle system I am developing.
**Column**
Toolkit 3.x > TK3 Amelioration
Colin begins to explore the world of object orientated programming and its part in the future of RPG Code, using a custom battle system project that will be developed over the coming weeks to help illustrate the key concepts.
**Past Columns**
Feb 28, '05
Feb 13, '05
Feb 7, '05
Jan 30, '05
Jan 16, '05
Feb 28, '05
Feb 13, '05
Feb 7, '05
Jan 30, '05
Jan 16, '05
