from django import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps.usuario.forms import RegistroForm  # Es como tener en UserCreationForm
from apps.usuario.models import Usuario


class SignUpView(CreateView):
    model = Usuario
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm

    # Verificar si un usuario se ha registrado:
    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificar widgets en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Nickname'})
        form.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'Nombre de usuario'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Apellidos'})
        form.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Correo electrónico'})
        form.fields['cedula'].widget = forms.TextInput(attrs={'placeholder': 'Número de cédula'})
        form.fields['telefono'].widget = forms.TextInput(attrs={'placeholder': 'Teléfono'})
        # Para no lidear con Select o ChoiceField y similares, no se coloca el campo 'sexo' en esta sección pero sí
        # en el 'registrar.html' y por defecto aparece las selecciones para este campo.
        form.fields['fecha_nacimiento'].widget = forms.SelectDateWidget(years=range(1919, 2019),
                                                                        attrs={'placeholder': 'Fecha de nacimiento'})
        form.fields['pais'].widget = forms.TextInput(attrs={'placeholder': 'País'})
        form.fields['ciudad'].widget = forms.TextInput(attrs={'placeholder': 'Ciudad'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Repite la contraseña'})
        return form
