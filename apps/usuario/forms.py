from datetime import date

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

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get("fecha_nacimiento")
        fecha_actual = date.today()
        dias = fecha_actual - fecha_nacimiento
        if dias.days < 6574:
            raise forms.ValidationError("Debes ser mayor de edad")
        return fecha_nacimiento


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'cedula', 'saldo', 'telefono', 'fecha_nacimiento',
                  'pais', 'ciudad']
        widgets = {
            'username': forms.TextInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput(),
            'cedula': forms.TextInput(),
            'saldo': forms.TextInput(),
            'telefono': forms.TextInput(),
            'fecha_nacimiento': forms.SelectDateWidget(years=range(1919, 2019)),
            'pais': forms.TextInput(),
            'ciudad': forms.TextInput(),
        }

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get("fecha_nacimiento")
        fecha_actual = date.today()
        dias = fecha_actual - fecha_nacimiento
        if dias.days < 6574:
            raise forms.ValidationError("Debes ser mayor de edad")
        return fecha_nacimiento


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya está registrado")
        return email
