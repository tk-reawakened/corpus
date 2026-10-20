---
kind: forum-thread
id: "toolkitzone-forums/11427"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "11427"
title: "sending images"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11427"
written: "2004-11-17T01:07:00"
last_post: "2004-11-23T12:24:00"
date_confidence: "exact"
captured: ["20041226222918"]
author: "sivart"
repliers: ["Euix", "Levi", "Colosseus"]
authors: ["sivart", "Euix", "Levi", "Colosseus"]
posts_present: 12
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_128943_amp_", captured: "20041226222918", sha256: "cfdb93617c37066b73f2d82ede3a126ba6c0207577bda53b108493eed15ea4d3", wayback_url: "https://web.archive.org/web/20041226222918/http://www.toolkitzone.com/forums/viewtopic.php?p=128943&amp="}
links: []
---

# sending images

### sivart · 2004-11-17 01:07 · #B126075

Over a winsock connection... It's stumped me for a while on how do you send an image to a co-ordinate over winsock using RTB Its for my chat heh , e.g
: ) = Smile
Yea im still at the sending text stage of winsock..... anyway could someone help?Thanks ,
Travis

### Euix · 2004-11-17 01:25 · #B126095

You probably won't be able to just send an image over and expect it to show up in a richtext box. You could just open up an image file in binary mode.. then save all the data to a string.. then just send that string over winsock to the other end. Then the other end could 'reassemble' the data into an image file. After that, just insert the image into the RTB. I'm not sure how you'd do that though ;P
There's probably a much better way. I've never really looked into this. Try looking for something on PSCode.com.

### sivart · 2004-11-17 01:44 · #B126103

I found a working example of a blank chat style thing where you just type Smile and when you enter it a smiley comes up , its just sending it :S

### Levi · 2004-11-17 04:02 · #B126167

Well, yeah that would be the easiest way. That was next on my agenda. In fact just design your chat with the smilies graphics already inside the program. So that when it recieves something like Smile it will turn it into a graphic. Of course you'll need to search the string in order to do that but that should be easy enough.

### Colosseus · 2004-11-23 09:47 · #B128920

I know a way to send images - albeit in Delphi... It is in binary, though, as Euix described it, but binary IS the way to do it.

### Levi · 2004-11-23 10:02 · #B128922

Yeah if you wanted to send any old image sure. But look at his question, he wants to send simlies over the net. That's a waste of good sendign time. He simply needs to send the text and have the images already premade in the application itself. No sending of images necessary.

### Colosseus · 2004-11-23 10:28 · #B128924

Uhm... the "text" IS the binary data. That's what we've been saying all along. Look at MSN messenger. What if he wants to enable the user to have his own, custom smilies? Then the images would have to be sent. And sending the binary data for a tiny little smiley would be about as fast as sending the text that tells the application which image to use.

### Levi · 2004-11-23 10:47 · #B128929

I know how they work colosseus. In the end its all Binary data, from the position of your mouse to text or images sent on the net. I know that. Thats computer basics 101.
However the format of the image for a RTB to take is a BMP and though a small 25x25 image in binary from a BMP wouldn't be overly large in any way shape or form, in fact to call it large at all would be a laugh, it would still waste more time than is necessary. Because once you recieve the data you have to seperate it from the sting of regular text or have some way that the text before and after the image are sent seperatly, then reassemble the image into a new file on the recievers computer only to load it into memory for the RTB to use. That alone must take about .5 seconds. What a waste.
Now I never said that sending images was ridiculous only sending smilies. If they want custom smilies They could ask for their smilies to be placed into smilie packets that come with an application that they could use. I mean, what If I don't want to see their smilies? This allows for a standardization and makes personalization able to be seen by the reciever as well as the sender.

### Colosseus · 2004-11-23 11:17 · #B128933

Asking to have their smilies put in a package, wait for that, and then requiring others to have that package too would be a way bigger waste of time than sending them.

### Levi · 2004-11-23 11:33 · #B128938

A waste of time yes but this way there is a benefit as opposed to the other way. I mean, would I rather allow my users to send me a sick smilie of something nasty or force them to use premade smilies and limit what can and cannot be sent? I personally would prefer to limit them. It saves on time and prevents immature sick people from displaying things I don't want to see.
I belive that many IM's have gotten lax on this lately and I don't like it.
now a compromise could be made where you give the option of whether or not you as a user would like to recieve any data other than premade smilies and test. If its selected yes then it could send smilies over and such, if no then they'd have to stick with regular smilies.
Either way you'd have to have premade smilies built in. Which is the easiest course of action.

### Colosseus · 2004-11-23 12:12 · #B128941

I think we're getting closer in the way of thinking now. An option to choose whether or not to receive custom data from other users would be optimal. However, when we talk about receiving sick stuff from even sicker people, I think you would agree with me when I say that in that case it would be easier to just block the user than blocking custom images and such. Because as we all know, sick people can simply write sick stuff in normal text as well... Are we supposed to block text now, too? Wink

### Levi · 2004-11-23 12:24 · #B128943

Indeed, so another addition. Though you make a valid point there are rare times, or common for some people, where they are required to tolerate such people in so the ability limit what they can send is still a very good thing to have. A block user option simply being an extra option on top of what we already have listed.
Maybe even a custom filter option. Filters are easy enough to make if you don't mind them changing somethings fairly inaccuratly. I mean a poorly designed filter where ass is eitehr ignored or changed to butt suddenly you ask your friend what the assignment was and it would change it to ignment or buttignment. But one should never simply assume that all users that one user doesn't wish to talk to can simply be blocked or ignored. There should be some extras for those who wish to use them.
