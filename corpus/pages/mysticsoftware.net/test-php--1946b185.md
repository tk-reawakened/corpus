---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=files/custombutton.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=files/custombutton.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040818023811"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_files_2Fcustombutton.prg", captured: "20040818023811", sha256: "803be39a33085cdde95ca72554531fbad17a65aa2a51720db48d6f35e26b8069", wayback_url: "https://web.archive.org/web/20040818023811/http://www.mysticsoftware.net/test.php?mode=6&file=files%2Fcustombutton.prg"}
---

# Mystic Software

********************************************** * These methods are created by (redacted: name)* * E-mail : (redacted: email) * * Website: www.nyctasoft.com * ********************************************** * #CreateButton * *********************************************** * This method create a button from a #Bitmap * * or #SetImage, or even in a board, without * * the need of an additional image. * * It allows you to reduce the amount of your * * game\'s images and to reduce the size of the * * bitmap\'s directory. * * You\'ll generally need to add your buttons * * directly to your image (ex.:your menu backg)* *********************************************** * Note: * * Requires Leuf\'s plugin (LitsnLogs) * * I supposed you all had it so I used it to * * shorten my code. * ********************************************************* * Command : * * * * #CreateButton(btnname$,btnx!,btnx2!,btny!,btny 2!) * * * ********************************************************* * btnx! = left X coord. of the button * * btnx2! = right X coord. of the button * * btny! = left Y coord. of the button * * btny2! = right Y coord. of the button * ***************************************** * btnname$ = name of the button * ***************************************** #Method CreateButton(btnname$,btnx!,btnx2!,btny!,btny2!) { #x1[btnname$]!=btnx! #x2[btnname$]!=btnx2! #y1[btnname$]!=btny! #y2[btnname$]!=btny2! *I used arrays to store btnx! and btny! vars... } ************************************************************ ************************************************************ ** #CheckB ** *************** * How To Use * *********************************************** * Use the name of the button you want to * * check. [ex.: #CheckB("Item") ] * * * * If this button is clicked, then the literal * * variable ButtonClicked$ will be equal to * * the chosen name [ex.: ButtonClicked="Item"] * * * * Use that for your button\'s actions. * * [ex.: #If(ButtonClicked$="Item"){ACTION} * * * * You can edit "ButtonClicked$" name, just * * modify it in the method code (it\'s not hard)* * * *********************************************** *********************************************** * Command : * * * * #CheckB(btnname$) * * * ********************************************** #Method CheckB(btnname$) { #MouseClick(msx!,msy!) #And(andres!,msx!>x1[btnname$]!,msx!y1[btnname$]!,msy! Find More at www.toolkitzone.virtualave.net <- * * Toolkit Zone is a part of Toolkit Zone Network * *******************************************************
