salud = 10
trolls_derrotados = 0
ataque_de_troll = 3

while salud > 0:
	trolls_derrotados += 1
	salud -= ataque_de_troll

	print("Nuestro guerrero venció a un troll")
	print("Pero recibió", ataque_de_troll, "puntos de daño")

print("Nuesto guerrero venció", trolls_derrotados, "trolls, pero el último lo cagó matando")