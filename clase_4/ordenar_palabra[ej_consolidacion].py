import random

listado_de_palabras = (
	'hola',
	'chau',
	'asiento',
	'comer',
	'heladera',
	'frenos'
)

listado_de_ayudas = (
	'Saludo usado al llegar a un lugar',
	'Saludo usado al irse de un lugar',
	'Lugar para sentarse',
	'Lo que se hace cuando se tiene hambre',
	'Electrodoméstico usado para mantener alimentos frescos',
	'Lo que necesita Lisa del plan dental'
)

palabra_desordenada = []
palabra_ordenada = random.choice(listado_de_palabras)
indice_de_palabra = listado_de_palabras.index(palabra_ordenada)

for letra in palabra_ordenada:
	palabra_desordenada += letra

random.shuffle(palabra_desordenada)
intentos_realizados = 0
palabra_ingresada = ''
solicito_pista = False

print('Bienvenido/a!', '\nLa siguiente palabra se encuentra desordenada:')
print(''.join(palabra_desordenada).upper())
print('Escriba !pista para obtener una pista', '\n')

while palabra_ingresada.lower() != palabra_ordenada:
	if palabra_ingresada.lower() == '!pista':
		print(listado_de_ayudas[indice_de_palabra])
		intentos_realizados -= 1
		solicito_pista = True
	elif intentos_realizados != 0:
		print('La palabra ingresada no es correcta, intente nuevamente!')

	palabra_ingresada = input('Ingrese la palabra ordenada: ')
	intentos_realizados += 1

puntos_obtenidos = 11 - intentos_realizados

if puntos_obtenidos > 0:
	print('\nFelicitaciones! Obtuviste', puntos_obtenidos ,'puntos por adivinar la palabra en', intentos_realizados, 'intento/s')
else:
	print('No obtuviste puntos por pifiarle tantas veces')
	puntos_obtenidos = 0

if not solicito_pista:
	puntos_obtenidos += 2
	print('Ganaste 2 puntos adicionales por no utilizar la pista!')

print('Tu puntaje:', puntos_obtenidos)

input('Presione ENTER para continuar')
