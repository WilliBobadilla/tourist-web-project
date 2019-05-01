from django.db import models

TIPO_ACTIVIDAD= (
    ("Arte", "Arte y cultura"),
    ("Bares", "Bares y vida nocturna"),
    ("Natu", "Naturaleza y deportes"),
    ("Comida", "Comida y restaurantes"),
    ("Compras", "Compras")
)

TIPO_SEXO= (
    ("Mas", "Masculino"),
    ("Fem", "Femenino"),
)

TIPO_IDIOMAS= (
    ("Esp", "Español"),
    ("Ing", "Ingles"),
    ("Gua", "Guarani"),
    ("Esp_Ing", "Español e ingles"),
    ("Esp_Ing_Gua", "Español, ingles y guarani"),
    ("Esp_Ing", "Español y Guarani"),
)

class TipoActividad(models.Model):
    nombre = models.CharField(null= False, blank= False, max_length=100)  
    descripcion = models.TextField(null= True, blank= True)
    foto = models.ImageField(null= True, blank= True)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(null= False, blank= False, max_length=100) 
    tipo = models.ForeignKey('TipoActividad', on_delete=models.CASCADE,null=False)
    guia = models.ForeignKey('Guia', on_delete=models.CASCADE,null=True)
    foto = models.ImageField(null=True, blank=True)
    descripcion = models.TextField(null= False, blank= False)
  
    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    titulo = models.CharField(max_length=100) #Campo/columna titulo de tipo "campo de caracteres" de longitud maxima de 100
    descripcion = models.TextField(null=True, blank=True) #Campo/columna titulo de tipo Texto, los argumentos blank y null son para que el campo sea opcional
    #estado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Guia(models.Model):
    nombre = models.CharField(max_length=100) #Campo/columna titulo de tipo "campo de caracteres" de longitud maxima de 100
    sexo = models.CharField(max_length=100, choices= TIPO_SEXO)
    ciudad = models.ForeignKey('Ciudad', on_delete=models.SET_NULL,null=True)
    foto = models.ImageField(null=True, blank=True)
    idioma = models.CharField(max_length=100, choices= TIPO_IDIOMAS)
    biografia = models.TextField(null=True, blank=True) #Campo/columna titulo de tipo Texto, los argumentos blank y null son para que el campo sea opcional
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
        
    