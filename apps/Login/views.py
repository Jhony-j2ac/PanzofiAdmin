from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from apps.Usuarios.models import *
from rest_framework.response import Response
from apps.Usuarios.serializer import *
from rest_framework import status

import json

class LoginView(APIView):
    
    #second_model = Funcionarios;
    model = Usuarios;
    
    def get(self, request):
        
        return Response([]);
    def post(self, request):
        
        status_rsp = "error";
        msg_rsp ="";
        try:
            # se parsea el json
            custom_data = json.loads(request.body)
            #return Response({'message': 'Datos recibidos correctamente'}, status=status.HTTP_200_OK)

            email = custom_data.get('email')
            password = custom_data.get('password')
            if(email is not None and email != ""  and password is not None and password != ""  ):
                
                usuario =  self.model.objects.get(Correo=email,Password=password );
                #print(usuario.Apellido)
                
                status_rsp = "ok";
                
            else:
                msg_rsp ="No hay datos de login"
                
            return Response({'status':  status_rsp, 'type':usuario.Tipo , 'message': msg_rsp}, status=status.HTTP_200_OK)
            
        except json.JSONDecodeError:
            return Response({'error': 'JSON inválido'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
        