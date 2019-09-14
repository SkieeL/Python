# El algoritmo elige un número aleatorio
# El usuario ingresa un número
# El programa indica si es el número, sino indica si el número es mayor o menor

import random

numero_aleatorio = random.randint(1, 100)
intentos_realizados = 1

print("Bienvenido/a, ingrese un número del 1 al 100 para jugar")

numero_ingresado = int(input("Ingrese un número: "))

while numero_ingresado != numero_aleatorio:
	if numero_ingresado > numero_aleatorio:
		print("Te pasaste!")
	else:
		print("Te quedaste corto..")

	intentos_realizados += 1
	numero_ingresado = int(input("Ingrese un número: "))

print("Felicitaciones! Adivinaste el número en ", intentos_realizados, "intentos")

input("Presione ENTER para salir")