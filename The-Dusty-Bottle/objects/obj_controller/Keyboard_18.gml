//Cheat codes

//Skip intro
if keyboard_check_pressed(ord("S")) {
	npc_outlaw1_mem_count = 1
	npc_sheriff_mem_count = 1
	intro_dialogue = ""
	continue_hint = "null"
	intro_in_progress = false
	npc_que = 0
	obj_phone.active = true
	if (object_exists(npc_landlord)) {
		instance_destroy(npc_landlord)
	}
	if (object_exists(npc_sheriff)) {
		instance_destroy(npc_sheriff)
	}
	if (object_exists(npc_outlaw1)) {
		instance_destroy(npc_outlaw1)
	}
	npc_spawned = false
	instance_destroy(dnk_tarantulaTequila)
	show_debug_message("ran skip intro")
}

//Spawn Outlaw1
if keyboard_check_pressed(ord("1")) {
	npc_roster[npc_que].dialogue = "null"
	instance_destroy(npc_roster[npc_que])
	dialogue = "null"
	continue_hint = "null"
	instance_create_layer(992,64,"Instances",npc_outlaw1)
}

//Spawn Outlaw2
if keyboard_check_pressed(ord("2")) {
	npc_roster[npc_que].dialogue = "null"
	instance_destroy(npc_roster[npc_que])
	dialogue = "null"
	continue_hint = "null"
	instance_create_layer(992,64,"Instances",npc_outlaw2)
}

//Spawn Sheriff
if keyboard_check_pressed(ord("3")) {
	npc_roster[npc_que].dialogue = "null"
	instance_destroy(npc_roster[npc_que])
	dialogue = "null"
	continue_hint = "null"
	instance_create_layer(992,64,"Instances",npc_sheriff)
}

//Spawn Miner1
if keyboard_check_pressed(ord("4")) {
	npc_roster[npc_que].dialogue = "null"
	instance_destroy(npc_roster[npc_que])
	dialogue = "null"
	continue_hint = "null"
	instance_create_layer(992,64,"Instances",npc_miner1)
}

//Spawn Townsfolk1
if keyboard_check_pressed(ord("5")) {
	npc_roster[npc_que].dialogue = "null"
	instance_destroy(npc_roster[npc_que])
	dialogue = "null"
	continue_hint = "null"
	instance_create_layer(992,64,"Instances",npc_townsfolk1)
}

//Skip a week ahead
if keyboard_check_pressed(ord("6")) {
	day_counter = 7;
}

//Add $50
if keyboard_check_pressed(ord("D")) {
	player_balance += 50
}

//Loose $50
if keyboard_check_pressed(ord("F")) {
	player_balance -= 50
}

//Add Quality
if keyboard_check_pressed(ord("G")) {
	quality += 10
}

//Lose Quality
if keyboard_check_pressed(ord("H")) {
	quality -= 10
}

//Add Rowdiness
if keyboard_check_pressed(ord("J")) {
	rowdiness += 10
}

//Lose Rowdiness
if keyboard_check_pressed(ord("K")) {
	rowdiness -= 10
}

//Add Morality
if keyboard_check_pressed(ord("Z")) {
	morality += 10
}

//Lose Morality
if keyboard_check_pressed(ord("X")) {
	morality -= 10
}