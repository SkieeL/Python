1. Mostrar instrucciones del juego

	 0 | 1 | 2
	-----------
	 3 | 4 | 5
	-----------
	 6 | 7 | 8

2. Determinar quién va primero
3. Crear tablero vacío
4. Mostrar el tablero
5. Mientras nadie gane y no se empate, se sigue jugando:
	Si es turno del humano:
		Obtener movimiento humano
	Si es turno de la máquina:
		Calcular movimiento de la máquina

	Actualizar el tablero con el movimiento
	Mostrar el tablero
	Intercambiar el turno
6. Mostrar el resultado de la partida

Combinaciones para ganar:
- 048
- 246
- 012
- 345
- 678
- 036
- 147
- 258

La maquina debría intentar:
1. Tratar de ganar
2. Tratar de no perder
3. Tratar de posicionarse en las mejores posiciones

Listado de funciones útiles:
- mostrar_instrucciones()
- solicitar_numero(texto, minimo=0, maximo=8)
- obtener_orden() # Chequea si el humano tiene X u O
- mostrar_tablero(tablero) # El tablero es una Lista
- obtener_movimientos_posibles(tablero) # Retorna una tupla con lugares vacíos
- obtener_ganador(tablero) # Chequea las combinaciones ganadoras
- obtener_movimiento_humano(tablero)
- obtener_movimiento_computadora(tablero, ficha_computadora, ficha_humano)
- obtener_siguiente_turno(ficha_que_recien_jugo)
- felicitar_ganador()
- main()
