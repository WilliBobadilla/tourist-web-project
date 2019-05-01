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
    contexto = {"ciudad":ciudad}
    return render(request, 'guiafinal.html', contexto)

def perfil_guia (request,id):
    print(id)
    guia = Guia.objects.get(id=id)
    actividades = Actividad.objects.filter(guia=guia)
    print(guia)
    #return HttpResponse(guia)
    contexto = {"guia":guia,"actividades":actividades}
    return render(request, 'guiafinal.html', contexto)


def detalle_actividad(request,id_tipo,id_ciudad):
    print(id)
    #Obtener actividad solicitada
    guia=Guia.objects.filter(ciudad=id_ciudad)
    lista_actividades = Actividad.objects.filter(tipo=id_tipo)
    lista_final=[]
    for acti in lista_actividades:
        if acti.guia in guia:
            lista_final.append(acti.guia)
    contexto = {"guias":lista_final}
    print(lista_final)

    return render(request,'actividadfinal.html', contexto)

# funcion para que aparezca plantilla actividad final
def acti_final(request,id):

    contenido = {
        "guias":Guia.objects.filter(ciudad=id),
    }

    return render(request, 'actividadfinal.html', contenido)
    
def localidad (request,id):
    print(id)
    ciudad = Ciudad.objects.get(id=id)
    print(ciudad)
    contexto = {"ciudad":ciudad}
    return render(request, 'ciudadfinal.html', contexto)    
