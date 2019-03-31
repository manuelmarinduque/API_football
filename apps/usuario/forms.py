from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.usuario.models import Usuario


# Create your forms here:
class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'cedula',
            'sexo',
            'telefono',
            'fecha_nacimiento',
            'pais',
            'ciudad',
        ]
