# api/views/vehiculo_views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404  # <-- Corregido a 404 aquí
from api.models import Vehiculo
from api.serializers import VehiculoSerializer
from api.permissions.roles import IsAdminOrReadOnly 

class VehiculoViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    # 1. INDEX: GET /api/vehiculos/
    def list(self, request):
        vehiculos = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. STORE: POST /api/vehiculos/
    def create(self, request):
        serializer = VehiculoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 3. SHOW: GET /api/vehiculos/{id}/
    def retrieve(self, request, pk=None):
        # Corregido a 404 aquí (como el findOrFail)
        vehiculo = get_object_or_404(Vehiculo, pk=pk)
        serializer = VehiculoSerializer(vehiculo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. UPDATE: PUT /api/vehiculos/{id}/
    def update(self, request, pk=None):
        # Corregido a 404 aquí
        vehiculo = get_object_or_404(Vehiculo, pk=pk)
        serializer = VehiculoSerializer(vehiculo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 5. DESTROY: DELETE /api/vehiculos/{id}/
    def destroy(self, request, pk=None):
        # Corregido a 404 aquí
        vehiculo = get_object_or_404(Vehiculo, pk=pk)
        vehiculo.delete()
        return Response(
            {"message": "Vehículo eliminado correctamente"}, 
            status=status.HTTP_204_NO_CONTENT
        )