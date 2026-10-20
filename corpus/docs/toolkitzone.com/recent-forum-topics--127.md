---
kind: doc
id: "toolkitzone.com/127"
site: "toolkitzone.com"
title: "Recent Forum Topics"
original_url: "http://toolkitzone.com/library.php?mode=read&doc=127"
written: "2005-01-01T17:17:00"
date_confidence: "exact"
updated: null
captured: ["20060312120223"]
author: "matt72186"
repliers: []
authors: ["matt72186"]
comments_present: 0
f_author: "matt72186"
f_date: "January 1, 2005, 5:17 pm"
f_description: "Brand new series of weekly columns from Matt72186 all about using the new object-orientated features of RPG Code. Excellent layout with easy to follow sections and recommended links, no doubt these tutorials will prove invaluable to those expanding their knowledge to the world of classes."
f_title: "Introduction to Objects"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_127", captured: "20060312120223", sha256: "44b78426a850172bb9920b471633f90358cf80ff0780056f275cb8a6a06f04d1", wayback_url: "https://web.archive.org/web/20060312120223/http://toolkitzone.com:80/library.php?mode=read&doc=127&PHPSESSID=bdcceeefceef8ff863ad82d0d089ece4"}
---

# Recent Forum Topics

RPG Code Class 1
Introduction to Objects
Posted By: Disrupter Posted By: spitfire **Recommended Links**
**Recent Forum Topics**
Welcome to the first installment of a series of articles, in this series titled "RPG Code Class" I will guide you through various features of RPG Code, and their uses. I intend to teach by example. Every issue will present you with a complete code, and then it will break it down and explain to you the various portions of the code.
The first few issues will discuss a new feature in RPG Code: RPG Code , and using an RPG Code to create them.ObjectsClass
In this first issue I'll show a simple example of how to create and implement a . I'll introduce some new RPG Code keywords including class, object, public, and private. And some special types of methods called constructors and destructors.class
So that I don't confuse you too much, every issue will be styled in the same way. At the start of the article you can read an introduction to the lesson. In the top-right are external links to recommended sites for you to read relevant to the topic. If any new terms are introduced they will be briefly explained after the introduction in dictionary format. Immediately after is a chunk of complete code. Thereafter I will break up the code to explain each piece for you.
- A class in real life is simply a way to group (or classify) things, you do this unawaringly everyday. For example you may classify dogs as pets or apple as fruit, and then you may classify fruit as food. **class**
- An object is a thing. It is the thing you're classifying. If you make a class called Food, there can be a whole bunch of objects of the class Food, some of these objects are Apples, Chicken, Rice, Hamburgers. An object is one instance of a class. **Object**
- With relevance to a class, a method is pretty much what a class can do. If you have the class called Animal, you may give it a method of Eat, Sleep, and Drink. All of these an Animal can do. **Method**
- A property is what describes a class. Using Animal as an example again, you might describe an animal by it's color, size, species, etc... Anything that can be used to describe the class is a property of that class. Finally there is a conclusion to the issue. **Property**
```
- Animal Class
- Public Scope
- Method Animal(speakArg$)
- Method ~Animal()
- Method Talk()
- Private Scope
- Variable whatToSay$
- Animal class
- public:
- Animal Method ( ) speakArg$
- ~Animal Method
- Talk Method
- private:
- whatToSay$
- ///////////////////////////
- // Animal Constructor
- ///////////////////////////
- Animal Animal Method ( ) speakArg$
- this whatToSay$ speakArg$
- ///////////////////////////
- // Animal Deconstructor
- ///////////////////////////
- Animal ~Animal Method
- MWin ( ) "Yay, I'm free!"
- ///////////////////////////
- // My Animal Method
- ///////////////////////////
- Animal Talk Method
- MWin ( ) this whatToSay$
- ///////////////////////////
```
If you're thinking "what is all of this?" don't worry, it's normal, unless you've had previous experience with Object Oriented programming this shouldn't make much sense to you. At first glance you can probably figure out a few things, but let's take a look at this piece by piece and find out what everything means.
The purpose of this section of code is to create the . It's purpose is to design how the class will work before you even have the class do anything. Here is the code with added comments on each line. I'll translate RPG Code into plain english phrases that are easier to understand, and describe what the line is doing.class
```
- Animal class // I want to make a class named Animal
- public:
- Animal Method ( ) speakArg$ // This method is for when an Animal object is created
- ~Animal Method // When an Animal object is deleted, this method will run
- Talk Method // An Animal object can Talk()
- private:
- whatToSay$ // The only property an Animal will have is whatToSay$
```
As you can see nothing actually happens, here. It is just preparing for what's ahead, once you write down how you want your class to look like, the next step is to give it some life, actually code each method you gave to your class.
Here are the methods we defined earlier. The first is called Animal, that's the same name you gave to your class. There is a reason for this, this special method is called a Constructor, and just like it sounds, it's used to "Construct" an instance of Animal class. In this case when an object is created of your class, it will take speech$ as a value, and it will set the object's whatToSay$ to the same value of speech$.method
The second method here is called ~Animal, this is also for a reason. Similiar to the Constructor, it uses the classname in it's name, only there is a tilde (~) before the name. This special method is the opposite of the Constructor, and it is called the Deconstructor. When an Animal is released (when it is deleted from the program) it will display a last message that says "You destroyed me"object
The last method is called Talk, you could have called it anything you like as long as it's a valid name. This method can do whatever you want it to do, in this case it will show the object's whatToSay$ value in a Message Window, remember when we set the object's whatToSay$ earlier when it was being created. Every Animal object can have a different whatToSay$ depending on what you made it when you created the .Methodobject
```
- ///////////////////////////
- // Animal Constructor
- ///////////////////////////
- Animal Animal Method ( ) speakArg$
- this whatToSay$ speakArg$
- ///////////////////////////
- // Animal Deconstructor
- ///////////////////////////
- Animal ~Animal Method
- MWin ( ) "Yay, I'm free!"
- ///////////////////////////
- // My Animal Method
- ///////////////////////////
- Animal Talk Method
- MWin ( ) this whatToSay$
```
Now that we have the class completed, let's make an . Keep in mind, an object is just one instance of a class. Our class is called Animal, so let's make a few Animals and let them say different things when we make them Talk().object
```
- Animal Lion ( ) "Grr, I'm a hungry Lion"
- Animal Tiger ( ) "Rawr I'm a striped Tiger"
- Animal Bear ( ) "Roar! I am the ferocious bear"
- Talk Lion
- Talk Tiger
- Talk Bear
- release Lion
- release Tiger
- release Bear
```
Here we are first creating a Lion, a Tiger, and a Bear. Then we make the Lion talk, then the Tiger, and last the Bear. Each says it's own message. Then last we release each object, each will say one last message. Then they are gone! After you release an object all of it's methods and parameters disappear. If you tried to make the Lion talk again after you released it you would get an error.
Well that's all for this issue. Next issue we'll dig deeper into classes, and see more of what they can do! I'll also introduce some main concepts of Object-Oriented programming good things to get the hang of so that your code will be at it's best...
Well until next time folks, Code On!
Talyn
January 1, 2005, 5:28 pm
Good article. The layout's easier to follow than anything I've seen so far on OOP in RPGCode 3.
reignofmagic
January 1, 2005, 8:25 pm
RPGCode class and C++ class are almost the same. It's a great tutorial!
John@aljo
January 2, 2005, 9:13 am
please tell me next week we are gonna do some of that class hierchy. Is a and has a relationships :P. Believe me it is a wonderful subject to learn as it makes classes even more useful.
MrB
January 4, 2005, 5:29 pm
I'm still a little confused... and confused enough to not be able to apply this to my coding yet. I don't know if you were in a hurry or what, but it almost seemed like you were picking and choosing different things to explain. And you would start to explain something, and then kind of just stop. There's also a lot I'm assuming is correct by looking at the example, but I'd feel a lot more better if I heard you confirm all the assumptions. Here's a few questions... What's the :: for? What is "this->"? Where did you ever get speech$ from? I never saw it in any of the code, but you kind of just threw it out there. I don't really understand public and private either. Isn't it all private unless you show it to the player...? And please do try to make sentences, not just long run-on's... it's hard following long statements with just random commas thrown in.
Xavier
January 7, 2005, 11:49 am
"What is "this->"?" The same as it is in PHP. It references the class and -> denotes what it is accessing. class->variablename class->methodname "this" means the class the method is within. "this class" basically.
spitfire
January 9, 2005, 1:15 pm
Good tutorial, but I have the same questions as Xontu does..... ::? speech$?
Moo Of Doom
January 11, 2005, 3:12 am
:: is just syntax to denote that that method belongs to that class. speech$ is a typo that's supposed to be either whattosay$ or speakarg$. Nice article, by the way.
Allan@Aljo
January 25, 2005, 4:46 pm
**Column**
RPG Code > RPG Code Class 101
Brand new series of weekly columns from Matt72186 all about using the new object-orientated features of RPG Code. Excellent layout with easy to follow sections and recommended links, no doubt these tutorials will prove invaluable to those expanding their knowledge to the world of classes.
**Past Columns**
Jan 8, '05
Jan 8, '05
