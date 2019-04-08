from django import forms
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from apps.usuario.forms import RegistroForm, ProfileForm, EmailForm  # Es como tener en UserCreationForm
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
        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Nickname'})
        form.fields['first_name'].widget = forms.TextInput(
            attrs={'class': 'inputL input', 'placeholder': 'Nombre de usuario'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class': 'inputR input', 'placeholder': 'Apellidos'})
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'input form-control mb-2', 'placeholder': 'Correo electrónico'})
        form.fields['cedula'].widget = forms.TextInput(
            attrs={'class': 'inputL input', 'placeholder': 'Número de cédula'})
        form.fields['telefono'].widget = forms.TextInput(attrs={'class': 'inputR input', 'placeholder': 'Teléfono'})
        # Para no lidear con Select o ChoiceField y similares, no se coloca el campo 'sexo' en esta sección pero sí
        # en el 'registrar.html' y por defecto aparece las selecciones para este campo.
        form.fields['fecha_nacimiento'].widget = forms.SelectDateWidget(years=range(1919, 2019),
                                                                        attrs={'placeholder': 'Fecha de nacimiento'})
        form.fields['pais'].widget = forms.TextInput(attrs={'class': 'inputL input', 'placeholder': 'País'})
        form.fields['ciudad'].widget = forms.TextInput(attrs={'class': 'inputR input', 'placeholder': 'Ciudad'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'input form-control mb-2', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'input form-control mb-2', 'placeholder': 'Repite la contraseña'})
        return form


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'usuario/profile_form.html'

    # ¿cómo conseguir el id o pk de tal usuario y poder actualizar sus datos.
    # ¿sería buena idea pasar el pk del usuario en el path? La respuesta es NO, porque cualquiera podría
    # editar los perfiles de otros usuarios sólo conociendo el pk.

    # Conocer el pk del usuario logueado sin necesidad de pasarlo en el path porque este se almacena
    # en la propia request:
    def get_object(self, queryset=None):
        # recuperar el objeto que se va a editar
        profile, created = Usuario.objects.get_or_create(username=self.request.user)
        return profile


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'usuario/profile_email_form.html'

    # ¿cómo conseguir el id o pk de tal usuario y poder actualizar sus datos.
    # ¿sería buena idea pasar el pk del usuario en el path? La respuesta es NO, porque cualquiera podría
    # editar los perfiles de otros usuarios sólo conociendo el pk.

    # Conocer el pk del usuario logueado sin necesidad de pasarlo en el path porque este se almacena
    # en la propia request:
    def get_object(self, queryset=None):
        return self.request.user

    # Widget de email modificado en tiempo de ejecución porque tiene sus propias validaciones
    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2','placeholder': 'Correo electrónico'})
        return form
