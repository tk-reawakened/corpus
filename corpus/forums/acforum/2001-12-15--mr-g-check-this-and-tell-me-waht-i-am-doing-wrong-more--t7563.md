---
kind: forum-thread
id: "acforum/7563"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "7563"
title: "mr g check this and tell me waht i am doing wrong...(more)"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1000&mode=1&msg=7563"
written: "2001-12-15T21:36:00"
last_post: "2001-12-15T24:52:00"
date_confidence: "exact"
captured: ["20011230005427", "20011230011621", "20011230021635", "20011230041525"]
author: "Imrial"
repliers: ["EB", "Vampz", "MrG"]
authors: ["Imrial", "EB", "Vampz", "MrG"]
posts_present: 4
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1000_mode_1_msg_7563", captured: "20011230041525", sha256: "9a7fbf0bb367596f18cb6b3649fd0b3656a3fdf1779dfad6b87e68aa667833f5", wayback_url: "https://web.archive.org/web/20011230041525/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1000&mode=1&msg=7563"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1000_mode_1_msg_7564", captured: "20011230005427", sha256: "8d23ebf7c46c45d631ea11d47290039ae5cd1ce31cef6110c9afd20cf01277e8", wayback_url: "https://web.archive.org/web/20011230005427/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1000&mode=1&msg=7564"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1000_mode_1_msg_7565", captured: "20011230011621", sha256: "f0492820ad3875e222cf2c8e8c9ab0d1960a2e9a13d169a49da0a61d95b54654", wayback_url: "https://web.archive.org/web/20011230011621/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1000&mode=1&msg=7565"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1000_mode_1_msg_7577", captured: "20011230021635", sha256: "14e71eb89318b0b75565d4cd24af53e6329c0917e5abef4d051531110b6c9653", wayback_url: "https://web.archive.org/web/20011230021635/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1000&mode=1&msg=7577"}
links:
  - {url: "http://ebpre.vt9.co.uk", status: "external", local: null}
  - {url: "http://starocean.homestead.com/files/EB_Productions_Small.GIF", status: "external", local: null}
  - {url: "http://starocean.homestead.com/files/EB_Small.GIF", status: "external", local: null}
  - {url: "http://tkzone.net", status: "external", local: null}
---

# mr g check this and tell me waht i am doing wrong...(more)

### Imrial · 2001-12-15 21:36 · #A1000-7563

here is your custom menu can you tell me what i am doing wrong because everytime i try the custom menu it says unrecognised file format and it just shows me the background image i put. Please help i really need this menu to work.
*********************************
*Copyright ©2001 Mystic Software*
******www.mysticsoftware.net*****
*********************************
**#FadeRect designed by Triuken**
*********************************
****The above portion of this****
**program must remain intact or**
****you will be violating the****
***********copyright*************
*********************************
*********!INSTRUCTIONS!**********
**PLEASE READ BEFORE CONTINUING**
*********************************
*To get the menu to work correctly in your game
*all that is required is that you use an image
*editor to make the background image, and buttons
*for your menu, and save them into your games
*BITMAP directory. Then type the filenames of each
*image in the appropriate section below.
*********************************
***********Profiles**************
*********************************
*For profiles to show up in the menu, they must
*be named in a certain format. The format is
*the characters name, followed by the extension
*stored in the variable JPG$, which is defaulted
*to ".jpg". An example of a character's profile
*image who is named George, would be George.jpg
*********************************
******Setting up your menu*******
*********************************
*After setting up your images, you can
*set your menu to work in your game by
*going into the Main File Editor, clicking
*on RPGCode, then on the Run Time Program
*box, and selecting this program. Then
*set your Run-Time activation key
*which is at the bottom of the same
*section in the Main File Editor.
*Dont forget to save your main file
*or the changes will not take effect.
*********************************
*********************************
*********************************
*If you have any other questions, please
*go to www.mysticsoftware.net
*********************************
#CustomMenu()
#Method CustomMenu()
{
**********************************
******Custom Menu Prefrences******
**********************************
*Make sure button sizes are only 30 pixels in height. They can be of any width however.
**********************************
#font$="archetect.fnt"
#font_size!=8
*Below is the value for each font color value "RGB"
#red!=255
#green!=66
#blue!=66
#button_width!=128
********************************************************************
*FOR THE BELOW VARIABLES, DO NOT REMOVE THE "", THEY ARE NECCESSARY*
********************************************************************
#main_image$="backg85.jpg"
#button01$="item.gif"
#button02$="equip.gif"
#button03$="details.gif"
#button04$="ability.gif"
#button05$="save.gif"
#button06$="load.gif"
#button07$="cards.gif"
#button07switch!=1 *Type 1 to turn button 7 on
#button08$="the1.gif"
#button08switch!=0 *Type 1 to turn button 8 on
#button09$="res.gif"
#button10$="quit.gif"
#button11$="the2.gif"
#button11switch!=0 *Type 1 to turn button 11 on
*The variable below deals with how far from the edge the character stats are
#stats_x_position!=12
*The variable below deals with how far from the edge the profile pictures are
#profile_x_position!=18.5
*The variable below deals with what format your profile images are saved in
#profile_image_format$=".jpg"
*The variables below deal with features you may want in your menu. The first one is
*game_time!, which shows the current hours and minutes the player has been playing the
*game. The second variable is show_gold!, which shows how much gold the player currently
*has. The third is show_location!, which shows the name of the 1st layer on the board.
*To turn any of these features off, just change the value from 1 to 0. To turn back on,
*change the value back to 1
#game_time!=1
#show_gold!=1
#show_location!=1

### EB · 2001-12-15 21:37 · #A1000-7564

**Umm. That's Spyders Custom Menu. -nt-**

---
![](http://starocean.homestead.com/files/EB_Small.GIF)
[![](http://starocean.homestead.com/files/EB_Productions_Small.GIF)](http://ebpre.vt9.co.uk)

---

### Vampz · 2001-12-15 21:40 · #A1000-7565

**Didn't you know - Spyder and MrG are the same person...**

...or they appear to be, but one has a sense of humour, and the other is a class act at rpg code.
=)
- Vampz
[The Toolkit Zone Network](http://tkzone.net)

### MrG · 2001-12-15 24:52 · #A1000-7577

**No no, you're confusing the word "one" with "both".. :P nt**

*(no text captured)*
