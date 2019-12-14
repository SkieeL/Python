from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	fecha_nacimiento = models.DateField('Fecha de nacimiento')
	email = models.EmailField('Correo')
	telefono = models.CharField(max_length=16)
	direccion = models.CharField(max_length=100)
	linkedin = models.URLField(max_length=100, default='')
	twitter = models.URLField(max_length=100, default='')
	instagram = models.URLField(max_length=100, default='')
	resumen = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=300)

	def __str__(self):
		return '{} {}'.format(self.apellido, self.nombre)

class ExperienciaLaboral(models.Model):
	fecha_desde = models.DateField()
	fecha_hasta = models.DateField(null=True, blank=True)
	nombre_empresa = models.CharField(max_length=100)
	tareas_principales = models.CharField(max_length=1000)

	def __str__(self):
		return '{} ({} - {})'.format(self.nombre_empresa, self.fecha_desde, self.fecha_hasta)

class TipoCapacitacion(models.Model):
	nombre_tipo_capacitacion = models.CharField(max_length=20)

	def __str__(self):
		return self.nombre_tipo_capacitacion

class Capacitacion(models.Model):
	fecha_desde = models.DateField()
	fecha_hasta = models.DateField(null=True, blank=True)
	nombre_institucion = models.CharField(max_length=100)
	titulo = models.CharField(max_length=100)
	tipo_capacitacion = models.ForeignKey(TipoCapacitacion, on_delete=models.CASCADE)

	def __str__(self):
		return '{} en {}'.format(self.titulo, self.nombre_institucion)

class Hobbie(models.Model):
	titulo = models.CharField(max_length=50)

	def __str__(self):
		return self.titulo
