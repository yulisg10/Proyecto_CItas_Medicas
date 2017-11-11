# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from modelos.cita_medica.models import CitaMedica
from modelos.cita_medica.forms import CitaMedicaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView #Importa clases vistas genericas 
from django.core.urlresolvers import reverse_lazy


# Create your views here.

def solicitud(request):
	return render(request,'cita_medica/solicitar_cita.html')
	#return HttpResponse("index")

class CitaList(ListView):
 	  model = CitaMedica
 	  template_name = 'CitaMedica/CitaMedica_list.html'

class CitaCreate(CreateView):
	#CitaMedica.objects.create()
 	model = CitaMedica
 	form_class = CitaMedicaForm
 	template_name = 'cita_medica/cita_medica_form.html'
 	#success_url = reverse_lazy("cita_medica:listarcita")

class CitaUpdate(UpdateView):
	model = CitaMedica
	form_class = CitaMedicaForm
	template_name = 'CitaMedica/cita_medica_form.html'
	#success_url = reverse_lazy("CitaMedica:listar_CitaMedica")

class CitaDelete(DeleteView):
	model = CitaMedica
	template_name = 'CitaMedica/CitaMedica_delete.html'
	#success_url = reverse_lazy("CitaMedica:listar_CitaMedica")



