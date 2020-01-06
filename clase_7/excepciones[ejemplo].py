try:
	x = float(input("Ingrese un número: "))
	y = float(input("Ingrese otro número: "))
	resultado = x / y
except ValueError as e:
	print("Hay que ingresar números papu")
	print(e)
except ZeroDivisionError as e:
	print("No podés dividir por 0, capoeira")
	print(e)
except Exception as e:
	print("Hubo un error", e)
else: # Se ejecuta si y solo si NO hubo ningún error en el try
	print(resultado)
finally: # Se ejecuta de todas formas, si hay o no error
	print("Éste es el bloque finally")
