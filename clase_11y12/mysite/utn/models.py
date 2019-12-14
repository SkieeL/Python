from django.db import models

# Create your models here.

class Persona(models.Model):
    class Meta:
        abstract = True

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

    def __str__(self):
        return "{} {}".format(self.apellido, self.nombre)

class Profesor(Persona):
    legajo = models.CharField(max_length=3)

class Estudiante(Persona):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    nota_primer_parcial = models.IntegerField()
    nota_segundo_parcial = models.IntegerField()
    nota_final = models.IntegerField()
