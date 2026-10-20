---
kind: page
id: "tkworld.mysticsoftware.net/tkworld.mysticsoftware.net/rpg/data2.ibf"
site: "tkworld.mysticsoftware.net"
title: "\"+Copy+\""
original_url: "http://www.tkworld.mysticsoftware.net/rpg/data2.ibf"
written: null
date_confidence: "unknown"
updated: null
captured: ["20050409030728", "20050409030728"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/tkworld.mysticsoftware.net/rpg/data2.ibf", captured: "20050409030728", sha256: "7b05c8e46a121c5270faff4e5ce1fa88378786416586e47e80ada708200815c5", wayback_url: "https://web.archive.org/web/20050409030728/http://www.tkworld.mysticsoftware.net/rpg/data2.ibf"}
  - {path: "wayback/mysticsoftware.net/www.tkworld.mysticsoftware.net/rpg/data2.ibf", captured: "20050409030728", sha256: "7b05c8e46a121c5270faff4e5ce1fa88378786416586e47e80ada708200815c5", wayback_url: "https://web.archive.org/web/20050409030728/http://www.tkworld.mysticsoftware.net/rpg/data2.ibf"}
---

# "+Copy+"

" Build += " \n" Build += content document.getElementById('ucpcontent').innerHTML = Build document.title = title } } function theUserNumberRequiredByTheMenu() { a=document.getElementById("userlinks").getElementsByTagName("a")[0]; if(a.href.match(/showuser=(.*)/)) { return RegExp.$1; } else { return "1"; }} function BuildRPGMenu(){ RPGMenu = new Array(); RPGMenu[RPGMenu.length] = new Array("Profile","RPG Profile"); RPGMenu[RPGMenu.length] = new Array("Donate","Donate Money"); RPGMenu[RPGMenu.length] = new Array("Shop","Itemshop"); RPGMenu[RPGMenu.length] = new Array("Bank","The Bank"); RPGMenu[RPGMenu.length] = new Array("Healing","Healing Center"); RPGMenu[RPGMenu.length] = new Array("Synthesis","Synthesis Shop"); RPGMenu[RPGMenu.length] = new Array("Equip","Equip"); RPGMenu[RPGMenu.length] = new Array("BattleGround","Battle Ground"); RPGMenu[RPGMenu.length] = new Array("SkillPoint","Skill Points"); RPGMenu[RPGMenu.length] = new Array("TT-Shop","RPG Triple Triad Shop"); RPGMenu[RPGMenu.length] = new Array("TT-Battle","RPG Triple Triad Battle Ground"); RPGMenu[RPGMenu.length] = new Array("TT-Tutorial","RPG Triple Triad Tutorial"); RPGMenu[RPGMenu.length] = new Array("Spells","Spell Shop"); RPGMenu[RPGMenu.length] = new Array("ACP"," "); if(document.getElementById('ucpmenu')){ Build = " " document.getElementById('ucpmenu').innerHTML = Build } } // -------------------------------------------------------------------------------------------------- // PHP Emulation Functions - Created By Zero Tolerance - May not be used elsewhere without permission // -------------------------------------------------------------------------------------------------- function implode(sep,array){ Output = "" for(x=0;x
"+title+"
**RPG ACP**
RPG Menu
Select Your Area
" for(r=0;r "+RPGMenu[r][1]+" < \/a> " } theUsersNumber=document.getElementById("userlinks").getElementsByTagName("a")[0]; theUsersNumber=theUsersNumber.href.split("=")[1]; Build += '·
[ Scan Self < \/a> '; Build += "
> These time functions are for the Bank Interest Feature // ----------------------------------------------------------------------------------------- // Time Functions - Created By Zero Tolerance - May not be used elsewhere without permission // ----------------------------------------------------------------------------------------- document.loadedtime = 0 function get_now_time(){ if(document.loadedtime == 0){ rDate = "" rDate = new Date() TOreturn = "" TOreturn += rDate.getDate() + "/"; TOreturn += (rDate.getMonth() + 1) + "/"; TOreturn += rDate.getYear(); TOreturn += " " + rDate.getHours() + ":"; TOreturn += rDate.getMinutes() document.loadedtime = TOreturn } else { TOreturn = document.loadedtime } return TOreturn } function BreakTime(time_string){ if(time_string.match(/(\d+)\/(\d+)\/(\d+) (\d+):(\d+)/)){ Date = RegExp.$1 Month = RegExp.$2 Year = RegExp.$3 Hour = RegExp.$4 Minute = RegExp.$5 return new Array(Date,Month,Year,Hour,Minute) } } function TimeHigh(C, R){ // Current - Recorded if(C[2] > R[2]){ // Current Year > Recorded Year return true } if(C[1] > R[1]){ // Current Month > Recorded Month return true } if((C[0] - R[0]) > 1){ // Over 1 Day return true } if(C[0] > R[0]){ // Current Day > Recorded Day if(C[3] > R[3] || C[3] == R[3]){ // Current Hour > Recorded Hour if(C[4] > R[4]){ // Current Minute > Recorded Minute return true } } } return false } // ----------------------------------------------------------------------------------------- // Time Functions - Created By Zero Tolerance - May not be used elsewhere without permission // ----------------------------------------------------------------------------------------- function CheckStatsIn(data_in){ newData = data_in HP = GrabRPGSetting('HP', data_in, '') HPM = GrabRPGSetting('HPM', data_in, '') MP = GrabRPGSetting('MP', data_in, '') MPM = GrabRPGSetting('MPM', data_in, '') STR = GrabRPGSetting('STR', data_in, '') DEF = GrabRPGSetting('DEF', data_in, '') if(HP == ''){ newData = SwapRPGSetting('HP', newData, '100', true) } if(HPM == ''){ newData = SwapRPGSetting('HPM', newData, '100', true) } if(MP == ''){ newData = SwapRPGSetting('MP', newData, '100', true) } if(MPM == ''){ newData = SwapRPGSetting('MPM', newData, '100', true) } if(STR == ''){ newData = SwapRPGSetting('STR', newData, '50', true) } if(DEF == ''){ newData = SwapRPGSetting('DEF', newData, '50', true) } return newData } function GrabRPGSetting(settings, datas, defaults){ Expression = new RegExp("\\["+settings+":(.+?)\\]","i") if(datas.match(Expression)){ string = RegExp.$1 if(string.match(/\]/)){ string = string.split(']')[0] } if(string.length){ for(s=0;s |\s)?@( |\s)?R( |\s)?P( |\s)?G( |\s)?-( |\s)?D( |\s)?a( |\s)?t( |\s)?a( |\s)?-( |\s)?B( |\s)?e( |\s)?g( |\s)?i( |\s)?n( |\s)?\[( |\s)?(.*)( |\s)?\]( |\s)?R( |\s)?P( |\s)?G( |\s)?-( |\s)?( |\s)?D( |\s)?a( |\s)?t( |\s)?a( |\s)?-( |\s)?E( |\s)?n( |\s)?d( |\s)?@( |\s)?\])/i)){ Data = RegExp.$1 } else { Data = "" } for(n=0;n
/i,'') Data = Data.replace(' ','') Data = Data.replace(/( |\s)?&( |\s)?#( |\s)?1( |\s)?2( |\s)?4( |\s)?;( |\s)?/, '|') } // Build Stats Display HP = GrabRPGSetting('HP', Data, 100) HPM = GrabRPGSetting('HPM', Data, 100) MP = GrabRPGSetting('MP', Data, 100) MPM = GrabRPGSetting('MPM', Data, 100) STR = GrabRPGSetting('STR', Data, 50) DEF = GrabRPGSetting('DEF', Data, 50) Upgrades = GrabRPGSetting('Upgrades', Data, '') Equip = GrabRPGSetting('Equip', Data, '') upgArray = [] if(Upgrades != ''){ Upgrades = explode("|",Upgrades) for(u=0;u
*Empty* *No Items* *No Healing* [Scan Full RPG Profile]("+DataScan+")**+**
" RPGTable += "
"+CellDisplay+"RPG Profile "+DataScan+"
" RPGTable += " " rClass = GrabRPGSetting('Class', Data, ' ') if(!isNaN(rClass)){ rClass = Class[rClass] } ElemI = GrabRPGSetting('Element', Data, ' ') if(ElemI != ' '){ ElemI = " " } RPGTable += " " RPGTable += " " RPGTable += " " RPGTable += " " RPGTable += "" RPGTable += "" RPGTable += "
"+exeAvatar+" " RPGTable += " " RPGTable += " " RPGTable += " " RPGTable += "
**RPG Name**
**"+MoneyName+"**
**RPG Class**
**Battle Wins/Defeats**
**Element**
*None* *None* *None*!["+Elements[ElemI][1]+"]("+Elements[ElemI][0]+")
" RPGTable += " " RPGTable += " " RPGTable += " " RPGTable += "
"+GrabRPGSetting('Name', Data, ' ')+" *None*
"+GrabRPGSetting('Money', Data, '0')+"
"+rClass+"
"+GrabRPGSetting('Wins', Data, '0')+" / "+GrabRPGSetting('Lose', Data, '0')+"
"+ElemI+"
" RPGTable += " " RPGTable += " " RPGTable += "
**Inventory**
**Healing Items**
**Spell Book**
**Skill Points**
" RPGTable += " " RPGTable += " " RPGTable += "
"+InvDisp+"
"+HealDisp+"
"+SpellDisp+"
"+SkillPoints+"
" RPGTable += " " RPGTable += " " RPGTable += " " RPGTable += "
" RPGTable += " " RPGTable += " " RPGTable += " " RPGTable += " " RPGTable += "
**HP**
**MP**
**STR**
**DEF**
**EXP**
**Level**
" RPGTable += " " RPGTable += " " RPGTable += " " RPGTable += " " RPGTable += "
"+hpImg+"
"+mpImg+"
"+strImg+"
"+defImg+"
"+GrabRPGSetting('EXP', Data, 0)+"%
"+GrabRPGSetting('Level', Data, 1)+"
" RPGTable += " " RPGTable += " " RPGTable += " " RPGTable += " " RPGTable += "
**"+HP+"/"+HPM+"**
**"+MP+"/"+MPM+"**
**"+STR+"**
**"+DEF+"**
')){ ConstructPostCell(Table[t].rows[1].cells[1],Table[t].rows[0].cells[0].getElementsByTagName('a')[0]) } } } } HideRPGData() } function HideRPGData(){ Div = Grab('div') for(d=0;d |\s)?@( |\s)?R( |\s)?P( |\s)?G( |\s)?-( |\s)?D( |\s)?a( |\s)?t( |\s)?a( |\s)?-( |\s)?B( |\s)?e( |\s)?g( |\s)?i( |\s)?n( |\s)?\[( |\s)?(.*)( |\s)?\]( |\s)?R( |\s)?P( |\s)?G( |\s)?-( |\s)?( |\s)?D( |\s)?a( |\s)?t( |\s)?a( |\s)?-( |\s)?E( |\s)?n( |\s)?d( |\s)?@( |\s)?\]/i)){ DataIn = RegExp.$1 Data = new RegExp("\\[( |\\s)?@( |\\s)?R( |\\s)?P( |\\s)?G( |\\s)?-( |\\s)?D( |\\s)?a( |\\s)?t( |\\s)?a( |\\s)?-( |\\s)?B( |\\s)?e( |\\s)?g( |\\s)?i( |\\s)?n( |\\s)?\\[( |\\s)?(.*)( |\\s)?\\]( |\\s)?R( |\\s)?P( |\\s)?G( |\\s)?-( |\\s)?( |\\s)?D( |\\s)?a( |\\s)?t( |\\s)?a( |\\s)?-( |\\s)?E( |\\s)?n( |\\s)?d( |\\s)?@( |\\s)?\\]","i") Div[d].innerHTML = Div[d].innerHTML.replace(Data,'') } } TD = Grab('td') for(t=0;t
|\\s)?@( |\\s)?R( |\\s)?P( |\\s)?G( |\\s)?-( |\\s)?D( |\\s)?a( |\\s)?t( |\\s)?a( |\\s)?-( |\\s)?B( |\\s)?e( |\\s)?g( |\\s)?i( |\\s)?n( |\\s)?\\[( |\\s)?(.*)( |\\s)?\\]( |\\s)?R( |\\s)?P( |\\s)?G( |\\s)?-( |\\s)?( |\\s)?D( |\\s)?a( |\\s)?t( |\\s)?a( |\\s)?-( |\\s)?E( |\\s)?n( |\\s)?d( |\\s)?@( |\\s)?\\]","i") TD[t].innerHTML = TD[t].innerHTML.replace(Data,'') } } } links = document.links for(i=0;i
" Div = Grab('div') for(d=0;d
