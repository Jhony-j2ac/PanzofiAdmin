from django.db import models
from apps.Usuarios.models import Usuarios as User

# Create your models here.
class Usuarios( models.Model):

    Fecha = models.DateTimeField(auto_now_add=True)
    Usuario = models.ForeignKey(User, blank=False,unique=False,null=True, on_delete=models.PROTECT);
    UltimaFecha = models.DateTimeField(auto_now_add=True)
    Boton1 = models.BigIntegerField();
    Boton2 = models.BigIntegerField();
    
    def __str__(self):
        return self.Usuario.Nombre;