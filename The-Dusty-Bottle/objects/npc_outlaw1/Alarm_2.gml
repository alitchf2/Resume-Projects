//Alarm for correct
show_debug_message("correct")
//increase quality level
obj_controller.quality += 3
//For outlaws only, decrease moral level
obj_controller.morality -= 8
if (obj_controller.drink_roster[drink_selection] != dnk_outlawsOath){
	obj_controller.rowdiness += obj_controller.drink_roster[drink_selection].rowd_value
}
obj_controller.player_balance += obj_controller.drink_roster[drink_selection].value + (obj_controller.drink_roster[drink_selection].value *.5)
if (interaction == 1) {
	dialogue = "null"
	state = 5
	intro_dialogue_state = 6
} else {
	dialogue = "Thank you!"
	active = false
}