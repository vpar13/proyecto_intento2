"""
URL configuration for taller project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Mecanico import views
from Secretaria import views as secretaria_views


urlpatterns = [

    # mecanico views
    path('', views.mecanico, name='mecanico'),

    # secretaria views
    path('crearCli/', secretaria_views.CrearCli, name='CrearCli'),  
    path('GestionarC/', secretaria_views.GestionarC, name='GestionarC'),  
    path('crearV/', secretaria_views.CrearV, name='CrearV'),
    path('gestionarV/', secretaria_views.GestionarV, name='GestionarV'),    
    path('crearR/', secretaria_views.CrearR, name='CrearR'),
    path('crearOT/', secretaria_views.CrearOT, name='CrearOT'),
    path('GestionarOT/', secretaria_views.GestionarOT, name='GestionarOT'),

    # admin views
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)