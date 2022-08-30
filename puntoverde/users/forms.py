from .models import CuentaAdmin
from django import forms
from crispy_forms.helper import FormHelper


class InputPassword(forms.ModelForm):
    class Meta:
        model = CuentaAdmin
        fields =[
            'password',
        ]
