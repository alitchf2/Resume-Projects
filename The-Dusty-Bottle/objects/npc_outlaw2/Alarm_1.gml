if (robbery) {
	self.dialogue = "All this robbin' gave me a thristn'. You get me a " + obj_controller.drink_roster[drink_selection].drinkName + " and I'll give you a little somethin' back so long as it doesn't get back 'round to 1."
	state = 4
} else {
	//Alarm for greeting
	show_debug_message("greeting")
	self.dialogue = "Hello There! Can I get a " + obj_controller.drink_roster[drink_selection].drinkName + "?"
	state = 4
}