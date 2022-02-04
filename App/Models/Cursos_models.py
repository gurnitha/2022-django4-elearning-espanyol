# App/Models/Cursos_models.py 

# Django modules
from django.db import models

# Locals
# from ..models import Cursos # <- ..models is the same as App.models
from App.models import Cursos

class Cursos_models():
    def cursos_list():
        cursos = Cursos.objects.order_by('Nombre')
        return cursos 