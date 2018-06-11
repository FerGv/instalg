from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Empleado


class TestEmpleado(TestCase):
    def setUp(self):
        self.empleado = Empleado()
        self.empleado.numero = "AE1"
        self.empleado.nombre = "Jael Karina"
        self.empleado.apellido_paterno = "Castillo"
        self.empleado.apellido_materno = "García"
        self.empleado.email = "email@email.com"
        self.empleado.calle = "Granaditas"
        self.empleado.colonia = "Centro"
        self.empleado.delegacion = "Coyoacán"
        self.empleado.municipio = "CDMX"
        self.empleado.codigo_postal = "09430"
        self.empleado.tipo = "IC"
        self.empleado.save()

    def test_numero_valido(self):
        self.assertEquals(self.empleado.numero, "AE1")

    def test_nombre_valido(self):
        self.assertEquals(self.empleado.nombre, "Jael Karina")

    def test_apellido_paterno_valido(self):
        self.assertEquals(self.empleado.apellido_paterno, "Castillo")

    def test_apellido_materno_valido(self):
        self.assertEquals(self.empleado.apellido_materno, "García")

    def test_email_valido(self):
        self.assertEquals(self.empleado.email, "email@email.com")

    def test_calle_valido(self):
        self.assertEquals(self.empleado.calle, "Granaditas")

    def test_colonia_valido(self):
        self.assertEquals(self.empleado.colonia, "Centro")

    def test_delegacion_valido(self):
        self.assertEquals(self.empleado.delegacion, "Coyoacán")

    def test_municipio_valido(self):
        self.assertEquals(self.empleado.municipio, "CDMX")

    def test_codigo_postal_valido(self):
        self.assertEquals(self.empleado.codigo_postal, "09430")

    def test_tipo_valido(self):
        self.assertEquals(self.empleado.tipo, "IC")

    def test_excepcion_numero_invalido(self):
        self.empleado.numero = "123"
        with self.assertRaises(ValidationError): self.empleado.full_clean()

    def test_excepcion_nombre_invalido(self):
        self.empleado.nombre = "F3rn@nd0"
        with self.assertRaises(ValidationError): self.empleado.full_clean()

    def test_excepcion_apellido_paterno_invalido(self):
        self.empleado.apellido_paterno = "C8stillo85"
        with self.assertRaises(ValidationError): self.empleado.full_clean()

    def test_excepcion_apellido_materno_invalido(self):
        self.empleado.apellido_materno = "Garc1a"
        with self.assertRaises(ValidationError): self.empleado.full_clean()

    def test_excepcion_email_invalido(self):
        self.empleado.email = "jaelcchz_21@gmail.com"
        with self.assertRaises(ValidationError): self.empleado.full_clean()

    def test_excepcion_calle_invalido(self):
        self.empleado.calle = "Gr@n@dit@s"
        with self.assertRaises(ValidationError): self.empleado.full_clean()

    def test_excepcion_colonia_invalido(self):
        self.empleado.colonia = "Centroarea4"
        with self.assertRaises(ValidationError): self.empleado.full_clean()

    def test_excepcion_delegacion_invalido(self):
        self.empleado.delegacion = "Coyoac@n"
        with self.assertRaises(ValidationError): self.empleado.full_clean()

    def test_excepcion_municipio_invalido(self):
        self.empleado.municipio = "CDMX 123"
        with self.assertRaises(ValidationError): self.empleado.full_clean()

    def test_excepcion_codigo_postal_invalido(self):
        self.empleado.codigo_postal = "0602584"
        with self.assertRaises(ValidationError): self.empleado.full_clean()

    def test_excepcion_tipo_invalido(self):
        self.empleado.tipo = None
        with self.assertRaises(ValidationError): self.empleado.full_clean()
