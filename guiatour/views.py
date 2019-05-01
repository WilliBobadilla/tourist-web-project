from django.shortcuts import render
from guiatour.models import Ciudad, TipoActividad, Actividad, Guia
from django.http import HttpResponse

# Create your views here.

def index(request):
    id_asuncion = Ciudad.objects.all()[0].id
    id_encarnacion = Ciudad.objects.all()[1].id
    id_cde = Ciudad.objects.all()[2].id
    contenido = {
        "id_asuncion" : id_asuncion,
        "id_encarnacion" : id_encarnacion, 
        "id_cde" : id_cde,
        "ciudades":Ciudad.objects.all(),
    }

    return render(request, 'index.html', contenido)


def detalle_ciudad(request,id):
    ciudad = Ciudad.objects.get(id=id)
    tipo_actividades = TipoActividad.objects.all()
    lista_actividades = Actividad.objects.filter(guia__ciudad__id=id)
    
    return HttpResponse(lista_actividades)

def perfil_guia (request,id):
    print(id)
    guia = Guia.objects.get(id=id)
    actividades = Actividad.objects.filter(guia=guia)
    print(guia)
    #return HttpResponse(guia)
    contexto = {"guia":guia,"actividades":actividades}
    return render(request, 'perfilguia.html', contexto)


def detalle_actividad(request,id):
    print(id)
    #Obtener actividad solicitada
    actividad = Actividad.objects.get(id=id)
    guia = actividad.guia
    contexto = {"actividad":actividad,"guia":guia}
    print(actividad)

    return render(request,'detalle_actividad.html', contexto)

# funcion para que aparezca plantilla actividad final
def acti_final (request):

    contenido = {
        "ciudades":Ciudad.objects.all(),
        "actividades":Actividad.objects.all(),
        "pepito": "HOOOOOOOOOOOOOOLLLLLLAAAAAAAAAAAAAA!!!!"
    }

    return render(request, 'actividadfinal.html', contenido)
    
def localidad (request,id):
    print(id)
    ciudad = Ciudad.objects.get(id=id)
    print(ciudad)
    contexto = {"ciudad":ciudad}
    return render(request, 'ciudadfinal.html', contexto)    
