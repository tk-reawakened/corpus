---
kind: file
id: "toolkitzone.com/1629"
site: "toolkitzone.com"
title: "Date Added"
original_url: "http://toolkitzone.com/files.php?file=1629&dl="
written: null
date_confidence: "unknown"
updated: null
captured: ["20100101162721", "20100101231308"]
author: "jackyboy"
repliers: []
authors: ["jackyboy"]
comments_present: 0
uploader: "jackyboy"
f_category: "All Categories Audio | -- Background | -- Effects | -- Other Graphics | -- Animations | -- Battle Backgrounds | -- Other | -- Tilesets | -- | -- Buildings (Exterior) | -- | -- Buildings (Interior) | -- | -- Characters | -- | -- Collections | -- | -- Items | -- | -- Monsters | -- | -- Other | -- | -- Terrain RPG Code | -- Custom Systems | -- Methods | -- Other | -- Plugins"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/files.php__file_1629", captured: "20100101162721", sha256: "cd7588ede2176bd241ad30bf344c71859dc9b74fe1004eb098ae783dc45c2b7c", wayback_url: "https://web.archive.org/web/20100101162721/http://toolkitzone.com/files.php?file=1629"}
  - {path: "wayback/toolkitzone.com/files.php__file_1629_dl_", captured: "20100101231308", sha256: "50333fc8eb16b98bca76ad12f4df1e1068d519141b91d662386740648c8f357e", wayback_url: "https://web.archive.org/web/20100101231308/http://toolkitzone.com/files.php?file=1629&dl"}
---

# Date Added

Enemy info Plugin
The Enemy info plugin allows you to load *.ene files into multiple slots. From there you may access all the information from the enemy file as well as the variables for that particular copy of the enemy. This will definitely help for anyone working on a battle system wanting to use RPG Toolkit's internal file formats. It's a very complete package that's gives you full acess to the otherwise unusable enemy files (unless you code a plugin yourself). Updated 10/03/2009 with bugfixes, and added the player animation commands and the ability to set a target and source handle.
![TBD](templates/default/images/icons/rating_blue_4.5.gif)
*5 votes cast.*
[![TBD](thumb.php?src=forum/images/avatars/625094848457cf1f58da78.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=14726)
Finally! Thank you jackyboy for this, slowly but surely I finally am are to use RPG Toolkit's file formats for custom systems without coding a plugin.
[![TBD](thumb.php?src=forum/images/avatars/43509536149364569d6764.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17184)
You're welcome. As always let me know if you think there's something missing, if you want something added. I have one more update planned but that doesn't include much. Always willing to add more.TBD
[![TBD](thumb.php?src=forum/images/avatars/1924818327482ffc2b5bca8.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=19774)
jackyboy, do you think it would be possible to allow us to set custom stats (like speed) in a future update? I am not sure if the toolkit would throw a hissy fit if you alter the contents of an ene file, but you could always achieve this by creating a second file with that data in it and just link the two using this plugin. That would make this ultra useful.
[![TBD](thumb.php?src=forum/images/avatars/5937009474a8b65302afca.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18678)
O.O 5/5
[![TBD](thumb.php?src=forum/images/avatars/1505334803496c35d8d33c4.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17691)
Enemyx, y, or layer should help, but this plugin is great!
[![TBD](thumb.php?src=forum/images/avatars/43509536149364569d6764.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17184)
Seeing as how enemies are not actually placed on the board unless you draw the animations keeping track of enemy X, Y, and layer in the plugin is unnecessary. Keeping track of it in RPGCode should be sufficient.
[![TBD](thumb.php?src=forum/images/avatars/5937009474a8b65302afca.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18678)
why does DrawAnimation() only draw 32x32?
[![TBD](thumb.php?src=forum/images/avatars/43509536149364569d6764.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17184)
Because you don't need anything bigger. If you think you do you're fooling yourself. Just kidding. Because in the midst of fixing some things I must have broken another. However with school, and an upcoming vacation I don't think I'll have time to fix it for at least another week or so. Just hang tight, and keep reporting any errors you find. The more I can fix in one update the better.
[![TBD](thumb.php?src=forum/images/avatars/58978235494dc827f11ef.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=24090)
Well, this is definitely what I need, but I am confused as to how you use this plugin after... y'know, plugging it in.
[![TBD](thumb.php?src=forum/images/avatars/911659324b28b467b9605.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=25718)
funny, i dont either.
armaniac wrote:
> Well, this is definitely what I need, but I am confused as to how you use this plugin after... y'know, plugging it in.
>
[![TBD](thumb.php?src=forum/images/avatars/49198935143f50e086344d.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=5812)
Nice work on the updates.
[![TBD](thumb.php?src=forum/images/avatars/43509536149364569d6764.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17184)
Maybe, I haven't actually tested the changes and additions. I find it easier to let others do that for me.
[![TBD](thumb.php?src=forum/images/avatars/5937009474a8b65302afca.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18678)
Should these two return the same thing? Because they don't. [code] debugger(getSMDamage("burn.spc")+"|"+GetBattleSmInfo("burn.spc",6)) function getSMDamage(file){ orig_hp = getHP(playerHandle[0]); useplayersm(0,0,file); cur_hp = getHp(playerHandle[0]) damage = orig_hp - cur_hp; giveHP(playerHandle[0], damage); return damage; }[/code] It shows RPGCode Error: 5|
[![TBD](thumb.php?src=forum/images/avatars/43509536149364569d6764.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17184)
Your questions are so silly, brenthenry. If it's not returning anything at all, not a zero, not anything, then there's something wrong and it's not acting like it should. Did you even try accessing the rest of the options? But to answer your question, yes they should but apparently one doesn't return anything at all. And that's admittedly my fault. I stupidly forgot to remove the place-holder at the end of the function. When I first create my functions have them all return an empty string by default until I work them out. Just forgot to remove that part when I finished it.
[![TBD](thumb.php?src=forum/images/avatars/5937009474a8b65302afca.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18678)
[quote="jackyboy"]Your questions are so silly, brenthenry. If it's not returning anything at all, not a zero, not anything, then there's something wrong and it's not acting like it should. Did you even try accessing the rest of the options? But to answer your question, yes they should but apparently one doesn't return anything at all.[/quote] So, is it bugged or is it just my "silliness"?
TBD
[![TBD](thumb.php?src=forum/images/avatars/43509536149364569d6764.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17184)
You're purposely being silly now aren't you? I already said it was both.
[![TBD](thumb.php?src=forum/images/avatars/5937009474a8b65302afca.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18678)
Your classy way of talking confuses me.
[![TBD](thumb.php?src=forum/images/avatars/43509536149364569d6764.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17184)
Bah, it's not classy. I'm just a naturally confusing person. Well the update was accepted so hopefully the problem is solved.
[![TBD](thumb.php?src=forum/images/avatars/18684430394b2e604981b19.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=27392)
You know what jackyboy, I don't even care what files you put on the site. if i were a staff member i would approve them ALL. Without even looking at it.
[![TBD](thumb.php?src=forum/images/avatars/43509536149364569d6764.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17184)
Uhhh, they accept everything that I've put up so far. But there is quality to be concerned with.
[![TBD](thumb.php?src=forum/images/avatars/625094848457cf1f58da78.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=14726)
Thank you jackyboy! I was putting off making a function to read fight backgrounds for last, and now I won't have toTBD
[![TBD](thumb.php?src=forum/images/avatars/185782029149cb95212c449.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=24442)
Yes!! Thanks alot jackyboy!
[![TBD](thumb.php?src=forum/images/avatars/14851889014b26c994e5caf.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=27557)
Good plugin, i have found it very useful!
Who's Online: , , , , , , , [algiz](community.php?user=27929) [jackyboy](community.php?user=17184) [Jon](community.php?user=16904) [Occasionally_Correct](community.php?user=94) [TK Game Boy](community.php?user=304) [z3ro](community.php?user=4618) [Zyrshnikashnu](community.php?user=254) [zzz](community.php?user=428)
