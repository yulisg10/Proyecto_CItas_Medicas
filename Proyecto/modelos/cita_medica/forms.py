from django import forms
from modelos.cita_medica.models import CitaMedica
from django.contrib.auth.models import user_logged_in, User
from django.http.request import HttpRequest 



class CitaMedicaForm(forms.ModelForm):

	

	class Meta:
		model = CitaMedica
		var = ''

		fields = [
			#'usuario',
			'medico',
			'fecha_cita',
			'hora_cita',
		]
		labels = {
			#'usuario': 'usuario',
			'medico': 'medico',
			'fecha_cita': 'fecha cita',
			'hora_cita': 'hora cita',

		}
		widgets = {

			#'usuario':forms.TextInput(attrs={'class':'form-control', 'value': var  }),
			'medico':forms.Select(attrs={'class':'form-control'}),
			'fecha_cita':forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'hora_cita':forms.TextInput(attrs={'class':'form-control','type':'time'}),

		}

		
