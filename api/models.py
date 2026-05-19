# api/models.py
from django.db import models

class Vehiculo(models.Model):  # <-- Asegúrate de que se llame exactamente así
    marca = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    aspirante = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca} - {self.aspirante}"