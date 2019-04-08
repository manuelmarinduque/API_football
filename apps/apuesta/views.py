from django.shortcuts import render,redirect,render_to_response, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from apps.apuesta.forms import ApuestaForm
from apps.apuesta.models import Apuesta
from django.views.generic import CreateView
from django.urls import reverse_lazy

"""
class ApuestaView(CreateView):
	model = Apuesta 
	template_name = 'apuesta/apuesta.html'
	form_class = Apuesta
	# Verificar si una apuesta se ha registrado:
"""


def index(request):
	return render(request,'apuesta/apuesta.html')


def apuesta_view(request):
	if request.method == 'POST':
		form = ApuestaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('apuesta:index')
	else:
		form = ApuestaForm()
	return render(request,'apuesta/apuesta.html',{'form':form})






