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



def apuesta_view(request):
	if request.method == 'POST':
		form = ApuestaForm(request.POST)
		if form.is_valid():

			form.save()
			return HttpResponseRedirect("/")
	else:
		form = ApuestaForm()
	return render(request,'apuesta/apuesta.html',{'form':form})


#def verifica_ganadores():

# Listas las apuestas en la vista
def apuesta_list(request):
	apuestaslist = Apuesta.objects.all().order_by('idApuesta')
	return render(request,'apuesta/apuesta.html',{'apuestaslist':apuestaslist})

#def apuesta_edit(request,id_apuesta):







