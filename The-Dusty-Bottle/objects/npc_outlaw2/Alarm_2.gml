//Alarm for correct
show_debug_message("correct")
//increase quality level
if (obj_controller.quality < 100){
	obj_controller.quality += 2
}
if (obj_controller.drink_roster[drink_selection] != dnk_outlawsOath){
	obj_controller.rowdiness += obj_controller.drink_roster[drink_selection].rowd_value
}
obj_controller.morality -= 4
obj_controller.player_balance += obj_controller.drink_roster[drink_selection].value
dialogue = "Thank you!"
active = false