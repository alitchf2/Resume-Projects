// Inherit the parent event
event_inherited();

obj_controller.npc_sheriff_mem_count += 1
interaction = obj_controller.npc_sheriff_mem_count
switch (interaction) {
	case 1:
		//sets intro sequence
		intro_dialogue_state = 1
		state = 5
	
		break;
	default:
		//Non interaction number based events
		fine = false
		if (obj_phone.called == true) {
			state = 7
			call_convo_state = 1
		} else {
			chance = irandom_range(1, 100)
			if (chance >= (obj_controller.morality + 50)) {
				fine = true
				state = 6
				fine_convo_state = 1
			} else {
				state = 1
			}
		}
		break;
}