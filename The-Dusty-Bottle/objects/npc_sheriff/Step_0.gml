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
        if (incorrect_counter >= 3) {
            state = 4;
			alarm_trigger = false
        }
        break;
		
	//New case to edit
	case 5:
		switch(intro_dialogue_state){
			case 1:
				obj_controller.intro_dialogue = "Howdy-do. Hope I ain't too early? Just saw the landlord moseyin' out, said you was open for business."
				break;
			case 2: 
				obj_controller.intro_dialogue = "First off I'd like to properly welcome you to our town. We all thought mighty high of your father. It's a real black spot on the sun that he's no longer vertical, but we're all glad to see you here filling his boots."
				break;
			case 3: 
				obj_controller.intro_dialogue = "Pardon my manners, I'm the sheriff. I'm the one charged with keepin' peace 'round these parts. And truth be told, I could use an extra set of eyes."
				break;
			case 4:
				obj_controller.intro_dialogue = "If you spot any of those sidewinders, you just give me a holler on the horn. I'll come take 'em in and you'll get the reward money for your trouble."
				break;
			case 5:
				obj_controller.intro_dialogue = "All that sheriffin' stuff bein' said, my throat's drier than a dust strom."
				break;
			case 6:
				obj_controller.intro_dialogue = "null"
				state = 1
				break;
		}
		if keyboard_check_pressed(vk_space){
			intro_dialogue_state++
			show_debug_message("advanced dialogue")
		}
		break;
	case 6:
		switch (fine_convo_state) {
			case 1:
				obj_controller.dialogue = "I thought when we first spoke, I could rely on your help. I never figured you'd stoop to consortin' with outlaws. That kind of behavior... it comes with a fine."
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			case 2:
				if(obj_controller.morality > 25){
					obj_controller.player_balance -= 50
					obj_controller.morality += 5
					fine_convo_state = 3
				} else {
					obj_controller.player_balance -= 100
					obj_controller.morality += 10
					fine_convo_state = 5
				}
				break;
			case 3:
				obj_controller.dialogue = "The good news is, you ain't in too deep yet. The fine is fifty dollars. Consider it a slap on the wrist, a chance to turn it 'round"
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			case 5:
				obj_controller.dialogue = "You've waded in pretty deep with that bunch. Why, one more step and I'd have to lock you up right alongside 'em. The fine is one hundred dollars. My hope is it stings enough to make you think better next time."
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			default:
				state = 1
				obj_controller.dialogue = "null"
				break;	
			}
		if keyboard_check_pressed(vk_space){
			fine_convo_state++
			show_debug_message("advanced dialogue")
		}
		break;
	case 7:
		switch (call_convo_state) {
			case 1:
				obj_controller.dialogue = "I'm glad you used the old horn to give me a call."
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			case 2:
				if(obj_phone.is_outlaw){
					obj_controller.player_balance += 50
					obj_controller.morality += 20
					call_convo_state = 3
				} else {
					call_convo_state = 5
				}
				break;
			case 3:
				obj_controller.dialogue = "Not only that, but I'm more excited than a jackrabbit in a lettuce patch that you helped me run one down. Here's your reward of $50. And wheil I'm here I might as well get a drink."
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			case 5:
				obj_controller.dialogue = "I hate to break it to you, but that ain't no outlaw. But I'll help you make up the business and order a drink."
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			default:
				state = 1
				obj_controller.dialogue = "null"
				obj_phone.called = false
				obj_phone.is_outlaw = false
				break;	
			}
		if keyboard_check_pressed(vk_space){
			call_convo_state++
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