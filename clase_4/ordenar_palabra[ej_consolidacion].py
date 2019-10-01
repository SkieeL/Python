import random

listado_de_palabras = (
	'sol',
	'hola',
	'mesa',
	'saludar',
	'dormir',
	'heladera'
)

palabra_ordenada_en_lista = []
palabra_ordenada = random.choice(listado_de_palabras)
# Acá se debería transformar la palabra ordenada en una lista, que tenga cada caracter en un slot distinto
palabra_desordenada = random.shuffle(palabra_ordenada_en_lista)
palabra_ingresada = ''

print('Bienvenido/a! La siguiente palabra se encuentra desordenada, ingrese la palabra que se puede formar')
print(palabra_desordenada.upper())

while palabra_ingresada.lower() != palabra_ordenada:
	palabra_ingresada = input('Ingrese una palabra: ')
else:
	print('Felicitaciones! Adivinaste la palabra:', palabra_ordenada.title())

# random.choice() # Sirve para elegir un elemento random de una secuencia (array, string, etc)
# random.shuffle() # Sirve para "mezclar" una secuencia mutable (lista) pasada por parámetro

# El programa debe mostrar en pantalla una palabra desordenada (elegida de una lista hardcodeada)
# El usuario debe ingresar la palabra ordenada y el programa debe verificar si la respuesta es correcta