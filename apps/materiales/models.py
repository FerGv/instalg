from django.db import models

from apps.proveedores.models import Proveedor


UNIDADES = (
    ('pz', 'Piezas'),
    ('g', 'Gramos'),
    ('kg', 'Kilogramos'),
    ('m', 'Metros'),
    ('cm', 'Centímetros'),
    ('mm', 'Milímetros'),
)

class Material(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    existencia = models.FloatField()
    descripcion = models.CharField("Descripción", max_length=50)
    precio = models.FloatField()
    unidades = models.CharField(max_length=2, choices=UNIDADES, default='pz')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.nombre}"
