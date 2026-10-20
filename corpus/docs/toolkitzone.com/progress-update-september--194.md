---
kind: doc
id: "toolkitzone.com/194"
site: "toolkitzone.com"
title: "Progress Update - September"
original_url: "http://toolkitzone.com/library.php?mode=read&doc=194"
written: "2006-09-05T12:19:00"
date_confidence: "exact"
updated: null
captured: ["20061004233108", "20070220005056", "20070308231752", "20070314195254"]
author: "Colin"
repliers: []
authors: ["Colin"]
comments_present: 0
f_author: "Colin"
f_date: "September 5, 2006, 12:19 pm"
f_description: "This month, as requested via the frontpage poll, RPG Code is the focus of attention. Colin details the inner workings of the brand new RPG Code subsystem and its inherent advantages, as well as giving you a first look at the new animation wizard."
f_section: "Toolkit 3.x > News"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_194", captured: "20061004233108", sha256: "b6ac7dde02156453481e5db4a56ff06ddb25f36d9fab553dd8e4304625b7ad88", wayback_url: "https://web.archive.org/web/20061004233108/http://toolkitzone.com:80/library.php?mode=read&doc=194&PHPSESSID=a820148b616163a5ea1de7ec3d784861"}
  - {path: "wayback/toolkitzone.com/library.php__doc_194_page_1", captured: "20070220005056", sha256: "4c820dffa556efa1e21747397d18495527e8cd76a2c60136db33a2a118794f77", wayback_url: "https://web.archive.org/web/20070220005056/http://www.toolkitzone.com/library.php?doc=194&page=1"}
  - {path: "wayback/toolkitzone.com/library.php__doc_194_highlight_", captured: "20070308231752", sha256: "70ad785225afe39a6ffb7b2360ff17d994e1eabe263ee4f1a7aef8e240395988", wayback_url: "https://web.archive.org/web/20070308231752/http://www.toolkitzone.com:80/library.php?doc=194&highlight"}
  - {path: "wayback/toolkitzone.com/library.php__doc_194", captured: "20070314195254", sha256: "4ffd6036b1c09d33fe511164890169445a11595d56327d518927b15397bc4c44", wayback_url: "https://web.archive.org/web/20070314195254/http://www.toolkitzone.com/library.php?doc=194"}
---

# Progress Update - September

By Colin
As expected, work on 3.0.7 continued throughout August. This article discusses some of the work accomplished last month as well as providing an introduction to RPGCode in 3.0.7. Our testing team has again expanded to expedite the testing process - this time, we welcome Tayln and OBCT, who we are sure will be valuable assets.
Because the Toolkit's scripting language has been notoriously non-backward compatible, many users have been concerned about 3.0.7's RPGCode. This release features a new RPGCode subsystem, which is much different in implementation from 3.0.6's, but similar to use. However, code containing certain elements which were previously discouraged will no longer work. This ensures that all code will execute faster. An RPGCode Updater is provided to transition your code.
We have promised that RPGCode in 3.0.7 will be faster than previous versions. It is. In previous versions, each line of RPGCode was parsed and interpreted each time it was encountered in a very slow process that was especially well-known for making loops ridiculously slow. However, in 3.0.7, RPGCode is handled in several phases. First, a lexical analyser makes tokens from the file, such as "colon", "addition sign", and "method keyword". Then a parser, using a list of grammar rules, processes the tokens to produce a set of "instructions".
Then a "compiler" reorders the instructions for maximum efficiency, similar to Java's bytecode. Then this set of instructions is saved to an RPGCode Cache so that if the same program is run again later in the game, it can be instantly executed. From the set of instructions, the RPGCode Interpreter has the trivial job of simply performing the tasks requested of it.
The instructions that the interpreter will process fall into two categories: data and commands. Commands are orders that are easy for the interpreter to process like "add" or "call"; they are not synonymous with functions like AddPlayer(). When transversing these instructions, the interpreter maintains a stack: to process a data instruction, the interprerter pushes data onto the stack. When processing a command with a set number of parameters, the interpreter pops off one piece of data for each argument where the last data off is the last parameter. Then, it pushes its return value onto the stack. Every command has a return value. As an example, consider the following line:
```
x = sin(5) + tan(3) * 2
```
As humans, we can see that the multiplication should be done first. In 3.0.6, there is a complicated and slow process for evaluating each line: it is parsed, precedence is found, and all sorts of slow things happen when the line is encountered - and they may happen again and again if the line is inside a loop. But in 3.0.7, the line is tackled before the program executes, but note that 3.0.7 does not "optimise" programs (that will have to wait for a later version!) so constants like sin(5) are not evaluated at compile-time. The process happens like this. First, the lexical analyser produces tokens like "identifier", "equals sign", "identifier", "left bracket", "number", "right bracket", and so on. Then a parser uses its grammar rules to produce instructions. In this case, the parser produces the following instructions:
```
x 3 tan 2 * 5 sin + =
```
These instructions are very easy for the interpreter to execute. First, it comes across "x", and "3", both data, and pushes them onto the stack. Then it finds "tan", a command requiring one parameter, and pops off the last piece of data, "3", to be its argument. Then, it pushes the result, the tangent of 3 (~0.052), onto the stack. Now the stack contains "x", and "0.052". Then, the interpreter finds "2", data, and "*", a command. So, it pops off the last two pieces of data, 0.052 and 2, and multiplies them. It then pushes the result, ~0.105, onto the stack. Now it finds "5", also data, and "sin", a command requiring one argument. It pops off the "5" and pushes on the sine of 5 (~0.087). Now the interpreter finds "+", a command requiring two parameters. The last two values on the stack are 0.105 and 0.087, so they are popped off, added, and then the result, 0.192, is pushed onto the stack. Now, the interpreter has reached the final instruction, "=", a command requiring two pieces of data. The last two items on the stack are now "x" and 0.192, so x is set to 0.192. It sounds like this would take a long time, but the interpreter can execute hundreds of instructions in a millisecond, depending on what they are doing. (The actual work done by a given RPGCode function might take longer.)
As mentioned above, there have been some slight changes to the syntax of the language, which are principally for speed reasons. They can also be viewed as encouraging better coding practices. The change that will be the most widely felt is that in 3.0.7, the assignment operator (=) and the equality operator (==) are distinct. The assignment operator cannot be used in place of the equality operator and vice versa. Do not worry if you have made dubious use of these operators in the past; the 3.0.7 code updater will correct them, but you will need to respect the difference between the two operators when writing new code. Character data ("strings") must be encased within double quotation marks in 3.0.7. If you have not quoted strings, the updater will handle it, but be weary of this rule in the future.
Another change is with the type system. Previous versions of RPGCode were more or less "strictly typed". This means that you could not use a string where a number was expected and vice versa, and variables had a symbol for their type: either numerical (!) or literal ($). The type system in 3.0.7, however, is "dynamically typed". This means that a variable's type can change over the course of execution and that you can use a string where a number might be expected. This also means that you can concatenate numbers and strings ("pi is " + 3.14) without casts. A peripheral advantage is that you no longer have to use type declaration characters anywhere. This regrettably means that if two separate variables whose names differ only by type both exist, 3.0.7 will mistake them for a single variable. But this situation should be rare, so it will probably not affect you.
We made vague references to an "RPGCode Updater" above. When you are upgrading from a previous version of the Toolkit, the Updater will launch when you open the Toolkit for the first time. (The Updater can be opened at any time later from the RPGCode Editor.) It will step you through a few pages of information and allow you to choose any files you would not like to update based on the information it provides. It will then update your files at a rapid pace and save backups in a "Backup" subdirectory of the "Prg" folder allowing you to revert to the previous versions in case the updater makes a mistake.
![The new rpgcode updater](library/images/docs/1007.png)
An animation wizard has also been added this month, an oft-requested tool that vastly simplifies the creation of sprites without sacrificing the flexibility of TK3's features. Based on the popular tool provided in TK2's character and item editors, the wizard caters for both tile- and image file-based animations (see image). A series of image files (such as jpegs) can be selected and ordered; the animation's transparent colour is taken from the frame's first pixel and it is resized to match the image size. Alternatively, a tileset can be opened and any number of multi-tile frames created; if more than one tile is present per frame, 'tile bitmaps' are necessarily created for each frame and saved in a subfolder.
The animation editor itself has also been tweaked slightly to provide a couple of new options, such as auto-sizing to image and the ability to enter a numerical delay value.
![The new animation editor](library/images/docs/1008.png)
In September, development will continue, along with regular testing cycles. Unfortunately, both Delano and I will be busier shortly, but 3.0.7 will continue to near a release. (We will not be offering an estimated release date, however.) We appreciate your continued interest in 3.0.7!
iFrog
September 5, 2006, 12:29 pm
Kewl. I was looking forward to a more in depth update like this. ;)
Joe the Outlaw
September 5, 2006, 12:46 pm
Wow, 3.0.7 is going to be quite the handy tool! Can't wait till octember comes around.
rentabuddha
September 5, 2006, 3:14 pm
crazy! this will be much easier!
Trent
September 5, 2006, 4:23 pm
That all sounds pretty badass. I expect 3.0.7 to rock my face off. And if it doesn't, I want a refund. :D
Nick Champagne
September 5, 2006, 4:57 pm
I assume since you said subfolder that we can create our own in other folder without it duplicating them. If so thats great because it will make organizing so much easier. Oh, great update!
Sir Pimpalot
September 5, 2006, 5:00 pm
I had no clue what it was talking about, but it sounded great! :) Where the hell is octember!?!?!?!?
legomaster88
September 5, 2006, 5:47 pm
It's awesome! Runs faster. Save for the fact that I didn't understand some of the words (lol) mostly cuz Im just a hobby programmer and only use TK at that. What would be neat to see is what the actaul commands are. Will they be the same ones as in 3.0.6? Or will they be a whole new breed for us older users to learn? heh. should be fun. Sorry if anything was answered in the above: I kinda skipped a few paragraphs (A tad boring for me to read a chapter willingly for a book. lol). So all in all, a good report as always [/suckingup]
TK Game Boy
September 5, 2006, 6:24 pm
All this looks so awesome. The TK is getting more and more flexible. Who knows, maybe flexible enough to make a near-perfect fighting game, the kind of game I like to make. Rock on Dev Team.
daman
September 5, 2006, 11:13 pm
So many new and faster features I think my head will explode on the execution of the program! I think that even SUPER ADVANCED users of the toolkit will take a while to get used to all of these new features.
Enzix
September 6, 2006, 12:05 am
It looks as if our beloved RPGCode scripting language is leaning closer and closer to an advanced programming language syntax, such as C++. Looking at the example code from the previous update concerning vectors and the new data stacks of this update...anyways, looks like this is going great. Kudos!
September 6, 2006, 12:20 pm
I am dying to know whether or not you can select mulitple tiles from the flyout-tileset thingy in the board editor and lay them all at once. (Like Fury2 had, if anyone ever tried that out.)
Euix
September 6, 2006, 7:15 pm
Concerning variable scope - will variables declared in methods, loops, and programs be local or will we have to explicitly declare their scope? I feel this should be done automatically. Variables should be local unless declared otherwise.
Colin
September 6, 2006, 7:26 pm
Just call autolocal() at the start of your program to make local the "preferred" scope. To the person who asked about new functions; the function names have not changed and there are only a few new functions. As the article states, "commands" are not the same thing as "functions". EB, I'm sorry to disappoint you - but you can't do that yet. There is (untested and unused) code that lets you plot down tile bitmaps in the board editor, and it may become used, but don't expect anything fancy like selection tools such as rectangles when choosing tiles.
spicydeath82
September 6, 2006, 9:39 pm
Wow guys it's looking awesome, this should help aleviate some headaches, plus with all the other new features this is fast becomeing a very powerful rpg tool.
????
September 7, 2006, 7:18 pm
I like EB's idea, maybe it could consider for a later release like 3.0.8
Montai
September 8, 2006, 1:37 pm
I'm looking foward to that feature... It's one of the most wanted/needed tools for the board editor.
polraudio
September 8, 2006, 4:37 pm
Looking better, cant wait till it comes out!
DarkElite
September 10, 2006, 9:57 am
My god, I can't wait till this comes out! Release it now! ^_^
September 10, 2006, 11:36 am
Turns out that Chris Reeves has already written an addition for the toolkit (v3.6) that allows you to multiple select tiles and lay them at once (Thanks DrakeLord), as well as select multiple tiles on the board and copy/cut/paste/delete. I don't see why this already working code can't be added to 3.0.7. I don't have the source code, but I have the patcher which updates 3.6 with the board editor tools for those who want it. http://www.ebproductions.co.uk/files/starocean/VIPBoardEditUpdate.rar These additions cut major time off how long it takes to design boards. The option to select then copy/paste is also fantastic.
Xavier
September 10, 2006, 6:32 pm
@EB: The patch has been downloaded by 351 users here at TKZ already ( ) after being put online last year, but it has been claimed to cause additional editor bugs. The dev team asked him for the source to be shared a long time ago, but he (Mr.Reeves) never did. Go figure. [link](http://toolkitzone.com/fileman.php?id=3&file=1212)
Colin
September 10, 2006, 10:34 pm
I know Xavier already touched on this, but I want to make sure that everybody understands that Christopher Reeves does for the community by releasing proprietary patches to our software. Please don't use anything written by him. You are hurting the community by doing so. The Toolkit is and it gives you freedoms. Everything Chris has ever released, by contrast, is designed to strip you of your freedoms. With Chris' patch, you are no longer free to study sources, and you are no longer free to release modifications. You have in fact become dependent on a proprietor: you only get fixes when Chris completes them (and the bugs his "patch" introduces have yet to be fixed) and you only get a version for 3.0.7 when he completes one. This is not free software! No, Chris' software model is nothing of the sort; it is the complete opposite, and it is altogether incompatible with the ideals of this community (actually, my ideals, but they should be those of any real community). Chris as a casestudy provides a compelling argument for releasing the Toolkit under a licence. People should not be legally entitled to commit the hoax - no, the evil - that Chris has perpetuated on this community! I should thank you, EB, because your comment regarding our including Chris' work has motivated me to write a more full account of why we need a copyleft licence and I hope we can start using a licence that will protect your freedom as soon as possible. **nothing**
gcn_zelda
September 11, 2006, 8:34 pm
Chris Reeves still exists? I haven't seen him or his brother in ages.
zero4367
September 12, 2006, 8:33 am
Hmmm... this is pretty sweet. Badass, indeed.
Colin
September 16, 2006, 2:18 pm
t's impossible to "implement" a "patch" when Chris' patches are always binary-only. I asked Chris for the source of his editor patches and told him to release the source for his battle system derivative, but he just won't. In the battle system's case, he actually has violated the , as it requires that derivative versions include the source. If the official release is missing features people want, they should go ahead and implement them, and they should contribute those features back to the community by releasing the source. They shouldn't keep their improvements proprietary, which is exactly what Chris is doing. Now, in order to satisfy the community's request for a feature, we have to implement it even though code for it already exists. Don't you see that Reeves has done nothing useful here? He has only created a forked properietary version of the Toolkit. It's evil for so many reasons that I don't think I need to give you a full answer here. Let's look at it from the other diirection. What does Chris have to gain by not releasing the source? The only thing he has to gain is satisfaction for his ego as everybody downloads his patch rather than an official release which he could have been a part of. I would have no problem if Chris would also submit a binary for immediate download so long as he provides us the source too so that everybody can have the features in the next version, but that's not what he did. He offers only a binary because he doesn't care to help people! As I said before, you are dependent on Chris, not us, for improvements in his patch. In 3.0.7 the board file format has changed and the whole board editor is rewritten, and you will not be able to use his features unless releases another patch which is not a simple job considering the internal changes (but if we'd had the source, his patch would have already been updated!), and to be frank, it isn't going to happen. Reeves tends to disappear for years at a time, and his features are now lost. To keep the Toolkit free, it is crucial that it not have a propretor. However, if he does release another patch, it will be free because I hope that we can release 3.0.7 under a copyleft licence. I haven't had a chance to fully articulate the case yet, though. I have a feeling that Chris will resist this modest request for his work to be contributed back to the community, and if he does, his work will simply not be accepted at the TKZ. "His" battle systems, derived from the official one, already violate licences, and should be removed as soon as possible from this resource site. You also make some irrelevant comments about cbm. The Toolkit is not only cbm's. It is a community project. The engine contains very little code by cbm and from a legal standpoint, he does not need to agree to our changing the licence, except for code by him, which is not that much in 3.0.7's engine. If he does not agree, I would even go so far as to rewrite the two or so files left by him with a different implementation. However, as a sign of courtesy, we would probably ask him. But keep in mind I haven't talked with Delano yet (I really hope he agrees to release his rewritten board editor under a copyleft licence!), so I don't really know if he'll agree, but it may be possible to release the whole Toolkit under the GPL even if contains some of cbm's BSD code since the latter is compatible with the former. One promise I will make is that none of my code (all of RPGCode, plugins, some file formats, some graphics stuff, and other miscellanea) will be released under a non-copyleft licence in 3.0.7. [licence](http://tk3.toolkitzone.com/dev/?page=acold)
**again**
*he*
Ddragon07
September 17, 2006, 4:46 pm
Hey, awesome! I have a suggestion for the new version though. If it wouldn't be too hard, could you make it possible to put a variable in the boards fighting skill? Or if this is already possible, let me know. I'm trying to make an overworld with the monster's changing as you progress. I have everything I need, just need to be able to use a variable in the skill level option of the board info. This would really help, thanks and keep it up!!!
Colin
September 18, 2006, 5:52 pm
I strongly disagree that binary-only patches are useful. You say Reeves "programmed a utility that people have been wanting, people are getting his program and using it, and he likes that. 'Reeves has done nothing useful here' just isn't true" but that is extremely selfish and not a good reason to withhold source. Reeves could help so many more people by releasing the source, even though it would not be so gratifying to his ego. We need to consider the greater community and it extends beyond Reeves' personal desires. Not releasing the source to keep a monopoly on its usage is completely unethical and nobody should respect that. It's just wrong. I apologise that I made what I said pretty personal. It frustrates me when some people around here think Reeves is more eager to share his sources than he really is. It's quite a common misunderstanding. I'm sure Christopher Reeves is a great person and I wish I would have had a chance to get to know him better, but this particular habit of his is very troubling. Yes, cbm maintained a binary-only product for many years and I don't applaud that either. The thing that makes a cbm a better person than Reeves is that cbm freed the Toolkit. If he hadn't done that, the Toolkit would have been long dead (like Reeves' patch, but on a much larger scale). But think, comfox, if cbm had done this earlier (or from the start), the TK would be so much farther advanced by now. With regards to being off-topic, yes, I guess. I'm not insulted by you and I hope you aren't insulted or offended by me. I think it's great when people want to help, but in order to help, they really need to make the source available.
Spyder
October 1, 2006, 1:26 am
Colin, calm the fuck down, seriously... Honestly, until 3.0.7 is released, or until someone else releases a similar patch along with the source code, then clearly Chris Reeve's patch " " in fact useful to quite a few people. Over 300 from TKZ's own count (minus margin of error).
**is**
Colin
October 4, 2006, 12:48 am
I don't think you fully appreciate the ethical and practical points in play here, Spyder. But it's not a problem if you don't. The days of anti-social proprietary "patches" like Reeves' are coming to a close with 3.0.7. We will be ushering in an age of social, free, open source patches.
This month, as requested via the frontpage poll, RPG Code is the focus of attention. Colin details the inner workings of the brand new RPG Code subsystem and its inherent advantages, as well as giving you a first look at the new animation wizard.
**Recent News**
Aug 8, '06
Jul 3, '06
Jan 5, '06
Jun 6, '05
Apr 5, '05
