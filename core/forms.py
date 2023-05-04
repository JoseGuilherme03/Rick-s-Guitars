from django import forms
from .models import Guitar


class GuitarForm(forms.ModelForm):
    class Meta:
        model = Guitar
        exclude = ["foto", "numero_serie", "preco"]

        widgets = {
            "fabricante": forms.Select(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "tipo": forms.Select(attrs={"class": "form-control"}),
            "madeira_tampo": forms.Select(attrs={"class": "form-control"}),
            "madeira_fundo": forms.Select(attrs={"class": "form-control"}),
        }