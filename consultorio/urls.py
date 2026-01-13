from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('listado/', views.list_pacientes, name='list_pacientes'),
    path('nuevo/', views.form_paciente, name='form_paciente'),
    # Esta línea es la que falta para el error 'editar_paciente'
    path('editar/<int:pk>/', views.form_paciente, name='editar_paciente'), 
    path('backup/', views.backup, name='backup'),
    path('base/', views.base, name='base'),
    
    path('imprimir/<int:pk>/', views.imprimir_paciente, name='imprimir_paciente'),
    
    
    
    path('eliminar/<int:pk>/', views.eliminar_paciente, name='eliminar_paciente'),






    
]
