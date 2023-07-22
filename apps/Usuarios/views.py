from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from apps.Usuarios.models import *



import json

class UsuariosView(APIView):
    def get(self, request):
        output = [
            {
                "name": output.Nombre,
                "lastname": output.Apellido
            }
            for output in Usuarios.objects.all()
        ]
        
        return Response(output );
    
    def post(self, request):
        
        try:
            
            # se parsea el json
            custom_data = json.loads(request.body)
            #return Response({'message': 'Datos recibidos correctamente'}, status=status.HTTP_200_OK)

            if(custom_data.get('login') is not None):
                print("exito")
            else:
                print("falso")
                
        
            
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid(raise_exception= True):
                serializer.save()
                return Response(serializer.data)
        
        except json.JSONDecodeError:
            return Response({'error': 'JSON inválido'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
        