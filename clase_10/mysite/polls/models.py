from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Estudiante(models.Model):
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	dni = models.CharField(max_length=8)
	legajo = models.CharField(max_length=8)
	fecha_nacimiento = models.DateField('Fecha de nacimiento')
	sexo = models.CharField(max_length=10)
	direccion = models.CharField(max_length=50)
	telefono = models.CharField(max_length=15)

	def __str__(self):
		return self.apellido + ' ' + self.nombre