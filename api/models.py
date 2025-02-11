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

class Charge(models.Model):
    name = models.CharField(max_length=255)
    fragility = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    volume = models.CharField(max_length=255)
    photoUrl = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Request(models.Model):
    id = models.BigAutoField(primary_key=True)
    initial_address = models.CharField(max_length=255)
    final_address = models.CharField(max_length=255)
    cost_aprox = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    tittle = models.CharField(max_length=255)
    business_id = models.BigIntegerField()
    state = models.CharField(max_length=50)
    photo_url = models.URLField(max_length=255)
    date_time = models.DateTimeField()

    def __str__(self):
        return self.tittle
    
class TransportWorker(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    type_of_transport = models.CharField(max_length=255)
    transport_id = models.CharField(max_length=255)
    photo_url = models.URLField(max_length=255)

    def __str__(self):
        return self.name
    
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    userName = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)

    def __str__(self):
        return self.userName
