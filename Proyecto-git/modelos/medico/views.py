# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from modelos.medico.models import Medico
from modelos.medico.forms import MedicoForm, UserForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView #Importa clases vistas genericas 
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from modelos.cita_medica.urls import urlpatterns

# Create your views here.
def index(request):
	return render(request,'medico/inicio.html')
	#return HttpResponse("index")


#Clase para crear medico doble tabla 
class MedicoCreate(CreateView):
	model = Medico
	template_name = "medico/registro.html"
	form_class = MedicoForm
	second_form_class = UserForm
	success_url = reverse_lazy("medico:success")

	def get_context_data(self, **kwargs):
		context = super(MedicoCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2']=self.second_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			medico = form.save(commit=False)
			medico.user = form2.save()
			medico.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))

class MedicoUpdate(UpdateView):
	model = Medico
	form_class = MedicoForm
	template_name = 'medico/medico_form.html'
	success_url = reverse_lazy("medico:listar_medico")

def registro_success(request):
	return render(request,'medico/registro_success.html')
