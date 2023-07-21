from django.db import models
from django.contrib.auth.models import User


class Tipo(models.Model):
    nombre = models.CharField(max_length = 50, choices=(('1', 'Regular'),('2', 'Admin')));


class DocumentosTipo(models.Model):
    nombre = models.CharField(max_length = 50, choices=(('CC', 'Cedula Ciudadania'),('TI', 'Tajeta de identidad')));
# Create your models here.
class Usuarios( models.Model):

    Nombre = models.CharField(max_length=50);
    Apellido = models.TextField(max_length=50);
    dni = models.BigIntegerField();
    Usuario = models.OneToOneField(User, blank=False, null=True, on_delete=models.PROTECT);
    Tipo = models.ForeignKey(Tipo, blank = False, null=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.Nombre;



