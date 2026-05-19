# api/permissions/roles.py
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):

    message = "No tienes los permisos de Administrador necesarios para realizar esta acción."
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
            
        return request.user and request.user.groups.filter(name='Admin').exists()