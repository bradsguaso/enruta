from django.db import models

# Create your models here.

from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    completado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
