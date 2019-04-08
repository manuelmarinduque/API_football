from django.views.generic import CreateView
from apps.usuario.models import Usuario


# Create your views here.
class HomePageView(CreateView):
    model = Usuario
    template_name = 'base.html'
    fields = ['saldo']
