inventario = [
	"espada",
	"armadura",
	"escudo",
	"poción de vida"
]

print("Bienvenido/a a su inventario\n")

if not inventario:
	print("Tu inventario está vacío")
else:
	print("Tenés en el inventario:")
	for elemento in inventario:
		print("-", elemento.capitalize())

print("\nIngrese el ítem que desea agregar")
print("(Para no agregar mas ítems ingrese 0)\n")

elemento_agregado = input("Ítem a agregar: ")

while elemento_agregado != "0":
	inventario.append(elemento_agregado)
	elemento_agregado = input("Ítem a agregar: ")

inventario[0] = "brújula"

print("\nTerminaste de agregar ítems a tu inventario\n")

if not inventario:
	print("Tu inventario está vacío")
else:
	print("Tenés en el inventario:")
	for elemento in inventario:
		print("-", elemento.capitalize())

input("Presione ENTER para continuar")