from django.shortcuts import render

# Create your views here.

def CrearCli (request):
    return render(request, 'Secretaria/crearCli.html')

def GestionarC (request):
    return render(request, 'Secretaria/GestionarC.html')

def CrearV (request):
    return render(request, 'Secretaria/crearV.html')

def GestionarV (request):
    return render(request, 'Secretaria/gestionarV.html')

def CrearR (request):
    return render(request, 'Secretaria/CrearReparaciones.html')

def CrearOT (request):
    return render(request, 'Secretaria/CrearOT.html')

def GestionarOT (request):
    return render(request, 'Secretaria/GestionarOT.html')