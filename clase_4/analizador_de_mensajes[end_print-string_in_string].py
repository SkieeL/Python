texto = input("Ingrese el texto: ")

print("Longitud del texto:", len(texto))
print("La letra E, la más común del Español, ", end="")

if 'e' in texto.lower():
	print("está en el texto.")
else:
	print("NO está en el texto.")
