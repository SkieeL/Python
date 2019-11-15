import random

cantidad_de_caras = 0
cantidad_de_cecas = 0

for lanzamiento in range(0, 100):
    moneda = random.randint(0, 1)

    if moneda == 1:
        cantidad_de_caras += 1
    else:
        cantidad_de_cecas += 1

print('Se lanzó una moneda 100 veces y salieron', cantidad_de_caras, 'caras y', cantidad_de_cecas, 'cecas')
input('Presione Enter para continuar')
