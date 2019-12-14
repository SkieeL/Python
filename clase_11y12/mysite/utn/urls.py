from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('estudiante/<int:id_estudiante>', views.estudiante, name='estudiante'),
    path('profesor/<int:id_profesor>', views.profesor, name='profesor')
]