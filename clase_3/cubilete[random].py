# Importación de módulo
import random

# Calcula el valor de los dados
dado1 = random.randint(1, 6)
dado2 = random.randrange(6) + 1
dado3 = random.randint(1, 6)

resultado = dado1 + dado2 + dado3

print("Tus dados fueron:")
print("*", dado1)
print("*", dado2)
print("*", dado3)
print("Por un total de:", resultado)

input("Presione ENTER para salir")

# Rango hasta 5 (no lo incluye)
# random.randrange(6) + 1