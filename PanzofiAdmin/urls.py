
from django.contrib import admin
from django.urls import path
#from django.contrib.auth.views import  LoginView


from apps.Usuarios.views import *
from apps.Login.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', LoginView.as_view(template_name = 'Usuarios/index.html'),  name="login"),
    #path('', LoginView.as_view(template_name = 'base.html'),  name="login"),
    path('Usuarios', UsuariosView.as_view(), name="serializer"),
    path('', LoginView.as_view(), name="login")
    
]
