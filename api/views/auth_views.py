# api/views/auth_views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from api.serializers import RegistroSerializer 

class RegistroView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegistroSerializer