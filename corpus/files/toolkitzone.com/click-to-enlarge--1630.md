---
kind: file
id: "toolkitzone.com/1630"
site: "toolkitzone.com"
title: "Click to enlarge"
original_url: "http://toolkitzone.com/files.php?file=1630"
written: null
date_confidence: "unknown"
updated: null
captured: ["20100101162654"]
author: "jackyboy"
repliers: []
authors: ["jackyboy"]
comments_present: 0
uploader: "jackyboy"
f_category: "All Categories Audio | -- Background | -- Effects | -- Other Graphics | -- Animations | -- Battle Backgrounds | -- Other | -- Tilesets | -- | -- Buildings (Exterior) | -- | -- Buildings (Interior) | -- | -- Characters | -- | -- Collections | -- | -- Items | -- | -- Monsters | -- | -- Other | -- | -- Terrain RPG Code | -- Custom Systems | -- Methods | -- Other | -- Plugins"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/files.php__file_1630", captured: "20100101162654", sha256: "61acd3b23d4b923deadd269cffadbcc48a8ef90b39eba1e008edba4bf59b72bd", wayback_url: "https://web.archive.org/web/20100101162654/http://toolkitzone.com/files.php?file=1630"}
---

# Click to enlarge

Default Menu Patch
If you use the default menu system then this plugin is a must have. It's identical to default menu, but with some changes that fix the item bugs. Be sure to read the included pdf as some new functionality was added as well.
*10 votes cast.*
Thank you, thank you thank you!!!! I lost almost 2 months trying to program my own menu. Of course I'll keep making it but, now that I have a menu to work with, I can test my game untill my own menu is finished. There are some issues concerning mainly graphics glitches but, what the hell, I can use and equip itmes now.
[![TBD](thumb.php?src=forum/images/avatars/5711064348bb73a961049.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=14694)
Many Thanks, we needed this, It works great. Only I found it just as I was building a new menu system. I give it a 5 star.
[![TBD](thumb.php?src=forum/images/avatars/43509536149364569d6764.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17184)
Thanks. I appreciate the kind words. If you find any bugs or if it just stops working, let me know. I never know if I'll find any problems. And the idea for these fixes came to me in the middle of the night. So I might have screwed up somewhere. Let me know.
I've just register, and I'm still a noob, so I was wondering how do people make plugins?
[![TBD](thumb.php?src=forum/images/avatars/131528095464f948060e4f.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=10850)
your awesome man thanx
[![TBD](thumb.php?src=forum/images/avatars/13485909144a0dfcd4489d3.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=24735)
Will this work on custom menus too?
[![TBD](thumb.php?src=forum/images/avatars/43509536149364569d6764.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17184)
This is only the patch of the default menu system to make items and equipping possible for new users avoiding the terrible crashing scenarios that had been so prevalent when 3.1 came out. So it won't assist you in making custom menus. It doesn't give you any extra commands. For that you need my Menu Help plugin. Otherwise this menu system uses all of the built-in methods of doing things.
[![TBD](thumb.php?src=forum/images/avatars/69830687449a51b3adb629.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=25459)
Hello! I am a complete newbie at the toolkit just putting together an up-to-date system (I am always scared of updating things in the middle of a project). Because I know all too well how getting entangled in coding everything yourself can kill the motivation for a project (my started game projects: more than I care to count; my finished game projects: 0), I plan to work with the default systems. Thus, installing your bug fixes for the battle system and the menu system sounds like a good idea. However, when I read the PDF coming with the menu bug fix, it says that two basic functions ( and , I think) should not be used. Now, I am not sure whether I would actually need them, but still, I wish to know whether there is a workaround for that loss. After all, as I said, I don't like changing something about the engine in the middle of things (T_T) Or can they be used as long as you also update that new array you describe? Deathworks
**Equip()** **Remove()**
[![TBD](thumb.php?src=forum/images/avatars/43509536149364569d6764.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17184)
The commands Equip() and Remove() allow you to equip or remove equipped items in RPGCode. Useful if you ever have a need to do so in a program. But because they use the default systems built into the toolkit, and it is these systems that fail to work properly you cannot use these commands in their current state. However my menuhelp plugin does contain fixes for Equip() and Remove() called nEquip() and nRemove(). This plugin uses the same method for equipping as the menu patch so they can work together. If you wanted to create your own equip system then the arrays that I mentioned in this menu patch along with other commands in my menu help plugin can allow you to do so, also.
[![TBD](thumb.php?src=forum/images/avatars/69830687449a51b3adb629.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=25459)
Hi! Okay. Thank you for that informative response. Well, I think I got my system up to the standards by adding your three plugins (the two bug fixes for the standard systems and the menu help plugin). So, I will be off experimenting (fortunately, I don't mind that encrypted distribution doesn't work (^_^;; ). Anyhow, I also want to thank you for doing all the programming and maintenance work (I am also using your improved trans3.exe). I hope that contrary to my previous forays I may return the favor with something made with the toolkit - but that is something I can't really promise (T_T) Ah, anyhow, good luck and thank you. Deathworks
[![TBD](thumb.php?src=forum/images/avatars/20515787084a57f7c9b6f3c.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=1384)
jackyboy, thank you for doing this. This has been needed to be done for years, and it looks like it's finally happened. Sure, some experienced members will shrug because it's the default menu, but for the newer users picking up TK3 for the first time, they shouldn't have been met with glaring bugs in the default systems. (I haven't tried it out personally, but I'm assuming you've squashed the big bugs handedly because, well, you're jackyboy, and you're great ).
TBD
Well, I hope this works, no matter what I did, the game kept crashing when I wanted to equip something. If this works, you are my saviour! If anyone knows a way of making music actually work on toolkit 2, please let me know. Cheers.
amazing! the greatest creation since sliced bread, and where would we all be without sliced bread?
[![TBD](thumb.php?src=forum/images/avatars/5937009474a8b65302afca.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18678)
And yet someone rated it a two. Was it you?(lol it rhymes) Oh yeah, I'm watching all of jackyboy's files.
[![TBD](thumb.php?src=forum/images/avatars/43509536149364569d6764.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17184)
Most likely rated a 2 because no matter how you slice the bread, it's still just the default menu system and nothing truly special. Although I did have to do a complete conversion from C++ to VB to get this done.
[![TBD](thumb.php?src=forum/images/avatars/5937009474a8b65302afca.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18678)
...but... well, yeah, I guess.TBD
[![TBD](thumb.php?src=forum/images/avatars/14851889014b26c994e5caf.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=27557)
I must give it a 5 star rating -- it fixed many 'item not found' glitches!
TBD
