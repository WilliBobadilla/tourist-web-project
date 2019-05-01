"""turismo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from guiatour import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index), #Index de la pagina, mostrar 3 ciudades
    path('ciudad/<int:id>/', views.localidad),#Ciudad , se debe ver las categorias de actividades
    path('actividad/<int:id>/', views.acti_final),#ListaGuias, me muestra los guias de un ciudad elegida
    path('guia/<int:id>/', views.perfil_guia),#Perfil Guia muestra, el perfil del guia
    path('activida/<int:id_tipo>/<int:id_ciudad>/', views.detalle_actividad),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
