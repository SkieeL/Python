from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('datos_personales/', views.datos_personales, name='datos_personales'),
    path('datos_contacto/', views.datos_contacto, name='datos_contacto'),
    path('experiencia_laboral/', views.experiencia_laboral, name='experiencia_laboral'),
    path('educacion/', views.educacion, name='educacion'),
    path('cursos/', views.cursos, name='cursos'),
    path('hobbies/', views.hobbies, name='hobbies'),
]