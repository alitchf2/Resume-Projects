if(obj_winorlose.isactive = true)
{
	

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
			} else if (position_meeting(mouse_x, mouse_y, obj_controller.drink_roster[other_drink_options[0]]) && drink_selection != 0){
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
		
	//New case to edit

}
if(!active){
	continue_hint = "(Press space to continue)"
	if(keyboard_check_pressed(vk_space)){
		obj_controller.npc_spawned = false
		obj_controller.npc_que++
		instance_destroy(self)	
	}
}
}