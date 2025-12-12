// Inherit the parent event
event_inherited();

robbery = false
chance = irandom_range(1, 100)
if (chance <= (obj_controller.morality - 50)) {
	robbery = true
	state = 5
	obj_phone.active = false
	rob_convo_state = 1
}