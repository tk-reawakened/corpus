---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/tutorials/coding/creating-a-turn-based-battle-system/like/"
site: "rpgtoolkit.net"
title: "May 22nd, 2010"
original_url: "http://rpgtoolkit.net/tutorials/coding/creating-a-turn-based-battle-system/like/"
written: "2010-05-22"
date_confidence: "day"
updated: null
captured: ["20111203113717"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/tutorials/coding/creating-a-turn-based-battle-system/like/index", captured: "20111203113717", sha256: "6b5db5dc90575d61e3e135af0e32bb20db1dc039d7d63a46ab9285c54a9b3242", wayback_url: "https://web.archive.org/web/20111203113717/http://rpgtoolkit.net/tutorials/coding/creating-a-turn-based-battle-system/like/"}
---

# May 22nd, 2010

[![aurum34](thumb/80/community/images/avatars/upload/177759702449f4701b4f43f.png)](member/aurum34/)
Published
**May 22nd, 2010**
Read times **4,470**
Written by aurum34
Creating A Turn-Based Battle System
**Aurum34's own step-by-step guide to making your own simple turn-based battle system.**
1. Introduction
2. Day 1
3. Day 2
4. DAY 3
5. day 4
Creating A Turn-Based Battle System
Introduction
This is a tutorial on how to make a simple turn-based battle system (BS). In this tutorial I will basically be creating my own BS and detail how it works , advice on how to customize things, and los of sample code for you to study and try out.
Of course, this is not the only way of going about making such a BS so if you don´t like how I've done some things or if you prefer a different technique then you´ll make me even happier! I just want to give you an idea on how things should work together so that you can go on to make your own.
When all the sample codes are brought together there should be an entire BS but remember that this is the core structure . I will not address additional things like status effects. So take it slowly , follow every step, and study the code to really learn everything you need to know.
**Requirements**
Since creating a BS from scratch is something that total newbies typical can't get their head around, I´ll quickly summarise the core understandings needed to achieve good custom systems with RPG Code.
- "if" structures
- loops
- canvases
- functions/methods
- structs
With an understand of these core concepts, you're ready to start building some pretty cool things.
**Thankings**
What´s a Toolkit resource without a segment thanking the members of the community that helped test and correct some of my English flaws. I have to thank them or their ghosts will probably hunt me forever *shaking*
- Dave the Hamster - He requested a BS, so I created this tutorial. Actually, I shouldn't give him credit for asking for a BS otherwise I'll have to give credit to every newbie here!
- Hannibal - Helped me by reading this and telling me on the things I should add/change.
I'll divide the tutorial by days. So, have fun!
Creating A Turn-Based Battle System
Day One
So, you want to make your own turn-based battle system with the RPG Toolkit? Of course you do, why else would you be reading this anyway?!
**Assets**
The first thing you have to concentrate on is planning and preperation.
You will have to create your own animations as you can´t use Toolkit´s due to the fact they only run one animation at a time so if you need everybody to run a single animation at the same time, like on multiple-target attacks, then the default animations can´t help you.
There are several things to plan;
- Animations
- Players
- Enemies
- Special Moves
- Interactions
And maybe more if you want to add more features, but let's keep it simple for now.
**Variable Trick**
A trick I use when I want to use a single variable to hold several values is to use strings and then split them, if there are numbers inside the string I use castnum() to get the values. This can be applied as a method, for example:
>
> debugger(add("4,85,69")) debugger(add("452,895,653,845,675,415,182,478,352,645"))
>
> method add(numbers) { split(numbers, ",", num[]) //this will split the numbers by the commas local(n)=0 local(answer)=0 until(num[n]=="") //go through all numbers { answer=answer+castNum(num[n]) //convert the num[] string to a number and add it to the answer n++ //go to the next number } return answer }[
>
When you run this code you´ll notice that all of the numbers are inside a string and that this means they are held in a single variable name. So no matter how many numbers we add we only need to use one variable to pass them as a parameter.
We will use this trick to make an animation. An animation need several frames so we will use this string of values to run a sequence of frames.
>
> anmIdl="0.05,frame1.png,frame2.png" RunAnm(anmidl, 20, 20, 64, 64)
>
> Method RunAnm(anm, x, y, width, height) { savescreen(2) split(anm, ",", anm[]) local(n)=1 until(anm[n]=="") { restorescreenarray(2) setImageTransparent(anm[n], x, y, width, height, 255, 255, 255) delay(castNum(anm[0]))//anm[0] is speed as string so i use castnum to make it a number n++ } restorescreenarray(2) n=0 //now the clean up until(anm[n]=="") { kill(anm[n]) n++ } kill(n) }
>
You may be wondering what the 0.05 before the frames is, right? Well, that´s the speed of the animation so you can open the animation editor, make the animation there, then copy the speed and the frames to a program like this one.
**Customisation**
Now it´s your time to shine - look at what I did here and maybe make your own simple animation method.
Creating A Turn-Based Battle System
Day Two
What we should do now is make structures for the players and the special moves. We shouldn't combine custom variables (speed, dex, ...) with default variables (fp, dp) because that could cause confusion at a later time, so let's just make all the structures now to start getting familiarized with them.
**Player Structure**
You just have to put the basic animations and variables you want to use and you're done. But also leave some methods for the menu options, if your player will have the options attack, special, run, then leave 3 option methods like I did. Put all the methods all the players will need, for example, if you have a player whose options on the menu will be "attack,special,run" and anotherone with "range,summon,run", the put the methods range, attack, summon, special and run, because you'll need them, for now they'll not do anything, but it's important to put them to know what we need to do.
>
> // i use struct to avoid accessing errors struct Player
>
> method Player(n, h, m, siz, spd, str, def, tec) // constructor, study classes
>
> name = n; // the animations will be setted with another method
> hp = h;
> maxhp = h;
> mp = m;
> maxmp = m;
> size = siz;
> speed = spd;
> strike = str;
> defense = def;
> tecniques = tec;
>
> ethod attack() // methods to be implemented later m
> ethod special() {}
> ethod run() {}
> ethod killPlayer() {}
> ethod PlayerMenu() ethod selectOption(option) {}
>
> // attributes
> name;
> hp;
> maxhp;
> oldhp; //this is to keep track of the changed hp
> mp;
> maxmp;
> size; //width and height of the animations
> menu; //string with the names of the options.
> speed; //speed variable
> anmIdl; //frames for idl animation
> anmAtk; //attacking
> anmCast; //casting SMove
> anmBlk; //blocking
> anmHrt; //hurt
> anmFrame; //current frame of the animation.
> anmSpeed; //this will handle the animations, explanation on day 3.
> strike; //um.. self-explanatory isn't it?
> defense; //you HAVE to know what is this for
> tecniques; //I'll use a string and split it to call the tecniques
> plx;
> ply; //location of the player
>
Now that the player structure is done you have to remember to use it, everytime you add a new player to the party you have to create a new player variable, and of course, remember to create the first player.
To create the players you just call the player() method inside the structure, thatway you can give a value to some of the variables, but the animations are another story, you'll have to call every animation variable and set it by yourself, but since the player[] will be a global variable, you don't have to worry about doing it again, just do it once and you're done.
Now let's make a player from the first playerHandle[] you have.
>
> #include "bsclass.prg"; //include the program were you saved the structure.
>
> Global(player[playerHandle[0]]) = Player("name", gethp(playerhandle[0]), getsmp(playerhandle[0]), 32, 1, getfp(playerhandle[0]), getdp(playerhandle[0]), "");
>
As you can see, we basically just called the player() method inside the structure and gave a value to the parameters of the player() method. Then the information is stored inside player[playerHandle[0]] global variable, so we don't have to do this again.
But now, we only gave a value to some of the variables inside the structure, we have to gave a value to everything to be done with it, so we have to call the variables one-by-one and give them values.
>
> #include "bsclass.prg"; //include the program were you saved the structure.
>
> Global(player[playerHandle[0]])=Player("name", gethp(playerhandle[0]), getsmp(playerhandle[0]), 32, 1, getfp(playerhandle[0]), getdp(playerhandle[0]), "");
>
> player[playerHandle[0]]->anmIdl="0.5,idlframe1.png,idlframe2.png";
>
> player[playerHandle[0]]->anmAtk="0.2,Atkframe1.png,Atkframe2.png,Atkframe3.png,Atkframe4.png";
>
> player[playerHandle[0]]->anmCast="0.8,Castframe1.png,Castframe2.png,Castframe3.png";
>
> player[playerHandle[0]]->anmBlk="0.08,Blkframe1.png,Blkframe2.png,Blkframe3.png";
>
> player[playerHandle[0]]->anmHrt="0.5,Hrtframe1.png,Hrtframe2.png";
>
Now this player is completely done because all of it's variables are setted, remember that everytime you add a new player for the first time you have to create a variable like how I did it here, make it global since otherwise you'll have lot's of bugs, and remember that if you take away the player from the party the variable will still be there, but the battle system won't use it because it goes between the members of the party.
**Enemy Structure**
As you can see by the player structure, the enemy structureneeds the same variables for the animations, so let's make the enemy structure, with all the variables we need.
>
> struct Enemy
>
> method Enemy(n, h, m, siz, spd, str, def, tec) // constructor
>
> name = n; // animations will be sett differently
> hp = h;
> maxhp = h;
> mp = m;
> maxmp = m;
> size = siz;
> speed = spd;
> strike = str;
> defense = def;
> tecniques = tec;
>
> ethod attack() {} m // methods to be implemented later m
> ethod killEnemy() {}
>
> name; // attributes
> hp; // to kill it
> maxhp; // in case it heals itself
> mp; // in case I want to steal it!
> maxmp;
> exp; // experience it will give you
> reward; // maybe an item?
> gp; // money!!
> size; //width and height of the animations
> speed; // speed variable
> anmIdl; // frames for idl animation
> anmAtk; // attacking
> anmCast; // casting SMove
> anmBlk; // blocking
> anmHrt; // hurt
> anmFrame; // current frame of the enimation
> anmSpeed; // this will handle the animations, explanation on day 3.
> strike;
> defense; tecniques; // I'll use a string and split it to call the tecniques
> enex;
> eney; // location of the enemy
>
You have to create enemies almost the same way as players, but the advantage is that you can just make methods to create every enemy andcall that method as many times you want instead of making global variables that will consume space of memory.
If we are going to make a ghost as an enemy, we can create a method that creates the ghost with all of it's animations and variables.
>
> Method ghost()
>
> local(ghost)=Enemy("Ghost", 200, 15, 32, 2, 20, 40, "");
>
> ghost->anmIdl="0.5,enemyes/ghostidl1.png,enemyes/ghostidl2.png";
>
> ghost->anmAtk="0.6,enemyes/ghostAtk1.png,enemyes/ghostAtk2.png,enemyes/ghostAtk3.png,enemyes/ghostAtk4.png";
>
> ghost->anmCast="0.05,enemyes/ghostCast1.png,enemyes/ghostCast2.png";
>
> ghost->anmBlk="0.4,enemyes/ghostBlk1.png,enemyes/ghostBlk2.png";
>
> ghost->anmHrt="0.15,enemyes/ghostHrt1.png,enemyes/ghostHrt2.png,enemyes/ghostHrt3.png";
>
> return ghost;
>
See? We created a method that makes a ghost by setting it's variables and animation, now we save this inside a program called "bsEnemy.prg" and we create all of the methods that creates enemies there, this will allow us to do something like
>
> #include "bsEnemy.prg";
>
> ene[0]=ghost();
>
> ene[1]=ghost();
>
> ene[2]=ghost();
>
Easy right? Just calling that method makes the enemy creation easier, and that's what we need, make things as easier as we can.
**Special Moves Structure**
Now, let's make the powers that you can call whenever you want.
>
> struct SMove
>
> ethod SMove(pwr, mpc, lvl, typ, anm, w, h)
>
> level = lvl;
> animation = anm;
> anmWidth = w;
> anmHeight = h;
> MPcost = mpc;
> Power = pwr;
> type = typ;
>
> ethod Action()
>
> level; //required level
> animation;
> anmWidth; // width of the animation
> anmHeight; // height of the animation
> MPcost;
> type; // to be explained later
> Power; // base power, to be increased with stats
>
Not much to say here, the special moves are almost the same as players, global variables, the only difference is that you have to put the name of the SMove inside the array to make it easier to call. But you can create your own way to call them from the bs, this is just one way to go.
>
> #include "bsClass.prg";
>
> local(FLAnm) = "0.1,flare1.png,flare2.png,flare3.png,flare4.png,flare5.png"
>
> Global(Tecniques["flare"]) = SMove(80, 12, 20, 2, FLAnm, 32, 32)
>
Just make it that way to make it easier to call from the player structure, I'll explain more about special moves on day 5 but for now this is enough for you to start making your SMoves.
*NOTE: Save all the structures in 1 prg file and the rest of the BS on another*
You have to make now the player structure and the special move structure, with these done, the battlesystem can start taking shape tomorrow. Take your time to figure out all the variables you want to put and all the commands you want to add to the structures. When you're done, take a rest and continue the tutorial, today was all about structures, so if there's something you don't understand, look for it because the rest of the BS will use these strucrures on every code, so if you have ANY doubts you should try to solve them before reading any further.** Customization
AND THAT WAS DAY 2!
Creating A Turn-Based Battle System
Day Three
This day will be focused on explaining the custom animation system that will be used for this BS.as you should know, the definition of animation is: several static images passed one after another, so to do the animations we have to just keep drawing images to the screen.of course, we have to clean the previous image, and still considerate that we have to handle lots of players and enemies, so when changing to a new frame, the rest should stay the same, to do this, I´ll use canvases.
If you´ve ever made a hp bar program you´ll know that canvases are perfect to change only one little part of the screen with a lot of speed, if you haven´t you´re about to learn it. So let´s start with a simple code using the custom animation explained on day 1.
>
> idlAnm="0.05,frame1.png,frame2.png,frame3.png";
> runAnm(idlAnm, 20, 20, 32, 32);
>
> Method RunAnm(anm, x, y, width, height)
>
> local(c)=createCanvas(width, height);
> split(anm, ",", anm[]);
> local(n) = 1;
>
> until(anm[n]=="")
>
> clear(c);
> setImageTransparent(anm[n], 0, 0, width, height, 255, 255, 255, c);
> drawCanvas(c, x, y);
>
> delay(castNum(anm[0])); //anm[0] is speed as string so i use castnum to conver it to float
>
> n++;
>
> n=0; //now the clean up
>
> until(anm[n]=="")
>
> kill(anm[n]);
> n++;
>
> kill(n);
>
*NOTE: from now on, you have to "manually" put the animations for the enemyes, this is done by calling the variable inside of the structure that is meant to hold the animation and giving it the value.*
>
> ene[0]=Enemy("Goblin", 10, 4, 32, 1, 3, 3);
>
> ene[0]->anmIdl="0.05,frame1.png,frame2.png"; //don´t leave spaces
>
> ene[0]->anmAtk="0.15,atkframe1.png,atkframe2.png,atkframe3.png";//and so on with all the animations
>
If you understand this you can totally tell that this is what you need, let´s just use a canvas for each player and for each enemy, the canvases must be created at the beginning of the battle and eliminated at the end so let´s start making the setupBattle method to create and draw the basic layout of the battle when it starts and let´s start anotherone to kill those canvases after the battle is done.
The setupBattle method is to put a basic layout of the battle system, draw the names of the enemies, put the background, play the music, and make the canvasses for every player and enemy on the fight. Also, it has to put the first frame of the idl animation of the players and enemies so.... It´s all going to look a lot like the following
*NOTE: from now on the players will be player[playerHandle[n]], kinda like playerHandle[n]. And the enemies will be ene[n].*
In addition the canvases for the players will be named CPlayer[playerHandle[n]] and the canvasses for the enemies will be Cene[n]
>
> method setupBattle(background, music)
>
> bitmap(background);
> mediaplay(music);
> local(n)=0 // let´s put the players;
>
> ntil(player[playerHandle[n]]=="")
>
> // first we save the player´s x and y location.
>
> player[playerHandle[n]]->plx=120+(castInt(n/2)*20);
>
> player[playerHandle[n]]->ply=250+(n*50)-(n*75);
>
> // now we create the Canvas for this player, take the // first frame of the idl animation, draw it to the.
>
> // canvas and draw the canvas ti the player´s x and y // location and save the moment with getTickCount.
>
> CPlayer[playerHandle[n]]=createCanvas(player[playerHandle[n]]->size, player[playerHandle[n]]->size);
>
> split(player[playerHandle[n]]->idlAnm, ",", anm[]);
>
> setImagetransparent(anm[1], 0, 0, player[playerHandle[n]]->size, player[playerHandle[n]]->size, 255, 255, 255, CPlayer[playerHandle[n]]);
>
> drawCanvas(CPlayer[playerHandle[n]], player[playerHandle[n]]->plx, player[playerHandle[n]]->ply);
>
> player[playerHandle[n]]->anmSpeed=getTickCount();
>
> player[playerHandle[n]]->anmFrame=1;
>
> // now we just put the name of the player on the screen // and step to the next player
>
> setImage("menuimage.png", 25+(20*n), 25+(22*n), getTextWidth(playerHandle[n])+10, getTextHeight(playerHandle[n])+10);
>
> pixelText(30+(20*n), 30+(22*n), player[playerHandle[n]]->name); //here is the name of the player
>
> n++;
>
> n = 0;
>
> until(anm[n]=="") //from this point it´s just clean-up memory leaks
>
> kill(anm[n]);
> n++;
>
> n=0 ;
>
> until(ene[n]=="") // now the enemies, let´s do the same.
>
> ene[n]->enex=400+(castInt(n/2)*20); // let´s save the location
>
> ene[n]->eney=250+(n*50)-(n*75); // to use it later
>
> Cene[n]=createCanvas(ene[n]->size, ene[n]->size);
>
> split(ene[n]->anmidl, ",", anm[]);
>
> setImageTransparent(anm[1], 0, 0, ene[n]->size, ene[n]->size, 255, 255, 255, Cene[n]);
>
> drawCanvas(Cene[n], ene[n]->enex, ene[n]->eney);
>
> ene[n]->anmSpeed=getTickCount();
>
> ene[n]->anmFrame=1;
>
> pixelText(340+(20*n), 30+(22*n), ene[n]->name);
>
> setImage("menuimage.png", 335+(20*n), 25+(22*n), getTextWidth(ene[n]->name)+10, getTextHeight(ene[n]->name)+10);
>
> n++; //kill the variable after use
>
> n = 0;
>
> until(anm[n]=="") // from this point it´s just clean-up the variables // that should be deleted
>
> kill(anm[n]);
> n++;
>
> kill(n);
>
This should be the last time we change this method, so don´t miss any of the details that you want to add. Here I just put the players and enemies on the screen and their names, put anything you want.now that the battle has started and we know how animations will work, let´s make a quick method to kill all the canvases before ontinue, I´m just killing canvases for now but if you have other useless variables that you won´t need outside of battle like CanRun or anything else, kill those variables on this Method.
>
> method endBatttle()
>
> local(n) = 0;
>
> until(CPlayer[playerHandle[n]]=="")
>
> killCanvas(CPlayer[playerHandle[p]]);
>
> n++;
>
> n=0;
>
> until(Cene[n]=="")
> killCanvas(Cene[n]);
> n++;
>
And now that we have the beginning of the animation, and the end of them, we just have to make the method that will control the movement of the idl animation while we wait for a turn.
>
> method AnimateBattle()
>
> local(n) = 0; //let´s put the players
>
> til(player[playerHandle[n]]=="")
>
> split(player[playerHandle[n]]->idlAnm, ",", anm[]);
>
> if(castnum(anm[0])*1000<=getTickCount()-player[playerHandle[n]]->anmSpeed) {
>
> clear(CPlayer[playerHandle[n]]);
>
> player[playerHandle[n]]->anmFrame++;
>
> if(anm[player[playerHandle[n]]->anmFrame]=="") {player[playerHandle[n]]->anmFrame=1};
>
> setImagetransparent(anm[player[playerHandle[n]]->anmFrame], 0, 0, player[playerHandle[n]]->size, player[playerHandle[n]]->size, 255, 255, 255, CPlayer[playerHandle[n]]);
>
> drawCanvas(CPlayer[playerHandle[n]], player[playerHandle[n]]->plx, player[playerHandle[n]]->ply);
>
> player[playerHandle[n]]->anmSpeed=getTickCount();
>
> n++;
>
> n=0;
>
> until(anm[n]=="") //from this point it´s just clean-up the variables that should be deleted
>
> kill(anm[n]);
>
> n++;
>
> n=0 ;
>
> until(ene[n]=="")//now the enemyes, let´s do the same.
>
> split(ene[n]->anmidl, ",", anm[]);
>
> if(castnum(anm[0])*1000<=getTickCount()-ene[n]->anmSpeed) //if it´s time for the nextframe
>
> clear(Cene[n]);
>
> ene[n]->anmFrame++;
>
> if(anm[ene[n]->anmFrame]=="") {ene[n]->anmFrame=1};
>
> setImageTransparent(anm[ene[n]->anmFrame], 0, 0, ene[n]->size, ene[n]->size, 255, 255, 255, Cene[n]);
>
> drawCanvas(Cene[n], ene[n]->enex, ene[n]->eney);
>
> ene[n]->anmSpeed=getTickCount();
>
> n++;
>
> n=0;
>
> until(anm[n]=="") //from this point it´s just clean-up the variables that should be deleted
>
> kill(anm[n]);
>
> n++;
>
> kill(n);
>
This method should do it, basically just takes a look at the time that has passed since the last frame of the animation was set, changes to the next frame and if the animation has ended it starts it all over. Then saves the tickCount to use it as reference for the next time the animation has to be setted.
: if you´re using anotherway of doing things you should make the methods I made, one for the setup of the battle, anotherone to the end of the battle, and anotherone to continue the animation. If you´re going to use my methods, then just take a good look and study the codes until you get how exactly do they work. **Customization**
Creating A Turn-Based Battle System
Day Four
This day will be a preparation for the turns.
Now that the basic BS is done, we only have to make the interactions, but to do so we have to decide whose turn is it, to do so you can do almost everything, I'll just use a temporal variable and add the speed to it until it's 100 or more, basically I'll do this:
>
> until(temp[1]>100) //check the value of a variable { temp[1]+=Player[playerHandle[0]]->speed; //add the player speed to this value } temp[1]-=100; //in case temp[1] is bigger than 100 we take that, so if it 105, it becomes 5.
>
Basically this is the idea, but I want to make a better method, one that will go through all the players and enemies, this method will check every player and enemy and will keep adding the speed value of each of them to a variable, and when the variable is 100 or more, then a method that should be inside the structure will be called and that's how the turns are made.
>
> Method decideTurn() { local(n)=0; until(playerHandle[n]=="") //go through all players { turn[playerHandle[n]]+=player[playerHandle[n]]->speed; //add this player's speed to this player's turn var. If(turn[playerHandle[n]]>99) //if the turn is 100 or more.... { turn[playerHandle[n]]-=100; //we take away the leftovers player[playerHandle[n]]->playerMenu(); //we call this method inside the class } } n=0; until(ene[n]=="") //now we do the same with the enemies { turn[n]+=ene[n]->speed; If(turn[n]>99) { turn[n]-=100; ene[n]->Attack(); } } }
>
See what it does? It's a simple code that adds the speed to the turn[] variable, and when it's 100 or more it calls a method that should be inside of the structure itself that should perform the attack.
Now, it seems rather pointless to make 2 methods to go through all the players and enemies (this and the animation one) so if we can join them (and we can) it means speed savings. Let's just do it at once OK? And let's call it different.
But remember that with this method now you won't need the other 2, so don't save them.
>
> Method Battle() { local(n)=0; until(playerHandle[n]=="") //go through all players { split(player[playerHandle[n]]->idlAnm, ",", anm[]); //split the current animation If(castnum(anm[0])*1000<=getTickCount()-player[playerHandle[n]]->anmSpeed); //check if it's time for next frame { clear(CPlayer[playerHandle[n]]); //clear the canvas of this player player[playerHandle[n]]->anmFrame++; //change to the next frame If(anm[player[playerHandle[n]]->anmFrame]=="") { player[playerHandle[n]]->anmFrame=1; //restart the animation if necessary } setImagetransparent(anm[player[playerHandle[n]]->anmFrame], 0, 0, player[playerHandle[n]]->size, player[playerHandle[n]]->size, 255, 255, 255, CPlayer[playerHandle[n]]); //set the next frame drawCanvas(CPlayer[playerHandle[n]], player[playerHandle[n]]->plx, player[playerHandle[n]]->ply); //draw canvas player[playerHandle[n]]->anmSpeed=getTickCount(); } turn[playerHandle[n]]+=player[playerHandle[n]]->speed; //add the speed to the turn[] var If(turn[playerHandle[n]]>99) //if it's this player's turn { turn[playerHandle[n]]-=100; //take 100 to say this turn has passed player[playerHandle[n]]->playerMenu(); //call this method to perform the turn } n++; } n=0; until(anm[n]=="") //from this point it's just clean-up the variables that should be deleted { kill(anm[n]); n++; } n=0 ; until(ene[n]=="")//now the enemies, let's do the same. { split(ene[n]->anmidl, ",", anm[]); if(castnum(anm[0])*1000<=getTickCount()-ene[n]->anmSpeed); //if it's time for the nextframe { clear(Cene[n]); ene[n]->anmFrame++; if(anm[ene[n]->anmFrame]=="") {ene[n]->anmFrame=1}; setImageTransparent(anm[ene[n]->anmFrame], 0, 0, ene[n]->size, ene[n]->size, 255, 255, 255, Cene[n]); drawCanvas(Cene[n], ene[n]->enex, ene[n]->eney); ene[n]->anmSpeed=getTickCount(); } turn[n]+=ene[n]->speed; If(turn[n]>99) { turn[n]-=100; ene[n]->Attack(); } n++; } n=0; until(anm[n]=="") //from this point it's just clean-up the variables that should be deleted. { kill(anm[n]); n++; } kill(n); }
>
As you can see I just joined the codes I had and now this will check if it's time to pass to the next frame of the animation and then checks to see if it's It's turn. Of course, now that we're using more variables, we have to kill them on the end battle method because we don't want those variables to have a value when we start a new battle.
>
> Method endBatttle() { local(n)=0; until(CPlayer[playerHandle[n]]=="") { killCanvas(CPlayer[playerHandle[p]]); kill(turn[playerHandle[n]]); n++; } n=0; until(Cene[n]=="") { killCanvas(Cene[n]); kill(turn[n]); n++; } }
>
Remember that any variable you use on battle that you don't kill right away (and that's not inside the structures) you have to kill it on this method.
So now we have the idl animations running and the turns being selected, now we just make the enemies attack us and the player's option menu and the BS will be done and working.
But first we have to make another set of canvases to draw the hp of the players. This is easy, we just have to make them on the same method were we do the other canvases, kill them on that same Method too, and reresh them in the same place everything is refreshed, the battle Method.
*NOTE:sorry if it bugs you the fact I'm repeating this method so many times but I have to make the changes step by step for everyone's sake (mostly mine)*
*NOTE:the reason why I didn't coded the hp before is that I didn't wanted to overcome you so much, but since the battle is really starting now (we'll see attacks on day 5) I though it was time to start managing hp*
>
> Method setupBattle(background, music) { bitmap(background); mediaplay(music); local(n)=0; //let's put the players until(player[playerHandle[n]]=="") { //first we save the player's x and y location player[playerHandle[n]]->plx=120+(castInt(n/2)*20); player[playerHandle[n]]->ply=250+(n*50)-(n*75); //now we create the Canvas for this player, take the first frame of the idl animation, draw it to the //canvas and draw the canvas ti the player's x and y location and save the moment with getTickCount CPlayer[playerHandle[n]]=createCanvas(player[playerHandle[n]]->size, player[playerHandle[n]]->size); split(player[playerHandle[n]]->idlAnm, ",", anm[]); setImagetransparent(anm[1], 0, 0, player[playerHandle[n]]->size, player[playerHandle[n]]->size, 255, 255, 255, CPlayer[playerHandle[n]]); drawCanvas(CPlayer[playerHandle[n]], player[playerHandle[n]]->plx, player[playerHandle[n]]->ply); player[playerHandle[n]]->anmSpeed=getTickCount(); player[playerHandle[n]]->anmFrame=1; //now we just put the name of the player on the screen and step to the next player setImage("menuimage.png", 55+(20*n), 25+(22*n), getTextWidth(playerHandle[n])+40, getTextHeight(player[playerHandle[n]]->name)+40); pixelText(55+(20*n), 30+(22*n), player[playerHandle[n]]->name); //here is the name of the player //create life Canvas Lplayer[playerHandle[n]]=CreateCanvas(30, getTextHeight(player[playerHandle[n]]->name)+10); pixelText(0, 5, player[playerHandle[n]]->hp+"/"+GetMaxHp(playerHandle[n]), Lplayer[playerHandle[n]]); drawCanvas(Lplayer[playerHandle[n]], 60+(20*n)+getTextWidth(player[playerHandle[n]]->name), 30+(22*n)); player[playerHandle[n]]->oldhp=player[playerhandle[n]]->hp; n++; } local(nn)=0; until(anm[nn]=="") //from this point it's just clean-up the variables that should be deleted { kill(anm[nn]); nn++; } kill(nn); n=0; until(ene[n]=="")//now the enemies, let's do the same. { ene[n]->enex=400+(castInt(n/2)*20); //let'
> s save the location ene[n]->eney=250+(n*50)-(n*75); //to use it later Cene[n]=createCanvas(ene[n]->size, ene[n]->size); split(ene[n]->anmidl, ",", anm[]); setImageTransparent(anm[1], 0, 0, ene[n]->size, ene[n]->size, 255, 255, 255, Cene[n]); drawCanvas(Cene[n], ene[n]->enex, ene[n]->eney); ene[n]->anmSpeed=getTickCount(); ene[n]->anmFrame=1; pixelText(340+(20*n), 30+(22*n), ene[n]->name); setImage("menuimage.png", 335+(20*n), 25+(22*n), getTextWidth(ene[n]->name)+10, getTextHeight(ene[n]->name)+10); n++; //kill the variable after use } local(nn)=0; until(anm[nn]=="") //from this point it's just clean-up the variables that should be deleted { kill(anm[nn]); nn++; } kill(nn); }
>
As you can see, I only did a small modification, the players now show their hp and I obtain the maxhp from the regular playerHandle[] structure.
The mp will be shown when the skills menu is activated, besides that, there's nothing to do, this method is done.
>
> Method Battle() { local(n)=0; //let's put the players until(player[playerHandle[n]]=="") { if(player[playerHandle[n]->hp>0) //if the player is alive { split(player[playerHandle[n]]->idlAnm, ",", anm[]); if(castnum(anm[0])*1000<=getTickCount()-player[playerHandle[n]]->anmSpeed) { clear(CPlayer[playerHandle[n]]); player[playerHandle[n]]->anmFrame++; if(anm[player[playerHandle[n]]->anmFrame]=="") {player[playerHandle[n]]->anmFrame=1}; setImagetransparent(anm[player[playerHandle[n]]->anmFrame], 0, 0, player[playerHandle[n]]->size, player[playerHandle[n]]->size, 255, 255, 255, CPlayer[playerHandle[n]]); drawCanvas(CPlayer[playerHandle[n]], player[playerHandle[n]]->plx, player[playerHandle[n]]->ply); player[playerHandle[n]]->anmSpeed=getTickCount(); } turn[playerHandle[n]]+=player[playerHandle[n]]->speed; If(turn[playerHandle[n]]>99) { turn[playerHandle[n]]-=100; player[playerHandle[n]]->playerMenu(); } if(player[playerHandle[n]]->hp~=player[playerHandle[n]]->oldhp) { clear(Lplayer[playerHandle[n]]); pixelText(0, 5, player[playerHandle[n]]->hp+"/"+GetMaxHp;(playerHandle[n]), Lplayer[playerHandle[n]]); drawCanvas(Lplayer[playerHandle[n]], 60+(20*n)+getTextWidth(player[playerHandle[n]]->name), 30+(22*n)); player[playerHandle[n]]->oldhp=player[playerHandle[n]]->hp; } } else {clear(CPlayer[playerHandle[n]]);drawCanvas(CPlayer[playerHandle[n]], player[playerHandle[n]]->plx, player[playerHandle[n]]->ply)) //if the player is death local(nn)=0; until(anm[nn]=="") //from this point it's just clean-up the variables that should be deleted { kill(anm[nn]); nn++; } n++; }
>
> local(n)=0; until(ene[n]=="")//now the enemies, let's do the same. { if(ene[n]->hp>0) //if the enemy is alive { split(ene[n]->anmidl, ",", anm[]); if(castnum(anm[0])*1000<=getTickCount()-ene[n]->anmSpeed) //if it's time for the nextframe { clear(Cene[n]); ene[n]->anmFrame++; if(anm[ene[n]->anmFrame]=="") {ene[n]->anmFrame=1} setImageTransparent(anm[ene[n]->anmFrame], 0, 0, ene[n]->size, ene[n]->size, 255, 255, 255, Cene[n]); drawCanvas(Cene[n], ene[n]->enex, ene[n]->eney); ene[n]->anmSpeed=getTickCount(); } turn[n]+=ene[n]->speed; If(turn[n]>99) { turn[n]-=100; ene[n]->Attack(); } } else {clear(Cene[n]; drawCanvas(Cene[n], ene[n]->enex, ene[n]->eney)) //if it's death local(nn)=0; until(anm[nn]=="") //from this point it's just clean-up the variables that should be deleted { kill(anm[nn]); nn++; } n++; }
>
> kill(n); kill(nn); }
>
One change too, the player part check to see if the hp has changed.
And finally, to finish, the end of the day is the end battle method, to kill the life canvasses
>
> Method endBatttle() { local(n)=0; until(CPlayer[playerHandle[n]]=="") { killCanvas(CPlayer[playerHandle[p]]); killCanvas(Lplayer[playerHandle[n]]); kill(turn[playerHandle[n]]); n++ } n=0; until(Cene[n]=="") { killCanvas(Cene[n]); kill(turn[n]); n++; } }
>
ll I did was implement a way to decide the turns and then I implemented a way to keep track of the player's hp. It's your turn!! You should find some things to draw to the life canvas besides of what i did, come on, show your talent! **Customization: A**
**END OF DAY 4**
