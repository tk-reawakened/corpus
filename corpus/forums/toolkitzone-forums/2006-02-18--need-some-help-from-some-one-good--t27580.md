---
kind: forum-thread
id: "toolkitzone-forums/27580"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "27580"
title: "Need some help from some one good."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27580"
written: "2006-02-18T19:22:00"
last_post: "2006-02-25T23:13:00"
date_confidence: "exact"
captured: ["20060303102326"]
author: "femi"
repliers: ["slipknot42388", "Lisha", "vrn790", "DrakeLord", "DrJ", "Walker-san", "Dont_Think_So"]
authors: ["femi", "slipknot42388", "Lisha", "vrn790", "DrakeLord", "DrJ", "Walker-san", "Dont_Think_So"]
posts_present: 15
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_301117_amp_3Bsid_23600f9be0666c28742bdbbf47a91ce0", captured: "20060303102326", sha256: "934c0d4b274f54805c498fb4a0622516c501b6009cbae5fee39babc59691901a", wayback_url: "https://web.archive.org/web/20060303102326/http://toolkitzone.com/forums/viewtopic.php?p=301117&amp%3Bsid=23600f9be0666c28742bdbbf47a91ce0"}
links: []
---

# Need some help from some one good.

### femi · 2006-02-18 19:22 · #B299556

Question Question Question Question Dudes I'm a newb to editing rpgs but how the heck do i make my rpg like installable cause i have studied the whole of rpg toolkit know all the codes that i only need for the game(the rest of codes like variables and methods if told em to piss of).I just want to know that cause ive tested a really small crappy game made with the stuff u already get. it last 15 mins and i want to know how to make it installable so i can know how to do that when i make my real rpg Very Happy Razz Very Happy Very Happy Smile Sad Surprised Confused Shocked Mad

### slipknot42388 · 2006-02-18 19:27 · #B299560

you just go to the build thing at the top and click create setup. Oh by the way you should really look into the variables because with out those making a game woulb be pointless because you would be running on everything defult and that is boring Wink

### Lisha · 2006-02-18 19:28 · #B299561

**slipknot42388 wrote:**

> you just go to the build thing at the top and click create setup. Oh by the way you should really look into the variables because with out those making a game woulb be pointless because you would be running on everything defult and that is boring Wink
>

I agree. Variables are definitely needed to make something interesting. Plus default stuff is known to screw up like heck.

### femi · 2006-02-18 22:06 · #B299641

I sux at variables may be you or anyone else can give me a tip show me a code? Very Happy

### vrn790 · 2006-02-18 23:51 · #B299656

Obviously, you know the mwin command. Now, i'm gonna make a variable called Bob!
Code:
Bob! = 1
Mwin("I have <Bob!> cookies...")
Now the message window will show you a message. Instead of showing the variable, it will show you the number or word that the variable represents. So, the above example will show you: I have 1 cookies.
How is this usefull you ask?
well, consider this:
Name$ = prompt("Whats your name")
Mwin( "My name is <Name$>" )
This program is simple too. The variable is Name$. Heres something important about variables: a variable with a "!" at the end represents a number and a variable with a "$" at the end represents a word. In the above example, the prompt command will ask the player what their name is, and let them type something. When they type it and press ok, the name$ variable will represent the word(s) they typed. Then, i use the mwin command. This shows the player a message that says their name is whatever they typed in.
Theres a lot more you can do with variables, so you should explore them.

### femi · 2006-02-21 07:59 · #B300290

whats the point if u could just say soming like
mwin("i have one cookies instead of making it complicated")
wait()

### DrakeLord · 2006-02-21 13:13 · #B300309

Because you could be adding more and more cookies without you knowing where. Otherwise you would have to find out where you would buy the cookies, how many cookies the player will buy, etc.
With this you don't have to do nearly as much. It's not that complicated.

### femi · 2006-02-22 16:12 · #B300683

this is all to complicated that why i don't wanna try variables Evil or Very Mad

### DrakeLord · 2006-02-22 17:40 · #B300699

**femi wrote:**

> this is all to complicated that why i don't wanna try variables Evil or Very Mad
>

Oh come on. It's not that comlicated. Just study a little each day and you'll get the hang of it. It took me a week to figure out RPGcode and then another week to figure out while() loops (I still don't know Laughing ), Getting data, variables, etc.
Just keep at it. Once you've figured it out, your game will be so much better.

### vrn790 · 2006-02-22 20:55 · #B300750

Ok, i'll start with a very simple and very important example.
If( Something! == 1){
Mwin("You can cross the bridge")
}
If( Something! == 0){
Mwin("Talk to the old man first")
}
Now, this is a program you would put on a bridge. Basically, there is a variable called something!. This variable will normally equal 0. If you try to cross the bridge while it is zero, you will get a message that you have to talk to an old man first before you cross the bridge. If you talk to the old man, (you have to make a different program for that) the old man will make it so that something! equals one. Then you can go back to the bridge and it willl tell you that you can cross.
So, heres the basics:
If( Something! = 1){ Commands }
The "commands" can be any commands that you want. They will only happen if something! equals 1. Otherwise, they will be skipped.
If( Something! = 2){ Commands }
The "commands" can be any commands that you want. They will only happen if something! equals two. If both of these are put into a program, only one of them will make the commands happen, and the other one will skip the commands. This is because something! can't be both 1 and 2 at the same time.
So, lets say you want something to happen, but only when the player did something before that.
You would the commands in an if statement and the commands {} will only happen if the condition inside the parenthasis() is true.
here's the point of using variables
for the cookie thing, you can't make it simple like you said, because, how would you know how many cookies the player had?
consider this:
pretend you had a program you only wanted to run once. Like a treasure chest. The only way you could do this is with variables.
Example:
giveitem("hat.itm")
this will give the player a hat. BUT, this program will run over and over every time the player talks to it. What if you wanted the program to only give the player a hat once? You would use this code:
If ( hat! == 0)
{
giveitem("Hat.itm")
hat! = 1
}
Basically, notice that the command that gives the player the hat is inside of brackets. Above the brackets is an if command. This is simple. If the hat variable is equal to 0, then the commands inside the brackets happen, the player gets the hat, and the variable will equal one. If the hat variable doesn't equal 0, then all the commands in the brackets are skipped.
The first time you talk to this program, hat is zero, so you will get the hat. Then a command will change it to one. If you try to talk to the program again, hat is one now, so nothing will happen because all the commands in the brackets will be skipped.

### Lisha · 2006-02-22 21:06 · #B300758

Variables are also useful for things like custom stats. I, for example, am making a horse simulation game. I use variables when you train your horse. Whenever you train, it will add such and such number to such and such variable. The variable will always be changing, which is why I can't say "speed! = 2" or something.

### femi · 2006-02-23 15:32 · #B300983

man i will tryto tudy variable but its really hard.. Shocked

### DrJ · 2006-02-23 23:28 · #B301117

No varibles are really easy.
for example in a program you can set a varible to a value for example

**Code:**

```
random(2, setvarible!)

if(setvarible!==1){var!=true}

else{var!=false}
```

Then somewhere else you can check to see what a varible is, running a program accordingly.

**Code:**

```
if(var!==true)

{

mwin("The varible was set to true so this ran!")

wait()

mwincls()

}

if(var!==false)

{

mwin("The varible was set to false...")

wait()

mwincls()

}
```

Also
a $ varible is equal to a word, not a number. It can't be equaled to true or false you must use ! varibles for true or false or numbers.

### Walker-san · 2006-02-24 04:09 · #B301183

I'm just gonna ignore everyone else's posts. Don't get me wrong, they do have very good information and it is explained quite easily....I just wanna give my own variation that's all
Variables. A variable, short and simple, is one thing that stands for another. In algebra, the most common variable is 'x'. Using 'x' we can make an easy to understand equation like such:
x + 3 = 5
Using basic algebraic rules (which if you don't know I suggest hittin wikipedia and looking up. There aren't many of them and they are quite easy) we know that x = 2. That is the basics of variables.
Variables in coding take a slightly different turn. In RPGCode, moreso.
There are two different types of variables in RPGCode. Numerical variables can only store numbers and end in !. Let's take a quite look. Say you build a simple shop program that asks the player how many apples he wants to buy. It would probably look like this:

**Code:**

```
numapple! = prompt("How many apples do you want to buy?")

mwin("You purchased <numapple!> apples!")

wait()
```

So the program asks how many apples the user wants. The player enters a number...say 4. 4 is stored into the variable 'numapple!'. Then we can later call that variable to tell us how many apples were purchase, as in the the next message window. We could take this a step further and put those apples into the players inventory using a clever series of loops...ah hell, let's try it.
Okay, same program but with a loop to add the apples to the player's inventory. For my next example, I need to create a new variable for my while loop. Read the program and I'll try to explain with comments:

**Code:**

```
numapple! = prompt("How many apples do you want to buy?")

// So we have the same program as above minus a line.  The

// next part is a little more tricky, but still very basic

// programming.  Oh, in case you didn't know, these

// double slashes are for comments.  The program ignores em.

count! = 0

// I made a new variable that I called count.  This is used for the

// next portion

while(count! != numapple!)

  {

     giveitem("apple.itm")

     count! = count! + 1

  }

//  Okay.  I told my while command to keep looping so long as count!

//  did not equal to numapple!.  So let's say the player said he wanted 5

//  apples.  So long as count! isn't equal to 5 (the amount put into

//  numapple!) then it will keep repeating the program between the

//  brackets.  Inside the brackets, I put the giveitem command.  The

//  reason for the loop is that giveitem only gives 1 of an item.  count!

//  is set equal to count! + 1.  It'll add 1 to count! every time the loop

//  is repeated.  Once that is done, the program checks count! against

//  numapple! again, and if they equal each other, it will break the loop

//  and move on to the next portion of program.  This is slightly more

//  advanced coding, but essential nonetheless.

mwin("You purchased <numapple!> apples!")

//  That one line I removed I put here.  You could just as easily

//  kept it where it was, but for sake of order, I put it here.

kill(numapple!, count!)

//  The kill command is used to delete variables.  If it is a variable

//  you'll need for awhile...say the strength stat of a character, you

//  shouldn't kill it.  But in this case, we'll want to remove the

//  variables from memory as we don't need them anymore.

wait()

mwincls()

//  wait pauses and waits for a keyinput without adding it to a variable.

//  mwincls clears the message window.  Should be used often.
```

whew. a lot there. You don't need to worry about that right now if you don't want. That was more than I should have put. As you saw though, I could add to a variable. You can also subtract, multiply, divide, etc variables. You can also add two variables together like:
a! = b! + c!
Literal variables are a bit tougher. These bad boys contain what are commonly called strings. Letters and numbers can be entered here. They use the $ to signify they are literal variables. So we'll say:
charname$ = "Walker-san"
mwin("My name is <charname$>")
Easiest example. you can also add literal's together, but I'm not familiar with doing that. I find I've rarely needed to. I actually rarely use literal variables myself.
I think, and I'm not sure on this so don't quote me, that in the new version that our developers are hard at work on will no longer typecast variables and use one dynamic variable type...so this mess with ! and $ that we've been dealing with since TK version 1.4 will no longer apply. It's still good to learn the variables themselves, but just know that it's not going to be numerical or literal, but both. Something like that.
Edit: Runnin that biggy through the tk using the test feature results in a prompt then nothing. It's been....years since I've used rpgcode so I don't really know what I'm doing wrong here.

### Dont_Think_So · 2006-02-25 23:13 · #B301654

The not-equal operator in RPGCode is ~=, not !=.
