show_debug_message("alarm trigger")
randomise()

//drink and npc roster declarations (so the game doesnt crash when attempting to remove old drinks on day 1)

//destroy old drinks from previous day
for(i=0; i<5; i++){
	instance_destroy(drink_roster[i])
}


//----------------NPC Randomizer----------------

npc_patron_array = [npc_sheriff,npc_miner1, npc_miner2, npc_miner3, npc_miner4, npc_miner5,
npc_outlaw1,npc_outlaw2,npc_outlaw3,npc_outlaw4,npc_outlaw5,npc_townsfolk1, npc_townsfolk2, npc_townsfolk3,
npc_townsfolk4,npc_townsfolk5,npc_townsfolk6,npc_townsfolk7,npc_townsfolk8]

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

//----------------Drink Randomizer----------------

full_drink_array = [dnk_rotgut, dnk_pissMissle, dnk_arbuckle, dnk_muleKick, dnk_tarantulaTequila, 
dnk_desertNectar, dnk_dustBowlGin, dnk_kentuckyBurbon, dnk_dragonsBreathBrandy, dnk_silverNailScotch, 
dnk_minerMirth, dnk_blackjackBurbon, dnk_sheriffsStar, dnk_outlawsOath, dnk_champaign]
		
//populate current day with drinks (rotgut gets factored out)
drink_roster[0] = dnk_rotgut
array_delete(full_drink_array, 0,1)
maximum = 13
for(i = 1; i <= 4; i++){
		
	randomVal = irandom_range(0,maximum)
	drink_roster[i] = full_drink_array[randomVal]
		
	array_delete(full_drink_array, randomVal, 1)
	maximum--
}


show_debug_message(drink_roster)


//---------------create new drinks---------------
y_position = 800
x_position = 10

for(i=0; i<5; i++){
	instance_create_layer(x_position, y_position, "Drinks", drink_roster[i])
	x_position += 270
	show_debug_message("spawned" + string(drink_roster[i]))
}

made = true