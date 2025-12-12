if (mouse_check_button_pressed(mb_left) && position_meeting(mouse_x, mouse_y, obj_phone) && active) {
	called = true
	if ((obj_controller.npc_roster[obj_controller.npc_que] == npc_outlaw1) || (obj_controller.npc_roster[obj_controller.npc_que] == npc_outlaw2) || (obj_controller.npc_roster[obj_controller.npc_que] == npc_outlaw3) || (obj_controller.npc_roster[obj_controller.npc_que] == npc_outlaw4) || (obj_controller.npc_roster[obj_controller.npc_que] == npc_outlaw5)) {
		is_outlaw = true
	}
	obj_controller.npc_roster[obj_controller.npc_que].dialogue = "null"
	instance_destroy(obj_controller.npc_roster[obj_controller.npc_que])
	obj_controller.dialogue = "null"
	obj_controller.continue_hint = "null"
	instance_create_layer(992,64,"Instances",npc_sheriff)
}