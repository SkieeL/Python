import random

texto = input("Ingrese el texto: ")

maximo = len(texto)
minimo = -len(texto)

for i in range(10):
	posicion = random.randrange(minimo, maximo)
	print("texto[", posicion, "]", end="\t")
	print(texto[posicion])