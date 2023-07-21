from rest_framework import serializers

from apps.Usuarios.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        #fields = ['Nombre', 'Apellido', "dni", "Tipo", "Usuario"]
        fields = '__all__'