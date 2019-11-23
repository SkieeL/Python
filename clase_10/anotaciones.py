Web

HTTPS: Comunicación cifrada (no encriptada) 
Con un contrato definido entre partes para saber cómo decodificar el mensaje

Servidores Web:
Apache
nginx
IIS (.NET sólo funciona con IIS)

Si el servidor no sabe interpretar la extensión del archivo, devuelve el archivo directamente.

==================================================

Tipos de Cloud:
IAAS (Infrastructure as a service) (Hosting convencional)
PAAS (Plataform as a service)
 - Heroku
 - Google App Engine
 - Elastic bininstall
BAAS (Backend as a service)
 Pequeñas herramientas para apps mobile
 - Firebase
 - Amazon mobile
SAAS (Software as a service) (obviamente no es backend)
 - Gmail
 - Google Drive
 - Dropbox

AWS: Tiene una banda de servicios que vaya uno a saber cómo funcionan.
Google: Tiene menos servicios, pero apuntan a que sea más simple (3 clicks y que funcione).

===================================================

Frameworks de desarrollo web en Python

Frameworks armados con todas las herramientas necesarias y más
- Django
	Viene con un Admin de ABM para todas las tablas de una DB
	Tiene excelente documentación
- TurboGears
- Web2Py

Microframeworks
- Flask
 Armado de formularios
 Templates
 Reemplazo de valores

- Bottle
- CherryPy

=============================
Estructura de proyecto Django

__init__.py = Archivo que indica 
settings.py = Configuraciones horarias, DB, etc
urls.py = 
wsgi.py = Tiene que estar para que el servidor ejecute la app (no se toca)

=============================
Levantar servidores locales

python -m http.server port # Levanta un servidor HTTP local con Python
php -S locahost:port # Levanta un servudor HTTP local con PHP

=============================
Dark reader (extensión del navegador del profe)

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