# App/Controllers/CursosController.py

# Django modules
from django.shortcuts import render

# Define your controller here.

class CursosController():
    def index(request):
        return render(request, 'views/cursos/cursos.html') 