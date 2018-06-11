import re

from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError

# from apps.puestos.models import Puesto


TIPOS_EMPLEADO = (
	('IC', 'Ingeniero civil'),
	('AE', 'Administrador de empleados'),
	('AM', 'Administrador de materiales'),
	('AS', 'Administrador del sistema'),
)

class Empleado(models.Model):
	numero = models.CharField("Número de Empleado", max_length=50)
	# puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
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
	user = models.OneToOneField(User, null=True, blank=True)

	class Meta:
		ordering = ['numero']

	def __str__(self):
		return f"{self.numero} - {self.nombre} {self.apellido_paterno} {self.apellido_materno}"

	def clean(self):
		if not self.numero or len(self.numero) < 2:
			raise ValidationError("Mínimo debes escribir 2 caracteres")

		if not self.numero or not re.search(r"[a-zA-Z]+", self.numero) or not re.search(r"\d+", self.numero):
			raise ValidationError("El patrón válido es al menos una letra y un número")

		if not self.nombre or re.search(r"[^a-zA-ZáéíóúÁÉÍÓÚ ]+", self.nombre):
			raise ValidationError("Solo puedes escribir letras y espacios")

		if not self.apellido_paterno or re.search(r"[^a-zA-ZáéíóúÁÉÍÓÚ ]+", self.apellido_paterno):
			raise ValidationError("Solo puedes escribir letras y espacios")

		if not self.apellido_materno or re.search(r"[^a-zA-ZáéíóúÁÉÍÓÚ ]+", self.apellido_materno):
			raise ValidationError("Solo puedes escribir letras y espacios")

		if not self.email or not re.search(r"[^A-Z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z]{2,4}$", self.email.upper()):
			raise ValidationError("Escribe un email válido. Ej: email@email.com")

		if not self.calle or re.search(r"\^w+", self.calle):
			raise ValidationError("Solo puedes escribir letras, números y espacios")

		if not self.colonia or re.search(r"[^a-zA-ZáéíóúÁÉÍÓÚ ]+", self.colonia):
			raise ValidationError("Solo puedes escribir letras y espacios")

		if not self.delegacion or re.search(r"[^a-zA-ZáéíóúÁÉÍÓÚ ]+", self.delegacion):
			raise ValidationError("Solo puedes escribir letras y espacios")

		if not self.municipio or re.search(r"[^a-zA-ZáéíóúÁÉÍÓÚ ]+", self.municipio):
			raise ValidationError("Solo puedes escribir letras y espacios")

		if not self.codigo_postal or len(self.codigo_postal) != 5 or not self.codigo_postal.isdigit():
			raise ValidationError("Escribe un código postal válido. Ej: 05032")

		if not self.tipo or not self.tipo in ['IC', 'AM', 'AE', 'AS']:
			raise ValidationError("Debes seleccionar un tipo de empleado válido")
