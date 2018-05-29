import time

from django.db import models

from apps.clientes.models import Cliente
from apps.empleados.models import Empleado


class Instalacion(models.Model):
    numero = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=50)
    numero_piso = models.CharField(max_length=50)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    empleados = models.ManyToManyField(Empleado)

    def __str__(self):
        return f"{self.id} - Piso {self.numero_piso} | Fecha {self.fecha} | Hora {self.hora.hour:02}:{self.hora.minute:02}"
