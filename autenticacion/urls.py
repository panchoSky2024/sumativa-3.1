from django.urls import path
from . import views

app_name = 'autenticacion'

urlpatterns = [
    path('ini/', views.ini, name='ini'),
    path('registro/', views.registro, name='registro'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]
