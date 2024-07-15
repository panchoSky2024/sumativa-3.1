from django.urls import path
from . import views

urlpatterns = [
    path('carrito/', views.carrito, name='carrito'),
    path('agregar/<int:zapatilla_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/zapas_del/<int:pk>/', views.zapas_del, name='zapas_del'),
    path('carrito_sin_autenticar/', views.carrito_sin_autenticar, name='carrito_sin_autenticar'),
]
