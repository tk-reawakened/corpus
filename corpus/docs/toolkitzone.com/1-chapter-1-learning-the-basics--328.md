---
kind: doc
id: "toolkitzone.com/328"
site: "toolkitzone.com"
title: "1. Chapter 1 - Learning the Basics"
original_url: "http://www.toolkitzone.com/library.php?doc=328"
written: "2009-11-22"
date_confidence: "day"
updated: "2009-11-22"
captured: ["20100314231204"]
author: "Marz"
repliers: []
authors: ["Marz"]
comments_present: 0
f_author: "Marz"
f_description: "Adds"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__doc_328", captured: "20100314231204", sha256: "5060dffafb6edf8978a946ef0b2e8d9aa4e4b5d0379174883b5651ec35070678", wayback_url: "https://web.archive.org/web/20100314231204/http://www.toolkitzone.com/library.php?doc=328"}
---

# 1. Chapter 1 - Learning the Basics

Browse
**1. Chapter 1 - Learning the Basics**
*I am in no way an expert, and the way this tutorial is written in no way implies that this is the correct way to code, nor is it the most optimized method.*
Chapter 1 - Learning the Basics
- Introduction
- Variables and Scope
- Variable Manipulation
- Naming Conventions
- Commenting
- Conclusion
Introduction
RPG Code is the scripting language used by the Toolkit in order to achieve anything from a simple message window to something as complex as a fully functional battle system. Given its flexibility, RPG Code can be relatively difficult to understand. Achieving basic features found in games for those without knowledge of other programming languages will be at a loss on how to structure their program files. This tutorial aims to remedy that by providing some knowledge on programming and using RPG Code syntax.
Variables and Scope
If you were to do calculus without variables, it would be pretty useless. Using variables is essential in any programming language you will learn, but understanding when and how to use them (as well as how they should be named) are important matters.
: a quantity that can assume any one of a set of values, such as text and numbers. **Definition - Variable**
: the name of a variable. **Definition - Identifier**
You can imagine that a game without variables would be very dull. Everything would be constant: a player's fight power would never change, there would be no "trigger events" (e.g. you can only go to the Deku Tree if you are wielding a sword and shield - that can't happen without variables), etc. In 3.1.0, we no longer have to worry about the "type" of a variable. That is, the Toolkit will now determine whether the variable is numeric or literal (contains a number or combination of letters). There are some apparent advantages here (like being easier), and if you were programming with previous versions of the TK you will no longer have to use functions like castLit(). Anyway, onto the actual code. In RPG Code we seek to define a variable with a name (identifier) as well as its value. We end the statement with a semi-colon ( ; ). Think of this semi-colon as the period at the end of a sentence, where each sentence needs one to be considered a complete statement. x = 1; y = "Thing"; Here I've created a variable, given it the name "x", and assigned it a numerical value of 1. What actually happens in your computer is the compiler allocates this special space in memory for a value, then it puts the value you assigned (1, in this case) to that memory space. It will stay in that space until the of your program ends. Similarly y gets a literal value "Thing" and the same thing happens. One thing to understand about variables is how long they "live" in memory. In other words, depending on how and where you declare a variable, it could live the entire length of the game, or for only a few seconds. A variable's lifetime is called its scope. : The boundaries in which a variable is accessible.
*scope*
**Definition - Scope**
**
Definition - Local Scope : The variable's boundaries are local to the prg file after which it is initialized : The variable is accessible to all program files in the entire game, provided it is initialized correctly. Understanding the scope of your variables can help keep your code neat and allows you to reuse common variable names in other programs. It is important to have a firm foundation on how scope works, otherwise you could be trying to access a variable that is no longer there. For instance, suppose I have created a local variable called "text". I use this variable throughout the prg file and everything is fine. Then in another prg file I attempt to access this same variable, but the compiler has no idea what I'm talking about. This is a failure to understand the scope of my variable "text" (Do you understand why?). Scope will become more important when we get into some later chapters of this tutorial, where determining whether a variable is global or local is a strategic decision that could make programming your game easier or harder. I'll delve a little further into it in this chapter, but its power becomes clear in the next chapter. Until then, here's some basic syntax on how to declare a variable with a certain scope: local (x); global (y);
**Definition - Global Scope**
Variable Manipulation
The ability to manipulate variables is what makes them dynamic. Manipulating variables is similar to algebra in many ways. We can manipulate a variable using some very basic and familiar techniques. It should be easy for you to understand what the following does: a = 8; b = 4; c = a + b; In case it's not obvious, the variable c here is now set to 12. One thing to note, however, is the order in which I set up the code. Suppose I had this instead: a = 8; c = a + b; b = 4; What would happen? In the RPG Code sense, b would be equal to 0, and thus c would be 8. In other more strict languages (such as C++) you would receive an error because b had not been initialized yet. Luckily the Toolkit catches this mistake and fixes it for you (for better or for worse). The point of this example is to make sure that variable you are trying to access is available in the scope.
Table 1: operators for numerical variable manipulation
**Operator**
Adds
Multiplies
Subtracts
Divides
The + operator seen above is very common in math and it's safe to say that by the age of 5, everyone has some concept of addition of numbers. In programming, the + operator can be used for several other things as well. For example, we can concatenate to strings using the + operator: a = "Hi"; b = "there"; c = a + b; The result here sets c to "Hithere". This probably isn't what we wanted, most people would want a space between the two words. Thus it is required for you to space out the variables yourself. So a solution to this problem is: a = "Hi "; Notice the space after Hi before we end the quotation mark. Perhaps another niffty feature is the ability to concatenate strings on the fly. Suppose you asked for the player to input a character name at the beginning of the game, and saved it in a variable called charName. Later on in the game, his best friend wants to talk to him: message = "Hi there " + charName + "!" Assuming charName was Vampz, the message would say "Hi there Vampz!" While the + operator can be used with literal variables (also called strings), we cannot use the other operators listed in Table 1. That is, the following will give you "garbage" results (in computer jargon, garbage means something useless): a = "High"; b = "Hi"; c = a - b; d = a * b; e = a / b; In case you're wondering, c and d will give you 0, and e will give you "-1.IND"... in other words, pure garbage :). Also, if you're wondering how to check what a variable is, use the following: show(x); wait(); Where x can be any variable. We'll go over more about functions at a later date.
Naming Conventions
You'll notice in several of my above examples, I used letters of the alphabet as names of different variables. While this is fine for purposes of such simple examples, it can become quite hard to read code for large games when the variable names are a1, b1, a2, b2, etc. It is important to give variables a meaningful name that's not too long and easily understood. Recall from an earlier example that I used the variable charName for the character's name used in the game. Let's compare this variable name with some other alternatives: charName cName characterName name cheese The only other decent alternative could be cName. The other alternatives either make no sense (cheese), are too vague (name), or are too long (characterName). You'll also notice that with each variable that had two "words" in it, the first word is all lowercase, while the second word has its first letter capitalized. Which one is easier to read: 1. charName 2. charname I certainly hope you think it's the first one, and even if you don't, most people still choose the first one anyway. It is a common naming convention used. Another convention used are for constant variables. A constant is a variable that never changes (or should never change), and its value is determined at the time of initialization. An example of a constant is pi. When naming a constant, we usually use all capital letters, so: PI = 3.14159; What happens if the constant is more than one word though? Well, then we use an underscore (_): ARRAY_SIZE = 10; In RPG Code, there is no definitive way of declaring a constant, so having the name as all uppercase reminds you not to change its value throughout the program. There are many other naming conventions out there, but for now these should be sufficient for what we will be programming.
Commenting
When you start programming your game you'll realize it's going to take forever to finish. This of course means several breaks that could go on for months on end while you start another project, play other video games, or take a vacation. When you come back, you're staring at possibly 100 different prg files. All of a sudden your left with daunting task of figure out what you were trying to accomplish in the program you've written way back when. Using the naming conventions above, you can develop a good understanding of what you're doing to each variable on each line. But sometimes code gets complicated. Complicated enough that basic English should be used to explain what's going on. If we write basic English in our program, we'll get an error because Toolkit doesn't understand English (it understands RPG Code). However, the toolkit does understand how to ignore something: b = 2; //Set b equal to the value 2 In this line of code, the compiler will perform b = 2; as it normally would. Then it sees //, and ignores the remainder of the line. This allows us to write "comments" about our code after the //. Of course, be careful of where you're commenting, because you usually don't want to comment out code (unless you think it's causing an error) like this: // b = 2; Set b equal to the value 2 Here we just commented out the entire line, so b = 2; will never get executed. Sometimes we'd like write a little bit more than one line of code. One way to do this is: // First line // Second line // Third line Thankfully, there is an alternative: /* First line Second line Third Line */ Everything in between the /* and */ is ignored by the toolkit, safely allowing you to write paragraphs of comments. Before I conclude the first chapter, I've failed to mention how/when you should comment. Paragraphs of comments are undesirable, as it might be easier to just read the code. Similarly, the comment above for b = 2; is unnecessary, as it should be pretty obvious what the statement b = 2; does. Comments should be reserved for complex logic in your programs that you know you or someone else will have trouble understanding later. Do not riddle you're entire program file with comments, and at the same time make sure there is adequate commenting to understand the more difficult lines of code.
Conclusion
This marks the end of the first part of this tutorial. Please leave any questions below, or notify me of any mistakes I might have made. I do apologize if this reads too much like a textbook, that's all they make you read in University.
**1. Chapter 1 - Learning the Basics**
[![TBD](thumb.php?src=forum/images/avatars/1788411534695c477a77d1.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=16450)
Great tutorial. This definitely helps to explain 3.1 RPGCode for beginners. Keep it up!
[![TBD](thumb.php?src=forum/images/avatars/9872561424b5ab1f09a7f9.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=14726)
Nice tutorial, covers a lot of basic mistakes in code posted in Newbie Haven or RPG Code. I'm adding this to my signature, maybe I'll get less private messages now...
Make one on OOP. Do it. Please. (Good stuff, by the way.)
TBD
[![TBD](thumb.php?src=forum/images/avatars/49198935143f50e086344d.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=5812)
Nice set tutorials. Are there going to be more in the near future?
[![TBD](thumb.php?src=forum/images/avatars/4668018904a48e8254cff8.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=12580)
nice tut marz, it gave me the memory goose i needed to get started on my project.
[![TBD](thumb.php?src=forum/images/avatars/3136116234b4f9f03dc1fe.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=16904)
This helped me out a lot. Thanks Marz.
[![TBD](thumb.php?src=forum/images/avatars/1165717839484c50c7a8325.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18499)
b = 2; //Set b equal to the value 2 In this line of code, the compiler will perform a = 2; well so far the first half bored me but thats only because i already knew all of that although i took a look at the end and had no clue what was going on so it will get better well at least for me for someone that didnt read the help files this would be a great place to start
TBD
TBD
idk about anyone else but i dont understand jack here marz this is explained in a really complex way i mean ive read this over and over and dont understands where ur going with lease bear with us average iqs :S
[![TBD](thumb.php?src=forum/images/avatars/86425383345de15b08496f.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=33)
Kidanis, out of curiosity how old are you/what level of high-school are you at? I didn't know exactly who my audience was when writing this tutorial because of the wide range of ages at the Toolkit Zone, and have evidently aimed this at the older crowd. Also, it would help if you told me what you didn't understand. "The whole thing doesn't make sense" isn't very constructive and I'm not about to rewrite the entire tutorial.
well im actualy 19 and im starting college but i just dont get the whole thing its like expresed in a way that not everyone would understand but i apreciate the effort ill keep reading on ill get it eventualy im just a moron when it comes to coding or programing im more of a graphics creation type myself
[![TBD](thumb.php?src=forum/images/avatars/86425383345de15b08496f.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=33)
Ah I see, well then I would advise reading my examples rather than the supporting text. When I first started programming, I didn't learn anything until I started dissecting the examples and trying code out myself. The text books you're about to read in college may be very similar in writing style to this, though... at least that's my experience.
This tutorial was really helpful; brilliant, really Thanks a miillllliooon!TBD
Havent looked at this in a while, plenty of new "chapters", I'm psyched.
[![TBD](thumb.php?src=forum/images/avatars/1503375594838d0f18836f.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18657)
thanks a bunch i hope you add more to this tutorial soon its been a big help
[![TBD](thumb.php?src=forum/images/avatars/8249348634649df41066d8.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=16496)
Awesome Marz!! I've been stuck on programming for so long, and after reading just the first chapter through, I was able to finally get it right! THANKS for doing this for us Newbies!
[![TBD](thumb.php?src=forum/images/avatars/16092367784831044cd4260.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=19885)
WOW well this is my first post so Hello all I've never seen any type of codes like these before and I have to say it's going to take a little time befor I can understand most of it but I usealy learn fast I was able to read and understand 1 to 5 and thanks for the text book readabuls
[![TBD](thumb.php?src=forum/images/avatars/19651451634946a0cc8b905.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=16982)
Very informative, it's helped me out a great deal! But right now I'm stuck with the Custom Mwin Check Point #1. ^^; I've read the chapter several times, yet I still haven't figured out how to make an image for the window. I've tried the drawCanvas() function a couple of times, and it works, but not to the extent I'd like. The image is stretched to fit the entire screen... and I don't know how to resize it to match the original size. I'm a total beginner, so if you could help me out, I'd really appreciate it. Just enough to get an idea, at least. I still want to learn for myself!
TBDTBD
[![TBD](thumb.php?src=forum/images/avatars/86425383345de15b08496f.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=33)
Check out the setImage function: http://tk3.toolkitzone.com/help/?page=19#setimage You don't need to use canvasses in that chapter, so don't worry about that too much. You'll realize why your drawCanvas method worked when you approach the canvas chapter.
[![TBD](thumb.php?src=forum/images/avatars/19651451634946a0cc8b905.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=16982)
Wow, I used this help file too, and just skimmed right past this. ^^; I guess I have to keep my eyes open a bit wider. Thanks Marz!TBD
[![TBD](thumb.php?src=forum/images/avatars/39905036498b662f0aef0.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=7931)
Awesome man. Should help a lot of people.
This is very nice
[![TBD](thumb.php?src=forum/images/avatars/20303561264ab1310bc4b88.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=94)
There are a couple things I noticed about the sections on objects that no longer apply in 3.1.0: Colin added a rudimentary garbage collector in 3.1.0. It runs at 10 minute intervals and cleans out objects that are no longer referenced by identifiers. This includes local vars that go out of scope, objects (even objects that belong to other objects), and arrays. Note that you still have to clean up and call release() yourself when you need to free memory allocated by plugins, canvases, cursor maps, etc. But for the most part you no longer need deconstructors. (Edit: It's also important that the GC won't call an object's deconstructor, it just frees "unbound" memory.) Instead of copy constructors (and the confusing "the first parameter doesn't do anything here" work around), it might be better to implement a copy(obj) function. I don't think copy constructors are actually a feature anymore -- because objects are always references, a copy constructor is never called unless you "force it," and that looks a little awkward. or feels a lot more natural to me.
Quote:
> With objects we cannot rely on the RPG Toolkit to get rid of them due to their complexity, and must call the destructor of the object ourselves.
>
TBD
Quote:
> copy constructors < snip >
>
*y->copy(x)* *x = y->copy()*
[![TBD](thumb.php?src=forum/images/avatars/86425383345de15b08496f.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=33)
RPG Code is generally a stepping stone for most users to other programming languages. Most people in the community are in some way interested or connected to computer science. Thus, I will keep the tutorial the way it is (doing your own garbage collection, copy constructors). However that is a very interesting tidbit on the 10 minute garbage collector. Thanks for the clarification OC
TBD
[![TBD](thumb.php?src=forum/images/avatars/142552219748dbe07f4d146.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=22869)
wow this helps a lot thanks keep up the good work.. us noobs need to start somewhere...TBD
That sure was a lot of information... I'm going to assume it's going to be useful, because I'm a complete newbie at this sort of stuff, but I think it'd be really neat to do. I'm trying, I'm trying... The way it was written was a bit confusing-ish, but I was able to understand it.
[![TBD](thumb.php?src=forum/images/avatars/95488741049ff61d231616.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=16981)
Looks like a great tutorial, will be defiantly reading soon!
[![TBD](thumb.php?src=forum/images/avatars/14822159884964ee3ea67ae.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=23755)
Great tutorial, this is just what I need to get on track with RPGCode programming. I've been enjoying the journey so far, but the toolkit does have a high learning curve. It's great to have another resource to learn the more difficult aspect of the program.
[![TBD](thumb.php?src=forum/images/avatars/185782029149cb95212c449.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=24442)
Nice tutorial! You explain it really well.
[![TBD](thumb.php?src=forum/images/avatars/17143353354936769651b69.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17430)
Nice! Even better than the ones in the help files! Because of this, I've understand how to use classes. Thanks a bunch! =3
[![TBD](thumb.php?src=forum/images/avatars/14854132954b537a0474677.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=27392)
The Mercenaries thing is something i have been trying to find a way to do FOREVER! THX! ------- If only i could focus long enough for the rest of the tut.....
TBD
Quick Jump
Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Editorials | -- Zone Awards | -- | -- 2008 | -- | -- 2009 | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
Keyword(s)
All Categories Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Editorials | -- Zone Awards | -- | -- 2008 | -- | -- 2009 | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
![Click for more details.](forum/images/avatars/86425383345de15b08496f.jpg)
**Published**
September 7th, 2008
**User Rating**
![TBD](templates/default/images/icons/rating_blue_5.gif)
*47 votes cast.*
**Views**
1608
Contents
Who's Online: , , , , , , [amv93](community.php?user=25718) [ASHBAD_ALVIN](community.php?user=28124) [Geep4W](community.php?user=13474) [jackyboy](community.php?user=17184) [Jon](community.php?user=16904) [Longelis](community.php?user=27495) [TropicalStar](community.php?user=28117)
