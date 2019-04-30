from django.shortcuts import render
from django.http import HttpResponse
from .models import Ciudad
from .models import Guia
# Create your views here.


def salida(request):
    despedida = Ciudad.objects.all()
    despe = Guia.objects.all()
    #return HttpResponse(despedida)
    return render(request,"index.html",{"ciudades":despedida, "guias":despe })