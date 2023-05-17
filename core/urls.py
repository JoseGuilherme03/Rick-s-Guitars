from django.urls import path
from core.views import index, cadastra_item, editar_item, item, deletar_item

urlpatterns = [
    path("", index, name="index"),
    path("cadastrar", cadastra_item, name="cadastro_guitar"),
    path("item/<int:guitar_numero_serie>", item, name="item"),
    path("editar-item/<int:guitar_numero_serie>", editar_item, name="editar_item"),
    path("deletar-item/<int:guitar_numero_serie>", deletar_item, name="deletar_item"),
]
