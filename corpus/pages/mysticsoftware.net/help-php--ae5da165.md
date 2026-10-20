---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/help.php?article=3&mode=1"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://mysticsoftware.net/help.php?mode=1&article=3"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040504142308"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/help.php__mode_1_article_3", captured: "20040504142308", sha256: "7c94fc67fd70c8d5499d3da10fac802de8dda0aa5d190894bde6e47bf8196bb2", wayback_url: "https://web.archive.org/web/20040504142308/http://mysticsoftware.net/help.php?mode=1&article=3"}
---

# Mystic Software

Key: STRING=Binary String INT=Binary Int LONG=Binary Long BYTE=Byte Here's how to load things like that: The board loading is done through VB, so the ints, longs and bytes are just handled by using normal binary access Get and Put functions. The strings, however, are loaded and written one character at a type, with each character corresponding to one byte in the file. Like this: Dim part As String * 1 length = Len(theString) For t = 1 To length part = Mid$(theString, t, 1) Put #fileNum, , part Next t Put #fileNum, , Chr$(0) Also, as you can see, each string is terminated with a NULL character STRING Header *generally RPGTLKT BOARD INT majorver INT minorver INT regYN *0 - Not Registered 1 - Registered STRING registeredstring *NOCODE if not registered INT sizex INT sizey INT sizelayer INT playerx *where the player starts INT playery INT playerlayer INT canyousave *0 - Can't save on board 1 - Can save INT lutsize *The size of the lookup table for the tiles 0 to lutsize STRING lookuptable tile next 1 to sizelayer 1 to sizey 1 to sizex INT instances *This is kinda weird. I think it's how many *times the tile reoccurs in a row, but if it's *more than once the number is negative, so you have *to do the absolute value of the number *then keep loading in the same values of the next *numbers till you hit test (the number of times it *appears) Keep in mind this is going by rows, so *you're adding one to x each time until you hit the *sizex, then you go down one y, etc. These next *values only come once, so don't load them more than *once from the file. INT boardcoords *coords indicating where on the board the tile is INT ambientred INT ambientgreen INT ambientblue BYTE tiletype *0 - Normal 1 - Solid 2 - Under 3 - Northsouth Normal 4 - Eastwest normal 11 - Elevate to layer 1 12 - Elevate to layer 2 ... 18 - Elevate to layer 8 next sizex next sizey next sizelayer STRING backgroundimage STRING foregroundimage STRING borderbackgroundimage LONG boardcolor LONG bordercolor INT ambienteffect *0- none 1- darkness 2- fog 3- watery STRING northlink STRING southlink STRING eastlink STRING westlink INT boardskill STRING fightingbackground INT fightingYN *1- yes 0- no INT daynightYN *1- yes 0- no INT usecustombattleoptionsatnight *1-yes 0- no INT skilllevelatnight STRING fightbackgroundatnight for 1 to 10 INT boardconstant next STRING boardmusic for 0 to 8 STRING boardtitle next INT numberofprograms for 0 to numberofprograms STRING programname INT progx INT progy INT proglayer STRING programgraphic INT active *0- always active 1- conditional active INT activationvariable INT activationvariable_after_the_program_is_done INT what_the_activationvariable_is_at_the_beginning_of_the_program INT what_the_activationvariable_is_at_the_end_of_the_program INT activationtype *0- step on 1- hit the key next STRING programentrance *program to run on entrace STRING backgroundprogram *No, I don't know what this is either INT numofitems *heh, not used for 0 to 10 STRING itemname INT ix INT iy INT ilayer STRING igraphic INT active *0- always active 1- conditional active INT activationvariable INT activationvariable_after_the_program_is_done INT what_the_activationvariable_is_at_the_beginning_of_the_program INT what_the_activationvariable_is_at_the_end_of_the_program INT activationtype *0- step on 1- hit the key STRING activationprogram STRING multitaskprogram next
