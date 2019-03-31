from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps.usuario.forms import RegistroForm
from apps.usuario.models import Usuario


class SignUpView(CreateView):
    model = Usuario
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('Home')
