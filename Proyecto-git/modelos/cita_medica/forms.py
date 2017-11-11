from django import forms
from modelos.cita_medica.models import CitaMedica


class CitaMedicaForm(forms.ModelForm):

	class Meta:
		model = CitaMedica

		fields = [
			'usuario',
			'medico',
			'fecha_cita',
			'hora_cita',
			'fecha_solicitud',
			'hora_solicitud',
		]
		labels = {
			'usuario': 'usuario',
			'medico': 'medico',
			'fecha_cita': 'fecha cita',
			'hora_cita': 'hora cita',

		}
		widgets = {

			'usuario':forms.TextInput(attrs={'class':'form-control'}),
			'medico':forms.Select(attrs={'class':'form-control'}),
			'fecha_cita':forms.TextInput(attrs={'class':'form-control'}),
			'hora_cita':forms.TextInput(attrs={'class':'form-control'}),

		}