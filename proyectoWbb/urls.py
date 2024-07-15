from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),  # Asigna la vista de inicio a la URL raíz de la aplicación
    # Puedes agregar más rutas aquí según sea necesario
]