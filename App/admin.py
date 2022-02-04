# App/admin.py

# Django modules
from django.contrib import admin

# Locals
from .models import Cursos, Categorias


class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("Nombre","Descripcion","Estado")
    search_fields = ('Nombre',)
    list_filter = ('Nombre', 'Estado')

# Register your models here.
admin.site.register(Cursos)
admin.site.register(Categorias,CategoriasAdmin)
