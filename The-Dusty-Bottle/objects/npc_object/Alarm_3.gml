show_debug_message("incorrect")
dialogue = "This is not what I want, I said a " + obj_controller.drink_roster[drink_selection].drinkName + ". I'm outta here!"
//reduce quality rating
if (obj_controller.rowdiness < 100){
	obj_controller.rowdiness += wrong_dnk.rowd_value
}
obj_controller.quality -= 5
active = false
