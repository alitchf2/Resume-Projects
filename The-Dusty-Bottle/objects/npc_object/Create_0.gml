//pick drink selection at random
randomise()
show_debug_message("created npc")

other_drink_options = [0,1,2,3,4]
index = 0
active = true

sound_bank = [snd_clink1, snd_clink2, snd_clink3]
select_sound = irandom_range(0,2)

drink_selection = irandom_range(0,4)

index = array_get_index(other_drink_options, drink_selection)
array_delete(other_drink_options, index, 1);

show_debug_message(other_drink_options)

depth = -100