from django.urls import path
from core.views import index, cadastra_item, edita_item

urlpatterns = [
    path("", index, name="index"),
    path("cadastrar", cadastra_item, name="cadastro_guitar"),
    path("item", edita_item, name="item")
]
