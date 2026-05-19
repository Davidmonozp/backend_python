# api/views/admin_temp.py
from django.contrib.auth.models import User
from django.http import HttpResponse

def crear_admin(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@ejemplo.com', 'mi_password_seguro')
        return HttpResponse("¡Usuario administrador creado con éxito!")
    return HttpResponse("El usuario ya existe.")