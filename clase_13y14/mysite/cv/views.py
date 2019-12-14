from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona, Capacitacion, ExperienciaLaboral, Hobbie

# Create your views here.

def home(request):
    datos_personales = list(Persona.objects.all())
    experiencias_laborales = list(
    	ExperienciaLaboral.objects.all().order_by('-fecha_desde')[:3]
    )
    educaciones = list(
    	Capacitacion.objects
    	.filter(tipo_capacitacion__nombre_tipo_capacitacion='Educacion')
    	.order_by('-fecha_desde')[:3]
    )
    cursos = list(
    	Capacitacion.objects
    	.filter(tipo_capacitacion__nombre_tipo_capacitacion='Curso')
    	.order_by('-fecha_desde')[:3]
    )
    hobbies = list(Hobbie.objects.all()[:3])
    context = {
    	'datos_personales': datos_personales,
    	'experiencias_laborales': experiencias_laborales,
    	'educaciones': educaciones,
    	'cursos': cursos,
    	'hobbies': hobbies,
    }
    return render(request, 'cv/home.html', context)

def datos_personales(request):
    datos_personales = list(Persona.objects.all())
    context = {'datos_personales': datos_personales }
    return render(request, 'cv/datos_personales.html', context)

def datos_contacto(request):
    datos_contacto = list(Persona.objects.all())
    context = {'datos_contacto': datos_contacto }
    return render(request, 'cv/datos_contacto.html', context)

def experiencia_laboral(request):
    experiencias_laborales = list(ExperienciaLaboral.objects.all())
    context = {'experiencias_laborales': experiencias_laborales }
    return render(request, 'cv/experiencia_laboral.html', context)

def educacion(request):
    educaciones = list(
    	Capacitacion.objects
    	.filter(tipo_capacitacion__nombre_tipo_capacitacion='Educacion')
    )
    context = {'educaciones': educaciones }
    return render(request, 'cv/educacion.html', context)

def cursos(request):
    cursos = list(
    	Capacitacion.objects
    	.filter(tipo_capacitacion__nombre_tipo_capacitacion='Curso')
    )
    context = {'cursos': cursos }
    return render(request, 'cv/cursos.html', context)

def hobbies(request):
    hobbies = list(Hobbie.objects.all())
    context = {'hobbies': hobbies }
    return render(request, 'cv/hobbies.html', context)