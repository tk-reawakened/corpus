---
kind: page
id: "mrgoldsoft.mysticsoftware.net/mrgoldsoft.mysticsoftware.net/shack/bstut/bstut2.htm"
site: "mrgoldsoft.mysticsoftware.net"
title: "Styles"
original_url: "http://mrgoldsoft.mysticsoftware.net/shack/bstut/bstut2.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20020705153008"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/mrgoldsoft.mysticsoftware.net/shack/bstut/bstut2.htm", captured: "20020705153008", sha256: "019d0e78cda73a14280dd0bdc0e9461d8b263a94d68c5def5b4d0ba05ef0c4c7", wayback_url: "https://web.archive.org/web/20020705153008/http://mrgoldsoft.mysticsoftware.net/shack/bstut/bstut2.htm"}
---

# Styles

Battle System Tutorial Part One
* Battle System Theory: The Ins and Outs of Battle System Design
>
> **Introduction**
>
> MrG Says:
>
Welcome to MrG and the reluctant Triuken's unofficial Battle System Tutorial! Hopefully this guide will assist everyone wanting to write their own custom battle system for the RPG Toolkit 2.0. This task, though I'm not telling you it's easy, is achievable through hard work and understanding. Hopefully we'll de-enigmatize this task, and let everyone who wants to expand this fantastic program even further than it already is.
Just one last note before I turn it over to my comrade; coming in, you will probably need a fairly basic knowledge of RPGCode. Not anything overly extensive, but you'll need to know what things like variables and commands are, as well as knowing what #If and #MWin and typical things like those do. If there is anything overly complicated, don't worry, we'll explain it. You can count on us to de-enigmatize your life as much as we possibly can.
>
> Triuken says:
>
Yep, we finally decided to get off our lazy arses and create a comprehensive guide to creating the BattleSytem of your dreams! We will attempt to provide the basic information you need to know before you venture where few have gone - creating the Custom BattleSystem. I recommend you have a simple understanding of the many aspects of RPGCode; by this, I mean Variables, #While and #If and such.
>
> MrG Says:
>
Now this part of the tutorial has a lot of writing in it, and is mainly concerned with battle system theory and how to build a good battle system. If you know exactly what you want and have it all scripted out in your mind, I would still reccomend taking a gander at some important concepts here like balancing and stuff, but you might want to skim on ahead and check out the battle system programming tutorial.
**Styles**
>
> MrG Says:
>
Styles bascially means what kind of battle you are having rage out there on the fields and forests of your land. There are many different choices, ranging from realtime or turnbased, stationary or moving, front view, side view, etc. All those neat little things that add spice and uniqueness to your very own battle system. There are many different styles that already incorporate such factors, and a few of these console battle system styles are the ones we hope to outline here.
>
> Triuken says:
>
There are a wide array of Styles, each of which are unique in their own aspects. My first piece of advice is to choose a battle type, and stick with it. You won't have to worry about being un-original, because, remember, you always have the oppurtunity to implement distinquishing features which separate your BattleSystem from the rest. We will now present a short outline of the styles used in the console games we have grown to love ('cept for MrG, the anti-video game groupie..). Remember, be creative!
>
> ** *FF6 - The Default and the Classic*
> ![](ff6.gif)
>
> MrG Says:
>
Basically what we already have in the TK is what FF6 style is. Though I have never had the chance to play any of these highly acclaimed video games, Triuken assures me that this is what the TK models it's battle system after. The only reason I can think of why anyone would want to change this is to skin [replace the base graphics with your own graphics] them or to modify the stat system and AI [Artificial Intelligence - What the enemies do on the battle field] a little bit. Luckily, the TK has a lot of flexibility in it's base battle system, so you won't have to rewrite everything for little things like this. However, if you are planning on a huge-scale modification of a normal FF6 system, you'll want to read on. Triuken?
>
> Triuken says:
>
The FF6 [Final Fantasy 3/6] Battling Style is usually regarded as the "Classic Style", as it is what many other RPGs mold their Battle Engines after. I personally prefer this setup to the others - its simple interface and turn-based action provides enjoyment in any battle. As my drunk friend notes, this is the default System for the TK, and it is recommended you stick with the defaults if you're new to the 'Kit. Skin the BG/border, experiment with AI and custom Stats; after all, the ToolKit was built on flexibility, and that includes the Internal BattleSystem. Let's move on. =)
>
> ***FFTactics - It's All About Range***
> ![](basic-throw-spec.gif)
>
> MrG Says:
>
Like my typically creatively starved title suggests, the main factor in a FFTactics battle system is range [the measure of distance between enemies and players]. While the other battle systems let the player always attack and basically treat the entire battle like the player and enemies are right next to each other the whole time, in a FFTactics system, you must manuever your player(s) into good attack and defense formations, adding a whole new layer of strategy. Mmmmm, strategy. Short range attacks must be made when the player is one unit, square, tile or whathaveyou away from the enemy, and long range attacks (bows, certain magic, etc.) can be done from as far away as they individually allow. Everything else (such as stat setup, which we haven't gotten to yet) remains the same, though a player's range is often an important factor in their overall skill makeup. For instance, we wouldn't want that bulky dwarf having the same range as the light, springy elf, would we?
On a personal note, my cat Fluffy died last week, but this tutorial is not about my cat Fluffy. On another personal note, this FFTactics system is what Triuken assures me I have modeled one of my own battle systems after, though, having never played the game, I cannot make any huge assumptions. I am however, something of an expert in these types of BS's, and will be happy to answer questions about it if you are making a FFTactics system.
>
> Triuken says:
>
*wipes tear* Poor Fluffy.. *sniff* Anywho, the FFT [Final Fantasy Tactics] style adds a whole new level of challenge, including pre-emptive planning your attack modes. For those of you who haven't played FFT, think Mystaria, Shining Force, and SIM RPG Maker (G: Or chess. A very good RPG.). You will need to lure your opponents and launch your attack when at the perfect distance, range. Different spells and attacks can span multiple blocks [long-range] or short one-way hits [short-range]. If you are wondering why I write so little compared to MrG, well, MrG has waaay too much time on his hands. *cough* =)
>
> MrG Says:
>
"We have so little to do and so much time to do it!" - Willy Wonka. Though he later corrected himself, I find it more appropriate in in it's original format.
** *RPG95/2000 - Staring Down Your Opponent*
![](010.gif)
>
> MrG Says:
>
There's really not much to say about the Toolkit's popular competitive engine's battle system. It's really only FF6 style, but done in first-person [straight ahead, as opposed to side or bird's eye; think Doom, Unreal, 3D, etc.]. I've never used this ugly, blasphemous engine but other people have, and you might be partial to it's fighting style. I'm sure Triuken has more comments on the subject, though he'll probably just use his space to gleefully blast my ignorance. The story of my life.
>
> Triuken says:
>
What can I say? It's simply FF6 with a different view - you fight face to face, not side to side. If you haven't used RPGMaker '95, think Phanasty Star... and God Bless you.. *ahem*. This sytem basically follows the same outline as FF6, 'cept for the Enemy view.
>
> MrG Says:
>
So basically there is no need to recreate this, because in the TK you have the option to fight your battles from a front view. Delicious, no?
>
> ***Lunar - d) All of the Above***
> ![](screens02.jpg)
>
> MrG Says:
>
Well, when Triuken and I originally sketched this out, he told me a Lunar battle system was, and I quote: "FF6 and FFTactics mixed together". Though it may be the result of brain damage due to past intoxication or simply a lack of ability to de-enigmatize Triuken's statement, I can't really tell you what this means. Perhaps my co-writer can.
>
> Triuken says:
>
Okay, I think everybody here has played Lunar, but, if not, I'll try to explain it. Lunar uses the side-to-side view of FF6, yet still retains the in-depth strategy elements of FFT, such as range. Characters launch their attacks as usual, as they march forward on the scene. Some attacks require Range as a crucial factor, while others, such as most spells, aren't effected by range. I doubt anyone would attempt to recreate this system exactly, because, frankly, it would be unoriginal.
***Zelda - Realtime, real action***
![](zelda.gif)
>
> MrG Says:
>
Zelda systems (realtime systems, really, but I'll refer to them as Zelda systems from now on simply because I don't like typing out wordy concoctions, and I called my battle system a Zelda system) are based primarily on two important factors: Combos and realtime action. Now, realtime is notoriously tricky to get right in the TK, but my early tests of my Zelda battle system prove it can be done. Combos don't work very well, however, because of the Toolkit's sensitive key handling.
In case you didn't know, combos are special moves, spells, or whathaveyou that you can use from bashing a certain key combonation. Think of fighting or skatboarding games [Tony Hawk, Trickstyle] to get the right idea.
**Stats**
>
> MrG Says:
>
Often the key to successful, challenging, balanced battles in your game lies in the kernel of the battle system: The stat system. Stats can range from the simplistic, basic variety [such as the base TK stats: FP, DP, HP, and SMP] to huge, complicated lists of stats and skills [for you PC players, think Daggerfall, Fallout; huge non-linear affairs that require many different venues of ability to make it through the game]. Basically, what it comes down to is how much micro-management you want in your system. Are you more focused on deep, involving storylines and gameplay, or large, epic-scale, complicated battles. Or commas. I find commas especially gratifying. Anyway, we will now attempt to outline some of the more basic stats you can find in most battle systems, and how and what they affect.
>
> MrG Says, Again:
>
The following four stats are probably the most common of any battle system you'll find (yes, I did just put in that again to use a comma; mmm, commas):
-- Offensive power: I.e AP
>
> MrG Says: Attack power, or AP, or FP, or whatever. This is basically just your common strength stat. It basically detirmines how much damage you're going to do.
>
-- Defensive power: I.e DP
>
> MrG Says: Again, a very basic stat. Your defense stat, the thing that shields and the like enhance. It basically detirmines how much damage you'll be able to keep them from doing.
>
-- Health measurement: I.e HP
>
> MrG Says: Here is an appropriate place for a desicive and emphatic duh. Health stat, this measures whether your dead or not, because you obviously couldn't tell by yourself.
>
-- Magic or special measurement: I.e MP
>
> MrG Says: This basically just encompasses all special stats out there. Magic, aura power, Force power, etc. This is generally a good place to flex your creative muscles and think up a system that gives a certain amount of flair and interest to an otherwise textbook battle system. Magic systems aren't something we'll go into here, as they are pretty much unique for your game. If you want to make a custom battle system, but can't think of any magic system to use, we pity you. But in this case you'll probably want to copy some other style's magic system, which we will (later) try to teach you how to do.
>
--Specials
>
> MrG Says: Depending on your system, you may have a variety of special stats that affect your performance in both battles and normal gameplay. Let's take a look at them.
>
> -Speed
> MrG Says: The major influence in turn-based battles because whomever's speed is the highest is the one that gets the first turn.
> -Magic Attack (Intelligence) / Defense (Willpower) MrG Says: Basically just a measurement of your special stat power attack skill and defense skill. -Personality MrG Says: This one really has no affect on battle systems, but it's a common enough stat that we thought we'd throw it in. This stat is usually used in the player's realtions with NPCs and is often an important factor in getting into places and may even keep you out of or get you into a battle or two. -Agility, Dexterity, etc. MrG Says: These are alternative physical skills used to figure in the amount of extra attack or defense power you have. The best way to look at these stats as two other possible variables in your equations, so you won't just have a cookiecutter Damage = AP - DP kind of equation. -Endurance MrG Says: Endurance is often used to figure in the amount of damage inflicted upon your player; i.e higher endurance results in more damage and lower endurance in less. Like adrenaline (see below), this stat can be used to give a more realistic, human feel to your stat sets. -Range MrG Says: Range is the single-handed culprit that is responsible for your more movement based battle systems such as FFTactics. Basically it's figured in with weapons and the like to see close far away the enemy has to be (on a grid) for them to inflict damage. If you really wanted to get complicated, you could even go so far as adding a "fading" effect to your range; i.e some arrows can go 5 units away but inflict less damage than if they were 4, 3, or even 2 units away. It can be done, but you'll have to ask yourself how complicated you want to get. -Luck MrG Says: Triuk's most foully detested stat. This adds basically just a random factor to your battle system, opening the window for a lucky shot here or an absurd miss there. Use with caution, as it can be a bigger balance upsetter (see Equations) than any of these other stats listed. -Adrenaline MrG Says: My personal favorite. This stat is used to get more of that human factor [reactions and events that would normally happen in real life] in your battles. It's generally best used as a boost when you're very close to winning or as a last ditch wild attempt to save your own skin when you're close to dying. Again, use wisely, because if the effects are too powerful, it can upset balance very quickly. -Fatigue MrG Says: The opposite of adrenaline, fatigue is used to drag down your power through the fact that you're bone tired and you haven't slept since that time the three-headed dragon woke up your peaceful slumber in the marble dungeon while you were dreaming of this sentence and wondering whether or not it was a run on. Basically, this is just a realistic stat to be used to figure in tiredness in the human body. It also serves well as an offsetter of the sometimes unbalanced adrenaline stat.
>
> **Equations**
>
> >
> > MrG Says:
> >
>
Ah, the all-important equations section. Just how do all those lovely RPGs figure out how much damage you or the aforementioned unfortunate ogre (try saying that three times fast) inflict upon one another? Through an often complicated, or sometimes deceptively simple set of equations.
Before your eyes start to glaze over and your mind is filled with terrifying visions of old algebra classes, hear me out. These equations aren't really hard to figure out, they actually make sense, and involve no animals or bored old teachers. Besides, if you put just a little thought and cleverness into your equations, you can make a sound, solid, and all-importantly original battle system.
Also, always remember that stats must be balanced and in preportion with one another so that there are no radical effects from your equations that have major impact on the battle from one side or another (unless of course you want it this way, but if your default equations heavily favor either the player or the enemy, the game gets real boring, real fast; so if you want a particuarly scripted event, simply beef up the stats of the enemy/player etc. Don't mess with your equations). For instance, make sure all your HP stats are high enough to take the damage from your AP stats, and make sure your APs are high enough to affect real damage on the HPs. Also, be careful when including random elements, because they can upset balance rather quickly.
>
> MrG Says:
>
What follows is a list of the standard situations in which an equation would be appropriate. Of course, there are probably far more situations in which you'd need another equation, but these surve as a good base. For example, what about magic damage? How do you figure that? Well, perhaps Magic AP - Opponent's Magic DP + Fatigue or something. Onward we go.
--DAMAGE: AP - Enemies DP
MrG Comments: Very simple. The attack power minus the defense power. Ta-da. --RUNNING AWAY: Standard: 70% Variety: Physical skills + Random between 1 and 10 > Enemy physical skills MrG Comments: The standard is very easy. A seventy percent chance of running away. The variety is a crazy concoction Triuk and I came up with. It's a little more realistic measurement; take your physical skills (i.e how in shape you are determines how fast you are) and a random number to toss a very small random factor in, and see if that's more than the enemy's physical skills (i.e ability to catch you). Of course, you could just have speed as the only physical skill, as well.
--IF THEY HIT FACTOR: Boring: Hit%. Starts at 60% and increases by 1% every level. Realistic: You'll want to balance this out with your physical skills, using whatever combonation you see fit. Perhaps your agility and dexterity can be measured on a scale from 1 to 100 (i.e based on percentages) and you can combine the two and divide by two for a decent hit percentage. MrG Comments: I'd personally go with the realistic because an all-encompassing Hit factor seems very conconcted and unrealistic to me (though this is what some old video games use.) Remember to factor in the accuracy of weapons and special moves as well. As usual, you can get as complicated or uncomplicated as you like here. Some games, like Fallout, have a lot of depth on measuring accuracy and unaccucy based on weapons, physical skills, situations, etc. while others sort of follow a "hit or miss" principle. --DYING: Standard: Err.. When HP reaches < = 0 Interesting: When HP at 10%, 10% drop in all stats But when at 2%, 40% *increase* in all stats to simulate adrenaline MrG Comments: As you might have noticed by now I like adrenaline very much. I like adrenaline for breaskfast, for lunch, and to mix with a light brandy for an after-dinner nightcap. Anyway, the interesting varation is a play at the simulation of real-life affects and situations. I reccomend playing around with this a bit (as with all equations) to make sure it feels right and seems to have the effect you want on your battles. --TURN: Standard: Speed Interesting: ??? MrG Comments: Though believe me I have tried, I have yet to come up with anything more effective than a simple speed variable for affecting what players go in what order. Take my advice, and stuck with this proven formula.
--LEVELS--
>
> MrG Says:
>
A sub-category, because levels aren't really an equation, but do factor in your stat and equation set. I personally don't use levels, relying rather on a Daggerfall-esque "if you use the stat it goes up" system, but I do know that most all RPGs use levels (cough..and take the easy way out..cough). So here is how you do it. First off, always give the option to the user on how to level up. It's quite boring to stick in a certain increase on certain stats every time you level up. This takes a lot away from the "Role Playing" nature of the game, because if you do this the user doesn't get to craft the kind of character he wants. It's far better to give them a specific number of points (or percentage) and allow them to apply that to whatever stat/skill they want. Speaking of points or percentage, there are generally two ways to go about levelling up. They're called linear and exponential. Linear bascially means you add a set number of points to each stat every time you level up, and exponential means you increase these stats by percentage (i.e if your exponential increase was 50% every level up, you would be able to add 2 points to a stat with 4 points). Therefore, you could give the player x number of points in a pool, or x number of percentage to overall increase stats. There are a couple methods to make leveling up more interesting. One is used in Chrono Cross, where you only level up after you defeat bosses. Bascially the idea is to make levelling up a compelling reward and not a mudane thing that you get tired of after a while. Think of some new creative way to apply it to make it something the player would want to achieve. Or don't. The other school of thought on this is generally one that works too: If it is a mudane, routine thing that isn't too easy to reach, and gets subtely harder as you go, with rewards and goals a'plently, ordinary leveling up can make for quite an addictive experience, as the popular Toolkit game Godiva:Alpha shows. Another method that I mentioned in the first paragraph that I like, is more of a realistic method. Namely, you only increase a stat or skill whenever it's used. For instance, if you pick a lock, your locking picking skill is increased. If you bash a troll with a sword, your strength stat and sword skill increases. Now doesn't this make sense? Finally, remember that experience generally governs when you level up (unless you're going by a more realistic system like the one described above), and the player generally gets this experience by defeating baddies around the land. Also, quests provide a convienent place to add experience and experience in quests provides a nice extra reward aside gold or items or what have you.
**Conclusion**
>
> MrG Says:
>
Well, that pretty much wraps up battle system theory. I think this is a pretty decent overall guide to the finer points of crafting your battle system and making it fun and effective for your players. Now, of course, you will want to know how to program it. Well, for that, you can simply advance to the next section (once I get it done) and you will be well on your way. Seeya there!
