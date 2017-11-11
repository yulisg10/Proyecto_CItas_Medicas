from django import forms
from modelos.usuario.models import Usuario
from django.contrib.auth.forms import User, UserCreationForm

class UsuarioForm(forms.ModelForm):

	class Meta:
		model = Usuario

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
			'eps',
			
			
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
			'genero_usuario':'Genero',
			'eps_usuario':'EPS',
			
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
			'genero_usuario':forms.TextInput(attrs={'class':'form-control'}),
			'eps':forms.Select(attrs={'class':'form-control'}),
			
			
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

	
	
		



