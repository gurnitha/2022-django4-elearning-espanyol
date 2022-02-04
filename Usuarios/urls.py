# Usuarios/urls.py

# Django modules
from django.contrib import admin
from django.urls import path

# Locals
from Usuarios.Controllers.IndexController import IndexController

urlpatterns = [

    # Users
    # Get the parameters that are entered through the url to execute 
    # the views according to the parameter
    path('', IndexController.index, name='index'),

    # Admin
    path('admin/', admin.site.urls),
]
