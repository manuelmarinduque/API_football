from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from apps.usuario.models import Usuario


# Create your forms here:
class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "cedula",
            "sexo",
            "telefono",
            "fecha_nacimiento",
            "pais",
            "ciudad",
        ]

    # Método para limpiar o validar el campo email
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado")
        return email