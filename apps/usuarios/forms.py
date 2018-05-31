from django import forms


class UsuarioForm(forms.Form):
    pass_actual = forms.CharField()
    pass_nuevo = forms.CharField()
    pass_nuevo_confirmacion = forms.CharField()