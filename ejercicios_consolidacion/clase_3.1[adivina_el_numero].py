import random

print('Bienvenido/a!')
print('Ingrese un número del 1 al 100 para adivinar el número secreto')

numero_secreto = random.randint(1, 100)
intentos_realizados = 0
numero_ingresado = None

while numero_ingresado != numero_secreto and intentos_realizados < 10:
    print('\nTe quedan', 10 - intentos_realizados, 'intento/s')
    numero_ingresado = int(input('Ingrese un número: '))
    intentos_realizados += 1

    if numero_ingresado > numero_secreto:
        print('Te pasaste!')
    elif numero_ingresado < numero_secreto:
        print('Te quedaste corto..')

if numero_ingresado == numero_secreto:
    print('\nFelicitaciones! El número secreto era', numero_secreto, 'y  lo adivinaste en', intentos_realizados, 'intentos!\n')
else:
    print('\nSólo tenías una cosa que hacer y no pudiste, el número secreto era el', str(numero_secreto) + '. Tan difícil era?\n')

input('Presione Enter para continuar')