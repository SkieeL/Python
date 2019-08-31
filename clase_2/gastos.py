print("Ingresar montos en patacones\n")

auto = int(input("* Fiat uno: "))
dpto = int(input("* Habitación en Laferrere: "))
bondi = int(input("* Gasto en sube: "))
regalos = int(input("* Regalos: "))
comida = int(input("* Comida: "))

total = auto + dpto + bondi + regalos + comida

print("Total de gastos:", total, "patacones")

input("Presiones ENTER para salir")