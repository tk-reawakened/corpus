---
kind: doc
id: "toolkitzone.com/96"
site: "toolkitzone.com"
title: "Published"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=96"
written: "2007-01-25"
date_confidence: "day"
updated: "2007-01-25"
captured: ["20081220052848", "20081220052848"]
author: "Khin"
repliers: []
authors: ["Khin"]
comments_present: 0
f_author: "Khin"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_96", captured: "20081220052848", sha256: "1427a48b84d359faff94401dd7dcd49a739b830e06f84de03fae4c83550f8c53", wayback_url: "https://web.archive.org/web/20081220052848/http://toolkitzone.com/library.php?mode=read&doc=96"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_96-e4f0af", captured: "20081220052848", sha256: "1427a48b84d359faff94401dd7dcd49a739b830e06f84de03fae4c83550f8c53", wayback_url: "https://web.archive.org/web/20081220052848/http://www.toolkitzone.com/library.php?mode=read&doc=96"}
---

# Published

Browse
Sprite Drawing Tutorial: Walking Sprite
This time around we are going to make our sprite walk. Our walking animation is designed to be simple: only three frames per direction. The frames will be based on the standing templates that we have created before. All we have to do is move around some parts like the shoulders, arms, feet, legs, and so on.
Alright, let's start.
We start off with this standing pose that we did earlier. Take note of the markings i made. The red circle is the shoulder. If he is to walk and step on his right leg, the left shoulder should move backwards. Please remember that although not exactly simulated, normal human walking behavior must be convincingly mimicked. That means when you use your left leg to step forward, your right arm would swing to your behind/back. Doing it otherwise would result into an undesirable walking animation.![](vault/documents/62.gif)
The blue circle indicates the elbow. If the arm should bend it will bend at this area.
The purple circle denotes the knee.
You can also see a pinkish/magenta line that extends horizontally. That's the shoulder level. It is destined to change as our sprite walks.
Let's draw the first step. First, look at teh shoulder line. It has become slanted now. That's because the sprite's left arm was swung forward. As a male, our sprite should move its shoulder when walking. Females normally do not exhibit this because they move they're arms, although at times they move their shoulders too. You can see the circles haven't changed. I left them intentionally for you to realize where the previous parts are located. Just cut out some pixels on the right leg, take note of the knee area, and you have a leg that moved rearward. The other leg that moves forward does not really differ form the standing leg, although it did get wider. The ral illusion that worked here is the foot. You can see that the foot was changed. It is used this way to denote that the character is stepping forward.![](vault/documents/63.gif)
Now the hands are not aligned. They really shouldn't be. One of them must be raised, and the other one must be lowered. Do not retain any of the hand nor feet position from the standing sprite. It shall defeat the purpose of animating it...so change as much parts as possible. Be reasonable when changing though. Only the parts that move should be the ones changed, of course.
The head is unchanged . Why? Because it shouldn't be. If we are doing a realistic animation it should move at some point , but this is just a 32x32 sprite, so no need to bother. The head stays as it is based on the standing pose.
You can think of this as a complete mirror of the previous piece. There will be no problem here since there's not much detail yet. But if the sprite already has hair, and detailed clothing, plus shading,![](vault/documents/64.gif) **do not flip it.**
The markings were kept to show you the original location of the parts. Note that the shoulder line has shifted to the other direction.
Now it's time for the sideview walking. Taking our reference from the standing view, I encircled the shoulder for you. This will move along with other parts of the body. Of course other parts will move but this one will have the greatest change overall. Here's why:
When the sprite walks and steps its right toe, all you have to do is draw some pixels on the locations you see above. The origin of the legs will not change, but the same could not be said with the shoulders. The left shoulder shall move at least a pixel leftward(our left) to indicate its movement. The right arm's origin is not tha same as the left one. They both had their origins adjusted. Just like in our front view walking animation.
When the other toe is used, the situation is reversed. Still, both arms have different virtual points of origin. You may also wonder why on the pic at your lefthand side, the guy's right leg seemed to connect too high from the butt. Take note: . It only looks as if the origin of the right leg is wrong, but it's not. If you lowered it, the perspective impression would change. **we are viewing the sprire in semi-top down orientation**
Now for the rear view animation. Not much to explain, because it's basically the front view animation, with a different drawing.
I encircled the ear in dark red and the hand in blue. They're both barely recognizable. Feel free to horizontally adjust the position of the toe that moved towards you.
Well I hope that was informative enough. All you need really uis look at the examples and study them. I just explained some things to help you out. Here's some more templates:
[![TBD](thumb.php?src=forum/images/avatars/20192717334761b60827deb.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=304)
I don't have a chance to read it but if its as good as the first one, i'll save it to my desktop.
[![TBD](thumb.php?src=forum/images/avatars/320771715488180b7095cb.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=1374)
khin, you have the front walking all wrong. Looking at your sprite walking south the left and right arm are going forward with the left and right leg. left-left right-right, should be left-right right-left
[![TBD](thumb.php?src=forum/images/avatars/42619274844250d6db4794.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=157)
my goodness!! You are totally correct. I have to do something..hmm..maybe I'll make a public apology.. tnx for that Kabuki.
TBD
[![TBD](thumb.php?src=forum/images/avatars/138364227142d5d1203ebc6.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=5898)
Opposite arms come up, Khin.
[![TBD](thumb.php?src=forum/images/avatars/2743431824393be4ec16cd.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=21)
I wouldn't say its "all" wrong. Its not that hard to change it yourself you lazy bums (jk).
Quick Jump
Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Editorials | -- Zone Awards | -- | -- 2008 | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
Keyword(s)
All Categories Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Editorials | -- Zone Awards | -- | -- 2008 | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
**Published**
December 22nd, 2004
**User Rating**
No votes cast.
**Views**
172
