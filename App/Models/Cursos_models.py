# App/Models/Cursos_models.py 

# Django modules
from django.db import models

# Locals
# from ..models import Cursos # <- ..models is the same as App.models
from App.models import Cursos, Categorias

class Cursos_models():
    def cursos_list():
        cursos = Cursos.objects.order_by('Nombre')
        return cursos 

    # def getcurso(idcurso):
    #     curso = Cursos.objects.get(CursoId=idcurso) 
    #     return curso 
        
    def getcurso(idcurso):
        curso = Cursos.objects.filter(CursoId=idcurso) 
        for item in curso:
            categoria = Categorias.objects.get(CategoriaID=item.CategoriaID.CategoriaID)
        return [item,categoria] 