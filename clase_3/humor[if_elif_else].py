import random, time

print("Uh bancame que adivino tu estado emocional..")

time.sleep(2)

print("Ommm estoy sintiendo tu energía..")

time.sleep(2)

numero = random.randint(1, 3)

print("Tu energía me dice que vos estás..")

if numero == 1:
	print("de 10!")
elif numero == 2:
	print("meh..")
else:
	print("para el balazo capo")

input("Presion ENTER para salir")