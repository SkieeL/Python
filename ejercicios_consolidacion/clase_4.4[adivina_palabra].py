import random

listado_de_palabras = (
	'hola',
	'chau',
	'asiento',
	'comer',
	'heladera',
	'frenos'
)

print('Bienvenido/a!\n')
print('Pensaré una palabra y usted deberá adivinarla, para esto, le indicaré')
print('la cantidad de letras que tiene y usted me podrá preguntar hasta 5 veces')
print('si contiene o no determinada letra. Listo?\n')

input('Presione ENTER para jugar')

palabra_seleccionada = random.choice(listado_de_palabras)
preguntas_restantes = 5

print('\nLa palabra tiene', len(palabra_seleccionada), 'letras\n')

while preguntas_restantes > 0:
	print('Ingrese una letra para consultar si se encuentra en la palabra')
	letra = input('Letra: ')

	if letra.lower() in palabra_seleccionada:
		print('Sí\n')
	else:
		print('No\n')

	preguntas_restantes -= 1

palabra_ingresada = input('Ingrese la palabra: ')

if palabra_ingresada == palabra_seleccionada:
	print('\nFelicitaciones! La palabra ingresada es correcta!')
else:
	print('\nLa palabra ingresada es incorrecta, la palabra correcta era', palabra_seleccionada)

input('\nPresione ENTER para continuar')
