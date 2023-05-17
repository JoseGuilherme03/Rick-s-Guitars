# Importe as configurações do Django
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# Importe o modelo Guitar do seu aplicativo
from core.models import Guitar

# Crie uma nova guitarra
guitarra1 = Guitar(
    numero_serie="123456",
    preco=1999.99,
    fabricante="Fender",
    modelo="Exemplo1",
    tipo="Eletrico",
    madeira_tampo="Maple",
    madeira_fundo="Alder",
    foto="",
)

guitarra2 = Guitar(
    numero_serie="123457",
    preco=1999.99,
    fabricante="Fender",
    modelo="Exemplo2",
    tipo="Eletrico",
    madeira_tampo="Maple",
    madeira_fundo="Alder",
    foto="",
)

# Salve a guitarra no banco de dados
guitarra1.save()
guitarra2.save()

print("Guitarra criada com sucesso!")
