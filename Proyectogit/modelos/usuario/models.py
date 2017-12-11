# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#Mis import
from django.contrib.auth.models import User
from modelos.eps.models import Eps
from modelos.ciudad.models import Ciudad
from django.core.signals import request_finished
from django.db.models.signals import post_save

from django.dispatch import receiver

#Fin mis import
# Create your models here.

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	numero_documento = models.CharField('ID', primary_key=True, max_length=30) 
	tipo_documento = models.CharField(max_length=30)
	nombre = models.CharField(max_length=50)
	appellido =  models.CharField(max_length=50)
	telefono = models.CharField(max_length=20)
	fecha_nacimiento = models.DateField()
	direccion = models.CharField(max_length=50)
	ciudad = models.ForeignKey(Ciudad)
	genero = models.CharField(max_length=1)
	eps = models.ForeignKey(Eps)
	password = models.CharField(max_length=30)

	def __str__(self):
		return '{}{}'.format(self.nombre,self.appellido)

	# @receiver(post_save, sender=User)
	# def create_user_usuario(sender, instance, created, **kwargs):
	# 	if created:
	# 		Usuario.objects.create(User=instance)

	# @receiver(post_save, sender=User)
	# def save_user_usuario(sender, instance, **kwargs):
	# 	instance.usuario.save()