from django import forms
from modelos.medico.models import Medico
from django.contrib.auth.forms import User, UserCreationForm

class MedicoForm(forms.ModelForm):

	class Meta:

		model = Medico

		fields = [
			'numero_documento', 
			'tipo_documento',
			'nombre',
			'appellido',
			'telefono',
			#'correo',
			'fecha_nacimiento',
			'direccion',
			'ciudad',
			'genero',
			'titulo',
			
			
		]
		labels = {
			'numero_documento': 'Numero Documento',
			'tipo_documento':'Tipo Documento',
			'nombre':'Nombre',
			'appellido':'Apellido',
			'telefono':'Telefono',
			#'correo':'Correo',
			'fecha_nacimiento':'Fecha Nacimiento',
			'direccion':'Direccion',
			'ciudad':'Ciudad',
			'genero_medico':'Genero',
			'titulo':'Titulo',
			
		}
		widgets = {
			'numero_documento':forms.TextInput(attrs={'class':'form-control-lg, form-control-sm '}),
			'tipo_documento':forms.TextInput(attrs={'class':'form-control-lg, form-control-sm' }),
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'appellido':forms.TextInput(attrs={'class':'form-control'}),
			'telefono':forms.TextInput(attrs={'class':'form-control'}),
			#'correo':forms.EmailInput(attrs={'class':'form-control'}),
			'fecha_nacimiento':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
			'ciudad':forms.Select(attrs={'class':'form-control'}),
			'genero_medico':forms.TextInput(attrs={'class':'form-control'}),
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			
			
		}

class UserForm(UserCreationForm):
	
	class Meta:
		model = User 
		fields = [
			'username',
			#'first_name',
			#'last_name',
			'email',
			
			
		]
		labels = {
			'username':'Numero de Identificacion',
			#'first_name':'Nombre',
			#'last_name':'Apellidos',
			'email':'Correo',
		}		

	
	
		



