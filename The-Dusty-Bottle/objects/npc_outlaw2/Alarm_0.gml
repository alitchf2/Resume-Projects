//if rotgut is selected
show_debug_message("took the easy way")
dialogue = "Eh, I guess ill take a rotgut"
obj_controller.player_balance += dnk_rotgut.value + (dnk_rotgut.value * .5)
obj_controller.rowdiness += dnk_rotgut.rowd_value
obj_controller.morality -= 2
active = false