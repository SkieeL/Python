def saludar(nombre):
	print('Hola', nombre, '!')

def multiplicar(nro_a, nro_b):
	return nro_a * nro_b

def obtener_instrucciones():
	return '''
- Tenés que usar la palabra reservada "def" y luego el nombre de la función
- Por convención, si el nombre de la función es compuesta, se usa snake case (todas las palabras en minúsculas separadas por guión bajo)
- Luego del nombre de la función se abren y cierran paréntesis, donde van los parámetros separados por coma si son más de uno
- Se ponen dos puntos, y a partir del siguiente renglón se tabula para indicar que el código se encuentra dentro de la función
- En caso de querer retornar un valor, se usa la palabra clave "return"
	'''

def imprimir_instrucciones():
	print(obtener_instrucciones())

saludar('Eze')

print(
	'El resultado de tu multiplicación es',
	multiplicar(5, 4)
)

imprimir_instrucciones()

