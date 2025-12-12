if(obj_winorlose.isactive = true)
{
//GUI rendering
draw_text(10,0,"Money: $" + string(player_balance))




		//draw dialogue (may need to make a function for this)
	if (dialogue != "null") {
	    draw_text_ext(obj_textbox.x,obj_textbox.y, dialogue, 25, 520);
	}

	//draw intro dialogue	
	if (intro_dialogue != "null") {
	    draw_text_ext(obj_textbox.x,obj_textbox.y, intro_dialogue, 25, 520);
	}

	if (continue_hint != "null"){
		draw_text_ext(obj_textbox.x, obj_textbox.y + 290, continue_hint, 25, 520);	
	}


}
