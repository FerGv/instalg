# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-30 21:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puestos', '0002_auto_20180530_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puesto',
            old_name='tipo_contrato',
            new_name='tipo',
        ),
    ]