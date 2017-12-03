# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from modelos.usuario.models import Usuario
from modelos.medico.models import Medico

# Create your models here.

class CitaMedica(models.Model):
	
	usuario = models.ForeignKey(Usuario)
	medico = models.ForeignKey(Medico)
	fecha_cita = models.DateField()
	hora_cita = models.DateTimeField()
	fecha_solicitud = models.DateField(auto_now_add=True, blank=True)
	hora_solicitud = models.DateTimeField(auto_now_add=True, blank=True)
