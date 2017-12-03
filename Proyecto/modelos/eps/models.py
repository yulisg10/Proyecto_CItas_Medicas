# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Eps(models.Model):
	nombre = models.CharField(max_length=50)
	regimen = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)