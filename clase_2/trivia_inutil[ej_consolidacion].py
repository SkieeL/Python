nombre = input("Hola. ¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tenés? "))
peso = int(input("Ok. Última pregunta: ¿Cuánto pesas? "))

nombre_en_minusculas = nombre.lower()
nombre_en_mayusculas = nombre.upper()
edad_en_segundos = edad * 365 * 24 * 60 * 60
peso_en_la_luna = peso / 6
peso_en_el_sol = peso * 27.1


print("\nSi no te funcionara el Shift, tu nombre se escribiría", nombre_en_minusculas)
print("\nAhora, si tuvieses el Caps Lock trabado, sería", nombre_en_mayusculas)
print("\nSi un nene chiquito te quisiera llamar la atención, tu nombre se volvería:\n" + nombre * 5)
print("\nTu edad es de", edad_en_segundos, "segundos.")
print("\n¿Sabías que en la Luna pesarías sólo", peso_en_la_luna, "kilos?")
print("Ahora bien, en el Sol, tu peso sería de", peso_en_el_sol, "kilos (aunque no por mucho tiempo)\n")

input("Presione ENTER para continuar")

# El peso en el sol es 27.1 veces que en la tierra
# El peso en la luna es la sexta parte que en la tierra