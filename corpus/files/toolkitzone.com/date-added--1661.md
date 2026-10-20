---
kind: file
id: "toolkitzone.com/1661"
site: "toolkitzone.com"
title: "Date Added"
original_url: "http://toolkitzone.com/files.php?file=1661"
written: null
date_confidence: "unknown"
updated: null
captured: ["20090325002840"]
author: "furyX639"
repliers: []
authors: ["furyX639"]
comments_present: 0
uploader: "furyX639"
f_category: "All Categories Audio | -- Background | -- Effects | -- Other Graphics | -- Animations | -- Battle Backgrounds | -- Other | -- Tilesets | -- | -- Buildings (Exterior) | -- | -- Buildings (Interior) | -- | -- Characters | -- | -- Collections | -- | -- Items | -- | -- Monsters | -- | -- Other | -- | -- Terrain RPG Code | -- Custom Systems | -- Methods | -- Other | -- Plugins"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/files.php__file_1661", captured: "20090325002840", sha256: "06cea8d2e81188d249f741b0bdcfa0c1e12e99f3588b0541b5313ad17cea1757", wayback_url: "https://web.archive.org/web/20090325002840/http://toolkitzone.com/files.php?file=1661"}
---

# Date Added

HTTP Plugin
The HTTP Plugin allows you to make HTTP requests from the RPG Toolkit. You can load a page using getURL or upload a file using putURL. It also includes sample PHP scripts that show you how to make the plugin communicate with your web server. Includes the added ability to store and retrieve text from the clipboard.
*3 votes cast.*
[![TBD](thumb.php?src=forum/images/avatars/625094848457cf1f58da78.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=14726)
The current version is pretty basic. I want to expand it to be more useful for web services so that you can do more cool things like invoke Amazon web services to download album art or download creative common flickr images. Something I'd like to bundle with this is an XML parser. Another plugin that might help is something that gets image data so that you can download pictures and know it's width/height.
[![TBD](thumb.php?src=forum/images/avatars/43509536149364569d6764.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17184)
Cool, people could download progressive updates to games now too. Just post it to a server, update an update file and have the game download the relevant information. This is awesome, thanks furyX639.
[![TBD](thumb.php?src=forum/images/avatars/165174359049bd594f5d974.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18678)
I sorta doubt it but, is there an upload file plugin that works on 3.1.0?
[![TBD](thumb.php?src=forum/images/avatars/625094848457cf1f58da78.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=14726)
Not yet, at least I don't think so... there was an FTP plugin, but it doesn't work in 3.10 Edit: Hey, I added the ability to upload files.
[![TBD](thumb.php?src=forum/images/avatars/2736223394945cd16e697f.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=4090)
Just wanted to say nice plugin. I played around with it for a bit to see what I could do. I noticed when getting a .brd file from online it would give you a error saying that you need to save the board in the board editor. I don't know if this was intended to be able to do this or not. But just thought I would let you know.
[![TBD](thumb.php?src=forum/images/avatars/625094848457cf1f58da78.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=14726)
Yeah I noticed something too. When I downloaded an image it was accessible for the setImage command, but in the RPG Toolkit Editor it wasn't listed in the file pane. It wasn't until I closed toolkit and opened it back up that it listed.
[![TBD](thumb.php?src=forum/images/avatars/165174359049bd594f5d974.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18678)
Would it be possible to make an mmorpg with this by creating text files, and uploading it to a server, and downloading them continuously and reading them to see where the people are, how they look, etc, or would it lag too much?
[![TBD](thumb.php?src=forum/images/avatars/2736223394945cd16e697f.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=4090)
I don't think in it's current version it could be done. But with a few updates I'm sure it will be possible. Right now though it doesn't offer enough to even relay information as if someone is just trying to talk. But the plugin would be better used for sending updates to your game rather then make a MMO. I'm sure MMO capabilities is something he has up his sleeve. I hope so myself. Cause I have some very good ideas to do for my game if this is possible
[![TBD](thumb.php?src=forum/images/avatars/165174359049bd594f5d974.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18678)
[quote="slipknot_hellraiser"]I don't think in it's current version it could be done. But with a few updates I'm sure it will be possible. Right now though it doesn't offer enough to even relay information as if someone is just trying to talk. But the plugin would be better used for sending updates to your game rather then make a MMO. I'm sure MMO capabilities is something he has up his sleeve. I hope so myself. Cause I have some very good ideas to do for my game if this is possible[/quote] Couldn't you just write a text file called board.txt and write something like this: playername x[1],y[1] upload it, so other exes can download it, view and put items on the board according to where player1's x and y is?
[![TBD](thumb.php?src=forum/images/avatars/2736223394945cd16e697f.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=4090)
Yeah but there would be no way to transfer data in variables. Like say you store a variable that holds a players message they just typed. You then send it off and have the other Trans 3 download it. The date in the variable would be useless to the other game clients because the txt file doesn't store any values to the variables that were wrote to it. This would be the case for any other variables that you try to send as well.
[![TBD](thumb.php?src=forum/images/avatars/165174359049bd594f5d974.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18678)
[quote="slipknot_hellraiser"]Yeah but there would be no way to transfer data in variables. Like say you store a variable that holds a players message they just typed. You then send it off and have the other Trans 3 download it. The date in the variable would be useless to the other game clients because the txt file doesn't store any values to the variables that were wrote to it. This would be the case for any other variables that you try to send as well.[/quote] Can't you write a text file that says what the person said, then just read it?
[![TBD](thumb.php?src=forum/images/avatars/2736223394945cd16e697f.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=4090)
With the current read/write plugins. There is no way to have it send "variable Values". So even if you had the user type something, then have it's variable wrote to a file, and send it. When the other user gets it the variable will "= nothing on there computer" With the current read/write plugins there is just no way.
[![TBD](thumb.php?src=forum/images/avatars/165174359049bd594f5d974.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18678)
I agree with that to some extent but... Can't you write a txt called talk1.txt, which contains only what text somebody is saying and just display what is in the text file?
slipknot_hellraiser wrote:
> With the current read/write plugins. There is no way to have it send "variable Values". So even if you had the user type something, then have it's variable wrote to a file, and send it. When the other user gets it the variable will "= nothing on there computer" With the current read/write plugins there is just no way.
>
[![TBD](thumb.php?src=forum/images/avatars/625094848457cf1f58da78.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=14726)
It's possible for you to send something to a webserver and have someone else download it, but it is not practical for a mmorpg or even any form on real time multiplayer gaming. This is not a planned feature nor will it ever be as far as this plugin goes. This is an HTTP plugin, and HTTP is not the way to go for multiplayer since it is the slowest online protocol. Sorry guys, maybe another plugin another time.
[![TBD](thumb.php?src=forum/images/avatars/165174359049bd594f5d974.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18678)
And so, he answers my very first question...TBD
[![TBD](thumb.php?src=forum/images/avatars/625094848457cf1f58da78.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=14726)
Little update on the HTTP Plugin adds a command urlEncode which makes your strings URL safe. This means strings with symbols and spaces won't get messed up when it's being sent to a URL.
[![TBD](thumb.php?src=forum/images/avatars/193907649248f8929061454.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=15584)
Hey, I've downloaded this plugin but haven't tried to use it yet online 'cause I don't have an internet connection at home. I am also planning to use it for an MMORPG. I agree with brenthenry on using .txt files, and have the exes download and reload these files once in a while. But what I'm afraid of is on the speed of the download. How fast can the plugin download files? Which is much better, multiple .txt downloads or one big .txt chunk download? And please someone make a plugin that extends Toolkit for online games.
[![TBD](thumb.php?src=forum/images/avatars/193907649248f8929061454.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=15584)
...Or maybe I could make my own plugin. But the problem is I have just started studying C++, or rather C#. Could someone point me to a good C++ or C# tutorial site? Which programming language can I use to make a plugin for TK? Does C# or VB count?
Quote:
> **Gaia Online! Cool!**
>
![User Image](http://img.photobucket.com/albums/v281/Cosmopanda/Astrology/Halos.jpg)
![User Image](http://a2.cdn.gaiaonline.com/gaia/members/ava/74/2b/b8a79e9ba2b74.jpg)
Who's Online: , , , , , , [crashdandicoot](community.php?user=14881) [fantom](community.php?user=15954) [jackyboy](community.php?user=17184) [Lawck](community.php?user=2988) [Marz](community.php?user=33) [slipknot_hellraiser](community.php?user=4090) [Valence](community.php?user=14598)
