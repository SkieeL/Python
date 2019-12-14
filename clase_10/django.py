pip install Django # Instala Django
python3 -m pip install Django # Alternativa para instalar Django

django-admin startproject mysite # Crea un proyecto nuevo 'mysite'
python3 -m django startproject mysite # Alternativa para crear un nuevo proyecto

python manage.py runserver port # Levanta servidor local
python manage.py runserver 0:port # Levanta un servidor en local accesible desde la red

python manage.py startapp polls # Crea una app nueva 'polls'

python manage.py makemigrations polls # Genera las migraciones
python manage.py migrate # Ejecuta las migraciones en la DB

1. Se crean o modifican Modelos en models.py
2. Se deben generar las Migraciones (python manage.py makemigrations nombre_app)
3. Se deben ejecutar las Migraciones (python manage.py migrate)

Las migraciones efectúan cambios en la DB, las cuales quedan registradas y permiten hacer rollback

python manage.py createsuperuser # Crea un superusuario para el panel de Administración

=======================================================
Consultas SQL a los modelos

# Aclaraciones: hay dos clases 'Estudiante' y 'Profesor', donde cada estudiante tiene un profesor asignado como FK

InstanciaEstudiante.save() # Guarda/actualiza la instancia de Estudiante en la DB, si se está haciendo un insert se le asigna el ID
InstanciaEstudiante.delete() # Borra el registro de la DB
Estudiante.objects.all() # Trae todos los registros de la DB
Estudiante.objects.filter(id=1) # Trae el registro con ID 1, sirve para filtrar por cualquier campo
Estudiante.objects.exclude(nombre__startswith='Eze') # Trae los registros cuyo atributo 'nombre' NO empiece con 'Eze'
Estudiante.objects.all().order_by('nombre').asc() # Trae todos los registros ordenándolos por nombre ascendentemente
Estudiante.objects.all().order_by('-nombre') # Trae todos los registros ordenándolos por nombre descendentemente
Estudiante.objects.filter(profesor__nombre='German') # Trae todos los alumnos que tengan seteado el profesor cuyo nombre sea 'German'
Estudiante.objects.get(id=2) # Trae el registro con ID 2, si no lo encuentra arroja una exception 'DoesNotExist' 
Estudiante.objects.get(pk=2) # Trae el registro con su PK igual a 2
InstanciaProfesor.estudiante_set.all() # Trae todos los objetos 'estudiante' cuyo FK sea igual a la instancia, donde estudiante tiene un atributo FK hacia la la clase del objeto instanciado
InstanciaProfesor.estudiante_set.count() # Retorna la cantidad de estudiantes que tienen seteados en su FK la instancia de Profesor
InstanciaProfesor.estudiante_set.create(nombre='Eze', apellido='Mahafud') # Crea un Estudiante llamado 'Eze Mahafud' y le asigna como FK el profesor de la instancia (guarda el nuevo estudiante automáticamente en la DB)
InstanciaProfesor.estudiante_set.filter(nombre__startswith='Eze') # Trae los registros de la tabla 'Estudiantes' cuyo nombre empiece con 'Eze' y tengan seteado el profesor de la instancia

# Por defecto retorna un objeto de tipo QuerySet, el cual debe ser casteado a lista
# Se pueden acceder a los atributos de la lista de la siguiente forma
estudiantes = list(Estudiante.objects.filter(id=1))
estudiantes[0]['nombre'] # Accede al atributo 'nombre' del primer elemento de la lista 
estudiantes[0].nombre # También accede al atributo 'nombre del primer elemento de la lista

Doc de métodos: https://docs.djangoproject.com/es/2.2/ref/models/querysets/#queryset-api
Mostrar img (no se sabe si funciona): https://stackoverflow.com/questions/29360395/display-images-in-django

=======================================================
Estructura de proyecto Django

__init__.py = Archivo que indica que es un paquete de Python bla bla bla
settings.py = Configuraciones horarias, DB, etc
urls.py = 
wsgi.py = Tiene que estar para que el servidor ejecute la app (no se toca)

=======================================================
Estructura del directorio polls

models.py = Modelos que van a estar mapeados a tablas de la DB
admin.py = 

=======================================================
ORM: Object Relational Manager
Capa de abstracción entre el modelo de clase del lenguaje y la DB

VENTAJAS
- Se abstrae del lenguaje SQL
- Se puede cambiar el motor de DB sin modificar el código
- No se trabajan con tablas intermedias, se encarga el ORM

DESVENTAJAS
- No se tiene control total sobre las consultas SQL
- Es menos performante
- DESVENTAJA DE DJANGO: Por defecto NO hace JOINS, si tiene que hacer un JOIN primero hace una consulta principal y luego hace otra consulta por cada registro que debe traer