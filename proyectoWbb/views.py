from django.shortcuts import render

# Create your views here.

def base(request):
    context = {}  # Puedes añadir datos al contexto si es necesario
    return render(request, 'proyectoWbb/base.html', context)
