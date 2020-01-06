# '*args' define que se pueden recibir múltiples parámetros posicionales
# Lo recibido como parámetro es una Tupla
def sumar(*args):
	resultado = 0
	for nro in args:
		resultado += nro
	return resultado

print(sumar(5, 1)) # Funciona
print(sumar(7, 5, 3)) # Funciona!

# Se puede pasar directamente una tupla como parámetro de la siguiente forma
tupla = (1, 2, 5, 7)
print(sumar(*tupla)) # Funciona!

# '**kwargs' define que se pueden recibir múltiples parámetros nombrados
# Lo recibido como parámetro es un Diccionario
def saludar_por_cumpleanios(**kwargs):
	print('Feliz cumple', kwargs['nombre'], 'tenés', kwargs['edad'], 'años')

#saludar_por_cumpleanios() # Funciona porque tiene los parámetros definidos por defecto
saludar_por_cumpleanios(nombre='Jorge', edad=29) # Funciona!

# Se pueda pasar directamente un diccionario como parámetro de la siguiente forma
diccionario = {
	'nombre': 'Marcelo',
	'edad': 35
}

print(saludar_por_cumpleanios(**diccionario))
