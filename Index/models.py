from django.db import models

# Create your models here.
class Paleta(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=250)
    anio = models.IntegerField()
    