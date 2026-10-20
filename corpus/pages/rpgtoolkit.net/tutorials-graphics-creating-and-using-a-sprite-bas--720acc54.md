---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/tutorials/graphics/creating-and-using-a-sprite-base/"
site: "rpgtoolkit.net"
title: "October 10th, 2010"
original_url: "http://rpgtoolkit.net/tutorials/graphics/creating-and-using-a-sprite-base/"
written: "2010-10-10"
date_confidence: "day"
updated: null
captured: ["20110318071517"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/tutorials/graphics/creating-and-using-a-sprite-base/index", captured: "20110318071517", sha256: "a01c6af037407b324414f80d1d2214b71816587668a70905451fb99363ea0916", wayback_url: "https://web.archive.org/web/20110318071517/http://rpgtoolkit.net/tutorials/graphics/creating-and-using-a-sprite-base/"}
---

# October 10th, 2010

[![StarRaven](thumb/80/community/images/avatars/upload/14367168564befa0084461c.png)](member/starraven/)
Published
**October 10th, 2010**
Read times **963**
Written by StarRaven
Creating and Using a Sprite Base
**StarRaven takes you through the keys to create a sprite base and then using it in animations and so forth.**
1. Part 1: South-Facing
2. Part 2: Making a Sprite from Your Base
3. Part 3: Southwest Facing
4. Part 4: West Facing
5. Part 5: Reverse Views
6. Interlude - About Programs
Creating and Using a Sprite Base
Part 1: South-Facing
*This tutorial will cover everything I know about making and using a sprite base, from making the base to animating it to making sprites with it. I will cover both standard and isometric views. If you have a question, please comment and I will do my very best to explain! Please note which page you are commenting on, though, if there's something specific.***
**This part of the tutorial is not for southeast/southwest isometric views - those will be covered later in the tutorial. For now, start with a south-facing sprite. It can't hurt.**
![](vault/images/30_1.PNG)
Choose a size for your sprite. This will depend on the type of sprites you are going for, so if you want to, find some sprites you like and note their size and proportions. Here, I have picked a 32x64 space to work in, and marked out some things: **Step One:**
X - Approximate top of head. (Putting it relatively low will give me plenty of room for big hair and varying the size of the sprites between short and tall characters.)
1-2 - Chin to hips. (This will also approximately mark the length of the arms.)
2-3 - Legs.
I am going for a highly stylized, "chibi" look, but with longer limbs, inspired by some art by various Nippon Ichi games, like . Split your work area in half. Aside from helping to make your sprite symmetrical, this is also to make sure the sprite is centered. Remember to leave your guidelines intact. Make the two sides different colors if you are working with an even number of pixels horizontally. Now to start drawing your sprite! I always like to start with the chin, draw the head, and then work downward. I initially skip drawing the arm or draw it in another color so that I can still see the body. Depending on the type of sprite you want to make, you might want to draw a silhouette and avoid drawing lines, at least for now. It might be helpful to draw some parts that overlap the main body in another color. You should also mark in important features - in the case of my sprite, its most important feature is its eyes, so I have determined a general shape and size and marked them in. [this](http://creativeuncut.com/gallery-01/pb-misc02.html)
![](vault/images/30_2.PNG) **Step Two:**
![](vault/images/30_3.PNG) **Step Three:**
For small/stylized sprites, start with a large circular shape for the head. From there, draw a rectangular body and add some width for the hips. Draw a line for the bottom of the feet, and mark out their width, then draw a line from the hip to the outside of the foot. ( .) Do the same for the inside of the legs. Last, draw in some blobs for the hands at the sprite's sides, and mark out the width of the shoulders. Draw a line from the outside of the shoulders to the hands, and if necessary from the body to the inside of the hands. (Optional) If you want your sprite to have lines, this is when you should put them in. For each part of the body, you will have to decide whether your lines should be on the outside or inside of the color. Often you will have to just do what looks best on each piece and even omit lines in some places. For example, I have outlined my sprite here, but I decided to just leave it lineless. That's it for the first part of this series of tutorials! Next up: Making a sprite from your base. **Guidelines:** *Paint's line tool is extremely useful for all of this as long as you understand that you will have to fix any bad lines later*
![](vault/images/30_4.PNG) **Step Four:**
** Creating and Using a Sprite Base
Part 2: Making a Sprite From Your Base
What? Jumping to making a sprite already? But the base isn't even done yet! I've only got one view! ...is what you might be thinking. Well, it's time to test that view out! If there are any errors left in your base, this is how you'll find them. I can almost guarantee that you'll shave off a few pixels here, add a few pixels there, etc. during the first time you make a sprite with your newly-made sprite base. Since all the other views are based on this first one, it will help to iron out the wrinkles here before getting started on the others. You don't need a character design, but you should know what you want your character to look like. (For the purpose of testing the base, it's a good idea to pick a character of medium height and build, without a lot of armor or other stuff that will get in the way.) Make a mental list of the important defining characteristics of the character. The number of these "defining characteristics" that you can include will vary depending on the size of your sprite base. Take a look at your base and think about how much detail can fit into each part of the sprite before deciding what you want to be the defining feature of your character. (I will be making Generic Villager #1. His "defining characteristics" will be a vest and a hat. How exciting.)
**Step One:**
![](vault/images/30_5.PNG)
Pick some colors that you want to use - you don't have to have a color palette, but if you've already got one, you can pick colors from that. You can always change the colors when you're done. **Step Two:**
![](vault/images/30_6.PNG)
Now start coloring. Try not to put similar colors next to each other, or they will be less distinct. If two colors are too similar, try making them lighter or darker. **Step Three:**
![](vault/images/30_7.PNG)
Gradually build up colors. While it's important to keep in mind the usual things like the direction of the light source, also important (arguably more important) is maintaining contrast between each color. Take a look at your sprite: if there are any places where your eye seems to blur the line between the two colors, there is not enough contrast. (Similarly, if your shadows look like they're popping off the object they're supposed to be shading, you have too much contrast.) **S** **tep Four:**
![](vault/images/30_8.PNG)
Eyes are quite important on larger and anime-style sprites. Here are some tips:
-
First off, don't make one eye and then copy+flip+paste it. If you can view them both together at a reasonable amount of zoom, then they're small enough to work on separately. Work on them both at the same time, rather than one and then the other. (If you must, draw the eye, copy+flip+paste it, and then draw the pupil, and copy and paste that inside the eye without flipping.)
-
If your eyes are slightly smaller than my sprite's, you might have a problem figuring out where the white space should be. If you can't put the pupils in the center of the eyes (or think that they're too small with white space on each side), then put the white space on the outside of the pupils. This will make the character appear to be looking forward (or perhaps slightly downward) and will most likely not look like he or she is cross-eyed. If you put the white space on the inside, something often looks a little off about them and gives the character a vacant look.
-
Since you have such a small area to work with, if you want the character's eye color to be obvious, you may want to color the top eyelid, bottom eyelid, or both the darkest color of the eye's palette. (On very small eyes, a bottom lid might not be necessary.)
-
You don't have to use white for the highlight on the eyes. If the eyes are a darker color, it might be better to use a lighter version of your base color.
![](vault/images/30_9.PNG)
Hairstyle and headgear is very important to a sprite where the head is the main focus. There are a lot of ways to draw hair for sprites, so I'll just show you the one I use.
-
Pick a color, then draw the front of the hair - the parts that overlap the face. Use a shade slightly darker than your base.
-
Draw in your base color on top of it. (Alternatively, you could draw in your base color and then shade it, but I find doing it this way easier.)
-
Draw in the rest of the hair in another color (I used the darkest shade of blue that I'll use for this.)
-
...and then shade that as well
-
Add highlights, and you're done.
At this point, you are pretty much done. For my own sprites, I like to put a black outline around them, to increase the contrast between the sprite and the background. Another option is to outline it in darker shades of your base colors, using black only where you need the most contrast or where you've already used the darkest shade of that color. Now that we've tested our new sprite base, we'll move on to the rest of the views! **Step Five:**
**Next up: Part 3: Southwest-Facing.**
**** Creating and Using a Sprite Base
Part 3: Southwest Facing
Time to make a southwest-facing view for your sprite base! Hmm? Not using isometric views? Why not? Just because you're not making an isometric game doesn't mean your sprites can't still face that direction if you're using pixel-based movement instead of tile-based. Still, if you really want to skip this part, you can go ahead and move on to Part 4: West-Facing.
Still here? Great! Grab your South-facing sprite base and have a look at it. Making a Southwest view will really be just about moving some things around. We'll start with the head. **Step One:**
- As long as it's a relatively simple roundish shape, you probably won't have to alter the shape. (At the most, you might have to push in the neck and a portion of the side of the head to show the bulge of the cheek, and move the chin forward a bit. I've shown it here, but I don't think my sprite warrants that kind of detail, so I'm going to skip it.)
- If the sprite has a neck, though, it should be pushed in or moved back just a bit.
- If the eyes are large, take the one on the left and reduce it by a pixel horizontally. Move the eyes closer together, and move them both toward the left side of the head.
- If the sprite has a mouth or other features, move them to the left as well. Make sure the nose is pointing left.
![](vault/images/30_10.PNG)
The body should not need to be changed much other than moving the arms. Move the arm on the left back, you might have to adjust the angle slightly. (On bigger sprites, you might want to move it up a pixel or two.) For the arm on the right, bring it forward and draw in the shape of the arm. (on bigger sprites, you might want to move it down.) **Step Two:**
![](vault/images/30_11.PNG)
The legs are the trickiest bit, and depend a little bit on exactly what kind of pose you want for your sprite. For the left leg, move it up just a bit, and alter the shape of the foot so it's pointing to the left. For the right leg, change the angle of leg to something more straight down or outward, instead of inward. **Step Three:**
![](vault/images/30_12.PNG)
At this point, if you are making isometric sprites only, you're pretty much finished. All you have to do now is flip it for a southeast view and change a few things for northwest and northeast. (That will be covered in Part 5: Reverse Views.)
**** Creating and Using a Sprite Base
Part 4: West Facing (Left Profile)
Like the southwest view, this view is mostly Grab your south and southwest views, you'll need them both for this. Like the southwest view, start with the south view. Again with the head, as long as it's a relatively simple roundish shape, you probably won't have to alter the shape. You might have to alter a few pixels to show the nose and chin if your sprite is large enough, similar to what I did for the southwest view.
**Part One:**
- If the sprite has a neck, it should be pushed in or moved back just a bit (slightly more than in the southwest view.)
- Delete the eye on the left side, and move the other one over to the left, to the left of the center of the face.
- If the sprite has a mouth or other features, move them to the left as well.
Erase the arms from your sprite. See your southwest view? Copy the arm from that view (the one in front.) Take the leg on the left - that is, the left-facing one, not the one in front - and copy that, too, While you're at it. (Make two copies of this, in two different colors if your sprite has no lines.) Paste them off to the side to be used in a minute. **Part Two:**
Take the arm and paste it into place underneath your sprite's neck, maybe slightly back depending on the sprite's pose. Now start shaving off pixels until the body is the right shape. Erase the legs while you're at it. **Part Three:**
Paste the legs on (the back one first) and adjust pixels until everything looks right. Done. **Part Four:**
![](vault/images/30_13.PNG)
**Next: Part 5 - Reverse Views**
****** Creating and Using a Sprite Base
Part 5: Reverse Views
It seemed like a waste to give the north-facing view its own page, so for this view: Delete the facial features and anything else specific to the front view (like the belly button) and add anything specific to the back view (like the shoulder blades.)
**Step One:**
Done. **Step Two:**
![](vault/images/30_14.PNG)
The northwest view is probably the hardest so far - at least, it was for me. Grab your southeast view, you'll need it for this.
As with the north view, start by deleting the facial features and anything else specific to the front view. **Step One:**
The leg that is supposed to be in front needs to come down, and the leg in the back needs to go up. Both feet should be pointing in the direction that the sprite is facing. **Step Two:**
Draw in the shape of the back over the far arm. The far arm might need to be shortened. **Step Three:**
Draw in the front arm in front of the body. **Step Four:**
![](vault/images/30_15.PNG)
Give yourself a pat on the back - you're finished with the standing sprite bases for every view! Take a well-earned break, and when you get back - Part 6: The Walking Animation.
*Current progress:*
![](vault/images/30_16.PNG)
Creating and Using a Sprite Base
Interlude - About Programs
Welcome back! I know it's been quite a while since I updated, but... well, I said to take a break, didn't I? Haha... ha.... Okay. So, the first thing that you might notice is that I've changed the colors I'm using to mock up the sprites from the garish pinks and blues from MS Paint's default palette to a nice set of teals. The reason for this is that in the time since I finished the last part, I have quit using MS Paint and started using GraphicsGale, which I'm going to talk about real quick: GraphicsGale is a free program that is much like Paint, but includes several features that Paint lacks such as layers and transparency. Two features useful for game-making include the ability to easily manipulate a color palette - palettes can be saved and loaded, and changes to a color on the palette will change all instances of that color in the picture - and the ability to create animations which can be saved either as several images (one per frame) or as multiple parts of a single image. The free version of GraphicsGale does not support saving as GIF format. (The shareware version supports animated GIFs, and Windows cursor and icon formats. As far as I've been able to tell, that's the only difference between that and the free version.) The reason I'm mentioning GraphicsGale here is because its animation capabilities will be useful for the next part of this guide, which, as you might have guessed, deals with animations. So, have I sold you on GraphicsGale yet? If not, then feel free to continue using whatever you were using before, but you may have a hard time following along in something like Paint, which doesn't support layers or frames, or Photoshop, which sucks for pixel art. Some things you will want to be aware of when animating in GraphicsGale: - For onion skinning to work, when making a new frame, transparency must be enabled and set to default white. - To save an image you have animated as either several images or a combined image, go to File -> Export. - The preview window automatically shows the animation in action as you work on it. To see only the frame you are working on, you will have to hit the pause button. You can use MS Paint, but since Paint has neither animation capabilities nor layers, there will be no way to check the accuracy of the animations until you start using them. You could also use Photoshop for animating, but setting Photoshop up to use for pixel art is a nuisance and I don't recommend it, especially if you use Photoshop for other types of image editing and don't want to mess with the settings. I can't talk about any other programs, because these are the only three that I am familiar with. If you use something else and need help, I'm afraid you are on your own. Some images because the document editor doesn't seem to want to put them in: Radiant Omen's (crappy) color palette, in GraphicsGale:
[ [image]
GraphicsGale's animation export screen:[ [image]
*Also yes, my palette sucks. I'm working on it. Shh.*
{"twitter":[{"text":"Site is up and running, seems any initial problems are solved. See you on the forums :)","date":"Thursday at 2:55pm"},{"text":"New site is online but many of you will see a white screen, it's a problem with the PHPBB software. Trying to fix it, stay patient :)","date":"Thursday at 2:17pm"},{"text":"Site is online, little initial bug so apologies to those in the first 5 minutes who wondered why everything was broke :) Should be okay now.","date":"Thursday at 1:50pm"}]}
