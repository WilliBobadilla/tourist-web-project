from django.contrib import admin
from .models import Guia, Ciudad, Actividad, TipoActividad

# Register your models here.

admin.site.register(Guia)
admin.site.register(Ciudad)
admin.site.register(Actividad)
admin.site.register(TipoActividad)
