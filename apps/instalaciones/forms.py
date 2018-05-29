from django import forms

from .models import Instalacion


class InstalacionForm(forms.ModelForm):
    class Meta:
        model = Instalacion
        fields = '__all__'

        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'},  format='%Y-%m-%d'),
            'hora': forms.TimeInput(attrs={'type': 'time'},  format='%H:%M'),
        }
