Estructura de proyecto Django

__init__.py = Archivo que indica que es un paquete de Python bla bla bla
settings.py = Configuraciones horarias, DB, etc
urls.py = 
wsgi.py = Tiene que estar para que el servidor ejecute la app (no se toca)

=======================================================

pip install Django # Instala Django

django-admin startproject mysite # Crea un proyecto nuevo 'mysite'

python manage.py runserver port # Levanta servidor local
python manage.py runserver 0:port # Levanta un servidor en local accesible desde la red

python manage.py startapp polls # Crea una app nueva 'polls'

python manage.py migrate # Ejecuta las migraciones en la DB
python manage.py makemigrations polls # Genera las migraciones
1. Se crean o modifican Modelos en models.py
2. Se deben generar las Migraciones (python manage.py makemigrations nombre_app)
3. Se deben ejecutar las Migraciones (python manage.py migrate)

Las migraciones efectúan cambios en la DB, las cuales quedan registradas y permiten hacer rollback

python manage.py createsuperuser # Crea un superusuario para el panel de Administración

=======================================================
Estructura del directorio polls

models.py = Modelos que van a estar mapeados a tablas de la DB
admin.py = 

=============================
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