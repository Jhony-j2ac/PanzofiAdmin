from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from apps.Usuarios.models import *
from rest_framework.response import Response
from apps.Usuarios.serializer import *
from rest_framework import status
from apps.Session.models import Usuarios as Session



import json

class LoginView(APIView):
    
    #second_model = Funcionarios;
    model = Usuarios;
    model2 = Session;
    
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
            tipo = "";
            user = "";
            session = "";
            if(email is not None and email != ""  and password is not None and password != ""  ):
                
                usuario =  self.model.objects.get(Correo=email,Password=password );
                #print(usuario.id)
                request.session['type'] = tipo =  usuario.Tipo.id
                user = usuario.id
                
                request.session['user'] = usuario.id
                
                sessionInsert = self.model2(Boton1=0, Boton2=0, Usuario=usuario)
                
                

                sessionInsert.save()
                
                request.session['session'] = sessionInsert.id
                session = sessionInsert.id
                
                
                status_rsp = "ok";
                
            else:
                msg_rsp ="No hay datos de login"
                
            return Response({'status':  status_rsp, 'type': tipo, 'user': user, 'session': session, 'message': msg_rsp}, status=status.HTTP_200_OK)
            
        except json.JSONDecodeError:
            return Response({'error': 'JSON inválido'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
        