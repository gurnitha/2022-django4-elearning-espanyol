# Usuarios/urls.py

# Django modules
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Locals
from App.Controllers.IndexController import IndexController

urlpatterns = [

    # Users
    # Get the parameters that are entered through the url to execute 
    # the views according to the parameter
    path('', IndexController.index, name='index'),
    path('about/', IndexController.about, name='about'),

    # Admin
    path('admin/', admin.site.urls, name='login'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)