from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # Obligamos a que al registrarse se elija uno de los dos roles de la prueba
    role = serializers.ChoiceField(choices=[('Viewer', 'Viewer'), ('Admin', 'Admin')], write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role']

    def create(self, validated_data):
        role = validated_data.pop('role')
        
        # Django encripta automáticamente la contraseña 
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        
        # Guardamos el rol asignando al usuario a un Grupo de Django (RBAC)
        grupo, _ = Group.objects.get_or_create(name=role)
        user.groups.add(grupo)
        
        return user