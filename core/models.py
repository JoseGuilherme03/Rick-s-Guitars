from django.db import models


class Guitar(models.Model):
    fabricantes = [
        ("Fender", "Fender"),
        ("Martin", "Martin"),
        ("Gibson", "Gibson"),
        ("Collings", "Collings"),
        ("Olson", "Olson"),
        ("Ryan", "Ryan"),
        ("PRS", "PRS"),
        ("Any", "Any"),
    ]
    tipos = [
        ("Acustico", "Acustico"),
        ("Eletrico", "Eletrico")
    ]
    madeiras = [
        ("Indian Rosewood", "Indian Rosewood"),
        ("Brazilian Rosewood", "Brazilian Rosewood"),
        ("Mahogany", "Mahogany"),
        ("Maple", "Maple"),
        ("Cocobolo", "Cocobolo"),
        ("Cedar", "Cedar"),
        ("Adirondack", "Adirondack"),
        ("Alder", "Alder"),
        ("Sitka", "Sitka"),
    ]
    numero_serie = models.CharField(max_length=50, primary_key=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    fabricante = models.CharField(max_length=50, choices=fabricantes, default="Any")
    modelo = models.CharField(max_length=150)
    tipo = models.CharField(max_length=50, choices=tipos, default="Eletrico")
    madeira_tampo = models.CharField(max_length=50, choices=madeiras)
    madeira_fundo = models.CharField(max_length=50, choices=madeiras)
    foto = models.ImageField(upload_to="guitars", blank=True)


