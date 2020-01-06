print('Bienvenido/a!', '\nSi no sabes cómo leer al revés yo te ayudo')
texto = input('Ingrese texto: ')

print('El texto ingresado al revés sería: ', end='')

for indice in range(len(texto)-1, -1, -1):
	print(texto[indice], end='')

input('\nPresione ENTER para continuar')