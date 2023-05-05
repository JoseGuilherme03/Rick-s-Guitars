from django import forms
from .models import Guitar


class GuitarForm(forms.ModelForm):
    class Meta:
        model = Guitar
        exclude = ["foto", "numero_serie", "preco", "modelo"]

        widgets = {
            "fabricante": forms.Select(attrs={"class": "form-control"}),
            "tipo": forms.Select(attrs={"class": "form-control"}),
            "madeira_tampo": forms.Select(attrs={"class": "form-control"}),
            "madeira_fundo": forms.Select(attrs={"class": "form-control"}),
        }


class CadastraGuitarForm(forms.ModelForm):
    class Meta:
        model = Guitar
        fields = "__all__"
        labels = {
            "numero_serie": "Número de Série",
            "preco": "Preço",
            "madeira_tampo": "Madeira do Tampo",
            "madeira_fundo": "Madeira do Fundo",
        }

        widgets = {
            "numero_serie": forms.TextInput(attrs={"class": "form-control"}),
            "preco": forms.NumberInput(attrs={"class": "form-control"}),
            "fabricante": forms.Select(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "tipo": forms.Select(attrs={"class": "form-control"}),
            "madeira_tampo": forms.Select(attrs={"class": "form-control"}),
            "madeira_fundo": forms.Select(attrs={"class": "form-control"}),
        }
