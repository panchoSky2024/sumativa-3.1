from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Correo Electrónico :⠀⠀⠀',
        max_length=254,
        help_text='Requerido. Ingrese un correo válido.',
    )
    password1 = forms.CharField(
        label='Contraseña :⠀⠀⠀⠀⠀⠀⠀⠀',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='La contraseña debe tener al menos 6 caracteres.'
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña :⠀',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='Ingrese la misma contraseña que antes, para verificación.'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de Usuario :⠀⠀',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email:
            raise forms.ValidationError('El correo electrónico debe contener un "@"')
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 6:
            raise forms.ValidationError('La contraseña debe tener al menos 6 caracteres.')
        return password1

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo Electrónico :')
    password = forms.CharField(label='Contraseña ⠀⠀⠀⠀⠀', widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    
    
