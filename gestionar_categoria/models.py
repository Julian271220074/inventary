
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

