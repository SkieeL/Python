import random

GALLETAS = [
    'La Macrisis te va a destruir',
    'Te novia está con otro :(',
    'Mañana te despiden',
    'En 2 años te vas a quedar pelado',
    'Tal vez mañana te encontrás $5'
]

galleta_seleccionada = random.randint(0, 4)

print(GALLETAS[galleta_seleccionada])

input('Presione Enter para continuar')