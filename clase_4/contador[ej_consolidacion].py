print('Bienvenido/a')

numero_inicial = int(input('Ingrese el número inicial: '))
numero_final = int(input('Ingrese el número final: '))
numero_de_saltos = int(input('Ingrese de cuanto en cuanto quiere contar: '))

print('Contando del', numero_inicial, 'al', numero_final, 'saltando de a', numero_de_saltos, 'unidad/es')

for numero in range(numero_inicial, numero_final+1, numero_de_saltos):
	print(numero)

input('Presione ENTER para continuar')