from django.urls import path
from core.views import index, cadastra_guitar

urlpatterns = [
    path("", index, name="index"),
    path("cadastrar", cadastra_guitar, name="cadastro_guitar"),
]
