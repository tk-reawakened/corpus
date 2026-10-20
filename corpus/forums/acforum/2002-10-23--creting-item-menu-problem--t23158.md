---
kind: forum-thread
id: "acforum/23158"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "23158"
title: "creting item menu problem"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=23158"
written: "2002-10-23T22:08:00"
last_post: "2002-10-23T22:08:00"
date_confidence: "exact"
captured: ["20021128062209"]
author: "phill_iv"
repliers: []
authors: ["phill_iv"]
posts_present: 1
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_23158", captured: "20021128062209", sha256: "375042ff13ae1bda625702576be1051ecd229f7e932796db6e8150f14a6a1152", wayback_url: "https://web.archive.org/web/20021128062209/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=23158"}
links: []
---

# creting item menu problem

### phill_iv · 2002-10-23 22:08 · #A1001-23158

ok I've figured out how to set up twp areas for item selection, the upper menu choosing current, rare, or equipment, now the program goes all weird when i press enter on current to drop down to the lower area( where the items will be )but as soon as I hit enter a blank mwin box comes up with three square boxes. and it won't work if i click back onto the screen and press the down or up arrows a run time error comes up. BTW the upper portion of the program seems to work fine but when you hit enter is when it goes bad.
Heres the current code.
***********************************************************************************
**********************************Item Menu****************************************
***********************************************************************************
#Font("times")
#Fontsize(18)
#bitmap("itemmenu.bmp")
#bold(on)
#text(4.3,2.3,"Current Items")
#text(16.5,2.3,"Rare Items")
#text(29.3,2.3,"Equipment")
#put (1.7,1.6, "cursor menu.tst1")
**************************************************************
#menuup!=1
#if (menuup!=1)
{
#cursorplace$="current"
#while(done!==0)
{
#get(cursor$)
#If(cursor$=="RIGHT")******right arrow key
{
#If(cursorplace$="current")
{
#put (15.7,1.6, "cursor menu.tst1")
#put (1.7,1.6, "cursor menu.tst2")
#cursorplace$="equipment"
#branch(:bottom)
}
#if(cursorplace$="rare")
{
#put (1.7,1.6, "cursor menu.tst1")
#put (8.4,1.6, "cursor menu.tst2")
#cursorplace$="current"
}
#if(cursorplace$="equipment")
{
#put (8.4,1.6, "cursor menu.tst1")
#put (15.7,1.6, "cursor menu.tst2")
#cursorplace$="rare"
}
:bottom
}
#If(cursor$=="LEFT")******right arrow key
{
#If(cursorplace$="equipment")
{
#put (1.7,1.6, "cursor menu.tst1")
#put (15.7,1.6, "cursor menu.tst2")
#cursorplace$="current"
#branch(:top_up)
}
#if(cursorplace$="rare")
{
#put (15.7,1.6, "cursor menu.tst1")
#put (8.4,1.6, "cursor menu.tst2")
#cursorplace$="equipment"
}
#if(cursorplace$="current")
{
#put (8.4,1.6, "cursor menu.tst1")
#put (1.7,1.6, "cursor menu.tst2")
#cursorplace$="rare"
}
:top_up
}
#if (cursor$=="ENTER")
{
#if(cursorplace$="current")
{
#put (1.7,3.6, "cursor menu.tst1")
#put (1.7,1.6, "cursor menu.tst2")
#menuup!=2
}
#if(cursorplace$="rare")
{
#put (8.4,3.6, "cursor menu.tst1")
#put (8.4,1.6, "cursor menu.tst2")
#menuup!=2
}
#if(cursorplace$="equipment")
{
#put (15.7,3.6, "cursor menu.tst1")
#put (15.7,1.6, "cursor menu.tst2")
#menuup!=2
}
}
}
#If (menuup!=2)
{
#cursorplace$="current_start"
#while(done!==0)
{
#get(cursor$)
#if (Cursor$=="DOWN")*******Moves the cursor with in the items list down
{
#If(cursorplace$="current_bottom")
{
#put (1.7,4.1, "cursor menu.tst1")
#put (1.7,3.6, "cursor menu.tst2")
#cursorplace$="current_mid"
#branch(:move_down)
}
#If(cursorplace$="current_mid"
{
#put (1.7,5.1, "cursor menu.tst1")
#put (1.7,4.1, "cursor menu.tst2")
#cursorplace$="current_start"
}
#If(cursorplace$="current_start"
{
#put (1.7,5.1, "cursor menu.tst1")
#put (1.7,4.1, "cursor menu.tst2")
#cursorplace$="current_bottom"
}
:move_down
}
#if (Cursor$=="UP")*******Moves the cursor with in the items list down
{
#If(cursorplace$="current_start")
{
#put (1.7,4.1, "cursor menu.tst1")
#put (1.7,3.6, "cursor menu.tst2")
#cursorplace$="current_bottom"
#branch(:move_up)
}
#If(cursorplace$="current_mid"
{
#put (1.7,5.1, "cursor menu.tst1")
#put (1.7,4.1, "cursor menu.tst2")
#cursorplace$="current_start"
}
#If(cursorplace$="current_bottom"
{
#put (1.7,5.1, "cursor menu.tst1")
#put (1.7,4.1, "cursor menu.tst2")
#cursorplace$="current_mid"
}
:move_up
}
}
}
