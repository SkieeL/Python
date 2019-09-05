nombre = input("Hola. ¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tenés? "))
peso = int(input("Ok. Última pregunta: ¿Cuánto pesas? "))

print("\nSi no te funcionara el Shift, tu nombre se escribiría", nombre.lower())
print("\nAhora, si tuvieses el Caps Lock trabado, sería", nombre.upper())
print("\nSi un nene chiquito te quisiera llamar la atención, tu nombre se volvería:\n" + nombre * 5)
print("\nTu edad es de", edad * 365 * 24 * 60 * 60, "segundos.")
print("\n¿Sabías que en la Luna pesarías sólo", peso / 6, "kilos?")
print("Ahora bien, en el Sol, tu peso sería de", peso * 27.1, "kilos (aunque no por mucho tiempo)\n")

input("Presione ENTER para continuar")

# El peso en el sol es 27.1 veces que en la tierra
# El peso en la luna es la sexta parte que en la tierra