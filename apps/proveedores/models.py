from django.contrib.auth.models import User
from django.db import models


class Proveedor(models.Model):
    numero = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    empresa = models.CharField(max_length=30)
    user = models.OneToOneField(User, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
        