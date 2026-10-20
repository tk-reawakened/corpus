---
kind: forum-thread
id: "toolkitzone-forums/12313"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12313"
title: "Global and local variables"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12313"
written: "2004-12-08T07:05:00"
last_post: "2004-12-11T22:37:00"
date_confidence: "exact"
captured: ["20041227215358"]
author: "Levi"
repliers: ["Occasionally_Correct", "Chamgorie Chanbear", "Colin", "Dont_Think_So", "solaceinsilence", "p90m16mp5a4"]
authors: ["Levi", "Occasionally_Correct", "Chamgorie Chanbear", "Colin", "Dont_Think_So", "solaceinsilence", "p90m16mp5a4"]
posts_present: 10
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_138175_amp_", captured: "20041227215358", sha256: "780133a531d09c58b12bb1e7cc14c76968294c5e1559354611c750117e5c2fff", wayback_url: "https://web.archive.org/web/20041227215358/http://www.toolkitzone.com/forums/viewtopic.php?p=138175&amp="}
links: []
---

# Global and local variables

### Levi · 2004-12-08 07:05 · #B136416

Okay. I'm not quite sure about how this all works. How do you define local and global variables? Are variables only local if defined in a method? Or do you actually have teh ability to determin which ones are local and global. Is there a difference as of yet?
Has TK3 changed how these work from TK2?
Just wondering. I wasn't able to find specifics in the help files. I probably missed something but I had to ask in case I didn't.

### Occasionally_Correct · 2004-12-08 14:34 · #B136465

I'm pretty sure there's a scope section in the currently released help files. Though, I've written a longer one for the next release:

**Quote:**

> Scope:
> When you create a variable in a program, it automatically sets itself to "global scope". "Global scope" means that the variable can be accessed from any program in your game unless you Kill() it. That means that if you have a variable called 'box!' that stores the number 5 in one program, you can still access that same variable through a different program. This is because global variables stay in your computers memory until you Kill() them or your game is ended.
> So, how do you make it so that your variables aren't always global? Well, there are two commands for this specific issue: when you want to create a variable of "local scope", all you need to do is use the Local() command. "Local scope" means that the variable can only be accessed by the program that it's created in, and it will be destroyed when the program ends, freeing up memory. Here's how you use the Local() command:
>
> **Code:**
>
> ```
> //Let's create a local variable called 'box' and
>
>
> //assign it the value 5...
>
>
> Local(box!)
>
>
> box! = 5
>
>
>
>
>
> //Now, let's show the contents of this variable...
>
>
> Show(box!)
> ```
>
> Once that program ends, the local variable 'box!' will be destroyed. If you try to access it through another program, the value will be 0 because the variable doesn't exist anymore.
> The second command you can use is AutoLocal(). This command takes it a step further by making local scope the default scope for variables. That means that all variables created in a program will be local, unless you use the Global() command to create a global variable.
>
> **Code:**
>
> ```
> //Make all implicitly declared variables local...
>
>
> AutoLocal()
>
>
>
>
>
> x! = 2 //A local variable
>
>
> y! = 8 //Another local variable
>
>
> Global(z!) //A global variable
> ```
>
> Scope isn't restricted to "normal" variables, however. Classes and methods also have scoping rules of their own. For example, when you declare a Local() variable inside of a method, the variable is destroyed when the method ends. The same thing happens with the parameters of a method. They're destroyed when the method ends, making it easier for you (since you don't have to kill() them).

### Chamgorie Chanbear · 2004-12-11 18:06 · #B138043

But what's the point of declaring a local variable? Does it save memory or something? Other than that I can't see the use. (In all my newness to RPGCode I know I'm probably wrong but please respond seriously anyway)

### Colin · 2004-12-11 18:29 · #B138052

You make them local because globals are pure evil.
The whole idea of object oriented programming is to protect all data with functions, globals destroy this ideal.

### Dont_Think_So · 2004-12-11 18:33 · #B138053

In other words, yes, one reason is to save memory. Another reason is to protect data from use in a totally innappropriate case.
For example, it wouldn't be very efficient to declare the done! variable as global then use it in all of your while loops, because then at some point you are going to have them interfere with eachother. That's not a very good example, but I'm try to stick with simplicity without going into classes.

### Colin · 2004-12-11 18:36 · #B138056

You make them local to avoid name conflicts too. Every level of a recursive call has its own scope so it can have the same vars with different names, for example.

### solaceinsilence · 2004-12-11 20:14 · #B138091

Well another reason is because there really isn't any reason to declare a variable Global when you are only using it in a certain method or section of code. A good rule to know when you use Global and when to use Local is this:
You know you need a Global variable when you need to access it from another method. Otherwise make it Local.
By default in RPGCode, all variables are declared Global unless you declare then with the Local() command. Oh and don't forget to use the Kill() command to remove the variable from memory when you are done using it. If you don't variables will build up in memory and eventually your game will crash because of lack of memory.

### Occasionally_Correct · 2004-12-11 20:26 · #B138097

**solaceinsilence wrote:**

> By default in RPGCode, all variables are declared Global unless you declare then with the Local() command.
>

You can also use AutoLocal().

**Quote:**

> variables will build up in memory and eventually your game will crash because of lack of memory.
>

I doubt someone will have that many variables in their game. Razz

### Dont_Think_So · 2004-12-11 22:14 · #B138164

**Code:**

```
For(x!=0;x!>=0;x!++)

{

AnotherVar[x!] = x!

ColorRGB(Random(255),Random(255),Random(255))

Text(4,4,"I am the memory-eating monster! RAWR!")

}
```

Mmmm... memory...

### p90m16mp5a4 · 2004-12-11 22:37 · #B138175

Ok.. so I'm ina battle yah.. and I have two dudes wearing the same armour only with one as CArmour ANd Parmour, (not really just example) can i use local so that i can use Armour for both my computer and player? Testing the local command is like number 20 on my list so if someone knows it would save me a bit of time ^^
*is currently developing game by himself...*
