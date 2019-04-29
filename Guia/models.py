from django.db import models

# Create your models here.


class Guia(models.Model):
    nombre = models.CharField(max_length=100) #Campo/columna titulo de tipo "campo de caracteres" de longitud maxima de 100
    sexo = models.CharField(max_length=100)
    foto = models.ImageField(max_length=100)
    idioma = models.CharField(max_length=100)
    biografia = models.TextField(null=True, blank=True) #Campo/columna titulo de tipo Texto, los argumentos blank y null son para que el campo sea opcional
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
        
    