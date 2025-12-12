fade_alpha = 0;
blur_strength = 0;
time_scale = 1;
game_state = "";
text_alpha = 0;
timer = 0;
tempmoney = 0;
islost = false;
ispaused = false;
//is active is true we are actively looking for the win cond if it is false then we are not
isactive = true;
iscontinue = false;
instance_deactivate_object(obj_continueday)
instance_deactivate_object(obj_gamereset)
//Day Count for checking when the day is over with, would refer to this when making the script switch days.
//daycount = 1;
end_timer = room_speed * 3;

show_debug_message(string(game_DayEndText));
//show_debug_message(string(daycount));

if (layer_exists("layer_blur")) {
    layer_blur_id = layer_get_id("layer_blur");
    fx_id = layer_get_fx(layer_blur_id);
} else {
    fx_id = undefined;
}
show_debug_message("made end week screen")