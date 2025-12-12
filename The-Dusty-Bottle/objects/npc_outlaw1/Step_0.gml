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
	//Intro
	case 5:
		switch(intro_dialogue_state){
			case 1:
				obj_controller.intro_dialogue = "Well, glory be. Thought that lawdog would swallow the key and never leave. Hold on now, don't go callin' him back just yet. Hear me out."
				break;
			case 2: 
				obj_controller.intro_dialogue = "A long time ago, me and my outfit couldn't darken the door of a saloon like this without hearin' a heap of \"long face\" jokes. So we decided to turn outlaw. Figured that'd put a stop to the chucklin' right quick. Ever since then I just go by 1."
				break;
			case 3: 
				obj_controller.intro_dialogue = "What I'm gettin' at is, me and the boys just want to be able to amble in here and wet our whistles from time to time. We'll even throw in a little extra for your...discretion, should that star-packer come nosin' around."
				break;
			case 4:
				obj_controller.intro_dialogue = "To show you how this arrangement could grease the wheels for us both... let me buy a drink."
				break;
			case 5:
				obj_controller.intro_dialogue = "null"
				state = 1
				break;
			case 6:
				obj_controller.intro_dialogue = "Glad you see things sensible-like. I'll make sure my boys treat you square when they ride in."
				break;
			case 7:
				obj_controller.intro_dialogue = "Just don't go 'round playin' sheriff's errand boy, or they might get a little... quick on the trigger. Much obliged for the drink."
				active = false
				break;
		}
		if keyboard_check_pressed(vk_space){
			intro_dialogue_state++
			show_debug_message("advanced dialogue")
		}
		break;
	case 6:
		switch (rob_convo_state) {
			case 1:
				obj_controller.dialogue = "Listen up. We tried to warn you. You do too much for that law-dog, and then we gotta ride in and show who's boss."
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
				obj_controller.dialogue = "Now, it ain't like you've been wearin' a deputy's badge or nothin', so I'll be kind. I'm takin' fifty dollars. Best be thankful I'm a merciful horse."
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			case 5:
				obj_controller.dialogue = "Since you've been playin' his errand boy, I'm takin' a good chunk. A hundred dollars, to be exact. Maybe next time, you'll think twice before choosin' your side of the law."
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