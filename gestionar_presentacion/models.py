from django.db import models


class Presentacion(models.Model):
    nombre = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
# Create your models here.
