---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=uploads/yesno.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=uploads/yesno.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040819081503"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_uploads_2Fyesno.prg", captured: "20040819081503", sha256: "f120ffbfeec57137fc8495793f139eb50e31ce4493201428a560ccc49b8809e4", wayback_url: "https://web.archive.org/web/20040819081503/http://www.mysticsoftware.net/test.php?mode=6&file=uploads%2Fyesno.prg"}
---

# Mystic Software

*Commands: *YesNoColor- Configures command *r1!,g1!,b1!- Color of unselected choice *r2!,g2!,b2!- Color of selected choice *YesNo- Calls YesNo menu *yes$- Text for "yes" *no$- Text for "no" *var!- Variable to return (1- Yes / 0-No) *x1!,y1!- Coords for yes *x2!,y2!- Coords for no *default!- Default choice (1- Yes / 0-No) *Have fun! *--KSNiloc *cjf@mail15.com #Method YesNoColor(r1!,g1!,b1!,r2!,g2!,b2!,confirm$) { #yesno_r1!=r1! #yesno_g1!=g1! #yesno_b1!=b1! #yesno_r2!=r2! #yesno_g2!=g2! #yesno_b2!=b2! #yesno_confirm$=confirm$ } #Method YesNo(yes$,no$,var!,x1!,y1!,x2!,y2!,default!) { #yesno_pos!=default! #yesno_done!=0 #while(yesno_done!=0) { #ColorRGB(yesno_r1!,yesno_g1!,yesno_b1!) #if(yesno_pos!=1) { #ColorRGB(yesno_r2!,yesno_g2!,yesno_b2!) } #Text(x1!,y1!,yes$) #ColorRGB(yesno_r1!,yesno_g1!,yesno_b1!) #if(yesno_pos!=0) { #ColorRGB(yesno_r2!,yesno_g2!,yesno_b2!) } #Text(x2!,y2!,no$) #yesno_done2!=0 #while(yesno_done2!=0) { #wait(yesno_wait$) #if(yesno_wait$="UP") { #if(yesno_pos!=0) { #yesno_pos!=1 #yesno_done2!=1 } } #if(yesno_wait$="DOWN") { #if(yesno_pos!=1) { #yesno_pos!=0 #yesno_done2!=1 } } #if(yesno_wait$=yesno_confirm$) { #var!=yesno_pos! #ReturnMethod(var!) #yesno_done!=1 #yesno_done2!=1 } } } }
