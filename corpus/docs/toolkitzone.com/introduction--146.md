---
kind: doc
id: "toolkitzone.com/146"
site: "toolkitzone.com"
title: "Introduction"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=146"
written: "2005-01-15T11:34:00"
date_confidence: "exact"
updated: null
captured: ["20051226053659"]
author: "Occasionally_Correct"
repliers: []
authors: ["Occasionally_Correct"]
comments_present: 0
f_author: "Occasionally_Correct"
f_date: "January 15, 2005, 11:34 am"
f_description: "OC revisits the popular and much sought after territory of custom stats for your characters, using the more recent additions to the Toolkit such as structures and classes."
f_title: "Organizing Custom Stats"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_146", captured: "20051226053659", sha256: "7d228c0fcd4924b65971e232652ea0dc05d749511077d232e711e860d31fd11f", wayback_url: "https://web.archive.org/web/20051226053659/http://www.toolkitzone.com:80/library.php?mode=read&doc=146&PHPSESSID=3a8877fdee63b0dcd9b5eb3ae54264d2"}
---

# Introduction

Hi there. OC here, and today I'll be revisiting a subject that I covered months and months ago in a tutorial -- custom stats. Since there have been big changes made to the TK since that tutorial, I thought it appropriate to re-do it. This time, however, you will learn how to keep them organized through the use of structures and classes. Having custom character/enemy stats in your game is always a nice way to add a special touch to your game. However, having all those global variables for your characters stats can get a little out of hand and unorganized. Here, you'll find out a nice way to keep your custom stats tightly packed and organized. The first step for organizing your stats is using a structure. Structures are used to group data together and recall it for later use. In this case, we're using a structure called PLAYER, which groups together the stats for the players. This structure contains all of the stats we'll be using, and will be used for all of the various characters. You can save it in file, calling it player.prg or something. It's not very useful right now, though, because it can't do anything. To make some use out of it, we'll have to create an object for it. If you don't know what objects are, you can check out Matt's . You'll want to put this in your start program somewhere that is sure to be run (a good place would be in your history() method, assuming you're using one). Of course, you'll want to assign values to the rest of the stats too, so don't forget those. Obviously, structures can't hold methods (even if they could, it would be irrelevant to have them there). This is where classes come to play in custom stats. Classes are like structures, except they can hold methods, restrict data, and many other things. You'll want to design a CPlayer class for use with custom battle systems (which I assume you'll try writing, if you want to use custom stats). And that's the class. The first method inside is the constructor, which is called each time an object is created from the class. It takes one parameter - player - of type PLAYER. This allows us to pass the object we made from the PLAYER structure into the method. From here, we get the stat variables from the object and store them in the private variables of the class. The next method is the copy constructor -- a special method that is called for things like passing objects as parameters by value, returning objects, etc.. It takes one parameter (rhs) of type CPlayer. All the method does is copies the data from rhs to private data. However, you may be wondering why there's a line saying, "if (this! ~= rhs!)." Well, 'this' is the same as saying 'this class,' basically. So, "if this is not equal to rhs." Next, we have overloaded operators. The first just returns the players name (allowing you to do things like this: text(1, 1, object) and have it show the players name). The second is the assignment operator. Every class should have this overloaded operator if it has a copy constructor. This does the same thing as the copy constructor, but is used in different places. Now, we have a levelUp() method, which raises the players stats. Next, we have a whole bunch of 'get' methods. Those are self-explanatory. Lastly, the private data. These variables are used to store the players stats temporarily. Here's an example of putting this class to use (let's say it's saved in our player.prg file, along with the PLAYER struct): Alright. A lot is happening in this example. First, we include the player.prg and system.prg files (system.prg is needed, as we're using the CArray class). Then, we create two instances of the PLAYER structure - Bob and Joe. We then assign values to some of their stats. Next, we create an array with 2 elements (0 and 1). Then, we create two instances of the CPlayer class, assigning them to the fighter array. We pass the Bob and Joe objects into the CPlayer constructor, so their stats will be stored in the fighter object. Finally, we show some of the stats and call the release() method on fighter, deleting it from memory (since fighter's destructor calls release() for each of the elements, we don't need to release the individual elements). Well, that's been the article for article for today. I hope you enjoyed it and learned something new from it. I might extend this at a later date to include a CEnemy class/struct and some more methods. If you want to use this class for a battle system, all you would need to do is add an attack() method, passing an enemy class object as it's parameter, and handling all the stats there. Of course, you could also write your own classes for this. If you have any comments, suggestions, or questions, you can ask them here, or PM me via the forum. **Organizing Custom Stats**
**Introduction**
**Organizing stats with Structures**
```
struct PLAYER
{
name$ // Players name
hp! // Hit points
maxhp! // Max hit points
mp! // Magic points
maxmp! // Max magic points
att! // Attack points
def! // Defense points
level! // Level
exp! // Experience
expNeeded! // Experience needed for the next level
}
```
```
Bob = PLAYER()
Bob->name$ = "Bob"
Bob->hp! = 50
Bob->maxhp! = 50
//etc...
```
**So, what's next?**
```
class CPlayer
{
public:
// Constructors
// Constructor
method CPlayer(PLAYER player!)
{
m_name$ = player->name$
m_hp! = player->hp!
m_maxhp! = player->maxhp!
m_mp! = player->mp!
m_maxmp! = player->maxmp!
m_att! = player->att!
m_def! = player->def!
m_level! = player->level!
m_exp! = player->exp!
m_expNeeded! = player->expNeeded!
}
// Copy constructor
method CPlayer(CPlayer rhs!)
{
if (this! ~= rhs!)
{
m_name$ = rhs
m_hp! = rhs->getHP()
m_maxhp! = rhs->getMaxHP()
m_mp! = rhs->getMP()
m_maxmp! = rhs->getMaxMP()
m_att! = rhs->getAtt()
m_def! = rhs->getDef()
m_level! = rhs->getLevel()
m_exp! = rhs->getEXP()
m_expNeeded! = rhs->getNeededEXP()
}
}
// Operators
// Returns m_name$
method operator$()
{
returnMethod(m_name$)
}
// Assignment operator
method operator=(CPlayer rhs!)
{
if (this! ~= rhs!)
{
m_name$ = rhs
m_hp! = rhs->getHP()
m_maxhp! = rhs->getMaxHP()
m_mp! = rhs->getMP()
m_maxmp! = rhs->getMaxMP()
m_att! = rhs->getAtt()
m_def! = rhs->getDef()
m_level! = rhs->getLevel()
m_exp! = rhs->getEXP()
m_expNeeded! = rhs->getNeededEXP()
}
}
// Methods
// Level up
method levelUp()
{
//Display a message
mwin(m_name$ + " has leveled up!")
wait()
mwincls()
//Raise the stats
m_maxhp! += 3
m_maxmp! += 2
m_att! += 2
m_def! += 2
m_level!++
m_expNeeded! += (m_expNeeded! / 2) + 100
}
method getHP()
{
returnMethod(m_hp!)
}
method getMaxHP()
{
returnMethod(m_maxhp!)
}
method getMP()
{
returnMethod(m_mp!)
}
method getMaxMP()
{
returnMethod(m_maxmp!)
}
method getAtt()
{
returnMethod(m_att!)
}
method getDef()
{
returnMethod(m_def!)
}
method getLevel()
{
returnMethod(m_level!)
}
method getEXP()
{
returnMethod(m_exp!)
}
method getNeededEXP()
{
returnMethod(m_expNeeded!)
}
private:
// Private data
m_name$
m_hp!
m_maxhp!
m_mp!
m_maxmp!
m_att!
m_def!
m_level!
m_exp!
m_expNeeded!
}
```
**The full example**
```
// Include the needed programs...
#include "player.prg"
#include "system.prg"
// Create an objects for the PLAYER structure
Bob = PLAYER()
Bob->name$ = "Bob"
Bob->maxhp! = 50
Bob->level! = 1
Joe = PLAYER()
Joe->name$ = "Joe"
Joe->att! = 15
// Create an array with the CArray class
fighter = CArray(1)
// Pass CPlayer objects into the array
fighter[0] = CPlayer(Bob)
fighter[1] = CPlayer(Joe)
// Show some stats
show(fighter[0]) // Output: "Bob"
show(fighter[0]->getLevel()) // Output: 1
show(fighter[1]->getAtt()) // Output: 15
wait()
// Get rid of the array
fighter->release()
```
**Conclusion**
vrn790
January 19, 2005, 9:01 pm
I found a small mistake in this, GetHP() and GetMaxHP() are actual rpg code commands so the methods won't work. Great Tutorial Though!!
Occasionally_Correct
January 20, 2005, 8:25 am
Actually, they will. You can create methods that are the same name as commands as long as you provide a different list of parameters. It's explained in the 'method overloading' section of the help files. :) Also, classes seem to be able to use command names for methods even if they do have the same parameters. For example: class CTest { public: method mwin(text$) { mwin(text$) } } test = CTest() test->mwin("Hello!") wait() test->release() That will work. It'll print 'Hello!' to the screen as you would want it to. If you wanted to get the method to call itself, though, you'd do this (don't, though. It's endless recursion. :p): class CTest { public: method mwin(text$) { this->mwin(text$) } } test = CTest() test->mwin("Hello!") wait() test->release()
stanleywuu
January 20, 2005, 3:40 pm
My question is Where did this CArray come from? I don't see it in my default system.prg I get an error saying that CArray is not found and my game just terminates
Occasionally_Correct
January 20, 2005, 3:52 pm
Are you using the System.prg file from TK3.0.5? If it doesn't have classes in it, it's an older version. You might want to go into the 'Basic' folder ('rpgtoolkit3\games\basic\') and take the System library from there. There's also a file in there called SystemDemo.prg, which is just an example of putting some of the system classes to use.
stanleywuu
January 20, 2005, 4:07 pm
It's weird....I don't see CArray in the system.prg in the basic folder, but in the systemDemo.prg, there is a line where they used CArray I'll download TK3.0.5 again then Thank you
vrn790
January 20, 2005, 5:54 pm
Overloaded [] operator must return a reference to a variable-- Character[Pos!] I get this error when I do Character = CArray(3) Character[Pos!] = CPlayer(Vadim) It still works though, so I use Debug("off") and leave it at that.
stanleywuu
January 21, 2005, 11:35 pm
Hm........they seem to take pretty long to load, how can I make it faster? Are they suitable for menus at all? Because it takes like two seconds for the next thing to show, I suspect that TK is taking data from the class, even if I use canvas, it'd take a while to wait and display everything at once
vrn790
January 29, 2005, 5:12 pm
I add menu methods into my class that call the stats directly from within the class. This speeds it up a lot.
Pests
January 30, 2005, 11:32 pm
"Obviously, structures can't hold methods" Only in RPGCode, seeing as how C++ can and all.
Colin
July 8, 2005, 2:12 pm
C++ doesn't have structures. The C++ 'struct' keyword creates a class that defaults to public visibility. C has structures, and they cannot, in fact, contain methods.
**Column**
RPG Code > Tips & Tricks
OC revisits the popular and much sought after territory of custom stats for your characters, using the more recent additions to the Toolkit such as structures and classes.
**Past Columns**
Feb 18, '05
Feb 11, '05
Jan 29, '05
Jan 8, '05
Dec 31, '04
Feb 18, '05
Feb 11, '05
Jan 29, '05
Jan 8, '05
Dec 31, '04
