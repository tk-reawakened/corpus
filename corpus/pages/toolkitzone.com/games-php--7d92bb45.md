---
kind: page
id: "toolkitzone.com/toolkitzone.com/games.php?image=11978"
site: "toolkitzone.com"
title: "Browse"
original_url: "http://toolkitzone.com/games.php?image=11978"
written: null
date_confidence: "unknown"
updated: null
captured: ["20100101194957"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/games.php__image_11978", captured: "20100101194957", sha256: "387e973bcbd47f36926c6563dab77ccfaa33f7d717177170fc186980a55252fa", wayback_url: "https://web.archive.org/web/20100101194957/http://toolkitzone.com/games.php?image=11978"}
---

# Browse

Posted on by (4 ) OutLines
**Friday 2.08am, August 14th 2009** **[aurum34](community.php?user=25910)**
i remember that superISO tryed to code something that would automaticly eliminate my white outLines, since that didn´t worked, i started to open every image with paint and paint the white outlines myself, but now i feel happy because i figured out a way to take away the white outLines automaticly, AND IT WORKS PERFECTLY!!!!
No votes cast.
![Click for more details.](vault/games/images/11978.PNG)
[![TBD](thumb.php?src=forum/images/avatars/177759702449f4701b4f43f.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=25910)
this is the code i used, it needs the fileBrowser AND misc plugins numOfFiles=Filelist("image", "Bitmap\NPC´s") local(img)=1 until(numOfFiles+1==img) { k=KillOutlines("NPC´s"+image[img]) saveToBitmap(k, "NPC´s2"+image[img]) img++ } Method KillOutlines(image) { local(width)=getImageWidth(image) local(height)=getImageHeight(image) local(width2)=0 local(height2)=0 local(r) local(g) local(b) local(r) local(g2) local(b2) local(r2) local(g3) local(b3) local(r4) local(g4) local(b4) getColor(r3, g3, b3) local(can)=createCanvas(width, height) local(can2)=createCanvas(width, height) split(image, ".", img[]) if(length(img[1])==3) {SetImage(image, 0, 0, width, Height, can);SetImage(image, 0, 0, width, Height, can2)} else() {DrawCanvas(image, 0, 0, width, Height, can)} kill(img[0]) kill(img[1]) getPixel(0, 0, r4, g4, b4, can) colorRGB(r4, g4, b4) until(height==height2 AND width==width2) { if(width2>width){width2=0; height2++} getPixel(width2, height2, r, g, b, can) getPixel(width2+1, height2, r2, g2, b2, can) if(r4==r2 AND g4==g2 AND b4==b2 AND r~=r4 AND g~=g4 AND b~=b4) { fillRect(width2, height2, width2, height2, can2) } getPixel(width2, height2+1, r2, g2, b2, can) elseif(r4==r2 AND g4==g2 AND b4==b2 AND r~=r4 AND g~=g4 AND b~=b4) { fillRect(width2, height2, width2, height2, can2) } getPixel(width2-1, height2, r2, g2, b2, can) elseif(r4==r2 AND g4==g2 AND b4==b2 AND r~=r4 AND g~=g4 AND b~=b4) { fillRect(width2, height2, width2, height2, can2) } getPixel(width2, height2-1, r2, g2, b2, can) elseif(r4==r2 AND g4==g2 AND b4==b2 AND r~=r4 AND g~=g4 AND b~=b4) { fillRect(width2, height2, width2, height2, can2) } width2++ } colorRGB(r3, g3, b3) returnMethod(can2) }
[![TBD](thumb.php?src=forum/images/avatars/65630946947656311390fd.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=7660)
pretty cool dude I may have to steal thatTBD
[![TBD](thumb.php?src=forum/images/avatars/15115625064ace8174540e0.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=13474)
This board looks tremendously better that it used to. Great work.
[![TBD](thumb.php?src=forum/images/avatars/177759702449f4701b4f43f.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=25910)
i´m so happy that i posted that code because i lost it when my computer was formated, now i don´t have to do it again!!!!!TBD
Keyword(s)
All Games |- Profiles |- In-Depth |- News |- Images |- Files Have Your Say Media Jobs |- Adverts |- Resumes
Game Menu
