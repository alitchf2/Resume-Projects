//populate first day drink roster
//----------------Drink Randomizer----------------

full_drink_array = [dnk_rotgut, dnk_pissMissle, dnk_arbuckle, dnk_muleKick, dnk_tarantulaTequila, 
dnk_desertNectar, dnk_dustBowlGin, dnk_kentuckyBurbon, dnk_dragonsBreathBrandy, dnk_silverNailScotch, 
dnk_minerMirth, dnk_blackjackBurbon, dnk_sheriffsStar, dnk_outlawsOath, dnk_champaign]
		
//populate current day with drinks (rotgut gets factored out)
drink_roster[0] = dnk_rotgut
array_delete(full_drink_array, 0,1)
maximum = 13
for(i = 1; i <= 4; i++){
		
	randomVal = irandom_range(0,maximum)
	drink_roster[i] = full_drink_array[randomVal]
		
	array_delete(full_drink_array, randomVal, 1)
	maximum--
}


show_debug_message(drink_roster)


//---------------create new drinks---------------
y_position = 800
x_position = 10

for(i=0; i<5; i++){
	instance_create_layer(x_position, y_position, "Drinks", drink_roster[i])
	x_position += 270
	show_debug_message("spawned" + string(drink_roster[i]))
}