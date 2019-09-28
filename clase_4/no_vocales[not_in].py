texto = input("Ingrese texto: ")
texto_sin_vocales = ""
VOCALES = "aeiou"

for letra in texto:
	if letra.lower() not in VOCALES:
		texto_sin_vocales += letra
		print(texto_sin_vocales)

print("El texto sin vocales es:", texto_sin_vocales)
