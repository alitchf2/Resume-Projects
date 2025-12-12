if (interaction == 1) {
	obj_controller.player_balance += 5 + 2.5
	obj_controller.rowdiness += obj_controller.drink_roster[drink_selection].rowd_value
	dialogue = "null"
	state = 5
	intro_dialogue_state = 6
} else {
	//if rotgut is selected
	show_debug_message("took the easy way")
	dialogue = "Eh, I guess ill take a rotgut"
	obj_controller.player_balance += dnk_rotgut.value + (dnk_rotgut.value * .5)
	obj_controller.rowdiness += dnk_rotgut.rowd_value
	obj_controller.morality -= 4
	active = false
}