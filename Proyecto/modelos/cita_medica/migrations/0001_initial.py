# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 04:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medico', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateField()),
                ('hora_cita', models.DateTimeField()),
                ('fecha_solicitud', models.DateField()),
                ('hora_solicitud', models.DateTimeField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medico.Medico')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario')),
            ],
        ),
    ]
