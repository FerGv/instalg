# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleados', '0001_initial'),
        ('materiales', '0001_initial'),
        ('instalaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField()),
                ('precio_unitario', models.FloatField()),
                ('subtotal', models.FloatField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiales.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('total', models.FloatField()),
                ('iva', models.FloatField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.Empleado')),
                ('instalacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instalaciones.Instalacion')),
                ('materiales', models.ManyToManyField(through='pedidos.DetallePedido', to='materiales.Material')),
            ],
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Pedido'),
        ),
    ]
