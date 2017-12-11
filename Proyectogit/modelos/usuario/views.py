# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from modelos.usuario.models import Usuario
from modelos.usuario.forms import UsuarioForm, UserForm
from modelos.cita_medica.models import CitaMedica
from modelos.cita_medica.views import CitaCreate
from modelos.cita_medica.forms import CitaMedicaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView #Importa clases vistas genericas 
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from modelos.cita_medica.urls import urlpatterns
from Proyecto.utilidad import render_to_pdf
from django.views.generic import View

# Create your views here.

def index(request):
	return render(request,'usuario/inicio.html')
	#return HttpResponse("index")


#Clase para crear usuario doble tabla 
class GeneratePDF(View):
	def get(self, request, *args, **kwars):
		citamedica = CitaMedica.objects.order_by('fecha_cita')[:10]
		pdf = render_to_pdf('usuario/reporte.html', {'citamedica': citamedica})
		return HttpResponse(pdf, content_type='application/pdf' )
class UsuarioCreate(CreateView):
	model = Usuario
	template_name = "usuario/registro.html"
	form_class = UsuarioForm
	second_form_class = UserForm
	success_url = reverse_lazy("usuario:success")

	def get_context_data(self, **kwargs):
		context = super(UsuarioCreate, self).get_context_data(**kwargs)
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
			usuario = form.save(commit=False)
			usuario.user = form2.save()
			usuario.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))



class citar(CreateView):
	CitaCreate()
	success_url = reverse_lazy("usuario:inicio")


class UsuarioUpdate(UpdateView):
	model = Usuario
	form_class = UsuarioForm
	template_name = 'usuario/usuario_form.html'
	success_url = reverse_lazy("usuario:listar_usuario")


def registro_success(request):
	return render(request,'usuario/registro_success.html')
