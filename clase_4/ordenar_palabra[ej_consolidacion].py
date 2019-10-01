import random

listado_de_palabras = (
	'hola',
	'chau',
	'mesa',
	'saludar',
	'comer',
	'heladera'
)

palabra_desordenada = []
palabra_ordenada = random.choice(listado_de_palabras)

for letra in palabra_ordenada:
	palabra_desordenada += letra

random.shuffle(palabra_desordenada)
intentos_realizados = 0
palabra_ingresada = ''

print('Bienvenido/a!', '\nLa siguiente palabra se encuentra desordenada:')
print(''.join(palabra_desordenada).upper(), '\n')

while palabra_ingresada.lower() != palabra_ordenada:
	if intentos_realizados != 0:
		print('La palabra ingresada no es correcta, intente nuevamente!')

	palabra_ingresada = input('Ingrese la palabra ordenada: ')
	intentos_realizados += 1
else:
	print('\nFelicitaciones! Adivinaste la palabra en', intentos_realizados, 'intento/s\n')

input('Presione ENTER para continuar')
