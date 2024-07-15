from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from zapatillas.models import Zapatilla
from .models import Carrito, ItemCarrito
from django.contrib import messages

@login_required
def carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items_carrito = carrito.items.all()
    return render(request, 'carrito/carrito.html', {'items_carrito': items_carrito})

def carrito_sin_autenticar(request):
    messages.warning(request, 'Debes iniciar sesión para ver tu carrito.')
    return render(request, 'autenticacion/ini.html')
@login_required
def agregar_al_carrito(request, zapatilla_id):
    zapatilla = get_object_or_404(Zapatilla, id_zapatilla=zapatilla_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    item_carrito, item_created = ItemCarrito.objects.get_or_create(carrito=carrito, zapatilla=zapatilla)
    
    if not item_created:
        item_carrito.cantidad += 1
        item_carrito.save()
    
    return redirect('catalogo')  # Redirigir a la página de catálogo u otra vista deseada

def zapas_del(request, pk):
    item_carrito = get_object_or_404(ItemCarrito, id=pk)
    item_carrito.delete()
    return redirect('carrito')  # Redirigir a la vista del carrito

@login_required
def carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items_carrito = carrito.items.all()
    return render(request, 'carrito/carrito.html', {'items_carrito': items_carrito})
