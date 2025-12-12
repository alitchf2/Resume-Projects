//Alarm for greeting
show_debug_message("greeting")
if (fight) {
	dialogue = "Well, dust settles but a man's thirst don't. Reckon I'll still have a " + obj_controller.drink_roster[drink_selection].drinkName + "."
	state = 4
} else {
	self.dialogue = "Hello There! Can I get a " + obj_controller.drink_roster[drink_selection].drinkName + "?"
	state = 4
}