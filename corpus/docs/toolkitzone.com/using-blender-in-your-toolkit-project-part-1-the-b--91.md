---
kind: doc
id: "toolkitzone.com/91"
site: "toolkitzone.com"
title: "Using Blender in Your Toolkit Project - Part 1: The Blender Interface By Juggernaut"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=91"
written: "2005-08-05T17:09:00"
date_confidence: "exact"
updated: null
captured: ["20060312120241", "20060612021319", "20060612021319"]
author: "Juggernaut"
repliers: []
authors: ["Juggernaut"]
comments_present: 0
f_author: "Juggernaut"
f_date: "August 5, 2005, 5:09 pm"
f_description: "As the blender rush continues with Toolkit projects, Juggernaut offers his introduction to the software, taking a look at the interface."
f_section: "Art & Graphics"
f_title: "Using Blender with Your Project"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_91", captured: "20060312120241", sha256: "454c5884798198037a18b1bc9e96a804b032e53cc75e40dfb275788d2260e5c1", wayback_url: "https://web.archive.org/web/20060312120241/http://toolkitzone.com:80/library.php?mode=read&view=cadd&doc=91&PHPSESSID=bdcceeefceef8ff863ad82d0d089ece4"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_91", captured: "20060612021319", sha256: "d522223337c3bea0beb00d30cad3f68aebcf0c1b3a9cd7efb341b5832d675dc0", wayback_url: "https://web.archive.org/web/20060612021319/http://toolkitzone.com/library.php?mode=read&doc=91"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_91-85004c", captured: "20060612021319", sha256: "d522223337c3bea0beb00d30cad3f68aebcf0c1b3a9cd7efb341b5832d675dc0", wayback_url: "https://web.archive.org/web/20060612021319/http://www.toolkitzone.com/library.php?mode=read&doc=91"}
---

# Using Blender in Your Toolkit Project - Part 1: The Blender Interface By Juggernaut

- After two rewrites(due to some pretty ridiculous mistakes on my part) it's finally here, my Blender tutorial. I have been an avid Blender user for the better part of a year now(being previously experienced in other modelling enviroments). By far it is one of the best I encountered, and being free, it is definitely one of the most amazing. Everyday I find something new I can do with it, or some new feature that does just the trick for the job. Whenever I feel like I know almost everything about it, the devoted development team throws me another version packed with new features. Another aspect of Blender that allows to overcome most any limit is it's integrated support for Python scripts. There are hundreds of useful scripts out there for just about every function you can imagine. The main program comes bundled with a very useful scripts package. I have never been restricted in my creativity when using Blender.
- In this tutorial, you will learn about the basics of the Blender Interface, and how to configure it to create a more productive workflow, then I will teach how to create a basic object and give it a material(in this case, a color). First, you will need to download the program from . The latest version as of writing is 2.37. There will be a link on the homepage that takes you directly to the download. It will have 2 options, a full installation package and a zipped folder. I highly recommend you download the intallation, because the zip won't install Blender onto your system, and you will have to access the unzipped folder each time you want to start it up. [**Blender3D.org**](http://Blender3d.org)
- After installation, a console will popup. It will say something about Python and "Import Site Failed". Though you can ignore this, don't exit from it, it will close the entire program. Blender should begin to run, and you'll get this screen(without the numbered boxes and circles of course): This is where the magic happens.
![](library/images/docs/680.jpg)
**Part 1 - Introduction to the Interface**
- As you can probably tell, there is A-LOT of buttons. Now, before you shut off your computer and go cry in a corner, there is something you must know. You will never have to use most of these buttons, and the ones you do use will generally only ever need to be used once in a while.
- One of the Beautiful things about Blender is that you almost never need to use the on-screen buttons. Everything can be accessed through keyboard shortcuts. This makes the workflow much faste. There is one rule of thumb amongst the Blender community. Keep one hand on the mouse and one on the keyboard. Another blessing is that all the diffrent sets of tools that serve a specific purpose are compacted into seperate "Windows" and "Panels"(you'll learn more about these later). At first, this is one of the most confusing aspects about Blender to new users, but you'll will soon find that it isn't as confusing as you think. In fact, it is so well structured that you will likely come to prefer the setup. Now for the explanation of the interface.
- At the top left of the interface, boxed in red(#1) is the task bar inherent in nearly every windows program around. The only button you'll ever use up here is the 'File' button. This gives you access to save and load functionality, and a few other functions that will become useful in time(append is one being most important). But otherwise you won't need any of the other menus up here.
- Next is that big window outlined in blue(#2). This is the Modeling Window. This is where you create an object of your fancy and move, scale, rotate, and otherwise manipulate it. You will spend most of your time here. Wait a minute, there is stuff already in here. Don't worry, these are created by default when you start a new project. We'll worry about them later.
- The green box(#3) runs along the bottom of the Modeling Window and outlines the 'Window Buttons'. Most of these determine how you work in the Modeling Window and how it is displayed.
- #4 is that big yellow box at the bottom. This is called a 'Panel'. A panel is just a set of tools for performing a specific task. The one currently displaying is called the Render Panel, this is where you specify how the pictures you make will output. You can change settings like size, file type, quality, output location, Oversampling(OSA, or Anti-Aliasing), motion blur, gamma correction, cartoon edges, etc. You will not use most of these buttons, and the ones you do use are one time settings.
- Just above the Render Panel toward the center are the Panel Buttons. It is outlined in gold(#5). Each panel has it's own set of these. What they do is allow you to access specialized tools for that panel. The two that are not pressed you will likely never need unless you are making cinematics(and even then, I have never needed them).
- To the left of that is a purple box(#6). These are the Panel Selection Buttons, where you select which panel to display. Though there are six of them, you will probably only use three of them in most cases. You'll probably also notice the three icons circled in blue. These are Window Selection Menus. You will be introduced to these when it is needed. Otherwise, you can ignore them.
- The one menu, with the purple oval around, will be used in the next part about how to configure your workspace.
**Part 2 - Configuring Your Workspace**
Wow, sorry if that information is overwhelming, but trust me, it will help just to know where everything is when I start throwing instructions at you. Don't turn back now.
- Blender's default workspace configuration is fine and dandy, but the one viewport isn't really flexible enough for regular tasks, so we're going to change it. Remember that button circled in purple? It should say "SCR:2-Model". If you click the double arrow icon, a drop down box appears. These are "Screens", or rather diffrent workspace configurations. They don't change how blender functions, just how everything is placed. Blender gives you four of these "screens" to start you off(Animation, Model, Material, Sequence), bit you'll never need to use them, because you are going to create your own.
- In the drop down menu, there is also and 'ADD NEW' selection. Click this. The name probably changed to something like "SCR:2-Model .001". Click on the name, and a red editing cursor appears. Delete(backspace) this(SCR: won't erase, this is OK). Now type in '5-2pt Model' and hit enter. Now when you access the dropdown menu, your 'Screen' appears on the list. But wait a minute, it looks exactly the same. We're going to fix this now.
- Normally, the 4 window setup(top, front, side, perspective) is the default workspace in a modeling enviroment, but this doesn't give you much space to work in, and it is hard to keep a handle on for most beginners. So we are going to take a 2 window approach. This is the setup I use most. So, we are going to need to split the one Modeling Window into two.
- Move your cursor up to the top edge of the Modelling window, it will turn to the resizing icon(a double arrow). Move it roughly to the center of the top edge(easiest way to center it is by lining it up with the green line of the grid). Right click and a dropdown menu appears. Select 'Split Area'.
- There finished, right. Wrong. We now have two windows, both showing the same exact view. What good will that do us? They are both in the Top view setting, or rather, the viewport is looking down on the objects. We are going to change this so that the left window is a front view, and the right window is a side view. Make sure your NumLock is active(it is always good to have it on when using Blender).
- Move your mouse so that it is over the left window(inside of it) and press 1 on your NumPad. The viewport has jumped to the Front view. Now positon your mouse in the righthand window and press 3 on the NumPad. It has jumped to the side view. If you ever need them back in the top view, it's as easy as positioning the mouse in the window and hitting NumPad 7. Make sure they are in Front and Side view right now and hit CTRL-U on your keyboard. What this does is save your default settings(Your selected workspace configuration, rendering options, and other things. Be careful not to change any of the settings before saving, you may regret it later). Have you pressed CTRL-U? Good, now exit Blender and open it again. There is your Workspace configuration.
- Now we are going to creat a basic object.
**Part 3 - You First Object**
- Now that you have a brand spanking new workspace, we are going to create a sphere and change its color. First, we are going to delete the box in the middle of the window. RIGHT Click near one of its edges, it becomes pink. hit X and click 'Erase Selected'. Now it is gone.
- Move your mouse into either of your Modelling Windows. Press the spacebar. A menu appears under the mouse. Now select Add->Mesh->UVSphere. Another dialog box appears up under the mouse. It says 'Segments: 32'. Click OK(and again when it asks "Rings: 32", and Whammy. You now have a sphere in your modeling windows. Not very significant, but this is one of the biggest steps a first timer can make.
- Now you can see all of the points(vertices) that make up the sphere. These are currently highlighted yellow. Right now you won't need to use these, so we are going to exit 'Edit Mode'. The Window Buttons(Green, #3) has a small box that currently says 'Edit Mode'. Click the double arrow icon next to it to access the menu and select 'Object Mode'. Now the sphere is completely highlighted pink.
- Hit the F12 key. A new window pops up and a picture of your sphere is drawn. Exit this window. Now to give it some color.
- Remember the Panel Selection Buttons(purple box, #6), click on the one that looks like a highlighted sphere. You are now in the Materials Panel. This is where you'll give you're objects texures, maps, and apply images to it. There are two tooboxes. 'Preview', which is empty, and 'Material'. In the 'Material' toolbox, click the button that says 'Add New'. You now have 4 toolboxes. Right now we'll only worry about one of them though.
- Changing the color of the object is the simplest way to change it's materials. Some materials can get to be very complex. A good example is doing a blood splatter. You can create a simple material with a color and a picture of a blood splatter. Or, you can make an extremely realistic material with a color map, bumo map, specularity map, and a reflection map all in one. For most applications you won't need to get this detailed though.
- To change an objects color, simply click on the grey colored box that is circled in green. A color selection dialog will appear(you should know how to use this). Select the desired color and hit enter. Now hit F12. The redering window appears again, and now the sphere is whatever color you chose.
Well, I hope you learned something today. Next time we'll learn how to model a basic scene, and how to export it for use in the RPGToolkit.
Happy Blending, The Juggernaut
corim123
August 9, 2005, 8:24 pm
NICE, very true and straight to the point can't wait for the next, keep it pumping!
Paper
September 27, 2005, 1:30 pm
Why use blender?
Fuzzman
December 1, 2005, 7:51 pm
Why not?
Lord_Valanx
April 6, 2006, 9:23 pm
Were can i get this program?
As the blender rush continues with Toolkit projects, Juggernaut offers his introduction to the software, taking a look at the interface.
May 2, '06
Apr 5, '06
Dec 7, '05
Oct 25, '05
Aug 7, '05
