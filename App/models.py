# App/models.py

# Django modules
from django.db import models

# Create your models here.


class Categorias(models.Model):
    CategoriaID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Estado = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.Nombre

    
class Cursos(models.Model):
    CursoId = models.AutoField(primary_key=True)
    Imagen = models.ImageField(null=True,upload_to='images/curso')
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Horas= models.IntegerField(default=0)
    Costo =  models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Estado = models.BooleanField()
    CategoriaID = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.Nombre


class Inscripcion(models.Model):
    CursoId = models.IntegerField(default=0)
    EstudianteID = models.IntegerField(default=0)
    Fecha = models.CharField(max_length=20)