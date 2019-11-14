class Gremlin:
	def __init__(self, nombre):
		self.__nombre = nombre
		self.__hambre = 0
		self.__aburrimiento = 0
		self.__deducir_humor()

	@property
	def nombre(self):
		return self.__nombre

	def hablar(self):
		self.__pasar_tiempo()
		return 'Hola soy ' + self.__nombre + ' y ahora estoy ' + self.__humor

	def comer(self, comida=4):
		self.__pasar_tiempo()
		self.__hambre -= comida
		if self.__hambre < 0:
			self.__hambre = 0
		self.__deducir_humor()
		return 'Ñom, ñom.. Que rico!'

	def jugar(self, jugar=4):
		self.__pasar_tiempo()
		self.__aburrimiento -= jugar
		if self.__aburrimiento < 0:
			self.__aburrimiento = 0
		self.__deducir_humor()
		return 'Wii, que divertido!'

	def __pasar_tiempo(self):
		self.__aburrimiento += 1
		self.__hambre += 1
		self.__deducir_humor()

	def __deducir_humor(self):
		infelicidad = self.__aburrimiento + self.__hambre

		if infelicidad < 5:
			self.__humor = 'Feliz'
		elif infelicidad <= 10:
			self.__humor = 'Ok'
		elif infelicidad <= 15:
			self.__humor = 'Incómodo'
		else:
			self.__humor = 'Enojado'

def main():
	print('Bienvenido al Jardín de Gremlins!\n')
	nombre = str(input('Ingrese un nombre para su Gremlin: '))
	gremlin = Gremlin(nombre)
	print('Ha nacido su Gremlin', nombre + '!')
	opcion_seleccionada = 0

	while opcion_seleccionada != 4:
		print('\n1. Escuchar a', gremlin.nombre)
		print('2. Darle de comer a', gremlin.nombre)
		print('3. Jugar con', gremlin.nombre)
		print('4. Salir\n')

		try:
			opcion_seleccionada = int(input('Ingrese una opción: '))
		except ValueError:
			print('\nDebe ingresar un número de opción!')
		else:
			print('\n', end='')
			if opcion_seleccionada == 1:
				print(gremlin.hablar())
			elif opcion_seleccionada == 2:
				print(gremlin.comer())
			elif opcion_seleccionada == 3:
				print(gremlin.jugar())
			elif opcion_seleccionada == 4:
				print('Hasta luego!')
			else:
				print('Opción inválida!')

if __name__ == '__main__':
	main()