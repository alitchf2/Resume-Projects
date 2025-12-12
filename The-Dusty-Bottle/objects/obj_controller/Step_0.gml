//-----------------Intro sequence-----------------
if(intro_in_progress) {
	if(npc_que < npc_spawn_num && npc_spawned == false) {
		if(first_day_drinks_spawned = false){
			alarm[4] = 2
			first_day_drinks_spawned = true
		}
		instance_create_layer(992, 64, "Instances", npc_roster[npc_que])
		show_debug_message("created from here")
		npc_spawned = true
	}
	if(npc_que >= npc_spawn_num) {
		intro_dialogue = ""
		continue_hint = "null"
		intro_in_progress = false
		npc_que = 0
		obj_phone.active = true
		instance_destroy(dnk_tarantulaTequila)
		show_debug_message("finished this")
	}
} else {

//-----------------State machine----------------- 
if(intro_in_progress == false || obj_winorlose.isactive == false){
	switch(game_state){
		case "active npc":
			if(day_counter % 8 == 0)
			{
				game_state = "end of week"
				break;
			}
			if(!alarm1_triggered){
				alarm[1] = 2
				alarm1_triggered = true
			}
			if(npc_que < npc_spawn_num && npc_spawned == false && made){
                instance_create_layer(992,64,"Instances",npc_roster[npc_que])
                npc_spawned = true
				show_debug_message("created here")
            }
			if(npc_que >= npc_spawn_num){
				game_state = "end of day"	
			}
			break;
		case "end of day":
			//end of day screen here
			
			obj_winorlose.game_state = "dayend";

			if(obj_winorlose.ispaused == false)
			{
				show_debug_message("end of day " + string(day_counter))
				npc_que = 0
				day_counter++
				alarm1_triggered = false
				made = false
				//Remove "Active NPC" and replace it with an if statement that checks if we have progressed past the end of day screen.
				game_state = "active npc"
			}
			break;
		case "end of week":
		show_debug_message("end of week " + string(week_counter))
			//end of week
			if(obj_winorlose.ispaused == false)
			{
				show_debug_message("ran to here")
			
				if(player_balance < rent_cost){
					//end game
				}
				player_balance -= rent_cost
				day_counter++
				week_counter++
				alarm1_triggered = false
				game_state = "active npc"
			} else {
				obj_winorlose.game_state = "week_end";
			}
			break;
		case "you lose":
			//game over screen here 
			
			obj_winorlose.game_state = "lost"
	}

	
}

}

if (rowdiness < 0) {
	rowdiness = 0
} else if (rowdiness > 100) {
	rowdiness = 100
}
if (morality < 0) {
	morality = 0
} else if (morality > 100) {
	morality = 100
}
if (quality < 0) {
	quality = 0
} else if (quality > 100) {
	quality = 100
}



