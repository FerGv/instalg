# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-31 00:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_auto_20180530_1822'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lista',
            new_name='Item',
        ),
    ]
