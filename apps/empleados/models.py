from django.contrib.auth.models import User
from django.db import models

from apps.puestos.models import Puesto


TIPOS_EMPLEADO = (
	('IC', 'Ingeniero civil'),
	('AE', 'Administrador de empleados'),
	('AM', 'Administrador de materiales'),
	('AS', 'Administrador del sistema'),
)

class Empleado(models.Model):
	numero = models.CharField("Número de Empleado", max_length=50)
	puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
	nombre = models.CharField("Nombre", max_length=50)
	apellido_paterno = models.CharField("Apellido Paterno", max_length=50)
	apellido_materno = models.CharField("Apellido Materno", max_length=50)
	email = models.EmailField()
	calle = models.CharField("Calle", max_length=50)
	colonia = models.CharField("Colonia", max_length=50)
	delegacion = models.CharField("Delegación", max_length=50)
	municipio = models.CharField("Municipio", max_length=50)
	codigo_postal = models.CharField("Código Postal", max_length=50)
	tipo = models.CharField(max_length=2, choices=TIPOS_EMPLEADO)
	user = models.OneToOneField(User, null=True)

	class Meta:
		ordering = ['numero']

	def __str__(self):
		return f"{self.numero} - {self.nombre} {self.apellido_paterno} {self.apellido_materno}"
