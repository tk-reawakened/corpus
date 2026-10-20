---
kind: file
id: "toolkitzone.com/503"
site: "toolkitzone.com"
title: "In this case I\u0092ll say I\u0092m using fade 2."
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=503"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041108064554", "20041113120520", "20041114182242"]
author: null
repliers: []
authors: []
comments_present: 0
f_description: "A blinds style effect where lots of vertical lines cross the screen."
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_503", captured: "20041108064554", sha256: "cf8ef5d29b4285dc7679f2325b47d6a6b76ddb0a07b36aa4d810a84344e1fde2", wayback_url: "https://web.archive.org/web/20041108064554/http://www.toolkitzone.com/fileman.php?id=3&file=503"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_503", captured: "20041113120520", sha256: "8daede979ce15d8b77a7b7437f6fb0491ab4a86f035a1c1746614c267acc424c", wayback_url: "https://web.archive.org/web/20041113120520/http://www.toolkitzone.com/fileman.php?id=10&file=503"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_503", captured: "20041114182242", sha256: "e046138d4e3b9e99dd5a4950c7fe1edcfb4cc4e9f2d9277d4646f67672cd6fa7", wayback_url: "https://web.archive.org/web/20041114182242/http://www.toolkitzone.com/fileman.php?id=5&file=503"}
---

# In this case Ill say Im using fade 2.

Bigger than normal so it looks different. (Or whatever you called your background)
writing a credits program.
Hi, thanks for downloading my guide to creating a credits program for your game. Hopefully you should find it useful!
**
Whats in this pack
1x HTML Document (this thing!)
1x README file.
1x credits JPEG file
**
How to use this guide
When you see something in its an RPG Code term. Red
Anything in a box is for more advanced users.
This guide assumes that you already have a basic knowledge of RPG code. If you dont I recommend downloading another guide to help you with the basics before you attempt to write a credits program.
**
Lets get started!
Right, the first thing that you assume with a credits program is that itll all be fully automated. If the user has to press keys to move onto the next slide, it feels sloppy and unreal. By making it automated, you give it that professional look!
Most credit reels you see at the cinema and even at the end of video games have a plain black background. You can create this in a painting program such as Paint Shop Pro, or even Paint. Alternatively, you can use the background included with this pack! Its the JPEG called "credits".
With all the required additional resources ready and waiting, lets get writing!
**
Start Writing!
Right, if youve read my other guide, youll know that I like to start any program with
#Fontsize(20)
Right, now we need to set the background.
Because youll probably be running this program from normal graphics, youll want to put a clear command in there to blank out the screen. So the next line would be:
#Clear()
Now use the #Bitmap command to place the blank background on the screen.
So put this:
#Bitmap("credits.jpg")
You also tend to have music with a credit reel. (Lets face it, theyre boring enough without having to sit in silence too!) Decide what music file you wish to use, and then put it into the code like this;
#Midiplay("credits.mid")
Right, so now you have the basics of a credit reel set up. Doesnt look much huh? Lol, well its a firm start.
Now for the important part: the text!
I dont like using Mwins for this sort of thing cos it looks tacky. Instead use the text command do put a line of text onto this screen.
This process is a lot longer than using Mwins, as you have to set the positioning of the text on the screen. Its a bit fiddly, but well worth it.
Heres a little rule of thumb to follow to speed up placing text.
The middle of y! is around about 10.
**
Number of Words
**
The x! position
1-3
3-5
5-8
Anything over 8 words and you want to be putting it onto two lines. This is only a rule of thumb, and is by no means always accurate!
So now put what text you want on the screen!
Its always good to start a credit reel with the name of your game. Therefore, your first line after the #bitmap line might be;
#Text(14,10, "My Game")
Now to automate the credit reel. Use the command #Delay to do this.
Write the next line as this:
#Delay(4)
This pauses the program for 4 seconds. You can change this as to suit the amount of text on the screen. For a screen with little text you might want to put a shorter delay etc.
The next step is to create the transition between one screen and another. This can be very simply achieved through using the #Fade command. With this command, you write #fade(!) then in the brackets where the ! is, you write a number. This number tells the computer which fade you want to perform. Heres what they are.
**
Fade Number
**
A blinds style effect where lots of vertical lines cross the screen.
A soft "fade-in" effect.
A white streak crosses the screen. (This is quite complicated and RAM eating!)
Once youve found the fade you like; insert the line of code.
#Fade(2)
Time for a quick recap of what weve done. This is what your program should look like so far:
#Fontsize(20)
#Midiplay("credits.mid")
#Bitmap("credits.jpg")
#Text(14,10, "My game")
#delay(4)
#fade(2)
Doesnt look much, but you now have the basis for the rest of the credits! Just copy what you did here again, and change what text you put in. So next you might put: "Produced by The True Games Company" into the text box.
So now the program would look something like this.
#Fontsize(20)
#Midiplay("credits.mid")
#Bitmap("credits.jpg")
#Text(14,10, "My game")
#delay(4)
#fade(2)
#Text(10,10, "Produced by The One True Games Company")
#delay(4)
#fade(2)
And then you repeat the process again, however many times you need to.
Thats the basics of doing a credit reel!
**
What else could I include?
You could make it fancy by adding colour to the titles, or using a different font on the titles. The skys the limit. Maybe even add a video sequence if your feeling adventurous!
**
What happens when the reel is finished?
We need to tell the computer what to do once the credit reel has finished. There are two things you could do.
- The player returns to the screen exactly as before the reel started.
2- The player is sent back to the title screen to either load a game or start a new one.
To write the first one simply put:
#return()
After the last line that creates text on the screen.
Or for the second option write:
#reset()
Again, after the last line you wrote.
Its nice to have another JPEG image to display at the end of the credit reel. This would say something like "Thanks for playing", or display your company logo (if you have one). This just adds a more professional feel to the credits again. Insert this line of RPG Code just before the #reset or #return.
Top Tip-
**
Conclusion
Thats just a very quick, whistle stop tour of how to create a credit reel! Hope you found it helpful and easy to use!
Thanks for reading
*
Twin Keyblade
Got any feedback? Please feel free to e-mail me at and give me your thoughts and suggestions!twin_keyblade@fsmail.net
