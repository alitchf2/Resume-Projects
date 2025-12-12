if(obj_winorlose.isactive = true)
{
	if (dialogue != "null") {
    draw_text_ext(obj_textbox.x,obj_textbox.y, dialogue, 25, 520);
	}

	if (continue_hint != "null"){
		draw_text_ext(obj_textbox.x, obj_textbox.y + 290, continue_hint, 25, 520);	
	}

	if(sprite_index != -1){
		draw_self()	
	}
}

