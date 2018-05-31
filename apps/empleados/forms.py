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

    def clean_codigo_postal(self):
        codigo_postal = self.cleaned_data.get("codigo_postal")

        if len(codigo_postal) != 5 or not codigo_postal.isdigit():
            raise forms.ValidationError("Escribe un código postal válido. Ej: 05032")
        return codigo_postal