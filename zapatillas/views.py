from django.shortcuts import render
from .models import Zapatilla

def catalogo(request):
    zapatillas = Zapatilla.objects.all()
    return render(request, 'zapatillas/catalogo.html', {'zapatillas': zapatillas})