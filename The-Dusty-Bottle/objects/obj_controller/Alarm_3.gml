//populate first day roster
//----------------NPC Randomizer----------------

npc_patron_array = [npc_sheriff,npc_miner1, npc_miner2, npc_miner3, npc_miner4, npc_miner5,
npc_outlaw1,npc_outlaw2,npc_outlaw3,npc_outlaw4,npc_outlaw5,npc_townsfolk1, npc_townsfolk2, npc_townsfolk3,
npc_townsfolk4,npc_townsfolk5,npc_townsfolk6,npc_townsfolk7, npc_townsfolk8]

//determine how many towns people show up depending on quality rating (can make more random later if needed)
npc_spawn_num = 0
if (quality <= 25){
	npc_spawn_num = 3	
}
if (quality > 25 and quality <= 50 ){
	npc_spawn_num = 4
}
if (quality > 50 and quality <= 75){
	npc_spawn_num = 5	
}
if (quality > 75){
	npc_spawn_num = 6	
}
show_debug_message(string(npc_spawn_num))


//populate the npc roster for the day
maximum1 = 18
for(i = 0; i <= npc_spawn_num; i++){
	
	randomVal1 = irandom_range(0,maximum1)
	npc_roster[i] = npc_patron_array[randomVal1]
	
	array_delete(npc_patron_array, randomVal1, 1)
	maximum1--
}
show_debug_message(npc_roster)
show_debug_message("created people roster")