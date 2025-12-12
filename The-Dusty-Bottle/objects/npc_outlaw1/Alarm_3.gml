if (interaction == 1) {
	dialogue = "Hmm. Mighty good thing the rest of my outfit ain't here, or they'd be right disappointed in the pour. But I know you're new to this so you get a 'nother chance." + obj_controller.drink_roster[drink_selection].drinkName + "."
	state = 4
} else {
	show_debug_message("incorrect")
	dialogue = "This is not what I want, I said a " + obj_controller.drink_roster[drink_selection].drinkName + ". I'm outta here!"
	//reduce quality rating
	obj_controller.quality -= 5
	active = false
}