import re

from django import forms

from .models import Empleado


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'numero',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'email',
            'calle',
            'colonia',
            'delegacion',
            'municipio',
            'codigo_postal',
            'tipo',
        ]

    def clean_numero(self):
        numero = self.cleaned_data.get("numero")

        if len(numero) < 2:
            raise forms.ValidationError("Mínimo debes escribir 2 caracteres")

        if not re.search(r"[a-zA-Z]+", numero) or not re.search(r"\d+", numero):
            raise forms.ValidationError("El patrón válido es al menos una letra y un número")

        return numero

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")

        if re.search(r"[^a-zA-ZáéíóúÁÉÍÓÚ ]+", nombre):
            raise forms.ValidationError("Solo puedes escribir letras y espacios")

        return nombre

    def clean_apellido_paterno(self):
        apellido_paterno = self.cleaned_data.get("apellido_paterno")

        if re.search(r"[^a-zA-ZáéíóúÁÉÍÓÚ ]+", apellido_paterno):
            raise forms.ValidationError("Solo puedes escribir letras y espacios")

        return apellido_paterno

    def clean_apellido_materno(self):
        apellido_materno = self.cleaned_data.get("apellido_materno")

        if re.search(r"[^a-zA-ZáéíóúÁÉÍÓÚ ]+", apellido_materno):
            raise forms.ValidationError("Solo puedes escribir letras y espacios")

        return apellido_materno

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email

    def clean_calle(self):
        calle = self.cleaned_data.get("calle")

        if re.search(r"\^w+", calle):
            raise forms.ValidationError("Solo puedes escribir letras, números y espacios")

        return calle

    def clean_colonia(self):
        colonia = self.cleaned_data.get("colonia")

        if re.search(r"[^a-zA-ZáéíóúÁÉÍÓÚ ]+", colonia):
            raise forms.ValidationError("Solo puedes escribir letras y espacios")

        return colonia

    def clean_delegacion(self):
        delegacion = self.cleaned_data.get("delegacion")

        if re.search(r"[^a-zA-ZáéíóúÁÉÍÓÚ ]+", delegacion):
            raise forms.ValidationError("Solo puedes escribir letras y espacios")

        return delegacion

    def clean_municipio(self):
        municipio = self.cleaned_data.get("municipio")

        if re.search(r"[^a-zA-ZáéíóúÁÉÍÓÚ ]+", municipio):
            raise forms.ValidationError("Solo puedes escribir letras y espacios")

        return municipio

    def clean_codigo_postal(self):
        codigo_postal = self.cleaned_data.get("codigo_postal")

        if len(codigo_postal) != 5 or not codigo_postal.isdigit():
            raise forms.ValidationError("Escribe un código postal válido. Ej: 05032")

        return codigo_postal
