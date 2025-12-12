if (interaction == 1) {
	dialogue = "Why you're still greener than spring grass, 'cause that ain't what I ordered. But go on ahead, take another swing at it. I want the " + obj_controller.drink_roster[drink_selection].drinkName + "."
	state = 4
} else {
	show_debug_message("incorrect")
	dialogue = "This is not what I want, I said a " + obj_controller.drink_roster[drink_selection].drinkName + ". I'm outta here!"
	//reduce quality rating
	obj_controller.quality -= 5
	active = false
}