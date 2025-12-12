if (game_state == "win" || game_state == "lose" || game_state == "dayend" || game_state == "week_end" )
{
    draw_set_alpha(fade_alpha * 0.6);
    draw_set_color(c_black);
    draw_rectangle(0, 0, display_get_gui_width(), display_get_gui_height(), false);
    draw_set_alpha(1);


    draw_set_font(TITLE);
    draw_set_halign(fa_center);
    draw_set_valign(fa_middle);
    draw_set_color(c_white);

    if (game_state == "win")
    {
        draw_text(display_get_gui_width()/2, display_get_gui_height()/2, game_WText);
    }
    else if (game_state == "lose")
    {
        draw_text(display_get_gui_width()/2, display_get_gui_height()/2, game_LText);
    }
	else if (game_state == "dayend")
	{
		draw_text(display_get_gui_width()/2, display_get_gui_height()/2 - 100, string(game_DayEndText) + " " + string(obj_controller.day_counter));
		draw_text(display_get_gui_width()/2, display_get_gui_height()/2 + 100, "Balance:" + " " + string(tempmoney));
	}
	else if (game_state == "week_end" && islost != true)
	{
		draw_text(display_get_gui_width()/2, display_get_gui_height()/2 - 300, string(game_WeekEndText));
		draw_text(display_get_gui_width()/2, display_get_gui_height()/2, "Rent:" + " -" + string(obj_controller.rent_cost));
		draw_text(display_get_gui_width()/2, display_get_gui_height()/2 + 300, "Balance:" + " " + string(tempmoney));
	}
		else if (game_state == "week_end" || islost == true)
	{
		draw_text(display_get_gui_width()/2, display_get_gui_height()/2 - 300, string(game_LText));
		draw_text(display_get_gui_width()/2, display_get_gui_height()/2, "Rent:" + " -" + string(obj_controller.rent_cost));
		draw_text(display_get_gui_width()/2, display_get_gui_height()/2 + 300, "Balance:" + " " + string(tempmoney));
	}
}

if(game_state == "")
{
	draw_set_font(fnt_dialogue); // resets to default
	draw_set_halign(fa_left);
	draw_set_valign(fa_top);
	draw_set_color(c_black);
}
