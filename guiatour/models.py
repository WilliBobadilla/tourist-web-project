from django.db import models

TIPO_ACTIVIDAD= (
    ("Arte", "Arte y cultura"),
    ("Bares", "Bares y vida nocturna"),
    ("Natu", "Naturaleza y deportes"),
    ("Comida", "Comida y restaurantes"),
    ("Compras", "Compras")
)

class Actividad(models.Model):
    nombre = models.CharField(null= False, blank= False, max_length=100) 
    tipo = models.CharField(max_length=100, choices= TIPO_ACTIVIDAD) 
    descripcion = models.TextField(null= False, blank= False)
  
class Ciudad(models.Model):
    titulo = models.CharField(max_length=100) #Campo/columna titulo de tipo "campo de caracteres" de longitud maxima de 100
    descripcion = models.TextField(null=True, blank=True) #Campo/columna titulo de tipo Texto, los argumentos blank y null son para que el campo sea opcional
    #estado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Guia(models.Model):
    nombre = models.CharField(max_length=100) #Campo/columna titulo de tipo "campo de caracteres" de longitud maxima de 100
    sexo = models.CharField(max_length=100)
    foto = models.ImageField(max_length=100)
    idioma = models.CharField(max_length=100)
    biografia = models.TextField(null=True, blank=True) #Campo/columna titulo de tipo Texto, los argumentos blank y null son para que el campo sea opcional
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
        
    