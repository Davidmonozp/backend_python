# api/serializers/vehiculo_serializers.py
from rest_framework import serializers
from api.models import Vehiculo  # Importa el modelo que está suelto en api/

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'