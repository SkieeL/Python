class Gremlin:
	total = 0

	def __init__(self, nombre, humor):
		# Atributo público
		#self.nombre = nombre
		self.__nombre = nombre
		# Así se define un atributo privado (con doble guión bajo)
		self.__humor = humor
		# Accede al método de clase "total" desde la instancia
		self.__class__.total += 1
		print('Ha nacido un nuevo Gremlin llamado', self.nombre, '!')

	# Propiedad (getter)
	@property
	def nombre(self):
		return self.__nombre

	# Propiedad (setter)
	@nombre.setter
	def nombre(self, nuevo_nombre):
		if nuevo_nombre == '':
			print('El nuevo nombre no puede estar vacío')
		else:
			self.__nombre = nuevo_nombre
			print('Nombre modificado exitosamente!')

	# Método de clase
	# Un decorador mete código alrrededor del objeto
	@classmethod
	def status(cls):
		print('Cantidad de Gremlins:', cls.total)

	# Esto es un método totalmente independiente, sólo que está dentro de la clase
	@staticmethod
	def funcion():
		print('Soy una función independiente, dentro de la clase Gremlin')

	# Un método que sólo recibe self, no recibe ningún parámetro
	# Todos los métodos en Python por defecto reciben como parámetro su propia instancia (self)
	def hablar(self):
		print('Hola, soy', self.nombre, 'y ahora me siento', self.__humor)

	# Método mágico, va a ser llamado cuando el objeto intente ser convertido a string
	# Sería una sobrecarga de un casteo a string
	def __str__(self):
		res = '===============\n'
		res += 'Objeto Gremlin\n'
		res += 'nombre:' + self.nombre + '\n'
		res += '==============='

		return res


def main():
	#print('Accediendo a atruibuto de clase...')
	#print(Gremlin.total)
	grem1 = Gremlin('Gizmo', 'feliz')
	#grem2 = Gremlin('Lucas', 'cansado')

	#Gremlin.status()
	# De esta forma (agregando _NombreDeClase) se puede acceder a un atributo privado desde fuera de la clase  
	print(grem1._Gremlin__humor)
	grem1.hablar()

	grem1.nombre = 'Jorge' # Llama al setter nombre que internamente setea el atributo __nombre
	print(grem1.nombre) # Llama al getter nombre que internamente llama al atributo __nombre

	#grem2.hablar()
	#print(grem1)
	#print(grem2.nombre)


# Sólo ejecuta el código si se está ejecutando el archivo, NO si se importa
if __name__ == '__main__':
	main()