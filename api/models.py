from django.db import models

# Create your models here.

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    completado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    
class Business(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    logo = models.URLField()

    def __str__(self):
        return self.name
