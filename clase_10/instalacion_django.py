Estructura de proyecto Django

__init__.py = Archivo que indica que es un paquete de Python bla bla bla
settings.py = Configuraciones horarias, DB, etc
urls.py = 
wsgi.py = Tiene que estar para que el servidor ejecute la app (no se toca)

=======================================================

pip install Django # Instala Django

django-admin startproject mysite # Crea proyecto nuevo

python manage.py runserver port # Levanta servidor local
python manage.py runserver 0:port # Levanta un servidor en local accesible desde la red

python manage.py startapp polls # 

python manage.py migrate # Ejecuta las migraciones en la DB
python manage.py makemigrations polls # Genera las migraciones
1. Se crean o modifican Modelos
2. Generación de Migraciones
3. Ejecucuón de Migraciones

Las migraciones efectúan cambios en la DB, las cuales quedan registradas y permiten hacer rollback

python manage.py createsuperuser # Crea un superusuario para el panel de Administración

=======================================================
Estructura del directorio polls

models.py = Modelos que van a estar mapeados a tablas de la DB
admin.py = 