from django.shortcuts import render
from rest_framework.views import APIView
from apps.Usuarios.models import Usuarios
from apps.Session.models import Usuarios as Session
from rest_framework.response import Response
from apps.Usuarios.serializer import *
from rest_framework import status
import json
from django.utils.timezone import localtime
from django.utils import timezone
from datetime import timedelta
import pytz

class SessionView(APIView):
    
    model = Session;
    
    def get(self, request):
        out = []
        consolidate = {
            "button1" : {},
            "button2" : {},
            "time" : {},
        }
        
        zona_horaria_colombia = pytz.timezone("America/Bogota")
        
        
        
        for output in Session.objects.all():
            
            idUsuario = int(output.Usuario.id)
            nombreCompleto  = output.Usuario.Nombre + " " + output.Usuario.Apellido
            diferencia_tiempo = output.UltimaFecha - output.Fecha
            horas = diferencia_tiempo.seconds // 3600
            minutos = (diferencia_tiempo.seconds // 60) % 60
            segundos = diferencia_tiempo.seconds % 60
            
            if nombreCompleto not in consolidate["button1"]:
                consolidate["button1"][nombreCompleto] =0
                consolidate["button2"][nombreCompleto] =0
                consolidate["time"][nombreCompleto] =0
            
            consolidate["button1"][nombreCompleto] +=output.Boton1
            consolidate["button2"][nombreCompleto] +=output.Boton2
            consolidate["time"][nombreCompleto] +=  diferencia_tiempo.total_seconds()
            
            out.append(
                {
                    "Fecha": output.Fecha.astimezone(zona_horaria_colombia),
                    "Usuario": nombreCompleto,
                    "UltimaFecha": f"{horas} horas, {minutos} minutos, {segundos} segundos" ,
                    "Boton1": output.Boton1,
                    "Boton2": output.Boton2,
                    "TimeSecs": diferencia_tiempo.total_seconds()
                }
                
            )
        
        response = {
            "out" : out,
            "consolidate": consolidate
        }  
        
        return Response(response );
    
    def post(self, request):
        
        status_rsp = "error";
        msg_rsp ="";
        data = {}
        try:
            
            
            # se parsea el json
            custom_data = json.loads(request.body)
            if(request.session['user'] is not None):
                status_rsp = "ok"
            else:
                msg_rsp = "No session"
                
            return Response({'status':  status_rsp, 'data': tipo, 'message': msg_rsp}, status=status.HTTP_200_OK)
            
        
        except json.JSONDecodeError:
            return Response({'error': 'JSON inválido'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request):
        status_rsp = "error";
        msg_rsp ="";
       
                
        custom_data = json.loads(request.body)
        if( custom_data['button'] is not None and custom_data['session'] is not None):
            
            session =  self.model.objects.get(id=custom_data['session']);
            print(session ,custom_data['session'] )
            if(custom_data['button'] == 1):
                session.Boton1 +=1;
            elif(custom_data['button'] == 2):
                session.Boton2 +=1;
            
            session.UltimaFecha = timezone.now()
            session.save()
                
                
            status_rsp = "ok"
        else:
            msg_rsp = "No session"
            
        return Response({'status':  status_rsp,  'message': msg_rsp}, status=status.HTTP_200_OK)
                
            
        
