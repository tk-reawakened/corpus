---
kind: file
id: "toolkitzone.com/445"
site: "toolkitzone.com"
title: "programs"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=445"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041114061640", "20060304161919", "20060312100102"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_445", captured: "20041114061640", sha256: "04ad4be804f92018261661d90e9a64689477f34971f3cbcfa9180ffd7d1e30bd", wayback_url: "https://web.archive.org/web/20041114061640/http://www.toolkitzone.com/fileman.php?id=5&file=445"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_445", captured: "20060304161919", sha256: "2d5602f89364f7874358c3d096e9ecc001d65cb3c1afccb27bbea2cf8731bfb8", wayback_url: "https://web.archive.org/web/20060304161919/http://www.toolkitzone.com:80/fileman.php?id=3&file=445&PHPSESSID=9e94a0bfd739af13980670d1e820a329"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_445", captured: "20060312100102", sha256: "18d0f170ea993d38364b3b64aff8aef04b6c56a01ac37ff14190f90119f3f5ae", wayback_url: "https://web.archive.org/web/20060312100102/http://www.toolkitzone.com/fileman.php?id=10&file=445"}
---

# programs

Ok this is Word2's Tutorial on the #FOR #while and the #if loop and programs.
GLossery 1. the For 2. the while 3. the IF IF you wanna get a in-code-demo. just scroll down. I also have my lesson in RPG code if you wanna try it on the computer.
1. The for loop:
THe for loop is a easy and efficent way to code somthing. Ok its not that easy. The command is: #for(Start number!; end number!; how much to add each time it loops!) { Stuff } The #for loop really looks like this:
#for(a!=0;a!>=15;a!=a!+1) { Stuff }
a!=0 is the starting number. a!>=15 this means only to stop when a! is greater or exactly 15. a!=a!+1 mean that each time the loop is run that it goes up by it adds 1 to it's total. think of it like a circle, when you get from point top to bottem to top again thats 1 loop then you say wel i havent done this 15 time's yet so i gotta do it again.
2. the while
The while loop is similer to the #for loop.
#idiot!=5 #while(idiot!==5) { stuff }
The while loop runs until somthing equels more then 5 or less then 5.
one way to do this is: #done!=0 #while(done!==0) { #mwin(im cool) #wait(A$) #done!=1 }
Or #done!=0 #while(done!==0) { #if(done!==0) { stuff #done!=1 } }
While loops run until the variable changes from 0 to 1.
3, IF loop
an if loop only exicutes if somthing is true, like done!=0 thats true so it runs the #if loop.
#If(done!==0) { stuff }
The IF loop is the basic nessisy in ANY program. battle and menu systems use #if loops all the time.
*************programs**************
***copy and paste the #for loop code**********
#for(A!=0;A!>=15,A!=A!+1) { #random(255,R!) #random(255,B!) #random(255,G!) #colorRGB(R!,B!,G) #fontsize(25) #text(5,5,"#FOR loop") #delay(.5) }
*********end for loop test***********
*****while loop test********* #done!=0 #while(done!==0) { #doom!=doom!+1 #if(doom!==5) { #mwin("see how easy this is!") #wait(A$) #done!=1 } } **********end while***********
********Start IF********** #done!=0 #if(done!==0) { #mwin(this is easy) #wait(A$) #earthquake(10) #end() } *********end if**************
