randomise()

//-------Dialogue text font styles-------
draw_set_font(fnt_dialogue)
draw_set_colour(c_black)
draw_set_halign(fa_left)
draw_set_valign(fa_top)


//make dialogue (game controller) always be up front
depth = -9999

//player var declarations
player_state = "waiting"
player_balance = 0
rent_cost = 100
incorrect_choice_counter = 0
day_counter = 1

//intro sequence var declarations
intro_in_progress = true
intro_dialogue = "null"
intro_dialogue_state = 1
dialogue = "null"
dialogue_state = 1
continue_hint = "null"


//status var declarations
morality = 50
rowdiness = 0
quality = 50
max_morality = 100
max_rowdiness = 100
max_quality = 100
rent_cost = 100

first_day_drinks_spawned = false
day_counter = 1
week_counter = 1
npc_spawned = false
npc_que = 0
npc_spawn_num = 3 //landlord, sheriff, and 1
restart_day = false
game_state = "active npc"


drink_roster = [dnk_rotgut,dnk_arbuckle,dnk_blackjackBurbon,dnk_champaign,dnk_desertNectar]
drink_selection = irandom_range(0,4)

npc_roster = [npc_landlord, npc_sheriff, npc_outlaw1, npc_townsfolk2, npc_townsfolk3, npc_townsfolk4, npc_townsfolk5, npc_townsfolk6]

//add npc counts here
npc_sheriff_mem_count = 0
npc_landlord_mem_count = 0
npc_miner1_mem_count = 0
npc_miner2_mem_count = 0
npc_miner3_mem_count = 0
npc_miner4_mem_count = 0
npc_miner5_mem_count = 0
npc_outlaw1_mem_count = 0
npc_outlaw2_mem_count = 0
npc_outlaw3_mem_count = 0
npc_outlaw4_mem_count = 0
npc_outlaw5_mem_count = 0
npc_townsfolk1_mem_count = 0
npc_townsfolk2_mem_count = 0
npc_townsfolk3_mem_count = 0
npc_townsfolk4_mem_count = 0
npc_townsfolk5_mem_count = 0
npc_townsfolk6_mem_count = 0
npc_townsfolk7_mem_count = 0
npc_townsfolk8_mem_count = 0

//variable triggered bool values
alarm1_triggered = false
made = false //people roster made by alarm[1]
que_triggered = false
