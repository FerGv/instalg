from django.db import models

from apps.empleados.models import Empleado
from apps.instalaciones.models import Instalacion
from apps.materiales.models import Material


class Pedido(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    subtotal = models.FloatField(null=True)
    iva = models.FloatField(null=True)
    total = models.FloatField(null=True)
    status = models.BooleanField(default=False)
    materiales = models.ManyToManyField(Material, through='Item')

    def __str__(self):
        return f"{self.id} - Fecha {self.fecha} | Hora {self.hora}"

class Item(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    precio_unitario = models.FloatField()
    importe = models.FloatField()

    def __str__(self):
        return f"{self.material} - {self.cantidad} - ${self.precio_unitario} - ${self.importe}"
