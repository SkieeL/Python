import random

print('Hola! Pensá un número del 1 al 100 y yo lo voy a adivinar!')
input('Presione Enter para continuar')
print('Listo? Aquí voy!')
input('Presione Enter para continuar')
numero_minimo = 1
numero_maximo = 100
numero_seleccionado = random.randint(numero_minimo, numero_maximo)

opcion_ingresada = None

while opcion_ingresada != 3:
    print('Es el', str(numero_seleccionado) + '?\n')
    print('1. El número es mayor')
    print('2. El número es menor')
    print('3. Ese es el número!\n')

    try:
        opcion_ingresada = int(input('Ingrese una opción: '))
    except ValueError:
        print('\nTenés que ingresar una opción capo\n')
    else:
        try:
            if opcion_ingresada == 1:
                numero_minimo = numero_seleccionado + 1
                numero_seleccionado = random.randint(numero_minimo, numero_maximo)
            elif opcion_ingresada == 2:
                numero_maximo = numero_seleccionado - 1
                numero_seleccionado = random.randint(numero_minimo, numero_maximo)
            elif opcion_ingresada == 3:
                print('\nGané! En tu cara papá!\n')
                input('Presione Enter para continuar')
            else:
                print('Tenés que ingresar una opción válida')
        except ValueError:
            print('\nMe estás haciendo trampa, cagón!\n')
            input('Presione Enter y váyase a la mierda')
