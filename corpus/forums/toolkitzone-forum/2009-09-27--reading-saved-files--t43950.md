---
kind: forum-thread
id: "toolkitzone-forum/43950"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "43950"
title: "Reading Saved Files"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=43950"
written: "2009-09-27T21:31:00"
last_post: "2009-10-12T08:50:00"
date_confidence: "exact"
captured: ["20100102024157"]
author: "Geep4W"
repliers: ["playsoon"]
authors: ["Geep4W", "playsoon"]
posts_present: 4
pages_present: [2]
pages_total: 2
posts_per_page: 10
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 10, url: "http://toolkitzone.com/forum/viewtopic.php?t=43950", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_483422", captured: "20100102024157", sha256: "cd09537f86743e32951bd30a3aacf1a7fef1358828d5822e5ae1f527c4d347ff", wayback_url: "https://web.archive.org/web/20100102024157/http://toolkitzone.com/forum/viewtopic.php?p=483422"}
links: []
---

# Reading Saved Files

> [!missing] gap:1-10 · http://toolkitzone.com/forum/viewtopic.php?t=43950 · never-captured
> Page 1 of 2 was not recovered.

### Geep4W · 2009-09-27 21:31 · #K482869

Thank you jackyboy. I appreciate the help.

### playsoon · 2009-10-09 10:47 · #K483368

Not sure if you figured it out or not yet, but this is what I currently use to check if a saved file exists and if it doesn't it creates the saved file.

**Code:**

```
///////////////////////////

//Checks if a file exists//

///////////////////////////

method fileExists(file, folder)

{

   setErrorHandler(:error);

   openFileInput(file, folder);

   closeFile(file);

   return true;

   :error

   return false;

}
```

False is returned if the file does not exist.

**Code:**

```
////////////////////////////////////////////

//If files doesn't exists, file is created//

////////////////////////////////////////////

tempsave1Used$ = fileExists("temp1.sav", folder$) //folder$ = "Saved" while playing in the toolkit

                                                  //editor. Change folder$ to "" when ready for                                                            //.exe packaging to read the saved files                                                                  //properly.

if(tempsave1Used$ == false)

{

   Save("temp1.sav")

}
```

Sets the variable tempsave1Used$ to true or false. If false, creates the save file.
I also noticed that when you save a game it seems to save within the .exe. Which is why it doesn't show up in the Saved folder. So when checking if the saved file exists while in the editor the folder$ spot should be "Saved", and while playing the exe the folder$ should be left blank, "". Reading saves, saving, and loading all work for me this way. And none of my saves are "deleted".

### playsoon · 2009-10-11 23:00 · #K483422

The save files don't show up in the Saved folder, just like you had said. But they seem to be somewhere because I can close the exe, reopen it, and the saved games are still there. The folder that I have the fileExists() method checking isn't the Saved folder. I don't completely know how it's working but it is... and saying that it seemed to save in the exe, was the only way I could try to explain this one.
I should be letting out a demo of a game I've been developing over the past couple months soon. That way you could see that it's not showing the saved games yet they are still there.
Also I don't use dirSave(). My game only allows for 3 saves. Each of which is created when you save the game on a designated save spot.

### playsoon · 2009-10-12 08:50 · #K483426

My main operating system is Vista, but I am developing my game in Windows XP using a virtual machine. Since my Vista seems to only run versions 3.04 down, that is how I must make it. Maybe the virtual machine doesn't delete those files in the appData folder?
