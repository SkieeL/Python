print("Abriendo y cerrando el archivo")

try:
	archivo = open("archivos/archivo.txt", "r")
	archivo.close()
except:
	print('Uh no existe tu archivo')

print("\nLeyendo caracteres del archivo")

archivo = open("archivos/archivo.txt", "r")
print(archivo.read(1)) # Lee 1 caracter (mueve el cursor 1 caracter)
print(archivo.read(5)) # Lee 5 caracteres (a partir del segundo caracter)
print(archivo.read()) # Lee todo el archivo (el resto de lo que quede)
archivo.close()

print("\nLeyendo el archivo línea a línea")

archivo = open("archivos/archivo.txt", "r")
print(archivo.readline()) # Lee una línea
archivo.close()

print("\nVolcando el archivo en una lista")
archivo = open("archivos/archivo.txt", "r")
lineas = archivo.readlines() # Lee todas las lineas del archivo y las mete en una lista
print("El archivo tiene", len(lineas), "lineas")
for linea in lineas:
	print(linea)
archivo.close()

print("\nIterando el archivo")
archivo = open("archivos/archivo.txt", "r")
for linea in archivo:
	print(linea)
archivo.close()

# .seek() sirve para mover el cursor en el archivo