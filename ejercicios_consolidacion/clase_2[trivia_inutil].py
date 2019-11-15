print('Bienvenido/a a la trivia inútil!\n')

nombre = input('¿Cuál es tu nombre? ')
edad = int(input('¿Cuántos años tenés? '))
peso = int(input('Ok, última pregunta, ¿cuánto pesas? '))

edad_en_segundos = edad * 365 * 24 * 60 * 60
peso_en_la_luna = peso / 6
peso_en_el_sol = peso * 27.1

print('\nSi no te funcionara el Shift tu nombre sería', nombre.lower())
print('Ahora, si tuvieras el Caps Lock trabado, sería', nombre.upper())
print('Si un nene chiquito te quisiera llamar la atención, tu nombre se volvería', nombre*5)
print('Tu edad es de', edad_en_segundos, 'segundos')
print('¿Sabías que en la Luna pesarías sólo', peso_en_la_luna, 'kilos?')
print('Eso sí, en el Sol, tu peso sería de', peso_en_el_sol, 'kilos, pero no por mucho tiempo..\n')

input('Presione Enter para continuar')

# El peso en el sol es 27.1 veces que en la tierra
# El peso en la luna es la sexta parte que en la tierra