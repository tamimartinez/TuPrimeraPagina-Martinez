from django.db import models

# Create your models here.

class Linea(models.Model):
    nombre = models.CharField(max_length=40)
    cuit = models.IntegerField()

class Terminal(models.Model):
    nombre = models.CharField(max_length=40)
    cuit = models.IntegerField()
    localidad = models.CharField(max_length=40)

class Incotems(models.Model):
    nombre = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=40)