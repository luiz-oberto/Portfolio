# core/forms.py
from django import forms

class NomeVisitanteForm(forms.Form):
    nome = forms.CharField(
        label='', # Qual seu nome?
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'})
    )
