---
kind: doc
id: "toolkitzone.com/36"
site: "toolkitzone.com"
title: "column"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=36"
written: "2004-11-21T23:17:00"
date_confidence: "exact"
updated: null
captured: ["20041216141627"]
author: "Colin"
repliers: []
authors: ["Colin"]
comments_present: 0
f_author: "Colin"
f_date: "November 21, 2004, 11:17 pm"
f_description: "The opening column in Colin's TK3 series details the design fundamentals that underpin programming, thus rpg code in its new age - especially when you factor in the forthcoming class system in the next 3.x release."
f_title: "Design Fundamentals"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_36", captured: "20041216141627", sha256: "2a3f196fb1611a4c199db3663950c3ca5aa560d42a0a77f5174e2338e83fe05a", wayback_url: "https://web.archive.org/web/20041216141627/http://www.toolkitzone.com/library.php?mode=read&doc=36"}
---

# column

Toolkit 3.x > TK3 Amelioration
The opening column in Colin's TK3 series details the design fundamentals that underpin programming, thus rpg code in its new age - especially when you factor in the forthcoming class system in the next 3.x release.
**TK3 Amelioration I – Design Fundamentals**
**Preface**
It has been a good year for version three of the RPGToolkit, herein referred to as TK3. It has risen from a virtually unusable state to a condition in which it stands to surpass versions fore. In this column, I plan to discourse information of coming features, speak of widespread concerns, and, of course, talk about, and practically apply some of the new RPGCode features you’ve been hearing about but just can’t fathom a use for. Like every good column write says, your input is welcome, and I will answer any questions you pose. If all goes as planned, you’ll be seeing this column every Monday; I hope you thoroughly enjoy the read.
Being as this is the first article in the series, it’s only fitting to lay down the foundation for subsequent writings; in the case of a column revolving around the betterment of a game creation system, this entails the excitement known as design fundamentals. While most of the information on this page will be tailored toward the coding aspect of the RPGToolkit, it can and should be taken much more abstractly. Without further adieu, thanks to that wonderful segue, we now proceed into the bulk of the article.
**Abstraction**
Regardless of whether you choose to accept it, abstraction is something that is all around us in day to day life. That is, the process of ignoring the details and focusing on what is essential to you. We watch television without worrying about how the program is sent to our terminal; we change the channel not caring how the television talks to the stations providing us with the correct one. The viewers just want entertainment; the advertisers just want their product known, the actors just want to perform, and the broadcasters just want a subset of it all to themselves. These fundamentally related parties need not worry about the operations of each other, nor do they worry about the underlying device which keeps them interconnected; they focus on what is important to them.
The computer is another blatant example of abstraction. Consider two identical computer programs, one written in assembly code, another in C. The assembly program must contain very explicit instructions so the computer knows exactly what to do. Details like commands to multiply numbers, however, are often distracting to the underlying functionality of the program. C hides this detail with a multiplication operator so programmers need not be distracted with subtleties which obscure from the purpose of the program. Even assembly is hiding details from you by enabling you to use the base ten number system, though, because the designers of assembly believed it was not realistic for programmers to perform casual math in binary.
**Procedural Abstraction**
As the name implies, procedural abstraction allows us to ignore details about processes that we invoke. When we use the ) command in RPGCode, a message window appears holding the text we request. But does it do that? How does the computer interpret the commands we demand it execute? RPGCode is a very high-level language because it abstracts what happens at a very high level. When you call ), program flow will trail through VB, a language built on Windows, which was coded in assembly and C. This will then trickle through hexadecimal byte strings ultimately to be changed to binary and evaluated by the CPU. Of course, this all happens so fast that it’s difficult to imagine it happening at all. MWin( *how* MWin(
While you could code every showing of the message window in assembly, simply calling a command to do it for you does much more than save you typing. It makes the program easier to understand hiding details that are unimportant. How the message window is shown is not what is important – what’s important is it shows a message window. Functions like MWin() make large programs simpler by allowing you think of your program as a set of logical operations, rather than a list of steps for the computer to perform. RPGCode—through methods—allows you to further abstract the steps you execute by enabling you to call your own sets of logical operations rather than thinking about the process every time. *that*
**Data Abstraction**
Another form of abstraction—data abstraction—provides you with means to ignore how data is represented in memory. All computer data can be viewed as binary numbers but it is rare that we think of them as such. All RPGCode numerical variables are eight byte—64 base two “bit”—numbers. How these bytes are stored in memory and how math on them is performed is not important to the RPGCoder. These variables can hold decimals, arithmetic can easily be done with them – that is what matters.
While almost all programming languages provide means to evaluate equations of floating points, literal variables are not as common. RPGCode provides a string data type that enables the RPGCoder to add strings in a fashion similar to numbers, using the addition operator; languages like C do not have this feature and force the coder to think of strings as bytes occupying consecutive memory locations. Data abstraction frequently also involves procedural abstraction – I don’t know how floating points are divided, nor do I care.
**Conclusion**
Abstraction is the basis of structured programming languages like RPGCode, previous to the upcoming version 3.05. Abstraction allows the coder to focus only on what is important and ignore the details, thus visualizing a program as a set of logical operations rather than a list of instructions. This is a concept integral to understanding when, where, and why we use classes – a concept, object oriented programming, I’ll likely discuss next time.
Talyn
November 22, 2004, 1:16 am
Thats brilliant. It's true, you never think about how much goes on behind the scenes when you use such a simple command as Mwin. Look forward to seeing this column every week Colin!
John@aljo
November 22, 2004, 3:59 am
Much like a Computer Theory class that makes you awwe and wonder about how the whole comeputer works. I look forward to the next article which explains more about the abstraction that we can make occur.
Colin
November 22, 2004, 4:19 am
Whether or not that was sarcasm, John, hopefully you weren't bored from your mind. I plan to talk about object oriented programmingencapsulation, the process that enforces abstractionnext time, along with providing some practical examples in response to post. [this](http://toolkitzone.com/forums/viewtopic.php?t=11543)
Colosseus
November 22, 2004, 11:36 am
So... RPGCode is based on Visual Basic which is based on C which is based on Assembly... Seems like a lot and even more, but it's actually not that hard to comprehend if you really think about it. And it's definately a good thing that it is that way too - it would be unnecessarily difficult to type 01000001 every time you wanted to write an A. Can't wait to read your next submission!
Colin
November 22, 2004, 2:44 pm
VB is based on Windows, which is written in C and assembly. I'm not sure what VB is written in, so I didn't try and guess :P
Alex0Xander
November 22, 2004, 5:30 pm
o.~ I'm famous! I'm studying Game Art and DEsign, but it doesn't hurt to learn some code right =P
oblivious_casualty
November 30, 2004, 3:39 pm
it's really weird to think that programming languages can be coded in other programming languages. so abstraction is the process of ignoring what exactly happens, and lets us focus on what we need to do?
Dec 12, '04
Dec 6, '04
Nov 28, '04
Dec 12, '04
toolkit 3.x > tk3 amelioration
Dec 6, '04
toolkit 3.x > tk3 amelioration
Nov 30, '04
rpg code
Nov 28, '04
toolkit 3.x > tk3 amelioration
