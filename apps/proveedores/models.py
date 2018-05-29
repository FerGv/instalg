from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    empresa = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"