if (interaction == 1) {
	self.dialogue = "Can I get a " + obj_controller.drink_roster[drink_selection].drinkName + "?"
	state = 4
} else if (robbery) {
	self.dialogue = "'Course, robbin' a man is thirsty work. Tell you what... you pour me a " + obj_controller.drink_roster[drink_selection].drinkName + ", and I reckon I can spare a little of your own money back."
	state = 4
} else {
	//Alarm for greeting
	show_debug_message("greeting")
	self.dialogue = "Hello There! Can I get a " + obj_controller.drink_roster[drink_selection].drinkName + "?"
	state = 4
}