from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from apps.Usuarios.models import *

from rest_framework.response import Response
from apps.Usuarios.serializer import *

class UsuariosView(APIView):
    def get(self, reques):
        output = [
            {"name": output.Nombre,
            "lastname": output.Apellido} for output in Usuarios.objects.all()
        ]
        
        return Response(output );
    
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data)