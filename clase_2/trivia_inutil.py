nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
peso = input("Ingrese su peso: ")

print("Si no te funcionara el Shif tu nombre se vería", nombre.lower())
print("Si se te trabara el CapsLock tu nombre se vería", nombre.upper())
print("Si un nene chiquito te quisisera llamar la atención te diría", nombre * 5)
print("Tu edad es de", edad * 365 * 24 * 60 * 60, "segundos")
print("Sabías que en la Luna pesarías sólo", peso / 6, "kilos")
print("Ahora bien, en el Sol, tu peso sería de", peso * 27.1, "kilos (aunque no por mucho tiempo)")

input("Presione ENTER para continuar")

# El peso en el sol es 27.1 veces que en la tierra
# El peso en la luna es la sexta parte que en la tierra