# App/admin.py

# Django modules
from django.contrib import admin
from django.utils.html import format_html

# Locals
from .models import Cursos, Categorias


class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("Nombre","Descripcion","Estado")
    search_fields = ('Nombre',)
    list_filter = ('Nombre', 'Estado')

class CursosAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img width="85" height="45" src="/media/{}" />'.format(obj.Imagen))
    image_tag.short_description = 'Imagen'
    readonly_fields = ['image_tag']
    raw_id_fields = ('CategoriaID', )
    list_display = ('image_tag','Nombre','Descripcion','Horas','Costo','Estado')
    list_filter = ('Nombre', 'Estado')
    search_fields = ('Nombre','Descripcion' )

    pass

# Register your models here.
admin.site.register(Categorias,CategoriasAdmin)
admin.site.register(Cursos,CursosAdmin)    