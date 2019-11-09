Trabajo integrador

Clase Gremlin
- str nombre
- int hambre
- int aburrimiento
+ str humor (debe tener propiedad)

Puede:
+ hablar()
+ comer(comida=4)
+ jugar(jugar=4)
- pasar_tiempo()

* Hablar muestra nombre y cómo se siente
* Comer le resta al hambre la cantidad de comida pasada por parámetro
* jugar le resta al aburrimiento la cantidad de jugar pasada por parámetro
* El humor es un getter, se define a partir del hambre y el aburrimiento
* Al hacer comer, hablar, jugar se debe pasar el tiempo
* El pasar tiempo le suma 1 al hambre y al aburrimiento
* El hambre y el aburrimiento no debe poder ser negativo
* Se debe confecionar un menú para jugar, comer, hablar, salir

Si la infelicidad es < 5
	Feliz
Si la infelicidad es entre 5 y 10
	Ok
Sino si la infelicidad está entre 11 y 15
	Frustrado
Sino
	Enojado