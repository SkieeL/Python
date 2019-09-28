inventario = (
	"espada",
	"armadura",
	"escudo",
	"poción de vida"
)

if not inventario:
	print("Tu inventario está vacío")
else:
	print("Tenés en el inventario:")
	for elemento in inventario:
		print("-", elemento.title())

input("Presione ENTER para continuar")