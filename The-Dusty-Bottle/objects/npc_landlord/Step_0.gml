switch(state){
	case 1:
		switch(intro_dialogue_state){
			case 1:
				obj_controller.intro_dialogue = "Howdy. Glad you made it."
				obj_controller.continue_hint = "(Press space to continue)"
				break;
			case 2: 
				obj_controller.intro_dialogue = "First off, my condolences for your Pa. He was a fine man, one of the best. Straight shooter, through and through. He must'a though mighty high of you, leavin' you The Dusty Bottle in his will."
				break;
			case 3:
				obj_controller.intro_dialogue = "We're keepin' to your father's drink schedule. Every mornin', someone'll swing by to switch out the stock so you keep a fresh variety for the patrons.When a feller asks for a drink, you just hand it over and he'll settle the tab. In fact, if you don't mind, I'll be your first customer. "
				break;
			case 4:
				obj_controller.continue_hint = "null"
				obj_controller.intro_dialogue = "Pour me a Rotgut Whiskey, would ya? It's the bottle on the far left."
				break;
			case 5:
				obj_controller.intro_dialogue = "Good try, but that ain't Rotgut. No matter, I know you're learnin' the ropes. Let's try again for the Rotgut, the one on the far left." 
				break;
			case 6:
				obj_controller.continue_hint = "(Press space to continue)"
				obj_controller.intro_dialogue = "Mmm, that hits the spot."
				break;
			case 7:
				obj_controller.intro_dialogue = "Around these parts everyone has a thirst for Rotgut. If you're ever in a tight spot and unsure what to pour, your best bet is always the ole Gut. That's why we always keep Rotgut on hand."
				break;
			case 8:
				obj_controller.intro_dialogue = "Here's your coin for the whiskey."
				alarm[5] = 2
				break;
			case 9:
				obj_controller.intro_dialogue = "Now don't go gettin' attached to me handin' over money. Truth is, the coin's mostly gonna flow the other way. See, The Dusty Bottle was your Pa's business, but this buildin' here, she's still mine. As a tribute to your father, I'll let this first week slide, but if you aim to keep these doors swinging, you'll need to have $100 ready for me when I come 'round Sunday eve."
				break;
			case 10:
				obj_controller.intro_dialogue = "'Fore I ride out let me give you a word to the wise. The West is a hard country. It can take everything you have and then ask for your boots if you aren't careful. Your old man, he knew how to make this land work for him. He understood the balance of keepin' a decent soul, servin' a decent product, and tendin' to keep a decent community in his saloon. As you stand behind this bar now, you'd do well to mind that balance."
				break;
			case 11: 
				obj_controller.intro_dialogue = "Well, I'll leave you to it. I'll be seein' you in a week. I'll spread the word in town that you're open for business. Good luck to ya, partner."
				active = false
				break;
		}
		
		// Cases that require SPACE to continue
		if(intro_dialogue_state != 4 && intro_dialogue_state != 5){ // Added new exclusion
			if keyboard_check_pressed(vk_space){
				intro_dialogue_state++
				show_debug_message("advanced dialogue")
			}
		}
	
		if(intro_dialogue_state == 4 or intro_dialogue_state == 5){
			if (mouse_check_button_pressed(mb_left) && position_meeting(mouse_x, mouse_y, dnk_rotgut)){
				intro_dialogue_state = 6
				audio_play_sound(snd_drinkPour, 1, false)
			}
			if (mouse_check_button_pressed(mb_left) && position_meeting(mouse_x, mouse_y, dnk_champaign)){
				intro_dialogue_state = 5
				audio_play_sound(sound_bank[select_sound], 1, false)
			}
		}
		
		break;
	default:		
		//New case to edit
		break;

}
if(!active){
	obj_controller.continue_hint = "(Press space to continue)"
	if(keyboard_check_pressed(vk_space)){
		obj_controller.npc_spawned = false
		obj_controller.npc_que++
		instance_destroy(self)	
	}
}