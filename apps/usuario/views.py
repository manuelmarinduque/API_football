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
        return reverse_lazy('Home') + '?register'
