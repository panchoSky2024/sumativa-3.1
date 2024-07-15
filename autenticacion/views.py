from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse_lazy

def ini(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    messages.success(request, 'Has iniciado sesión correctamente.')
                    return redirect('base')  # Redirigir a la página principal
                else:
                    messages.error(request, 'Credenciales incorrectas.')
            except User.DoesNotExist:
                messages.error(request, 'Usuario no encontrado.')
        else:
            messages.error(request, 'Formulario no válido.')
    else:
        form = LoginForm()
    
    return render(request, 'autenticacion/ini.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"Usuario registrado: {user.username}")  # Verifica en la consola que el usuario se ha registrado correctamente
            return redirect('autenticacion:ini')  # Redirige al usuario a la página 'ini.html' después del registro
        else:
            print("El formulario no es válido. Errores:", form.errors)  # Verifica los errores del formulario en la consola
    else:
        form = CustomUserCreationForm()

    return render(request, 'autenticacion/registro.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect(reverse_lazy('base'))  # Ajusta 'base' por la URL a la que deseas redirigir después de cerrar sesión
