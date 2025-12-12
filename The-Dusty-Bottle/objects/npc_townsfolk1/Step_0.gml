switch(state){
	case 0:
		if(alarm_trigger == false){
		alarm[0] = 2
		alarm_trigger = true
		}
		break;
	//greeting
	case 1:
		if(alarm_trigger == false){
			alarm[1] = 2
			alarm_trigger = true
		}
		break;
	//correct
	case 2:
		if(alarm_trigger == false){
			alarm[2] = 2
			alarm_trigger = true
		}
		break;
	//incorrect
	case 3:
		if(alarm_trigger == false){
			alarm[3] = 2
			alarm_trigger = true
		}
		break;
	//waiting
	case 4:
		
		if(mouse_check_button_pressed(mb_left)){
			if(position_meeting(mouse_x,mouse_y,obj_controller.drink_roster[drink_selection])){
				audio_play_sound(snd_drinkPour, 1, false)
				input = 1
			}
			else if(position_meeting(mouse_x, mouse_y, obj_controller.drink_roster[other_drink_options[0]]) && drink_selection != 0){
				audio_play_sound(snd_drinkPour, 1, false)
				input = 2
			} else if (position_meeting(mouse_x, mouse_y, obj_controller.drink_roster[other_drink_options[1]])) {
				wrong_dnk = obj_controller.drink_roster[other_drink_options[1]]
				audio_play_sound(sound_bank[select_sound], 1, false)
				input = 3
			} else if (position_meeting(mouse_x, mouse_y, obj_controller.drink_roster[other_drink_options[2]])) {
				wrong_dnk = obj_controller.drink_roster[other_drink_options[2]]
				audio_play_sound(sound_bank[select_sound], 1, false)
				input = 3
			} else if (position_meeting(mouse_x, mouse_y, obj_controller.drink_roster[other_drink_options[3]])) {
				wrong_dnk = obj_controller.drink_roster[other_drink_options[3]]
				audio_play_sound(sound_bank[select_sound], 1, false)
				input = 3
            }
			switch(input){
				case 1: 
					state = 2
					alarm_trigger = false					
					break;
				case 2:
					state = 0
					alarm_trigger = false	
					break;
				case 3:
					state = 3
					alarm_trigger = false
			}
		}
        break;
	case 5:
		switch(convo_state){
			case 1:
				obj_controller.dialogue = "Reckon I hate to be the one bringin' bad tidings, but I just saw a couple of liquored-up patrons mixin' it up. They've cooled their heels for now, but they done left a mark."
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			case 2:
				if(obj_controller.rowdiness <= 25){
					obj_controller.quality -= 15
					obj_controller.player_balance -= 25
					obj_controller.rowdiness -= 3
					convo_state = 3
				}
				if(obj_controller.rowdiness > 25 and obj_controller.rowdiness <= 50){
					obj_controller.quality -= 20
					obj_controller.player_balance -= 50
					obj_controller.rowdiness -= 6
					convo_state = 5
				}
				if(obj_controller.rowdiness > 50 and obj_controller.rowdiness <= 75){
					obj_controller.quality -= 25
					obj_controller.player_balance -= 75
					obj_controller.rowdiness -= 12
					convo_state = 7
				}
				if(obj_controller.rowdiness > 75){
					obj_controller.quality -= 30
					obj_controller.player_balance -= 100
					obj_controller.rowdiness -= 24
					convo_state = 9
				}
				break;
			case 3:
				obj_controller.dialogue = "Tussle didn't do too much harm. It'll only set you back 'bout twenty-five dollars to patch up. I reckon a few folks got their feathers ruffled by the commotion too."
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			case 5:
				obj_controller.dialogue = "They done a fair bit of damage. It'll be fifty dollars to fix 'er up proper. Got some sour looks from the regulars too. That scrap left a bad taste in more'n a few mouths."
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			case 7:
				obj_controller.dialogue = "They made a right mess of it. Gonna take a solid seventy-five dollars to get this place back in shape. Not only that but the ruckus put a real damper on the mood. More'n a couple fellas finished their drinks early and headed out."
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			case 9:
				obj_controller.dialogue = "Place is near tore up. It's a full hundred dollars in damage, easy. Your reputation also took a beatin'. Folks left in a huff, and word of a place that lets brawls break out travels faster than a prairie fire."
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			default:
				state = 1
				obj_controller.dialogue = "null"
				break;
		}
		if keyboard_check_pressed(vk_space){
			convo_state++
			show_debug_message("advanced dialogue")
		}
		break;

}
if(!active){
	continue_hint = "(Press space to continue)"
	if(keyboard_check_pressed(vk_space)){
		obj_controller.npc_spawned = false
		obj_controller.npc_que++
		instance_destroy(self)	
	}
}