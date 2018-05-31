# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-30 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0002_auto_20180530_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='unidades',
            field=models.CharField(choices=[('pz', 'Piezas'), ('g', 'Gramos'), ('kg', 'Kilogramos'), ('m', 'Metros'), ('cm', 'Centímetros'), ('mm', 'Milímetros')], default='pz', max_length=2),
        ),
    ]
