from django.shortcuts import render
from django.http import HttpResponse
from .models import Estudiante, Profesor

# Create your views here.

def index(request):
    return HttpResponse('Hola UTN!')

def estudiante(request, id_estudiante):
    try:
        estudiantes = list(Estudiante.objects.filter(id=id_estudiante))
        estudiante = estudiantes[0]
    except IndexError:
        return HttpResponse('El ID del estudiante que ingresaste no corresponde a nadie!')
    except:
        return HttpResponse('Hubo un error inesperado, contacte al Administrador!')
    else:
        return HttpResponse('El ID del estudiante que ingresaste corresponde a: {}'.format(estudiante))

def profesor(request, id_profesor):
    try:
        profesor = list(Profesor.objects.filter(pk=id_profesor))[0]
    except IndexError:
        return HttpResponse('El ID del profesor que ingresaste no corresponde a nadie!')
    except:
        return HttpResponse('Hubo un error inesperado, contacte al Administrador!')
    else:
        return HttpResponse('El ID del profesor que ingresaste corresponde a: {}'.format(profesor))