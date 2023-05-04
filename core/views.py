from django.shortcuts import render
from core.models import Guitar
from .forms import GuitarForm


def index(request):
    filtro = GuitarForm()
    guitars = Guitar.objects.all()

    if request.method == "POST":
        if "form-filtro" in request.POST:
            form = GuitarForm(request.POST)
            if form.is_valid():
                fabricante = form.cleaned_data["fabricante"]
                modelo = form.cleaned_data["modelo"]
                tipo = form.cleaned_data["tipo"]
                madeira_tampo = form.cleaned_data["madeira_tampo"]
                madeira_fundo = form.cleaned_data["madeira_fundo"]

                # Filtra as guitarras de acordo com as opções escolhidas no formulário
                guitars = Guitar.objects.filter(
                    fabricante=fabricante,
                    modelo__icontains=modelo,
                    tipo=tipo,
                    madeira_tampo=madeira_tampo,
                    madeira_fundo=madeira_fundo,
                )
                
        elif "form-busca" in request.POST:
            nome_da_busca = request.POST.get("consulta")
            guitars = Guitar.objects.filter(modelo__icontains=nome_da_busca)

    return render(request, "index.html", {"guitars": guitars, "filtro": filtro})
