# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita_medica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citamedica',
            name='fecha_solicitud',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='citamedica',
            name='hora_solicitud',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]