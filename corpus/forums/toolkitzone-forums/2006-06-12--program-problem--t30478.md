---
kind: forum-thread
id: "toolkitzone-forums/30478"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "30478"
title: "Program problem"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=30478"
written: "2006-06-12T09:41:00"
last_post: "2006-06-12T15:19:00"
date_confidence: "exact"
captured: ["20060628062251"]
author: "metalboss"
repliers: ["Mick", "Icbim"]
authors: ["metalboss", "Mick", "Icbim"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_326821_amp_3Bsid_7d08da24988c57a13ad3b528728759c8", captured: "20060628062251", sha256: "7adf169f9660fb6117d610a560c23eeea94a48dc09856b80a359e1976ea6a338", wayback_url: "https://web.archive.org/web/20060628062251/http://toolkitzone.com/forums/viewtopic.php?p=326821&amp%3Bsid=7d08da24988c57a13ad3b528728759c8"}
links:
  - {url: "http://tk3.toolkitzone.com/help/?page=18.2#con.operators", status: "captured", local: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_18.2"}
---

# Program problem

### metalboss · 2006-06-12 09:41 · #B326786

Can someone please help me!!! I really need this program to work correctly. Theres something wrong when you press on 4 to flirt and when you pres on 5 to Leave.
Thanks.
#Bitmap("waitress.PNG")
#Mwin("Waitress: Welcome to Ye Olde Pub, what may I get you?")
#Mwin("1. Bier!")
#Mwin("2. Meal.")
#Mwin("3. Talk.")
#Mwin("4. Flirt.")
#Mwin("5. Leave.")
#Wait(a!)
#Mwincls()
#If(a!=1)
{
#GetGP(gp)
#If(gp<2)
{
#Mwin("Waitress: Oh, sorry, that's not enough for a bier.")
#Wait(a$)
#Mwincls()
#End
}
#If(gp=>2)
{
#TakeGP(2!)
#Mwin("Waitress: Here's your bier sir, enjoy!")
#Wait(a$)
#Mwincls()
#Fade(2)
#GiveHP("Ed",20)
#End
}
}
#If(a!=2)
{
#GetGP(gp)
#If(gp<5)
{
#Mwin("Waitress: Oh, sorry, that's not enough for a meal.")
#Wait(a$)
#Mwincls()
#End
}
#If(gp=>5)
{
#Mwin("Waitress: Of course, plenty of room left, any table you like sir."))
#Wait()
#Mwincls()
#Send(pub_eat.brd,8,7,1)
#wait()
#GiveHP("Ed",100)
#Send(pub.brd,5,13,1)
#End
}
}
#If(a!=3)
{
#Mwin("Ed: Actually, I just want to talk.")
#Mwin("Waitress: Oh really? That's kind. I don't get much people like you.")
#Wait()
#Mwincls()
#Mwin("What do you ask?")
#Mwin("1. What's you name?")
#Mwin("2. Can I have your phone number because I lost mine.")
#Mwin("3. You wanna go out?")
#Wait(b!)
#Mwincls()
#If(b!=1)
}
#Mwin("Waitress: Rosa, and you?")
#Mwin("Ed:What a beautiful name, my name's Ed.")
#Mwin("Rosa:Why thank you!")
#Wait()
#Mwincls()
#Mwin("Take a look at what's left:")
#Mwin("1. Can I have your phone number because I lost mine.")
#Mwin("2. You wanna go out?")
#Wait(c!)
#Mwincls()
{
{
#If(c!=1)
}
#Mwin("Waitress: Yeah sure here you go.")
#Wait()
#Mwincls()
#Mwin("CONGRATULATIONS! You've got her phone number! You can now flirt.")
#talked!=1
#Wait()
#Mwincls()
#End
{
{
#If(c!=2)
}
#Mwin("Waitress: Never! You really don't know how to chat up a girl!")
#Mwin("OUPS! Try again chum!")
#Wait(c$)
#Mwincls()
#End
{
{
#If(b!=2)
}
#Mwin("Waitress: Lame! You're a jerk!")
#Mwin("OUPS! Try again chum!")
#Wait()
#Mwincls()
#End
{
{
#If(b!=3)
}
#Mwin("Waitress: Never! You really don't know how to chat up a girl!")
#Mwin("OUPS! Try again chum!")
#Wait(b$)
#Mwincls()
#End
{
{
#If(a!=4)
}
#If(talked!=0)
{
#Mwin("Waitress: Lame! You're a jerk!")
#Mwin("OUPS! Try again chum!")
#Wait()
#Mwincls()
#End
}
#If(talked!=1)
{
#Mwin("Ed: So, you got a boyfriend?")
#Mwin("Rosa: Well... let me see, nope!")
#Mwin("Ed: Good, you know I'm not seeing anyone either...")
#Wait()
#Mwincls()
#Mwin("Rosa: So...?")
#Mwin("Ed: Well, maybe we can go out some time, eh, what do you think?")
#Mwin("Rosa: I'd love to!")
#Wait()
#Mwincls()
#Mwin("CONGRATULATIONS! You've completed the chatting up the waitress missions!")
#Mwin("You can start again when you want!")
#talked!=0
#Wait()
#Mwincls()
#End
}
}
#If(a!=5)
{
#Mwin("Waitress: Goodbye and thank you for choosing Ye Olde Pub")
#Wait(a$)
#Mwincls()
#End
}

### Mick · 2006-06-12 15:15 · #B326818

This belongs in the RPG Code Section.
I didn't go through your entire code, but from what I saw, your conditional operators were messed up. Just remember this, one equal sign is for declarations (var1! = 5) and two is what you use in your if statements. Also, remember your equal signs go after your greater than or less than signs (>= , <=)
<http://tk3.toolkitzone.com/help/?page=18.2#con.operators>

### Icbim · 2006-06-12 15:19 · #B326821

**Quote:**

> Can I have your phone number because I lost mine.
>

Priceless Smile
