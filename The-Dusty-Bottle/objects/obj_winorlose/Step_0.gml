//
//if (lives <= 0)
//{
//	if(text_alpha < 1)
//	{
//		text_alpha += 0.01;
//	}
//	game_state = "lose";
//}

	
if (game_state == "win" || game_state == "lose" || game_state == "dayend" || game_state == "week_end") {
    time_scale = max(time_scale - 0.02, 0);
    fade_alpha = min(fade_alpha + 0.02, 1);
    blur_strength = min(blur_strength + 0.2, 8);
	timer +=1;

    if (fx_id != undefined) {
        fx_id.parameters[0] = blur_strength;
    }
	isactive = false;
	ispaused = true;
	tempmoney = obj_controller.player_balance
	instance_deactivate_object(obj_statusBars);
	instance_deactivate_object(obj_textbox);
	instance_activate_object(obj_continueday)
	//instance_deactivate_object(obj_textbox);
	if(game_state == "dayend" || game_state == "week_end")
	{
		//show_debug_message(string(iscontinue)); commented out because it threw endless 0's until moved off screen
		if(game_state == "week_end")
		{
			instance_activate_object(obj_gamereset)
			if(obj_controller.player_balance <= 0)
			{
				islost = true;
				instance_deactivate_object(obj_continueday);
			}
		}
		if(iscontinue == true)
		{
			game_state = "";
			show_debug_message("Continue");
			instance_activate_object(obj_statusBars);
			instance_activate_object(obj_textbox);
			instance_deactivate_object(obj_continueday)
		    instance_deactivate_object(obj_gamereset)
			isactive = true;
			iscontinue = false;
			ispaused = false;
			
		}
		
		
	}
}
	