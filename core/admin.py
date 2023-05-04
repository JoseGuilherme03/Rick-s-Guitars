from django.contrib import admin
from core.models import Guitar


class GuitarAdmin(admin.ModelAdmin):
    list_display = ("numero_serie", "preco", "fabricante", "modelo", "tipo", "madeira_tampo", "madeira_fundo")
    list_filter = ("fabricante", "tipo", "madeira_tampo", "madeira_fundo")
    search_fields = ("numero_serie", "preco", "fabricante", "modelo", "tipo", "madeira_tampo", "madeira_fundo")


admin.site.register(Guitar, GuitarAdmin)

