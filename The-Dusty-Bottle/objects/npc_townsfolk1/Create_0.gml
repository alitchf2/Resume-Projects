// Inherit the parent event
event_inherited();

fight = false
chance = irandom_range(1, 200)
if (chance <= obj_controller.rowdiness) {
	fight = true
	state = 5
	convo_state = 1
}