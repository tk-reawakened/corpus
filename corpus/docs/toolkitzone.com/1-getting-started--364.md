---
kind: doc
id: "toolkitzone.com/364"
site: "toolkitzone.com"
title: "1. Getting Started"
original_url: "http://www.toolkitzone.com/library.php?doc=364"
written: "2008-04-06"
date_confidence: "day"
updated: "2008-04-06"
captured: ["20080511004619"]
author: "crazydrivr"
repliers: []
authors: ["crazydrivr"]
comments_present: 0
f_author: "crazydrivr"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__doc_364", captured: "20080511004619", sha256: "ce64b46dd781e229b0f665b5ece97920d88e803df684bded6e8653cb54d26642", wayback_url: "https://web.archive.org/web/20080511004619/http://www.toolkitzone.com/library.php?doc=364"}
---

# 1. Getting Started

Browse
**1. Getting Started**
This tutorial was written and designed around the RPG Toolkit 3.1.0. So I have returned to the toolkit after leaving for a while. I know that classes are a hard concept to grasp, although it is barely harder than methods are, if any harder at all.
Just in case you don't know how to use methods here is a quick tutorial for them, although I would hope that you already know how to use methods before coming here. Anyway, methods are basically an organization of commands that can be called with one line of code. Take a look at this example code:
>
> method talk() { mwin("talking"); wait(); mwincls(); }
>
To use methods start with the keyword method. Then type in the name of the method, preferablly not one that is already in the toolkit (like pixeltext). After that put an open and a close parenthesis. Add an open curly brace '{' after that, then all of the code that will be run, then a closeing curly brace '}'.
Now if you run this, you will notice it won't show anything on the screen. That is because talk() wasn't called. In order for this to work you need to call talk(). That is easy all you have to do is add the new command you made 'talk()' anywhere in the program, like the very top.
Look at this new code that does work:
>
> talk();
>
> method talk() { mwin("talking"); wait(); mwincls(); }
>
This is just the basics that you will need to know to get by in classes or OOP. For more on methods go . [here](http://www.toolkitzone.com/library.php?doc=328&page=5)
Now on to OOP (Object Oriented Programming). As mentioned earlier OOP consists of things called classes. Like methods which are a grouping of commands, classes are a grouping of methods. OOP uses objects of a class. This way you can have multiple classes stored at once. The cool thing about OOP is that variables made are specific to it object. Lets look at this simple class that does the same thing as the talk() command above.
Start a new program, or delete the methods one if you followed along with that above.
>
> class talk { public: //constructor method talk(); private: //we will talk about this later }
>
Now once again if you run this, it won't do anything. Before we make it actually work, lets talk about the preceeding code a little.
Instead of starting with the keyword method, start with the keyword class. Then add the name of the class you a going to make. I used talk again. This time however, it doesn't have parenthesis. Once again use the open curly brace '{'.
Now as I said earlier, classes are a grouping of methods. You can see that I have the method talk() under the public: section. Now public: says that the methods stated there can be called from outside of the class. This is a concept that may take a few times to get.
Lets continue with forming this to work. There are two big problems with this code.
1: the method talk() has no code in it at all. If we were to call it, there would be no code to run. 2: there is no way to call the class right now.
Lets start with the first problem. There are two ways to go about this. I will go over both ways.
One way to fix this is to take off the semicolon on 'method talk();' and make it work by adding code and treating it just like you normally would a method.
>
> class talk { public: //constructor method talk() { mwin("talking"); wait(); mwincls(); }
>
> private: //we will talk about this later }
>
This way would work if you had shorter methods, but when you start getting in to larger classes, you will probably want to do this the second way, as shown below.
>
> class talk { public: //constructor method talk();
>
> private: //we will talk about this later }
>
> method talk::talk() { mwin("talking"); wait(); mwincls(); }
>
So wait hold on just a second, this isn't that hard. So if you take off the part method talk::talk() and everthing after that, you will notice that we already saw this above two code sections ago. I am going to go line through line of all of the lines here. We already talked about the class talk line. It just states that we are using a class called talk.
Then we have the word public: which we haven't gone through yet. It is to specify that you can use the method talk() outside of the class. If it is in the private: then it can't be seen from outside the class.
Now the line //constructor is indeed a comment. I would hope you already knew that, but it is important to go over. I put that there because the method talk() is a constructor. Who would have guessed!? Anyway, constructors MUST have the SAME name as the class. As you can see the class and the method have the same name. Why you ask? When you first use the class, you call it's constructor. You may have more than one constructor, but they must have different amounts of parameters in them. We will hit this later as well.
We already talked of private: so lets hit the line 'method talk::talk()'. This is actually an easy command to use. First start with the keyword method. After that use the name of the class. Then use the '::' operator. After that use the method name that you are going to add the code for. So speaking in terms of how things are organized, you would define a method in the class like this:
>
> method :: () { //code here }
>
A note about using this form, you must have the line up in the public: section and declare all parameters in it there.
Using this form you can make up all of the methods in a class. Of course for the constructors, the will be the same as the .
After even all of this, we still don't have any code that will produce any output. So now that we have covered problem 1: talk() not having code, lets learn how to make an instance of the class. This will cover problem 2 that we had much eariler.
>
> variable = talk();
>
> class talk { public: //constructor method talk(); private: //nothing is private yet }
>
> method talk::talk() { mwin("talking"); wait(); mwincls(); }
>
Lets run through how this works. Everything from class talk down is the same exact code you have seen in the other examples above. But now, we have a line above that, 'variable = talk();'. With this line, we make a new variable, or much more correct, an object of the talk class.
Now at first look, you may think that 'variable = talk()' is calling the whole class of talk. That isn't exactly correct. It actually runs the constructor of the class talk. If you were to add a line of code like 'mwin("test")' just above 'private:' you would find that it wouldn't be called. That is because basically everything involved in a class should be done through methods (hence the small methods tutorial at the beginning of this tutorial).
so 'variable = talk()' basically runs the method talk(). Now why would you go through all of this work, just to have it run a method? That is something that I will get into later, but it will make it so that if you have to adjust a lot of variables/settings, it will actually shorten code quite a bit. It is kind of like an exponential curve. At first it will not show any real benifits and might even be a worse choice in the long run, but as you start adding a whole lot of commands for the class, it will become much more effective.
Now when will you ever use this talk class? You probably never will again. So lets start working on a custom cursor map shall we?
Don't go off thinking at this point that you have learned everything there is to know about classes. We don't even know how to make a method that ISN'T a constructor yet. There is a different form to calling it than the simple = sign. Look at this line of code
>
> var->setup();
>
Have you ever seen this before? This is just a pointless example to show how to run all methods from a class that aren't constructors. We will hit this topic again later, lets take a look at the beginnings of our custom cursor class.
>
> myCursor = cursor();
>
> class cursor { public: //constructor method cursor();
>
> private: //variables for the class should almost always be in the private section myX; myY; myWidth; myHeight;
>
> image; }
>
> method cursor::cursor() { //Initialize variables here myX = 100; myY = 100; myWidth = 17; myHeight = 17;
>
> image = "mwin.jpg"; }
>
So once again, we don't have any code here that produces any output. All it does right now is initialize five variables. Now you might be thinking, why would you put the variable names up in the private: section, without assigning them, then later assign them in a method? Technically you don't need them in RPGCode, but you do in other languages. So it is good coding habit.
Lets talk about what each variable will do so far. myX will be the x position for the cursor map, the myY variable will be the y position of the cursor map, myWidth will be the width of the cursor map, and likewise, myHeight is the height. Image is the file to use for setting the image later.
We have a slight problem here though. We have an x value and a y value for the cursor maps. So what if we have more than one cursor? When I mean more than one cursor I mean more than one item to choose with the cursor, not literally two cursors running at the same time. For example, lets say you are making a menu. There is more than just items in the menu. There might be save, quit, magic, continue, etc. So anyway if we set the x value for the first cursor, what do we do with the second cursor? If we just overwrite it, then we no longer have the first one in memory. This is where arrays come in.
**1. Getting Started**
[![TBD](thumb.php?src=forum/images/avatars/49198935143f50e086344d.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=5812)
A long, but nice tutorial.
[![TBD](thumb.php?src=forum/images/avatars/182121120446f07bb466f32.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=13049)
Thanks Auron. So if anyone has any questions/suggestions for how I can improve this tutorial, just PM me.
Quick Jump
Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Editorials | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
Keyword(s)
All Categories Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Editorials | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
![Click for more details.](forum/images/avatars/182121120446f07bb466f32.jpg)
**Published**
April 6th, 2008
**User Rating**
![TBD](templates/default/images/icons/rating_blue_2.5.gif)
*4 votes cast.*
**Views**
Contents
Who's Online: , , , , , , , , , , [Bad Kids](community.php?user=335) [Bagel](community.php?user=4798) [Baphomet](community.php?user=18078) [Colin](community.php?user=226) [DrJ](community.php?user=5307) [jmandiablo](community.php?user=18876) [k-hos](community.php?user=13905) [Mineat](community.php?user=17691) [Mr Picso](community.php?user=3699) [Sharmandra](community.php?user=7502) [zyrshnikashnu](community.php?user=254)
