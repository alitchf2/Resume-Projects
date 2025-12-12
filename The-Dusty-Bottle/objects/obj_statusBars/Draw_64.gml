draw_set_colour(c_black)

//render quality bar
quality_x_pos = 130
quality_y_pos = 50
bar_width = 400
bar_height = 20

draw_rectangle(quality_x_pos,quality_y_pos,bar_width + quality_x_pos ,bar_height + quality_y_pos,true)
draw_text(10,43,"Quality:")

quality_percentage = obj_controller.quality/obj_controller.max_quality
filled_width1 = bar_width * quality_percentage
draw_rectangle(quality_x_pos,quality_y_pos,quality_x_pos + filled_width1, quality_y_pos + bar_height, false)

//render rowdiness
rowd_x_pos = 130
rowd_y_pos = 100
bar_width = 400
bar_height = 20

draw_rectangle(rowd_x_pos,rowd_y_pos,bar_width + rowd_x_pos ,bar_height + rowd_y_pos,true)
draw_text(10,93,"Rowdiness:")

rowd_percentage = obj_controller.rowdiness/obj_controller.max_rowdiness
filled_width2 = bar_width * rowd_percentage
draw_rectangle(rowd_x_pos,rowd_y_pos,quality_x_pos + filled_width2, rowd_y_pos + bar_height, false)

//render morality
mor_x_pos = 130
mor_y_pos = 150
bar_width = 400
bar_height = 20

draw_rectangle(mor_x_pos,mor_y_pos,bar_width + mor_x_pos ,bar_height + mor_y_pos,true)
draw_text(10,143,"Morality:")

morality_percentage = obj_controller.morality/obj_controller.max_morality
filled_width3 = bar_width * morality_percentage
draw_rectangle(mor_x_pos,mor_y_pos,mor_x_pos + filled_width3, mor_y_pos + bar_height, false)