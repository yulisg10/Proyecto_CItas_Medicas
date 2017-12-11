# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from django.contrib.auth.models import User
from modelos.ciudad.models import Ciudad


# Create your models here.

class Medico(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	numero_documento = models.CharField('ID', primary_key=True, max_length=30) 
	tipo_documento = models.CharField(max_length=30)
	nombre = models.CharField(max_length=50)
	appellido=  models.CharField(max_length=50)
	telefono = models.CharField(max_length=20)
	correo = models.EmailField()
	fecha_nacimiento = models.DateField()
	direccion = models.CharField(max_length=50)
	ciudad = models.ForeignKey(Ciudad)
	genero = models.CharField(max_length=1)
	titulo = models.CharField(max_length=50)

	def __str__(self):
		return '{}{}'.format(self.nombre,self.appellido)