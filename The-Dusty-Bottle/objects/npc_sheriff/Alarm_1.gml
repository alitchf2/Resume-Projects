if (interaction == 1) {
	show_debug_message("greeting")
	self.dialogue = "Can I get a " + obj_controller.drink_roster[drink_selection].drinkName + "?"
	state = 4
} else if (fine) {
	self.dialogue = "But truth be told, I still like you, son. I want this place to succeed. So, how's this, I'll stop with the sheriff'n and just be a customer. I'll take a " + obj_controller.drink_roster[drink_selection].drinkName + "?"
	state = 4
} else {
	//Alarm for greeting
	show_debug_message("greeting")
	self.dialogue = "Can I get a " + obj_controller.drink_roster[drink_selection].drinkName + "?"
	state = 4
}