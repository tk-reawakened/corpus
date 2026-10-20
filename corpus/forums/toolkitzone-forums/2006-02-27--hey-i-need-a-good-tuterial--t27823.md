---
kind: forum-thread
id: "toolkitzone-forums/27823"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "27823"
title: "Hey! i need a good tuterial!"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27823"
written: "2006-02-27T20:10:00"
last_post: "2006-03-02T17:02:00"
date_confidence: "exact"
captured: ["20060321081819"]
author: "Lars141"
repliers: ["DrakeLord", "tc", "Walker-san"]
authors: ["Lars141", "DrakeLord", "tc", "Walker-san"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_302790_amp_3Bsid_02410647d8764ea16352521b482ef8b0", captured: "20060321081819", sha256: "84a1b2b7f8782a032ad61581626502b2f114b11de60f14400c4806252e7a7c67", wayback_url: "https://web.archive.org/web/20060321081819/http://toolkitzone.com/forums/viewtopic.php?p=302790&amp%3Bsid=02410647d8764ea16352521b482ef8b0"}
links: []
---

# Hey! i need a good tuterial!

### Lars141 · 2006-02-27 20:10 · #B302108

Hey!
Im Dutch...
I can speak English but its better for me to speak Dutch.
So is there someone that can write me a good tuterial?
ty!
Lars141

### DrakeLord · 2006-02-27 23:31 · #B302162

For one thing, what type of tutorial?
That would help...

### tc · 2006-02-28 09:15 · #B302257

if i know what kind off tut I can wright one in dutch i think

### Walker-san · 2006-02-28 10:10 · #B302265

I would assume something on the TK, and being in the code forum, a tutorial on RPGCode...
but that would be common sense....and there is no sense around here.

### Lars141 · 2006-02-28 16:34 · #B302307

I need a Dutch tuterial for making NPC's, i need a Dutch one for making items, and a Dutch one for makin a boat for crossing the water

### tc · 2006-03-02 17:02 · #B302790

om te beginnen, een van de belangrijkste dingen bij programeren is bedenken wat een programma moet doen, dan bedenk je wat voor comaando's je nodig hebt.
NPC
bij de NPC's wil je ze waarschijnlijk laten praten dus heb je mwin() of een zelfgemaakte tekst commando. een programma voor een npc zou er als volgt uit kunnen zien:

**Code:**

```
mwin("hoi ik ben een NPC") //om hem iets te laten zeggen

wait() //nu wordt er gewacht todat er een toets ingedrukt is
```

om dit programma met een NPC te gebruiken maak je een item via de item editor. ze geeft hem de graphics van je NPC. je vinkt het vakje met Board-driven aan. dan kan je op het vakje edit drukken, daar klik je dan op. dan bij het vak Program to run when picked up: vul je de programma naam van hierboven in. als je je NPC wil laten rond lopen dan doe je in het veld daar boven wander.prg in, die zit als het goed is standaart in de map prg
items
hier gaan we eerst kijken wat de item moet doen, of het bijvoorbeeld een zwaard is of een levens drakje om je hp weer terug naar normaal te brengen.
bij het voorbeeld van een zwaard (werkt het zelfde voor een helm en dat soort dingen, je past alleen een paar kleine dingen aan) begin je met het maken van een nieuw item in the item editor. je vinkt het vakje equipable aan. je drukt op het edit vakje wat klikbaar geworden is. daar kies je waar de item equiped kan worden, in het geval van het zwaard wordt het left hand en right hand, omdat je een zwaard in beide handen kunt dragen. een zwaard zorgt er meestal voor dat je meer damage doet dus vul je bij efects of equipping item in het vakje fp increase by (fighting points) het aantal fp wat hij omhoog moet gaan je kan er van alles van maken en als het zwaard je slapper moet maken vul je er een negatief getal in.
en bij het voorbeeld van het levens drankje (werkt ook bij een smp drankje, je moet wel weer kleine aanpassingen maken)vinkje het vakje menu driven aan en druk je op edit. dan vul je in het vak effects of using item in health increases by het getal van het hp wat er bij moet en als er hp af moet vul je er een negatief getal in.
boot
een boot maken is niet al te moeilijk. je begint met het maken van de graphics van de boot met player erin. dan maak je een player met de boot graphics die sla je op als boot.tem of iets wat er oplijkt. dan als je speler de boot krijgt dan laat je dit programma draaien:

**Code:**

```
boot! = 1 //slaat 1 op in variable boot!
```

dan als de speler het water in wil lopen dan stop je op de water vakken het volgende programma:

**Code:**

```
if(boot! == 1) //kijkt of je een boot hebt

{

newPlyr("boot.tem") //geeft de player het uitlijk van een boot met de  //player erin

}

else() //als het bovenste niet waar is wordt het volgende gedaan

{

mwin("je hebt geen boot") //laat een tekst zien

wait() // wacht tot er een toets is ingedrukt.

}
```

dan zet je op de vakje langs de kant (als de speler weer op het land komt) het volgende programma:

**Code:**

```
newplyr("normaleplayernaam.tem")// normaleplayernaam is de naam

//van het bestand van de orginele speler van hoe je hem genoemd hebt
```

ik hoop dat helpt
