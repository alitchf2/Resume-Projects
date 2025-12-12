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
		switch (rob_convo_state) {
			case 1:
				obj_controller.dialogue = "Well look what we have 'ere. I do recollect 1 warnin' you 'bout cosyin' up too the law. Now we gotta come remind folks who run the shadows 'round here. And don't even think 'bout pickin' up that horn or we'll have a real problem."
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			case 2:
				if(obj_controller.morality < 75){
					obj_controller.player_balance -= 50
					obj_controller.morality -= 5
					rob_convo_state = 3
				} else {
					obj_controller.player_balance -= 100
					obj_controller.morality -= 10
					rob_convo_state = 5
				}
				break;
			case 3:
				obj_controller.dialogue = "1 said to only take fifty dollars. Got lucky you haven't been wearin' a tin star, or it would've been more."
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			case 5:
				obj_controller.dialogue = "You been helpin' the star-packer more'n a little so now we're settlin' up with a hundred dollars. to be exact. If you got a problem with it, take it up with 1 and see how it turns out."
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			default:
				state = 1
				obj_controller.dialogue = "null"
				break;	
			}
		if keyboard_check_pressed(vk_space){
			rob_convo_state++
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