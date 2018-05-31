from django.db import models


TIPOS_CONTRATO = (
    ('B', 'Base'),
    ('C', 'De confianza'),
)

class Puesto(models.Model):
    nombre = models.CharField(max_length=20)
    estado = models.BooleanField("Activo", default=True)
    tipo = models.CharField(max_length=1, choices=TIPOS_CONTRATO)

    def __str__(self):
        return f"{self.nombre}"