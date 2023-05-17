from django.shortcuts import render, redirect, get_object_or_404
from core.models import Guitar
from .forms import GuitarForm, CadastraGuitarForm


def index(request):
    filtro = GuitarForm()
    guitars = Guitar.objects.all()

    if request.method == "POST":
        if "form-filtro" in request.POST:
            form = GuitarForm(request.POST)
            if form.is_valid():
                fabricante = form.cleaned_data["fabricante"]
                tipo = form.cleaned_data["tipo"]
                madeira_tampo = form.cleaned_data["madeira_tampo"]
                madeira_fundo = form.cleaned_data["madeira_fundo"]

                # Filtra as guitarras de acordo com as opções escolhidas no formulário
                guitars = Guitar.objects.filter(
                    fabricante=fabricante,
                    tipo=tipo,
                    madeira_tampo=madeira_tampo,
                    madeira_fundo=madeira_fundo,
                )

        elif "form-busca" in request.POST:
            nome_da_busca = request.POST.get("consulta")
            guitars = Guitar.objects.filter(modelo__icontains=nome_da_busca)

        elif "cadastra-guitar" in request.POST:
            form = CadastraGuitarForm(request.POST, request.FILES)
            if form.is_valid():
                # Pega os dados do formulário e salva no banco de dados
                form.save()

    return render(request, "index.html", {"guitars": guitars, "filtro": filtro})


def cadastra_item(request):
    form = CadastraGuitarForm()
    return render(request, "cadastro.html", {"form": form})


def item(request, guitar_numero_serie):
    guitar = get_object_or_404(Guitar, pk=guitar_numero_serie)
    return render(request, "item.html", {"guitar": guitar})


def editar_item(request, guitar_numero_serie):
    guitar = Guitar.objects.get(numero_serie=guitar_numero_serie)
    form = CadastraGuitarForm(instance=guitar)

    if request.method == "POST":
        form = CadastraGuitarForm(request.POST, request.FILES, instance=guitar)
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(
        request, "editar_item.html", {"form": form, "numero_serie": guitar_numero_serie}
    )


def deletar_item(request, guitar_numero_serie):
    guitar = Guitar.objects.get(numero_serie=guitar_numero_serie)
    guitar.delete()
    return redirect("index")
