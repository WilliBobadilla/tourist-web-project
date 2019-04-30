from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse
from .models import Ciudad
from .models import Guia
# Create your views here.


def salida(request):
    despedida = Ciudad.objects.all()
    despe = Guia.objects.all()
    #return HttpResponse(despedida)
    return render(request,"index.html",{"ciudades":despedida, "guias":despe })
=======
from guiatour.models import Ciudad, TipoActividad, Actividad, Guia
from django.http import HttpResponse

# Create your views here.

def index(request):
    id_asuncion = Ciudad.objects.all()[0].id
    id_encarnacion = Ciudad.objects.all()[1].id
    id_cde = Ciudad.objects.all()[2].id
    contexto = {
        "id_asuncion" : id_asuncion,
        "id_encarnacion" : id_encarnacion, 
        "id_cde" : id_cde,
    }

    return HttpResponse(id_encarnacion)


def detalle_ciudad(request,id):
    ciudad = Ciudad.objects.get(id=id)
    tipo_actividades = TipoActividad.objects.all()
    lista_actividades = Actividad.objects.filter(guia__ciudad__id=id)
    
    return HttpResponse(lista_actividades)

def perfil_guia (request,id):
    print(id)
    guia = Guia.objects.get(id=id)
    print(guia)
    #return HttpResponse(guia)

    return render(request, 'perfilguia.html', {"guia":guia})

    
    
>>>>>>> cfdb2c8e7600039f80a91720ef90e7e707b4987f
