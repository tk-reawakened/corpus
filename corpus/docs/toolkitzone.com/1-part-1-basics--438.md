---
kind: doc
id: "toolkitzone.com/438"
site: "toolkitzone.com"
title: "1. Part 1: Basics"
original_url: "http://toolkitzone.com/library.php?doc=438"
written: "2010-02-05"
date_confidence: "day"
updated: "2010-02-05"
captured: ["20100216114649"]
author: "Lotusware"
repliers: []
authors: ["Lotusware"]
comments_present: 0
f_author: "Lotusware"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__doc_438", captured: "20100216114649", sha256: "ac990b43ebf76fd4683373e380979995328f2cdc93149831d23a072b28d0ad75", wayback_url: "https://web.archive.org/web/20100216114649/http://toolkitzone.com/library.php?doc=438"}
---

# 1. Part 1: Basics

Browse
**1. Part 1: Basics**
**::[** **Lotusware's Pixel Art Tutorial for Game Creation ]::**
>
> >
> > >
> > > > *All of the art aspects for this series were and thus can be created in , so don't worry about fancy programs here. Those will be in some sort of **MS Paint*** *Board Illustration tutorial and will not be covered. Anyway, lets get started. Just to let you know, I'll be designing all these tiles in a , but you can use the same techniques to make or take the 16x16 tiles that you make and bump them up to 32x32, which I'll get into later. **resolution of 16x16** **32x32 tiles** **So lets begin!***
> > > >
> > >
> >
>
~ **~ Part 1: Basic Tiles**
In this section, we'll be dealing with the basic tiles and techniques used in the creation of a typical scene
**
Tiles
[ Grass - C liffs - Water ]
**
Tips/Techniques
[ Palettes - Light Source - Ratios - Tile Joints ]
**
Tip 1 Choosing a Palette and a light source
>
> There isn't really any wrong palette to pick (aside from a few horrendous colors), but keep in mind that you should keep in a consistent range from tile-to-tile and board-to-board, or else when you combine them, they may not mesh very well and some elements will be too distracting! So if you decide to go for a vibrant palette-- ! Same goes for darker palettes or muted palettes. I prefer to go with a muted palette of limited shades, that way all my tiles seem consistent all the way through the game, not to mention from tile-to-tile. **STICK WITH IT**
>
> >
> > >
> > > *
> > >
> > > *![Palette Used for EraFlux](http://toolkitzone.com/vault/documents/1338.png)*
> > >
> >
>
> Another important thing to remember is ! I can't stress this enough. If you design your sprites with the light coming in from the left, do the same with your tiles. Although tiles themselves are flat, you can still give the illusion of shape with your lighting. Keeping a consistent light source on all of your objects help push that illusion into the game and makes your scene more and . **keep the lighting consistent** **believable** **dynamic**
> ![Lighting](http://toolkitzone.com/vault/documents/1339.png)
>
**Tile 1 The Grass Tile**
> No joking around when I say this, but a grass tile can pretty much make or break your project and a good grass tile is generally hard to acheive.
>
>
> > ![Grass Tiles](http://toolkitzone.com/vault/documents/1340.png)
> >
>
**Tile 2 The Cliff Tile**
> Depending on how you want to make your cliff (type of stone, wear, jaggedness, etc) there are a few ways to go about shaping them. But at this moment, you still need to design them. So here we go.
>
>
> > ![Cliffs](http://toolkitzone.com/vault/documents/1348.png)
> >
>
**Tile 3 The Water Tile**
> This is a little harder to get to work. I came up with a method, albeit it creates a simple-structured water, so don't expect anything crazy awesome or realistic. But this is a two frame technique and its pretty effective.
>
> > ![Water Tiles](http://toolkitzone.com/vault/documents/1342.png)
> >
>
**
Tip 2 Acheiving a Ratio
>
> So now, you have a tileset built out of 16x16 tiles and you have a choice. You can either of these tiles making them 32x32 or you could to make one larger 32x32 tile. To give a comparison between the difference, look at everything on the left column (double-sized) and the right column (groups of 4). Usually, the double-sized tiles are used if you want your game to have a retro feel, as most modern games would have them at a 1:1 ratio rather than the 2:1 ratio of the double-sized tiles. **double the size** **arrange four mini-tiles** **ONLY**
>
Now, using the tiles we just created, we're going to make a board...so here we go. I'll use both proportion methods to give you a better judgement as to which kind of ratio you want to use for your game. It all comes down to the ammount of detail you want, which may be important later on, because for large objects that decorate your board, you should know how much detail you want for them.
>
> >
> > > ![Comparison](http://toolkitzone.com/vault/documents/1344.png)
> > >
> >
>
**Tip 3 Jointing Tiles**
> So, the above looks very bland and really terribly put together because the tiles aren't joined properly. The transitions are flat lines--you can't even tell where the raised platform cuts off. Even with an amazing tileset, if you fail at making your tiles work together, then sadly the board and thus the tiles fail as well. **ONLY**
>
> The easiest technique is to erase the edge of a tile up until some of the darker pixels, then add a darker rim around the edge. This goes for pretty much any kind of tile. For water though, it depends on the surface that it is trying to join into. Since we're dealing with a cliff-to-water tile, it will be the example I'll be showing you. But basically, it depends on the . **contour of the surface**
>
> > ![Joints](http://toolkitzone.com/vault/documents/1347.png)
> >
>
Now that you have all your joints done, lets rebuild the same scene above with our extra tile joints and see how it works. ? I hope you still have it, because we can use that as the shadow from the cliff! **Remember that grass tile I told you to save**
>
> >
> > > ![Shadows](http://toolkitzone.com/vault/documents/1346.png)
> > >
> >
>
>
> > ![Closing](http://toolkitzone.com/vault/documents/1343.png)
> >
>
**1. Part 1: Basics**
[![TBD](thumb.php?src=forum/images/avatars/65630946947656311390fd.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=7660)
great tut. i might use this in a project im doing at the moment
[![TBD](thumb.php?src=forum/images/avatars/11449746124abfc69729fd7.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=14019)
Wow... that's so simple and informative, even could probably make a tileset now! *I*
[![TBD](thumb.php?src=forum/images/avatars/3562418274b63542554ed2.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=15954)
nice, if you have the time i would like to see a tree tutorial. i cant seem to make a decent one for my life.
[![TBD](thumb.php?src=forum/images/avatars/17143353354936769651b69.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17430)
Nice tutorial! That will give me a headstart in making my custom tileset! =3
[![TBD](thumb.php?src=forum/images/avatars/65630946947656311390fd.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=7660)
step 2 and 3 of the cliff is the same as the grass, but i can work out what has to be done from the pictures.
[![TBD](thumb.php?src=forum/images/avatars/5099177444b4a7677eabb5.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=3630)
Thanks for your positive feedback guys! The next section is for scenery, so that will include trees, rocks, flowers, paths, ladders and other stuff. Oh yea, I see that now. I'll fix it up ASAP. I hope to put up a new part weekly, and just to give you guys an idea of what it will cover, it will be everything from tiles, to menus, to sprites, to effects. Every aspect of RPG art will be eventually covered.
**@fantom**
**@Grindalf**
[![TBD](thumb.php?src=forum/images/avatars/65630946947656311390fd.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=7660)
great im gunna put my secret project on hold until i get ahold of theseTBD
[![TBD](thumb.php?src=forum/images/avatars/3562418274b63542554ed2.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=15954)
hmm animating the water tiles? that would lag a ton, at least it does on my computer lol
[![TBD](thumb.php?src=forum/images/avatars/3306586874a4bf686c3e8f.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=25939)
Nice i have been needing one of the for a while
[![TBD](thumb.php?src=forum/images/avatars/65630946947656311390fd.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=7660)
Its ok if you use only a few water tiles(like a river, or pond) if you do a sea it slows down tremendesly
[![TBD](thumb.php?src=forum/images/avatars/5099177444b4a7677eabb5.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=3630)
My recommendation for large-scaled bodies of water would be to stop before you to the highlights. You'd be left with a toned down water tile that still looks like water, but still looks fine without being animated.
[![TBD](thumb.php?src=forum/images/avatars/4668018904a48e8254cff8.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=12580)
the only part I'm confused about is how does it transition from the grass to the cliff top. do you do it similar to the water to cliff? oh wait... do you just run the cliff tiles up one more tile then place the grass over it?
This is great. Simple, yet if done well, can boost the appereance of the graphics, maybe even the sprites, regarding shadow and dramatic touches here and there.
[![TBD](thumb.php?src=forum/images/avatars/11806637724a7b23d6b1614.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=27235)
[![TBD](thumb.php?src=forum/images/avatars/5099177444b4a7677eabb5.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=3630)
What with work getting in the way, I apologize for not updating this more frequently. Next up I guess will be some sprite work, seeing as how I guess its more important that advancing tiles stuff. *actual*
[![TBD](thumb.php?src=forum/images/avatars/14854132954b537a0474677.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=27392)
Ok this tutorial is really great but i think i'm going to totally suck at RPGtoolkit 4ever because i just can't pay attention long enough to read any of the tutorialsTBD
[![TBD](thumb.php?src=forum/images/avatars/14851889014b26c994e5caf.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=27557)
Whoa, this is N-SPIRING! It just makes me wanna try it out RIGHT NOW! Thanks, Lotusware!
[![TBD](thumb.php?src=forum/images/avatars/5099177444b4a7677eabb5.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=3630)
Part 3 and 4 coming THIS CHRISTMAS!
[![TBD](thumb.php?src=forum/images/avatars/7870256364b553f876ae06.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18678)
Yayzka.
[![TBD](thumb.php?src=forum/images/avatars/2220074864b74a74645303.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=27403)
YESSSSSS!!!!!!!!!!!!!!! EDIT: They didn't come out on christmas. It's been a while since christmas, and they still haven't came out
Lotusware wrote:
> Part 3 and 4 coming THIS CHRISTMAS!
>
TBD
[![TBD](thumb.php?src=forum/images/avatars/5099177444b4a7677eabb5.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=3630)
Part 3 is currently pending approval.
[![TBD](thumb.php?src=forum/images/avatars/7870256364b553f876ae06.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=18678)
Yayza.
[![TBD](thumb.php?src=forum/images/avatars/2220074864b74a74645303.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=27403)
Part 3! Yeah!
[![TBD](thumb.php?src=forum/images/avatars/65630946947656311390fd.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=7660)
Nice I really like the stone stairs, look for them in a Darkened worlds screenshot soonTBD
Quick Jump
Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Editorials | -- Zone Awards | -- | -- 2008 | -- | -- 2009 | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
Keyword(s)
All Categories Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Editorials | -- Zone Awards | -- | -- 2008 | -- | -- 2009 | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
**Published**
February 5th, 2010
**User Rating**
![TBD](templates/default/images/icons/rating_blue_5.gif)
*7 votes cast.*
**Views**
597
Contents
