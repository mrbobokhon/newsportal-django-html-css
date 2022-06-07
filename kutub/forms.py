from django import forms
from .models import Kutubxona


class KutubxonaForm(forms.ModelForm):
    class Meta:
        model = Kutubxona
        fields = '__all__'
