print("Bienvenido/a!")

listado_puntajes = [10, 20, 30]
opcion_seleccionada = None

while opcion_seleccionada != 0:
	if opcion_seleccionada == 1:
		print("Los puntajes cargados son:\n")
		for puntaje in listado_puntajes:
			print("-", puntaje)
	elif opcion_seleccionada == 2:
		print("Ingrese el puntaje a cargar")
		puntaje_ingresado = int(input("Puntaje: "))
		listado_puntajes.append(puntaje_ingresado)
	elif opcion_seleccionada == 3:
		print("Ingrese el puntaje que desea eliminar")
		puntaje_ingresado = int(input("Puntaje a eliminar: "))
		if puntaje_ingresado in listado_puntajes:
			listado_puntajes.remove(puntaje_ingresado)
			print("El puntaje", puntaje_ingresado, "fue eliminado de la lista!")
		else:
			print("El puntaje", puntaje_ingresado ,"ingresado no se encuentra en la lista")
	elif opcion_seleccionada == 4:
		listado_puntajes.sort(reverse=True)
		print("Los puntajes fueron reordenados de menor a mayor!")
	elif opcion_seleccionada == 0:
		break
	else:
		print("Opción incorrecta")


	print("\n1. Mostrar puntajes")
	print("2. Agregar puntajes")
	print("3. Eliminar puntajes")
	print("4. Ordenar puntajes")
	print("0. Salir\n")

	opcion_seleccionada = int(input("Seleccione una opcion: "))

print("Hasta luego!\n")
input("Presione ENTER para salir")
