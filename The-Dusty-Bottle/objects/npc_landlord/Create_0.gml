// Inherit the parent event
event_inherited();

obj_controller.npc_landlord_mem_count += 1
interaction = obj_controller.npc_landlord_mem_count
switch (interaction) {
	case 1:
		//sets intro sequence
		intro_dialogue_state = 1
		state = 1
	
		break;
	default:
		//other landlord interaction (asking for rent)
		break;
}