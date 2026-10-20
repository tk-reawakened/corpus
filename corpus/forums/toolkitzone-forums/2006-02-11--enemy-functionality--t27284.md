---
kind: forum-thread
id: "toolkitzone-forums/27284"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "tkgaming"
skin: "phpbb2"
thread_id: "27284"
title: "Enemy Functionality"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27284"
written: "2006-02-11T00:51:00"
last_post: "2006-02-14T18:12:00"
date_confidence: "exact"
captured: ["20060307043844"]
author: "UltimaWizard"
repliers: ["Colin", "Stephen", "MrB", "Z", "Hamster", "Johnstein", "venstor"]
authors: ["UltimaWizard", "Colin", "Stephen", "MrB", "Z", "Hamster", "Johnstein", "venstor"]
posts_present: 14
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_297137_amp_3Bsid_40935223b093a968c6e24c3a365290cb", captured: "20060307043844", sha256: "0c22ee41a6657e435457bf8bef72c28803446fb9b9a4d001bcbd40fc3f9b768d", wayback_url: "https://web.archive.org/web/20060307043844/http://toolkitzone.com/forums/viewtopic.php?p=297137&amp%3Bsid=40935223b093a968c6e24c3a365290cb"}
links: []
---

# Enemy Functionality

### UltimaWizard · 2006-02-11 00:51 · #B296659

I've been playing lots of games lately to prepare myself for programming the BS to Ander's Journey. I've noticed somethings that can make a game's gameplay better.
First: The power of enemies. I think most enemies are too weak. In most games, you can 1-hit-kill or 2-hit-kill enemies...they're not really all that strong. If there's a Death mechanic in the game, but most of the enemies are too weak to do enough damage to kill you before they are the ones killed, what's the point of programming it? Why not just be a good version of Sephiroth?
Now, I don't advocate random encounters that have boss-battle difficulty in every battle...just make battles harder some. Add about 5% of ATK, DEF, HP, SPD, everything to an enemy...and give your BS a run. If enemies can do damage to you, you can work on making your level design more challenging and tweak the game to make it a more fulfilling experience.
Second: The IQ of enemies. I know your average snail, wolf, or highly advanced mechanoid...well, is a black-market thug with an IQ of 3...but does it HAVE to be that way? For your basic enemies, they should be able to tell a hero in critical condition (i.e. one in a fetile position with open wounds) from a perfectly healthy and dangerous goodie, and attack the weaker one...I'm currently implementing a solution to this in the AJ AI programming...but I think that more games should take a look at random encounters and don't just have them to break up the story's monotony with 'gameplay.' The word game implies 2 things: randomness and challenge. For most games, I ask this: where's...either?

### Colin · 2006-02-11 01:13 · #B296671

Enemies generally are meant to wear down the player's party, not provide any serious threat from one battle.

### Stephen · 2006-02-11 01:21 · #B296673

Also, I don't know if this is available right now, but is it possible to make some areas on a board have certain enemies and other areas have different?

### UltimaWizard · 2006-02-11 01:24 · #B296674

Yes. But that's the general problem with enemies right now--they don't really even succeed in wearing down heroes to start with, as you usually have recourse to both healing and restorative magic. Unless you're an oddball like me and choose to only introduce an attack and restorative mage in the later parts of the game when you need one, enemies are no challenge, really not even an annoyance.
Besides, lets be reasonable. I'm an OK swordsman in real life (I'm not kidding, I train with Saber, rapier, and am beginning to take up some Kendo...strange stuff O.o), but even I would think twice about attacking a bear with 3 friends...or even worse, 4 bears with 3 friends. If they had rifles and we could one-hit kill them (or mortally wound them, anyways), we might stand a chance.
Of course, that's now put me down a completely diffrent path than what I originally intended to emphasize: the functionality of magic.

### MrB · 2006-02-11 14:45 · #B296789

I agree that the average game has too easy of random enemies. I don't really agree with increased IQ though. If anything, it takes away the fun moments of having a character almost dead and praying that the enemy will pick someone else.

### Z · 2006-02-11 14:50 · #B296793

**MrB wrote:**

> I agree that the average game has too easy of random enemies. I don't really agree with increased IQ though. If anything, it takes away the fun moments of having a character almost dead and praying that the enemy will pick someone else.
>

True, It's just an RPG Style though, most RPGs (Even Commercial ones) Do this.

### Hamster · 2006-02-11 16:18 · #B296810

also it would be cool that, when encountering a really really really weak enemy(like the ones found on the first few boards when you just start playing the game), if you were high level and really strong, that the enemies would just run away(earthbound has that). that way you wouldnt have to worry about wasting time and stuff fighting things that you could kill 5 in one hit.

### UltimaWizard · 2006-02-12 05:50 · #B297137

That's something I'm doing with my AI scripts...actually, I'm working on a dual AI level/emotion routine for all entities, NPCs included. If an enemy is really weak, and it sees an equally powerful ally cut down in one hit, it (and any enemy of the same power, really...) will run for their lives. All you have to do is make one quick hit, and boom. Enemies go bye-bye.
Of course, the Duel System in Ander's Journey also kind of neutralizes the weak enemies' weaknesses...as if you botch your attack, the enemy can deal you decent damage...meaning be careful of weaker enemies, as even they can pose a threat if you blow them off. Especially considering how you start off with Antidotes, and I don't wait 30 minutes to introduce the Poison ST-ATK. (Petrify is a spell effect only in mine...Sleep is ignored, because it's useless.)
Point is, if you've read this, try beefing up all your enemies a little. Don't overdo it, but make the game more interesting.
Just don't make wolves be able to drop broadswords. First, it cracks me up, second, it raises too many wolf-anatomical questions.

### Johnstein · 2006-02-13 05:13 · #B297439

the issue you run into with RPG's and battles is that sometimes it feels contradictory to slow down your story with lots of tough battles, but to also make the battles challenging enough that you feel a sense of accomplishment when you get through them.
when you make each battle tougher, then you have a greater chance of dying more often, requiring you to replay areas over and over again... which can really frustrate a player... UNLESS of course, the game's goal is to be a real challenge. in that case, the story has to reflect that by developing a story that can still be interesting if presented at a slower pace.
as for AI. as long as the game's BS and story complement each other, the AI would be a pretty flexible feature. and personally, if you want to go for realism, a weaker player would attack with lower damage, therefore I would want my enemies to attack the *stronger* players to weaken them and make them less effective Smile but like I said, AI is flexible.

### UltimaWizard · 2006-02-13 06:14 · #B297459

**Johnstein wrote:**

> As for AI. as long as the game's BS and story complement each other, the AI would be a pretty flexible feature. and personally, if you want to go for realism, a weaker player would attack with lower damage, therefore I would want my enemies to attack the *stronger* players to weaken them and make them less effective Smile but like I said, AI is flexible.
>

And that, my friend, is why AJ is gonna have about 7 diffrent AI scripts...5 of which I've conceptualized. I might even add more. You never know! AI is flexible.

### venstor · 2006-02-14 02:10 · #B297782

I kind of like the idea of each battle potentially ending in defeat. Enemies that don't necessarily just overpower your characters, but having enough strategy involved that if you make a stupid move, it can cost you. Having a save system like Dark Age 2 where it automatically saves before each battle can cut down on the frustration factor and just allow you to focus on outwitting your enemies each battle. Battles are just more fun for me if there's a sense of danger and I'm engaged in planning a strategy instead of just continuously pressing the same attack key.
Random encounter rates should be set low. Even if your battle system is fun, there can be too much of a good thing.

### Z · 2006-02-14 02:20 · #B297796

**venstor wrote:**

> I kind of like the idea of each battle potentially ending in defeat. Enemies that don't necessarily just overpower your characters, but having enough strategy involved that if you make a stupid move, it can cost you. Having a save system like Dark Age 2 where it automatically saves before each battle can cut down on the frustration factor and just allow you to focus on outwitting your enemies each battle. Battles are just more fun for me if there's a sense of danger and I'm engaged in planning a strategy instead of just continuously pressing the same attack key.
> Random encounter rates should be set low. Even if your battle system is fun, there can be too much of a good thing.
>

Hmm, you just gave me an idea to put in my BS. Thanks Venstor, you got my Appreciated man vote next time around Wink

### Johnstein · 2006-02-14 04:22 · #B297906

**venstor wrote:**

> ...Having a save system like Dark Age 2 where it automatically saves before each battle can cut down on the frustration factor and just allow you to focus on outwitting your enemies each battle...
>

that would be a good way to do it probly. I've also seen some games where when you lose, you have to start all over, but you get to keep your exp, and/or gold/items. so yea, you have to start over, but the next time you'll be stronger. but really, just as long as the feature works with the gameplay and story, I'd say pretty much anything could work... so long that it fits Smile

### UltimaWizard · 2006-02-14 18:12 · #B298079

With Ander's Journey (at least, my future releases... Wink ), there's no such thing as a 'random' encounter--you see generic models roam around on the boards and fight actual formations in battle, a lot like in Tales of Symphonia, the inspiration for that...and most of my boards are gonna be WIDE open--you can evade fights if you don't want to fight, and if you do managed to get sucked in, you can always bug out with [Flee]...see that topic for more.
Anyways, I'm making the enemies tough(er) to reinforce the realism of my game...they'll still be pretty much pushovers, as Colin was right--the point of enemies is to wear the party down, not to pose a serious threat, even though the enemies you face will be threatening enough if ignored.
The moral of the story? Think before and while you act.
