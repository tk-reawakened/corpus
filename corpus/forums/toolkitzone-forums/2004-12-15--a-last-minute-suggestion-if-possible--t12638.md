---
kind: forum-thread
id: "toolkitzone-forums/12638"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "12638"
title: "A last minute suggestion if possible"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12638"
written: "2004-12-15T01:36:00"
last_post: "2004-12-19T03:01:00"
date_confidence: "exact"
captured: ["20050119211734"]
author: "????"
repliers: ["Dont_Think_So", "Compugeek", "Akura_TheDragonBlader", "MightyLink", "tacofernandez"]
authors: ["????", "Dont_Think_So", "Compugeek", "Akura_TheDragonBlader", "MightyLink", "tacofernandez"]
posts_present: 10
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139808_amp_", captured: "20050119211734", sha256: "e9f99cbc974f93abe665b24ed6596c07f5ea610bc94a9c609a0762771e656570", wayback_url: "https://web.archive.org/web/20050119211734/http://www.toolkitzone.com/forums/viewtopic.php?p=139808&amp="}
links: []
---

# A last minute suggestion if possible

### ???? · 2004-12-15 01:36 · #B139803

I think that toolkit installer should have an uninstall option, for when there is a new toolkit release, you can uninstall the old one and install the new one

### Dont_Think_So · 2004-12-15 01:40 · #B139808

The "Delete" button should do nicely.
Although, this is a much-needed feature because the TK now assigns FileTypes, and it wouldn't be good to have people edit their registry.

### Compugeek · 2004-12-17 02:48 · #B140947

I think KSNiloc just added that. Although you don't really need to uninstall the old version, just overwrite it.

### Dont_Think_So · 2004-12-17 04:46 · #B140996

Yeah, he did.

### Akura_TheDragonBlader · 2004-12-17 18:19 · #B141113

**Dont_Think_So wrote:**

> The "Delete" button should do nicely.
> Although, this is a much-needed feature because the TK now assigns FileTypes, and it wouldn't be good to have people edit their registry.
>

Just open any folder, go to View/Folder options, go to the File types tab, go down to the RPGCode Program file entry, and hit Remove. ...An uninstaller would be easier Confused.

### MightyLink · 2004-12-18 03:57 · #B141386

I know TK3 is allready released but you gata make a patch adding the #System.Pause command to it. I hate using #Wait because alot of important info gets skiped wile a character is walking. I dont know why you excluded #System.Pause from TK3 but its the only reason why I went back to TK2.

### tacofernandez · 2004-12-18 04:06 · #B141396

The Pause method comes in the system.prg file that comes with the Toolkit. So if you want to use system.pause, you need to put this file in the necessary folder.

### Dont_Think_So · 2004-12-19 02:43 · #B141906

As far as I know, System.Pause is still there.
If not, System.prg from TK2 should work equally well with TK3.

### MightyLink · 2004-12-19 02:53 · #B141911

no i tryed, #system.pause dont work, and if i replace the tk3 system file with the tk2 one, wont i lose some of the tk3 features like pixle movement and stuff.

### Dont_Think_So · 2004-12-19 03:01 · #B141914

No. System.prg just contains all of the System methods, like Pause.
