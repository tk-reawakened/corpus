---
kind: forum-thread
id: "toolkitzone-forums/22839"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Programming"
skin: "phpbb2"
thread_id: "22839"
title: "MySQL query help"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=22839"
written: "2005-08-25T09:12:00"
last_post: "2005-08-25T13:32:00"
date_confidence: "exact"
captured: ["20051031003948", "20060108015009", "20060108021119"]
author: "Colosseus"
repliers: ["Xavier"]
authors: ["Colosseus", "Xavier"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_249934_amp_3Bsid_0cf693abe1e4a3c7d4d75a608ec292a0", captured: "20060108015009", sha256: "77915011c99da8ac15ce8f44639cee70d4490fa4fd7931bfa34401b5ff96959a", wayback_url: "https://web.archive.org/web/20060108015009/http://www.toolkitzone.com/forums/viewtopic.php?p=249934&amp%3Bsid=0cf693abe1e4a3c7d4d75a608ec292a0"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_249958_amp_3Bsid_0cf693abe1e4a3c7d4d75a608ec292a0", captured: "20060108021119", sha256: "78f15a5d00de9df96c96cbe24b6aa104e42bbef37cea471d816ac4f19b05df9e", wayback_url: "https://web.archive.org/web/20060108021119/http://www.toolkitzone.com/forums/viewtopic.php?p=249958&amp%3Bsid=0cf693abe1e4a3c7d4d75a608ec292a0"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_249973_amp_3Bsid_9cb115aff7d3b8ba5814f106b2283f26", captured: "20051031003948", sha256: "17e906f410c6602082df7bf41b08c9226eeb4abc135823d60977d56ace5183d5", wayback_url: "https://web.archive.org/web/20051031003948/http://www.toolkitzone.com/forums/viewtopic.php?p=249973&amp%3Bsid=9cb115aff7d3b8ba5814f106b2283f26"}
links:
  - {url: "http://www.w3schools.com/sql/default.asp", status: "external", local: null}
---

# MySQL query help

### Colosseus · 2005-08-25 09:12 · #B249934

Okay, I'll be short - I need a MySQL search function. I have a form, in which the user types a string. This string is then used to search in a table named "items", which has the form "item_blabla", "item_blablabla", and so on. What is particularly interesting now, though, is the "item_name" field, which is a 255-character long VARCHAR field.
Here's the thing: I need a query that searches the table for records where the "item_name" field contains the string submitted from the search form ($_POST['search'] for your information).
Here's some pseudocode to provide some clarity around what I want:

**Code:**

```
select * from items where item_name contains $search
```

Anyone have any ideas for me?

### Xavier · 2005-08-25 12:06 · #B249958

I highly recommend actually reading some very, very basic information on SQL because that's all you need to perform such a simple query. A good set of pages for beginners are [here](http://www.w3schools.com/sql/default.asp).
Obviously the = sign would be to find a matching string, but the SQL term LIKE can be used with % used as a wildcard. Simple stuff.

### Colosseus · 2005-08-25 13:32 · #B249973

I actually looked at the LIKE function with its wildcards, but it seemed to me that LIKE would only find things following the conditions set by their wildcards, and not what I wanted - something that can find anything containing the string, no matter its placement in the sentence. But okay, I'll look further into it. Thank you Smile
EDIT: Yes, it seems as if though my research on this subject was too crappy once again. It works fine now. Thanks for letting me waste your time anyway Wink
