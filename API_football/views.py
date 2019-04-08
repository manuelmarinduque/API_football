from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from apps.usuario.models import Usuario


# Create your views here.
class HomePageView(CreateView):
    model = Usuario
    template_name = 'base.html'
    fields = ['saldo']


# Para mostrar los usuarios al administrador:
@method_decorator(login_required, name='dispatch')
class UsuarioList(ListView):
    model = Usuario


@method_decorator(login_required, name='dispatch')
class UsuarioDetailView(DetailView):
    model = Usuario


# Para actualizar el saldo de un usuario:
@method_decorator(login_required, name='dispatch')
class SaldoUpdate(UpdateView):
    model = Usuario
    fields = ['saldo', 'saldo2']
    template_name = 'usuario/saldo_aumento.html'
    reverse_lazy('listado')

    def get_success_url(self):
        return reverse_lazy('actu_saldo', args=[self.object.cedula])
