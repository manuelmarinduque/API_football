from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.usuario.models import Usuario


# Create your forms here:
class RegistroForm(UserCreationForm):
    generos = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )
    sexo = forms.ChoiceField(choices=generos)

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
