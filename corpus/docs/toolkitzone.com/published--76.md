---
kind: doc
id: "toolkitzone.com/76"
site: "toolkitzone.com"
title: "Published"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=76"
written: "2007-01-25"
date_confidence: "day"
updated: "2007-01-25"
captured: ["20081219093912", "20081219093912"]
author: "Khin"
repliers: []
authors: ["Khin"]
comments_present: 0
f_author: "Khin"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_76", captured: "20081219093912", sha256: "49f3a825970fe4979a82b41dd939cfb39a5aa989c1a525702dcf7b16713a9ca2", wayback_url: "https://web.archive.org/web/20081219093912/http://toolkitzone.com/library.php?mode=read&doc=76"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_76-1901d9", captured: "20081219093912", sha256: "685cb9e5a71631d2e48287a904b0a9092bd2fbec7241036fe0568b1ec7ae46a0", wayback_url: "https://web.archive.org/web/20081219093912/http://www.toolkitzone.com/library.php?mode=read&doc=76"}
---

# Published

Browse
Sprite Drawing Tutorial: Standing on All Four Directions
Some weeks ago I posted a sprite drawing tutorial on the section. It covered the procedures on how to draw a 32x32 standing sprite facing south--from the line art to full coloring. This article is a continuation of the said topic, but to avoid the feeling of , let me restart from the beginning. ***Arts*** *picking up where we left off*
The following tutorial is just a suggestion and by no means a way of telling you "this is how you do it, your process is wrong", or "this is the best way.". I'm not an artist by profession. I only do these by practice (hobby, pastime, leisure), so it's really up to you if you want to take my advice or not. I'm not a perfect artist. If you find my wok pleasing, then you'll be pleased with the tutorial. If not, I'd rather that you do not read any further.
Ok, so let's begin.
First off, we select a canvas. Since most game makers here still make 32x32 sprites, we're going to make 32x32 sprites. After selecting the canvas, I suggest you fill it with a "buffer color". It's supposed to be a color that wouldn't appear in your sprite. This would make things easier for us if we ever have to cut out things, or for transparency. Most Graphics programs default to WHITE (MSPaint, Photoshop, etc.). Here, I used Green--RGB value(0,255,0). A grid would also be nice. Since we are working on a very tiny piece, it's useful to have a grid. Some may not prefer it though. What we are going to create is a standing pose. Ideally, on a generic RPG view, it should be symmetrical--the left side is opposite but equal to the right side in terms of measurement. That's the reason why it is important to get the middle section of the canvas. Since this is a 32 px width canvas, we don't really have a mid section... that's why I put a 2px wide line there. That's our reference mid section.![](vault/documents/26.gif)
The next thing I draw is the Head. It's just a matter of preference, really...but to give you an idea, take a look at this:
Notice that I placed the head at the 5th pixel from the top. Yours may vary depending on your desired head size. After laying down the head it's time to build the contour of the head. remember we only need to draw half of it. The chin area should be a few pixels narrower than the top of the head. Just observe how i did the head. From this drawing, let's put something on the face.![](vault/documents/27.gif)
I put an eye along with the eyebrow. I also completed half of the sprite. Observe the lines. The white line marks the line of the head. Measure the difference between the top of the head and the shoulder. It may vary but you should keep this in mind: The shoulder should NEVER be located below the chin area. Unless the perspective of your game is side or front view, don't do that technique. A sprite like this is assumed to be viewed semi-top-down, so the shoulder somewhat reaches the level of the ear. Take note that our shoulder is only a pixel away from the ear. The blue line marks the chest area. Actually that's not the chest, that's where the neck and the chest meet. Again, necks shouldn't really protrude in a perspective such as this. You can see that there's actually no neck. What you see is the neck area of the shirt, not the man's neck. If the guy has no clothes, you don't have to draw those lines below the chin. Also, please remember that nothing should go horizontally straight here: not the shoulder, not the waist, not the head ..nothing. Every shape should be drawn like an ellipse, where it tends to go lower as it goes near the center area. The orange area is supposed to be the guy's hip area, though sometimes i prefer the line below it. Notice how the hips ISN'T horizontally straight. In normal human anatomy, the hands should reach the leg...but to be more accurate, our elbows are almost at the level of our hips (not exactly the hip, but that area where females have that hip curve ..I think you call it belly?). The orange line also marks the palm area. Since sprites don't have to capture the true human anatomy, it may seem that the arm brace area has disappeared... it's actually just a pixel or two above our palm area. Alright, below the hip area is of course the leg. The yellow line marks the end of the leg and start of the foot...but this isn't really where they connect. Since it's in semi top view, it sort of vanished from our sight. You can imagine that the pixel above the yellow line is where the leg and the toe actually connect. Please observe how they are proportioned. I copied the left part, pasted it and flipped it. I positioned it to meet the center mark, but as you can see, our sprite would look too wide! Ideally, we should have drawn the left half thinner so that we would avoid this result. I did this so that I may show you what you could do in times like this...or if you want you can just redraw half of the sprite and rearrange the proportions.. Anyway, what I did is just I repositioned both halves, so they would form a satisfying sprite. Take note however that our sprite is no longer centered... but for small pieces like these, that wouldn't be noticed. Besides, our background will be transparent, so people will hardly notice that our sprite is off-centered.![](vault/documents/28.gif)
![](vault/documents/29.gif)
There, it looks better now, doesn't it? Now it looks like an acceptable standing sprite. It's time to color it..
![](vault/documents/32.gif)
Shaded it. Did it look like i jumped too far ahead? Actually I've had some shading tutorials posted some time ago, but let me explain them to you briefly. First, think of a light source. In my piece it's from the northeastern corner, in front of the sprite (remember that light-sourcing is somewhat 3 dimensional). That said, you should comprehend that as a mass of body approaches light, it should be shaded lighter, and those away from it should be darker. That's what I simply did. To the left side of the pic are the darker shades because they are "away" from the light. However, DO NOT make the mistake of simply using linear gradients. Remember that this isn't a flat surface we're doing. This is something that actually has mass, and shape...and complicated at that. First, the head. The head is circular, so notice how it is shaded. In between the eyes is supposedly the nose. Since the side of the nose would receive amount of light, the "other side" that's hidden should be shaded. If you remove the nose shading it would appear that the sprite doesn't have a nose. Also, since this is bald, we should put that "shine" in his head. Next, the arms, legs, and toes. Left side is darkened, right side is kept neutral. Why isn't there a hint of shine on them? If you try putting some, the piece would look like a balloon, or a porcelain vase. We don't want that. Besides, he really should be all that shiny. It's just his head that should come out as this. The shoes also benefited from lighter shading, but it's not as saturated as the one i gave to the head. if i did that, that'll give the impression of a very shiny shoe, which in the case of the piece should be avoided because the material is supposed to be coarse leather, not smooth one. Last one is the upper body clothing. It probably has 2 shades greater than the rest of the piece. Just remember to put dark shading on armpits and the line for the chest itself. Then put another dark one (but lighter than the previous) as the area approaches the light.
Two types of shadows: solid and dithered. Whichever one you prefer. Just don't use pure BLACK. It'll look like your character is walking on oil. You may however, darken the color ...darker than what I used.
Added hair. Why did i use pure BLACK when i said you shouldn't? Well this is to show you how you should color in case you started with a "pure" one. In this piece, the BLACK color of the hair is the midtone. Instead it will be the dark tone. We should put lighter tones from now on as the hair area approaches light. Again, use a line gradient technique. Follow the shape of the hair. I also put a couple of white pixels there to indicate hair shine. How do i define my colors? Easy, i use the stepping method (additive and/or subtractive). For example, take the color of the pants. Let's say that's rgb(0,64,64). For the darker shade, i just subtract 20 for each value... making the dark shade a rgb(0,44,44). This method may vary however, depending on your desired contrast/saturation. For lighter shade i do the same. I add 20 for each value. By the way, in this particular piece, the constant i use is 40(+40,-40). Well, the sprite is acceptably finished. More professional sprites however, remove the black lines and use either AA (anti-aliasing), or sel-out (selective outlining). These are somewhat advanced concepts and we'll just tackle that some other time. The sprite we made is good anyways(don't you think?). All you got to do now is save it as a . That way you won't have to redraw everyone in your game. For example, all generic male NPCs could be derived from this sprite. All you got to do is give him hair and more clothes. Actually, most pixel artists make templates (or with underwear at least). **not** **do not**
**template** **nude**
Next, let us move to drawing the side view.
First of all, . To illustrate this point, observe the two pictures: **do not visualize drawing a side-viewed sprite as actually being viewed sideways**
Once again, our is located slightly above the sprite and therefore we are not going to draw a sprite viewed on a 0 degree angle. *camera*
As usual, create a canvas. This time, we won't really need a guideline to mark the center, but if you feel compelled to do so, by any means do it.
![](vault/documents/37.gif)
Draw the head. The initial location of the head will mostly be undesirable. It can really be tough at times to position where the head should go because the canvas is blank and we have no point of reference. Good thing we can move it around. My technique is I use the sprite facing south as the reference. Their heads are roughly at the same location.
The nose need not be protruding, unless that was your point. For generic sprites, noses are not important. Concentrate on the eyes instead, but to indicate the nose area, I encircled it for you.
The orange circle denotes the , the purple one is the , and the red circle is supposed to be the , but like before, the neck will not be necessary here. **nose** **mouth area** **neck**
I also placed the in a location that would make our sprite's face definitive. If you move it 1 pixel rightward or leftward, the result will tremendously change, you'll see. If you positioned it higher it would look awkward and you would violate our camera rule. If you lowered it it would touch the mouth area, which is very bad. **eye**
There is also an , which I don't do normally, but I did this just for experiment. We'll modify this as we go. **ear**
Draw the . Observe its distance from the jaw area. Observe the alignment of the shoulders and arms with the back of the head. Of course you may still adjust the arm as you prefer, and believe me when I say that I have undergone a lot of adjustments with his arm. Sometimes it is also better to draw the body first so you'd have a reference for the arms. **shoulders**
Draw the . The neck is not needed. Denote the chest as a more protruded area, but not too much or it will look like a breast. Observe how long the body is. **body**
The red circle denotes the , adjusting this is mainly up to your preference, but personally, it would look very bad if it were raised or lowered. **distance between the shoulder the neck area**
The purple circle denotes the sprite's area. If this were a woman we'd make this part bulging, or if this guy's muscular we can make this area protrude just a wee bit. If this guy is a thin guy we'll move the lines inward (which we shall do later). **chest**
The yellow circled area is the . Adjust accordingly depending on how fat your sprite is. **belly**
Between the blue and red lines is the area. If his arms should bend, we'll bend it at this point. **elbow**
The is 2 pixels away from the hand's tip. Should he walk and bend his knees we'll bend it at this point. **knee**
The size of the is again up to you, but based on the front view of this sprite, I think this is just enough. **feet**
Colored the base. We have completed a template! :)
We can further this piece by putting basic clothing over it. Just like the front view, I put a white shirt and a blue-green pants with brown shoes. Don't forget to observe the lines of the clothes-- the sleeves, the pant's length, and the collar.
![](vault/documents/42.gif)
I added the hair and colored it. We already covered this part so I need not explain how I color the hair.
Notice the ear. I changed it because I found this to be more appropriate.
All you have to do is shade it now and it's ready to go.
The side view is completed, but let me give you additional example. In this section I'd like you to observe the sprite to your right against the one on your left. The right one effectively achieved a look, did it not? All I did was reduced the chest and belly area, encircled in light purple. I also adjusted the shoulder rightward and moved it closer to the body area to get that I wanted to achieve. And since he is thin, the legs should also be trimmed. Encircled in red, observe how I adjusted the pants. *thin guy* *stiff look*
Finally there's the back view (or the North Direction)
It has been obvious (at least for me) that the back view is similar to the front view. Of course they are not the same but the proportions are undoubtedly similar unless you are making a hunchback. For this reason we are not going to start from scratch in making our back view, but if you feel like doing it form scratch then go ahead.
Let's start from the front view. We'll use this as our starting point:
![](vault/documents/45.gif)
Okay, we now make some adjustments. First, what parts are not needed here? We remove the eyes. Preferably I'd remove the collar, but this depends on the clothing, but if we are to make a nude template we'll remove this and the sleeves as well.
The butt area should be seen, contrary to the pubic area that we see now, so we'll modify the lines a bit to reflect the changes.
The feet should also be adjusted so that it would seem to be pointing northward instead of what it is now. To achieve such effect we just add a few pixels to the north of the feet.
Observe the modifications I made:
![](vault/documents/46.gif)
Well that was easy...and fast too! As you can see, all it needed was a bit of tweaking and here we have a new sprite facing the northern direction.
The purple circle indicates the of the sprite. Compare it with the front view sprite and you'll notice a slight change in position. It has been adjusted and moved inward placed nearer the body. **shoulder**
The red circle indicates the . Of course they are needed as breasts are needed for front views. But they may be omitted. **wing bones**
The waist line has been adjusted, and you can see the yellow encircled area, that it has been raised to denote the position at which the back is poised. A plain horizontal line will effectively denote the butt area, but you are encouraged to modify this depending on your preference and the character you are making.
Encircled in blue is the . You can see the difference with this one from the front view. A few pixels added and we have a foot facing north. You may also adjust the length of the pants, but I didn't see it necessary. **foot**
With clothes and colored, plus the hair.
Well that wraps it up for this edition. If you'll notice, I have no word about creating a sprite facing west. Truth be told it is obviously a right-side view flipped horizontally, so no need to discuss it all over. But for some sprites however, when the left side is not identical to the right side, like creatures with more elaborate designs, or someone similar to Batman's , you may need to redraw the other side of the sprite. *Two-face*
Keep tuned in and your fingers crossed. Pray that I would have more spare time so we can cover drawing walking sprites on all four direction, and then there's the isometric/diagonal directions.
I leave you with the following useable sprites. :D
(Requires Adobe Photoshop to be opened) [Download the template](http://www.toolkitzone.com/stuff/files/157/spriteTut.zip)
[![TBD](thumb.php?src=forum/images/avatars/http://www.boomspeed.com/ppandj112/muffin2.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=4691)
This is an exceptional article - great for beginning spriters especially! This really helped me out a lot. I hope to see more of this in the future.
[![TBD](thumb.php?src=forum/images/avatars/332517804416d4090b239e.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=2186)
This is pretty good khin, short. simple, and effective. its helped me create better sideview graphix already.
[![TBD](thumb.php?src=forum/images/avatars/854920603444e76d660439.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=76)
hell wish there would of been RPGCode tutorials as effective as this one is for drawing while I was code manager. You did a great job.
[![TBD](thumb.php?src=forum/images/avatars/20192717334761b60827deb.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=304)
Khin, when it comes to drawing, YOU ARE MY HERO!!!!!!!!!
Very good explanation on makeing characters thanks
[![TBD](thumb.php?src=forum/images/avatars/32165894248aedb3c1e269.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=3094)
Nice, good tutorial, I wish ther was a better 32 x 64 sprite tutorial
[![TBD](thumb.php?src=forum/images/avatars/20495816454164bd2fbe6ff.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=4351)
Great tutorial, now i can finish my sprite lol
I love you.
[![TBD](thumb.php?src=forum/images/avatars/1945424367429f22ad02913.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=6484)
this was actually the technique I was using before... the only thing I actually needed to know was shading awesome!TBD
[![TBD](thumb.php?src=forum/images/avatars/210510045843fe20869fac5.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=10096)
Yeah, it is very good, but i am a complete and total newbie and need a demenstration or something.
[![TBD](thumb.php?src=forum/images/avatars/126317573345e1e3a4d15c7.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=14610)
incredible tutorial! I don't know what I would've done without it!!!
Quick Jump
Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Editorials | -- Zone Awards | -- | -- 2008 | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
Keyword(s)
All Categories Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Editorials | -- Zone Awards | -- | -- 2008 | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
**Published**
December 7th, 2004
**User Rating**
![TBD](templates/default/images/icons/rating_blue_5.gif)
*1 vote cast.*
**Views**
360
