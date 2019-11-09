from abc import ABC, abstractmethod

# ABC hace que la clase herede de la "Abstract Base Clase" (clase abstracta base), la cual la convierte en abstracta
class Enemigo(ABC):
	# Esto hace explícito que las clases hijas van a tener que implementar un método morir
	@abstractmethod
	def morir(self):
		pass

# Clase que hereda de Enemigo
class Alien(Enemigo):
	# Este método morir reemplaza el implementado en Enemigo
	def morir(self):
		print('Ouch, soy un alien y me cagaron matando :(')

class Jugador:
	def reventar(self, enemigo):
		print('Soy un jugador y reventé un enemigo :D')
		enemigo.morir()


heroe = Jugador()
invasor = Alien()
heroe.reventar(invasor)