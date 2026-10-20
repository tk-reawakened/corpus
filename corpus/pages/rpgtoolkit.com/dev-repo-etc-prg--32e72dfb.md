---
kind: page
id: "rpgtoolkit.com/rpgtoolkit.com/dev_repo/etc.prg"
site: "rpgtoolkit.com"
title: "Etc program"
original_url: "http://rpgtoolkit.com/dev_repo/etc.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20000902200033"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.com/dev_repo/etc.prg", captured: "20000902200033", sha256: "d1fbd022d882ee319304740edddc83e5c68d8673487137812a9785f38c412a0d", wayback_url: "https://web.archive.org/web/20000902200033/http://rpgtoolkit.com/dev_repo/etc.prg"}
---

# Etc program

```
*Etc program
*Version 2.1 Ext
*RPGCode extension
*Total new commands: {[(11)]}
*By Matias Colotto
*from Argentina
#Method HealingMaxHPVarity(mhpheal_Handle$,mhpheal_Base!,mhpheal_Increment1EachXMaxHP!)
{
#GetMaxHP(mhpheal_Handle$,toAdd!)
#toAdd!=toAdd!/mhpheal_Increment1EachXMaxHP!
#GiveHP(mhpheal_Handle$,mhpheal_Base!
#GiveHP(mhpheal_Handle$,toAdd!)
#Kill(mhpheal_Handle$)
#Kill(mhpheal_Base!)
#Kill(mhpheal_Increment1EachXMaxHP!)
#Kill(toAdd!)
}
#Method HealingMaxSMPVarity(smp_Handle$,smp_Base!,smp_Increment1EachXMaxSMP!)
{
#GetMaxSMP(smp_Handle$,toAdda!)
#toAdda!=toAdda/smp_Increment1EachXMaxSMP!
#GiveHP(smp_Handle$,smp_Base!)
#GiveHP(smp_Handle$,toAdda!)
#Kill(smp_Handle$)
#Kill(toAdda!)
#Kill(smp_Base!)
#Kill(smp_Increment1EachXMaxSMP!)
}
* Thanks, AWESOME SOFTWARE!!! Now i can do a healing method that increases
* with the LV!
#Method HealingLVVarity(lv_Handle$,lv_Base!,lv_Increment1EachXLV!)
{
#GetLevel(lv_Handle$,lvHandle!)
#GiveHP(lv_Handle$,lv_Base!)
#For(c!=0;c! < =lvHandle!;c!=c!+lv_Increment1EachXLV!)
{
#GiveHP(lv_Handle$,1)
}
#Kill(lv_Handle$)
#Kill(lvHandle!)
#Kill(lv_Base!)
#Kill(lv_Increment1EachXLV!)
}
* The above method is easy to use:
* First, heals Handle$ the value determined by Base! then
* for each Increment1EachXLV in the level count
* gives Handle$ 1HP..
* For example:
* #HealingLVVarity("Target",10,3)
* if Target's LV is 12
* then it heals 14HP!
* Or if target's LV is 16
* Then it heals 15HP!
* If you want this method give, for example, 5 more HP per LV, then
* put 0.2 in the third parameter!
#Method HealingDPVarity(hdp_Handle$,hdp_base!,hdp_Heal1EachXDP!)
{
#GetDP(hdp_Handle$,DP!)
#GiveHP(hdp_Handle$,hdp_base!)
#For(b!=0;b! < =DP!;b!=b!+hdp_Heal1EachXDP!)
{
#GiveHP(hdp_Handle$,1)
}
#Kill(hdp_Handle$)
#Kill(hdp_base!)
#Kill(hdp_Heal1EachXDP!)
#Kill(DP!)
}
* These methods are useful for guided tactics. I don't know
* how to do guided tactics, but... Ah, also for special
* moves!!!!
#Method DamageOne(don_Handle$, don_Damage!)
{
#CastLit(don_Damage!,lita$)
#lita$="-"+lita$
#CastNum(lita$,dam!)
#GetDP(don_Handle$,dest!)
#dam!=dam!-dest!
#If(dam!>=0)
{
#GiveHP(don_Handle$,dam!)
}
#Kill(dam!)
#Kill(don_Handle$)
#Kill(don_Damage!)
#Kill(lita$)
#Kill(dest!)
}
#Method DrainOne(dro_Handle$, dro_drainquantity!)
{
#CastLit(dro_drainquantity!,lit$)
#lit$="-"+lit$
#CastNum(lit$,drain!)
#GiveSMP(dro_Handle$, drain!)
#Kill(dro_drainquantity!)
#Kill(dro_Handle$)
#Kill(lit$)
#Kill(drain!)
}
*Method for getting the DP of anyone
*Ok, AWESOME SOFTWARE, this #GetDP method is far away from
*good use, but i can delete it if you create a new method
*#GetDP.
*Flip to User's guide for notes.
#Method GetDP(dp_Handle$,dp_dest!)
{
#RPGCode("dp_dest!="+dp_Handle$+"[defence]!")
#ReturnMethod(dp_dest!)
#Kill(dp_Handle$)
#Kill(dp_dest!)
}
*This gets the FP of anyone
#Method GetFP(fp_Handle$,fp_dest!)
{
#RPGCode("fp_dest!= [fight]!")
#ReturnMethod(fp_dest!)
#Kill(fp_Handle$)
#Kill(fp_dest!)
}
*Method to give a certain number of Max HP to someone
#Method GiveMaxHP(gmhp_Handle$,maxhp_to_add!)
{
#GetMaxHP(gmhp_Handle$,hismaxHP!)
#hismaxHP!=hismaxHP!+maxhp_to_add!
#MaxHP(gmhp_Handle$,hismaxHP!)
#Kill(hmhp_Handle$)
#Kill(maxhp_to_add!)
#Kill(hismaxHP!)
}
*Method that gives a certain number of Max SMP to someone
#Method GiveMaxSMP(gmsp_Handle$,maxsmp_to_add!)
{
#GetMaxSMP(gmsp_Handle$,hismaxSMP!)
#hismaxSMP!=hismaxSMP!+maxsmp_to_add!
#MaxSMP(gmsp_Handle$,hismaxSMP)
#Kill(gmsp_Handle$)
#Kill(maxsmp_to_add!)
#Kill(hismaxSMP!)
}
*Method that calculates the X% of a number
#Method Calc%(number_to_evaluate!,Quantity%placed!,destinyvar!)
{
#destinyvar!=number_to_evaluate!/100*Quantity%placed!
#ReturnMethod(destinyvar!)
#Kill(number_to_evaluate!)
#Kill(destinyvar!)
#Kill(Quantity%placed!)
}
*Report actualizations
*V 2.1 Ext
*.Added #Kill to Calc%
*"""""""""""""""""""""""""""""BEST UPDATE"""""""""""""""""""""""""
*V 2.1
*.Added #Calc%
*"""""""""""""""""""""""""""""BEST UPDATE"""""""""""""""""""""""""
*Improved US's guide(user's guide)
*V 2.0
*.This is only a bug-fix, but it is a REALLY BIG bug fix because
*i have a problem with ALL methods; names were repetitive. Also,
*i added #Kill(xxx!$) at the end of each method.
*"""""""""""""""""""""""FAR AWAY BEST UPDATE""""""""""""""""""""
*.Added contact and distribution info
*V 1.1
*.Added #GetFP
*"""""""""""""""""""""""""""BEST UPDATE"""""""""""""""""""""""""
*.Improved User's guide
*V 1.0 ECmp
*.#DamageOne will not heal someone
*"""""""""""""""""""""""""""BEST UPDATE"""""""""""""""""""""""""
*.Improved User's guide
*V 1.0 Cmp
*.Fixed a bug that affected 2 healing methods
*"""""""""""""""""""""""""""BEST UPDATE"""""""""""""""""""""""""
*.Improved User's guide
*V 1.0 Ext
*.Fixed a bug that caused #GetDP don't work well
*""""""""""""""""""""""""""""BEST UPDATE""""""""""""""""""""""""""
*V 1.0
*.Added GiveMaxHP & GiveMaxSMP
*"""""""""""""""""""""""""""BEST UPDATE"""""""""""""""""""""""""
*.Improved User's Guide
*.Added DP support to DamageOne
*V 0.3 Cmp
*.Added Recommendations in User's guide
*"""""""""""""""""""""""""""Best update""""""""""""""""""""""""""
*V 0.3 Ext
*.Added HealingDPVarity
*"""""""""""""""""""""""""""Best update""""""""""""""""""""""""""
*V 0.3
*.Added a GetDP command
*"""""""""""""""""""""""""""Best update""""""""""""""""""""""""""
*.Improved User's guide
*V 0.2 Cmp
*.Added User's guide
*"""""""""""""""""""""""""""""Best update"""""""""""""""""""""""""""""""
*V 0.2 Ext
*.Now you don't have to enter a negative value with DamageOne and DrainOne.
*"""""""""""""""""""""""""""""Best update"""""""""""""""""""""""""""""""
*V 0.2
*.Added DamageOne and DrainOne
*.Fixed a bug that caused that if you use any of the healing
*methods, it sets the HP.
*"""""""""""""""""""""""""""""Best update"""""""""""""""""""""""""""""""
*.Added HealingLVVarity (Hey, this one isn't soooooooooooooooooooooooo long!!!!!(the name))
*User's guide
*Contents
*1.Healing Methods
*1-0 HealingMaxHPVarity *1-1 HealingMaxSMPVarity *1-2 HealingLVVarity
*1-3 HealingDPVarity *2.Damage Methods
*2-0 DamageOne
*2-1 DrainOne
*3.Aditional character Methods
*3-0 GetDP [wonderful!]
*3-1 GiveMaxHP *3-2 GiveMaxSMP *3-3 GetFP [wonderful!]
*4.Variable manipulation
*4-0 Calc% *5.Contact info
*1-0 HealingMaxHPVarity
*Syntax:
*HealingMaxHPVarity(Handle$,Base!,Increment1EachXMaxHP!)
*Gives Base! hps to Handle$, and for each Increment1EachXMaxHP
*in Handle$'s MaxHP, heals an extra 1.
*Example:
*#HealingMaxHPVarity("Frap",5,5)
*If Frap's Max HP Were Then Heals
*50 15
*100 30
*2000 405
*Other example:
*#HealingMaxHPVarity("Frap",10,10)
*If Frap's Max HP Were Then Heals
*80 18
*84 18
*125 22
*5400 550
*Recommended:
*LV learned Base! recommended Exponent recommended
*12 5 16-15
*32 20 15-13
*61 58 13-12
*100 80 12-10
*______________________________________________________
*1-1 HealingMaxSMPVarity
*Syntax:
*#HealingMaxSMPVarity(Handle$,Base!,Increment1EachXMaxSMP!)
*Same as above, but with the max SMP.
*Recommended:
*LV learned Base! recommended Exponent recommended
*15 6-9 8-10
*42 25 6-9
*100 75 5-7
*______________________________________________________
*1-2 HealingLVVarity
*Syntax:
*#HealingLVVarity(Handle$,Base!,Increment1EachXLV!)
*Same as above, but with LV.
*NOTE: It will not work with enemies!!
*Examples:
*1: #HealingLVVarity("Frap",5,2) 2: #HealingLVVarity("Target",0,8)
*If Frap's LV were Then heals If target's LV were Then heals
*10 10 5 1
*105 57 44 5
*200 105 240 30
*NO RECOMMENDATIONS
*______________________________________________________
*1-3 HealingDPVarity *Syntax:
*#HealingDPVarity(Handle$,base!,Heal1EachXDP!)
*Same as above, but with DP.
*NOTE: Elabored using #GetDP . Flip to the #GetDP
*section and if it says something that it will
*not work, then don't use it in this command!!!!!
*Recommended:
*LV learned Base! recommended Exponent recommended
*14 6-9 5-6
*47 31-37 4-5
*100 70-85 4-6, but also 3
*______________________________________________________
*2-0 DamageOne
*Syntax:
*#DamageOne(Handle$,Damage!)
*Takes Damage! hps from Handle$, but using DPs.
*NOTE: If #GetDP don't work, this command will not work!!!
*Example:
*#DamageOne("Tano",10)
*Takes 10 hps from Tano.
*______________________________________________________
*2-1 DrainOne
*Syntax:
*#DrainOne(Handle$,drainquantity!)
*Same as above but with SMP.
*______________________________________________________
*3-0 GetDP
*Syntax:
*#GetDP(Handle$,dest!)
*This is a WONDERFUL method, anyway, i'm too sorry, it doesn't work with
*enemies...
*First of all, make sure that the character has his DP in the variable "Handle$[defence]" (This can be set in the character editor).
*And now, you can use this command!!
*NOTE: It may work with enemies, but you need to make variables like "MyEnemy[defence]"
*Hint: Create a program with all enemies'variables and when you want to use this command simply put a #Include command.
*_________________________________________________________________________________________
*3-1 GiveMaxHP *Syntax:
*#GiveMaxHP(Handle$,maxhp_to_add!)
*This command gives maxhp_to_add of MaxHP to Handle$.
*Example:
*#MaxHP("Target",50) *Target's max HP is 50.
*#GiveMaxHP("Target",8) *Now is 58.
*_________________________________________________________________________________________
*3-2 GiveMaxSMP *Syntax:
*#GiveMaxSMP(Handle$,maxsmp_to_add!)
*Like above, but with the max SMP.
*_________________________________________________________________________________________
*3-3 GetFP *Syntax:
*#GetFP(Handle$,dest!)
*Gets the FP of Handle$ and places it on dest!.
*This command works almost exactly that #GetDP, but you need to have a variable "Handle$[fight]!".
*_________________________________________________________________________________________
*4-0 Calc%
*Syntax:
*#Calc%(evaluate!,%toput,dest!)
*This command evaluates evaluate! value and puts the %toput% into dest!.
*Example:
*#varprb!=50
*#Calc%(varprb!,20,desty!)
*#MWin(desty!)*Will show 10.
*_________________________________________________________________________________________
*5.Contact info
*Feel free to distribute this without selling. If you want to sell this,
*send me 25 us dollars OR 5 extensions of Pokémon cards to:
*Matias Colotto
*2974, San Juan, 9ºA
*Cod. Postal: 1232
*Buenos Aires, Argentina
*You can send me messages on the RPG Toolkit Message board, or
*via E-mail to
*(redacted: email)
*Thanks!
*Matias Programming S.A.
*Matias
*'''''''''''''''''''''''''''End of guide''''''''''''''''''''''''
*
```
